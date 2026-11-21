"""Discover modulus-q cuts using weighted parallel fibers and type counts.

The 0th fiber coefficient is set to zero without loss: subtracting a constant
from all five point coefficients is absorbed by the four type coefficients.
The type coefficient possibilities are minimized by a q-state exact dynamic
program (when integer weights are supplied), not sampled.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
from math import lcm
import argparse,json,time
import numpy as np
from parallel_family import TYPES,COUNTS,FORMS,FIBERS

HERE=Path(__file__).resolve().parent

def optimize_types(cost,base,q):
    # Return minimum lhs for each residue of base + sum a_t n_t.
    dp={base%q:(0,())}
    for t in range(4):
        new={}
        for old,(val,bits) in dp.items():
            for a in range(q):
                nr=(old+a*COUNTS[t])%q;candidate=(val+cost[t][a],bits+(a,))
                if nr not in new or candidate<new[nr]:new[nr]=candidate
        dp=new
    return dp

def scan(doc,q,exact=False):
    rows=doc['weights'];ms=[int(r['mask']) for r in rows];free=int(doc['free_mask'])
    ts=np.array([TYPES.index((r['size'],r['cost'])) for r in rows]);Q=1
    if exact:
        for r in rows:Q=lcm(Q,r['denominator'])
        weights=[r['numerator']*(Q//r['denominator']) for r in rows]
    else:weights=np.array([r['numerator']/r['denominator'] for r in rows])
    best=None;tested=0;violations=[]
    lambdas=np.array([(0,)+lam for lam in product(range(q),repeat=4)],dtype=int)
    for f in range(31):
        occupancy=np.array([[(m&h).bit_count() for h in FIBERS[f]] for m in ms],dtype=int)
        free_occ=np.array([(free&h).bit_count() for h in FIBERS[f]],dtype=int)
        all_residues=(lambdas@occupancy.T)%q
        bases=(lambdas@free_occ)%q
        for k,lam in enumerate(lambdas):
            residue=all_residues[k];W=[[0]*q for t in TYPES]
            if exact:
                for t,r,w in zip(ts,residue,weights):W[int(t)][int(r)]+=w
            else:
                for t in range(4):
                    ii=ts==t;W[t]=np.bincount(residue[ii],weights=weights[ii],minlength=q).tolist()
            costs=[[sum(((r+a)%q)*W[t][r] for r in range(q)) for a in range(q)] for t in range(4)]
            dp=optimize_types(costs,int(bases[k]),q)
            for r in range(1,q):
                value,a=dp[r];gap=value-Q*r;row=(gap,value,f,tuple(map(int,lam)),a,r)
                if best is None or row<best:best=row
                tested+=1
                if gap<(-1e-8 if not exact else 0):violations.append(row)
    def describe(row):
        gap,val,f,lam,a,r=row
        return {'form_index':f,'form':FORMS[f],'fiber_coefficients':lam,'type_coefficients':a,
                'rhs':r,'lhs':str(Fraction(val,Q)) if exact else float(val),
                'gap':str(Fraction(gap,Q)) if exact else float(gap)}
    return {'modulus':q,'exact':exact,'coefficient_normalization':'lambda_0=0',
            'dp_residue_checks':tested,'represented_index_checks':31*q**7*(q-1),
            'minimum':describe(best),'violating_dp_minima':len(violations),
            'strongest_violations':[describe(row) for row in sorted(violations)[:20]]}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--frames',type=int,nargs='+',default=[1,2,3,4,5]);p.add_argument('--moduli',type=int,nargs='+',default=[3]);p.add_argument('--exact',action='store_true');p.add_argument('--witness-dir',type=Path,default=HERE/'full_system');a=p.parse_args()
    for f in a.frames:
        doc=json.loads((a.witness_dir/f'cover_{f}.json').read_text())
        for q in a.moduli:
            start=time.monotonic();result={'frame':f,**scan(doc,q,a.exact),'seconds':time.monotonic()-start}
            (HERE/f'modular_{f}_q{q}_exact{int(a.exact)}.json').write_text(json.dumps(result,indent=2)+'\n')
            print(json.dumps(result),flush=True)
