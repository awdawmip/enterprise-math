#!/usr/bin/env python3
"""Exact combinatorial preflight for T6 p13 order9 signed split(2,7)."""
from itertools import product, groupby, combinations_with_replacement
from math import comb

def partitions(total,low=1):
    if total==0:
        yield ()
        return
    for x in range(low,total+1):
        for tail in partitions(total-x,x):
            yield (x,)+tail

def run():
    out=[]
    for pat in partitions(7):
        groups=[len(tuple(g)) for _,g in groupby(pat)]
        nro=common=0
        for blks in product(*(combinations_with_replacement(range(1,13),k)
                             for k in groups)):
            neg=tuple(zip(pat,(r for block in blks for r in block)))
            d1=len({r for q,r in neg if q==1})
            d2=len({r for q,r in neg if q==2})
            # Positive q-order2 is either one q2 atom (12 ways) or
            # a multiset of two q1 residues (C(13,2)=78 ways).
            # Shared named positive atom count is exact by complement.
            common+=d2 + 78-comb(13-d1,2)
            nro+=1
        out.append(dict(pattern=pat,negative_rosters=nro,raw_pairs=90*nro,
                        common_canceled=common,disjoint_pairs=90*nro-common))
    total=lambda key:sum(row[key] for row in out)
    assert total("negative_rosters")==153960
    assert total("raw_pairs")==13856400
    assert total("common_canceled")==5547384
    assert total("disjoint_pairs")==8309016
    return out

if __name__=="__main__":
    for row in run():print(row)
