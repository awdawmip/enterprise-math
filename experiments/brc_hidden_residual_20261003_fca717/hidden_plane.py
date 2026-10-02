#!/usr/bin/env python3
"""Exact hidden-readout tests in native X6; no primitive fractional Cell moves."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb, pi
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, EffectHistogram, MomentState, eye, ma, mm, mv, sm, transpose
from enterprise_math.brc_weighted import CWM_ZERO, cwm_edge, cwm_propagate, cwm_recoalesce


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


NATIVE_PATH = ROOT/'experiments/brc_native_x6_residual_20261002_fca717/run_x6.py'
SPATIAL_PATH = ROOT/'experiments/brc_residual_spatial_decay_20261002_fca717/run_spatial_decay.py'
OLD_RESULT = ROOT/'experiments/brc_x6_replay_20261002_fca717/weighted_return_results.json'
native = load('hidden_native_reference', NATIVE_PATH)
spatial = load('hidden_old_spatial_reference', SPATIAL_PATH)
STEPS = native.STEPS
ZERO = (0,)*6
U = tuple(tuple(F(i == j % 2) for j in range(6)) for i in range(2))
E = sm(F(1, 3), mm(transpose(U), U))
P = ma(eye(6), sm(-1, E))
P5 = tuple(tuple(F(i == j)-F(1, 6) for j in range(6)) for i in range(6))
SAMPLES = {1, 2, 3, 4, 8, 16, 32, 64, 128}
CHECKS = Counter()


def check(key, actual, expected):
    CHECKS[key] += 1
    if actual != expected:
        raise AssertionError((key, actual, expected))


def norm2(x):
    return sum((v*v for v in x), F())


def outer(x, y):
    return tuple(tuple(a*b for b in y) for a in x)


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F())


def add(x, y):
    return tuple(a+b for a, b in zip(x, y))


def hidden(x):
    sums = (sum(x[::2]), sum(x[1::2]))
    return tuple(F(a)-F(sums[i % 2], 3) for i, a in enumerate(x))


def old_step(law, noise):
    out = {}
    for x, w in law.items():
        for step, prob in noise.items():
            y = add(x, step)
            out[y] = cwm_recoalesce(out.get(y, CWM_ZERO), cwm_propagate(w, cwm_edge(prob)))
    return out


def routing_cases():
    # Both three-axis groups have total probability 1/2; the old planar
    # directions thus keep probability 1/4 for every case.
    old_noise = spatial.axis_law(2, F(1))
    cases = []
    uniform_returns = {}
    for label, q in [('uniform', (F(1, 3),)*3),
                     ('mild', (F(1, 2), F(1, 4), F(1, 4))),
                     ('strong', (F(4, 5), F(1, 10), F(1, 10)))]:
        probabilities = tuple(q[i//2]/2 for i in range(6))
        terms = [(dx, probabilities[i//2]/2) for i, dx in enumerate(STEPS)]
        push_noise = {}
        for dx, p in terms:
            y = mv(U, dx)
            push_noise[y] = push_noise.get(y, F())+p
        check('old_one_step_probability_law', push_noise, old_noise)
        innovation_cov = tuple(tuple(probabilities[i] if i == j else F() for j in range(6)) for i in range(6))
        hidden_cov = mm(mm(P, innovation_cov), P)
        one_trace_square = trace(mm(hidden_cov, hidden_cov))
        effective_rank = trace(hidden_cov)**2/one_trace_square
        conditional_spread_rate = 1-sum(v*v for v in q)
        packet = EffectHistogram.from_terms(6, [(p, Affine(eye(6), dx), 1) for dx, p in terms])
        state = MomentState.from_point(ZERO)
        law = {ZERO: cwm_edge(1)}
        old = {(0, 0): cwm_edge(1)}
        rows = []
        for n in range(1, 129):
            state = state.then(packet)
            mass, mean, covariance = native.matrix_stats(state.to_matrix())
            check('native_mass_and_mean', (mass, mean), (F(1), ZERO))
            check('native_covariance', covariance, sm(n, innovation_cov))
            hc = mm(mm(P, covariance), P)
            check('full_hidden_covariance', hc, sm(n, hidden_cov))
            hs = trace(hc)
            k4 = -2*n*one_trace_square
            gamma = k4/hs**2
            check('constant_single_step_hidden_norm', hs, F(2*n, 3))
            check('hidden_effective_rank_law', gamma, -2/(effective_rank*n))
            cond_spread = n*conditional_spread_rate if n % 2 == 0 else None
            cond_gamma = -F(n-2, 2*n*(n-1)) if n % 2 == 0 and label == 'uniform' else None
            enum_end = 6 if label == 'uniform' else 4
            if n <= enum_end:
                law, edges = native.cwm_step(law, terms)
                CHECKS['native_primitive_edges'] += edges
                old = old_step(old, old_noise)
                pushed = {}
                groups = {}
                hidden_fourth = F()
                conditional_cov = sm(0, eye(6))
                for x, weight in law.items():
                    y = mv(U, x)
                    h = hidden(x)
                    t = norm2(h)
                    check('native_position_integer', all(type(a) is int for a in x), True)
                    check('hidden_is_in_readout_kernel', mv(U, h), (F(), F()))
                    check('squared_component_decomposition', norm2(x), t+norm2(y)/3)
                    pushed[y] = cwm_recoalesce(pushed.get(y, CWM_ZERO), weight)
                    accum = groups.setdefault(y, [F(), F(), F(), F()])
                    accum[0] += weight.total
                    accum[1] += weight.total*t
                    accum[2] += weight.total*t*t
                    accum[3] += weight.total*t*t*t
                    hidden_fourth += weight.total*t*t
                    if y == (0, 0):
                        conditional_cov = ma(conditional_cov, sm(weight.total, outer(h, h)))
                check('old_planar_endpoint_support', set(pushed), set(old))
                for y in old:
                    check('old_planar_probability_law', pushed[y].total, old[y].total)
                    check('old_CWM_count_refinement', pushed[y].count, old[y].count*3**n)
                    check('old_CWM_dominant_refinement', pushed[y].dominant, old[y].dominant*max(q)**n)
                    if label == 'uniform':
                        check('hidden_spread_conditioned_on_every_old_endpoint', groups[y][1]/groups[y][0], hs)
                check('explicit_hidden_fourth', hidden_fourth, hs**2+2*trace(mm(hc, hc))+k4)
                if n % 2 == 0:
                    mass0, m2, m4, m6 = groups[(0, 0)]
                    check('conditioned_hidden_spread', m2/mass0, cond_spread)
                    if label == 'uniform':
                        cond_cov = sm(1/mass0, conditional_cov)
                        check('conditioned_hidden_covariance', cond_cov, hc)
                        ck = m4/mass0-hs**2-2*trace(mm(cond_cov, cond_cov))
                        check('conditioned_hidden_fourth', ck/hs**2, cond_gamma)
                        if n == 2:
                            check('zero_fourth_still_has_atom', law[ZERO].total/mass0, F(1, 3))
                            check('zero_fourth_non_Gaussian_sixth', m6/mass0, F(16, 3))
                if label == 'uniform':
                    uniform_returns[n] = sum((w.total for x, w in law.items() if hidden(x) == ZERO), F())
            if n in SAMPLES:
                rows.append(dict(n=n, native_covariance=covariance, hidden_covariance=hc,
                                 hidden_squared_spread=hs, hidden_kappa4_contraction=k4,
                                 hidden_normalized_kappa4=gamma,
                                 hidden_squared_spread_given_old_zero=cond_spread,
                                 hidden_normalized_kappa4_given_old_zero=cond_gamma))
        cases.append(dict(id=label, axis_probabilities=probabilities, within_group_axis_probabilities=q,
                          old_readout_law_unchanged=True, hidden_effective_rank=effective_rank,
                          hidden_spread_given_old_zero_rate=conditional_spread_rate,
                          conditional_zero_fourth_example=(dict(n=2, full_zero_atom=F(1, 3), hidden_M6=F(16, 3),
                                                               same_covariance_Gaussian_M6=F(64, 9)) if label == 'uniform' else None), rows=rows))
    return cases, uniform_returns


def return_queries(short_returns):
    # Independent integer lattice count: in either three-axis group, hidden
    # zero means the two coordinate differences vanish. Its six possible
    # projected steps are +/- (1,0), +/- (0,1), +/- (1,1).
    triangle_steps = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1))
    law = {(0, 0): 1}
    g = [1]
    for n in range(1, 129):
        out = {}
        for (x, y), count in law.items():
            for dx, dy in triangle_steps:
                key = x+dx, y+dy
                out[key] = out.get(key, 0)+count
        law = out
        g.append(law.get((0, 0), 0))
        check('triangle_word_count', sum(law.values()), 6**n)
        CHECKS['triangle_endpoint_observations'] += len(law)
    prior = json.loads(OLD_RESULT.read_text())
    old_returns = {r['step']: r for r in prior['returns']['rows']}
    rows = []
    for n in range(1, 129):
        count = sum(comb(n, j)*g[j]*g[n-j] for j in range(n+1))
        ph = F(count, 12**n)
        if n in short_returns:
            check('hidden_return_independent_lattice_matches_full_X6_CWM', ph, short_returns[n])
        p6 = F(old_returns[n]['full_X6_return']) if n % 2 == 0 else F()
        if n == 3:
            check('hidden_odd_return', ph, F(1, 72))
        if n in SAMPLES or n in {6, 12, 24, 48, 96}:
            rows.append(dict(n=n, hidden_zero_probability=ph, full_native_zero_probability=p6,
                             full_zero_given_hidden_zero=p6/ph if ph else None,
                             n_squared_hidden_zero_probability=n*n*ph))
    return dict(lattice_dimension=4, spatial_ontology_unchanged='native X6', period=1,
                exact_horizon=128, rows=rows, asymptotic='P(H_n=0) ~ 3/(pi^2*n^2)',
                asymptotic_constant_decimal=3/pi**2,
                distinction='H=0 is a readout-kernel event, not native Cell return or a crystal-layer return')


def directed_response_coupling():
    # New sensitivity test, retaining the previous iid scalar baseline exactly.
    # A acts only on rational response Z; integer native X takes primitive steps.
    beta = F(1, 4)
    ones = (1,)*6
    v = (1, -1, 0, 0, 0, 0)
    a = ma(eye(6), sm(beta, outer(v, ones)))
    check('old_scalar_transition_unchanged', tuple(sum(a[i][j] for i in range(6)) for j in range(6)), ones)
    packet = EffectHistogram.from_terms(6, [(F(1, 12), Affine(a, xi), 1) for xi in STEPS])
    state = MomentState.from_point(ZERO)
    s1 = s2 = s4 = F()
    joint = {(ZERO, ZERO): cwm_edge(1)}
    rows = []
    for n in range(1, 129):
        k = n-1
        s1 += k
        s2 += k*k
        s4 += k**4
        state = state.then(packet)
        _, mean, cov = native.matrix_stats(state.to_matrix())
        expected = ma(ma(sm(F(n, 6), eye(6)), sm(beta*s1/6, ma(outer(v, ones), outer(ones, v)))),
                      sm(beta*beta*s2, outer(v, v)))
        check('coupled_full_response_covariance', cov, expected)
        check('coupled_old_scalar_variance', sum(sum(row) for row in cov), n)
        hc = mm(mm(P5, cov), P5)
        spread = trace(hc)
        k4 = -F(5*n, 18)-8*beta**4*s4
        check('coupled_hidden_spread', spread, F(5*n, 6)+2*beta**2*s2)
        conditional_spread = F(5*n, 6)+beta**2*F(n*n*(n+1), 6) if n % 2 == 0 else None
        if n <= 3:
            out = {}
            for (x, z), weight in joint.items():
                for xi in STEPS:
                    target = add(x, xi), add(mv(a, z), xi)
                    out[target] = cwm_recoalesce(out.get(target, CWM_ZERO), cwm_propagate(weight, cwm_edge(F(1, 12))))
            joint = out
            independent = Counter()
            for word in product(STEPS, repeat=n):
                x = tuple(sum(w[i] for w in word) for i in range(6))
                accumulated = sum((n-1-j)*sum(w) for j, w in enumerate(word))
                z = add(x, tuple(beta*b*accumulated for b in v))
                independent[(x, z)] += 1
            check('coupled_joint_support', set(joint), set(independent))
            m4 = zero_mass = zero_m2 = F()
            pushed = {}
            for (x, z), count in independent.items():
                weight = joint[(x, z)]
                check('coupled_joint_CWM_triple', (weight.count, weight.total, weight.dominant),
                      (count, F(count, 12**n), F(1, 12**n)))
                check('coupled_same_scalar_path', sum(x), sum(z))
                h = mv(P5, z)
                m4 += weight.total*norm2(h)**2
                s = sum(z)
                pushed[s] = pushed.get(s, F())+weight.total
                if s == 0:
                    zero_mass += weight.total
                    zero_m2 += weight.total*norm2(h)
            check('coupled_old_scalar_complete_law', pushed, {2*j-n: F(comb(n, j), 2**n) for j in range(n+1)})
            check('coupled_explicit_fourth', m4-spread**2-2*trace(mm(hc, hc)), k4)
            if zero_mass:
                check('coupled_conditional_hidden_spread', zero_m2/zero_mass, conditional_spread)
        if n in SAMPLES:
            rows.append(dict(n=n, native_squared_spread=n, old_scalar_variance=n,
                             hidden_response_squared_spread=spread, hidden_response_kappa4=k4,
                             hidden_response_normalized_kappa4=k4/spread**2,
                             hidden_response_spread_given_old_scalar_zero=conditional_spread,
                             full_response_covariance=cov))
    return dict(beta=beta, A=a, transfer_direction=v, response_type='Z in Q6, not native Cell position',
                source_class='new controlled coupling, matched old iid scalar law',
                hidden_update='H_next=H + beta*v*S + P5*xi; S=sum(Z)',
                hidden_spread_asymptotic='n^3/24', hidden_normalized_kappa4_asymptotic='-18/(5*n)',
                transfer_scope='explicit visible-to-hidden response forcing; no conserved physical flux is asserted', rows=rows)


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


def main():
    CHECKS.clear()
    check('hidden_projector', mm(P, P), P)
    cases, short = routing_cases()
    result = dict(schema='BRC_HIDDEN_X6_PLANE_REVIEW_V1', horizon=128,
                  definition='H=P4 X is a rational component readout of full native X6, not another native Cell address',
                  U=U, P4=P, routing_cases=cases, hidden_returns=return_queries(short),
                  directed_coupling=directed_response_coupling())
    result['checks'] = dict(CHECKS)
    result['exact_check_calls'] = sum(CHECKS.values())-CHECKS['triangle_endpoint_observations']-CHECKS['native_primitive_edges']
    result['all_checks_passed'] = True
    result['source_sha256'] = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in (Path(__file__), NATIVE_PATH, SPATIAL_PATH, OLD_RESULT,
                                         ROOT/'src/enterprise_math/brc_transport.py', ROOT/'src/enterprise_math/brc_weighted.py')}
    (HERE/'hidden_plane_results.json').write_text(json.dumps(encode(result), ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', exact_check_calls=result['exact_check_calls'], counters=result['checks'])))
    return result


if __name__ == '__main__':
    main()
