#!/usr/bin/env python3
"""PREFIX-621 exact original X6-BRC robust terminal phase-sensor checker.
Frozen science: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
All arithmetic uses exact fractions. Run: python3 PREFIX621_R2_native_phase_robust_sensors_checker.py
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-v if c>0 else v for v in STARS[a] if v!=abs(c))
PH=tuple((a,p,s*c) for a in range(4) for c in STARS[a] for s in (-1,1) for p in near(a,s*c))
INDEX={p:i for i,p in enumerate(PH)}
def successors(i):
    a,p,c=PH[i]
    b=next(j for j in range(4) if j!=a and abs(c) in STARS[j])
    return [INDEX[v] for v in ([(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])]
EDGES=[(i,j) for i in range(48) if abs(PH[i][2]) not in (5,6) for j in successors(i)]
assert len(PH)==48 and len(EDGES)==96 and INDEX[(0,1,-3)]==4

HC=((2,3,15),(5,28,29),(27,38,39),(16,17,41))
HB=({3:1,14:1,15:1},{17:2,40:2,41:2},{26:4,27:4,39:4},{4:4,5:8,29:8})
PURE=(2,28,38,16)
W_ONLY=(14,40,26,4)
W_GROUPS=tuple(tuple(sorted(g)) for g in HB)
ALL_W=tuple(sorted(set(j for d in HB for j in d)))
SUPPORT=tuple(sorted(set(i for g in HC for i in g)|set(ALL_W)))
S8=(3,4,5,14,17,26,27,40)
S14=(2,3,4,5,14,15,17,26,27,29,38,39,40,41)

def sensor_row(i,r):
    active=((r+2)%4,(r+3)%4)
    return (F(sum(i in HC[j] for j in active)),)+tuple(F(d.get(i,0)) for d in HB)
def observation_matrix(S,r):
    return [sensor_row(i,r) for i in S]
def rank(M):
    if not M:return 0
    A=[list(map(F,row)) for row in M]
    m,n=len(A),len(A[0]); k=0
    for j in range(n):
        piv=next((u for u in range(k,m) if A[u][j]),None)
        if piv is None:continue
        A[k],A[piv]=A[piv],A[k]
        pv=A[k][j]
        for u in range(k+1,m):
            if A[u][j]:
                scale=A[u][j]/pv
                for v in range(j,n):A[u][v]-=scale*A[k][v]
        k+=1
        if k==m:break
    return k

def Qstep(x,g):
    y=[F(0)]*48
    for i,j in EDGES:
        y[i]+=(F(1) if i==4 else (g+3 if j==4 else F(2)))*x[j]
    return y
def lift(c,w):
    y=[F(0)]*48
    for j,inds in enumerate(HC):
        for i in inds:y[i]+=c[j]
    for j,coeffs in enumerate(HB):
        for i,k in coeffs.items():y[i]+=k*w[j]
    return y
def native(a,b,lam,word):
    d=[F(0)]*48
    for i in (4,11,14,32):d[i]=lam
    x=Qstep(Qstep(d,a),b)
    for g in word:x=Qstep(x,g)
    return x

def solve_linear(A,y):
    R=[list(map(F,row))+[F(v)] for row,v in zip(A,y)]
    n=5;m=len(R);k=0;pivots=[]
    for j in range(n):
        piv=next((u for u in range(k,m) if R[u][j]),None)
        if piv is None:continue
        R[k],R[piv]=R[piv],R[k]
        scale=R[k][j];R[k]=[v/scale for v in R[k]]
        for u in range(m):
            if u!=k and R[u][j]:
                z=R[u][j];R[u]=[a-z*b for a,b in zip(R[u],R[k])]
        pivots.append(j);k+=1
    assert k==n and all(any(R[u][:n]) or R[u][n]==0 for u in range(m))
    out=[F(0)]*n
    for u,j in enumerate(pivots):out[j]=R[u][n]
    return out
def full_from_sensors(S,r,values):
    coeff=solve_linear(observation_matrix(S,r),values)
    c=[coeff[0] if j in ((r+2)%4,(r+3)%4) else F(0) for j in range(4)]
    return lift(c,coeff[1:])
def erasure_check(S,e):
    n=0
    for r in range(4):
        for lost in combinations(S,e):
            remain=tuple(i for i in S if i not in lost)
            assert rank(observation_matrix(remain,r))==5,(S,r,lost)
            n+=1
    return n

def main():
    assert len(SUPPORT)==16 and len(ALL_W)==12 and set(ALL_W).isdisjoint(PURE)
    for g in (F(0),F(1)):
        for j in range(8):
            c=[F(0)]*4;w=[F(0)]*4
            (c if j<4 else w)[j%4]=F(1)
            assert Qstep(lift(c,w),g)==lift([2*c[3],2*c[0],2*c[1],2*c[2]],
                                         [4*(g+3)*w[3],w[0],w[1],w[2]])
    n1=erasure_check(S8,1)
    n2=erasure_check(S14,2)
    assert n1==32 and n2==364
    obstruction=[]
    for extra in (None,)+PURE:
        subset=ALL_W+(extra,) if extra is not None else ALL_W
        r=next(r for r in range(4) if extra is None or sensor_row(extra,r)[0]==0)
        active={(r+2)%4,(r+3)%4}
        mixed_to_w={0:0,1:3,2:2,3:1}
        lost=tuple(W_ONLY[mixed_to_w[j]] for j in sorted(active))
        remain=[i for i in subset if i not in lost]
        assert rank(observation_matrix(remain,r))==4
        obstruction.append({'extra_pure_C':extra,'residue':r,'erased':list(lost),'remaining_rank':4})
    native_cases=0;coordinate_checks=0;erased_recovery_checks=0
    cfg=((F(0),F(0),F(1)),(F(1),F(2),F(3,2)),(F(7,3),F(5,2),F(13,7)))
    for a,b,lam in cfg:
        for t in range(4,12):
            gates=[F((2*j*j+5*j)%9,(j%3)+1) for j in range(1,t+1)]
            x=native(a,b,lam,gates)
            w=[lam*(b+3),lam*(a+3),lam,lam/2]
            for g in gates:w=[4*(g+3)*w[3],w[0],w[1],w[2]]
            c=[F(4*2**t)*lam if j in ((t+2)%4,(t+3)%4) else F(0) for j in range(4)]
            assert x==lift(c,w)
            native_cases+=1;coordinate_checks+=48
            for S,e in ((S8,1),(S14,2)):
                for lost in combinations(S,e):
                    remain=[i for i in S if i not in lost]
                    assert full_from_sensors(remain,t%4,[x[i] for i in remain])==x
                    erased_recovery_checks+=1
    corruption_cases=0
    for r in range(4):
        theta=F(11,3);w=[F(2),F(7,2),F(5,3),F(8)]
        true=[sum(a*b for a,b in zip(sensor_row(i,r),[theta]+w)) for i in S14]
        for bad in range(len(S14)):
            vals=true[:];vals[bad]+=F(7,11)
            candidates=[]
            for suspect in range(len(S14)):
                remain=[i for j,i in enumerate(S14) if j!=suspect]
                try:
                    co=solve_linear(observation_matrix(remain,r),[vals[j] for j in range(len(S14)) if j!=suspect])
                except AssertionError:
                    continue
                pred=[sum(a*b for a,b in zip(sensor_row(i,r),co)) for i in S14]
                if sum(a!=b for a,b in zip(pred,vals))<=1:candidates.append(co)
            assert candidates and all(co==[theta]+w for co in candidates)
            corruption_cases+=1
    result={
      'schema':'PREFIX621_R2_NATIVE_BRC_ROBUST_TERMINAL_SENSORS_V1',
      'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'scope':'48 original native phase sums; four-point probe; unknown a,b,lambda; known t; fixed phase-coordinate sensors; t>=4 minimality',
      'active_possible_phase_rows':list(SUPPORT),'W_groups':[list(x) for x in W_GROUPS],
      'minimum_0_erasure_from_PREFIX620':6,
      'minimum_1_erasure':8,'one_erasure_fixed_rows':list(S8),
      'minimum_2_erasures_and_1_adversarial_corruption':14,'two_erasure_fixed_rows':list(S14),
      'three_erasure_possible':False,
      'exact_rank_checks_1_erasure':n1,'exact_rank_checks_2_erasure':n2,
      'lower_bound_obstructions_12_or_13_rows':obstruction,
      'native_exact_gate_cases':native_cases,'native_full48_coordinate_comparisons':coordinate_checks,
      'erased_sensor_reconstructions':erased_recovery_checks,
      'single_corrupted_sensor_decodes':corruption_cases,
      'native_intertwiner_integer_coordinate_checks':768,
      'proof':'W-group counting plus active-pair C-repair; Fraction exact rank for all erasures',
      'status':'PASS_AUTHOR_SIDE_EXACT; INDEPENDENT_REVIEW_PENDING'}
    path=Path(__file__).with_name('PREFIX621_R2_native_phase_robust_sensors_results.json')
    path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in (
        'minimum_1_erasure','minimum_2_erasures_and_1_adversarial_corruption',
        'exact_rank_checks_1_erasure','exact_rank_checks_2_erasure',
        'native_exact_gate_cases','native_full48_coordinate_comparisons',
        'erased_sensor_reconstructions','single_corrupted_sensor_decodes')}))
if __name__=='__main__':main()
