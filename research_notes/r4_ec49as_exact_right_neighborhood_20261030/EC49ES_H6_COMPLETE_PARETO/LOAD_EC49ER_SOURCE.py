#!/usr/bin/env python3
"""Recover the exact already published EC49ER implementation from its versioned archive."""
from pathlib import Path
import hashlib,base64,tarfile,io
here=Path(__file__).resolve().parent
src=here.parent/'EC49ER_H6_LOW_CACHE_EXACT'/'EC49ER_COMPLETE_EVIDENCE.tar.gz.b64'
b=base64.b64decode(src.read_text(encoding='ascii'))
digest=hashlib.sha256(b).hexdigest()
assert digest=='bee8a4768604ef74a2d0261524b8ad901ef5b9362251b17ab462e7cc3cd7665a',digest
wanted={'VERIFY_EC49ER.py','VERIFY_EC49ER_M3_MILP.py','EC49ER_EXECUTED.json','EC49ER_ALL_M3_EXECUTED.json'}
with tarfile.open(fileobj=io.BytesIO(b),mode='r:gz') as tf:
  for name in wanted:
    f=tf.extractfile(name);assert f is not None,name
    dest=here/name
    content=f.read()
    if dest.exists():assert dest.read_bytes()==content,('conflicting reused parent file',dest)
    else:dest.write_bytes(content)
    print('VERIFIED',name,len(content))
print('PARENT_EC49ER_SOURCE_SHA256',digest)
