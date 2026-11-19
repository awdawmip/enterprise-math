#!/usr/bin/env python3
"""Minimum certified even order for the existing table-free short-step transport."""
import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha1
import json
from math import comb, gcd, isqrt
from pathlib import Path
from statistics import median
import sys
from time import perf_counter_ns
import tracemalloc


@dataclass(frozen=True)
class Source:
    n: int
    multiplier: int
    root: int
    remainder: int


def source(n, m):
    j = isqrt(m*n)
    return Source(n, m, j, m*n-j*j)


def modules(repo):
    files = {'brc_table_free_tail':'aaef03c9d8e68de5ace75b6736d1169faa4b2918',
             'brc_pairwise_multiplier_transport':'ae93cbf1f706654876801c1a5827d3cdcc62c9a3'}
    for name, pin in files.items():
        data = (repo/'src'/'enterprise_math'/(name+'.py')).read_bytes()
        assert sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest() == pin
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_table_free_tail, brc_pairwise_multiplier_transport
    return brc_table_free_tail,brc_pairwise_multiplier_transport


def atan_bracket(z, scale):
    value = Fraction(0)
    power = z
    terms = 0
    while True:
        term = Fraction((-1)**terms, (2*terms+1)*power)
        if abs(term)*scale<=1:
            return min(value,value+term),max(value,value+term),terms
        value += term
        terms += 1
        power *= z*z


@lru_cache(maxsize=None)
def pi_bounds(bits):
    denom=1<<(bits+2)
    l5,u5,n5=atan_bracket(5,64*denom)
    l239,u239,n239=atan_bracket(239,64*denom)
    L=16*l5-4*u239
    U=16*u5-4*l239
    lo=(L.numerator*denom)//L.denominator
    hi=-((-U.numerator*denom)//U.denominator)
    assert 3*denom<lo<hi<4*denom and hi-lo<=4
    return lo,hi,denom,n5+n239,max(L.denominator.bit_length(),U.denominator.bit_length())


def charge(stats, name, *operands):
    if stats is not None:
        stats[name]+=1
        stats['max_materialized_comparison_bits']=max(stats['max_materialized_comparison_bits'],
                                                       *(v.bit_length() for v in operands))


def bounds(root,a,b,k,pi_num,pi_den,upper,stats):
    # Returns a sufficient strict reject when upper, a sufficient accept otherwise.
    # h/m reduced to a/b. The equality case of either auxiliary comparison is safe.
    if a==b:
        left=root*root
        right=(k+1)**2
    else:
        if stats is not None:
            stats['integer_base_power_calls_in_proxies']+=1+int(a!=1)
        numerator_power=pow(a,k+1) if a!=1 else 1
        left=(root*numerator_power)**2
        right=((2*b-a)*(k+1)*pow(b,k))**2
    if upper:
        lhs=32*k*pi_den*left
        rhs=pi_num*(32*k*k+8*k+1)*right
        charge(stats,'outward_reject_tests',lhs,rhs)
        return lhs>=rhs
    lhs=32*(k+1)*pi_den*left
    rhs=pi_num*(32*k*k+40*k+9)*right
    charge(stats,'outward_accept_tests',lhs,rhs)
    return lhs<=rhs


def exact_catalan(j,a,b,k,stats=None):
    if stats is not None:
        stats['integer_base_power_calls_in_exact_tests']+=1+int(a!=1)
    central=comb(2*k,k)
    coefficient=central//(k+1)
    right=(2*b-a)*pow(4*b,k)
    left=j*coefficient*(pow(a,k+1) if a!=1 else 1)
    charge(stats,'catalan_tests',left,right,central)
    if stats is not None:
        stats['largest_binomial_order']=max(stats['largest_binomial_order'],k)
        stats['materialized_central_binomial_bits']+=central.bit_length()
    return left<=right


def minimum_even(root,m,h,stats=None):
    if any(isinstance(t,bool) or not isinstance(t,int) for t in (root,m,h)):
        raise ValueError('integral state and step required')
    if root<0 or h not in (1,2) or m<h:
        raise ValueError('outside the frozen alternating-tail domain')
    g=gcd(m,h)
    a,b=h//g,m//g
    left,right=root*a**3,8*(2*b-a)*b*b
    charge(stats,'degree_two_fixed_tests',left,right)
    if left<=right:
        return 2
    if a==b:
        high=1<<((2*root.bit_length()+2)//3)
    else:
        high=4
        while not bounds(root,a,b,high,3,1,False,stats):
            high*=2
    bits=3*high.bit_length()+7
    before=pi_bounds.cache_info().misses if stats is not None else 0
    lo_pi,hi_pi,den,terms,internal_bits=pi_bounds(bits)
    if stats is not None:
        stats['largest_upper_degree']=max(stats['largest_upper_degree'],high)
        stats['largest_dyadic_denominator_bits']=max(stats['largest_dyadic_denominator_bits'],den.bit_length())
        if pi_bounds.cache_info().misses>before:
            stats['pi_series_terms_built']+=terms
            stats['largest_final_Machin_denominator_bits']=max(stats['largest_final_Machin_denominator_bits'],internal_bits)
    # Index 1 (=degree 2) is known to fail. high is proven to pass.
    lo,hi=1,high//2
    while hi-lo>1:
        mid=(lo+hi)//2
        if bounds(root,a,b,2*mid,lo_pi,den,False,stats):
            hi=mid
        else:
            lo=mid
    E=2*hi
    k=E-2
    if k==2 or bounds(root,a,b,k,hi_pi,den,True,stats):
        return E
    return k if exact_catalan(root,a,b,k,stats) else E


def exact_bisect(root,m,h,stats=None):
    d=gcd(m,h)
    a,b=h//d,m//d
    lo,hi=0,1
    while not exact_catalan(root,a,b,2*hi,stats):
        lo,hi=hi,2*hi
    while hi-lo>1:
        mid=(lo+hi)//2
        if exact_catalan(root,a,b,2*mid,stats):
            hi=mid
        else:
            lo=mid
    return 2*hi


def scan(frozen,state,h):
    k=2
    while not frozen.two_correction_certificate(state.root,state.multiplier,h,k):
        k+=2
    return k


def state_pair(s):
    return s.root,s.remainder


def direct(s,h):
    if s.multiplier<h or s.root**2+s.remainder != s.multiplier*s.n or not 0<=s.remainder<=2*s.root:
        raise ValueError('invalid source')
    t=s.multiplier+h
    val=t*s.n
    r=isqrt(val)
    out=(r,val-r*r)
    assert out[0]**2+out[1]==val and 0<=out[1]<=2*out[0]
    return out


def prime(n):
    if n%2==0:
        return n==2
    return n>=3 and all(n%i for i in range(3,isqrt(n)+1,2))


def fixed_cases():
    # Every timed n is specified by, and independently checked against, its factors.
    groups={'small-order':[(1009,1013,48+i,1+(i%2)) for i in range(8)],
            'diagonal':[(3,q,1+i%2,1+i%2) for i,q in enumerate((1009,2003,4001,8009,16001,32003,64007,128021))],
            'large-order-diagonal':[(3,q,1+(i%2),1+(i%2)) for i,q in enumerate((1000003,1000033,1000037,1000039))],
            'interior':[(1009,1013,3+i%4,1+i%2) for i in range(8)]}
    for cases in groups.values():
        for p,q,m,h in cases:
            assert prime(p) and prime(q) and m>=h
    return groups


def direct_cases(frozen,pair):
    primes=(3,5,7,11,13,17,19,23,29,31,37,41,43,47)
    counts=Counter()
    corrections=Counter()
    selected=Counter()
    for i,p in enumerate(primes):
        for q in primes[i:]:
            for h in (1,2):
                for m in range(h,65):
                    s=source(p*q,m)
                    ledger=Counter()
                    k=minimum_even(s.root,m,h,ledger)
                    prev=scan(frozen,s,h)
                    assert k==prev==exact_bisect(s.root,m,h)
                    out=frozen.transport_certified_tail(s,m+h,degree=k)
                    assert state_pair(out)==direct(s,h)==state_pair(pair.transport_multiplier_root_state(s,m+h))
                    assert out.target_value==(m+h)*s.n and 0<=out.correction_steps<=2
                    assert ledger['catalan_tests']<=1
                    counts['states']+=1
                    counts['selector_expensive_comparisons']+=ledger['catalan_tests']
                    counts['degree_two_tests']+=ledger['degree_two_fixed_tests']
                    counts['outward_probes']+=ledger['outward_reject_tests']+ledger['outward_accept_tests']
                    counts['linear_frozen_certificate_calls_for_selection']+=k//2
                    selected[k]+=1
                    corrections[out.correction_steps]+=1
    return {'counts':counts,'orders':selected,'corrections':corrections}


def near_threshold(frozen,pair):
    out=[]
    for m,h,k in [(1,1,2),(2,2,2),(3,2,16),(4,2,8),(5,1,6)]:
        g=gcd(m,h);a,b=h//g,m//g
        threshold=Fraction((2*b-a)*pow(4*b,k),pow(a,k+1)*(comb(2*k,k)//(k+1)))
        j=threshold.numerator//threshold.denominator
        for target in (j,j+1):
            # Find an actual odd semiprime in the required source square shell.
            lower=(target**2+3*m-1)//(3*m)
            upper=((target+1)**2-1)//(3*m)
            # At very small roots 3q need not occur; other odd prime pairs are included.
            found=next(((3,q) for q in range(max(3,lower)|1,upper+1,2) if prime(q)),None)
            if found is None:
                found=next(((p,q) for p in (5,7,11,13) for q in range(3,41,2)
                            if prime(q) and isqrt(m*p*q)==target),None)
            assert found is not None
            s=source(found[0]*found[1],m)
            pi_bounds.cache_clear()
            ledger=Counter()
            chosen=minimum_even(s.root,m,h,ledger)
            assert s.root==target and chosen==scan(frozen,s,h)
            assert frozen.two_correction_certificate(target,m,h,k)==(target<=threshold)
            value=frozen.transport_certified_tail(s,m+h,degree=chosen)
            assert state_pair(value)==direct(s,h)==state_pair(pair.transport_multiplier_root_state(s,m+h))
            out.append({'odd_prime_factors':found,'m':m,'h':h,'test_order':k,'integer_root':target,
                        'degree_threshold':str(threshold),'original_degree_passes':target<=threshold,
                        'selected':chosen,'ledger':dict(ledger),'corrections':value.correction_steps})
    return out


def algebraic_checks():
    plo,phi,den,terms,_=pi_bounds(70)
    pl,pu=Fraction(plo,den),Fraction(phi,den)
    for k in range(1,257):
        f=lambda k,t:Fraction(4*k+1,4)+Fraction(1,32*(k+t))
        for t in (0,1):
            diff=(2*k+1)**2*f(k+1,t)-4*(k+1)**2*f(k,t)
            exact=Fraction((12*t-3)*(k+t)-4*(t-1)**2,32*(k+t)*(k+t+1))
            assert diff==exact and (diff>0)==(t==1)
        B=Fraction(comb(2*k,k),4**k)
        assert pu*f(k,1)*B*B < 1 < pl*f(k,0)*B*B
        C=comb(2*k,k)//(k+1)
        assert (C&-C).bit_length()-1 == (k+1).bit_count()-1
    return {'rational_Wallis_sandwich_orders':256,
            'Machin_series_terms_at_70_bits':terms,
            'primitive_Machin_argument_check':(476*239+480,480*239-476)}


def large_semiprime(frozen,pair):
    factors=[]
    for e in (61,89):
        assert prime(e)
        M=(1<<e)-1
        u=4
        for _ in range(e-2):
            u=(u*u-2)%M
        assert u==0
        factors.append(M)
    n=factors[0]*factors[1]
    runs=[]
    for m,h in ((1,1),(2,2),(3,2),(32,1)):
        pi_bounds.cache_clear()
        s=source(n,m);meter=Counter()
        k=minimum_even(s.root,m,h,meter)
        g=gcd(m,h);a,b=h//g,m//g
        lo,hi,den,_,_=pi_bounds(3*meter['largest_upper_degree'].bit_length()+7)
        assert bounds(s.root,a,b,k,lo,den,False,None)
        assert bounds(s.root,a,b,k-2,hi,den,True,None)
        outcome={'source_multiplier':m,'step':h,'root':s.root,'least_degree':k,
                 'ledger':dict(meter),'full_transport_executed':k<1000}
        if k<1000:
            assert frozen.two_correction_certificate(s.root,m,h,k)
            assert not frozen.two_correction_certificate(s.root,m,h,k-2)
            full=frozen.transport_certified_tail(s,m+h,degree=k)
            assert state_pair(full)==direct(s,h)==state_pair(pair.transport_multiplier_root_state(s,m+h))
            outcome['corrections']=full.correction_steps
        runs.append(outcome)
    return {'prime_exponents_via_Lucas_Lehmer':[61,89],'bits':n.bit_length(),'runs':runs}


def warm_reset(frozen,pair):
    pi_bounds.cache_clear()
    frozen.binomial_half_coefficients.cache_clear()
    frozen.scaled_even_truncation.cache_clear()
    pair.pairwise_scale_constant.cache_clear()


def reproducible_cost(frozen,pair):
    groups={}
    for name,cases in fixed_cases().items():
        runs=[]
        for alg in ('frozen-linear','catalan-binary','wallis'):
            warm_reset(frozen,pair)
            stats=Counter()
            orders=[]
            output=[]
            for p,q,m,h in cases:
                s=source(p*q,m)
                if alg=='frozen-linear':
                    k=scan(frozen,s,h)
                    stats['native_selection_certificate_calls']+=k//2
                elif alg=='catalan-binary':
                    k=exact_bisect(s.root,m,h,stats)
                else:
                    k=minimum_even(s.root,m,h,stats)
                v=frozen.transport_certified_tail(s,m+h,degree=k)
                stats['native_final_certificate_calls']+=1
                stats['odd_width_corrections']+=v.correction_steps
                orders.append(k);output.append(state_pair(v))
            runs.append({'algorithm':alg,'degrees':orders,'ledger':dict(stats),
                         'degree_vector_cache_cold_misses':frozen.scaled_even_truncation.cache_info().misses,
                         'degree_vector_cache_hits':frozen.scaled_even_truncation.cache_info().hits,
                         'pi_cache_entries':pi_bounds.cache_info().currsize,
                         'pi_cache_hits':pi_bounds.cache_info().hits})
        assert all(r['degrees']==runs[0]['degrees'] for r in runs)
        groups[name]=runs
    return groups


def benchmark(frozen,pair):
    results={}
    for name,cases in fixed_cases().items():
        ss=[(source(p*q,m),h) for p,q,m,h in cases]
        known=[minimum_even(s.root,s.multiplier,h) for s,h in ss]
        def repeat(alg):
            for i,(s,h) in enumerate(ss):
                if alg=='isqrt':
                    direct(s,h)
                elif alg=='pairwise':
                    state_pair(pair.transport_multiplier_root_state(s,s.multiplier+h))
                else:
                    if alg=='frozen-linear':
                        k=scan(frozen,s,h)
                    elif alg=='catalan-binary':
                        k=exact_bisect(s.root,s.multiplier,h)
                    elif alg=='wallis':
                        k=minimum_even(s.root,s.multiplier,h)
                    else:
                        k=known[i]
                    state_pair(frozen.transport_certified_tail(s,s.multiplier+h,degree=k))
        algs=['frozen-linear','catalan-binary','wallis','frozen-known-order','isqrt','pairwise']
        cold={a:[] for a in algs};hot={a:[] for a in algs}
        for r in range(9):
            for a in algs[r%len(algs):]+algs[:r%len(algs)]:
                warm_reset(frozen,pair)
                start=perf_counter_ns();repeat(a)
                cold[a].append((perf_counter_ns()-start)/len(ss))
                start=perf_counter_ns()
                for _ in range(12):
                    repeat(a)
                hot[a].append((perf_counter_ns()-start)/(12*len(ss)))
        result={}
        for a in algs:
            warm_reset(frozen,pair)
            tracemalloc.start();repeat(a)
            cold_peak=tracemalloc.get_traced_memory()[1];tracemalloc.stop()
            tracemalloc.start();repeat(a)
            hot_peak=tracemalloc.get_traced_memory()[1];tracemalloc.stop()
            result[a]=[round(median(cold[a])),round(median(hot[a])),cold_peak,hot_peak]
        results[name]=result
    return {'columns':['median_cold_ns_per_state','median_hot_ns_per_state','cold_batch_peak_bytes','hot_batch_peak_bytes'],
            'python':sys.version.split()[0],'cases':fixed_cases(),'results':results}


def main():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--repo',type=Path)
    cli.add_argument('--out',type=Path)
    cli.add_argument('--benchmark',action='store_true')
    args=cli.parse_args()
    repo=args.repo or next((p for p in (Path.cwd(),*Path(__file__).resolve().parents)
                            if (p/'src/enterprise_math/brc_table_free_tail.py').is_file()),None)
    if repo is None:
        raise SystemExit('Use --repo /path/to/enterprise-math')
    frozen,pair=modules(repo)
    if args.benchmark:
        res=benchmark(frozen,pair)
    else:
        res={'Wallis_checks':algebraic_checks(),'large_semiprime':large_semiprime(frozen,pair),
             'bounded_semiprime_domain':direct_cases(frozen,pair),
             'actual_boundary_semiprimes':near_threshold(frozen,pair),
             'cost_groups':reproducible_cost(frozen,pair)}
    raw=json.dumps(res,sort_keys=True,indent=2)+'\n'
    if args.out:
        args.out.write_text(raw,encoding='utf-8')
    else:
        sys.stdout.write(raw)

if __name__=='__main__':
    main()
