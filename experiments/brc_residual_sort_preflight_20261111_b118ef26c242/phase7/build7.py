"""Compile phase 7 using the frozen phase-5 driver and previously pinned sources."""
import argparse
import hashlib
from pathlib import Path
import subprocess
import sys

p=argparse.ArgumentParser(description=__doc__)
p.add_argument("source_root",type=Path)
args=p.parse_args()
here=Path(__file__).resolve().parent
five=here.parent/"phase5"
build=here/"build"
build.mkdir(exist_ok=True)
src=(five/"bench.cpp").read_bytes()
assert hashlib.sha256(src).hexdigest()=="bfa11e51556e2634af463ac5a8dfcbf94c7b8b9c09b7ee2d0aaa1ee218a54b58"
signature=b"int main(int argc,char** argv)"
assert src.count(signature)==1
(build/"bench5_frozen.hpp").write_bytes(src.replace(signature,b"int phase5_frozen_entry(int argc,char** argv)"))
subprocess.run([sys.executable,str(five/"build.py"),str(args.source_root.resolve()),
                "--unit",str(here/"bench7.cpp"),"--output",str(build/"bench7")],check=True)
