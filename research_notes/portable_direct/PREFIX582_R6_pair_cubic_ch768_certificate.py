#!/usr/bin/env python3
"""PREFIX582-R6: exact 768-depth Cayley-Hamilton zero-series certificate."""
from collections import Counter
from PREFIX565_positive_marginal_certificate import edge, ACTIONS, ZERO_ROOT, SCIENCE_PIN
import json
import time

assert SCIENCE_PIN=="f42f2906d77f24085c123f3ccfe9667d41caa96d"
N=96
LIMIT=8*N
edges=[]
for i in range(N):
    row=[]
    for a in ACTIONS:
        j,w=edge(i,a,ZERO_ROOT)
        h=64*w[6]-(3*w[0]+w[1]+3*w[2]+w[3])
        P=(w[0]+w[1],w[2]+w[3],w[4]+w[5])
        assert sum(P)==1
        row.append((j,h,P))
    edges.append(row)
assert Counter(j for row in edges for j,h,p in row)==Counter({i:6 for i in range(N)})
assert sum(h for row in edges for j,h,p in row)==-N*6
assert [sum(p[k] for row in edges for j,h,p in row) for k in range(3)]==[N*2]*3
subsets=[[(s,m^s) for s in range(8) if s&m==s] for m in range(8)]
def witness_test(a,b):
    V=[[0]*N for _ in range(8)]
    V[0]=[1]*N
    for n in range(LIMIT):
        S=[sum(row) for row in V]
        D=N*6**n
        assert S[0]==D,(n,"mass")
        q=9*S[7]-3*n*(S[3]+S[5])+9*n*S[6]-2*n**3*D
        assert q==0,(a,b,n,q)
        if n==LIMIT-1:
            break
        W=[[0]*N for _ in range(8)]
        for i,row in enumerate(edges):
            for j,h,p in row:
                e=(h,p[a],p[b])
                prod=[1,e[0],e[1],e[0]*e[1],e[2],e[0]*e[2],e[1]*e[2],e[0]*e[1]*e[2]]
                for m in range(8):
                    Wm=W[m]
                    for s,rem in subsets[m]:
                        v=V[s][i]
                        if v:
                            Wm[j]+=prod[rem]*v
        V=W
    return LIMIT
if __name__=="__main__":
    started=time.time()
    c00=witness_test(0,0)
    c12=witness_test(1,2)
    assert c00==c12==768
    print("ALL_CHECKS_PASS")
    print(json.dumps({
        "status":"ALL_CHECKS_PASS",
        "states":96,"labeled_actions":576,
        "science_pin":SCIENCE_PIN,
        "operator_dimension":768,
        "CH_integer_zero_checks":c00+c12,
        "witnesses":{"Q_00":c00,"Q_12":c12},
        "theorem":"C(n)=q_n*[[0,1,-1],[1,-1,0],[-1,0,1]] for all n>=0",
        "proof_kind":"Cayley-Hamilton plus exhaustive exact-integer base checks",
        "initial":"uniform 96 native ports",
        "root":[0,0,0,0,0,0],
        "elapsed_seconds":round(time.time()-started,3)
    },indent=2))
