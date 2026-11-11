"""Exact fixed-probe design envelope for singleton preferences. Standard library."""
import argparse,json
from pathlib import Path
from functools import cache
from itertools import combinations
def ceiling(N):return (N-1).bit_length()
def count(d,h):
    j=min(d,h);return (1<<j)*(1+d-j)
def exact(n,h,s=0):
    d=0
    while (1<<s)*count(d,h)<n:
        d+=1
    return d
def run():
    # Enumerate every extra nonconstant, nonduplicate query, up to complement.
    rows=[]
    for n in range(2,9):
        full=(1<<n)-1
        eq=tuple(1<<i for i in range(1,n))
        nontrivial=tuple(j for j in range(2,full,2) if j not in eq)
        for h in range(3):
            best=n-1;tested=0
            for a in range(min(h,len(nontrivial))+1):
                for combo in combinations(nontrivial,a):
                    tested+=1
                    @cache
                    def f(U):
                        if U.bit_count()<2:return 0
                        return 1+min(max(f(U&m),f(U&~m))for m in eq+combo if U&m and U&~m)
                    best=min(best,f(full))
            assert best==exact(n,h);rows.append([n,h,best,tested])
    grid=0
    for d in range(1,21):
        for h in range(21):
            a=1+count(d-1,h)
            b=0 if h==0 else 2*count(d-1,h-1)
            assert count(d,h)==max(a,b);grid+=1
    return dict(status='PASS',enumerated=rows,designs=sum(r[-1] for r in rows),capacity_grid=grid,
                examples={n:[exact(n,h) for h in range(6)] for n in (5,8,16,32)})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).with_name('capacity_results.json'));a=p.parse_args()
    out=run();a.out.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print('capacity ok',out['designs'])
