"""Rebuild the translation-only exclusion from the native menus and size/cost census."""
from pathlib import Path
import tempfile,subprocess,json,sys
from generate import BASE,observation_file
from translation import solve
HERE=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory()as tmp:
    work=Path(tmp)
    observation_file(work/'obs')
    exe=work/'enum'
    subprocess.run(['c++','-O3','-mpopcnt','-std=c++17',str(HERE.parent/'low/class_enumeration.cpp'),'-o',str(exe)],check=True)
    subprocess.run([str(exe),str(work/'obs'),str(work/'lowseeds')],stdout=subprocess.DEVNULL,check=True)
    target=json.loads((HERE/'translation.json').read_text())
    print(json.dumps({k:[cap,solve(work,cap,int(k))] for k,(cap,_) in target.items()},sort_keys=True))
