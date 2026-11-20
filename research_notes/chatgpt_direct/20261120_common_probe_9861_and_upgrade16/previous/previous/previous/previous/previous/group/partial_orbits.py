"""Enumerate partial translation orbits of equally shaped cheap classes modulo affine maps."""
from itertools import combinations
from pathlib import Path
import sys
from generate import maps,profiles
from single_orbit import bits

def make(work,length,upper):
    lin,trans,gs=maps()
    with (work/'bank').open()as f:
        rows={}
        for _ in range(int(next(f))):
            s,c,n=map(int,next(f).split())
            rows[s,c]={(lo|hi<<64)for lo,hi in (map(int,next(f).split())for _ in range(n))}
    ts=list(rows);prof=profiles(ts,upper);collect=[]
    for k,key in enumerate(ts):
        if not any(cnt[k]>=length for c,cnt in prof):continue
        bank=set(rows[key])
        while bank:
            seed=min(bank);pts=list(bits(seed))
            transforms={tuple(sorted(a[i]for i in pts))for a in lin}
            orbit={sum(1<<t[i]for i in q)for t in trans for q in transforms}
            assert orbit<=bank
            bank-=orbit
            trmap=[[1<<i for i in t]for t in trans]
            orbit_keys=set()
            # The full group orbit allows the first class of the selected run to be fixed at seed.
            # All directions and choices of the other steps are then considered.
            for t in trans[1:]:
                pow=[seed]
                for _ in range(4):pow.append(sum(1<<t[i]for i in bits(pow[-1])))
                if len(set(pow))!=5:continue
                for ix in combinations(range(1,5),length-1):
                    parts=[seed]+[pow[i]for i in ix]
                    used=0
                    for v in parts:
                        if used&v:break
                        used|=v
                    else:
                        if used in orbit_keys:continue
                        # Re-anchor any selected row at the representative seed, up to a linear action.
                        variants=set()
                        for m in parts:
                            row=list(bits(m));start=pts[0]
                            for a in lin:
                                rot=[a[x]for x in row]
                                for x in rot:
                                    shift=25*((start//25-x//25)%5)+5*((start//5%5-x//5%5)%5)+((start%5-x%5)%5)
                                    h=trmap[shift]
                                    if sum(h[i]for i in rot)==seed:
                                        variants.add(sum(h[a[j]]for j in bits(used)))
                        assert used in variants
                        orbit_keys.update(variants)
                        collect.append((k,used,parts))
    with (work/f'partial{length}').open('w')as f:
        for k,u,parts in collect:
            print(k,u%(1<<64),u>>64,*[z for m in parts for z in (m%(1<<64),m>>64)],file=f)
    return len(collect)
if __name__=='__main__':print(make(Path(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])),flush=True)
