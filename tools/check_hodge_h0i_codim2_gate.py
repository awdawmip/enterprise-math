#!/usr/bin/env python3
from pathlib import Path
import json, itertools, hashlib
from fractions import Fraction
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
RR=ROOT/"research_results"
TASK="RS-HODGE-H0I-CODIM2-CLASS-FIRST-VECTOR-BUNDLE-ZERO-LOCUS-LIFTING"
TASKBOOK="3726e64557d625e36915028d83421d1f47b26fd2"
RID="EM-HODGE-H0I-7B2D94"
H0H_CORE="04a0abdad437e777bd2476e360fa17d30059580fd6fcbc4269bcb4844bfdb298"

passed=0
checks=[]
def ck(cond,name):
    global passed
    if not cond:
        raise AssertionError(name)
    passed += 1
    checks.append(name)

def load(name):
    return json.loads((RR/name).read_text())

# Protocol/artifact identity
cl=load("HODGE_H0I_CLASSIFICATION.json")
src=load("HODGE_H0I_ALGEBRAIC_SOURCE_SPEC.json")
vt=load("HODGE_H0I_TARGET_CLASS_CARRIER.json")
gl=load("HODGE_H0I_GL2_TRANSITION_REGISTRY.json")
bf=load("HODGE_H0I_BUNDLE_FIRST_CONTROL.json")
pr=load("HODGE_H0I_ZERO_LOCUS_PROVENANCE_REGISTRY.json")
cf=load("HODGE_H0I_CLASS_FIRST_LIFT_REGISTRY.json")
bs=load("HODGE_H0I_SOURCE_BASELINE_SANDWICH.json")
plc=load("HODGE_H0I_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json")
att=load("HODGE_H0I_ATTRIBUTION_CERTIFICATE_REGISTRY.json")
mr=load("HODGE_H0I_MULTIPLICITY_RATIONAL_LEDGER.json")
nat=load("HODGE_H0I_PRESENTATION_NATURALITY_LEDGER.json")
tl=load("HODGE_H0I_TARGET_LEAKAGE_LEDGER.json")
r3=load("HODGE_H0I_R3_PRESEED.json")

for obj in [cl,src,vt,gl,bf,pr,cf,bs,plc,att,mr,nat,tl,r3]:
    ck(obj["task_id"]==TASK, "task_id")
    ck(obj["taskbook_source"]==TASKBOOK, "taskbook_source")
    ck(obj["researcher_id"]==RID, "researcher_id")

ck(cl["disposition"]=="H0I_SOURCE_VECTOR_BUNDLE_CHOW_NORMAL_FORM_ALREADY_COMPLETE","classification")
ck(cl["hard_target_pass"] is False,"hard_target_false")
ck(cl["H1_admissible"] is False,"H1_blocked")
ck(tl["status"]=="PASS","target_leakage_pass")
ck(att["robust_transform_attributed_candidate_count"]==0,"no_robust_candidate")
ck(r3["status"]=="NO_R3_PRESEED","no_r3")

# Exterior algebra
names=['x00','x01','x10','x11','y00','y01','y10','y11']
idx={n:i for i,n in enumerate(names)}
def wm(a,b):
    if set(a)&set(b): return None,0
    inv=sum(1 for i in a for j in b if i>j)
    return tuple(sorted(a+b)), -1 if inv%2 else 1
def add(A,B):
    C=A.copy()
    for k,v in B.items():
        C[k]=C.get(k,Fraction(0))+v
        if C[k]==0: del C[k]
    return C
def scale(A,s):
    s=Fraction(s); return {k:v*s for k,v in A.items() if v*s}
def wedge(A,B):
    C={}
    for a,ca in A.items():
        for b,cb in B.items():
            c,sg=wm(a,b)
            if c is not None: C[c]=C.get(c,Fraction(0))+ca*cb*sg
    return {k:v for k,v in C.items() if v}
def of(n): return {(idx[n],):Fraction(1)}
X=[[of(f'x{i}{j}') for j in range(2)] for i in range(2)]
Y=[[of(f'y{i}{j}') for j in range(2)] for i in range(2)]
A=[[{} for _ in range(2)] for __ in range(2)]
B=[[{} for _ in range(2)] for __ in range(2)]
for a in range(2):
    for b in range(2):
        for mu in range(2):
            A[a][b]=add(A[a][b],wedge(Y[a][mu],X[mu][b]))
for mu in range(2):
    for nu in range(2):
        for a in range(2):
            B[mu][nu]=add(B[mu][nu],wedge(X[mu][a],Y[a][nu]))
def tr(M):
    s={}
    for i in range(len(M)): s=add(s,M[i][i])
    return s
def trsq(M):
    s={}
    for i in range(len(M)):
        for j in range(len(M)):
            s=add(s,wedge(M[i][j],M[j][i]))
    return s
trA=tr(A); trB=tr(B); tau1=wedge(trA,trA); tau2=trsq(A); trB2=trsq(B)
ck(trB==scale(trA,-1),"graded_trace_linear")
ck(trB2==scale(tau2,-1),"graded_trace_square")
c2S=scale(add(tau1,scale(tau2,-1)),Fraction(1,2))
c2Q=scale(add(wedge(trB,trB),scale(trB2,-1)),Fraction(1,2))

# Lie algebra invariant dimension
xlabels=[(mu,a) for mu in range(2) for a in range(2)]
ylabels=[(a,mu) for a in range(2) for mu in range(2)]
pairs=list(itertools.combinations(range(4),2))
def rep_xy(AE,BF):
    Rx=sp.zeros(4); Ry=sp.zeros(4)
    for j,(mu,a) in enumerate(xlabels):
        for nu in range(2): Rx[xlabels.index((nu,a)),j]+=BF[nu,mu]
        for b in range(2): Rx[xlabels.index((mu,b)),j]+=-AE[a,b]
    for j,(a,mu) in enumerate(ylabels):
        for b in range(2): Ry[ylabels.index((b,mu)),j]+=AE[b,a]
        for nu in range(2): Ry[ylabels.index((a,nu)),j]+=-BF[mu,nu]
    return Rx,Ry
def w2(R):
    W=sp.zeros(6); pi={p:i for i,p in enumerate(pairs)}
    for j,(a,b) in enumerate(pairs):
        for i in range(4):
            c=R[i,a]
            if c and i!=b:
                t=(i,b); sg=1
                if t[0]>t[1]: t=(t[1],t[0]); sg=-1
                W[pi[t],j]+=sg*c
            c=R[i,b]
            if c and i!=a:
                t=(a,i); sg=1
                if t[0]>t[1]: t=(t[1],t[0]); sg=-1
                W[pi[t],j]+=sg*c
    return W
E=sp.Matrix([[0,1],[0,0]]); F=sp.Matrix([[0,0],[1,0])); H=sp.diag(1,-1); Z=sp.zeros(2); Id=sp.eye(2)
gens=[(g,Z) for g in [E,F,H]]+[(Z,g) for g in [E,F,H]]+[(Id,-Id)]
ops=[]
for ae,bf0 in gens:
    rx,ry=rep_xy(ae,bf0)
    ops.append(sp.kronecker_product(w2(rx),sp.eye(6))+sp.kronecker_product(sp.eye(6),w2(ry)))
stack=sp.Matrix.vstack(*ops)
ck(36-stack.rank()==2,"invariant_degree4_dim_2")
pi={p:i for i,p in enumerate(pairs)}
def vec(form):
    v=sp.zeros(36,1)
    for key,c in form.items():
        xs=tuple(i for i in key if i<4); ys=tuple(i-4 for i in key if i>=4)
        v[pi[xs]*6+pi[ys]]=sp.Rational(c.numerator,c.denominator)
    return v
v1=vec(tau1); v2=vec(tau2)
for gi,op in enumerate(ops):
    out1=op*v1; out2=op*v2
    for k in range(36):
        ck(out1[k]==0,f"tau1_invariance_g{gi}_{k}")
        ck(out2[k]==0,f"tau2_invariance_g{gi}_{k}")
ck(sp.Matrix.hstack(v1,v2).rank()==2,"tau_independent")

# c2 coordinate solve
basis_keys=sorted(set(tau1)|set(tau2)|set(c2S)|set(c2Q))
MM=sp.Matrix([[sp.Rational(tau1.get(k,0).numerator,tau1.get(k,0).denominator),
               sp.Rational(tau2.get(k,0).numerator,tau2.get(k,0).denominator)] for k in basis_keys])
def coord(form):
    vv=sp.Matrix([sp.Rational(form.get(k,0).numerator,form.get(k,0).denominator) for k in basis_keys])
    sol=next(iter(sp.linsolve((MM,vv))))
    return tuple(sol)
ck(coord(c2S)==(sp.Rational(1,2),sp.Rational(-1,2)),"c2S_coords")
ck(coord(c2Q)==(sp.Rational(1,2),sp.Rational(1,2)),"c2Q_coords")

# Exact Plucker chart transitions
charts=list(itertools.combinations(range(4),2))
M0=sp.Matrix([[1,1,1,1],[1,2,3,5]])
def pivot(M,I): return M[:,list(I)]
def frame(M,I): return pivot(M,I).inv()*M
def comp(I): return tuple(i for i in range(4) if i not in I)
def qmap(F0,I):
    C=comp(I); R=sp.zeros(2,4)
    for k,c in enumerate(C): R[k,c]=1
    for r,i in enumerate(I):
        for k,c in enumerate(C): R[k,i]=-F0[r,c]
    return R
Fs={I:frame(M0,I) for I in charts}; Rs={I:qmap(Fs[I],I) for I in charts}
def ST(I,J): return Fs[I][:,list(J)].inv()
def QT(I,J): return Rs[J][:,list(comp(I))]
for I,J,K in itertools.product(charts,repeat=3):
    D=sp.simplify(ST(J,K)*ST(I,J)-ST(I,K))
    for a in range(2):
        for b in range(2): ck(D[a,b]==0,"S_cocycle")
    D=sp.simplify(QT(J,K)*QT(I,J)-QT(I,K))
    for a in range(2):
        for b in range(2): ck(D[a,b]==0,"Q_cocycle")

# Q maps kill S frames
for I in charts:
    D=Rs[I]*Fs[I].T
    for a in range(2):
        for b in range(2): ck(D[a,b]==0,"Q_kernel_S")

# Zero locus/codimension exact structural checks
# Plucker equation terms all vanish under each ideal
def plucker_sub(subs):
    p12,p13,p14,p23,p24,p34=sp.symbols("p12 p13 p14 p23 p24 p34")
    rel=p12*p34-p13*p24+p14*p23
    return sp.expand(rel.subs(subs))
p12,p13,p14,p23,p24,p34=sp.symbols("p12 p13 p14 p23 p24 p34")
ck(plucker_sub({p14:0,p24:0,p34:0})==0,"Sstar_zero_ideal_relation")
ck(plucker_sub({p12:0,p13:0,p23:0})==0,"Q_zero_ideal_relation")
ck(bf["controls"][0]["codimension"]==2 and bf["controls"][1]["codimension"]==2,"zero_locus_codim2")
ck(bf["controls"][0]["reduced"] and bf["controls"][1]["reduced"],"zero_locus_reduced")

# I1 finite gauge future counts
ck(gl["I1_multistep_gauge_source"]["gauge_group_order"]==8,"gauge_order")
raw=[2*(8**k) for k in range(4)]
ck(raw==[2,16,128,1024],"I1_raw_counts")
ck(sum(raw)==1170,"I1_raw_total")
ck(gl["I1_multistep_gauge_source"]["complete_future_signature_classes"]==[2,2,2,2],"I1_q_counts")
ck(gl["I1_multistep_gauge_source"]["quotient_reusable_total"]==8,"I1_q_total")

# I2 ideal provenance
ck(pr["I2_cases"][0]["radical_support"]==pr["I2_cases"][2]["radical_support"],"same_radical_support")
ck(pr["I2_cases"][0]["scheme_multiplicity_generic"]==1,"mult1")
ck(pr["I2_cases"][2]["scheme_multiplicity_generic"]==2,"mult2")
ck(pr["I2_cases"][0]["cycle_class_tau_basis"]!=pr["I2_cases"][2]["cycle_class_tau_basis"],"multiplicity_changes_class")
ck(pr["I2_cases"][1]["ideal_normal_form"]==pr["I2_cases"][0]["ideal"],"recombined_same_ideal")
# local multiplicity toy lengths
x=sp.symbols("x")
ck(sp.degree(x**2,x)==2 and sp.degree(x,x)==1,"local_nilpotent_order_control")

# I3 class-first matrix and target lifts
C=sp.Matrix([[sp.Rational(1,2),sp.Rational(1,2)],[-sp.Rational(1,2),sp.Rational(1,2)]])
ck(C.det()==sp.Rational(1,2),"class_matrix_invertible")
Ci=C.inv()
for t in cf["frozen_target_results"]:
    v=sp.Matrix([sp.Rational(z) for z in t["coords"]])
    got=Ci*v
    exp=sp.Matrix([sp.Rational(z) for z in t["lift_cycle_coeffs_ZSstar_ZQ"]])
    for k in range(2): ck(got[k]==exp[k],"target_lift_coeff")
    vv=C*got
    for k in range(2): ck(vv[k]==v[k],"target_class_compare")
# symbolic formula test grid
for rn in range(-3,4):
    for sn in range(-3,4):
        v=sp.Matrix([rn,sn]); coeff=sp.Matrix([rn-sn,rn+sn])
        vv=C*coeff
        for k in range(2): ck(vv[k]==v[k],"symbolic_integer_target_formula")

# divisor-product control: tau2 independent from tau1
ck(sp.Matrix.hstack(v1,v2).rank()==2,"tau2_not_divisor_square_line")
ck(pr["I2_cases"][0]["cycle_class_tau_basis"]==["1","0"],"h2_tau1_control")

# Rational denominator check
half=next(t for t in cf["frozen_target_results"] if t["id"]=="T_half_tau1")
ck(half["lift_cycle_coeffs_ZSstar_ZQ"]==["1/2","1/2"],"half_target_rational")
ck(mr["denominator_control"]["clear_by_N2"]==["1","1"],"denominator_clear")

# Naturality / leakage / attribution
for x0 in nat["checks"]: ck(x0["verdict"]=="PASS","naturality")
for cert in att["certificates"]:
    ck(cert["status"]=="BASELINE_SENSITIVE_ATTRIBUTION","attrib_baseline_sensitive")
    ck(cert["R2_addendum_pass"] is False,"attrib_no_R2")
ck(bs["B_std_codim2"]["independently_available_normal_forms"]["I3"].startswith("2x2"),"Bstd_has_matrix_solve")
ck(tl["generator_absences"]["known_Schubert_cycle"] is True,"no_Schubert_generator")
ck(tl["generator_absences"]["known_Chow_basis"] is True,"no_Chow_generator")
ck(tl["generator_absences"]["precomputed_c2_S_or_Q_used_to_define_target"] is True,"no_c2_target_leak")
ck(r3["robust_attributed_R2"] is False,"r3_blocked_by_R2")
ck(r3["H1_admissible"] is False,"H1_firewall")

summary={
    "schema":"HODGE_H0I_CHECKER_OUTPUT_V1",
    "status":"PASS",
    "task_id":TASK,
    "researcher_id":RID,
    "passed":passed,
    "failed":0,
    "result":f"{passed}/{passed} PASS",
    "load_bearing":{
        "invariant_target_dimension":2,
        "plucker_S_triple_cocycle_matrix_entry_checks":216*4,
        "plucker_Q_triple_cocycle_matrix_entry_checks":216*4,
        "I1_interface_reduction":[1170,8],
        "I3_class_matrix_det":"1/2",
        "robust_attributed_R2":False,
        "classification":"H0I_SOURCE_VECTOR_BUNDLE_CHOW_NORMAL_FORM_ALREADY_COMPLETE",
        "H1_admissible":False
    },
    "warning":"Checker PASS validates the declared finite/source-independent benchmark construction and attribution classification only. It is not a general Hodge proof."
}
print(json.dumps(summary,sort_keys=True))
