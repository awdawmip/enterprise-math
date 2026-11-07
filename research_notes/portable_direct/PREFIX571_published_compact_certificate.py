"""PREFIX571 compact exact graph/kernel certificate for frozen native X6-BRC.
Imports the published PREFIX565/566 action model. Run from their directory.
For positive-factor scan separately execute PREFIX570_compact_certificate.py.
"""
from collections import Counter, deque
import json
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN, ZERO_ROOT, ROOTS
from PREFIX566_gate_quotient_certificate import (marginal_gate_rows,
    weighted_quotient, native_involution, symmetric_to_uvz)

PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'

def certify():
    assert SCIENCE_PIN==PIN
    native=marginal_gate_rows(ZERO_ROOT)
    assert all(marginal_gate_rows(r)==native for r in ROOTS)
    ids,Q,growth=weighted_quotient(native)
    assert len(native)==96 and len(Q)==37
    swap=native_involution()
    fixed=sorted({ids[i] for i in range(96) if swap[i]==i})
    assert len(fixed)==11 and sum(swap[i]==i for i in range(96))==32
    U=[sum(n for (j,x,y,g),n in row.items() if g) for row in Q]
    assert [(i,n) for i,n in enumerate(U) if n]==[(4,1),(15,1),(17,1)]
    assert all(j==5 and x==y==0 for row in Q for (j,x,y,g),n in row.items() if g)
    adjacency=[set() for _ in Q]
    for i,row in enumerate(Q):
        for (j,x,y,g),n in row.items():
            if not g:adjacency[i].add(j);adjacency[j].add(i)
    colors=[None]*len(Q)
    for root in range(len(Q)):
        if colors[root] is not None:continue
        colors[root]=0;queue=deque([root])
        while queue:
            i=queue.popleft()
            for j in adjacency[i]:
                if colors[j] is None:colors[j]=colors[i]^1;queue.append(j)
                else:assert colors[j]==(colors[i]^1)
    assert all(colors[i]!=colors[5] for i in (4,15,17))
    A=[Counter({(0,0):n}) if n else Counter() for n in U]
    K=[]
    for d in range(7):
        p=A[5]
        assert all(p.get((y,x),0)==n for (x,y),n in p.items())
        k=symmetric_to_uvz({(x,y,0):n for (x,y),n in p.items()})
        K.append(k)
        if d==6:break
        nxt=[]
        for row in Q:
            out=Counter()
            for (j,x,y,g),multiplicity in row.items():
                if not g:
                    for (a,b),n in A[j].items():out[a+x,b+y]+=n*multiplicity
            nxt.append(+out)
        A=nxt
    assert all(not K[d] for d in (0,1,2,4,6))
    assert K[3]=={(0,0,0):4,(1,0,0):8}
    assert K[5]=={(2,0,0):80,(0,1,0):128}
    return dict(status='ALL_CHECKS_PASS',science_pin=PIN,
       nine_root_native_edge_checks=len(ROOTS)*96*6,
       quotient_states=len(Q),fixed_classes=fixed,
       ungated_graph_bipartite=True,gate_target=5,
       gate_sources=[4,15,17],kernel_coeff_t3='4+8u',
       kernel_coeff_t5='80u^2+128v',
       proof_use='c(t)=rho+t^2 gamma(t); exact full-length parity of K; '
                 'symbolic Newton theorem and diagonal sign lemma use prior PREFIX570 factor scan')

if __name__=='__main__':print(json.dumps(certify(),ensure_ascii=False,indent=2))
