"""R251 author-side exact checks of the declared positive-BRC affine packet.
SymPy certifies Laurent identities; integer DP propagates positive paths.
This is not an import of native enterprise_math.
"""
from collections import Counter
import json
import sympy as sp
x=sp.symbols('x', nonzero=True)
A=sp.Matrix([[0,1/x],[x,0]])
B=sp.diag(x,1/x)
C=sp.diag(1/x,x)
N=sp.zeros(6)
for src,dst,block in ((0,2,A+B),(1,0,A+B),(2,1,C),(2,2,B)):
    for i in range(2):
        for j in range(2): N[2*src+i,2*dst+j]+=block[i,j]
out={"schema":"EM_R251_EXACT_VERIFICATION_V1","source":"AUTHOR_SIDE_ONLY","status":"PASS","cases":{}}
for i in (0,1):
    alpha=sp.zeros(1,6);alpha[0,i]=1;alpha[0,2+i]=-1
    w=[alpha]
    for _ in range(4):w.append(sp.simplify(w[-1]*N))
    ranks=[sp.Matrix.vstack(*w[:k+1]).rank() for k in range(5)]
    assert ranks==[1,2,3,4,4]
    assert all(sp.cancel(z)==0 for z in (w[4]+w[2]-(x+1/x)*w[1]))
    minor=sp.factor(sp.Matrix.vstack(*w[:4])[:,[0,1,2,3]].det())
    assert minor!=0
    observed=[[sp.factor(sum(z[0,2*s+j] for s in range(3))) for j in range(2)] for z in w]
    assert observed[:3]==[[0,0]]*3 and all(v!=0 for v in observed[3])
    out['cases'][f'alpha_{i}']={'ranks':ranks,'minor':str(minor),
      'depth3':[str(z) for z in observed[3]],'depth4':[str(z) for z in observed[4]]}
lam=sp.symbols('lambda')
assert sp.cancel(N.charpoly(lam).as_expr()-lam**2*(lam-x-1/x)*(lam**3+lam-x-1/x))==0

# Exactly the six-axis affine subfamily (epsilon,k) where epsilon flips axes 1,2.
edges={0:((2,(-1,-1)),(2,(1,-1))),1:((0,(-1,-1)),(0,(1,-1))),
       2:((1,(1,1)),(2,(1,-1)))}
def then(f,g):return g[0]*f[0],g[0]*f[1]+g[1]
def advance(h):
    ans=Counter()
    for (control,effect),num in h.items():
        for target,new_effect in edges[control]:
            ans[(target,then(effect,new_effect))]+=num
    return ans
def observe(h):
    ans=Counter()
    for (_,effect),num in h.items():ans[effect]+=num
    return ans
record={}
for start in (0,1):
    h=Counter({(start,(1,0)):1});reads=[]
    for depth in range(11):
        obs=observe(h)
        assert sum(obs.values())==2**depth
        reads.append(obs)
        h=advance(h)
    record[start]=reads
assert all(record[0][i]==record[1][i] for i in range(3))
assert record[0][3]!=record[1][3]
cmp={str(k):record[0][3].get(k,0)-record[1][3].get(k,0)
     for k in set(record[0][3])|set(record[1][3])}
assert sorted(cmp.values())==[-1,-1,0,0,1,1]
out['direct_positive_dp']={'checked_depths':list(range(11)),
  'first_difference':3,'depth3_external_signed_comparison':cmp,
  'weight_per_branch':1,'multiplicity_per_branch':1}
if __name__=='__main__':print(json.dumps(out,sort_keys=True,indent=2))
