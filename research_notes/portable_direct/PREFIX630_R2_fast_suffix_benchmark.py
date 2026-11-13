#!/usr/bin/env python3
"""PREFIX-630: exact native phase-only suffix pullback benchmark.
Dependency: PREFIX629_phase_only_suffix_checker.py from the same source directory.
The dependency executes its published exact tests when imported; timings below
exclude that one-time import and the fixed symbolic coefficient setup.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from PREFIX629_phase_only_suffix_checker import (Q,ACTIONS,evolve,phase,phase_five,
    reconstruct_prefix,suffix_paths,G)
from pathlib import Path
import json

# PREFIX-630: same exact phase-only input, compare synthetic-prefix replay
# with direct endpoint bit-port decoder + 16-state native pullback.
# Frozen source: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
import time
import statistics
import hashlib
import sympy as S

ROWS=(0,2,4,6,8,10,12,14,32,34,36,38,48,50,52,54)
COLS=(0,4,8,12,16,18,20,22,24,28,42,46,56,60,64,68)

# Original typed actions: (src, dst, fixed_weight, gated). Sparse 96x96 action matrix.
A0=S.zeros(96,96); A1=S.zeros(96,96)
for src,dst,w,gated in ACTIONS:
    if gated: A1[dst,src]+=1
    else: A0[dst,src]+=int(w)
T=A0*A0; V=A1*A0
K=T.extract(ROWS,COLS)
assert K.det()==-65536
G0=T[:,COLS]; G1=V[:,COLS]
KI=K.inv();N0=KI*(A0*G0)[list(ROWS),:]; N1=KI*(A0*G1)[list(ROWS),:]
assert N1[2,7]==S.Rational(1,2) and sum(bool(v) for v in N1)==1
assert A0*G0==G0*N0 and A0*G1==G0*N1
assert A1*G0==G1*N0 and A1*G1==G1*N1
U=N0.inv(); assert S.simplify((N1*U).trace())==S.Rational(1,3)

def fractions_matrix(M):
    return tuple(tuple(Q(int(x.p),int(x.q)) for x in M.row(i)) for i in range(M.rows))
MKI=fractions_matrix(KI); MU=fractions_matrix(U)
MG0=fractions_matrix(G0); MG1=fractions_matrix(G1)

# Compress zero coefficients; operations counted in a platform-independent manner.
def sparse_mat(M):
    return tuple(tuple((j,x) for j,x in enumerate(row) if x) for row in M)
SKI=sparse_mat(MKI); SU=sparse_mat(MU)
SG0=sparse_mat(MG0); SG1=sparse_mat(MG1)

def dotrows(M,vec):
    return tuple(sum((w*vec[j] for j,w in row),Q(0)) for row in M)

def endpoint_from_phase(v,g):
    """Original native exact D_g decoder at any reached t>=2."""
    ell=v[3]+v[14]+v[15]-2*v[2]
    delta=(g-1)*ell/(3*(g+3))
    out=[Q(0)]*96
    for i,x in enumerate(v):
        if i==G:
            out[2*i]=out[2*i+1]=x
        else:
            d=delta if i in (3,14,15) else Q(0)
            out[2*i]=(x-d)/2
            out[2*i+1]=(x+d)/2
    return out

def backward(state,gate_previous):
    """16-state exact left inverse: state r_(k+1) and gate g_k -> r_k."""
    g=gate_previous
    k=dotrows(SKI,[state[i] for i in ROWS])
    y=dotrows(SU,k)
    correction=(g/(1+g/3))*y[7]/2
    x=tuple(y[i]-correction*MU[i][2] for i in range(16))
    a=dotrows(SG0,x);b=dotrows(SG1,x)
    return tuple(a[i]+g*b[i] for i in range(96))

def phase_five_fast(v,n):
    # Closed residue counts replace the O(n) range scan in PREFIX-629's readout.
    t=n-2
    lam=v[(2,28,38,16)[(t+2)%4]]/(4*2**t)
    assert lam>0
    w=(v[14],v[40]/2,v[26]/4,v[4]/4)
    prod={}
    for r in range(4):
        wraps=(n-r)//4-(2-r)//4
        j=(({0:2,1:1,2:0,3:3})[r]+t)%4
        prod[r]=w[j]/(lam*({0:Q(1),1:Q(1),2:Q(1),3:Q(1,2)}[r])*4**wraps)
        assert prod[r]>0
    return lam,prod

def fast_prefix(v,n,L,saved):
    """Minimal memory for t=4 (L gates) and t>=5 (L+1 gates)."""
    t=n-L
    assert t>=4
    rn=endpoint_from_phase(v,saved[-1])
    if t==4:
        assert len(saved)==L
        # Only the g4 factor in the residue-0 product is unsaved.
        lam,products=phase_five_fast(v,n)
        assert (lam,products)==phase_five(v,n) if n<=64 else True
        later=Q(1)
        for k,g in zip(range(5,n+1),saved):
            if k%4==0:later*=g+3
        g4=products[0]/later-3
        assert g4>=0
        prev=(g4,)+tuple(saved[:-1])
    else:
        assert len(saved)==L+1
        prev=tuple(saved[:-1])
    rk=rn
    for gk in reversed(prev):
        rk=backward(rk,gk)
    return rk,tuple(saved[-L:])

def sparse_factors(gates):
    # O(n) only to generate the test input; result verified against actual native propagation.
    return {r:__import__('math').prod([g+3 for k,g in enumerate(gates,1) if k%4==r]) for r in range(4)}

def bits(x):
    y=Q(x)
    return max(abs(y.numerator).bit_length(), y.denominator.bit_length())

def summary_bits(r):
    nz=[v for v in r if v]
    return {'count':len(nz),'max_num_bits':max((abs(x.numerator).bit_length() for x in nz),default=0),
            'max_den_bits':max((x.denominator.bit_length() for x in nz),default=0)}

def run_case(n,L,pattern,seed):
    lam=Q(5,3)
    if pattern=='one':
        gates=(Q(1),)*n
    elif pattern=='rational':
        gates=tuple(Q(2+((k*7+seed)%5),1+((k+seed)%3)) for k in range(1,n+1))
    elif pattern=='zero_mix':
        gates=tuple(Q(0) if k%7==0 else Q(1) for k in range(1,n+1))
    elif pattern=='zero_all':
        gates=(Q(0),)*n
    else:raise ValueError(pattern)
    st=time.perf_counter_ns(); rn=evolve(lam,gates)
    source_ms=(time.perf_counter_ns()-st)/1e6
    v=phase(rn); t=n-L; saved=gates[t-1:] if t>=5 else gates[t:]
    assert len(saved)==(L+1 if t>=5 else L)
    trial=[]
    # Precompute all output tensors within each measured method; avoid measuring oracle validation.
    for mode in ('synthetic','inverse'):
        times=[]; restored=None; out=None; h=None
        # A warm-up iteration for each implementation, outside timed samples.
        if mode=='synthetic':
            rw,tw,_,_,_=reconstruct_prefix(v,n,L,saved)
        else:
            rw,tw=fast_prefix(v,n,L,saved)
        _=suffix_paths(rw,tw)
        for i in range(3):
            a=time.perf_counter_ns()
            if mode=='synthetic':
                restored,tail,h,_,_=reconstruct_prefix(v,n,L,saved)
            else:
                restored,tail=fast_prefix(v,n,L,saved)
            # Include all retained original action labels in a full sparse ordered path tensor.
            out=suffix_paths(restored,tail)
            times.append((time.perf_counter_ns()-a)/1e6)
        assert tuple(restored)==tuple(evolve(lam,gates[:t]))
        trial.append({'method':mode,'median_ms':round(statistics.median(times),4),'min_ms':round(min(times),4),'max_ms':round(max(times),4),
                      'input_phase_count':48,'saved_gate_count':len(saved),
                      'prefix_ports':summary_bits(restored),'output_nonzero_paths':len(out),
                      'output_mass_bits':summary_bits(out.values()),
                      'saved_gate_bits':summary_bits(saved),
                      'synthetic_prefix_gate_count':len(h) if h is not None else None,
                      'output_digest':hashlib.sha256(repr(sorted(out.items())).encode()).hexdigest()})
    assert trial[0]['output_digest']==trial[1]['output_digest']
    assert trial[0]['prefix_ports']==trial[1]['prefix_ports']
    return {'n':n,'L':L,'mode':pattern,'seed':seed,'source_forward_ms':round(source_ms,4),
            'terminal_phase_bits':summary_bits(v),'methods':trial,
            'ratio_synthetic_to_inverse':round(trial[0]['median_ms']/trial[1]['median_ms'],4)}

if __name__=='__main__':
    cases=[]
    for pattern in ('one','rational','zero_mix'):
        for n,L in ((5,1),(7,3)):
            cases.append(run_case(n,L,pattern,seed=2))
        for n in (16,32,64,128,256,512):
            for L in (1,3):
                cases.append(run_case(n,L,pattern,seed=2))
    # Explicitly verify exact-zero-gate boundary at prefix cut t=4 and longer histories.
    for n,L in ((5,1),(7,3),(64,1),(64,3)):
        cases.append(run_case(n,L,'zero_all',2))
    # Additional time-age 1024 stress probe; one small suffix per mode.
    cases.append(run_case(1024,1,'one',2))
    assert all(c['methods'][0]['output_digest']==c['methods'][1]['output_digest'] for c in cases)
    result={'schema':'PREFIX630_NATIVE_PHASE_ONLY_SUFFIX_BENCH_V1','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'platform':'Python Fraction / sympy one-off exact setup, native 576 action arcs, wall-clock perf_counter_ns, one warmup then 3 timed full reconstruction and output runs per method; precomputed coefficients excluded',
            'status':'ALL_ASSERTIONS_PASS',
            'theorem':'For n>=L+4, exact terminal 48-phase and the sharp L saved gates (n=L+4) or L+1 saved gates (n>=L+5) recover the complete original tagged L-suffix tensor using native D_gate and rank-16 native inverse, in O(L) fixed-dimensional work plus output enumeration except for terminal product extraction O(log n) at the t=4 boundary.',
            'preprocessing':['native symbolic A0/A1/G/K/N and exact sparse 16-state inverse constructed once, excluded from per-query timings',
                             'terminal phase supplied as input; full original propagation timed separately as source_forward_ms',
                             'same minimal L at n=L+4 or L+1 at n>=L+5 saved gate register input to both algorithms'],
            'cases':cases}
    Path(__file__).with_name('PREFIX630_native_phase_suffix_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    for pattern in ('one','rational','zero_mix'):
        print(pattern,[(x['n'],x['L'],x['ratio_synthetic_to_inverse']) for x in cases if x['mode']==pattern])
    print('ALL_ASSERTIONS_PASS',len(cases),'cases')
