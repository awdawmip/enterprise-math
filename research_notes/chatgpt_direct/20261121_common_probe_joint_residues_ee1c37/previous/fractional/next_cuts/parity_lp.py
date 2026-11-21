"""Test the full candidate type LP with all 15 coordinate-fiber parity cuts.

Floating status is diagnostic. When feasible, reconstruct and verify an exact
rational basic solution. The complete native candidate bank is reused, not only
the support of previous witnesses.
"""
from pathlib import Path
from fractions import Fraction
import argparse,json,time
import numpy as np
import sympy as sp
from scipy.optimize import linprog
from scipy.sparse import csr_matrix
HERE=Path(__file__).resolve().parent
from discovery_common import DELIVERY_ROOT,load_problem
from fiber_parity import fibers

def run(frame,bank_path,output_dir,delivery_root=DELIVERY_ROOT,seconds=60):
    source,fd,bank,masks,ts,types,eq,target=load_problem(frame,bank_path,delivery_root)
    core_doc=json.loads((delivery_root/'fractional/proof'/f'cover_{frame}.json').read_text());cores=list(map(int,core_doc['core_masks']))
    subset=fibers();coeff=np.array([[(m&h).bit_count()%2 for m in masks]for _,_,h in subset],dtype=np.int8)
    rhs=np.array([1-sum((m&h).bit_count()%2 for m in cores)for _,_,h in subset],dtype=int)
    assert np.all(rhs==1)
    start=time.monotonic()
    fit=linprog(np.zeros(len(masks)),A_eq=eq,b_eq=target,A_ub=csr_matrix(-coeff),b_ub=-rhs,bounds=(0,None),method='highs',options={'time_limit':seconds})
    out={'frame':frame,'complete_candidates':len(masks),'solver_status':int(fit.status),'solver_message':fit.message,'seconds':time.monotonic()-start}
    if fit.x is not None:
        support=np.flatnonzero(fit.x>1e-8);active=np.flatnonzero(abs(coeff@fit.x-rhs)<1e-7)
        A=sp.Matrix(eq[:,support].toarray());b=sp.Matrix([int(t)for t in target])
        if len(active):A=A.col_join(sp.Matrix(coeff[np.ix_(active,support)]));b=b.col_join(sp.Matrix(rhs[active]))
        solution,params=A.gauss_jordan_solve(b);assert not params.rows
        weights=[Fraction(int(v.p),int(v.q))for v in solution];assert all(w>0 for w in weights)
        parity=[sum((weights[k]*int(coeff[i,j])for k,j in enumerate(support)),Fraction())for i in range(15)]
        assert all(x>=1 for x in parity)
        rows=[{'mask':str(masks[j]),'size':types[ts[j]][0],'cost':types[ts[j]][1],'numerator':w.numerator,'denominator':w.denominator}for j,w in zip(support,weights)]
        cert={'frame':frame,'free_mask':str(fd['free']),'core_masks':core_doc['core_masks'],'weights':rows,'parity_weights':[str(x)for x in parity]}
        (output_dir/f'parity_cover_{frame}.json').write_text(json.dumps(cert,separators=(',',':'))+'\n')
        out.update(exact_feasible=True,support=len(rows),active_parity_cuts=len(active),minimum_parity_weight=str(min(parity)))
    print(json.dumps(out),flush=True);return out

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bank',type=Path,required=True,help='complete <QQII candidate bank; see prepare_discovery_bank.py')
    parser.add_argument('--output-dir',type=Path,required=True,help='separate directory for rediscovered witnesses and solver receipts')
    parser.add_argument('--delivery-root',type=Path,default=DELIVERY_ROOT)
    parser.add_argument('--frames',type=int,nargs='+',choices=range(1,6),default=list(range(1,6)))
    parser.add_argument('--seconds',type=float,default=60,help='LP time limit per frame')
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    if args.seconds<=0:parser.error('--seconds must be positive')
    results=[]
    for frame in args.frames:
        results.append(run(frame,args.bank,args.output_dir,args.delivery_root,args.seconds))
        (args.output_dir/'parity_lp_result.json').write_text(json.dumps(results,indent=2)+'\n')
