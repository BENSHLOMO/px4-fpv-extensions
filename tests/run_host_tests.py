#!/usr/bin/env python3
"""Test actual new headers extracted from the immutable exported patch.
No PX4 build, target scheduling, installed firmware or ESC test is performed.
"""
import hashlib,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from patch_reader import extract_new_headers

def main():
    manifest=json.loads((ROOT/'evidence/PATCH_MANIFEST.json').read_text())
    patch=ROOT/manifest['patch']
    if hashlib.sha256(patch.read_bytes()).hexdigest()!=manifest['patch_sha256']:
        raise SystemExit('STOP: snapshot patch checksum mismatch')
    compiler=os.environ.get('CXX','g++')
    if not shutil.which(compiler):raise SystemExit('STOP: g++/CXX compiler not found')
    with tempfile.TemporaryDirectory(prefix='dragonfly-review-tests-') as td:
        work=Path(td)
        paths=extract_new_headers(patch,work)
        print(f'PASS: {len(paths)} new-file Git blob hashes verified',flush=True)
        for name,extra in [('rc',[]),('core',[]),('fault_matrix',[]),('mapping',[]),('interlock',['interlock_other.cpp'])]:
            exe=work/name
            cmd=[compiler,'-std=c++14','-O2','-Wall','-Wextra','-Werror',
                 '-fsanitize=undefined','-fno-sanitize-recover=all','-pthread',
                 '-I'+str(work/'src/drivers/dshot'),'-I'+str(work/'src'),
                 str(ROOT/'tests'/('test_'+name+'.cpp'))]
            cmd += [str(ROOT/'tests'/p) for p in extra]+['-o',str(exe)]
            subprocess.run(cmd,check=True)
            subprocess.run([str(exe)],check=True)
    print('PASS: all 5 host suites against exact exported new headers; not a full PX4 build')
if __name__=='__main__':main()
