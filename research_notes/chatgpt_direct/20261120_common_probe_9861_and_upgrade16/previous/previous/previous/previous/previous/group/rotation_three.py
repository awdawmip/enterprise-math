"""Exclude every choice of three classes from a single four-cycle of the witness rotation."""
from pathlib import Path
import json, subprocess, tempfile
from generate import main as generate
from packet_floor import make
from replay import solve
HERE=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory() as tmp:
    work=Path(tmp)
    generate(work)
    exe=work/'residual'
    subprocess.run(['c++','-O3','-mpopcnt','-std=c++17',str(HERE/'one.cpp'),'-o',str(exe)],check=True)
    make(work,3)
    (work/'neighbor3_rot').replace(work/'neighbor3')
    n=len((work/'neighbor3').read_text().splitlines())
    print(json.dumps(solve(exe,work,range(n),['8727','3','rot']),sort_keys=True))
