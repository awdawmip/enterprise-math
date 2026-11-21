"""Construct exact points satisfying full stars and all 155 affine-fiber parity cuts."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from itertools import product
import argparse,json,time
import numpy as np
import sympy as sp
from scipy.optimize import linprog
from scipy.sparse import csr_matrix
HERE=Path(__file__).resolve().parent
from discovery_common import DELIVERY_ROOT,load_problem,points,verify_stars,native_module
P=list(product(range(5),repeat=3))
FORMS=[(0,0,1)]+[(0,1,a)for a in range(5)]+[(1,a,b)for a in range(5)for b in range(5)]
FIBERS=[sum(1<<i for i,p in enumerate(P)if sum(x*y for x,y in zip(a,p))%5==v)for a in FORMS for v in range(5)]

def solve_frame(frame,bank_path,initial_dir,output_dir,delivery_root=DELIVERY_ROOT,seconds=180,lp_seconds=30):
    source,fd,bank,masks,ts,types,eq,target=load_problem(frame,bank_path,delivery_root)
    initial=json.loads((initial_dir/f'parity_cover_{frame}.json').read_text());core=list(map(int,initial['core_masks']));free=int(initial['free_mask'])
    assert free==int(fd['free'])
    linears,shifts=native_module(delivery_root).symmetries();removed=list(points(((1<<125)-1)^free));stab=[]
    for lin in linears:
        r=[lin[i]for i in removed]
        for sh in shifts:
            if sum(sh[i]for i in r)==((1<<125)-1)^free:
                stab.append([sh[lin[i]].bit_length()-1 for i in range(125)])
    coeff=np.array([[(m&h).bit_count()%2 for m in masks]for h in FIBERS],dtype=np.int8)
    rhs=np.array([1-sum((m&h).bit_count()%2 for m in core)for h in FIBERS],dtype=int)
    rng=np.random.default_rng(202611201+frame);weights=defaultdict(Fraction);type_for={};started=time.monotonic();vertices=0;history=[]
    while time.monotonic()-started<seconds:
        if vertices==0:rows=initial['weights']
        else:
            fit=linprog(rng.normal(size=len(masks)),A_eq=eq,b_eq=target,A_ub=csr_matrix(-coeff),b_ub=-rhs,bounds=(0,None),method='highs',options={'time_limit':lp_seconds})
            if fit.x is None:
                print('solver stopped',frame,fit.message,flush=True);break
            support=np.flatnonzero(fit.x>1e-8);active=np.flatnonzero(abs(coeff@fit.x-rhs)<1e-7)
            A=sp.Matrix(eq[:,support].toarray());b=sp.Matrix([int(t)for t in target])
            if len(active):A=A.col_join(sp.Matrix(coeff[np.ix_(active,support)]));b=b.col_join(sp.Matrix(rhs[active]))
            exact,params=A.gauss_jordan_solve(b);assert not params.rows
            rows=[{'mask':str(masks[j]),'size':types[ts[j]][0],'cost':types[ts[j]][1],'numerator':int(w.p),'denominator':int(w.q)}for j,w in zip(support,exact)]
        assert all(r['numerator']>0 for r in rows)
        # Each source point satisfies all fiber cuts exactly before averaging.
        for h in FIBERS:
            odd=sum((Fraction(r['numerator'],r['denominator'])for r in rows if(int(r['mask'])&h).bit_count()%2),Fraction(sum((m&h).bit_count()%2 for m in core)))
            assert odd>=1
        for r in rows:
            m=int(r['mask']);w=Fraction(r['numerator'],r['denominator'])/len(stab)
            for g in stab:
                nm=sum(1<<g[p]for p in points(m));weights[nm]+=w;type_for[nm]=r['size'],r['cost']
        vertices+=1;normalized={m:w/vertices for m,w in weights.items()};q,best=verify_stars(normalized,free)
        row={'frame':frame,'source_vertices':vertices,'stabilizer_order':len(stab),'support':len(normalized),'min_star_slack':str(Fraction(best[0],q)),'min_star_slack_float':best[0]/q,'seconds':time.monotonic()-started}
        print(json.dumps(row),flush=True);history.append(row)
        if best[0]>=0:
            final={'schema':'FULL_STAR_AND_AFFINE_FIBER_PARITY_COVER_V1','frame':frame,'free_mask':str(free),'core_masks':initial['core_masks'],'weights':[{'mask':str(m),'size':type_for[m][0],'cost':type_for[m][1],'numerator':w.numerator,'denominator':w.denominator}for m,w in sorted(normalized.items())]}
            dest=output_dir/'full_system';dest.mkdir(parents=True,exist_ok=True)
            (dest/f'cover_{frame}.json').write_text(json.dumps(final,separators=(',',':'))+'\n')
            break
    else:print('time limit',frame,flush=True)
    (output_dir/f'joint_history_{frame}.json').write_text(json.dumps(history,indent=2)+'\n')
    return history

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bank',type=Path,required=True,help='complete <QQII candidate bank; see prepare_discovery_bank.py')
    parser.add_argument('--initial-dir',type=Path,help='directory containing parity_cover_1..5.json; defaults to the shipped witnesses')
    parser.add_argument('--output-dir',type=Path,required=True,help='separate directory for rediscovered full_system witnesses and histories')
    parser.add_argument('--delivery-root',type=Path,default=DELIVERY_ROOT)
    parser.add_argument('--frames',type=int,nargs='+',choices=range(1,6),default=list(range(1,6)))
    parser.add_argument('--seconds',type=float,default=180,help='discovery time budget per frame')
    parser.add_argument('--lp-seconds',type=float,default=30,help='time limit for each supplementary LP')
    args=parser.parse_args()
    if args.seconds<=0 or args.lp_seconds<=0:parser.error('time budgets must be positive')
    args.output_dir.mkdir(parents=True,exist_ok=True)
    initial_dir=args.initial_dir or args.delivery_root/'fractional/next_cuts'
    for frame in args.frames:
        solve_frame(frame,args.bank,initial_dir,args.output_dir,args.delivery_root,args.seconds,args.lp_seconds)
