"""Separate modulus cuts coupling two original coordinate directions.

Each point coefficient is lambda(x_axis1)+mu(x_axis2), not a replacement of
the joint native state by either marginal. All q^8 normalized pairs of fiber
functions and all q^4 type coefficients are covered by a q-state DP.
"""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction
from math import lcm
import argparse,json,time
import numpy as np
from parallel_family import TYPES,COUNTS,POINTS,FIBERS
from modular_fibers import optimize_types

HERE=Path(__file__).resolve().parent
AXIS_FORMS=(6,1,0)

def scan_joint(doc,q=3,exact=False):
    rows=doc['weights'];ms=[int(r['mask']) for r in rows];free=int(doc['free_mask'])
    ts=np.array([TYPES.index((r['size'],r['cost'])) for r in rows]);Q=1
    if exact:
        for row in rows:Q=lcm(Q,row['denominator'])
        weights=[row['numerator']*(Q//row['denominator']) for row in rows]
    else:weights=np.array([row['numerator']/row['denominator'] for row in rows])
    coeff=np.array([(0,)+x for x in product(range(q),repeat=4)],dtype=np.int16)
    residue=[];base=[]
    for f in AXIS_FORMS:
        occ=np.array([[(m&h).bit_count() for h in FIBERS[f]] for m in ms],dtype=np.int16)
        occfree=np.array([(free&h).bit_count() for h in FIBERS[f]],dtype=np.int16)
        residue.append((coeff@occ.T)%q);base.append((coeff@occfree)%q)
    best=None;violations=[];tested=0
    type_indices=[ts==t for t in range(4)]
    for ax,ay in combinations(range(3),2):
        for k,lam in enumerate(coeff):
            for h,mu in enumerate(coeff):
                rr=(residue[ax][k]+residue[ay][h])%q;W=[[0]*q for t in TYPES]
                if exact:
                    for t,r,w in zip(ts,rr,weights):W[int(t)][int(r)]+=w
                else:
                    for t in range(4):W[t]=np.bincount(rr[type_indices[t]],weights=weights[type_indices[t]],minlength=q).tolist()
                costs=[[sum(((r+a)%q)*W[t][r] for r in range(q)) for a in range(q)] for t in range(4)]
                dp=optimize_types(costs,int(base[ax][k]+base[ay][h]),q)
                for r in range(1,q):
                    value,a=dp[r];gap=value-Q*r;row=(gap,value,ax,ay,tuple(map(int,lam)),tuple(map(int,mu)),a,r)
                    if best is None or row<best:best=row
                    tested+=1
                    if gap<(-1e-8 if not exact else 0):violations.append(row)
    def describe(row):
        gap,val,ax,ay,lam,mu,a,r=row
        return {'axes':[ax,ay],'fiber_coefficients':[lam,mu],'type_coefficients':a,'rhs':r,
                'point_coefficients':[(lam[p[ax]]+mu[p[ay]])%q for p in POINTS],
                'lhs':str(Fraction(val,Q)) if exact else float(val),
                'gap':str(Fraction(gap,Q)) if exact else float(gap)}
    return {'modulus':q,'exact':exact,'dp_residue_checks':tested,
            'represented_index_checks':3*q**11*(q-1),'minimum':describe(best),
            'violating_dp_minima':len(violations),'strongest_violations':[describe(x) for x in sorted(violations)[:40]]}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--frames',type=int,nargs='+',default=[1,2]);p.add_argument('--q',type=int,default=3);p.add_argument('--exact',action='store_true');p.add_argument('--witness-dir',type=Path,default=HERE/'modular_closure_2345');p.add_argument('--prefix',default='floating_feasible_');a=p.parse_args()
    for f in a.frames:
        d=json.loads((a.witness_dir/f'{a.prefix}{f}.json').read_text());start=time.monotonic()
        result={'frame':f,**scan_joint(d,a.q,a.exact),'seconds':time.monotonic()-start}
        (HERE/f'joint_axes_{f}_q{a.q}_exact{int(a.exact)}.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({'frame':f,'violating_dp_minima':result['violating_dp_minima'],'minimum':result['minimum'],'seconds':result['seconds']}),flush=True)
