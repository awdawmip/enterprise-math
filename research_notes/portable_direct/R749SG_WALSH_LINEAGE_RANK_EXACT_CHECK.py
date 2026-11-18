#!/usr/bin/env python3
"""Exact, finite signed-Port graph check of lineage/Walsh rank for R749SG."""
from collections import defaultdict, Counter
from itertools import combinations
import json

ports=[(i,s) for i in range(6) for s in (-1,1)]
V=[frozenset(z) for z in combinations(ports,2) if z[0][0]!=z[1][0]]
sup=lambda v:frozenset(a for a,s in v)
adj=lambda u,v:len(u&v)==1 and len(sup(u)|sup(v))==3
nbr={v:[w for w in V if adj(v,w)] for v in V}
E=[(u,v) for u in V for v in nbr[u]]
L=defaultdict(list)
for e in E:L[(sup(e[0]),sup(e[1]))].append(e)
assert len(V)==60 and len(E)==960 and len(L)==120
assert all(len(z)==8 for z in L.values())

unbr={B:sorted({sup(w) for v in V if sup(v)==B for w in nbr[v]},key=lambda z:tuple(sorted(z))) for A,B in L}
assert all(len(v)==8 for v in unbr.values())
sgn={e:dict(e[0]|e[1]) for e in E}
trans={}
for (A,B),starts in L.items():
    for C in unbr[B]:
        ends=L[(B,C)]
        isforced=C==(A^B)
        for p in (0,1,2): # 0: p=0; 1: p=1/2; 2: p=1
            if p==2 and not isforced:continue
            d=18 if p==1 and isforced else (1 if p==2 else 2)
            M=[]
            for (u,v) in starts:
                f=u^v
                row=[]
                for (vv,w) in ends:
                    if vv!=v:row.append(0)
                    elif p==2:row.append(int(w==f))
                    elif isforced and p==1:row.append(17 if w==f else 1)
                    else:row.append(1)
                assert sum(row)==d
                M.append(row)
            trans[(A,B,C,p)]=(d,M)

def mul(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(8)) for j in range(8)] for i in range(8)]

def lineage(A,B,path,p):
    h={a:(a,0) for a in A|B};x,y=A,B
    for z in path:
        if z==x^y:
            a=next(iter(x-y));o=h[a]
            if o is not None:
                h[a]=None if p==0 else (o[0],o[1]+1)
        else:
            old=next(iter(x-y));new=next(iter(z-y))
            del h[old];h[new]=None
        x,y=y,z
    return h

def check(A,B,path,p):
    initial=L[(A,B)];x,y=A,B
    D=1;M=[[int(i==j) for j in range(8)] for i in range(8)]
    for C in path:
        d,N=trans[(x,y,C,p)]
        M=mul(M,N);D*=d;x,y=y,C
    final=L[(x,y)]
    h=lineage(A,B,path,p)
    axes=tuple(sorted(x|y))
    assert set(axes)==set(h)
    for mask in range(8):
        subset=[axes[i] for i in range(3) if (mask>>i)&1]
        if any(h[a] is None for a in subset):
            target=[0]*8;factor_denom=1
        else:
            src=[h[a][0] for a in subset]
            k=sum(h[a][1] for a in subset)
            assert len(src)==len(set(src))
            factor_denom=9**k if p==1 else 1
            numerator=8**k if p==1 else (1 if p==2 else (1 if k==0 else 0))
            target=[D*numerator*__import__('math').prod(sgn[e][a] for a in src) for e in initial]
        out_sign=[__import__('math').prod(sgn[e][a] for a in subset) for e in final]
        for i in range(8):
            actual=sum(M[i][j]*out_sign[j] for j in range(8))
            assert actual*factor_denom==target[i],(A,B,path,p,subset,actual, target[i],D)
    return sum(o is not None for o in h.values())

def main():
    hist=Counter();total=0
    for p in (0,1):
        for A,B in L:
            for C in unbr[B]:
                for D in unbr[C]:
                    r=check(A,B,(C,D),p)
                    hist[(p,r)]+=1;total+=1
    A,B=next(iter(L));extra=0
    for C in unbr[B]:
        for D in unbr[C]:
            for G in unbr[D]:
                check(A,B,(C,D,G),1);extra+=1
    for A,B in L:
        assert check(A,B,(A^B,),2)==3
    counts={str(p):{str(r):hist[(p,r)] for r in range(4)} for p in (0,1)}
    assert total==15360 and extra==512
    print(json.dumps({'status':'PASS','signed_vertices':60,'signed_directed_edges':960,
     'unsigned_directed_edges':120,'depth2_paths_tested':total,'depth3_paths_tested':extra,
     'p_equals_0_rank_histogram':counts['0'],'p_equals_half_rank_histogram':counts['1'],
     'p_equals_1_all_120_forced_rows_tested':True,'native_event_permission':False},indent=2,sort_keys=True))

if __name__=='__main__':main()
