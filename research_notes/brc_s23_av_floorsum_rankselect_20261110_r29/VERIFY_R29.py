#!/usr/bin/env python3
"""R29 source-preserving exact floor-sum and signed Farey certificate."""
from fractions import Fraction as F
from bisect import bisect_right
import argparse, csv

D=10**24
LO=262204504569236716045286
HI=262204504569236716045287
M=128
CASES=[(14298,3749,25339,6644,9),
       (154021,40385,168319,44134,2),
       (6318118,1656639,10899111,2857796,5)]

def floors(n,m,a,b):
    x,a=divmod(a,m)
    y,b=divmod(b,m)
    ans=x*n*(n-1)//2+y*n
    while 1:
        if a>=m:
            ans+=n*(n-1)*(a//m)//2
            a%=m
        if b>=m:
            ans+=n*(b//m)
            b%=m
        w=a*n+b
        if w<m:return ans
        n=w//m
        b=w%m
        m,a=a,m

def sf(L,U,s,T):
    return floors(U-L,D,T,(L-s)*T)

def old_order(T):
    return sorted(range(M),key=lambda s:(s*T)%D)

def arcs(T):
    ids=old_order(T)
    return [(ids[i],ids[(i+1)%M],
             (ids[i]*T)%D > (ids[(i+1)%M]*T)%D) for i in range(M)]

def count(L,U,arc,T):
    a,b,wrap=arc
    return sf(L,U,a,T)-sf(L,U,b,T)+(U-L)*(
        (a*T)//D-(b*T)//D+int(wrap))

def stable_floors(L,U):
    A=L-M+1
    B=U
    return floors(B-A,D,LO,A*LO)==floors(B-A,D,HI,A*HI)

def owner(t,T,phase_list):
    return (bisect_right(phase_list,(t*T)%D)-1)%M

def frac(t,T):
    return F((t*T)%D,D)

def strict_limit(num,den):
    """Largest integer k with k < num/den."""
    assert num>0 and den>0
    return (num.numerator*den.denominator-1)//(
        num.denominator*den.numerator)

def solve(q,p,j,c,expected_K,event_rows):
    assert j>=q>M and stable_floors(j-q+1,j)
    assert (p*D>q*HI) or (p*D<q*LO)
    upper=p*D>q*HI
    assert (j*p-q*c==1 if upper else q*c-j*p==1)
    A=arcs(LO)
    assert A==arcs(HI)
    def covered(H):
        return all(count(j-H,j,a,LO)>0 for a in A)
    assert covered(q-1)
    l,r=M,q-1
    while l<r:
        h=(l+r)//2
        if covered(h):r=h
        else:l=h+1
    H=l
    assert H==164 and covered(H) and not covered(H-1)
    assert stable_floors(j-H,j)
    hs=[]
    for a in A:
        l,r=1,H
        while l<r:
            h=(l+r)//2
            if count(j-h,j,a,LO)>0:r=h
            else:l=h+1
        assert count(j-l,j,a,LO)==1
        if l>1:assert count(j-l+1,j,a,LO)==0
        hs.append(l)
    assert max(hs)==H
    assert sum(h>128 for h in hs)==36
    assert [i for i,h in enumerate(hs) if h==164]==[127]
    leaders=[j-h for h in hs]
    assert sorted(t-j for t in leaders)==(
        list(range(-164,-97))+list(range(-61,0)))
    assert all(count(t,t+1,arc,T)==1
               for T in (LO,HI) for t,arc in zip(leaders,A))
    phase={T:[(s*T)%D for s in old_order(T)] for T in (LO,HI)}
    # Directional slack and neighbor-positivity bounds hold at both endpoints.
    Kowner=10**30
    Kneighbor=10**30
    for T in (LO,HI):
        e=F(p*D-q*T,D) if upper else F(q*T-p*D,D)
        v=F(j*T-c*D,D) if upper else F(c*D-j*T,D)
        assert e>0 and v>0
        Kneighbor=min(Kneighbor,strict_limit(v,e))
        for t in range(j-H,j):
            a,b,w=A[owner(t,T,phase[T])]
            gap=(frac(t,T)-frac(a,T))%1 if upper else (
                frac(b,T)-frac(t,T))%1
            assert gap>0
            Kowner=min(Kowner,strict_limit(gap,e))
    K=min(Kowner,Kneighbor)
    assert K==expected_K
    for T in (LO,HI):
        for t in range(j-H,j):
            initial=owner(t,T,phase[T])
            for k in range(K+1):
                assert owner(t+k*q,T,phase[T])==initial
    for k in range(K+1):
        # Both sign-convention cases are symmetric under reflection.
        e_coeff=(p,-q) if upper else (-p,q)
        v_coeff=(-c-k*p,j+k*q) if upper else (
            c+k*p,-j-k*q)
        e_below=all(e_coeff[0]*D+e_coeff[1]*T
                    <=v_coeff[0]*D+v_coeff[1]*T for T in (LO,HI))
        v_below=all(v_coeff[0]*D+v_coeff[1]*T
                    <=e_coeff[0]*D+e_coeff[1]*T for T in (LO,HI))
        assert e_below or v_below
        coeff=e_coeff if e_below else v_coeff
        for t in leaders:
            n=q+t+1+k*q
            assert j+k*q+1<=n<=j+(k+1)*q
            if event_rows:assert event_rows.get(n)==coeff,(n,coeff)
    return H,K,Kowner,Kneighbor,128*(K+1)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--r27-events",
                    help="Optional immutable R27 EVENT TSV with n,delta_A,delta_B")
    args=ap.parse_args()
    event_rows={}
    if args.r27_events:
        with open(args.r27_events,encoding="utf-8") as f:
            for row in csv.DictReader(f,delimiter="\t"):
                event_rows[int(row["n"])]=(
                    int(row["delta_A"]),int(row["delta_B"]))
    assert old_order(LO)==old_order(HI)
    assert stable_floors(M,2*M)
    total=0
    for q,p,j,c,k in CASES:
        H,K,Ko,Kn,events=solve(q,p,j,c,k,event_rows)
        total+=events
        print("PASS",q,"j",j,"H",H,"K",K,
              "owner_limit",Ko,"neighbor_limit",Kn,"events",events)
    assert total==2432
    print("PASS_R29_FLOORSUM_SIGNED_SUFFIX_BATCH"+(
        "_R27_CROSSCHECK" if event_rows else "_STANDALONE"))
if __name__=="__main__":main()
