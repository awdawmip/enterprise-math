#!/usr/bin/env python3
"""EC49FWK: exact one-erasure/one-error probe bounds for BRC16943 ten-cycle.
Independent implementation of the pinned EC49FWJ P10 four-slope predicate.
Uses exact 10-bit integers and exhausts all 2^10 probe sets.
"""
import json
from collections import defaultdict
from itertools import combinations
from math import gcd

N = 10
FULL = (1 << N) - 1
SLOPES = {(0,0): {3}, (0,1): {0,3,4,'inf'},
          (1,0): {2,3,4,'inf'}, (1,1): {2,3}}

def reflect(word, center):
    return sum(1 << ((center-j) % N) for j in range(N) if word & (1 << j))

def spectrum(word):
    return tuple((word ^ reflect(word,c)).bit_count() for c in range(N))

def p10(h,n):
    h %= N; n %= N
    if h % 5 == n % 5 == 0:
        return False
    slope = 'inf' if h % 5 == 0 else n * pow(h % 5,-1,5) % 5
    return slope in SLOPES[(h%2,n%2)]

def from_direction(a,b):
    h0,n0 = next((h,n) for h in range(N) for n in range(N)
                 if ((b-a)*h - a*n+1)%N == 0)
    return sum(1<<t for t in range(N) if p10(h0+a*t,n0+(b-a)*t))

def fibers(words,weight):
    f = defaultdict(list)
    for w in words:
        key = (spectrum(w),w.bit_count()) if weight else spectrum(w)
        f[key].append(w)
    return tuple(tuple(sorted(v)) for v in f.values())

def patterns(f):
    d = set()
    for group in f:
        d.update(a^b for a,b in combinations(group,2))
    return d

def mindist_on(Q, ds):
    return min(((Q & d).bit_count() for d in ds), default=N+1)

def optimum_fixed(ds,required_distance):
    feasible = [q for q in range(1<<N) if mindist_on(q,ds)>=required_distance]
    if not feasible:
        return {'minimum':None,'number_at_minimum':0,'optimal_sets':[]}
    min_n = min(q.bit_count() for q in feasible)
    optimal = sorted(q for q in feasible if q.bit_count()==min_n)
    return {'minimum':min_n,'number_at_minimum':len(optimal),
            'optimal_sets':[[i for i in range(N) if q>>i&1] for q in optimal]}

def optimum_adaptive(f,required_distance):
    worst = 0
    for group in f:
        ds = [a^b for a,b in combinations(group,2)]
        opt = optimum_fixed(ds,required_distance)['minimum']
        if opt is None:
            return None
        worst = max(worst,opt)
    return worst

def solve_domain(words):
    ret = {}
    for weight in (False,True):
        f=fibers(words,weight);ds=patterns(f)
        fixed_no=optimum_fixed(ds,1)
        fixed_erase=optimum_fixed(ds,2)
        fixed_error=optimum_fixed(ds,3)
        ret['defect_plus_weight' if weight else 'defect_only']={
            'fibers':len(f),'nonzero_difference_patterns':len(ds),
            'min_difference_support':min(d.bit_count() for d in ds),
            'fixed_zero_erasure': {'minimum':fixed_no['minimum'], 'number_at_minimum':fixed_no['number_at_minimum']},
            'fixed_one_erasure':fixed_erase,
            'adaptive_one_erasure_worst':optimum_adaptive(f,2),
            'one_adversarial_bit_error_possible':fixed_error['minimum'] is not None,
        }
    return ret

def optimal_physical_counts(kind, m, F):
    """Construct minimum redundancy n_j for all ten-cycle support patterns."""
    n = [0] * N
    groups = ([{j,j+5} for j in range(5)] if kind=='universal'
              else [{1,4,6,9},{2,7},{3,8}])
    if m > min(len(g)*F for g in groups):
        return None
    for group in groups:
        remaining=m
        for j in sorted(group):
            take=min(F,remaining)
            n[j]=take
            remaining-=take
        assert remaining==0
    return n

def crt_sites(counts,V):
    """For every j use distinct available v layers; CRT t = v+11*((j-v) mod 10)."""
    sites=[]
    for j,count in enumerate(counts):
        for v in V[:count]:
            t=(v + 11*((j-v) % N)) % 110
            assert t%10==j and t%11==v
            sites.append(t)
    assert len(sites)==len(set(sites))
    return sorted(sites)

def physical_results(f,m,F,kind):
    counts=optimal_physical_counts(kind,m,F)
    if counts is None:
        return {'min_samples':None,'reason':'pairwise support capacity'}
    V=list(range(1,11)) if F==10 else list(range(11))
    sites=crt_sites(counts,V)
    # Every pair in every selected domain fiber achieves at least the target Hamming distance.
    distances=[sum(counts[j] for j in range(N) if (a^b)>>j&1)
               for group in f for a,b in combinations(group,2)]
    assert distances and min(distances)>=m
    if m == 3:
        direct=[sum((((a >> (t % 10)) & 1) != ((b >> (t % 10)) & 1))
                    for t in sites)
                for group in f for a,b in combinations(group,2)]
        assert direct == distances
    # Construction has exact cardinality lower bound: three disjoint frozen families,
    # or five disjoint antipodal pairs for the universal domain.
    expected=(5 if kind=='universal' else 3)*m
    assert len(sites)==expected
    return {'min_samples':expected,'minimum_restricted_distance':min(distances),
            'sample_sites':sites if m==3 else None,
            'multiplicities':counts if m==3 else None}

def main():
    words_all=tuple(range(1<<N))
    words_frozen=tuple(sorted({from_direction(a,b) for a in range(N)
                              for b in range(N) if gcd(gcd(a,b),N)==1}))
    assert len(words_frozen)==50
    universe=solve_domain(words_all)
    restricted=solve_domain(words_frozen)
    for key in ('defect_only','defect_plus_weight'):
        un=universe[key]; fr=restricted[key]
        assert (un['fibers'], un['fixed_zero_erasure']['minimum'],
                un['fixed_one_erasure']['minimum'],
                un['fixed_one_erasure']['number_at_minimum'],
                un['adaptive_one_erasure_worst']) == ((473 if key=='defect_plus_weight' else 272),5,10,1,4)
        assert (fr['fibers'],fr['fixed_zero_erasure']['minimum'],
                fr['fixed_one_erasure']['minimum'],
                fr['fixed_one_erasure']['number_at_minimum'],
                fr['adaptive_one_erasure_worst']) == ((40 if key=='defect_plus_weight' else 38),3,6,6,2)
        assert not un['one_adversarial_bit_error_possible']
        assert not fr['one_adversarial_bit_error_possible']
        assert all(set(s).issuperset({2,3,7,8}) and len(set(s)&{1,4,6,9})==2
                   for s in fr['fixed_one_erasure']['optimal_sets'])
        assert un['fixed_one_erasure']['optimal_sets']==[list(range(N))]
    # Witness from the pinned upstream file, equality under indexed Delta and weight.
    x=sum(1<<v for v in (0,1,2,6,7))
    y=sum(1<<v for v in (1,2,5,6,7))
    assert spectrum(x)==spectrum(y) and x.bit_count()==y.bit_count()==5
    assert [i for i in range(10) if (x^y)>>i&1]==[0,5]
    for kind, words in (('universal', words_all),('frozen_P10',words_frozen)):
        for weight in (False,True):
            fs=fibers(words,weight)
            for F in (10,11):
                for m in range(1,2*F+1):
                    physical_results(fs,m,F,kind)
                assert optimal_physical_counts(kind,2*F+1,F) is None
    physics={}
    for F in (10,11):
        physics[f'F_{F}']={}
        for kind,words in (('universal',words_all),('frozen_P10',words_frozen)):
            fs=fibers(words,True)
            physics[f'F_{F}'][kind]={
                'all_m_1_through':2*F,
                'optimal_sample_formula':'5*m' if kind=='universal' else '3*m',
                'm_2_one_erasure':physical_results(fs,2,F,kind)['min_samples'],
                'm_3_one_bit_error':physical_results(fs,3,F,kind),
                'm_above_capacity':2*F+1}
    result={
      'scientific_pin':'BRC16943','status':'ALL PASS',
      'domain':{'universal_words':1024,'frozen_P10_words':50,'source_primitive_directions':72},
      'observation':'complete indexed reflection defect spectrum, optionally ten-bit support weight, plus fixed/adaptive binary membership probes',
      'failure_model':'up to r known-position erasures or e adversarial bit flips; required pairwise Hamming distance m=r+1 or m=2e+1',
      'universal':universe,'frozen_P10':restricted,
      'crt_replicated_physical_probe_optima':physics,
      'witness_distance_two':{'a':[0,1,2,6,7],'b':[1,2,5,6,7],'difference':[0,5],'same_weight':5},
      'limit':'Finite ten-cycle/CRT auxiliary certificate only; no native Farey transition F or downstream Y established; no independent review.'}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
