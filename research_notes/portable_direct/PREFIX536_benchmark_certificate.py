#!/usr/bin/env python3
"""PREFIX-536: exact evaluated benchmark of native BRC-gate observers.
Science pin: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Loads definitions from sibling PREFIX535_rooted_parity_certificate.py, not its test main.
"""
from collections import defaultdict
from pathlib import Path
from statistics import median
import json, time, gc, platform, tracemalloc

SOURCE=Path(__file__).with_name('PREFIX535_rooted_parity_certificate.py')
code=SOURCE.read_text(encoding='utf-8')
head=code.split('\nresults=[]\n')[0]
assert 'def delta_coefficients' in head and 'def evaluate_roots' in head
ns={'__name__':'prefix535_definition_only'}
exec(compile(head, str(SOURCE), 'exec'), ns)
PHASES,NEXT,TARGET=ns['PHASES'],ns['NEXT'],ns['TARGET']
sign,flag=ns['sign'],ns['flag']
delta_coefficients=ns['delta_coefficients']

V=2; Q=V*V; Z=3; ROOT=0
PRECURSORS=tuple(i for i in range(48) if TARGET in NEXT[i])
assert len(PRECURSORS)==3
PRESET=set(PRECURSORS)
CSTATES=tuple((i,b) for i in range(48) for b in ((0,1) if i in PRESET else (0,)))
assert len(CSTATES)==51
DEN=[1,4,-2304,-102016,-2056192,-5971968,565248000,10154409984,
     37484494848,-1492132036608,-14676708556800,126806761930752]
assert len(DEN)==12 and DEN[0]==1
for modulus in (1000000007,998244353):
    assert [c%modulus for c in DEN]==delta_coefficients(Q,Z,modulus)

EDGE51={}
for i,b in CSTATES:
    a=[]
    for j in NEXT[i]:
        weight=V**(flag(i)+flag(j))
        for branch in (0,1):
            next_b=branch if j in PRESET else 0
            factor=weight*(Z if b and branch and j==TARGET else 1)
            a.append(((j,next_b),factor))
    EDGE51[(i,b)]=a
assert sum(map(len,EDGE51.values()))==306

def direct_51(n,root=ROOT):
    dp={(root,0):1}; series=[]
    for depth in range(n+1):
        weighted=0
        for (i,_),value in dp.items():
            denom=V**abs(sign(i)-sign(root))
            assert value%denom==0
            weighted+=value//denom
        series.append(weighted)
        if depth==n:break
        ndp=defaultdict(int)
        for state,value in dp.items():
            for target,factor in EDGE51[state]:ndp[target]+=value*factor
        dp=ndp
    return series

EDGE49=[[(j,2*(V**(flag(i)+flag(j)))) for j in NEXT[i]] for i in range(48)]
GATE49=[]
for i in range(48):
    vals=defaultdict(int)
    for middle in NEXT[i]:
        if TARGET in NEXT[middle]:
            vals[V**(flag(i)+2*flag(middle)+flag(TARGET))]+=1
    GATE49.append(tuple(vals.items()))
assert sum(sum(n for _,n in row) for row in GATE49)==9

def direct_49(n,root=ROOT):
    f=[V**(2-abs(sign(i)-sign(root))) for i in range(48)]; g=0
    series=[]
    for depth in range(n+1):
        assert f[root]%V**2==0
        series.append(f[root]//(V**2))
        if depth==n:break
        nf=[sum(w*f[j] for j,w in EDGE49[i]) +
            sum(weight*mult*g for weight,mult in GATE49[i]) for i in range(48)]
        f,g=nf,(Z-1)*f[TARGET]
    return series

def scalar_parity_11(n,initial):
    assert len(initial)==23
    seq=initial[:min(23,n+1)]
    for d in range(23,n+1):
        seq.append(-sum(DEN[j]*seq[d-2*j] for j in range(1,12)))
    return seq

assert len(DEN)==12 and DEN[-1]!=0
PRE=direct_49(22)
for limit in (0,1,2,7,23,24,35,60):
    x=direct_51(limit)
    y=direct_49(limit)
    z=scalar_parity_11(limit,PRE)
    assert x==y==z,('mismatch',limit,next(((j,a,b,c) for j,(a,b,c) in enumerate(zip(x,y,z)) if a!=b or a!=c),None))

def native_raw_integer(n=7):
    dp={(ROOT,0,0,0):1}; check=[]
    for d in range(n+1):
        total=0; weighted=0
        for (i,b,k,h),count in dp.items():
            correction=abs(sign(i)-sign(ROOT))
            assert k>=correction and (k-correction)%2==0
            total+=count
            weighted+=count*(Q**((k-correction)//2))*(Z**h)
        assert total==6**d
        check.append(weighted)
        if d==n:break
        ndp=defaultdict(int)
        for (i,b,k,h),count in dp.items():
            for j in NEXT[i]:
                visits=k+flag(i)+flag(j)
                for branch in (0,1):
                    delta=int(b==1 and branch==1 and j==TARGET)
                    ndp[(j,branch,visits,h+delta)]+=count
        dp=ndp
    return check
assert native_raw_integer(7)==direct_51(7)

SIGN_ROOTS={sgn:[i for i in range(48) if sign(i)==sgn] for sgn in (-1,0,1)}
assert sum(map(len,SIGN_ROOTS.values()))==48

def all_roots_49(n):
    out=[[] for _ in range(48)]
    for sgn,roots in SIGN_ROOTS.items():
        f=[V**(2-abs(sign(i)-sgn)) for i in range(48)];g=0
        for depth in range(n+1):
            for root in roots:
                assert f[root]%(V**2)==0
                out[root].append(f[root]//(V**2))
            if depth==n:break
            nf=[sum(w*f[j] for j,w in EDGE49[i]) +
                sum(weight*mult*g for weight,mult in GATE49[i]) for i in range(48)]
            f,g=nf,(Z-1)*f[TARGET]
    return out

def all_roots_51(n):
    return [direct_51(n,root=root) for root in range(48)]

def all_roots_scalar_cold(n):
    return [scalar_parity_11(n,seq) for seq in all_roots_49(22)]

for n in (0,7,23,40):
    a,b,c=all_roots_51(n),all_roots_49(n),all_roots_scalar_cold(n)
    assert a==b==c,('all-root mismatch',n)

def eval_scalar_cold(n):return scalar_parity_11(n,direct_49(22))
METHODS=[('controller_51',direct_51),('linear_49',direct_49),('parity_11_cold',eval_scalar_cold)]

def profile_one(fn,n,repetitions=5):
    times=[]; out=None
    for k in range(repetitions):
        gc.collect()
        t=time.perf_counter_ns();res=fn(n);dur=time.perf_counter_ns()-t
        times.append(dur)
        if out is None:out=res
        else:assert res==out
    gc.collect();tracemalloc.start();res=fn(n);_,peak=tracemalloc.get_traced_memory();tracemalloc.stop()
    assert res==out
    return {'median_ms':round(median(times)/1e6,3),'min_ms':round(min(times)/1e6,3),
            'max_ms':round(max(times)/1e6,3),'tracemalloc_peak_bytes':peak,
            'final_digits':len(str(out[-1])),'final_bit_length':out[-1].bit_length(),'length':len(out)}

def profile_all_roots(fn,n,repetitions=5):
    times=[];out=None
    for _ in range(repetitions):
        gc.collect();t=time.perf_counter_ns();res=fn(n);dur=time.perf_counter_ns()-t
        times.append(dur)
        if out is None:out=res
        else:assert out==res
    gc.collect();tracemalloc.start();res=fn(n);_,peak=tracemalloc.get_traced_memory();tracemalloc.stop()
    assert res==out
    return {'median_ms':round(median(times)/1e6,3),
            'min_ms':round(min(times)/1e6,3),
            'max_ms':round(max(times)/1e6,3),
            'tracemalloc_peak_bytes':peak,
            'output_coefficients':48*(n+1),
            'final_first_root_bit_length':out[0][-1].bit_length()}

RESULT={
 'status':'ALL_CHECKS_PASS','kind':'exact_evaluated_observer_benchmark',
 'science_pin':'enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'provenance':'PREFIX-535 definitions loaded without test main',
 'parameters':{'q':Q,'z':Z,'root':list(PHASES[ROOT]),'N_macros':[64,256,1024],
               'repetitions':5,'outputs':'all weighted integer coefficients a_d for d=0..N'},
 'states':{'phase':48,'deterministic_controller':51,'lift_linear':49,
           'parity_recurrence_each':11,'controller_labeled_transitions':306},
 'parity_denominator_u_coefficients':DEN,
 'raw_check':{'depth_0_to_7_exact':True,'root':list(PHASES[ROOT])},
 'exact_crosschecks_at_depths':[0,1,2,7,23,24,35,60],
 'environment':{'python':platform.python_version(),'platform':platform.platform()},
 'benchmarks':{},'all_root_benchmarks':{},
 'all_root_reuse_lemma':'49-lift initial endpoint depends only on sign_1(root); 48 roots need three shared evolutions.'
}
for n in [64,256,1024]:
    vals={}
    for name,fn in METHODS:vals[name]=profile_one(fn,n)
    RESULT['benchmarks'][str(n)]=vals
    print('N',n,'time ms',{k:v['median_ms'] for k,v in vals.items()})
    assert direct_51(n)==eval_scalar_cold(n)==direct_49(n)
for n in [64,256]:
    vals={}
    for name,fn in [('controller_51',all_roots_51),('linear_49_shared_sign',all_roots_49),
                    ('parity_11_shared_cold',all_roots_scalar_cold)]:
        vals[name]=profile_all_roots(fn,n)
    RESULT['all_root_benchmarks'][str(n)]=vals
    print('all 48 roots N',n,'time ms',{k:v['median_ms'] for k,v in vals.items()})
    assert all_roots_51(n)==all_roots_49(n)==all_roots_scalar_cold(n)
Path(__file__).with_name('PREFIX536_EXACT_EXECUTION.json').write_text(json.dumps(RESULT,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS')
