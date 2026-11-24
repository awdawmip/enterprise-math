#!/usr/bin/env python3
"""Certify all (9n,12n,16n) local moments from Lambda and paid matching error.

Two shared prime-power prefixes generate every new interval. Historical true
q samples are opened only after generation, and used only for postchecking
complete triples. No complete D, c, E, or q array is read or generated.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial, isqrt, prod
import argparse
import hashlib
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True


def load_module(path):
    spec = importlib.util.spec_from_file_location('geometric_harmonic_interval', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def primes_to(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start::p] = b'\x00' * ((limit - start) // p + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def ipow(m, value, k):
    result = m.ONE
    while k:
        if k & 1:
            result = m.mul(result, value)
        value = m.mul(value, value)
        k //= 2
    return result


def sign(interval):
    return 'positive' if interval[0] > 0 else 'negative' if interval[1] < 0 else 'unresolved'


def bound_record(m, interval):
    # One global fixed denominator; omit repeated width strings from 1,935 rows.
    return {'integer_bounds': list(map(str, interval)),
            'lower': m.decimal(interval[0]),
            'upper': m.decimal(interval[1], up=True)}


def signature_runs(rows):
    out = []
    for row in rows:
        if out and row['actual_sign'] == out[-1]['sign'] and row['n'] == out[-1]['last_n'] + 1:
            out[-1]['last_n'] = row['n']
        else:
            out.append({'first_n': row['n'], 'last_n': row['n'], 'sign': row['actual_sign']})
    return out


def compute(m, geometry, family):
    n_min, n_max = geometry['n_min'], geometry['n_max']
    assert geometry['endpoint_multipliers'] == [9, 12, 16]
    assert n_max - n_min + 1 == geometry['expected_packet_count']
    assert geometry['observation_window'][0] <= 9*n_min
    assert 16*n_max <= geometry['observation_window'][1]
    thickness = list(map(F, family['nodes']))
    weights = list(map(F, family['weights']))
    assert len(thickness) == len(weights) == geometry['matching_thickness_count'] == 11
    assert len(set(thickness)) == len(thickness) and all(a > 0 for a in thickness)
    assert sum(weights) == 1
    assert all(sum(w*a**j for w,a in zip(weights,thickness)) == 0 for j in range(1,len(thickness)))
    k = len(thickness) + 1
    assert k == geometry['matching_exponent'] == 12
    coefficient = prod(thickness) / factorial(k)
    limit = 16*n_max
    assert m.log_int(limit)[1] <= k*m.S

    # Exact symbolic identity: 4 log(16n)+3 log(9n)-7 log(12n)
    # has log(n) coefficient zero, log(2) coefficient two, log(3) coefficient -1.
    exponents = {'n': 4+3-7, '2': 4*4-7*2, '3': 3*2-7}
    assert exponents == {'n':0, '2':2, '3':-1}
    beta = m.log_unit(4,3)
    expanded = m.sub(m.add(m.qmul(m.log_int(16),4),m.qmul(m.log_int(9),3)),m.qmul(m.log_int(12),7))
    assert m.overlap(beta,expanded)

    queries = sorted({c*n for n in range(n_min,n_max+1) for c in (9,12,16)})
    origin = queries[0]
    primes = primes_to(limit)
    events = []
    for p in primes:
        power = p
        while power <= limit:
            if power > origin:
                events.append((power,p))
            power *= p
    events.sort()
    prefix_a, prefix_b = {}, {}
    acc_a = acc_b = m.ZERO
    event_index = 0
    for y in queries:
        while event_index < len(events) and events[event_index][0] <= y:
            power, prime = events[event_index]
            logp = m.log_int(prime)
            acc_a = m.add(acc_a,logp)
            acc_b = m.add(acc_b,m.qmul(logp,1,power))
            event_index += 1
        prefix_a[y], prefix_b[y] = acc_a, acc_b
    assert event_index == len(events)

    rows, raw = [], {}
    counts = {'reference':{'positive':0,'negative':0,'unresolved':0},
              'actual':{'positive':0,'negative':0,'unresolved':0}}
    for n in range(n_min,n_max+1):
        l,x,r = 9*n,12*n,16*n
        a,b,h = 3*n,4*n,7*n
        left = m.qmul(m.sub(m.sub(prefix_a[x],prefix_a[l]),
                               m.qmul(m.sub(prefix_b[x],prefix_b[l]),l)),1,a)
        right = m.qmul(m.sub(m.qmul(m.sub(prefix_b[r],prefix_b[x]),r),
                                m.sub(prefix_a[r],prefix_a[x])),1,b)
        mass = m.add(left,right)
        reference = m.sub(beta,mass)
        eta = m.qmul(ipow(m,m.log_int(r),k),coefficient)
        radius = m.qmul(eta,7,32)[1]
        actual = reference[0]-radius,reference[1]+radius
        factor = F(343*n,81)
        assert factor == F(h**3,l*l)
        budget = m.qmul(m.square(m.positive(actual)),factor)
        reference_budget = m.qmul(m.square(m.positive(reference)),factor)
        counts['reference'][sign(reference)] += 1
        counts['actual'][sign(actual)] += 1
        raw[n] = {'reference':reference,'actual':actual,'budget':budget,
                  'radius':radius,'mass':mass}
        rows.append({'n':n,'L':l,'x':x,'R':r,
                     'reference_t':bound_record(m,reference),
                     'matching_radius_upper_integer':str(radius),
                     'actual_t':bound_record(m,actual),
                     'actual_sign':sign(actual),
                     'normalized_single_packet_budget':bound_record(m,budget),
                     'reference_budget':bound_record(m,reference_budget)})

    max_n = max(raw,key=lambda n:raw[n]['budget'][1])
    second_upper = max(v['budget'][1] for n,v in raw.items() if n != max_n)
    unique_maximum = raw[max_n]['budget'][0] > second_upper
    maximum_interval = (max(v['budget'][0] for v in raw.values()),
                        max(v['budget'][1] for v in raw.values()))
    assert maximum_interval[1] < m.rat(F(361,40000))[0]
    # Focused independent accumulation of the selected extremal and boundary hats.
    spotchecks = []
    for n in sorted({n_min,max_n,n_max}):
        l,x,r = 9*n,12*n,16*n
        direct = m.ZERO
        for power,prime in events:
            if l < power < r:
                phi = F(power-l,3*n) if power <= x else F(r-power,4*n)
                direct = m.add(direct,m.qmul(m.log_int(prime),phi/power))
        assert m.overlap(direct,raw[n]['mass'])
        background = m.sub(m.add(m.qmul(m.log_int(r),4),m.qmul(m.log_int(l),3)),m.qmul(m.log_int(x),7))
        assert m.overlap(background,beta)
        spotchecks.append(n)
    cost = {'sieve_limit':limit,'ordinary_primes_in_sieve':len(primes),
            'prime_power_events_accumulated_once':len(events),
            'shared_weighted_prefixes':2,'prefix_queries':len(queries),
            'prefix_origin_excluded':origin,'thickness_count':len(thickness),
            'matching_exponent':k,'matching_coefficient':str(coefficient),
            'thickness_exponential_calls':0,
            'complete_D_c_E_q_arrays_read_or_generated':False,
            'gamma_used':False,'unit_and_pre_origin_annihilation':'exact local tent identity',
            'focused_direct_hat_checks_n':spotchecks}
    summary = {'counts':counts,'maximizing_n':max_n,
               'maximum_is_strictly_separated':unique_maximum,
               'simple_strict_uniform_budget_upper':'361/40000',
               'simple_strict_uniform_root_budget_upper':'19/200',
               'maximum_normalized_single_packet_budget':m.record(maximum_interval),
               'largest_other_packet_upper':m.record((second_upper,second_upper)),
               'maximum_matching_radius':m.record((max(v['radius'] for v in raw.values()),)*2),
               'minimum_signed_t_lower':m.record((min(v['actual'][0] for v in raw.values()),)*2),
               'maximum_signed_t_upper':m.record((max(v['actual'][1] for v in raw.values()),)*2),
               'sign_runs':signature_runs(rows)}
    return rows,raw,beta,cost,summary


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--prior',type=Path,required=True)
    ap.add_argument('--geometry',type=Path,default=Path(__file__).with_name('fixed_geometry.json'))
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('geometric_tent_certificate.json'))
    ap.add_argument('--skip-postcheck',action='store_true')
    args = ap.parse_args()
    harmonic = args.prior / 'dependencies/certify_fast_harmonic_energy.py'
    family_path = args.prior / 'prefix_compute/fixed_matched_family.json'
    m = load_module(harmonic)
    geometry = json.loads(args.geometry.read_text())
    family = json.loads(family_path.read_text())
    started = time.perf_counter()
    rows,raw,beta,cost,summary = compute(m,geometry,family)
    generation_seconds = time.perf_counter()-started
    generated_complete = len(rows) == geometry['expected_packet_count']
    assert generated_complete
    postcheck = {'performed':False}
    if not args.skip_postcheck:
        # This is deliberately the first read of historical actual sample bytes.
        old_path = args.prior / 'inputs/rh_partial_frontier_20261122/sparse_sample_observations.json'
        old_bytes = old_path.read_bytes()
        old = json.loads(old_bytes)
        samples = {row['n']:m.decode(row['value']) for row in old['samples']}
        queries = {c*n for n in raw for c in (9,12,16)}
        complete, partial = [], []
        for n in raw:
            l,x,r = 9*n,12*n,16*n
            available = sum(y in samples for y in (l,x,r))
            if available == 3:
                actual_old = m.sub(m.qmul(m.sub(samples[x],samples[l]),1,3*n),
                                   m.qmul(m.sub(samples[r],samples[x]),1,4*n))
                new = raw[n]['actual']
                assert new[0] <= actual_old[0] <= actual_old[1] <= new[1]
                complete.append({'n':n,'historical_t':bound_record(m,actual_old),
                                 'contained':True})
            elif available:
                partial.append({'n':n,'available_points':available})
        postcheck = {'performed':True,'read_after_all_new_intervals_generated':True,
                     'historical_sample_count':len(samples),
                     'distinct_generated_query_nodes_in_historical_samples':len(queries & samples.keys()),
                     'complete_triples_checked':len(complete),
                     'partial_triples_not_compared':len(partial),
                     'complete_triples':complete,'partial_triples':partial,
                     'historical_source_sha256':hashlib.sha256(old_bytes).hexdigest()}
    result = {'schema':'RH_FIXED_GEOMETRIC_LOCAL_TENT_CERTIFICATE_V1',
              'status':'PASS_AUTHOR_CERTIFICATE',
              'scope':'1935 overlapping individual packet observations; no disjoint-layer sum asserted',
              'input_geometry':geometry,
              'decimal_denominator_power_of_10':m.DIGITS,
              'background_exact':'log(4/3)','background_interval':m.record(beta),
              'matching_radius_formula':'(7/32) * a_m * log(16n)^12',
              'normalized_budget_formula':'(343*n/81) * (t_D)_+^2',
              'generation_seconds':generation_seconds,'cost':cost,
              'summary':summary,'postcheck':postcheck,'packets':rows,
              'inputs':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
                        for p in [harmonic,family_path,args.geometry]]}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'packet_count':len(rows),
                      'background':m.record(beta),'summary':{k:v for k,v in summary.items() if k!='sign_runs'},
                      'postcheck':{k:v for k,v in postcheck.items() if k not in ['complete_triples','partial_triples']},
                      'cost':cost,'generation_seconds':generation_seconds},indent=2))


if __name__ == '__main__':
    main()
