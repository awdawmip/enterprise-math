"""Exact-cost search below an incumbent, for partitions invariant under a nonzero translation."""
from collections import defaultdict
from itertools import combinations,product
from pathlib import Path
import json,sys
from generate import BASE,maps
from single_orbit import bits
sys.path.insert(0,str(BASE/'bounds'))
sys.path.insert(0,str(BASE/'curve'))
from cyclic11 import observations,class_cost
from verify import MINIMA,lower
POINTS=list(product(range(5), repeat=3))
DIRECTIONS=[(0,0,1),(0,1,1),(0,1,2),(1,1,1),(1,1,2)]
def ix(p):return 25*(p[0]%5)+5*(p[1]%5)+p[2]%5
def shift(i,d,t):return ix(tuple(a+t*b for a,b in zip(POINTS[i],d)))
def lower_bound(n,k):
    if n<0 or k<0:return 10**9
    return lower(n,k)
def solve(work,maxcost,labels):
    bad,obs=observations()
    def price(group):return None if any(bad[a][b]>>c&1 for a,b,c in combinations(group,3)) else class_cost(group,obs)
    linear,_,_=maps()
    limits={8:550,9:740,10:880,11:1090,12:1230,13:1350}
    canonical=defaultdict(dict)
    for line in (work/'lowseeds').read_text().splitlines():
        s,c,*q=map(int,line.split())
        canonical[s].setdefault(tuple(q),c)
    all_results=[]
    for direction in DIRECTIONS:
        lines=sorted({tuple(sorted(shift(i,direction,t)for t in range(5)))for i in range(125)})
        lineid={v:i for i,line in enumerate(lines)for v in line}
        fixed=[(1<<i,price(line),line)for i,line in enumerate(lines)]
        for a,b in combinations(range(25),2):
            line=lines[a]+lines[b];v=price(line)
            if v is not None:fixed.append((1<<a|1<<b,v,line))
        minfixed=[min((p for m,p,_ in fixed if m.bit_count()==k),default=10**9)for k in (1,2)]
        options=[];needs={}
        for a in range(labels+1):
            for b in range(labels-a+1):
                left=labels-a-b; n=25-a-2*b
                if left%5 or n<0:continue
                k=left//5;fc=a*minfixed[0]+b*minfixed[1]
                if fc+5*lower_bound(n,k)>maxcost:continue
                options.append((a,b,k,n))
                for s in range(1,14):
                    cap=(maxcost-fc)//5-lower_bound(n-s,k-1)
                    if cap>=MINIMA[s]:needs[s]=max(needs.get(s,0),cap)
        # For this problem every case capable of beating the reference has two
        # nonconstant orbits. Include one-orbit and zero-orbit cases explicitly if needed.
        if any(k!=2 for a,b,k,n in options):raise ValueError((direction,options))
        for s,cap in needs.items():assert s in limits and cap<=limits[s] or s==13 and cap>=1296,(s,cap)
        # All 13-point classes (from the census) cost 1296.
        seeds={}
        for s,cap in sorted(needs.items()):
            # Quotient supports are invariant under translation along direction;
            # enumerate 25 remaining translations explicitly.
            reps=[l[0] for l in lines]
            best={}
            done=set()
            for pts,c in sorted(canonical[s].items(),key=lambda kv:kv[1]):
                if c>cap:break
                if pts in done:continue
                oriented={tuple(sorted(g[i]for i in pts))for g in linear}
                for pp in oriented:
                    for j in pp:
                        delta=tuple(-v for v in POINTS[j]);done.add(tuple(sorted(shift(i,delta,1)for i in pp)))
                    if len({lineid[i]for i in pp})<s:continue
                    for j in reps:
                        shifted=tuple(shift(i,POINTS[j],1)for i in pp)
                        support=sum(1<<lineid[i]for i in shifted)
                        if support not in best:best[support]=(c,shifted)
            seeds[s]=best
        # Enumerate sets of the required number of disjoint invariant components,
        # keeping the cheapest realizing partition of a given fixed support.
        top=maxcost+1;witness=None;fixed_cases=0
        for a,b,k,n in options:
            bymask={}
            for singles in combinations((r for r in fixed if r[0].bit_count()==1),a):
                for pairs in combinations((r for r in fixed if r[0].bit_count()==2),b):
                    selected=singles+pairs;sup=0;fc=0
                    for m,c,row in selected:
                        if sup&m:break
                        sup|=m;fc+=c
                    else:
                        if fc+5*lower(n,k)<=maxcost and (sup not in bymask or fc<bymask[sup][0]):
                            bymask[sup]=(fc,[r[2]for r in selected])
            fixed_cases+=len(bymask)
            def consider(fixed_rows,fc,c,r,v):
                nonlocal top,witness
                cc=fc+5*(c+v[0])
                if cc<top:
                    top=cc
                    witness=fixed_rows+[[shift(i,direction,t)for i in row]for row in (r,v[1])for t in range(5)]
            for s in seeds:
                if n-s<s or n-s not in seeds:continue
                left,right=seeds[s],seeds[n-s]
                if len(right)<len(bymask):
                    for u,(c,r) in left.items():
                        for v,other in right.items():
                            if u&v:continue
                            f=bymask.get(((1<<25)-1)^u^v)
                            if f:consider(f[1],f[0],c,r,other)
                else:
                    for sup,(fc,fixed_rows) in bymask.items():
                        free=((1<<25)-1)^sup
                        for u,(c,r) in left.items():
                            if u&sup:continue
                            v=right.get(free^u)
                            if v:consider(fixed_rows,fc,c,r,v)
        all_results.append(dict(direction=direction,options=options,needs=needs,fixed_cases=fixed_cases,attained=top if witness else None))
        if witness:
            assert sorted(i for row in witness for i in row)==list(range(125))
            assert len(witness)==labels and sum(price(row)for row in witness)==top
            (work/f'translation{labels}_{top}.json').write_text(json.dumps(witness))
    return all_results
if __name__=='__main__':print(json.dumps(solve(Path(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])),sort_keys=True))
