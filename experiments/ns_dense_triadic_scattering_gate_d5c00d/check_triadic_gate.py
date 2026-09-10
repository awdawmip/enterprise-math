#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product, permutations
import argparse, json
from pathlib import Path


def coeffs(common, diff):
    return F(common + 2*diff, 3), F(common - diff, 3)


def triad(x, d, o):
    a,b,c=x
    return (d*a+o*b+o*c, o*a+d*b+o*c, o*a+o*b+d*c)


def dot(x,y): return sum(a*b for a,b in zip(x,y))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('results_18.json')); a=ap.parse_args()
    classes=[]
    for common,diff in product((1,-1), repeat=2):
        d,o=coeffs(common,diff)
        cols=[triad(tuple(F(i==j) for i in range(3)),d,o) for j in range(3)]
        assert all(dot(cols[i],cols[j])==(1 if i==j else 0) for i in range(3) for j in range(3))
        classes.append((common,diff,d,o))
    assert classes==[(1,1,F(1),F(0)),(1,-1,F(-1,3),F(2,3)),(-1,1,F(1,3),F(-2,3)),(-1,-1,F(-1),F(0))]
    orders=tuple(permutations(range(6))); assert len(orders)==720
    cases={}
    for common,diff in ((1,-1),(-1,1)):
        d,o=coeffs(common,diff)
        resolved=set(); residual=set()
        for h in orders:
            rank={axis:k for k,axis in enumerate(h)}
            emit=tuple(o*d**rank[i] for i in range(6))
            residual.add(emit)
            beta=tuple(o*d**(5-rank[i])*emit[i] for i in range(6))
            resolved.add((d**12,beta))
            assert d**12 + 2*sum(e*e for e in emit) <= 1
        assert len(resolved)==1 and len(residual)==720
        center,betas=next(iter(resolved)); assert len(set(betas))==1
        beta=betas[0]; assert beta==4*d**7
        if common==1: bg=(F(1),F(1),F(1))
        else: bg=(F(2),F(-1),F(-1))
        assert triad(bg,d,o)==bg
        cases[str((common,diff))]={
            'diag':str(d),'offdiag':str(o),'sum_preserving':common==1,
            'center':str(center),'each_neighbor':str(beta),'laplacian_coefficient':str(beta),
            'I_coefficient':str(center+12*beta),'resolved_order_classes':len(resolved),
            'residual_order_signatures':len(residual),'dense_triad_background_fixed':True}
    assert cases[str((1,-1))]['laplacian_coefficient']=='-4/2187'
    assert cases[str((-1,1))]['laplacian_coefficient']=='4/2187'
    lam=F(11665,531441)
    assert F(1,531441)+12*F(4,2187)==lam
    assert F(1,531441)/lam==F(1,11665) and F(4,2187)/lam==F(972,11665)
    assert all(not all(p[i]==i for p in orders) for i in range(6))
    for h in orders:
        q=h; seen=[]
        for _ in range(6): seen.append(q[0]); q=q[1:]+q[:1]
        assert set(seen)==set(range(6)) and q==h
    data={
      'schema':'EM_DENSE_TRIADIC_SCATTERING_GATE_RESULTS_V1',
      'event_id':'NS-DENSE-TRIADIC-SCATTERING-GATE-20260910-D5C00D-18',
      'S3_classes':[[c,d,str(x),str(y)] for c,d,x,y in classes],
      'one_layer_cavity_triples':66,'one_layer_max_direct_ports':2,
      'bare_symmetric_axis_selector_exists':False,'fair_order_orbit_bound':720,
      'cases':cases,
      'positive_normalized_shape':{'attenuation':str(lam),'center':'1/11665','neighbor_each':'972/11665','operator':'I+(972/11665) Delta_X6'},
      'fresh_rerun_expected_deterministic':True,
      'nonclaims':['algebraic triad != certified TRIADIC_CLOSURE_E','two-sweep compression != all-time heat law','no NS or viscosity theorem']}
    text=json.dumps(data,indent=2)+'\n'; a.output.write_text(text); print(text)

if __name__=='__main__': main()
