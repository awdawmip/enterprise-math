#!/usr/bin/env python3
"""Exact, synthetic BRC calibration; no empirical or N0-native claim.

Run from any directory with Python 3.11+. Core checks use stdlib + existing BRC.
Gaussian reference means/covariances are closed-form, independently evaluated.
The optional plot uses matplotlib; all reported equalities use Fraction.
"""
from __future__ import annotations

import csv
import hashlib
import json
from fractions import Fraction as F
from math import comb, isqrt
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from enterprise_math.brc_transport import Affine, EffectHistogram, MomentState, inv

TRAIN = 8
HORIZON = 64


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F())


def transform(a, x, b):
    return tuple(dot(row, x) + v for row, v in zip(a, b))


def qroot(q):
    n, d = isqrt(q.numerator), isqrt(q.denominator)
    assert F(n*n, d*d) == q, 'This experiment requires rational branch offsets'
    return F(n, d)


def reference(kind, n, x):
    """Closed-form Gaussian linear-system moments, not BRC calls."""
    if kind == 'decay':
        a, q = F(3, 4), F(1, 16)
        return (a**n*x[0],), ((q*(1-a**(2*n))/(1-a*a),),)
    if kind == 'diffusion':
        return (x[0]+F(n, 3),), ((F(n, 4),),)
    re, im = F(1), F()
    for _ in range(n):
        re, im = F(3, 5)*re-F(4, 5)*im, F(4, 5)*re+F(3, 5)*im
    return (re*x[0]-im*x[1], im*x[0]+re*x[1]), ((F(n, 50), F()), (F(), F(n, 50)))


def regress(rows, targets):
    # Exact overdetermined least squares. Existing rational inverse is reused.
    cols = tuple(zip(*rows))
    gram = tuple(tuple(dot(a, b) for b in cols) for a in cols)
    gi = inv(gram)
    result = []
    for target in zip(*targets):
        rhs = tuple(dot(col, target) for col in cols)
        result.append(tuple(dot(row, rhs) for row in gi))
    assert all(tuple(dot(p, row) for p in result) == y for row, y in zip(rows, targets))
    return tuple(result)


def infer(kind, initial):
    d = len(initial[0])
    rows, targets = [], []
    for x in initial:
        for n in range(TRAIN):
            rows.append(reference(kind, n, x)[0]+(F(1),))
            targets.append(reference(kind, n+1, x)[0])
    coef = regress(rows, targets)
    a, b = tuple(r[:-1] for r in coef), tuple(r[-1] for r in coef)
    innovations = []
    for n in range(TRAIN):
        p, pn = reference(kind, n, initial[0])[1], reference(kind, n+1, initial[0])[1]
        innovations.append(tuple(tuple(pn[i][j]-sum((a[i][k]*p[k][l]*a[j][l]
            for k in range(d) for l in range(d)), F()) for j in range(d)) for i in range(d)))
    q = tuple(tuple(sum((p[i][j] for p in innovations), F())/TRAIN
                    for j in range(d)) for i in range(d))
    assert all(p == q for p in innovations)
    assert all(q[i][j] == (q[0][0] if i == j else 0) for i in range(d) for j in range(d))
    sigma = qroot(d*q[0][0])
    offsets = [tuple(sigma*sign if i == axis else F() for i in range(d))
               for axis in range(d) for sign in (-1, 1)]
    terms = [(F(1, 2*d), Affine(a, tuple(bi+ni for bi, ni in zip(b, noise))), 1)
             for noise in offsets]
    packet = EffectHistogram.from_terms(d, terms)
    return a, b, q, sigma, offsets, packet


def read_moments(state):
    m = state.to_matrix()
    d = state.dimension
    assert m[d][d] == 1
    mean = tuple(m[i][d] for i in range(d))
    p = tuple(tuple(m[i][j]-mean[i]*mean[j] for j in range(d)) for i in range(d))
    return mean, p


def enumerate_step(dist, a, b, offsets):
    out = {}
    for x, weight in dist.items():
        base = transform(a, x, b)
        for noise in offsets:
            y = tuple(v+z for v, z in zip(base, noise))
            out[y] = out.get(y, F())+weight/len(offsets)
    return out


def scalar_k4(kind, n, a, sigma):
    if kind != 'oscillator':
        return -2*sigma**4*sum((a[0][0]**(4*k) for k in range(n)), F())
    # Cumulants add for independent innovations. Project rotated innovations
    # onto the first coordinate; rotations preserve u^2+v^2=1.
    u, v, out = F(1), F(), F()
    for _ in range(n):
        out += sigma**4*((u**4+v**4)/2-F(3, 4)*(u*u+v*v)**2)
        u, v = u*a[0][0]+v*a[1][0], u*a[0][1]+v*a[1][1]
    return out


def checks_for(kind):
    train_x = [(F(-2),), (F(),), (F(3),)] if kind != 'oscillator' else [
        (F(), F()), (F(1), F()), (F(), F(1)), (F(-2), F(3))]
    test_x = [(F(7, 3),), (F(-5, 2),)] if kind != 'oscillator' else [
        (F(7, 3), F(-5, 2)), (F(-4), F(7))]
    a, b, q, sigma, offsets, packet = infer(kind, train_x)
    rows = []
    checked = 0
    for ix, x in enumerate(train_x+test_x):
        state = MomentState.from_point(x)
        for n in range(1, HORIZON+1):
            state = state.then(packet)
            got_m, got_p = read_moments(state)
            want_m, want_p = reference(kind, n, x)
            assert (got_m, got_p) == (want_m, want_p)
            checked += 1
            if ix == 0:
                k4 = scalar_k4(kind, n, a, sigma)
                variance = got_p[0][0]
                rows.append(dict(model=kind, n=n, split='train' if n <= TRAIN else 'heldout',
                    mean_error=F(), covariance_error=F(), deterministic_residual_mse=sum(
                    (got_p[i][i] for i in range(len(x))), F()), variance_x=variance,
                    gaussian_k4=F(), brc_k4_x=k4, excess_kurtosis_x=k4/variance**2,
                    radial_fourth_cumulant=-F(n, 625) if kind == 'oscillator' else k4))
    # Independent full distribution enumeration is feasible only for short n.
    x = train_x[0]
    dist = {x: F(1)}
    explicit_checks = 0
    for n in range(1, 6):
        dist = enumerate_step(dist, a, b, offsets)
        mean, cov = reference(kind, n, x)
        assert sum(dist.values(), F()) == 1
        for i in range(len(x)):
            assert sum((w*y[i] for y, w in dist.items()), F()) == mean[i]
            for j in range(len(x)):
                assert sum((w*(y[i]-mean[i])*(y[j]-mean[j]) for y, w in dist.items()), F()) == cov[i][j]
        fourth = sum((w*(y[0]-mean[0])**4 for y, w in dist.items()), F())
        assert fourth-3*cov[0][0]**2 == scalar_k4(kind, n, a, sigma)
        if kind == 'oscillator':
            radial_fourth = sum((w*sum(((y[i]-mean[i])**2 for i in range(2)), F())**2
                                for y, w in dist.items()), F())
            gaussian_radial_fourth = sum((cov[i][i] for i in range(2)), F())**2 + 2*sum(
                (cov[i][j]**2 for i in range(2) for j in range(2)), F())
            assert radial_fourth-gaussian_radial_fourth == -F(n, 625)
        explicit_checks += 1
    if kind != 'oscillator':
        # Separate raw central-moment recurrence verifies the cumulant formula
        # over the full horizon, not just short branch enumeration.
        moments = [F(1), F(), F(), F(), F()]
        noise = [F(1), F(), sigma*sigma, F(), sigma**4]
        for n in range(1, HORIZON+1):
            moments = [sum((comb(k, j)*a[0][0]**j*moments[j]*noise[k-j]
                            for j in range(k+1)), F()) for k in range(5)]
            assert moments[4]-3*moments[2]**2 == scalar_k4(kind, n, a, sigma)
    else:
        # Independent radial recurrence for isotropic covariance and fixed
        # innovation radius: S[n+1]=S[n]+4*sigma^2*E||R[n]||^2+sigma^4.
        radial_fourth = F()
        for n in range(HORIZON):
            radial_fourth += 4*sigma**2*F(n, 25)+sigma**4
            assert radial_fourth == F(2*(n+1)**2-(n+1), 625)
    return dict(model=kind, A=a, b=b, Q=q, branch_offset=sigma,
                calibration_transitions=len(train_x)*TRAIN,
                trajectory_moment_checks=checked, explicit_distribution_checks=explicit_checks,
                unseen_initial_conditions=len(test_x), all_exact_checks_passed=True,
                n64=rows[-1]), rows


def counterexamples():
    # Both positive rational distributions have mean 0 and second moment 1.
    laws = [{F(-1): F(1, 2), F(1): F(1, 2)},
            {F(-2): F(1, 8), F(): F(3, 4), F(2): F(1, 8)}]
    raw = [[sum((w*x**k for x, w in law.items()), F()) for k in range(5)] for law in laws]
    assert raw[0][:3] == raw[1][:3] == [1, 0, 1]
    assert [r[4] for r in raw] == [1, 4]
    # Under nonlinear Y=X^2, mean remains 1, variance becomes 0 versus 3.
    nonlinear_variances = [r[4]-r[2]**2 for r in raw]
    assert nonlinear_variances == [0, 3]
    zero_k4 = {F(): F(1, 2), F(-1): F(1, 6), F(1): F(1, 6),
               F(-2): F(1, 12), F(2): F(1, 12)}
    raw_zero_k4 = [sum((w*x**k for x, w in zero_k4.items()), F()) for k in range(7)]
    assert raw_zero_k4 == [1, 0, 1, 0, 3, 0, 11]
    # Same frozen fitted model, but variance rate doubles after time 16.
    # Run both production BRC transports, including the changed branch shape.
    *_, stationary_packet = infer('diffusion', [(F(-2),), (F(),), (F(3),)])
    changed_packet = EffectHistogram.from_terms(1, [
        (weight, Affine(((F(1),),), (F(1, 3)+noise,)), 1)
        for noise, weight in [(F(-1), F(1, 4)), (F(), F(1, 2)), (F(1), F(1, 4))]])
    frozen, changed = MomentState.from_point((0,)), MomentState.from_point((0,))
    for n in range(64):
        frozen = frozen.then(stationary_packet)
        changed = changed.then(stationary_packet if n < 16 else changed_packet)
    fm, fp = read_moments(frozen)
    cm, cp = read_moments(changed)
    assert fm == cm == (F(64, 3),)
    stationary_prediction, shifted_observation = fp[0][0], cp[0][0]
    assert stationary_prediction == 16 and shifted_observation == 28
    assert shifted_observation-stationary_prediction == 12
    # Mean-only calibration cannot distinguish deterministic/branching kernels.
    return dict(equal_first_two_moments=raw[0][:3], distinct_fourth_moments=[r[4] for r in raw],
        nonlinear_x_squared_variances=nonlinear_variances,
        zero_fourth_cumulant_non_gaussian_raw_moments=raw_zero_k4,
        same_variance_possible_innovation_k4=[F(-2), F(1), F()],
        changed_noise_n64_prediction=stationary_prediction,
        changed_noise_n64_observation=shifted_observation,
        changed_noise_n64_covariance_error=shifted_observation-stationary_prediction,
        mean_only_noise_identifiable=False)


def json_value(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: json_value(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [json_value(v) for v in x]
    return x


def run():
    outcomes, rows = [], []
    for kind in ('decay', 'diffusion', 'oscillator'):
        outcome, model_rows = checks_for(kind)
        outcomes.append(outcome)
        rows.extend(model_rows)
    summary = dict(experiment='BRC_MODEL_BENCHMARK_20261002_FCA717',
        evidence='EXACT_SYNTHETIC_CALIBRATION_NOT_EMPIRICAL_NOT_N0_PROMOTION',
        train_steps=TRAIN, horizon=HORIZON,
        reuse_resolution='REUSE_EXECUTED: brc_transport.Affine/EffectHistogram/MomentState/inv',
        models=outcomes, counterexamples=counterexamples(),
        source_sha256={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (Path(__file__), ROOT/'src/enterprise_math/brc_transport.py')})
    (HERE/'results.json').write_text(json.dumps(json_value(summary), indent=2, ensure_ascii=False)+'\n')
    with (HERE/'residuals.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps(json_value(summary), indent=2, ensure_ascii=False))


if __name__ == '__main__':
    run()
