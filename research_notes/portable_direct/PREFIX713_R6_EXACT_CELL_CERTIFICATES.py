#!/usr/bin/env python3
"""PREFIX-713 companion: certify four fine Gamma cells exactly; symmetric cells follow by exchangeability.
Run after PREFIX713_R6_EXACT_TWO_WITNESSES.py in the same directory."""
import contextlib,io,runpy,json
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from functools import lru_cache

folder=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    M=runpy.run_path(str(folder/'PREFIX713_R6_EXACT_TWO_WITNESSES.py'))
N=189;D=768;Z=2**(2*N-1);L=D**(N-1);R=L*L*Z
rows=M['rows']
old_mu,old_W=M['moments'](Q(3,20))
new_mu,new_W=M['moments'](Q(149,1000))
cells=((28,88),(34,91),(57,163),(74,138))
indices=sorted({v for i,j in cells for v in (i,i+1,j,j+1)})
T={}
for i in indices:
    a,b=i,D-i; ap=[1];bp=[1]
    for _ in range(N):
        ap.append(ap[-1]*a)
        bp.append(bp[-1]*b)
    T[i]=[sum(v*ap[k]*bp[n-k] for k,v in row.items())*D**(N-1-n)
          for n,row in enumerate(rows[:N])]
A={i:sum(v) for i,v in T.items()}
B={i:sum((n+1)*v for n,v in enumerate(ls)) for i,ls in T.items()}
C=[[comb(n+m,n)*2**(2*N-2-n-m) for m in range(N)] for n in range(N)]
@lru_cache(None)
def pair(i,j):
    a,b=T[i],T[j]
    cross0=sum(a[n]*sum(C[n][m]*b[m] for m in range(N)) for n in range(N))
    cross1=sum(a[n]*sum((n+m+1)*C[n][m]*b[m] for m in range(N)) for n in range(N))
    return Q((A[i]+A[j])*L*Z-cross0,R),Q(2*(B[i]+B[j])*L*Z-cross1,R)

def endpoint_margins(i,j,mu,w):
    ml=pair(i,j)[0]
    U=pair(i+1,j+1)[1]-ml**2
    return (w-U,w-mu/2-U+ml/2)

records=[]
for i,j in cells:
    a0,a2=endpoint_margins(i,j,old_mu,old_W)
    b0,b2=endpoint_margins(i,j,new_mu,new_W)
    assert min(a0,a2)<=0
    assert b0>0 and b2>0
    records.append({
      'lower_i':i,'lower_j':j,
      'old_pass':False,'new_pass':True,
      'new_L0_floor_micro':int(b0*10**6),
      'new_L_half_floor_micro':int(b2*10**6)})
assert len(records)==4
result_path=folder/'PREFIX713_R6_EXACT_TWO_WITNESS_RESULTS.json'
result=json.loads(result_path.read_text())
result['new_fine_cells_evaluated']=records
result['newly_certified_ordered_fine_beyond_PREFIX712_at_least']=8
result['PREFIX712_all_q_certified_fine']=137168
result['PREFIX713_all_q_certified_fine_at_least']=137176
result['PREFIX713_all_q_certified_fraction_lower']='17147/18432'
result['exact_fine_check']='ALL_CHECKS_PASS PREFIX713-FINE'
result_path.write_text(json.dumps(result,indent=2)+'\n')
print('ALL_CHECKS_PASS PREFIX713-FINE')
