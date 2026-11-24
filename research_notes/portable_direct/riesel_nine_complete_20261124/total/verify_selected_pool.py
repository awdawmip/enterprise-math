#!/usr/bin/env python3
"""Exact selected-pool covering minima for eight saved zero-W v15 roots.

The pool is explicitly finite. Its minima are not unrestricted tau lower bounds.
This script uses only the standard library and claims no native BRC execution.
"""
from __future__ import annotations
from functools import lru_cache,reduce
import json
from math import gcd,isqrt,lcm,prod
from pathlib import Path

HERE=Path(__file__).resolve().parent
P=(7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417)


def factors(n):
    result=[];p=2
    while p*p<=n:
        if n%p==0:
            result.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:result.append(n)
    return result


def minimal_clauses(clauses):
    keep=[]
    for clause in sorted(set(clauses),key=lambda x:(x.bit_count(),x)):
        if not any(c&clause==c for c in keep):keep.append(clause)
    return tuple(keep)


def main():
    data=json.loads((HERE/'source_input.json').read_text())
    pool=tuple(data['pool_primes']);orders={int(q):d for q,d in data['exact_orders'].items()}
    certs=data['prime_certificates'];verified=set()
    def verify_prime(q):
        if q in verified:return
        c=certs[str(q)]
        if c['kind']=='trial':assert q>=2 and all(q%d for d in range(2,isqrt(q)+1))
        else:
            assert c['kind']=='lucas_n_minus_one'
            fs={int(p):e for p,e in c['factorization'].items()}
            assert prod(p**e for p,e in fs.items())==q-1
            for p in fs:verify_prime(p)
            w=c['witness'];assert pow(w,q-1,q)==1
            assert all(gcd(pow(w,(q-1)//p,q)-1,q)==1 for p in fs)
        verified.add(q)
    for q in pool:
        verify_prime(q);d=orders[q]
        assert pow(2,d,q)==1 and all(pow(2,d//p,q)!=1 for p in factors(d))
    assert len(pool)==86 and len(data['free_budget_nine_primes'])==59
    results=[]
    for row in data['roots']:
        a=int(row['root']);active_phases={}
        assert a*a-1>max(pool)
        for q in pool:
            x=a*a%q
            for n in range(orders[q]):
                if x==1:active_phases[q]=n;break
                x=x*2%q
        active=tuple(active_phases)
        period=lcm(*(orders[q] for q in active));full=(1<<period)-1
        masks={q:sum(1<<n for n in range(active_phases[q],period,orders[q])) for q in active}
        original=tuple(sorted(set(P)|{5,13}|set(map(int,row['tail_v_phases']))))
        assert len(original)==29
        assert reduce(int.__or__,(masks[q] for q in original),0)==full
        original_private={q:masks[q]&~reduce(int.__or__,(masks[p] for p in original if p!=q),0) for q in original}
        assert all(original_private.values())
        old_private={q:masks[q]&~reduce(int.__or__,(masks[p] for p in active if p!=q),0) for q in P}
        assert all(old_private.values())
        clauses=[0]*period
        for i,q in enumerate(active):
            for n in range(active_phases[q],period,orders[q]):clauses[n]|=1<<i
        assert all(clauses)
        reduced=minimal_clauses(clauses)
        @lru_cache(None)
        def solve(cs):
            if not cs:return ()
            first=cs[0];bits=[]
            while first:
                b=first&-first;first-=b;bits.append(b)
            bits.sort(key=lambda b:-sum(bool(c&b) for c in cs))
            alternatives=[(b.bit_length()-1,)+solve(minimal_clauses(c for c in cs if not c&b)) for b in bits]
            return min(alternatives,key=lambda x:(len(x),x))
        selected=tuple(sorted(active[i] for i in solve(reduced)))
        assert len(selected)==29
        assert reduce(int.__or__,(masks[q] for q in selected),0)==full
        def witness(bits):
            n=(bits&-bits).bit_length()-1
            return period if n==0 else n
        results.append({'type':row['type'],'root':row['root'],'inherited_supplementary_minimum':9,
                        'active_prime_count':len(active),'active_phases':active_phases,
                        'complete_period':period,'original_dictionary':original,
                        'original_29_private_indices':{str(q):witness(b) for q,b in original_private.items()},
                        'old_P_private_indices_in_expanded_pool':{str(q):witness(b) for q,b in old_private.items()},
                        'minimal_hitting_clauses':list(reduced),'minimum_cover_in_specified_pool':len(selected),
                        'a_selected_minimum_pool_dictionary':selected,'DP_states':solve.cache_info().currsize,
                        'unrestricted_total_upper_bound':29,'unrestricted_total_lower_bound_claimed':False})
    result={'schema':'RIESEL_V15_FINITE_POOL_TOTAL_OBSERVATION','status':'PASS',
            'pool_primes':pool,'pool_size':len(pool),'verified_prime_nodes':len(verified),
            'pool_definition':'P20, the seven fixed active R3 supplements, and all 59 free budget-nine observer primes',
            'cases':results,'all_eight_specified_pool_minima':29,
            'no_unrestricted_tau_lower_bound_from_finite_pool':True,
            'native_BRC_execution':False,'independent_project_review':False}
    target=HERE/'selected_pool_certificate.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','pool_size':len(pool),'prime_nodes':len(verified),
                      'cases':[(r['type'],r['active_prime_count'],r['minimum_cover_in_specified_pool']) for r in results],
                      'output':str(target)},indent=2))


if __name__=='__main__':main()
