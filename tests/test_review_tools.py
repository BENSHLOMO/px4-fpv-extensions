"""Synthetic tests of packaging/verifier mechanics, not PX4 correctness."""
import hashlib,os,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
from verify_pinned_base import check
from patch_reader import sections

def run(repo,*args):
    return subprocess.check_output(['git','-C',str(repo),*args],stderr=subprocess.STDOUT)
class ReviewTools(unittest.TestCase):
    def test_apply_roundtrip_preserves_checkout_index_and_head(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td);repo=d/'repo';repo.mkdir();run(repo,'init','-q')
            run(repo,'config','user.name','Test Fixture');run(repo,'config','user.email','fixture@invalid.local')
            p=repo/'src/example.cpp';p.parent.mkdir();p.write_text('old\n')
            run(repo,'add','.');run(repo,'commit','-qm','base');base=run(repo,'rev-parse','HEAD').decode().strip()
            p.write_text('new\n');q=repo/'src/helper.hpp';q.write_text('#pragma once\n')
            run(repo,'add','.')
            diff=run(repo,'diff','--cached','--full-index',base);patch=d/'change.patch';patch.write_bytes(diff)
            sha=hashlib.sha256(diff).hexdigest();before=(repo/'.git/index').read_bytes()
            result=check(repo,patch,base,sha)
            self.assertEqual(result['verified_paths'],2)
            self.assertEqual(before,(repo/'.git/index').read_bytes())
            self.assertEqual(run(repo,'rev-parse','HEAD').decode().strip(),base)
            self.assertEqual(p.read_text(),'new\n');self.assertEqual(q.read_text(),'#pragma once\n')
            with self.assertRaises(ValueError):check(repo,patch,base,'0'*64)
    def test_unsafe_path_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'bad.patch'
            p.write_text('diff --git a/../../bad b/../../bad\nindex '+'1'*40+'..'+'2'*40+'\n--- a/../../bad\n+++ b/../../bad\n@@ -1 +1 @@\n-a\n+b\n')
            with self.assertRaises(ValueError):sections(p)
if __name__=='__main__':unittest.main(verbosity=2)
