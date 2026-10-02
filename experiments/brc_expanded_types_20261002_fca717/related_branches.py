#!/usr/bin/env python3
"""Exact weighted, finite-window, and correlated BRC residual experiments.

All equality checks use Fraction. Early calibration is a diagnostic of declared
families, not blind law discovery. No production files are modified.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from enterprise_math.brc_transport import (
    Affine, EffectHistogram, MomentState, eye, ma, point_moment, sm,
)

HORIZON = 128
CALIBRATION = 16
SAMPLE_N = {0, 1, 2, 4, 8, 16, 32, 64, 128}


def scalar_packet(amplitude):
    return EffectHistogram.from_terms(1, [
        (F(1, 2), Affine(eye(1), (sign*amplitude,)), 1)
        for sign in (-1, 1)])


def convolve_scalar(dist, amplitude):
    out = {}
    for x, weight in dist.items():
        for sign in (-1, 1):
            y = x + sign*amplitude
            out[y] = out.get(y, F()) + weight/2
    return out


def fit_diagnostic(rows, shape_key, train_selector=None):
    train = [r for r in rows if r['n'] <= CALIBRATION and r['gamma4'] is not None
             and (train_selector is None or train_selector(r))]
    heldout = [r for r in rows if r['n'] > CALIBRATION and r['gamma4'] is not None]
    amplitude = sum((r[shape_key]*r['gamma4'] for r in train), F()) / sum(
        (r[shape_key]**2 for r in train), F())
    errors = [abs(amplitude*r[shape_key]-r['gamma4']) for r in heldout]
    return dict(calibration_points=len(train), heldout_points=len(heldout),
                amplitude=amplitude, max_absolute_heldout_error=max(errors),
                exact_heldout_matches=sum(e == 0 for e in errors))


def weighted_independent():
    families = {
        'equal': lambda j: F(1),
        'linear_j': lambda j: F(j),
        'geometric_decay': lambda j: F(3, 4)**(j-1),
        'geometric_growth': lambda j: F(4, 3)**(j-1),
    }
    outputs, moment_checks, explicit_checks = {}, 0, 0
    for name, weight_at in families.items():
        state = MomentState.from_point((0,))
        raw = [F(1), F(), F(), F(), F()]
        dist = {F(): F(1)}
        sum2, sum4, rows = F(), F(), []
        for n in range(1, HORIZON+1):
            weight = weight_at(n)
            state = state.then(scalar_packet(weight))
            innovation = [F(1), F(), weight**2, F(), weight**4]
            raw = [sum((comb(k, j)*raw[j]*innovation[k-j] for j in range(k+1)), F())
                   for k in range(5)]
            sum2 += weight**2
            sum4 += weight**4
            matrix = state.to_matrix()
            assert matrix == ((sum2, F()), (F(), F(1)))
            assert raw[:3] == [1, 0, sum2]
            k4 = raw[4]-3*raw[2]**2
            assert k4 == -2*sum4
            effective_count = sum2**2/sum4
            gamma = k4/sum2**2
            assert gamma == -2/effective_count
            if name == 'equal':
                assert effective_count == n
            elif name == 'linear_j':
                assert sum2 == F(n*(n+1)*(2*n+1), 6)
                assert sum4 == F(n*(n+1)*(2*n+1)*(3*n*n+3*n-1), 30)
            else:
                ratio = F(3, 4) if name == 'geometric_decay' else F(4, 3)
                assert sum2 == (1-ratio**(2*n))/(1-ratio**2)
                assert sum4 == (1-ratio**(4*n))/(1-ratio**4)
            moment_checks += 1
            if n <= 8:
                dist = convolve_scalar(dist, weight)
                direct = [sum((p*x**k for x, p in dist.items()), F()) for k in range(5)]
                assert direct == raw
                explicit_checks += 1
            rows.append(dict(n=n, variance=sum2, kappa4=k4, gamma4=gamma,
                             effective_count=effective_count,
                             inverse_effective_count=1/effective_count,
                             inverse_time=F(1, n), constant=F(1)))
        effective_fit = fit_diagnostic(rows, 'inverse_effective_count')
        assert effective_fit['amplitude'] == -2
        assert effective_fit['exact_heldout_matches'] == HORIZON-CALIBRATION
        outputs[name] = dict(
            rows=rows, effective_count_fit=effective_fit,
            inverse_time_fit=fit_diagnostic(rows, 'inverse_time'),
            constant_fit=fit_diagnostic(rows, 'constant'),
            asymptotic=dict(
                effective_count=('n' if name == 'equal' else '5*n/9' if name == 'linear_j' else '25/7'),
                gamma4=('-2/n' if name == 'equal' else '-18/(5*n)' if name == 'linear_j' else '-14/25'),
                rms_width_exponent=(-2 if name == 'equal' else '-2/3' if name == 'linear_j'
                                    else 'no_unbounded_width' if name == 'geometric_decay' else 0)))
    return dict(families=outputs, production_moment_checks=moment_checks,
                explicit_distribution_checks=explicit_checks)


def finite_windows():
    outputs, moment_checks, explicit_checks = {}, 0, 0
    for length in (2, 4, 8):
        shift = tuple(tuple(F(j == i-1) if i else F() for j in range(length))
                      for i in range(length))
        packet = EffectHistogram.from_terms(length, [
            (F(1, 2), Affine(shift, (F(sign),)+(F(),)*(length-1)), 1)
            for sign in (-1, 1)])
        state = MomentState.from_point((0,)*length)
        dist = {(F(),)*length: F(1)}
        rows = []
        for n in range(1, HORIZON+1):
            state = state.then(packet)
            matrix = state.to_matrix()
            count = min(n, length)
            assert matrix[-1][-1] == 1
            assert all(matrix[i][-1] == 0 for i in range(length))
            assert all(matrix[i][j] == F(i == j and i < count)
                       for i in range(length) for j in range(length))
            variance = sum((matrix[i][j] for i in range(length) for j in range(length)), F())
            assert variance == count
            # The maintained coordinates are distinct independent signs. This
            # combinatorial fourth moment is checked against explicit states.
            fourth = F(count+6*comb(count, 2))
            k4 = fourth-3*variance**2
            assert k4 == -2*count
            gamma = k4/variance**2
            if n <= length+2:
                nxt = {}
                for x, p in dist.items():
                    for sign in (-1, 1):
                        y = (F(sign),)+x[:-1]
                        nxt[y] = nxt.get(y, F())+p/2
                dist = nxt
                assert sum(dist.values(), F()) == 1
                assert sum((p*sum(x, F())**2 for x, p in dist.items()), F()) == variance
                assert sum((p*sum(x, F())**4 for x, p in dist.items()), F()) == fourth
                explicit_checks += 1
            if n >= length:
                assert gamma == -F(2, length)
            moment_checks += 1
            rows.append(dict(n=n, variance=variance, gamma4=gamma,
                             inverse_time=F(1, n), constant=F(1)))
        constant_fit = fit_diagnostic(rows, 'constant', lambda r: r['n'] >= length)
        assert constant_fit['exact_heldout_matches'] == HORIZON-CALIBRATION
        outputs[str(length)] = dict(rows=rows, saturated_constant_fit=constant_fit,
                                   inverse_time_fit=fit_diagnostic(rows, 'inverse_time'),
                                   stationary_gamma4=-F(2, length),
                                   initial_condition='zero padded until full window')
    return dict(windows=outputs, production_moment_checks=moment_checks,
                explicit_distribution_checks=explicit_checks)


def markov_signs():
    outputs, moment_checks, explicit_checks, degenerate_points = {}, 0, 0, 0
    for rho in (F(-1), F(-1, 2), F(), F(1, 2), F(3, 4), F(1)):
        probabilities = {(source, target): (1+rho*source*target)/2
                         for source in (-1, 1) for target in (-1, 1)}
        edges = {(source, target): EffectHistogram.from_terms(1, [
            (p, Affine(eye(1), (F(target),)), 1)])
            for (source, target), p in probabilities.items() if p > 0}
        # Half mass in either hidden sign at n=0, independent of X_0=0.
        matrices = {sign: sm(F(1, 2), point_moment((0,))) for sign in (-1, 1)}
        raw = {sign: [F(1, 2), F(), F(), F(), F()] for sign in (-1, 1)}
        dist = {(sign, 0): F(1, 2) for sign in (-1, 1)}
        rows = []
        for n in range(1, HORIZON+1):
            nxt_matrix = {sign: ((F(), F()), (F(), F())) for sign in (-1, 1)}
            nxt_raw = {sign: [F()]*5 for sign in (-1, 1)}
            for (source, target), edge in edges.items():
                p = probabilities[source, target]
                nxt_matrix[target] = ma(nxt_matrix[target], edge.moment_action(matrices[source]))
                for k in range(5):
                    nxt_raw[target][k] += p*sum((comb(k, j)*target**(k-j)*raw[source][j]
                                                for j in range(k+1)), F())
            matrices, raw = nxt_matrix, nxt_raw
            for sign in (-1, 1):
                assert matrices[sign] == ((raw[sign][2], raw[sign][1]),
                                           (raw[sign][1], raw[sign][0]))
                assert raw[sign][0] == F(1, 2)
            totals = [sum((raw[sign][k] for sign in (-1, 1)), F()) for k in range(5)]
            assert totals[0] == 1 and totals[1] == 0 and totals[3] == 0
            variance = totals[2]
            closed_variance = n+2*sum(((n-k)*rho**k for k in range(1, n)), F())
            assert variance == closed_variance
            k4 = totals[4]-3*variance**2
            gamma = k4/variance**2 if variance else None
            if rho == 0:
                assert gamma == -F(2, n)
            elif rho == 1:
                assert variance == n*n and gamma == -2
            elif rho == -1:
                assert variance == n % 2
                assert gamma == (-2 if n % 2 else None)
            if variance == 0:
                assert k4 == 0
                degenerate_points += 1
            if n <= 10:
                nxt = {}
                for (source, x), weight in dist.items():
                    for target in (-1, 1):
                        p = probabilities[source, target]
                        if p:
                            key = target, x+target
                            nxt[key] = nxt.get(key, F())+weight*p
                dist = nxt
                for sign in (-1, 1):
                    assert [sum((p*x**k for (target, x), p in dist.items() if target == sign), F())
                            for k in range(5)] == raw[sign]
                explicit_checks += 1
            moment_checks += 1
            rows.append(dict(n=n, variance=variance, kappa4=k4, gamma4=gamma,
                             n_gamma4=None if gamma is None else n*gamma,
                             inverse_time=F(1, n), constant=F(1),
                             boundary=None if variance else 'ZERO_VARIANCE_NORMALIZATION_UNDEFINED'))
        if abs(rho) < 1:
            diffusion = (1+rho)/(1-rho)
            k4_rate = diffusion*(1-3*diffusion**2)
            coefficient = 1/diffusion-3*diffusion
            asymptotic = dict(variance_rate=diffusion, fourth_cumulant_rate=k4_rate,
                              n_gamma4_limit=coefficient,
                              n128_n_gamma4=rows[-1]['n_gamma4'],
                              n128_coefficient_error=rows[-1]['n_gamma4']-coefficient,
                              status='PROVED_LEADING_ORDER_WITH_FINITE_TIME_CORRECTIONS')
        else:
            asymptotic = dict(status='OUTSIDE_MIXING_HYPOTHESIS',
                              reason='ballistic persistent sign' if rho == 1 else
                              'period two; all even times have zero variance')
        outputs[str(rho)] = dict(rows=rows, asymptotic=asymptotic,
                                inverse_time_fit=fit_diagnostic(rows, 'inverse_time'),
                                constant_fit=fit_diagnostic(rows, 'constant'),
                                retains_hidden_sign=True,
                                initial_condition='stationary sign, deterministic X_0=0')
    return dict(correlations=outputs, production_moment_checks=moment_checks,
                conditional_raw_moment_checks=moment_checks,
                exact_variance_formula_checks=moment_checks,
                explicit_distribution_checks=explicit_checks,
                zero_variance_points=degenerate_points)


def rational_json(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: rational_json(v) for key, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [rational_json(v) for v in value]
    return value


def sampled_export(value):
    """Keep all diagnostics, sample trajectories after all 128 checks finish."""
    if not isinstance(value, dict):
        return value
    out = {}
    for key, item in value.items():
        if key != 'rows':
            out[key] = sampled_export(item) if isinstance(item, dict) else item
            continue
        selected = set(SAMPLE_N)
        changes, previous = [], None
        undefined = []
        for row in item:
            gamma = row['gamma4']
            if gamma is None:
                undefined.append(row['n'])
                continue
            if previous is not None and gamma*previous['gamma4'] < 0:
                changes.append([previous['n'], row['n']])
                selected.update(changes[-1])
            if gamma == 0:
                selected.update((row['n']-1, row['n'], row['n']+1))
            previous = row
        retained = [dict(n=0, variance=F(), kappa4=F(), gamma4=None,
                         boundary='INITIAL_ZERO_VARIANCE_NORMALIZATION_UNDEFINED')]
        retained.extend({k: v for k, v in row.items()
                         if k not in ('inverse_time', 'constant', 'inverse_effective_count')}
                        for row in item if row['n'] in selected)
        out['rows'] = retained
        out['row_sampling'] = dict(
            full_checked_times='1..128 inclusive', default_retained_times=sorted(SAMPLE_N),
            retained_times=[row['n'] for row in retained],
            gamma4_sign_change_pairs=changes,
            undefined_normalization_checked_times=undefined,
            diagnostics_use_all_calibration_and_heldout_times=True,
            full_trajectories_reproducible_from_script=True)
    return out


def run():
    result = dict(
        experiment='BRC_EXPANDED_RELATED_BRANCHES_20261002',
        researcher_id='EM-DIRECT-A48630',
        activity_id='RA-70DB5A0661EF6ED2B729F8A4',
        evidence='EXACT_DECLARED_MODELS_NOT_BLIND_DISCOVERY_OR_DRIVER_REVIEW',
        horizon=HORIZON, calibration_end=CALIBRATION,
        reuse_resolution='COMPOSE_APPLIED: affine BRC moments, finite shift state, two-sign control indexing',
        weighted_independent=weighted_independent(),
        finite_windows=finite_windows(),
        markov_signs=markov_signs(),
        source_sha256={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in (Path(__file__), ROOT/'src/enterprise_math/brc_transport.py')})
    sections = [result[k] for k in ('weighted_independent', 'finite_windows', 'markov_signs')]
    result['counts'] = dict(
        production_moment_checks=sum(s['production_moment_checks'] for s in sections),
        explicit_distribution_checks=sum(s['explicit_distribution_checks'] for s in sections),
        conditional_markov_raw_moment_checks=result['markov_signs']['conditional_raw_moment_checks'],
        exact_markov_variance_checks=result['markov_signs']['exact_variance_formula_checks'],
        zero_variance_points=result['markov_signs']['zero_variance_points'])
    (HERE/'related_results.json').write_text(json.dumps(rational_json(sampled_export(result)), indent=2)+'\n')
    print(json.dumps(dict(status='PASS', **result['counts'])))
    return result


if __name__ == '__main__':
    run()
