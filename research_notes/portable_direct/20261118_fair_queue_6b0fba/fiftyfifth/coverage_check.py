"""Finite-law list and entropy checks. Run with Python 3.9+."""
import json
from fractions import Fraction as F
from itertools import combinations
from math import ceil, comb, exp, log, sqrt


TAU = F(1, 4)
DELTA = F(1, 64)
T = TAU + DELTA
NEXT = TAU + 4*DELTA


def subsets(p):
    for size in range(1,p):
        yield from combinations(range(p),size)


def low_set(weights, threshold):
    p, den = len(weights), sum(weights)
    return [j for j,w in enumerate(weights) if p*w < den*threshold]


def lists(weights, K):
    p, den = len(weights), sum(weights)
    cut = T * len(K) * den
    return [x for x in range(p) if p*sum(weights[(k-x)%p] for k in K) <= cut]


def bound_checks():
    cases = hits = equal_positive = 0
    for p in (3,5,7):
        masks = list(subsets(p))
        laws = [[int(i not in E) for i in range(p)] for E in masks]
        laws += [[(i*i+2*d*i+d)%p for i in range(p)] for d in range(1,p)]
        for w in laws:
            E = low_set(w,NEXT)
            for K in masks:
                u = len(K)
                overlap = ceil((1-T/NEXT)*u)
                L = lists(w,K)
                assert len(L)<= min(p,u*len(E)//overlap)
                assert all(sum((k-x)%p in E for k in K)>=overlap for x in L)
                cases += 1
                hits += len(L)
                equal_positive += bool(L) and len(L)==min(p,u*len(E)//overlap)
    return dict(law_subset_pairs=cases,listed_residues=hits,positive_equalities=equal_positive)


def d_binary(a,b):
    a,b=float(a),float(b)
    extra = 0 if a==0 else a*log(a/b)
    return extra if a==1 else extra+(1-a)*log((1-a)/(1-b))


def correlated_holes():
    p,u=101,11
    # beta=1/2, beta'=1/3, with exact lattice thresholds.
    assert (u-1)**2 < p <= u**2 and u**3 < p*p
    K=tuple(range(u))
    total=[0]*p
    true_hit, total_list, signatures=0,0,set()
    radius=int(T*u*(p-u)/p)
    for y in range(p):
        w=[int((h+y)%p not in K) for h in range(p)]
        L=lists(w,K)
        assert set(L)=={(y+j)%p for j in range(-radius,radius+1)}
        true_hit+=y in L
        total_list+=len(L)
        signatures.add(tuple(L))
        for h,weight in enumerate(w):
            total[(y+h)%p]+=weight
    assert total==[0]*u+[p]*(p-u)
    assert true_hit==p and len(signatures)==p
    alpha=F(u,p)
    freq=F(total_list,p*p)
    # Approaching the strict low-mass threshold from below.
    near=[]
    for scale in (1,16,256,4096):
        floor=TAU*(1-F(1,scale))
        low=floor/p
        high=(1-u*low)/(p-u)
        H=-sum(float(v)*log(float(v)) for v in [low]*u+[high]*(p-u) if v)
        assert low<TAU/p and d_binary(TAU*alpha,alpha)<log(p)-H
        near.append(round(log(p)-H,12))
    return dict(p=p,u=u,nonempty_low_residues=low_set(total,TAU),
                true_hit_probability=str(F(true_hit,p)), list_radius=radius,
                list_size=2*radius+1, distinct_list_messages=len(signatures),
                list_event_uniform_mass=str(freq),event_KL_nats=round(-log(float(freq)),12),
                MI_list_and_Y_nats=round(log(p),12),
                sharp_entropy_floor_nats=round(d_binary(TAU*alpha,alpha),12),
                approaching_deficits_nats=near)


def histograms():
    # Y fair, B_0=Bernoulli(1/4), B_1=Bernoulli(3/4).
    answers=[]
    last=-1
    for n in (1,2,4,8,16,32,64):
        residual=0.
        error=F(0)
        for j in range(n+1):
            a=F(comb(n,j)*3**(n-j),2*4**n)
            b=F(comb(n,j)*3**j,2*4**n)
            error+=min(a,b)
            residual-=float(a)*log(float(a/(a+b)))+float(b)*log(float(b/(a+b)))
        MI=log(2)-residual
        assert MI>last and float(error)<=0.5*(sqrt(3)/2)**n*(1+1e-12)
        h=-.25*log(.25)-.75*log(.75)
        if n<=8:
            # Each ordered word is enumerated without binning it in advance.
            full=0.
            for word in range(2**n):
                bits=bin(word).count("1")
                a,b=F(3**(n-bits),2*4**n),F(3**bits,2*4**n)
                full+=float(a)*log(float(2*a/(a+b)))+float(b)*log(float(2*b/(a+b)))
            assert abs(full-MI)<1e-12
        answers.append(dict(n=n,information_nats=round(MI,12),
                            ordered_entropy_nats=round(n*h+MI,12),
                            optimal_classification_error=str(error)))
        last=MI
    return answers


def valid_large_group():
    # Lucas-Lehmer, followed by source-constant checks using integer inequalities.
    p=2**127-1
    s=4
    for _ in range(125):
        s=(s*s-2)%p
    assert s==0 and 64**4<p and 384**8<p
    # 2e/delta<384 because e<3. Chernoff condition at n=1 fails:
    # delta^2 p^(-3/4)/2 < 1 hence p exp(-... ) >= p/e > delta/100.
    u0=2**60
    assert u0*u0<p and 5*(p-u0)<16*p
    return dict(p=str(p),omitted_interval_size=str(u0),beta_prime="1/2",beta="3/4",
                delta="1/64",tau="1/4", law_MI_nats=0, terminal_prob_each="1/p",
                original_chernoff_at_one_trial=False)


if __name__=="__main__":
    print(json.dumps(dict(local_counts=bound_checks(),correlated_holes=correlated_holes(),
                          two_law_histogram=histograms(),valid_transfer=valid_large_group()),indent=2))
