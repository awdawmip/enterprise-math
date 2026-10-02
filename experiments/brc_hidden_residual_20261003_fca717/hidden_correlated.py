#!/usr/bin/env python3
"""Exact hidden residual statistics, keeping native X6 and the Markov sign.

Only the new hidden observations are studied. Prior source functions and its
immutable numeric output are reused without rewriting prior experiments.
H=P5 X is a fractional component readout, never a new native Cell address.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, EffectHistogram, eye, ma, mm, sm, point_moment
from enterprise_math.brc_weighted import cwm_edge

OLD_DIR = ROOT/'experiments/brc_x6_replay_20261002_fca717'
OLD_SCRIPT = OLD_DIR/'correlated_replay.py'
OLD_RESULTS = OLD_DIR/'correlated_results.json'
old = {'__file__': str(OLD_SCRIPT), '__name__': 'prior_correlated_reference'}
exec(compile(OLD_SCRIPT.read_text(), str(OLD_SCRIPT), 'exec'), old)
D, HORIZON, ENUM_END = 6, 128, 4
RHOS = old['RHOS']
ZERO = (0,)*D
P5 = tuple(tuple(F(i == j)-F(1, D) for j in range(D)) for i in range(D))
A, B, T3 = F(5, 6), F(5, 36), F(5, 9)
SAMPLES = {1, 2, 3, 4, 8, 16, 32, 64, 128}
OBSERVABLES = ('mass', 's', 's2', 'q', 'q2', 'a3', 'sa3', 'q3')


def trace(m):
    return sum((m[i][i] for i in range(len(m))), F())


def readout(x):
    s = sum(x)
    h6 = tuple(D*v-s for v in x)
    q = F(sum(v*v for v in h6), D*D)
    a3 = F(sum(v**3 for v in h6), D**3)
    return dict(mass=F(1), s=F(s), s2=F(s*s), q=q, q2=q*q,
                a3=a3, sa3=s*a3, q3=q**3)


def closed_step(states, probabilities):
    result = {}
    for e in (-1, 1):
        v = {name: sum((probabilities[source, e]*states[source][name]
                       for source in (-1, 1)), F()) for name in OBSERVABLES}
        result[e] = dict(
            mass=v['mass'], s=v['s']+e*v['mass'],
            s2=v['s2']+2*e*v['s']+v['mass'],
            q=v['q']+A*v['mass'],
            q2=v['q2']+F(7, 3)*v['q']+A*A*v['mass'],
            a3=v['a3']+e*T3*v['mass'],
            sa3=v['sa3']+e*v['a3']+e*T3*v['s']+T3*v['mass'],
            q3=v['q3']+F(9, 2)*v['q2']+F(15, 4)*v['q']
               +A**3*v['mass']+F(4*e, 3)*v['a3'])
    return result


def independent_axis_words():
    """No CWM or recursive propagation: enumerate axis words for fixed signs."""
    cache = {}
    checks = dict(fixed_sign_words=0, explicit_axis_words=0)
    examples = []
    for n in range(1, ENUM_END+1):
        cache[n] = {}
        for signs in product((-1, 1), repeat=n):
            endpoints = Counter()
            for axes in product(range(D), repeat=n):
                x = [0]*D
                for e, axis in zip(signs, axes):
                    x[axis] += e
                endpoints[tuple(x)] += 1
                checks['explicit_axis_words'] += 1
            direct = {name: F() for name in OBSERVABLES}
            zero = F()
            for x, count in endpoints.items():
                value, probability = readout(x), F(count, D**n)
                for name in OBSERVABLES:
                    direct[name] += probability*value[name]
                if value['q'] == 0:
                    zero += probability
            s = sum(signs)
            assert direct['q'] == A*n
            assert direct['q2'] == F(35*n*n-10*n, 36)
            assert direct['a3'] == T3*s
            assert direct['sa3'] == T3*s*s
            assert direct['q3'] == F(5, 216)*(63*n**3-54*n*n+16*s*s)
            cache[n][signs] = endpoints
            checks['fixed_sign_words'] += 1
            if signs in ((1, 1), (1, -1)):
                examples.append(dict(signs=signs, scalar_sum=s, observations=direct,
                                     hidden_zero_probability=zero))
    return cache, checks, examples


def independent_markov_law(n, rho, word_cache):
    # Integrating epsilon_0 gives P(epsilon_1=+/-1)=1/2. Enumerated sign words
    # here therefore have one fewer hidden label than the old CWM initialization.
    law = {}
    for signs, endpoints in word_cache[n].items():
        probability = F(1, 2)
        for a, b in zip(signs, signs[1:]):
            probability *= (1+rho*a*b)/2
        if probability:
            for x, count in endpoints.items():
                key = signs[-1], x
                law[key] = law.get(key, F())+probability*F(count, D**n)
    return law


def case(rho, old_case, word_cache):
    probabilities = {(a, b): (1+rho*a*b)/2 for a in (-1, 1) for b in (-1, 1)}
    matrices = {e: sm(F(1, 2), point_moment(ZERO)) for e in (-1, 1)}
    packets = {e: EffectHistogram.from_terms(D, [
        (F(1, D), Affine(eye(D), tuple(e if i == axis else 0 for i in range(D))), 1)
        for axis in range(D)]) for e in (-1, 1)}
    states = {e: {name: F(name == 'mass', 2) for name in OBSERVABLES} for e in (-1, 1)}
    law = {(e, ZERO): cwm_edge(F(1, 2)) for e in (-1, 1)}
    reference = {row['n']: row for row in old_case['rows']}
    rows, distribution_rows = [], []
    checks = dict(full_native_moment_steps=0, hidden_closed_moment_steps=0,
                  exact_formula_timepoints=0, old_sample_row_matches=0,
                  full_cwm_timepoints=0, independent_joint_law_matches=0,
                  joint_cwm_endpoints=0, primitive_edges=0,
                  conditional_observable_comparisons=0)
    for n in range(1, HORIZON+1):
        matrices = {e: packets[e].moment_action(ma(sm(probabilities[-1, e], matrices[-1]),
                                                      sm(probabilities[1, e], matrices[1])))
                    for e in (-1, 1)}
        states = closed_step(states, probabilities)
        joint = ma(matrices[-1], matrices[1])
        assert joint[-1][-1] == 1 and all(joint[i][-1] == 0 for i in range(D))
        covariance = tuple(tuple(joint[i][j] for j in range(D)) for i in range(D))
        hcov = mm(mm(P5, covariance), P5)
        assert hcov == sm(F(n, D), P5)
        total = {name: sum((states[e][name] for e in (-1, 1)), F()) for name in OBSERVABLES}
        variance = n+2*sum(((n-k)*rho**k for k in range(1, n)), F())
        assert total['s2'] == variance == sum((sum(row) for row in covariance), F())
        assert total['q'] == trace(hcov) == A*n
        assert total['q2'] == F(35*n*n-10*n, 36)
        assert total['a3'] == 0 and total['sa3'] == T3*variance
        assert total['q3'] == F(5, 216)*(63*n**3-54*n*n+16*variance)
        sign_a3 = states[1]['a3']-states[-1]['a3']
        assert sign_a3 == T3*sum((rho**k for k in range(n)), F())
        k4 = total['q2']-total['q']**2-2*trace(mm(hcov, hcov))
        c4 = k4/total['q']**2
        assert k4 == -F(5*n, 18) and c4 == -F(2, 5*n)
        # Odd unconditioned tensors vanish. On rank-5 covariance n*P5/6,
        # contraction of the 4+2 partitions is (9*n/2)*K4.
        k6 = total['q3']-F(9*n, 2)*k4-F(35*n**3, 24)
        assert k6 == F(10, 27)*variance
        standard_sixth = total['q3']/total['q']**3
        assert standard_sixth == F(63, 25)-F(54, 25*n)+F(16, 25*n**3)*variance
        if n in reference:
            prior = reference[n]
            assert covariance == tuple(tuple(F(v) for v in row) for row in prior['full_covariance'])
            assert variance == F(prior['scalar_variance'])
            assert trace(covariance) == F(prior['full_msd'])
            checks['old_sample_row_matches'] += 1
        if n <= ENUM_END:
            law, edges = old['full_cwm_step'](law, probabilities)
            expected = independent_markov_law(n, rho, word_cache)
            assert {key: value.total for key, value in law.items()} == expected
            histogram, pzero = {}, F()
            direct = {e: {name: F() for name in OBSERVABLES} for e in (-1, 1)}
            for (e, x), value in law.items():
                observed = readout(x)
                for name in OBSERVABLES:
                    direct[e][name] += value.total*observed[name]
                q = observed['q']
                histogram[q] = histogram.get(q, F())+value.total
                if q == 0:
                    pzero += value.total
            assert direct == states
            if n == 2:
                assert pzero == (1-rho)/12
                assert total['q3'] == (200+20*rho)/27
            distribution_rows.append(dict(n=n, hidden_zero_probability=pzero,
                                          hidden_squared_width_law=sorted(histogram.items())))
            checks['full_cwm_timepoints'] += 1
            checks['independent_joint_law_matches'] += 1
            checks['joint_cwm_endpoints'] += len(law)
            checks['primitive_edges'] += edges
            checks['conditional_observable_comparisons'] += 2*len(OBSERVABLES)
        checks['full_native_moment_steps'] += 1
        checks['hidden_closed_moment_steps'] += 1
        checks['exact_formula_timepoints'] += 1
        if n in SAMPLES:
            rows.append(dict(n=n, scalar_variance=variance, full_native_covariance=covariance,
                             hidden_second=total['q'],
                             hidden_fourth=total['q2'], hidden_kappa4_contraction=k4,
                             hidden_standardized_kappa4=c4, hidden_sixth=total['q3'],
                             hidden_kappa6_contraction=k6, hidden_standardized_sixth=standard_sixth,
                             hidden_sixth_gaussian_excess=standard_sixth-F(63, 25),
                             scalar_times_hidden_cubic=total['sa3'],
                             final_sign_times_hidden_cubic=sign_a3))
    return dict(rho=rho, checked_times='1..128 inclusive', sampled_times=sorted(SAMPLES),
                rows=rows, short_full_distribution=distribution_rows, checks=checks)


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(item) for item in value]
    return value


def run():
    prior = json.loads(OLD_RESULTS.read_text())
    assert prior['source_sha256'][str(OLD_SCRIPT.relative_to(ROOT))] == hashlib.sha256(OLD_SCRIPT.read_bytes()).hexdigest()
    word_cache, independent_checks, examples = independent_axis_words()
    old_cases = {F(item['rho']): item for item in prior['cases']}
    cases = [case(rho, old_cases[rho], word_cache) for rho in RHOS]
    totals = {key: sum(item['checks'][key] for item in cases) for key in cases[0]['checks']}
    result = dict(schema='NATIVE_X6_HIDDEN_CORRELATED_RESIDUAL_V1',
                  terminology='立体=原生完整六维；三维=其中一层晶包；时间另型；本程序不定义层选择。',
                  retained_state='full integer native X6 plus Markov sign; H=P5*X only an additional component readout',
                  hidden_readout='H=X-(sum X)*ones/6; not a Cell address or inter-axis flux',
                  shared_hidden_covariance=dict(formula='Cov(H_n)=n*unit_matrix, all six rho',
                                                unit_matrix=sm(F(1, D), P5)),
                  universal_scope='fixed arbitrary sign histories, iid uniform axis routing independent of signs: second and fourth moments',
                  low_moment_warning='stationary sign-reversal symmetric chains have identical H tensor moments through order 5; full H law depends on rho',
                  earliest_difference=dict(time=2, hidden_zero_probability='(1-rho)/12',
                                           pure_hidden_moment_degree=6, hidden_sixth='(200+20*rho)/27',
                                           mixed_scalar_hidden_degree=4),
                  cases=cases, checks=totals, independent_axis_word_checks=independent_checks,
                  fixed_sign_examples=examples,
                  source_sha256={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in (Path(__file__), OLD_SCRIPT, OLD_RESULTS,
                                           ROOT/'src/enterprise_math/brc_transport.py',
                                           ROOT/'src/enterprise_math/brc_weighted.py',
                                           ROOT/'definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md')})
    (HERE/'hidden_correlated_results.json').write_text(json.dumps(encode(result), ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', **totals, independent_axis_words=independent_checks)))
    return result


if __name__ == '__main__':
    run()
