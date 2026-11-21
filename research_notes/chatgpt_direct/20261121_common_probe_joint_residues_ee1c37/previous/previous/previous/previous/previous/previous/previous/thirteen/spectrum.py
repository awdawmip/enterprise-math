"""Generate every possible total cost between the global floor and the witnessed cap."""
from functools import cache
import json
from pathlib import Path
import subprocess
import sys
import tempfile

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(BASE/'curve'))
sys.path.insert(0,str(BASE/'bounds'))
from prior_bounds import observation_file
from verify import MINIMA, lower

def spectrum():
    upper = json.loads((BASE/'curve/open_witnesses.json').read_text())['13']['cost']
    prices = {s:set() for s in range(9,14)}
    assert all(MINIMA[s]+lower(125-s,12)>upper for s in range(1,9))
    # Recording ceilings compiled in curve/class_minima.cpp; check that each covers
    # every candidate price that could appear under the budget.
    limits = {9:587,10:780,11:965,12:1140,13:1350}
    assert all(limits[s]+1+lower(125-s,12)>upper for s in prices)
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        observation_file(work/'menus')
        exe=work/'classes'
        subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(BASE/'curve/class_minima.cpp'),'-o',str(exe)],check=True)
        subprocess.run([str(exe),str(work/'menus'),str(work/'seeds')],stdout=subprocess.DEVNULL,check=True)
        for line in (work/'seeds').read_text().splitlines():
            size,cost,_ = line.split(' ',2)
            size,cost = int(size),int(cost)
            if size in prices and cost+lower(125-size,12)<=upper:
                prices[size].add(cost)
    @cache
    def remaining(n,k,budget):
        if k==0:
            return {0} if n==0 else set()
        values=set()
        for s,costs in prices.items():
            if s>n:continue
            for cost in costs:
                if cost+lower(n-s,k-1)<=budget:
                    values.update(cost+v for v in remaining(n-s,k-1,budget-cost))
        return values
    return sorted(remaining(125,13,upper))

if __name__=='__main__':
    print(json.dumps(spectrum()))
