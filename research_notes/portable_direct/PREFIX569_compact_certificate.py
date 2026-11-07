"""PREFIX569: exact certificate for all-k, 128-excess e-positive gate bands.
Run alongside the published PREFIX565 and PREFIX566 modules; stdlib only.
Pinned science: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import Counter
import json
from PREFIX565_positive_marginal_certificate import ZERO_ROOT, ROOTS, ACTIONS, edge, clean, SCIENCE_PIN
from PREFIX566_gate_quotient_certificate import (marginal_gate_rows, weighted_quotient,
                                                 native_involution, symmetric_to_uvz)

def step(vec, Q):
    out=[]
    for row in Q:
        r=Counter()
        for (j,x,y,g),m in row.items():
            if g:continue
            for (a,b),v in vec[j].items():r[a+x,b+y]+=m*v
        out.append(clean(r))
    return out

def e_basis(p):
    assert all(p.get((b,a),0)==v for (a,b),v in p.items())
    return symmetric_to_uvz({(a,b,0):v for (a,b),v in p.items()})

def certify(excess=128):
    assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
    raw=marginal_gate_rows(ZERO_ROOT)
    assert all(marginal_gate_rows(root)==raw for root in ROOTS)
    ids,Q,growth=weighted_quotient(raw)
    assert len(Q)==37
    for i,row in enumerate(raw):
        proj=Counter()
        for (j,x,y,g),m in row.items():proj[ids[j],x,y,g]+=m
        assert proj==Q[ids[i]]
    lift=native_involution()
    fixed=sorted({ids[i] for i,j in enumerate(lift) if i==j})
    assert len(fixed)==11 and sum(i==j for i,j in enumerate(lift))==32
    for i in range(96):
        for action in ACTIONS:
            j,w=edge(i,action,ZERO_ROOT)
            swapped=(lift[j],w[:4]+(w[5],w[4])+w[6:])
            assert sum(edge(lift[i],a,ZERO_ROOT)==swapped for a in ACTIONS)==1
    targets={j for row in Q for (j,x,y,g),m in row.items() if g}
    assert targets=={5}
    assert all(x==y==0 for row in Q for (j,x,y,g),m in row.items() if g)
    U=[sum(m for (j,x,y,g),m in row.items() if g) for row in Q]
    assert [(i,v) for i,v in enumerate(U) if v]==[(4,1),(15,1),(17,1)]
    A=[{(0,0):v} if v else {} for v in U]
    B=[{(0,0):1} for _ in Q]
    first={i:None for i in fixed};counts={'A':0,'K':0,'B':0};lead=None
    for n in range(excess+5):
        for i in fixed:
            e=e_basis(A[i]);counts['A']+=len(e)
            assert all(v>=0 for v in e.values())
            if e and first[i] is None:first[i]=n
        ke=e_basis(A[5]);be=e_basis(B[5]);counts['K']+=len(ke);counts['B']+=len(be)
        assert all(v>=0 for v in ke.values()) and all(v>=0 for v in be.values())
        if n==3:lead=ke
        if n<excess+4:A,B=step(A,Q),step(B,Q)
    assert lead=={(0,0,0):4,(1,0,0):8}
    assert max(first.values())==4 and min(first.values())==0
    # Exact formal resolvent identity yields all-k claim from these finite factors.
    return {'status':'ALL_CHECKS_PASS','science_pin':SCIENCE_PIN,
       'fixed_classes':fixed,'minimal_gate_depths':{str(i):first[i]+1 for i in fixed},
       'positive_excess_s': [0,excess],'gate_count':'ALL_INTEGERS_k>=1',
       'factor_scan_depth':[0,excess+4],'positive_e_basis_positions':counts,
       'gate_target':5,'gate_sources':[i for i,v in enumerate(U) if v],
       'native_projected_edges':len(ROOTS)*96*6,'native_involution_edges':96*6,
       'theorem':'[z^k t^(delta_i+4(k-1)+s)]F_i in N[u,v] for every fixed port i, k>=1, 0<=s<=128',
       'scope':'q1..q4=1; x=q5,y=q6; gate z; roots r5=r6=0; frozen four-STAR kernel'}

if __name__=='__main__':print(json.dumps(certify(),indent=2,ensure_ascii=False))
