"""Recompute four-coordinate finite evidence and compare to the archived results."""
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent

def check_script(pair):
    program,expected=pair
    output=subprocess.check_output([sys.executable,'-B',str(ROOT/program)],text=True)
    assert json.loads(output)==json.loads((ROOT/expected).read_text()),program
    print('PASS',program,flush=True)

def verify():
    with ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(check_script,(('check.py','result.json'),('exchanges.py','exchanges.json'),('rank_two.py','rank_two.json'))))
    with tempfile.TemporaryDirectory()as scratch:
        exe=Path(scratch)/'two'
        subprocess.run(['c++','-O3','-std=c++17',str(ROOT/'two_templates.cpp'),'-o',str(exe)],check=True)
        templates=json.loads((ROOT/'certificate.json').read_text())['templates']
        data=''.join(' '.join(map(str,row))+'\n'for row in templates)
        out=subprocess.check_output([str(exe)],input=data,text=True)
        assert json.loads(out)==json.loads((ROOT/'two_templates.json').read_text())
        print('PASS two_templates.cpp')

if __name__=='__main__':
    verify()
