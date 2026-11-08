#!/usr/bin/env python3
"""PREFIX-606: exact sampled full prefix-operator gate identifiability for native X6-BRC derived tail.
Frozen science f42f2906d77f24085c123f3ccfe9667d41caa96d. SymPy exact arithmetic.
"""
import json
from pathlib import Path
import sympy as sp

STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STAR[a] if k!=abs(c))
phases=tuple((a,p,sgn*k) for a in range(4) for k in STAR[a] for sgn in (-1,1) for p in near(a,sgn*k))
assert len(phases)==48 and len(set(phases))==48
index={q:i for i,q in enumerate(phases)}
def successor(i):
    a,p,c=phases[i]
    b=next(k for k in range(4) if k!=a and abs(c) in STAR[k])
    return tuple(index[q] for q in ([(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)]))
N=[successor(i) for i in range(48)]
g=index[(0,1,-3)]
assert g==4
def Q(z):
    M=sp.zeros(48)
    for i,js in enumerate(N):
        if abs(phases[i][2]) in (5,6): continue
        for j in js: M[i,j]=1 if i==g else (3+z if j==g else 2)
    return M
def B(z):
    return sp.Matrix([[0,0,0,4*(z+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
def products(q,t=None):
    t=len(q) if t is None else t
    p=[sp.Integer(1)]*4
    for k in range(t): p[k%4]*=sp.sympify(q[k])+3
    return tuple(p)
def transfer(q,t=None):
    t=len(q) if t is None else t
    p=products(q,t)
    F=sp.zeros(4)
    for j in range(4):
        residue=(3-j)%4
        count=len(range(residue,t,4))
        F[(j+t)%4,j]=4**count*p[residue]
    return F
def intervals(times):
    return list(zip((0,)+times[:-1],times))
def recover(q,times):
    assert times and times[-1]==len(q)
    prev=(sp.Integer(1),)*4
    found=[None]*len(q)
    for lo,hi in intervals(times):
        assert hi-lo<=4
        curr=products(q,hi)
        for j in range(lo,hi): found[j]=curr[j%4]/prev[j%4]-3
        prev=curr
    return tuple(found)

schedules=0; count_by_n={}; max_rank_gap=0
for n in range(1,10):
    count=0
    for mask in range(1<<(n-1)):
        times=tuple(j for j in range(1,n) if mask>>(j-1)&1)+(n,)
        J=sp.zeros(4*len(times),n)
        for block,(lo,hi) in enumerate(intervals(times)):
            for j in range(lo,hi): J[4*block+j%4,j]=sp.Rational(1,4)
        expected=sum(min(4,hi-lo) for lo,hi in intervals(times))
        assert J.rank()==expected,(n,times,expected)
        assert expected==n-sum(max(hi-lo-4,0) for lo,hi in intervals(times))
        if all(hi-lo<=4 for lo,hi in intervals(times)):
            q=tuple(sp.Rational((5*j+1)%11,(j%3)+1) for j in range(n))
            assert recover(q,times)==q
        else:
            max_rank_gap=max(max_rank_gap,n-expected)
        count+=1
    count_by_n[n]=count;schedules+=count

q=(sp.Integer(0),sp.Integer(2),sp.Integer(1),sp.Integer(5),sp.Integer(3),sp.Integer(4),sp.Integer(7),sp.Integer(6))
assert recover(q,(4,8))==q
for t in (4,8):
    F=sp.eye(4)
    for v in q[:t]: F=B(v)*F
    assert F==transfer(q,t)

p=(sp.Integer(1),)*8
alt=(sp.Integer(0),sp.Integer(1),sp.Integer(1),sp.Integer(1),sp.Rational(7,3),sp.Integer(1),sp.Integer(1),sp.Integer(1))
assert p!=alt
for t in (5,8):
    assert products(p,t)==products(alt,t)
    assert transfer(p,t)==transfer(alt,t)
assert transfer(p,1)!=transfer(alt,1)

transient=Q(0)*Q(1)
full=transient;other=transient;native_checks=0
for t in range(1,9):
    full=Q(p[t-1])*full
    other=Q(alt[t-1])*other
    if t in (5,8):
        assert full==other
        native_checks+=48
    if t==1: assert full!=other
result={
 'schema':'PREFIX606_R2_GATE_PREFIX_SAMPLING_EXACT_V1',
 'frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'native_phase_count':48,'native_port_count':96,'native_tagged_actions':576,
 'fixed_axis_weights':[1,1,1,1,0,0],
 'scope':'complete 48-phase linear prefix operators after common two-step native transient; nonnegative real gates',
 'theorem':'injective iff all checkpoint gaps <=4; minimal samples ceil(n/4)',
 'rank_formula':'sum min(4,gap); interior fiber dimension sum max(0,gap-4)',
 'exact_schedules_tested':schedules,'schedules_by_n':count_by_n,
 'max_unidentified_dimensions_tested':max_rank_gap,
 'n8_recovery_samples':[4,8],'n8_recovered_gate_word':[str(x) for x in q],
 'ambiguous_words':{'baseline':[str(x) for x in p],'alternative':[str(x) for x in alt],
                    'identical_samples':[5,8],'different_sample':1},
 'full_native_48_phase_basis_equalities':native_checks,
 'status':'AUTHOR_SIDE_EXACT_DERIVATION_AND_EXECUTED_CHECKS; INDEPENDENT_REVIEW_PENDING',
 'boundary':'not raw tagged paths, a single readout vector, noisy observations or physical time'
}
Path(__file__).with_name('PREFIX606_R2_gate_prefix_sampling_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PREFIX606 PASSED',schedules,'schedules; native 48-phase basis comparisons',native_checks)
