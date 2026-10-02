#!/usr/bin/env python3
"""Replay the existing sign chain in full native X6 with independent axis routing.

sum(X) equals the old scalar process path by path. Probability laws are kept;
path counts and largest individual path weights change under the 6^n routing
refinement. All checks use Fraction and all spatial steps are +/- E_i.
"""
from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, EffectHistogram, eye, ma, sm, point_moment
from enterprise_math.brc_weighted import CWM_ZERO, cwm_edge, cwm_propagate, cwm_recoalesce

D = 6
HORIZON = 128
ENUM_END = 4
SAMPLES = {1, 2, 3, 4, 8, 16, 32, 64, 128}
RHOS = (F(-1), F(-1, 2), F(), F(1, 2), F(3, 4), F(1))
ZERO = (0,)*D
OLD_SOURCE = ROOT/'experiments/brc_expanded_types_20261002_fca717/related_branches.py'


def old_reference():
    # Execute definitions without running its main or writing a pyc/old output.
    namespace = {'__file__': str(OLD_SOURCE), '__name__': 'old_sign_reference'}
    exec(compile(OLD_SOURCE.read_text(), str(OLD_SOURCE), 'exec'), namespace)
    assert namespace['HORIZON'] == HORIZON
    return namespace['markov_signs']()


def norm2(x):
    return sum((a*a for a in x), F())


def trace(matrix):
    return sum((matrix[i][i] for i in range(len(matrix))), F())


def conditional_radial_step(old, probabilities):
    # Entries are unnormalized E[1_{hidden sign} * observable]. Here T=||X||^2.
    # The closed observable family is 1,S,S^2,T,T*S,T^2.
    result = {}
    for target in (-1, 1):
        a = [sum((probabilities[source, target]*old[source][k]
                  for source in (-1, 1)), F()) for k in range(6)]
        mass, s, s2, t, ts, t2 = a
        result[target] = [
            mass,
            s+target*mass,
            s2+2*target*s+mass,
            t+F(2*target, D)*s+mass,
            ts+target*t+F(2*target, D)*s2+(1+F(2, D))*s+target*mass,
            t2+F(4*target, D)*ts+(2+F(4, D))*t+F(4*target, D)*s+mass,
        ]
    return result


def full_cwm_step(law, probabilities):
    nxt = {}
    edges = 0
    for (source, x), value in law.items():
        for target in (-1, 1):
            probability = probabilities[source, target]
            if not probability:
                continue
            edge = cwm_edge(probability/D)
            for axis in range(D):
                y = tuple(a+(target if i == axis else 0) for i, a in enumerate(x))
                assert sum(abs(a-b) for a, b in zip(x, y)) == 1
                assert sum(y)-sum(x) == target
                key = target, y
                nxt[key] = cwm_recoalesce(nxt.get(key, CWM_ZERO), cwm_propagate(value, edge))
                edges += 1
    return nxt, edges


def scalar_cwm_step(law, probabilities):
    nxt = {}
    for (source, scalar), value in law.items():
        for target in (-1, 1):
            probability = probabilities[source, target]
            if probability:
                key = target, scalar+target
                nxt[key] = cwm_recoalesce(nxt.get(key, CWM_ZERO),
                                         cwm_propagate(value, cwm_edge(probability)))
    return nxt


def verify_distribution(full, scalar, radial, covariance, scalar_row, n):
    projected = {}
    for (sign, x), value in full.items():
        key = sign, sum(x)
        projected[key] = cwm_recoalesce(projected.get(key, CWM_ZERO), value)
    assert set(projected) == set(scalar)
    for key, old in scalar.items():
        new = projected[key]
        assert new.total == old.total
        assert new.count == old.count*D**n
        assert new.dominant == old.dominant/D**n
    for sign in (-1, 1):
        direct = [F()]*6
        for (target, x), value in full.items():
            if target != sign:
                continue
            s, t = F(sum(x)), norm2(x)
            for j, observable in enumerate((F(1), s, s*s, t, t*s, t*t)):
                direct[j] += value.total*observable
        assert direct == radial[sign]
    assert sum((value.total for value in full.values()), F()) == 1
    direct_covariance = tuple(tuple(sum((value.total*x[i]*x[j] for (_, x), value in full.items()), F())
                                       for j in range(D)) for i in range(D))
    assert direct_covariance == covariance
    scalar_second = sum((value.total*s*s for (_, s), value in scalar.items()), F())
    scalar_fourth = sum((value.total*s**4 for (_, s), value in scalar.items()), F())
    assert scalar_second == scalar_row['variance']
    assert scalar_fourth-3*scalar_second**2 == scalar_row['kappa4']


def run_case(rho, old_case):
    probability = {(source, target): (1+rho*source*target)/2
                   for source in (-1, 1) for target in (-1, 1)}
    assert all(sum(probability[source, target] for target in (-1, 1)) == 1
               for source in (-1, 1))
    axis_packets = {target: EffectHistogram.from_terms(D, [
        (F(1, D), Affine(eye(D), tuple(target if i == axis else 0 for i in range(D))), 1)
        for axis in range(D)]) for target in (-1, 1)}
    matrices = {sign: sm(F(1, 2), point_moment(ZERO)) for sign in (-1, 1)}
    radial = {sign: [F(1, 2)]+[F()]*5 for sign in (-1, 1)}
    full = {(sign, ZERO): cwm_edge(F(1, 2)) for sign in (-1, 1)}
    scalar = {(sign, 0): cwm_edge(F(1, 2)) for sign in (-1, 1)}
    rows, checks = [], dict(production_moment_steps=0, old_scalar_comparisons=0,
                           independent_radial_closure_checks=0, full_distribution_steps=0,
                           cwm_joint_endpoint_observations=0, cwm_primitive_edge_checks=0,
                           projected_cwm_triple_checks=0, old_undefined_normalizations=0)
    old_rows = old_case['rows']
    assert len(old_rows) == HORIZON
    previous_old_sign, previous_full_sign, sign_changes = None, None, []
    for n in range(1, HORIZON+1):
        new_matrices = {}
        for target in (-1, 1):
            mixture = ma(sm(probability[-1, target], matrices[-1]),
                         sm(probability[1, target], matrices[1]))
            new_matrices[target] = axis_packets[target].moment_action(mixture)
        matrices = new_matrices
        radial = conditional_radial_step(radial, probability)
        matrix = ma(matrices[-1], matrices[1])
        assert matrix[-1][-1] == 1
        assert all(matrix[i][-1] == 0 for i in range(D))
        covariance = tuple(tuple(matrix[i][j] for j in range(D)) for i in range(D))
        old_row = old_rows[n-1]
        assert old_row['n'] == n
        scalar_variance, scalar_k4 = old_row['variance'], old_row['kappa4']
        predicted = tuple(tuple(F(n, D)*(i == j)+(scalar_variance-n)/(D*D)
                                for j in range(D)) for i in range(D))
        assert covariance == predicted
        total = [sum(radial[sign][k] for sign in (-1, 1)) for k in range(6)]
        assert total[0] == 1 and total[1] == 0
        assert total[2] == scalar_variance
        assert sum((covariance[i][j] for i in range(D) for j in range(D)), F()) == scalar_variance
        full_msd = trace(covariance)
        assert total[3] == full_msd == ((D-1)*n+scalar_variance)/D
        trace_square = sum((covariance[i][j]**2 for i in range(D) for j in range(D)), F())
        full_k4 = total[5]-full_msd**2-2*trace_square
        assert full_k4 == (scalar_k4-2*(D-1)*n)/(D*D)
        full_gamma = full_k4/full_msd**2
        assert full_gamma == (scalar_k4-10*n)/(5*n+scalar_variance)**2
        longitudinal, transverse = scalar_variance/D, F(n, D)
        assert full_msd == longitudinal+(D-1)*transverse
        if rho == -1:
            assert scalar_variance == n % 2
            assert full_gamma == -F(2, 5*n+n % 2)
        elif rho == 1:
            assert scalar_variance == n*n
            assert full_gamma == -F(2*n**4+10*n, (n*n+5*n)**2)
        elif rho == 0:
            assert covariance == tuple(tuple(F(n, D) if i == j else F() for j in range(D)) for i in range(D))
            assert full_gamma == -F(1, 3*n)
        if old_row['gamma4'] is None:
            checks['old_undefined_normalizations'] += 1
        if n <= ENUM_END:
            full, edge_count = full_cwm_step(full, probability)
            scalar = scalar_cwm_step(scalar, probability)
            verify_distribution(full, scalar, radial, covariance, old_row, n)
            checks['full_distribution_steps'] += 1
            checks['cwm_joint_endpoint_observations'] += len(full)
            checks['cwm_primitive_edge_checks'] += edge_count
            checks['projected_cwm_triple_checks'] += len(scalar)
        checks['production_moment_steps'] += 1
        checks['old_scalar_comparisons'] += 1
        checks['independent_radial_closure_checks'] += 1
        old_sign = None if scalar_k4 == 0 else (1 if scalar_k4 > 0 else -1)
        full_sign = None if full_k4 == 0 else (1 if full_k4 > 0 else -1)
        if n > 1 and ((old_sign is not None and previous_old_sign is not None and old_sign != previous_old_sign)
                      or (full_sign is not None and previous_full_sign is not None and full_sign != previous_full_sign)):
            sign_changes.append([n-1, n])
        previous_old_sign, previous_full_sign = old_sign, full_sign
        rows.append(dict(n=n, scalar_variance=scalar_variance, scalar_kappa4=scalar_k4,
                         scalar_gamma4=old_row['gamma4'], full_covariance=covariance,
                         full_msd=full_msd, longitudinal_squared_readout=longitudinal,
                         transverse_squared_readout=(D-1)*transverse,
                         longitudinal_eigenvalue=longitudinal,
                         transverse_eigenvalue=transverse, transverse_multiplicity=5,
                         covariance_rank=5+(scalar_variance > 0), full_radial_fourth_moment=total[5],
                         full_kappa4_contraction=full_k4, full_gamma4=full_gamma,
                         scalar_zero_with_positive_full_msd=scalar_variance == 0 and full_msd > 0))
    retained = set(SAMPLES)
    for pair in sign_changes:
        retained.update(pair)
    asymptotic = dict(status='NONMIXING_BOUNDARY', rho=rho)
    if abs(rho) < 1:
        diffusion = (1+rho)/(1-rho)
        scalar_rate = diffusion*(1-3*diffusion**2)
        full_coefficient = (scalar_rate-10)/(5+diffusion)**2
        assert full_coefficient < 0
        asymptotic = dict(status='PROVED_LEADING_ORDER', scalar_variance_rate=diffusion,
                          scalar_kappa4_rate=scalar_rate,
                          scalar_n_gamma4_limit=1/diffusion-3*diffusion,
                          full_n_gamma4_limit=full_coefficient,
                          n128_full_n_gamma4=HORIZON*rows[-1]['full_gamma4'])
    return dict(rho=rho, stationary_hidden_sign=True, old_horizon_preserved=HORIZON,
                axis_routing='iid uniform on six axes, independent of entire sign process',
                exact_scalar_observer='sum of all six raw coordinates',
                checks=checks, asymptotic=asymptotic,
                all_checked_full_kappa4_negative=all(r['full_kappa4_contraction'] < 0 for r in rows),
                finite_sign_result_scope='verified n=1..128 for this rho; not a universal finite-n theorem',
                row_sampling=dict(checked_times='1..128 inclusive', retained_times=sorted(retained),
                                  sign_change_pairs=sign_changes),
                rows=[r for r in rows if r['n'] in retained])


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [encode(v) for v in x]
    return x


def run():
    old = old_reference()
    cases = [run_case(rho, old['correlations'][str(rho)]) for rho in RHOS]
    totals = {key: sum(case['checks'][key] for case in cases) for key in cases[0]['checks']}
    result = dict(schema='EXACT_OLD_SIGN_MODEL_TO_NATIVE_X6_REPLAY_V1',
                  terminology={'立体': '完整六维原生空间', '三维': '用户定义的一层晶包；本程序不定义具体层划分'},
                  scalar_probability_law_preserved=True, full_cwm_triple_preserved=False,
                  provenance_refinement='for each old sign word: 6^n axis words; projected count times 6^n, dominant divided by 6^n, total unchanged',
                  transverse_scope='component-square linear algebra, not a crystal layer or new native perpendicularity',
                  horizon=HORIZON, full_joint_distribution_depth=ENUM_END, cases=cases, checks=totals,
                  source_sha256={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in (Path(__file__), OLD_SOURCE, ROOT/'src/enterprise_math/brc_transport.py',
                                           ROOT/'src/enterprise_math/brc_weighted.py',
                                           ROOT/'definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md')})
    (HERE/'correlated_results.json').write_text(json.dumps(encode(result), ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', **totals)))
    return result


if __name__ == '__main__':
    run()
