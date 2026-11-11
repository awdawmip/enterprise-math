"""Validate forward and reverse enclosure on exact two-endpoint path controls."""
from argparse import ArgumentParser
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
from extend_region import header

if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--last',type=int,default=32)
    a=p.parse_args()
    cases=[(r,c) for c in range(3,a.last+1) for r in range(2,c-1)]
    data=header(a.last,3)+''.join(f'{r} {c}\n' for r,c in cases)
    with TemporaryDirectory() as d:
        e=Path(d)/'clip'
        subprocess.run(['g++','-O3','-std=c++17',str(Path(__file__).with_name('region_search.cpp')),'-lgmpxx','-lgmp','-o',str(e)],check=True)
        out=subprocess.run([str(e),'--controls'],input=data,text=True,check=True,capture_output=True).stdout
    rows=[tuple(map(int,x.split())) for x in out.splitlines()]
    assert [(r,c) for r,c,n in rows]==cases and all(n==18*r for r,c,n in rows)
    print(json.dumps(dict(last_stock=a.last,verified_stocks=len(rows),control_paths=9*len(rows),
                          exact_endpoint_clips=sum(n for _,_,n in rows)),indent=2))
