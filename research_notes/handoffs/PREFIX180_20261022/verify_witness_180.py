"""Independent exact arithmetic witness verification, rebuilding the lattice from integers."""
from itertools import combinations_with_replacement
from pathlib import Path
import json
H=Path(__file__).resolve().parent

def delta(n):
    return [(a,b,c,n-a-b-c) for a in range(n+1) for b in range(n-a+1) for c in range(n-a-b+1)]
def support(x):return sum(v!=0 for v in x)
x=delta(8)
x1x2=[z for z in x if support(z)<=2 and z!=(4,4,0,0)]
x3=[z for z in x if support(z)==3]
x4=[z for z in x if support(z)==4]
assert len(x1x2)==45 and len(x3)==84 and len(x4)==35
Q0=[0,1,2,3,4,51,64,71,74]
W0=[0,4,8,10,11,14,19,22,25,26,29,34]
S=x1x2+[x3[i] for i in Q0]+[x4[i] for i in W0]
assert len(S)==len(set(S))==66
S2={tuple(a[j]+b[j] for j in range(4)) for a,b in combinations_with_replacement(S,2)}
T=set(delta(16))
assert len(T)==len(S2)==969 and S2==T
(H/'WITNESS_PREFIX180.json').write_text(json.dumps({'model':'four integer coordinates, exact Boolean support','Q0':Q0,'W0':W0,'R':x1x2,'Q_vectors':[x3[i] for i in Q0],'W_vectors':[x4[i] for i in W0],'sumset_targets':len(S2),'sumset_exact':True},sort_keys=True,indent=2)+'\n')
print('PREFIX180_WITNESS_INDEPENDENT_PASS cardinality=66 targets=969')
