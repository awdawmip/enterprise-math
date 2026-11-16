"""Verify the base single-class lower bounds from the actual 250 public menus."""
from pathlib import Path
import sys
import tempfile
import subprocess

ROOT = Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'bounds'))
from prior_bounds import observation_file
from verify import MINIMA

def run():
    with tempfile.TemporaryDirectory() as tmp:
        folder=Path(tmp)
        observation_file(folder/'observations.bin')
        exe=folder/'class_minima'
        subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(ROOT/'class_minima.cpp'),'-o',str(exe)],check=True)
        raw=subprocess.check_output([str(exe),str(folder/'observations.bin'),str(folder/'seeds')],text=True)
        costs={int(v[0]):int(v[2]) for line in raw.splitlines() if (v:=line.split())}
        assert costs=={k:MINIMA[k] for k in range(2,14)}
        print('PASS single-class minima on the common-action service', costs)

if __name__=='__main__':
    run()
