"""Glue the finite unlabelled-column band to the long-first-gap uniform derivative bound."""
from fractions import Fraction as F
from functools import cache
from argparse import ArgumentParser
from math import comb
from pathlib import Path
import json,sys

def main(model):
    sys.path.insert(0,str(model.resolve()))
    from stock_shift import block
    @cache
    def visible(r,c,v):
        rho,tau=block(r,c,c-v)
        k=2*r+1
        return rho<1 and 4*tau < rho*F(3*k,k+4*v)
    rows=[]
    # L_r(c) counts a certified family of words identifiable among arbitrary
    # competitors at this stock. The finite first-divergence band gives ALL.
    @cache
    def count(r,c):
        if not r:return 1
        cap=100 if r<=4 else (40 if r<=6 else 35)
        if c<=cap:return comb(r+c-2,r)
        return sum(count(r-1,v) for v in range(2,c+1) if visible(r,c,v))
    for cap,rmax in [(100,4),(40,6),(35,33)]:
        for r in range(1,rmax+1):
            if r<=4 and cap!=100:continue
            if 5<=r<=6 and cap!=40:continue
            c=cap+1
            good=[v for v in range(2,c+1) if visible(r,c,v)]
            lim=max(good,default=1)
            assert good==list(range(2,lim+1))
            rows.append(dict(r=r,finite_cap=cap,at_cap_plus_one_landing_limit=lim,
                             lower_bound_uniform_identified_suffixes=str(sum(count(r-1,v) for v in good))))
    return dict(rows=rows)

if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--prior',type=Path,required=True,help='C68/twoblocks directory')
    print(json.dumps(main(p.parse_args().prior),indent=2))
