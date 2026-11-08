#!/usr/bin/env python3
"""Exact native X6-BRC zero-weight spectral boundary certificate (PREFIX-599).
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Reconstructs the 48 native phases (original 96 ports, 576 typed actions).
All arithmetic is exact SymPy integer/polynomial arithmetic.
"""
import json
from pathlib import Path
import sympy as sp

z, t = sp.symbols('z t')
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STAR[a] if k!=abs(c))
phases=tuple((a,p,sgn*k) for a in range(4) for k in STAR[a]
             for sgn in (-1,1) for p in near(a,sgn*k))
idx={q:i for i,q in enumerate(phases)}
def successor(i):
    a,p,c=phases[i]
    b=next(k for k in range(4) if k!=a and abs(c) in STAR[k])
    return tuple(idx[v] for v in
      ([(a,c,q) for q in near(a,c) if q!=p] + [(b,c,q) for q in near(b,c)]))
N=tuple(successor(i) for i in range(48))
axis=tuple(abs(q[2])-1 for q in phases)
g=idx[(0,1,-3)]
assert len(phases)==48 and len(idx)==48 and g==4
assert all(len(ns)==3 for ns in N)
assert sum(g in ns for ns in N)==3
assert sum(a<4 for a in axis)==32

def Q0(gate):
    Q=sp.zeros(48)
    for i,ns in enumerate(N):
        if axis[i]>=4:
            continue
        for j in ns:
            Q[i,j]=(1 if i==g else (3+gate if j==g else 2))
    return Q

M=Q0(z)
I=sp.eye(48)
M2=M*M; M4=M2*M2; M6=M4*M2; M8=M4*M4; M10=M8*M2
T=M10-(4*z+28)*M6+16*(4*z+12)*M2
assert all(sp.expand(a)==0 for a in T), 'universal polynomial annihilator'

C_expected=lambda gate: sp.Poly(t**32*(t**4-16)**3*(t**4-4*gate-12),t)
for gate in (0,1):
    assert sp.Poly(Q0(gate).charpoly(t).as_expr(),t)==C_expected(gate)

rows=(0,1,2,3,4,5,6,7,12,13,14,15,16,17,18,19,
      24,25,26,27,28,29,30,31,36,37,38,39,40,41,42,43)
cols=(0,2,4,6,8,9,10,11,12,14,16,18,20,21,22,23,
      24,26,28,30,32,33,34,35,36,38,40,42,44,45,46,47)
minor=sp.factor(M.extract(rows,cols).det(method='domain-ge'))
assert sp.expand(minor-sp.Integer(7044820107264)*(z+3))==0
assert Q0(-3).rank()==31

Z1=Q0(1); Z12=Z1*Z1; Z14=Z12*Z12
assert (Z12*(Z14-16*I)).is_zero_matrix
assert Z1.rank()==32

Zm=Q0(-3); Zm2=Zm*Zm; Zm4=Zm2*Zm2
lower=Zm4*(Zm4-16*I)
assert lower[4,8]==-128
assert (Zm*lower).is_zero_matrix

for gate in (0,2):
    A=Q0(gate)
    assert A.rank()==32
    assert all(sp.expand(a)==0 for a in
               A**10-(4*gate+28)*A**6+16*(4*gate+12)*A**2)

result={
 "title":"PREFIX-599 exact zero-axis-weight classification",
 "input_science_commit":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "axis_weights":[1,1,1,1,0,0], "phase_count":48,
 "original_ports":96, "typed_actions":576, "gate_target_phase":g,
 "charpoly":"t^32*(t^4-16)^3*(t^4-4*z-12)",
 "all_z_annihilator":"t^2*(t^4-16)*(t^4-4*z-12)",
 "sharp_degrees":{"z=1":6,"z=-3":9,"all_other_real_z":10},
 "nonnegative_gate":{"z=1":6,"z>=0_and_z!=1":10},
 "rank":{"z!=-3":32,"z=-3":31},
 "rank_minor":{"rows":rows,"cols":cols,
               "det":"7044820107264*(z+3)"},
 "special":{"z=1_annihilator":"t^2*(t^4-16)",
            "z=-3_annihilator":"t^5*(t^4-16)",
            "z=-3_lower_witness":
            "[Q(-3)^4*(Q(-3)^4-16I)]_(4,8)=-128"},
 "verification":"exact SymPy arithmetic, two charpolys and affine interpolation, full symbolic annihilator, minor and rank",
 "assertions_passed":True,
 "mathematical_status":"AUTHOR_PROVED_UNREVIEWED"
}
Path(__file__).with_name('PREFIX599_R2_zero_weight_minpoly_results.json').write_text(
    json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,ensure_ascii=False,indent=2))
