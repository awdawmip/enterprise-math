#!/usr/bin/env python3
"""Exact S23/AV Farey-epoch event sweep. Python stdlib only."""
from fractions import Fraction as F
from bisect import bisect_left, bisect_right
P,Q=262204504569236716045286,10**24
LO,HI=F(P,Q),F(P+1,Q)
TH=(LO+HI)/2
M,N=128,2000128

def theta_certificate():
    def log(z):
        acc,term=F(0),z
        for k in range(160):
            acc+=2*term/F(2*k+1);term*=z*z
        return acc,acc+2*term/((321)*(1-z*z))
    a,b=log(F(3,4));c,d=log(F(3,17));lo,hi=a/d,b/c
    def th(r):return 79*(2074774-380295*r)/(79*r-431)-46
    assert 79*lo>431 and LO<th(hi)<th(lo)<HI

def branch(x,y):
    v=[x[0]-y[0]+(x[1]-y[1])*t for t in (LO,HI)]
    assert all(z>0 for z in v) or all(z<0 for z in v) or v==[0,0]
    return (v[0]>0)-(v[0]<0)

def advance(a,b,c,d):
    z=[(b+d)*t-(a+c) for t in (LO,HI)]
    assert z[0]*z[1]>0
    return (a+c,b+d,c,d) if z[0]>0 else (a,b,a+c,b+d)

def farey(n):
    a,b,c,d=0,1,1,1
    while b+d<=n-1:a,b,c,d=advance(a,b,c,d)
    return a,b,c,d

def members_of_historical_arcs():
    orders=[];positions=[]
    for t in (LO,HI):
        x=sorted(((i*t.numerator)%t.denominator,i) for i in range(M))
        orders.append([i for _,i in x]);positions.append([v for v,_ in x])
    assert orders[0]==orders[1]
    out=[[] for _ in range(M)]
    for i in range(N):
        ix=[]
        for j,t in enumerate((LO,HI)):
            ix.append(bisect_right(positions[j],(i*t.numerator)%t.denominator)-1)
        assert ix[0]==ix[1],('phase order ambiguous',i)
        out[ix[0]].append(i)
    return out

def risk(n,a,b,c,d,arr):
    U,V,W=(-a,b),(c,-d),(c-a,b-d)
    A,B=1,0
    for row in arr:
        x,y=bisect_left(row,n-b),bisect_left(row,d)
        options=[]
        if x:options.append(U)
        if bisect_left(row,n)>y:options.append(V)
        if y>x:options.append(W)
        assert options
        winner=options[0]
        for z in options[1:]:
            if branch(z,winner)>0:winner=z
        A-=winner[0];B-=winner[1]
    return A,B

def run():
    theta_certificate();arr=members_of_historical_arcs()
    a,b,c,d=farey(M);n=M;blocks=[];epochs=0;candidates=0
    while n<=N:
        epochs+=1;end=min(N,b+d);cut={n}
        for row in arr:
            if not row:continue
            t=b+row[0]+1
            if n<t<=end:cut.add(t)
            k=bisect_left(row,d)
            if k<len(row):
                t=row[k]+1
                if n<t<=end:cut.add(t)
            if k:
                t=b+row[k-1]+1
                if n<t<=end:cut.add(t)
        cs=sorted(cut);candidates+=len(cs)-1
        for i,at in enumerate(cs):
            till=cs[i+1]-1 if i+1<len(cs) else end
            expr=risk(at,a,b,c,d,arr)
            if blocks and blocks[-1][1]+1==at and blocks[-1][2]==expr:
                blocks[-1]=(blocks[-1][0],till,expr)
            else:blocks.append((at,till,expr))
        n=end+1
        if n<=N:a,b,c,d=advance(a,b,c,d)
    assert blocks[0]==(M,M,(0,0)) and blocks[-1][1]==N
    assert all(blocks[i][1]+1==blocks[i+1][0] and branch(blocks[i+1][2],blocks[i][2])>0 for i in range(len(blocks)-1))
    for n,ans in {200128:(479873,-1830144),322177:(520258,-1984165),1000128:(-5169279,19714688),2000128:(-21156991,80688896)}.items():
        got=next(z[2] for z in blocks if z[0]<=n<=z[1]);assert got==ans,(n,got,ans)
    assert next(z for z in blocks if z[0]<=1000128<=z[1])[1]==1106579
    assert next(z for z in blocks if z[0]==1106580)[2]==(-5003990,19084306)
    print('CERTIFIED_THETA_160_TERMS',P,P+1,Q)
    print('FAREY_EPOCHS',epochs,'CANDIDATE_THRESHOLDS',candidates,'MAXIMAL_RISK_BLOCKS',len(blocks))
    print('R(128,2000000)',*blocks[-1][2],float(blocks[-1][2][0]+blocks[-1][2][1]*TH))
    print('NEXT_GROWTH_AFTER_L1000000','L=1106452','delta=165289-630382*theta')
    print('PASS_S23_AV_FAREY_EVENT_GENERATOR_2M')
    with open('BLOCKS_2M.tsv','w') as f:
        f.write('n_start\tn_end\tA\tB\n')
        for a,b,(c,d) in blocks:f.write(f'{a}\t{b}\t{c}\t{d}\n')
if __name__=='__main__':run()
