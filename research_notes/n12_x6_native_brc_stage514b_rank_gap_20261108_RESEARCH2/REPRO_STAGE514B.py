#!/usr/bin/env python3
"""Stage514-B finite checker for arbitrary query-rank sets, reusing Stage513 BRC F and D_h machinery."""
from pathlib import Path
import importlib.util, json
from itertools import product, combinations

base=Path(__file__).resolve().parent.parent
candidate_paths=[base/'stage513b'/'repro_stage513b.py',base/'n12_x6_native_brc_stage513b_rank1_sharp_cap_20261108_RESEARCH2'/'REPRO_STAGE513B.py']
source=next((p for p in candidate_paths if p.exists()),None)
if not source:raise FileNotFoundError('Need sibling Stage513-B exact source')
spec=importlib.util.spec_from_file_location('stage513_verified',source)
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)


def cap(S):
    prev=0;out=0
    for s in sorted(S):out=max(out,s-prev-1);prev=s
    return out


def check(tags,h,R,S,stats):
    D,nstates=b.exposure(tags,h,R,S);T=cap(S)
    w=tuple((i,(i*7+3)%12,int(tags[i])) for i in range(len(tags)))
    work=[(w,b.compress(w,D,T),0)]
    while work:
        full,small,t=work.pop()
        assert small==b.compress(full,D,T)
        obs=b.F([x[1] for x in full]); recom=b.F([])
        for part in small: recom=b.join(recom,b.F([part[1][1]]) if part[0]=='T' else part[1])
        assert obs==recom
        stats['nodes']+=1
        if t==h:continue
        for act in b.actions(len(full),R,S):
            nxt,compressed=b.apply(full,small,D,T,act)
            stats['transitions']+=1
            if nxt is not None:
                assert compressed==b.compress(nxt,D,T)
                if t+1<h:work.append((nxt,compressed,t+1))
    stats['roots']+=1;stats['preprocessor_states']+=nstates


def sharp(S):
    Q=sorted(S); prev=0; maxgap=0;target=0;m=0
    for k in Q:
        if k-prev>maxgap:maxgap=k-prev;target=k;m=prev
        prev=k
    if maxgap==1:return None
    d=maxgap;T=d-1;g=max(4,d);suffix_len=m+5
    n=2+g+suffix_len
    a=[1,1]+[1]*(d-2)+[0]*(g-d+2)+[0]*5+[1]*m
    z=[1,1]+[1]*(d-1)+[0]*(g-d+1)+[0]*5+[1]*m
    assert len(a)==len(z)==n
    # Explicitly SET the prefix and all suffix tokens, never a gap token.
    R={n-1-i for i in list(range(2))+list(range(2+g,n))}
    D1,_=b.exposure(a,1,R,set(S));D2,_=b.exposure(z,1,R,set(S))
    assert D1==D2,(S,D1,D2)
    directions=[0,2]+[4]*g+[(6+2*i)%12 for i in range(suffix_len)]
    w1=tuple((i,directions[i],a[i]) for i in range(n))
    w2=tuple((i,directions[i],z[i]) for i in range(n))
    assert b.compress(w1,D1,T-1)==b.compress(w2,D2,T-1)
    # Lower cap conflates the two histories but rank target removes E1 versus E2.
    k=target
    p1=[i for i,x in enumerate(w1) if x[2]];p2=[i for i,x in enumerate(w2) if x[2]]
    id1=p1[-k];id2=p2[-k]
    assert id1==0 and id2==1,(S,id1,id2)
    f1=b.F([x[1] for j,x in enumerate(w1) if j!=id1]);f2=b.F([x[1] for j,x in enumerate(w2) if j!=id2])
    assert f1!=f2
    return {'S':Q,'T_opt':T,'T_failed':T-1,'n':n,'rank':k,'mask_len':len(D1),'distance_coords1':list(f1[1]),'distance_coords2':list(f2[1])}


def main():
    stats=dict(roots=0,nodes=0,transitions=0,preprocessor_states=0)
    ranksets=[]
    for K in (2,3,4):
        ranksets.extend(tuple(s) for size in range(1,K+1) for s in combinations(range(1,K+1),size) if K in s)
    for n in range(2,7):
        for tags in product((0,1),repeat=n):
            for S in ranksets:
                for h in (1,2):check(tags,h,{0,2,n-1},set(S),stats)
    for n in (7,9,12):
        for j in range(8):
            tags=[int(((i*17+j*3)%11)<5) for i in range(n)]
            for S in ((2,4),(1,3),(1,2,3,4),(3,5)):
                check(tags,3,{0,2,n-2},set(S),stats)
    sharpness=[sharp(S) for S in ((3,),(1,3),(1,4),(2,4),(1,2,4),(2,5),(1,2,3,4),(1,3,6))]
    sharpness=[x for x in sharpness if x is not None]
    print(json.dumps({'version':'STAGE514B','cap_formula':'max_j (s_j-s_(j-1)-1), s_0=0','verified':stats,'sharpness':sharpness,'assertions':'PASS','type':'exact X6 6D signed + 144 directed BRC adjacency'},indent=2))
if __name__=='__main__':main()
