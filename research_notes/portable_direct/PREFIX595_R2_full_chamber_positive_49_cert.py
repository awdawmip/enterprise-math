#!/usr/bin/env python3
"""PREFIX-595-R2: exact native X6-BRC 96->49 nonnegative factor certificate.
Reconstruct native STARS/P/N/TARGET; integer only, no packages/network/floats.
"""
from itertools import product
from pathlib import Path
import json

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
P=tuple((a,p,t*k) for a in range(4) for k in STARS[a] for t in (-1,1) for p in near(a,t*k))
IX={s:i for i,s in enumerate(P)}
def successors(i):
    a,p,c=P[i]
    b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
    return tuple(IX[s] for s in ([(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)]))
N=tuple(successors(i) for i in range(48))
G=IX[(0,1,-3)]
axis=tuple(abs(p[2])-1 for p in P)
assert len(P)==48 and len(set(P))==48
assert G not in N[G] and sum(G in z for z in N)==3

# 49x96 fixed positive encoder: 47 ordinary phase-bit sums + two gate bits.
key=[(j,None) for j in range(48) if j!=G]+[(G,0),(G,1)]
assert len(key)==49
C=[[0]*96 for _ in range(49)]
for m,(j,bit) in enumerate(key):
    for u in ((0,1) if bit is None else (bit,)):
        C[m][2*j+u]=1
assert all(sum(C[m]) in (1,2) for m in range(49))
assert all(sum(C[m][i] for m in range(49))==1 for i in range(96))

def native_generators():
    A=[[[0]*96 for _ in range(96)] for _ in range(7)]
    for i in range(48):
        k=axis[i]
        for j in N[i]:
            for u,v in product((0,1),repeat=2):
                label=6 if (j==G and u==v==1) else k
                if label==6:assert k==0
                A[label][2*i+u][2*j+v]+=1
    return A
A=native_generators()
assert [sum(sum(row) for row in M) for M in A]==[93,96,96,96,96,96,3]

# Each original ordinary bit-pair has identical columns in every generator.
B=[[[0]*49 for _ in range(96)] for _ in range(7)]
for k in range(7):
    for m,(j,bit) in enumerate(key):
        col=2*j+(0 if bit is None else bit)
        for i in range(96):
            B[k][i][m]=A[k][i][col]
        if bit is None:
            assert all(A[k][i][2*j]==A[k][i][2*j+1] for i in range(96))
    for i in range(96):
        for j in range(96):
            assert A[k][i][j]==sum(B[k][i][m]*C[m][j] for m in range(49))

# All 49-state update generator coefficients remain nonnegative integers.
M=[[[sum(C[p][i]*B[k][i][j] for i in range(96)) for j in range(49)]
      for p in range(49)] for k in range(7)]
assert all(v>=0 for row in C for v in row)
assert all(v>=0 for Bk in B for row in Bk for v in row)
assert all(v>=0 for Mk in M for row in Mk for v in row)
assert all(sum(C[p][i]*A[k][i][j] for i in range(96))==
           sum(M[k][p][m]*C[m][j] for m in range(49))
           for k in range(7) for p in range(49) for j in range(96))

def matvec(M,r):
    return [sum(a*b for a,b in zip(row,r)) for row in M]
def eval_weighted(generators,x,z):
    weights=list(x)+[x[0]*z]
    rows=len(generators[0]);cols=len(generators[0][0])
    return [[sum(weights[k]*generators[k][i][j] for k in range(7))
             for j in range(cols)] for i in range(rows)]
def step96(r,x,z):
    return matvec(eval_weighted(A,x,z),r)
def step49(w,x,z):
    return matvec(eval_weighted(M,x,z),w)
def read96(w,x,z):
    return matvec(eval_weighted(B,x,z),w)

inputs=[[int(i==j) for i in range(96)] for j in range(96)]+[
    [1]*96,[int(i%9==0) for i in range(96)],[(7*i+3)%11 for i in range(96)]]
sequences=[
    [((1,1,1,1,1,1),0),((2,3,5,7,11,13),1),((1,2,1,2,1,2),5),((3,0,4,0,5,0),0)],
    [((0,1,0,1,0,1),0),((1,0,1,0,1,0),2),((3,4,0,6,0,7),0),((1,1,1,1,1,1),1)],
    [((1,2,3,4,5,6),0),((1,2,3,4,5,6),0),((1,2,3,4,5,6),0),((1,2,3,4,5,6),0)],
]
checks=0
for r0 in inputs:
    for sequence in sequences:
        r=r0[:];w=matvec(C,r)
        for x,z in sequence:
            r=step96(r,x,z)
            assert read96(w,x,z)==r
            w=step49(w,x,z)
            assert w==matvec(C,r)
            assert min(w)>=0
            checks+=1
assert checks==1188

result={
    'schema':'PREFIX595_R2_ALL_NONNEGATIVE_GATE_POSITIVE_49_V1',
    'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'source_basis':'Frozen STARS/P/N/TARGET, PREFIX589_R2_dual_carrier_certificate.py, blob cf64036c1c7cb95eb6ec0bdc9151082432cb0291',
    'native_ports':96,'phases':48,'labelled_actions':576,'gate_target_phase':G,
    'encoder_rows':49,'decoder_rows':96,
    'factorization':'A_k=B_k*C, M_k=C*B_k for all 7 native labels',
    'domain':'all x1..x6>=0 and z>=0, arbitrary finite nonstationary sequences',
    'rank_generic':'49 if all axes nonzero and z!=1; PREFIX593 rank proof',
    'rank_unit_gate':'48 if all axes nonzero and z=1',
    'original_nnz_by_label':[sum(sum(row) for row in Ak) for Ak in A],
    'decoder_nnz_by_label':[sum(sum(row) for row in Bk) for Bk in B],
    'update_nnz_by_label':[sum(sum(row) for row in Mk) for Mk in M],
    'coeff_A_eq_BC_checked':7*96*96,
    'coeff_CA_eq_MC_checked':7*49*96,
    'full_port_and_state_exact_step_checks':checks,
    'tested_singleton_original_endpoints':96,
    'gate_values_tested':[0,1,2,5],
    'status':'ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED'}
Path(__file__).with_name('PREFIX595_R2_full_chamber_positive_49_results.json').write_text(
    json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(result['status'],checks)
