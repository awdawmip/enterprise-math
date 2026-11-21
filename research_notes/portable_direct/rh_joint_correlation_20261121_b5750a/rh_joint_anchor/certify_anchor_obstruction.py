#!/usr/bin/env python3
"""Directed finite checks for the anchored coefficient-envelope obstruction.

Universal claims are proved in ANCHORED_ENVELOPE_OBSTRUCTION.md. The examples
are arbitrary auxiliary coefficients, not coefficients of the actual roads.
Only exact integers and Fraction are used for certified values.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'rh_correlation_rational'))
from certify_matched_nodes import (  # noqa: E402
    Elementary, SCALE, DIGITS, ZERO, rat, add, sub, scale, ceildiv, render,
)


def record(x):
    return {**render(x, 30), 'integer_bounds': list(map(str, x)),
            'denominator_power_of_10': DIGITS}


def square(x):
    lo = 0 if x[0] <= 0 <= x[1] else min(x[0] ** 2, x[1] ** 2)
    return lo // SCALE, ceildiv(max(x[0] ** 2, x[1] ** 2), SCALE)


def b(d, n):
    r = n % d
    return F(d*d-1, 12*d) - F(r*(d-r), 2*d)


def construction(A, H, evaluate=False):
    assert H*16 <= A and H*H >= 40*A
    kmin, kmax = ceildiv(A, H), 3*A//(2*H)
    ds, ranges = [], []
    for k in range(kmin, kmax+1):
        lo, hi = ceildiv(8*A, 8*k+1), A//k
        length = F(A, k) - F(8*A, 8*k+1)
        assert length >= F(H*H, 20*A) >= 2
        assert hi-lo+1 >= length/2
        ranges.append({'k': k, 'first_d': lo, 'last_d': hi})
        ds.extend(range(lo, hi+1))
    assert len(ds) == len(set(ds))
    assert len(ds) >= F(H, 160)
    radius = H//192
    # First differences bound every intermediate point. Exact endpoint checks
    # also catch the residue and interval rounding conventions.
    for d in ds:
        assert H < 2*d <= 2*H
        assert 8*(A % d) <= d
        assert b(d, A) >= F(d, 48)
        assert b(d, A+radius) >= F(d, 64)
        assert F(d, 64*(A+radius)) - F(d*d, 8*A*A) > 0
    theorem_lower = F(H**5, 192*40960**2) / (F(A)+F(H,192))**4
    result = {
        'A': A, 'H': H, 'theta': '1/2',
        'coefficient_class': 'arbitrary auxiliary c_d in {0,1}; not actual road coefficients',
        'selected_divisor_count': len(ds),
        'guaranteed_count_lower': str(F(H,160)),
        'selected_ranges': ranges,
        'coherent_window': [A, A+radius],
        'coherent_window_integer_count': radius+1,
        'universal_energy_lower_exact': str(theorem_lower),
        'universal_energy_lower': record(rat(theorem_lower)),
        'power_factor_H5_over_A4': str(F(H**5,A**4)),
        'all_selected_endpoint_and_phase_checks_passed': True,
    }
    if evaluate:
        elementary = Elementary()
        harmonic = [ZERO]
        for n in range(1, A+radius+1):
            harmonic.append(add(harmonic[-1], rat(F(1,n))))
        energy = ZERO
        values = []
        for n in range(A, A+radius+1):
            total = ZERO
            for d in ds:
                value = add(scale(sub(sub(harmonic[n], harmonic[n//d]),
                                      elementary.log_integer(d)), F(n,d)),
                            rat(F(d-1-2*(n%d),2*d)))
                total = add(total, value)
                assert value[0] >= rat(F(d,128*n))[1]
            assert total[0] >= rat(F(H*H,40960*n))[1]
            values.append({'n':n, 'P_H':record(total)})
            energy = add(energy, scale(square(total), F(1,n*n)))
        assert energy[0] >= rat(theorem_lower)[1]
        result['direct_coherent_energy'] = record(energy)
        result['all_coherent_values'] = values
        result['elementary_counts'] = {
            'harmonic_terms': A+radius,
            'direct_phase_terms': len(ds)*(radius+1),
        }
    return result


def approximation_checks():
    # Include n<d, n near d, exact period jumps, and d small relative to n.
    ns = [2,3,4,5,16,17,31,32,127,128,1024,1025,16384,16389]
    ds = [2,3,4,5,7,16,31,64,127,128,256,1024,2048]
    harmonic, elementary = [ZERO], Elementary()
    for n in range(1,max(ns)+1):
        harmonic.append(add(harmonic[-1],rat(F(1,n))))
    worst, worst_case = F(0), None
    for n in ns:
        for d in ds:
            p = add(scale(sub(sub(harmonic[n],harmonic[n//d]),
                              elementary.log_integer(d)),F(n,d)),
                    rat(F(d-1-2*(n%d),2*d)))
            error = sub(p,rat(b(d,n)/n))
            upper_abs = max(abs(error[0]),abs(error[1]))
            bound = F(d*d,8*n*n)
            assert F(upper_abs,SCALE) <= bound
            ratio = F(upper_abs,SCALE)/bound
            if ratio > worst:
                worst,worst_case = ratio, {'n':n,'d':d}
    return {'checked_pairs':len(ns)*len(ds),
            'n_values':ns,'d_values':ds,
            'maximum_certified_error_over_bound':record(rat(worst)),
            'maximum_case':worst_case,
            'arithmetic':'directed integer intervals at 60 decimal places; no tolerance'}


def main():
    start = time.perf_counter()
    source = ROOT/'rh_correlation_rational/certify_matched_nodes.py'
    data = {
        'status':'finite checks supporting the accompanying proved auxiliary theorem',
        'input_oracle_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'uniform_approximation':approximation_checks(),
        'small_direct_energy':construction(16384,1024,True),
        'explicit_five_sixths_family_t1':construction(2**24,2**20,False),
        'elapsed_seconds_diagnostic_only':time.perf_counter()-start,
    }
    output = Path(__file__).with_name('anchor_obstruction_certificate.json')
    output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'output':str(output),
                      'checks':data['uniform_approximation']['checked_pairs'],
                      'small_energy':data['small_direct_energy']['direct_coherent_energy'],
                      'large_selected_count':data['explicit_five_sixths_family_t1']['selected_divisor_count'],
                      'seconds':data['elapsed_seconds_diagnostic_only']},ensure_ascii=False))


if __name__ == '__main__':
    main()
