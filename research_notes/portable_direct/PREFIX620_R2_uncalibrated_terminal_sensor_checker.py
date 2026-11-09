#!/usr/bin/env python3
"""Exact original native X6-BRC four-point probe sensor theorem checker.
Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Reconstructs original 48-phase positive-branch STAR operator, not a surrogate.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

STAR = ((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-v if c>0 else v for v in STAR[a] if v!=abs(c))
PH = tuple((a,p,s*c) for a in range(4) for c in STAR[a] for s in (-1,1) for p in near(a,s*c))
I = {p:i for i,p in enumerate(PH)}
def succ(i):
    a,p,c=PH[i]
    b=next(j for j in range(4) if j!=a and abs(c) in STAR[j])
    return [I[x] for x in [(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)]]
E=[(i,j) for i in range(48) if abs(PH[i][2]) not in (5,6) for j in succ(i)]
assert len(PH)==48 and len(E)==96 and I[(0,1,-3)]==4
HC = ((2,3,15),(5,28,29),(27,38,39),(16,17,41))
HB = ({3:1,14:1,15:1},{17:2,40:2,41:2},{26:4,27:4,39:4},{4:4,5:8,29:8})
PURE = (2,28,38,16)
UNIFORM6 = (14,3,40,26,27,4)
WITNESS4 = (14,40,26,4)

def Qstep(x,g):
    y=[F(0)]*48
    for i,j in E:
        y[i]+=(F(1) if i==4 else (g+3 if j==4 else F(2)))*x[j]
    return y

def lift(c,w):
    y=[F(0)]*48
    for j,inds in enumerate(HC):
        for i in inds: y[i]+=c[j]
    for j,coefs in enumerate(HB):
        for i,k in coefs.items(): y[i]+=k*w[j]
    return y

def native(a,b,lam,word):
    d=[F(0)]*48
    for i in (4,11,14,32): d[i]=lam
    y=Qstep(Qstep(d,a),b)
    for g in word: y=Qstep(y,g)
    return y

def base(t,lam):
    c0=[F(0),F(0),4*lam,4*lam]
    return [F(2)**t*c0[(j-t)%4] for j in range(4)]

def from_sensor_values(t,samples,kind):
    w=[F(0)]*4
    if kind=='time_aware' and t==0:
        lam=samples[26]/4
        w=[samples[14],samples[40]/2,lam,lam/2]
    elif kind=='time_aware' and t==1:
        lam=samples[4]/4
        w=[samples[14],samples[40]/2,samples[26]/4,lam]
    else:
        w=[samples[14],samples[40]/2,samples[26]/4,samples[4]/4]
        if kind=='time_aware':
            j=(t+2)%4
            lam=samples[PURE[j]]/(4*2**t)
        else:
            v0=samples[3]-samples[14]
            v2=samples[27]-samples[26]
            j=(t+2)%4
            lam=(v0 if j==0 or (t+3)%4==0 else v2)/(4*2**t)
    return lift(base(t,lam),w),lam

def matrix_at_residue(r):
    # normalized lambda-column: c_r = 4*2^t*(e_(r+2)+e_(r+3))
    a=[(r+2)%4,(r+3)%4]
    rows=[]
    for i in range(48):
        rows.append(tuple(sum(int(i in HC[j]) for j in a) for _ in [0])+
                    tuple(HB[j].get(i,0) for j in range(4)))
    return rows

def rank_int(A):
    # Fraction-free integer Gaussian elimination (Bareiss).
    M=[list(r) for r in A]
    if not M: return 0
    m,n=len(M),len(M[0]); rank=0; denom=1
    for col in range(n):
        piv=next((j for j in range(rank,m) if M[j][col]),None)
        if piv is None:continue
        M[rank],M[piv]=M[piv],M[rank]
        x=M[rank][col]
        for j in range(rank+1,m):
            y=M[j][col]
            for k in range(col+1,n):
                M[j][k]=(x*M[j][k]-y*M[rank][k])//denom
            M[j][col]=0
        denom=x
        rank+=1
        if rank==m: break
    return rank

def main():
    # Gate-affine intertwiner: checking g=0 and g=1 proves all rational g,
    # since both the native and compressed maps are affine in g.
    for g in (F(0),F(1)):
        for j in range(8):
            c=[F(0)]*4; w=[F(0)]*4
            (c if j<4 else w)[j if j<4 else j-4]=F(1)
            lhs=Qstep(lift(c,w),g)
            cc=[2*c[3],2*c[0],2*c[1],2*c[2]]
            ww=[4*(g+3)*w[3],w[0],w[1],w[2]]
            assert lhs==lift(cc,ww)
    examples=[]
    configs=((F(1),F(2),F(3,2)),(F(0),F(0),F(1)),(F(5,3),F(7,2),F(11,7)),(F(3),F(1),F(2)))
    ns=(0,1,2,3,4,5,6,7,8,12,20)
    checked=0
    for case,(a,b,lam) in enumerate(configs):
        for t in ns:
            word=[F((7*j*j+3*j+case)%9,(2*j+case)%5+1) for j in range(1,t+1)]
            native_x=native(a,b,lam,word)
            c=base(t,lam)
            w=[lam*(b+3),lam*(a+3),lam,lam/2]
            for q in word: w=[4*(q+3)*w[3],w[0],w[1],w[2]]
            assert native_x==lift(c,w)
            six={i:native_x[i] for i in UNIFORM6}
            re6,l6=from_sensor_values(t,six,'uniform6')
            assert re6==native_x and l6==lam
            if t==0: dynamic=(14,40,26)
            elif t==1: dynamic=WITNESS4
            else: dynamic=WITNESS4+(PURE[(t+2)%4],)
            re5,l5=from_sensor_values(t,{i:native_x[i] for i in dynamic},'time_aware')
            assert re5==native_x and l5==lam
            checked+=96
            if case==0:examples.append({'t':t,'dynamic_sensors':list(dynamic),'uniform_sensors':list(UNIFORM6),'recovered_lambda':str(l5),'pass':True})
    # Every phase index that can appear in the 8D embedding (16 rows).
    support=sorted(set(i for inds in HC for i in inds)|set(i for col in HB for i in col))
    assert len(support)==16
    rows=[matrix_at_residue(r) for r in range(4)]
    ranks6=[rank_int([rows[r][i] for i in UNIFORM6]) for r in range(4)]
    assert ranks6==[5]*4
    five_total=0;five_any_full=0;five_all_full=0;best_coverage=0
    for S in combinations(support,5):
        five_total+=1
        cov=sum(rank_int([rows[r][i] for i in S])==5 for r in range(4))
        five_any_full+=int(cov>0)
        five_all_full+=int(cov==4)
        best_coverage=max(best_coverage,cov)
    assert five_total==4368 and five_all_full==0
    # time-specific witness dimensions from the displayed monomial coordinate laws
    dimensions={'t0':3,'t1':4,'t_ge_2':5}
    result={
      'schema':'PREFIX620_R2_UNCALIBRATED_TERMINAL_SENSOR_CERTIFICATE_V1',
      'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'observer_scope':'native original X6 positive-branch 48-phase sum with d=e4+e11+e14+e32',
      'tested_input_configs':len(configs),'tested_lengths':list(ns),'tested_cases':len(configs)*len(ns),
      'exact_full48_reconstruction_coordinate_checks':checked,
      'symbolic_affine_intertwiner_coordinate_checks':768,
      'time_specific_minimum':'3 at t=0, 4 at t=1, 5 at t>=2',
      'uniform_time_independent_minimum_for_all_t_ge_4':6,
      'six_sensors':list(UNIFORM6),'uniform_six_rank_certificates':ranks6,
      'possible_support_rows':support,'all_five_subsets_tested':five_total,
      'five_sets_full_rank_at_all_four_time_residues':five_all_full,
      'best_five_set_full_rank_residues':best_coverage,
      'time_specific_examples':examples,
      'status':'PASS_AUTHOR_SIDE_EXACT_AND_EXHAUSTIVE_5_SUBSETS; INDEPENDENT_REVIEW_PENDING'
    }
    target=Path(__file__).with_name('PREFIX620_R2_uncalibrated_terminal_sensor_results.json')
    target.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:result[k] for k in ('tested_cases','exact_full48_reconstruction_coordinate_checks','all_five_subsets_tested','five_sets_full_rank_at_all_four_time_residues','best_five_set_full_rank_residues','uniform_six_rank_certificates')}))
if __name__=='__main__':main()
