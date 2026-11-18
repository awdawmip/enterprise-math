"""Cross-check both sweeps by uncompressed all-phase enumeration, including ties."""
from collections import Counter
from pathlib import Path
from random import Random
import subprocess

BASE=Path(__file__).resolve().parent
def call(name,header,rows,flags=()):
    inp=" ".join(map(str,header))+"\n"+"".join(" ".join(map(str,r))+"\n" for r in rows)
    return list(map(int,subprocess.check_output([str(BASE/name),*flags],input=inp,text=True).split()))

def check(pts,q):
    n=len(pts)
    cells=[Counter(((x+a)//q,(y+b)//q) for x,y in pts)
           for a in range(q) for b in range(q)]
    cnt=[sum(v==1 for v in c.values()) for c in cells]
    h=sum(all(i==j or max(abs(x-z),abs(y-w))>=q for j,(z,w) in enumerate(pts))
          for i,(x,y) in enumerate(pts))
    wanted=(sum(cnt),sum(map(len,cells)),sum(sum(v==2 for v in c.values()) for c in cells),h,h)
    assert tuple(call("sweep",(n,q,0),pts))==wanted
    # All q equally long y intervals, even when a breakpoint is unused.
    data=[(x//q,y//q,q-x%q,q-y%q) for x,y in pts]
    assert call("extrema",(n,q,q),data)==[min(cnt),max(cnt)]
    expanded=[list(range(q+1)),list(range(q+1)),*data]
    assert call("extrema",(n,q,q),expanded,("--moments",))==[min(cnt),max(cnt),sum(cnt),sum(v*v for v in cnt)]

if __name__=="__main__":
    rng=Random(794012)
    for pts in [[(0,0)],[(0,0)]*5,[(0,0),(8,8)],[(0,0),(4,4),(4,4),(8,8)],[(7,1),(8,1),(16,1)]]:
        check(pts,8)
    for _ in range(80):
        q=rng.choice((4,6,8,10))
        pts=[(rng.randrange(6*q),rng.randrange(6*q)) for _ in range(rng.randrange(1,45))]
        check(pts,q)
    print("85 all-phase comparisons verified for both sweeps, first and second moments, and robust isolation.")
