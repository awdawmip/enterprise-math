#!/usr/bin/env python3
"""PREFIX-593-R6 original 96-port BRC all-nine-root, all-horizon cubic proof.
Uses the pinned original PREFIX565_positive_marginal_certificate.
Exact rational graded upper bounds and mod-1000003 native-path lower ranks.
"""
from fractions import Fraction as F
from math import comb
import json
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN, PHASES, ACTIONS, ROOTS, ZERO_ROOT, edge
assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
assert len(ACTIONS)==6 and len(ROOTS)==9 and len(PHASES)==48
EXPS=[(a,b,d-a-b) for d in range(4) for a in range(d+1) for b in range(d-a+1)]
P=1000003
G=[int(i//2==42) for i in range(96)]
assert PHASES[42]==(3,-2,4)
class QBasis:
    def __init__(self): self.rows={}; self.vectors=[]
    def reduce(self,x):
        v=[F(t) for t in x]
        for j,r in sorted(self.rows.items()):
            if v[j]:
                c=v[j]
                for k in range(j,96):v[k]-=c*r[k]
        return v
    def add(self,x):
        v=self.reduce(x)
        j=next((i for i,t in enumerate(v) if t),None)
        if j is None:return False
        c=v[j];v=[t/c for t in v]
        self.rows[j]=v;self.vectors.append(v)
        return True
    def contains(self,x):return not any(self.reduce(x))
class ModBasis:
    def __init__(self):self.rows={}
    def add(self,x):
        v=[int(t)%P for t in x]
        for j,r in sorted(self.rows.items()):
            if v[j]:
                c=v[j]
                for k in range(j,96):v[k]=(v[k]-c*r[k])%P
        j=next((i for i,t in enumerate(v) if t),None)
        if j is None:return False
        c=pow(v[j],-1,P);v=[t*c%P for t in v]
        self.rows[j]=v;return True
    def __len__(self):return len(self.rows)

def analyze(root):
    E=[]
    for i in range(96):
        row=[]
        for a in ACTIONS:
            j,w=edge(i,a,root)
            t=192*w[6]-5*w[0]+w[1]-5*w[2]+w[3]+4*w[4]+4*w[5]
            row.append((j,t,w[0]+w[1],w[2]+w[3]))
        E.append(row)
    def op(alpha,v,mod=None):
        a,b,c=alpha
        vals=[sum(t**a*p0**b*p1**c*v[j] for j,t,p0,p1 in E[i]) for i in range(96)]
        return [t%mod for t in vals] if mod else vals
    W=[]
    for d in range(4):
        S=QBasis()
        if d==0:S.add([1]*96)
        else:
            for v in W[d-1].vectors:S.add(v)
            for alpha in EXPS:
                h=sum(alpha)
                if 0<h<=d:
                    for v in W[d-h].vectors:S.add(op(alpha,v))
        j=0
        while j<len(S.vectors):
            S.add(op((0,0,0),S.vectors[j]))
            j+=1
        W.append(S)
    for d in range(4):
        for alpha in EXPS:
            if d+sum(alpha)<=3:
                assert all(W[d+sum(alpha)].contains(op(alpha,v)) for v in W[d].vectors)
    upper=[len(s.vectors) for s in W]
    f={alpha:([1]*96 if sum(alpha)==0 else [0]*96) for alpha in EXPS}
    modspaces=[ModBasis() for d in range(4)]
    by_depth=[]
    for n in range(9):
        for alpha,v in f.items():
            for d in range(sum(alpha),4):
                modspaces[d].add(v)
        by_depth.append([len(s) for s in modspaces])
        if n==8:break
        future={}
        for alpha in EXPS:
            v=[0]*96
            for beta in EXPS:
                if all(beta[i]<=alpha[i] for i in range(3)):
                    gamma=tuple(alpha[i]-beta[i] for i in range(3))
                    c=comb(alpha[0],beta[0])*comb(alpha[1],beta[1])*comb(alpha[2],beta[2])
                    u=op(gamma,f[beta],P)
                    for i in range(96):v[i]=(v[i]+c*u[i])%P
            future[alpha]=v
        f=future
    lower=by_depth[-1]
    assert lower==upper,(root,upper,lower)
    in2=W[2].contains(G);in3=W[3].contains(G)
    assert in3
    assert in2==(upper[2]==33)
    if not in2:
        assert upper[3]==upper[2]+1 and W[2].reduce(G)==G
    return dict(root=list(root),graded_dimensions=upper,
                finite_modular_lower_ranks=lower,
                first_depth_full_rank=[next(n for n,v in enumerate(by_depth) if v[d]==upper[d]) for d in range(4)],
                g_in_quadratic=in2,g_in_cubic=in3,finite_depths_checked=[0,8])
result=[analyze(r) for r in ROOTS]
assert len(result)==9
assert all(r['graded_dimensions'][3]==33 for r in result)
out={'schema':'PREFIX593_R6_ALL_NINE_NATIVE_ROOTS_CUBIC_OBSERVER_V1',
     'status':'ALL_CHECKS_PASS','science_pin':SCIENCE_PIN,
     'native_ports':96,'original_labeled_actions':6,
     'modulus':P,'native_phase_indicator_ports':[84,85],
     'root_results':result,
     'theorem_scope':'all n>=0; nine allowed native frozen roots; cubic and lower T,P0,P1 moments; arbitrary initial port law',
     'formal_CLAIM_Result_Review':False}
print('ALL_CHECKS_PASS')
print(json.dumps(out,indent=2))
