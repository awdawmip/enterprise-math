#!/usr/bin/env python3
"""Local signed prime-power tent oracle for actual matched-road moments.

All numerical endpoints use outward integer intervals through the pinned
logarithm evaluator. Historical actual-road intervals are consumed only after
the local reference moments and matching radii have been generated.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial, isqrt, prod
from bisect import bisect_left, bisect_right
import argparse
import importlib.util
import json


def module_at(path):
    spec = importlib.util.spec_from_file_location('harmonic_interval', path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def primes_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p::p] = b'\x00' * ((n-p*p)//p + 1)
    return [p for p in range(2,n+1) if sieve[p]]


def phi(n, l, x, r):
    if l < n <= x:
        return F(n-l,x-l)
    if x < n < r:
        return F(r-n,r-x)
    return F(0)


def ipow(m, x, k):
    out = m.ONE
    while k:
        if k & 1:
            out = m.mul(out,x)
        x = m.mul(x,x)
        k //= 2
    return out


def exact_checks():
    """Exhaustive finite impulse check, including L=1 and unbalanced tents."""
    count = impulses = 0
    harmonics=[F(0)]
    for n in range(1,18):
        harmonics.append(harmonics[-1]+F(1,n))
    for l in range(1,16):
        for x in range(l+1,17):
            for r in range(x+1,18):
                a,b,h=x-l,r-x,r-l
                assert sum((phi(n,l,x,r) for n in range(l+1,r)),F(0)) == F(h,2)
                assert sum((phi(n,l,x,r)**2 for n in range(l+1,r)),F(0)) == F(h,3)+F(1,6*a)+F(1,6*b)
                unit=sum((phi(n,l,x,r)/n for n in range(l+1,r)),F(0))
                assert unit==F(r,b)*(harmonics[r]-harmonics[x])-F(l,a)*(harmonics[x]-harmonics[l])
                for n in range(1,r+1):
                    q=lambda y: max(F(y,n)-1,F(0))
                    tp=(q(x)-q(l))/a-(q(r)-q(x))/b
                    assert tp == -phi(n,l,x,r)/n
                    impulses += 1
                count += 1
    return {'all_triples':'1 <= L < x < R <= 17',
            'triples':count,'source_impulses':impulses,
            'kernel_identity':True,'hat_mass':True,'hat_square_mass':True,
            'unit_background_harmonic_identity':True,
            'prehistory_and_endpoint_impulses_annihilated':True}


def compute(m, geometry, family):
    B=max(b['Y'] for b in geometry['blocks'])
    nodes=list(map(F,family['nodes']))
    weights=list(map(F,family['weights']))
    assert len(nodes)==len(weights)>0
    assert len(set(nodes))==len(nodes) and all(a>0 for a in nodes)
    assert sum(weights)==1
    assert all(sum(w*a**j for a,w in zip(nodes,weights))==0 for j in range(1,len(nodes)))
    k=len(nodes)+1
    coef=prod(nodes)/factorial(k)
    assert m.log_int(B)[1] <= k*m.S
    primes=primes_to(B)
    events=[]
    for p in primes:
        n=p
        while n<=B:
            events.append((n,p))
            n*=p
    events.sort()
    event_positions=[n for n,p in events]
    # Values below the first left endpoint never enter a local moment.
    eta={}
    point_radius={}
    for b in geometry['blocks']:
        for level in b['levels']:
            for p in level['packets']:
                for y in (p['L'],p['x'],p['R']):
                    if y not in eta:
                        eta[y]=m.qmul(ipow(m,m.log_int(y),k),coef)
                        point_radius[y]=m.qmul(eta[y],F((y-1)*(y-2),2*y))[1]
    blocks=[]
    visits=0
    for block in geometry['blocks']:
        X=block['X']
        levels=[]
        for level in block['levels']:
            rows=[]
            energy=m.ZERO
            actual_energy=m.ZERO
            match_square=m.ZERO
            point_match_square=m.ZERO
            active_diagonal=m.ZERO
            active_offdiagonal=m.ZERO
            active_background=m.ZERO
            active_cross=m.ZERO
            prime_only_energy=m.ZERO
            pp_payment=m.ZERO
            kappa_payment=m.ZERO
            prime_only_background=m.ZERO
            prime_only_cross=m.ZERO
            prime_only_diagonal=m.ZERO
            prime_only_offdiagonal=m.ZERO
            max_h=0
            for p in level['packets']:
                l,x,r=p['L'],p['x'],p['R']
                a,b,h=x-l,r-x,r-l
                g=lambda y:m.qmul(m.log_int(y),y)
                background=m.sub(m.qmul(m.sub(g(r),g(x)),1,b),m.qmul(m.sub(g(x),g(l)),1,a))
                prime_sum=m.ZERO
                prime_mass=m.ZERO
                power_mass=m.ZERO
                diag=m.ZERO
                prime_diag=m.ZERO
                event_count=0
                for n,base in events[bisect_right(event_positions,l):bisect_left(event_positions,r)]:
                    term=m.qmul(m.log_int(base),phi(n,l,x,r)/n)
                    prime_sum=m.add(prime_sum,term)
                    diag=m.add(diag,m.square(term))
                    if n==base:
                        prime_mass=m.add(prime_mass,term)
                        prime_diag=m.add(prime_diag,m.square(term))
                    else:
                        power_mass=m.add(power_mass,term)
                    event_count+=1
                visits+=event_count
                t=m.sub(background,prime_sum)
                radius=m.qmul(eta[r],F(h,2*r))[1]
                truth=(t[0]-radius,t[1]+radius)
                ep_radius=(m.qmul((point_radius[l],point_radius[l]),1,a)[1]
                           +m.qmul((point_radius[x],point_radius[x]),F(1,a)+F(1,b))[1]
                           +m.qmul((point_radius[r],point_radius[r]),1,b)[1])
                factor=F(h**3,X**2)
                max_h=max(max_h,h)
                unit_background=m.sub(m.qmul(m.sub(m.harmonics(r)[0],m.harmonics(x)[0]),r,b),
                                      m.qmul(m.sub(m.harmonics(x)[0],m.harmonics(l)[0]),l,a))
                kappa_correction=m.sub(background,unit_background)
                prime_only=m.sub(unit_background,prime_mass)
                assert m.overlap(t,m.sub(m.add(prime_only,kappa_correction),power_mass))
                assert kappa_correction[0]>=0
                prime_only_energy=m.add(prime_only_energy,m.qmul(m.square(m.positive(prime_only)),factor))
                pp_payment=m.add(pp_payment,m.qmul(m.square(power_mass),factor))
                kappa_payment=m.add(kappa_payment,m.qmul(m.square(kappa_correction),factor))
                prime_sign=1 if prime_only[0]>0 else -1 if prime_only[1]<0 else 0
                assert prime_sign!=0
                if prime_sign>0:
                    prime_only_background=m.add(prime_only_background,m.qmul(m.square(unit_background),factor))
                    prime_only_cross=m.add(prime_only_cross,m.qmul(m.mul(unit_background,prime_mass),-2*factor))
                    prime_only_diagonal=m.add(prime_only_diagonal,m.qmul(prime_diag,factor))
                    prime_only_offdiagonal=m.add(prime_only_offdiagonal,m.qmul(m.sub(m.square(prime_mass),prime_diag),factor))
                energy=m.add(energy,m.qmul(m.square(m.positive(t)),factor))
                actual_energy=m.add(actual_energy,m.qmul(m.square(m.positive(truth)),factor))
                match_square=m.add(match_square,m.qmul(m.square((radius,radius)),factor))
                point_match_square=m.add(point_match_square,m.qmul(m.square((ep_radius,ep_radius)),factor))
                sign=1 if t[0]>0 else -1 if t[1]<0 else 0
                assert sign != 0
                assert truth[0]>0 if sign>0 else truth[1]<0
                if sign>0:
                    active_diagonal=m.add(active_diagonal,m.qmul(diag,factor))
                    active_offdiagonal=m.add(active_offdiagonal,m.qmul(m.sub(m.square(prime_sum),diag),factor))
                    active_background=m.add(active_background,m.qmul(m.square(background),factor))
                    active_cross=m.add(active_cross,m.qmul(m.mul(background,prime_sum),-2*factor))
                rows.append({**p,'reference':m.record(t),'actual_enclosure':m.record(truth),
                             'background':m.record(background),'prime_power_tent_mass':m.record(prime_sum),
                             'prime_only_tent_deficit':m.record(prime_only),
                             'unit_background_tent_mass':m.record(unit_background),
                             'ordinary_prime_tent_mass':m.record(prime_mass),
                             'higher_prime_power_tent_mass':m.record(power_mass),
                             'kappa_minus_one_tent_mass':m.record(kappa_correction),
                             'prime_only_deficit_sign':prime_sign,
                             'local_matching_radius':m.record((radius,radius)),
                             'three_point_matching_radius':m.record((ep_radius,ep_radius)),
                             'radius_ratio_exact':str(F(ep_radius,radius)),
                             'certified_reference_and_actual_sign':sign,
                             'local_prime_power_events':event_count})
            expanded=m.add(m.add(active_background,active_cross),m.add(active_diagonal,active_offdiagonal))
            assert m.overlap(expanded,energy)
            prime_expanded=m.add(m.add(prime_only_background,prime_only_cross),
                                 m.add(prime_only_diagonal,prime_only_offdiagonal))
            assert m.overlap(prime_expanded,prime_only_energy)
            pp_universal=F(288*max_h**3,X**3)
            kappa_universal=F(max_h**4,16*X**7)
            assert pp_payment[1]<=m.rat(pp_universal)[0]
            assert kappa_payment[1]<=m.rat(kappa_universal)[0]
            # Adjacent packets may share endpoints, where their hats vanish.
            supports=sorted((p['L'],p['R']) for p in level['packets'])
            assert all(r<=ll for (l,r),(ll,rr) in zip(supports,supports[1:]))
            levels.append({'level':level['level'],'packets':rows,
                           'normalized_reference_positive_budget':m.record(energy),
                           'normalized_actual_positive_budget_enclosure':m.record(actual_energy),
                           'normalized_local_matching_square_payment':m.record(match_square),
                           'normalized_three_point_matching_square_payment':m.record(point_match_square),
                           'normalized_prime_only_positive_budget':m.record(prime_only_energy),
                           'normalized_higher_prime_power_square_payment':m.record(pp_payment),
                           'normalized_kappa_minus_one_square_payment':m.record(kappa_payment),
                           'universal_higher_power_square_payment_exact':str(pp_universal),
                           'universal_kappa_minus_one_square_payment_exact':str(kappa_universal),
                           'prime_only_gated_correlation':{
                              'background_square':m.record(prime_only_background),
                              'background_prime_cross':m.record(prime_only_cross),
                              'prime_diagonal':m.record(prime_only_diagonal),
                              'prime_offdiagonal':m.record(prime_only_offdiagonal),
                              'sum':m.record(prime_expanded)},
                           'gated_correlation':{'background_square':m.record(active_background),
                              'background_prime_cross':m.record(active_cross),
                              'prime_diagonal':m.record(active_diagonal),
                              'prime_offdiagonal':m.record(active_offdiagonal),
                              'sum':m.record(expanded)},
                           'correlation_expansion_matches_direct_square':True})
        blocks.append({'X':X,'Y':block['Y'],'levels':levels})
    return blocks,{'sieve_limit':B,'prime_count':len(primes),'prime_power_events':len(events),
                  'local_event_visits':visits,'thickness_count':len(nodes),'matching_exponent':k,
                  'matching_coefficient_exact':str(coef),'thickness_exponential_calls':0,
                  'D_c_E_q_full_arrays_generated':False,'complete_prefix_generated':False,
                  'uniform_eta_B':m.record(eta[B])}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--harmonic-module',type=Path,required=True)
    ap.add_argument('--family',type=Path,required=True)
    ap.add_argument('--geometry',type=Path,required=True)
    ap.add_argument('--comparison',type=Path)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('local_arithmetic_certificate.json'))
    args=ap.parse_args()
    m=module_at(args.harmonic_module)
    geometry=json.loads(args.geometry.read_text())
    family=json.loads(args.family.read_text())
    checks=exact_checks()
    blocks,cost=compute(m,geometry,family)
    compared=0
    old_budget=[]
    if args.comparison:
        old=json.loads(args.comparison.read_text())
        for block,ob in zip(blocks,old['roads']['q']['dyadic_blocks']):
            assert (block['X'],block['Y'])==(ob['X'],ob['Y'])
            for level,ol in zip(block['levels'],ob['levels']):
                total=m.ZERO
                for p,op in zip(level['packets'],ol['packets']):
                    assert (p['L'],p['x'],p['R'])==(op['L'],op['x'],op['R'])
                    cert=m.decode(p['actual_enclosure'])
                    truth=m.decode(op['signed_charge'])
                    assert cert[0]<=truth[0]<=truth[1]<=cert[1]
                    total=m.add(total,m.qmul(m.square(m.positive(truth)),F((p['R']-p['L'])**3,block['X']**2)))
                    compared+=1
                level['historical_actual_normalized_budget']=m.record(total)
                old_budget.append((block['X'],level['level'],total))
    ratios=[F(p['radius_ratio_exact']) for b in blocks for l in b['levels'] for p in l['packets']]
    rec={'status':'PASS','schema':'RH_LOCAL_ARITHMETIC_TENT_V1',
         'scope':'Exact local kernel and error transfer; finite original 38 packets, no unbounded arithmetic estimate',
         'arithmetic':{'denominator_power_of_10':m.DIGITS,'method':'outward integer intervals; rational error radii'},
         'exact_checks':checks,'cost':cost,'historical_actual_packets_contained':compared,
         'comparison_consumed_only_after_new_oracle_completed':True,
         'minimum_radius_improvement_exact':str(min(ratios)),
         'maximum_radius_improvement_exact':str(max(ratios)),
         'blocks':blocks}
    args.output.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':rec['status'],'exact_checks':checks,'cost':cost,
          'historical_actual_packets_contained':compared,
          'radius_improvement_min':float(min(ratios)),'radius_improvement_max':float(max(ratios)),
          'budgets':[{'X':b['X'],'level':l['level'],'reference':l['normalized_reference_positive_budget']['upper'],
                     'actual_upper':l['normalized_actual_positive_budget_enclosure']['upper'],
                     'local_payment':l['normalized_local_matching_square_payment']['upper'],
                     'point_payment':l['normalized_three_point_matching_square_payment']['upper']} for b in blocks for l in b['levels']]},ensure_ascii=False))


if __name__=='__main__':
    main()
