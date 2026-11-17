#!/usr/bin/env python3
"""Exact finite checks for the scoped R5 one-merger rigidity theorem.

Scientific model: two measures, a single shared source LR=1 at t=1,
stop/declare P,Q or continue once to a terminal signal at t=2.
All arithmetic is fractions.Fraction; deterministic behavior is enumerated
completely only for the declared small examples. The all-real theorem
is proved separately in RESEARCH.md.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import random

ZERO, ONE = F(0), F(1)
RHO = (F(1,2), F(1,2))
A = ((F(1,4),F(1,8)), (F(1,2),F(1,2)), (F(1,4),F(3,8)))
B_DISTINCT = ((F(1,3),F(1,6)), (F(1,3),F(1,3)), (F(1,3),F(1,2)))
B_SAFE = ((F(1,4),F(1,8)), (F(1,6),F(1,6)),
          (F(1,3),F(1,3)), (F(1,4),F(3,8)))

def check_channels(channels):
    for C in channels:
        assert all(q>0 and p>0 for q,p in C)
        assert sum((q for q,p in C), ZERO)==ONE
        assert sum((p for q,p in C), ZERO)==ONE

def nu(C):
    d=defaultdict(F)
    for q,p in C: d[p/q]+=q
    return dict(d)

def knots(channels):
    return sorted({ZERO, *(p/q for C in channels for q,p in C)})

def g(C,x):
    return sum((min(p,x*q) for q,p in C), ZERO)

def info(C,x):
    return min(ONE,x)-g(C,x)

def quant_gap(channels,x):
    vals=[info(C,x) for C in channels]
    mean=sum((rho*v for rho,v in zip(RHO,vals)), ZERO)/sum(RHO)
    gap=sum((rho*abs(v-mean) for rho,v in zip(RHO, vals)),ZERO)/2
    return vals,mean,gap

def observation(channels, root_probs, term_p_rates):
    ep=eq=tp=tq=ZERO
    for i,C in enumerate(channels):
        mass=RHO[i]
        stp,stq,cont=root_probs[i]
        assert stp>=0 and stq>=0 and cont>=0 and stp+stq+cont==ONE
        # Stop and declare P: error under Q; stop and declare Q: error under P.
        eq+=mass*stp
        ep+=mass*stq
        tp+=mass*(stp+stq+2*cont)
        tq+=mass*(stp+stq+2*cont)
        for j,(q,p) in enumerate(C):
            rate=term_p_rates[(i,j)]
            assert ZERO<=rate<=ONE
            eq+=mass*cont*q*rate
            ep+=mass*cont*p*(ONE-rate)
    return ep,eq,tp,tq

def lr_observation(channels, root, rates_by_lr):
    rp=[root for _ in channels]
    rates={(i,j):rates_by_lr[p/q] for i,C in enumerate(channels) for j,(q,p) in enumerate(C)}
    return observation(channels,rp,rates)

def full_deterministic_vectors(channels):
    for acts in product('PQC', repeat=len(channels)):
        roots=[(ONE,ZERO,ZERO) if x=='P' else (ZERO,ONE,ZERO) if x=='Q'
               else (ZERO,ZERO,ONE) for x in acts]
        for term_bits in product((ZERO,ONE), repeat=sum(len(C) for C in channels)):
            it=iter(term_bits)
            rates={(i,j):next(it) for i,C in enumerate(channels) for j in range(len(C))}
            yield observation(channels,roots,rates)

def lr_deterministic_vectors(channels):
    lrs=sorted({p/q for C in channels for q,p in C})
    for act in 'PQC':
        root=((ONE,ZERO,ZERO) if act=='P' else
              (ZERO,ONE,ZERO) if act=='Q' else (ZERO,ZERO,ONE))
        for bits in product((ZERO,ONE), repeat=len(lrs)):
            yield lr_observation(channels,root,dict(zip(lrs,bits)))

def dot(w,o): return sum((a*b for a,b in zip(w,o)),ZERO)

def markovize(channels, full_roots, full_terminal_p_rates):
    assert all(nu(C)==nu(channels[0]) for C in channels)
    rho_sum=sum(RHO,ZERO)
    root=tuple(sum((RHO[i]*full_roots[i][a] for i in range(len(channels))),ZERO)/rho_sum for a in range(3))
    continued=sum((RHO[i]*full_roots[i][2] for i in range(len(channels))),ZERO)
    nv=nu(channels[0])
    alpha={}
    for lam,weight in nv.items():
        numerator=sum((RHO[i]*full_roots[i][2]*q*full_terminal_p_rates[(i,j)]
                       for i,C in enumerate(channels)
                       for j,(q,p) in enumerate(C) if p/q==lam),ZERO)
        denominator=continued*weight
        alpha[lam]=numerator/denominator if denominator else ZERO
        assert ZERO<=alpha[lam]<=ONE
    return root,alpha

for channels,expected in [((A,B_SAFE),True),((A,B_DISTINCT),False)]:
    check_channels(channels)
    k=knots(channels)
    same=(nu(channels[0])==nu(channels[1]))
    assert same==expected
    finite_test=all(g(channels[0],x)==g(channels[1],x) for x in k)
    assert finite_test==same
    print('finite_knots', 'SAFE' if same else 'DISTINCT',*[str(x) for x in k])

safe=(A,B_SAFE)
full_count=lr_count=0
for acts in product('PQC',repeat=2):
    roots=[(ONE,ZERO,ZERO) if x=='P' else (ZERO,ONE,ZERO) if x=='Q'
           else (ZERO,ZERO,ONE) for x in acts]
    for bits in product((ZERO,ONE),repeat=7):
        it=iter(bits)
        rates={(i,j):next(it) for i,C in enumerate(safe) for j in range(len(C))}
        root,alphas=markovize(safe,roots,rates)
        lr=lr_observation(safe,root,alphas)
        obs=observation(safe,roots,rates)
        assert lr==obs
        full_count+=1
lr_count=sum(1 for _ in lr_deterministic_vectors(safe))
assert full_count==1152 and lr_count==24
print('safe_full_deterministic_matched',full_count,'seedless_LR_deterministic',lr_count)

rng=random.Random(202610291744)

def simplex3():
    z=[rng.randrange(0,8) for _ in range(3)]
    if not any(z):z[0]=1
    return tuple(F(a,sum(z)) for a in z)

for _ in range(300):
    roots=[simplex3(),simplex3()]
    rates={(i,j):F(rng.randrange(0,12),11) for i,C in enumerate(safe) for j in range(len(C))}
    root,alphas=markovize(safe,roots,rates)
    assert observation(safe,roots,rates)==lr_observation(safe,root,alphas)
print('safe_random_fraction_policies_matched',300)

bad=(A,B_DISTINCT)
vals,mean,gap=quant_gap(bad,ONE)
assert vals==[F(1,8),F(1,6)] and mean==F(7,48) and gap==F(1,96)
w=(F(96),F(96),F(7),F(7))
full_set=list(full_deterministic_vectors(bad))
lr_set=list(lr_deterministic_vectors(bad))
assert len(full_set)==576 and len(lr_set)==24
fmin=min(dot(w,o) for o in full_set)
lmin=min(dot(w,o) for o in lr_set)
assert (fmin,lmin)==(F(109),F(110))
witness=(F(1,12), F(5,6),F(3,2),F(3,2))
assert witness in full_set and dot(w,witness)==F(109)
assert all(dot(w,v)>=F(110) for v in lr_set)
print('distinct_information',*[str(v) for v in vals],'tau',mean,'support_gap',gap)
print('exact_separator_full_LR',fmin,lmin,'witness',*[str(x) for x in witness])
print('full_LR_extreme_vertex_counts',len(full_set),len(lr_set))

# Stress-test the complete signed Bellman formula, including negative error coefficients.
for a,b,c,d in product((-2,-1,0,1,2),repeat=4):
    W=(F(a),F(b),F(c),F(d))
    s=F(min(a,b))+F(c+d)
    G=[]
    for C in bad:
        terminal=sum((min(F(a)*p,F(b)*q) for q,p in C),ZERO)
        G.append(F(c+d)+terminal-F(min(a,b)))
    expected_full=s + sum((RHO[i]*min(ZERO,G[i]) for i in range(2)),ZERO)
    expected_lr=s + min(ZERO,sum((RHO[i]*G[i] for i in range(2)),ZERO))
    assert expected_full == min(dot(W,v) for v in full_set)
    assert expected_lr == min(dot(W,v) for v in lr_set)
print('signed_direction_Bellman_exact_checks',5**4)
print('PASS_EXACT_R5_ONE_MERGER_LR_RIGIDITY')
