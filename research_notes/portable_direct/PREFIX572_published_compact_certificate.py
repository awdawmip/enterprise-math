#!/usr/bin/env python3
"""PREFIX-572 exact 14-pair BRC gate recurrence; pinned four-STAR 96-port source.
Dependencies: published PREFIX565 and PREFIX566 files, SymPy. Exact integers only.
"""
import json
from collections import Counter,deque
import sympy as S
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN,ZERO_ROOT,ROOTS
from PREFIX566_gate_quotient_certificate import marginal_gate_rows,weighted_quotient,native_involution
PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
x,y,z,L,u,v=S.symbols('x y z lambda u v')
def check():
    assert SCIENCE_PIN==PIN
    native=marginal_gate_rows(ZERO_ROOT)
    assert len(native)==96 and all(marginal_gate_rows(r)==native for r in ROOTS)
    ids,Q,growth=weighted_quotient(native)
    assert len(Q)==37 and growth==[1,4,13,21,33,37]
    for i,row in enumerate(native):
        t=Counter()
        for (j,a,b,g),n in row.items():t[ids[j],a,b,g]+=n
        assert t==Q[ids[i]]
    sig=native_involution();induced={}
    for i in range(96):
        if ids[i] in induced:assert induced[ids[i]]==ids[sig[i]]
        induced[ids[i]]=ids[sig[i]]
    for i,row in enumerate(Q):
        assert Q[induced[i]]==Counter({(induced[j],b,a,g):n for (j,a,b,g),n in row.items()})
    adj=[set() for _ in Q]
    for i,row in enumerate(Q):
        for (j,a,b,g),n in row.items():adj[i].add(j);adj[j].add(i)
    color=[None]*37
    for i in range(37):
        if color[i] is not None:continue
        color[i]=0;todo=deque([i])
        while todo:
            a=todo.popleft()
            for b in adj[a]:
                if color[b] is None:color[b]=color[a]^1;todo.append(b)
                else:assert color[b]!=color[a]
    left=[i for i in range(37) if color[i]==0]
    right=[i for i in range(37) if color[i]==1]
    assert (len(left),len(right))==(17,20)
    li={n:i for i,n in enumerate(left)};ri={n:i for i,n in enumerate(right)}
    A=S.zeros(17,20);B=S.zeros(20,17);gates=Counter()
    for i,row in enumerate(Q):
        for (j,a,b,g),n in row.items():
            term=n*x**a*y**b*z**g
            if color[i]==0:A[li[i],ri[j]]+=term
            else:B[ri[i],li[j]]+=term
            if g:assert j==5 and a==b==0;gates[i]+=n
    assert gates==Counter({4:1,15:1,17:1})
    chi=(A*B).charpoly(L).as_expr()
    E=0
    for (p,g),h in S.Poly(chi,L,z).terms():
        hh,rem,m=S.symmetrize(h,[x,y],formal=True)
        assert rem==0
        E+=S.expand(hh.subs({m[0][0]:u,m[1][0]:v}))*L**p*z**g
    E=S.expand(E)
    assert S.Poly(E,z).degree()==1 and S.Poly(E,L).degree()==17
    cubic=L**3+4*L**2-(32*u+16*v)*L+192*v
    q,rem=S.div(S.Poly(E,L),S.Poly(cubic,L))
    assert rem.is_zero and q.degree()==14 and q.LC()==1
    assert S.Poly(q.as_expr(),z).degree()==1
    # N_z Q14_z(N_z^2) 1=0: exact coefficientwise evaluation in Z[x,y,z]^37.
    coeff=[{m:int(w) for m,w in S.Poly(S.expand(q.nth(14-j).subs({u:x+y,v:x*y})),x,y,z).terms()}
           for j in range(15)]
    f=[{(0,0,0):1} for _ in Q];odd=[]
    for d in range(30):
        if d%2:odd.append(f)
        next_f=[]
        for row in Q:
            t=Counter()
            for (j,a,b,g),mult in row.items():
                for (xx,yy,gg),w in f[j].items():t[xx+a,yy+b,gg+g]+=mult*w
            next_f.append({m:w for m,w in t.items() if w})
        f=next_f
    assert len(odd)==15
    total=[Counter() for _ in Q]
    for j in range(15):
        for i in range(37):
            for (a,b,g),n in coeff[j].items():
                for (xx,yy,gg),w in odd[14-j][i].items():total[i][xx+a,yy+b,gg+g]+=n*w
    positions=sum(len(row) for row in total)
    assert all(all(w==0 for w in row.values()) for row in total)
    return dict(status='ALL_CHECKS_PASS',scientific_pin=PIN,
        native_port_count=96,roots=len(ROOTS),weighted_quotient_classes=37,
        bipartition=[17,20],gate_rank_one_sources=[4,15,17],
        gate_affine_characteristic=True,symmetric_uv=True,
        characteristic_terms=len(S.Poly(E,L,u,v,z).terms()),
        cubic_factor='lambda^3+4lambda^2-(32u+16v)lambda+192v',
        reduced_factor_degree=14,exact_annihilator_zero=True,
        zero_coeff_positions=positions,
        full_depth_recurrence='all classes, every d>=29, all gate counts, 14 two-step lags',
        complete_Q14=str(q.as_expr()))
if __name__=='__main__':print(json.dumps(check(),ensure_ascii=False,indent=2))
