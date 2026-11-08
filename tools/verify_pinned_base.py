#!/usr/bin/env python3
"""Check the exported patch against Git objects in an existing PX4 repository.
Reads only from that repository. Does not modify its source/index/HEAD, rebuild,
flash, add tags, or publish. All patch application occurs in a temporary folder.
"""
from __future__ import annotations
import argparse,hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from patch_reader import sections,git_blob
ROOT=Path(__file__).resolve().parents[1]

def git(repo: Path,*args: str) -> bytes:
    env=os.environ.copy()
    for key in list(env):
        if key.startswith('GIT_'):env.pop(key)
    env.update({'GIT_OPTIONAL_LOCKS':'0','GIT_TERMINAL_PROMPT':'0','GIT_PAGER':'cat'})
    p=subprocess.run(['git','--no-optional-locks','-C',str(repo),*args],env=env,
                     stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if p.returncode:
        raise RuntimeError(p.stderr.decode(errors='replace').strip() or 'Git command failed')
    return p.stdout

def check(repo: Path,patch: Path,base: str,expected_sha: str) -> dict:
    if hashlib.sha256(patch.read_bytes()).hexdigest()!=expected_sha:
        raise ValueError('Patch checksum differs from frozen review manifest')
    actual=git(repo,'rev-parse','--verify',base+'^{commit}').decode().strip()
    if actual!=base:raise ValueError('Base revision did not resolve to expected full commit')
    rows=sections(patch)
    with tempfile.TemporaryDirectory(prefix='dragonfly-base-check-') as td:
        dest=Path(td)
        for r in rows:
            if r['new_file']:
                # It must truly be absent at the pinned base.
                try:git(repo,'cat-file','-e',base+':'+r['path'])
                except RuntimeError:pass
                else:raise ValueError('New-file path already exists at base: '+r['path'])
                continue
            data=git(repo,'show',base+':'+r['path'])
            if git_blob(data)!=r['base_blob']:raise ValueError('Base blob mismatch: '+r['path'])
            p=dest/r['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
        git(dest,'apply','--check','--whitespace=nowarn',str(patch.resolve()))
        git(dest,'apply','--whitespace=nowarn',str(patch.resolve()))
        for r in rows:
            if git_blob((dest/r['path']).read_bytes())!=r['target_blob']:
                raise ValueError('Applied target blob mismatch: '+r['path'])
    return {'base_commit':base,'patch_sha256':expected_sha,'verified_paths':len(rows),
            'base_blobs_and_applied_target_blobs':'PASS','build_performed':False,
            'hardware_test_performed':False,'source_repo_modified':False}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('px4_repository',type=Path)
    args=ap.parse_args()
    m=json.loads((ROOT/'evidence/PATCH_MANIFEST.json').read_text())
    r=check(args.px4_repository.resolve(),ROOT/m['patch'],m['base_commit_reported'],m['patch_sha256'])
    print('PASS: pinned base, clean temporary patch application and all target blobs match')
    print(json.dumps(r,indent=2))
    print('No build, flash, parameter write, source/index update or publication.')
if __name__=='__main__':
    try:main()
    except (OSError,ValueError,RuntimeError) as e:raise SystemExit('STOP: '+str(e))
