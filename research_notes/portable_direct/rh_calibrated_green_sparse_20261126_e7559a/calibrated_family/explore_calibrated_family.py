#!/usr/bin/env python3
"""Labeled floating exploration of two added thickness nodes, not a certificate."""
from pathlib import Path
from fractions import Fraction as F
import argparse
import json
import mpmath as mp


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,required=True,help='riemann_signed_green_thickness_phase_20261124 package')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('calibration_exploration.json'))
    args=parser.parse_args();mp.mp.dps=100
    path=args.previous/'prior/riemann_native_residual_growth_20261124/prior/riemann_matching_isotonic_anchors_20261124/prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123/prefix_compute/fixed_matched_family.json'
    nodes=list(map(F,json.loads(path.read_text())['nodes']));cache={}
    def number(x):return mp.mpf(x.numerator)/x.denominator
    def weights(xs):return [mp.fprod(number(b/(b-a)) for b in xs if b!=a) for a in xs]
    def dc(a):
        x=number(a);z=mp.zeta(1+x);g=1/z;gp=-mp.diff(mp.zeta,1+x)/z**2
        return g/x,1+mp.euler+(mp.euler-1)*g/x+(gp-1)/x
    def coeff(xs):
        w=weights(xs)
        for a in xs:
            if a not in cache:cache[a]=dc(a)
        return mp.fsum(w[i]*cache[a][0] for i,a in enumerate(xs))-1,mp.fsum(w[i]*cache[a][1] for i,a in enumerate(xs))
    rows=[]
    choices=[(F(1,8),F(3,8)),(F(1,4),F(3,8)),(F(1,8),F(1,3)),(F(1,1000),F(1,2000)),
             (F(1,32),F(3,32)),(F(1,64),F(1,32)),(F(1,16),F(3,16)),(F(1,4),F(1,3))]
    for u,v in choices:
        sets=[nodes,nodes+[u],nodes+[u,v]]
        (d0,c0),(d1,c1),(d2,c2)=map(coeff,sets)
        alpha,beta=mp.lu_solve(mp.matrix([[d1-d0,d2-d1],[c1-c0,c2-c1]]),mp.matrix([-d0,-c0]))
        mixture=[1-alpha,alpha-beta,beta]
        bases=[weights(xs)+[mp.mpf(0)]*(13-len(xs)) for xs in sets]
        actual=[mp.fsum(mixture[i]*bases[i][j] for i in range(3)) for j in range(13)]
        hs=[mp.fprod(number(a)/(number(a)+1) for a in xs) for xs in sets]
        ratio=mp.fsum(abs(mixture[i])*hs[i] for i in range(3))/hs[0]
        rows.append({'u':str(u),'v':str(v),'co':[mp.nstr(x,20) for x in mixture],
                     'tv':mp.nstr(mp.fsum(abs(x) for x in actual),20),'radius_ratio_s1':mp.nstr(ratio,20),
                     'density_errors':[mp.nstr(x,12) for x in [d0,d1,d2]],
                     'constants':[mp.nstr(x,12) for x in [c0,c1,c2]]})
    result={'arithmetic':'mpmath100 floating exploration, no certificate decisions','rows':rows}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'EXPLORATION_ONLY','rows':len(rows)}))


if __name__=='__main__':main()
