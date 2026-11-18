"""Check each labeled source against direct cell sweeps on integer toy inputs."""
from collections import Counter
from pathlib import Path
from random import Random
import subprocess
EXE=Path(__file__).resolve().parent/'individual'

def check(points,h):
    xs=sorted({x+u for x,y in points for u in (0,h)})
    ys=sorted({y+u for x,y in points for u in (0,h)})
    xrank={v:k for k,v in enumerate(xs)}; yrank={v:k for k,v in enumerate(ys)}
    data=[f'{len(points)} {len(xs)} {len(ys)}',' '.join(map(str,xs)),' '.join(map(str,ys))]
    data.extend(f'{xrank[x]} {xrank[x+h]} {yrank[y]} {yrank[y+h]}' for x,y in points)
    out=subprocess.check_output([str(EXE)],input='\n'.join(data)+'\n',text=True)
    result=[tuple(map(int,row.split())) for row in out.splitlines()]
    area=[0]*len(points)
    for u in range(h):
        for v in range(h):
            cells=[((x+u)//h,(y+v)//h) for x,y in points]
            counts=Counter(cells)
            for i,cell in enumerate(cells): area[i]+=counts[cell]==1
    for a,row in zip(area,result):
        assert row[:3]==(a,int(a>0),int(a==h*h)),(points,a,row)
    return sum(area)

if __name__=='__main__':
    rng=Random(20261119)
    cases=[([(0,0)],4), ([(0,0),(0,0),(4,0),(0,4)],4), ([(0,0),(4,0),(-4,0),(0,4),(0,-4)],4)]
    for _ in range(200):
        h=rng.randrange(1,11); n=rng.randrange(1,35)
        cases.append(([(rng.randrange(-12,13),rng.randrange(-12,13)) for k in range(n)],h))
    print('direct checks',len(cases),'labeled templates',sum(len(points) for points,h in cases),
          'successful template-phase instances',sum(check(points,h) for points,h in cases))
