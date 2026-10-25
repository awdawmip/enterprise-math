"""R288: exact checks of one-step BRC tail propagation and radical-free gap factors.

Finite checks are corroboration only; see R288_AUTHOR_PROOF.md for all-length proofs.
The model is the positive ordered six-edge auxiliary BRC automaton, not native X6.
"""
import json
from collections import defaultdict
from math import comb
from decimal import Decimal, getcontext

MAX_N=700
CHECK_KERNEL_N=155
MAX_M=24
TRANSITIONS = (
    ((2,-1,-1),(2,+1,-1)),
    ((0,-1,-1),(0,+1,-1)),
    ((1,+1,+1),(2,+1,-1)),
)
DEG=MAX_N//2+3

def mul(a,b,deg=DEG):
    out=[0]*(deg+1)
    for i, ai in enumerate(a[:deg+1]):
        if not ai: continue
        for j,bj in enumerate(b[:deg+1-i]):
            if bj: out[i+j]+=ai*bj
    return out

def polypow(p,n,deg=DEG):
    out=[1]+[0]*deg
    while n:
        if n&1: out=mul(out,p,deg)
        n//=2
        if n: p=mul(p,p,deg)
    return out

# Define h by its *positive* formal fixed point, and T=u/x=(1+y)(1+h).
h=[0]*(DEG+1)
for d in range(1,DEG+1):
    total=int(d==4)
    for shift,weight in ((1,1),(2,2),(3,1),(4,1)):
        if d>=shift: total+=weight*h[d-shift]
    for shift,weight in ((1,1),(2,2),(3,1)):
        if d>=shift:
            total+=weight*sum(h[i]*h[d-shift-i] for i in range(d-shift+1))
    h[d]=total
assert h[:4]==[0,0,0,0]
assert all(x>0 for x in h[4:])
one_plus_h=h.copy(); one_plus_h[0]+=1
one_plus_y=[1,1]
T=mul(one_plus_y,one_plus_h)

# Delta_m^+ / x^(m+2) = (1+y)^m (1+h)^(m+1) [1-2y-y(1+y)h].
# Delta_m^- / x^(m+2) = (1+y)^(m-2) (1+h)^(m-1) [1-y(1+y)(1+h)].
def gap_series(eps,m):
    if eps==1:
        B=[1,-2]+[0]*(DEG-1)
        for i,v in enumerate(h):
            if i+1<=DEG: B[i+1]-=v
            if i+2<=DEG: B[i+2]-=v
        core=mul(polypow(one_plus_y,m),polypow(one_plus_h,m+1))
    else:
        assert m>=2
        B=[1]+[0]*DEG
        for i,v in enumerate(T):
            if i+1<=DEG: B[i+1]-=v
        core=mul(polypow(one_plus_y,m-2),polypow(one_plus_h,m-1))
    return mul(core,B)

base_plus=gap_series(1,13)
base_minus=gap_series(-1,11)
next_plus=gap_series(1,14)
next_minus=gap_series(-1,12)
assert next_plus==mul(base_plus,T)
assert next_minus==mul(base_minus,T)

families={(eps,m):[] for eps in (1,-1) for m in range(1,MAX_M+2)}
states={(0,1,0,False):1}
raw_words_checked=0
negative_witnesses={}
checks_gaps=0
positive_base_layers={'+13':0,'-11':0}
min_base_gap={'+13':None,'-11':None}
for n in range(MAX_N+1):
    P=defaultdict(int)
    for (q,eps,k,last_zero),count in states.items():
        if q==0: P[(eps,k)]+=count
    if n<=14:
        brute=defaultdict(int)
        for word in range(1<<n):
            q,eps,k,lz=0,1,0,False
            for bpos in range(n-1,-1,-1):
                b=(word>>bpos)&1
                if lz and b==0: break
                q, eta, step=TRANSITIONS[q][b]
                eps,k,lz=eta*eps,eta*k+step,b==0
            else:
                if q==0: brute[(eps,k)]+=1
        assert dict(brute)==dict(P),(n,'raw mismatch')
        raw_words_checked+=1<<n
    for eps,m in families:
        families[(eps,m)].append(P[(eps,-m)])
    for eps,m,name,coeffs in ((1,13,'+13',base_plus),(-1,11,'-11',base_minus),
                               (1,14,'+14',next_plus),(-1,12,'-12',next_minus)):
        j=(n-m-2)//2
        expected=coeffs[j] if n>=m+2 and (n-m)%2==0 else 0
        gap=P[(eps,-m)]-P[(eps,-m-2)]
        assert gap==expected,(n,eps,m,expected,gap)
        checks_gaps+=1
        if name in positive_base_layers and n>=m+2 and (n-m)%2==0:
            assert gap>=0,(n,eps,m,gap)
            positive_base_layers[name]+=1
            old=min_base_gap[name]
            min_base_gap[name]=gap if old is None else min(gap,old)

    if n in (23,24,19,20):
        witness={23:(1,11),24:(1,12),19:(-1,9),20:(-1,10)}[n]
        eps,m=witness
        negative_witnesses[f'{eps}:{m}:{n}']=P[(eps,-m)]-P[(eps,-m-2)]
    if n<MAX_N:
        nxt=defaultdict(int)
        for (q,eps,k,last_zero),count in states.items():
            for bit,(qnext,eta,step) in enumerate(TRANSITIONS[q]):
                if last_zero and bit==0: continue
                nxt[(qnext,eta*eps,eta*k+step,bit==0)]+=count
        states=nxt

# Independent direct F_{m+1} = u F_m test; the m=1 negative family isn't in stated scope.
one_step_checks=0
for eps in (1,-1):
    for m in range(1 if eps==1 else 2,MAX_M+1):
        source=families[(eps,m)]
        target=families[(eps,m+1)]
        for n in range(CHECK_KERNEL_N+1):
            rhs=sum(T[j]*source[n-1-2*j] for j in range(n//2) if n-1-2*j>=0)
            assert target[n]==rhs,('one-step',eps,m,n,target[n],rhs)
            one_step_checks+=1

# The two earlier candidate base indices fail; hence 13+ and 11- are
# minimal possible starting points for a *universal one-step* tail monotonicity.
assert all(v<0 for v in negative_witnesses.values()),negative_witnesses

# Leading asymptotic constants for W_m(y)=[Delta_m/x^(m+2)] under rho.
getcontext().prec=60
five=Decimal(5); sqrtfive=five.sqrt()
phi=(1+sqrtfive)/2
rho=(3-sqrtfive)/2
beta=five.sqrt().sqrt()/phi
pi=Decimal('3.141592653589793238462643383279502884197169399375105820974944')

def leading_const(eps,m):
    derivative=(phi**m)*(rho**2)*(Decimal(m)-2*phi)/(1+rho) if eps==1 else \
               (phi**(m-2))*(rho*Decimal(m)-1)/(1+rho)
    return beta*derivative/(2*pi.sqrt())

asymptotic={}
for eps,m,label,ser in ((1,13,'plus13',base_plus),(-1,11,'minus11',base_minus)):
    c=leading_const(eps,m)
    assert c>0
    j=300
    empirical=Decimal(ser[j])*(rho**j)*(Decimal(j)**3).sqrt() # sqrt(j^3)=j^(3/2)
    asymptotic[label]={'constant_y_j':str(c),'j':j,
                       'scaled_coefficient_j':str(empirical),
                       'scaled_over_constant':str(empirical/c)}

result={
 'schema':'EM_R288_ONE_STEP_POSITIVE_TAIL_AND_SINGULAR_COEFFICIENT_V1',
 'status':'PASS',
 'source_model':'ordered positive six-edge auxiliary BRC; exact affine effect; clean no 00; terminal q0',
 'proof_claims':'one-step u kernel and radical-free gap products are algebraic all-length identities; fixed-m asymptotic via singularity analysis',
 'max_dp_n':MAX_N,
 'raw_word_length_max':14,
 'raw_words_checked':raw_words_checked,
 'one_step_kernel_max_n':CHECK_KERNEL_N,
 'one_step_kernel_exact_comparisons':one_step_checks,
 'four_gap_factor_exact_compares':checks_gaps,
 'finite_base_positivity_layers':positive_base_layers,
 'finite_base_min_gap':{k:str(v) for k,v in min_base_gap.items()},
 'negative_lower_index_witnesses':negative_witnesses,
 'factor_neighbor_identity':'Delta_m+1 = u Delta_m',
 'conditional_finite_candidate_count':26,
 'four_to_two_base_reduction':{'plus':[13],'minus':[11]},
 'fixed_index_asymptotics':asymptotic,
 'scope_warning':'No all-length positivity proof for base Delta_13^+ or Delta_11^-. No effective global peak N. No official Task Claim or Driver review.',
}
print(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False))
