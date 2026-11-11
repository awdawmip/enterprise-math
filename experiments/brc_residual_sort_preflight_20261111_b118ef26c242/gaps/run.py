"""Reproduce the exact residual diagnostic using the phase-five reference root."""
import argparse
import hashlib
from pathlib import Path
import subprocess
import sys

here = Path(__file__).resolve().parent
driver = here.parent/'phase5'
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('prior_source_root',type=Path)
args = p.parse_args()
build = here/'build'
build.mkdir(exist_ok=True)
src = (driver/'bench.cpp').read_bytes()
assert hashlib.sha256(src).hexdigest()=='bfa11e51556e2634af463ac5a8dfcbf94c7b8b9c09b7ee2d0aaa1ee218a54b58'
entry=b'int main(int argc,char** argv)'
assert src.count(entry)==1
(build/'frozen_phase5.hpp').write_bytes(src.replace(entry,b'int phase5_offline_entry(int argc,char** argv)'))
binary=build/'residual_gaps'
subprocess.run([sys.executable,str(driver/'build.py'),str(args.prior_source_root.resolve()),
                '--unit',str(here/'residual_gaps.cpp'),'--output',str(binary)],check=True)
subprocess.run([str(binary),str(here)],check=True)
subprocess.run([sys.executable,str(here/'summarize.py')],check=True)
