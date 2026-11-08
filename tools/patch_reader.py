"""Read the pinned unified diff without applying it to the user's checkout."""
from __future__ import annotations
import hashlib
import re
from pathlib import Path, PurePosixPath

def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def sections(patch: Path) -> list[dict]:
    text = patch.read_text(encoding="utf-8")
    result = []
    for block in re.split(r"(?=^diff --git )", text, flags=re.M):
        if not block.startswith("diff --git "):
            if block.strip(): raise ValueError("Unexpected patch preamble")
            continue
        match = re.search(r"^\+\+\+ b/(.+)$", block, re.M)
        hashes = re.search(r"^index ([a-f0-9]{40})\.\.([a-f0-9]{40})", block, re.M)
        if not match or not hashes: raise ValueError("Unsupported patch format")
        path = PurePosixPath(match.group(1))
        if path.is_absolute() or '..' in path.parts or '\\' in str(path) or path.parts[0] != 'src':
            raise ValueError(f"Unsafe/unexpected path: {path}")
        if any(r['path'] == str(path) for r in result): raise ValueError("Duplicate diff path")
        new_file = 'new file mode 100644\n' in block
        added = [l[1:] for l in block.splitlines() if l.startswith('+') and not l.startswith('+++')]
        payload = ('\n'.join(added) + '\n').encode() if new_file else None
        if payload is not None and git_blob(payload) != hashes.group(2):
            raise ValueError(f"New-file blob hash mismatch: {path}")
        result.append({'path':str(path),'base_blob':hashes.group(1),'target_blob':hashes.group(2),
                       'new_file':new_file,'payload':payload,'block':block})
    if not result: raise ValueError("No diff sections")
    return result

def extract_new_headers(patch: Path, destination: Path) -> list[str]:
    paths=[]
    for r in sections(patch):
        if r['new_file']:
            path=destination/r['path']; path.parent.mkdir(parents=True,exist_ok=True)
            path.write_bytes(r['payload']);paths.append(r['path'])
    return paths
