#!/usr/bin/env python3
"""Exact S23/AV prefix-cell occupancy for arbitrary finite H and prefix length n.

Requires VERIFY_UNIVERSAL.py from the same research directory.
"""
from VERIFY_UNIVERSAL import rational_key,rank_lt,select

def occupancy(n,H,left,right):
    assert n>=0 and H>=1
    p,d,_,_,_=rational_key(n+H)
    vL,jL=left
    vR,jR=right
    X=-p*vR+d*jR
    Y=-p*vL+d*jL
    assert X<Y,(n,H,left,right,X,Y)
    return rank_lt(n,p,d,Y)-rank_lt(n,p,d,X+1)

def main():
    for H in range(1,14):
        p,d,_,_,_=rational_key(H)
        entries=sorted((p*v-d*j,v,j) for v in range(H+1) for j in range(H-v+1))
        for n in [0,1,2,3,5,10,15]:
            pp,dd,_,_,_=rational_key(n+H)
            prefix=[pp*l-dd*k for l in range(n+1) for k in range(n-l+1)]
            for i in range(len(entries)-1):
                L=entries[i][1:]
                R=entries[i+1][1:]
                X=-pp*R[0]+dd*R[1]
                Y=-pp*L[0]+dd*L[1]
                expected=sum(X<K<Y for K in prefix)
                actual=rank_lt(n,pp,dd,Y)-rank_lt(n,pp,dd,X+1)
                assert actual==expected,(H,n,L,R,actual,expected)
        print('EXHAUSTIVE_PASS',H,len(entries),'7 prefix budgets')
    H=10**12
    for n in [2455069,10**12]:
        pt,dt,_,_,_=rational_key(H)
        pp,dd,_,_,_=rational_key(H+n)
        M=(H+1)*(H+2)//2
        counts=[]
        for s in [0,1,M//7,M//2,M-2]:
            _,vl,jl=select(H,pt,dt,s)
            _,vr,jr=select(H,pt,dt,s+1)
            X=-pp*vr+dd*jr
            Y=-pp*vl+dd*jl
            c=rank_lt(n,pp,dd,Y)-rank_lt(n,pp,dd,X+1)
            assert c>=0
            counts.append(c)
        print('HUGE_EXACT_OCCUPANCY_PASS',H,'n',n,'cells',len(counts),'min_count',min(counts),'max_count',max(counts),'prefix_convergent',pp,dd)
    print('PASS_UNIVERSAL_FINITE_PREFIX_OCCUPANCY')

if __name__=='__main__':main()
