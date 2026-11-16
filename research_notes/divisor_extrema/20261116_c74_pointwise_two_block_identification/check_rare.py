"""Exact row scan for the near-synchrony condition with K=3 and B=1."""
from fractions import Fraction as Q
import json


def near_rows(limit):
    # rho(n,s) = 4*prefix[n]/prefix[s-1]; prefix decreases strictly.
    prefix=[Q(1)]
    for k in range(1,limit+1):
        prefix.append(prefix[-1]*Q(4*k+3,4*(k+3)))
    rows={2:[],8:[]}
    equalities={2:[],8:[]}
    tested=0
    for n in range(2,limit+1):
        factor=4*prefix[n]
        near=None
        # Find the first rho>=1; rho strictly increases in s.
        lo,hi=2,n
        while lo<hi:
            mid=(lo+hi)//2
            if factor<prefix[mid-1]:lo=mid+1
            else:hi=mid
        for s in range(max(2,lo-1), min(n,lo)+1):
            rho=factor/prefix[s-1]
            err=abs(1-rho)
            if near is None or err < near[0]:near=err,s
        err,s=near
        if n<=64:
            complete=[(abs(1-factor/prefix[j-1]),j) for j in range(2,n+1)]
            assert near==min(complete)
        for e in (2,8):
            if err < Q(1,n**e):rows[e].append([n,s])
            if err == Q(1,n**e):equalities[e].append([n,s])
        tested+=1
    return dict(max_stock=limit,rows_tested=tested,strict_bounds=rows,
                threshold_equalities=equalities,full_minimum_controls_through=64)


if __name__=='__main__':
    print(json.dumps(near_rows(1024),indent=2))
