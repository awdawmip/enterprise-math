#!/usr/bin/env python3
"""Exact BRC spatial-scale and shell-flux controls; no gravity claim.

Classical toy coordinates, graph shells, and normalized probabilities are
explicit comparison choices, not changes to Enterprise Math native geometry.
"""
from __future__ import annotations
import csv
import hashlib
import json
from fractions import Fraction as F
from itertools import product
from math import comb, isqrt
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, EffectHistogram, MomentState, eye
from enterprise_math.brc_histogram import WeightHistogram, histogram_serial
from enterprise_math.brc_weighted import CWM_ZERO, CWM_ONE, cwm_edge, cwm_propagate, cwm_recoalesce


def moments(law, order=6):
    return [sum((p*x**k for x, p in law.items()), F()) for k in range(order+1)]


def cumulants(raw):
    out = [F()]
    for n in range(1, len(raw)):
        out.append(raw[n]-sum((comb(n-1, j-1)*out[j]*raw[n-j]
                              for j in range(1, n)), F()))
    return out


def packet(law, d):
    return EffectHistogram.from_terms(d, [(p, Affine(eye(d), x), 1)
                                        for x, p in law.items() if p])


def axis_law(d, s):
    return {tuple(sign*s if i == a else F() for i in range(d)): F(1, 2*d)
            for a in range(d) for sign in (-1, 1)}


def independent_step(dist, noise):
    out = {}
    for x, p in dist.items():
        for y, q in noise.items():
            z = tuple(a+b for a, b in zip(x, y))
            out[z] = out.get(z, F())+p*q
    return out


def radial_statistics(law, d):
    assert sum(law.values(), F()) == 1
    mean = tuple(sum((p*x[i] for x, p in law.items()), F()) for i in range(d))
    assert mean == (0,)*d
    cov = tuple(tuple(sum((p*x[i]*x[j] for x, p in law.items()), F())
                      for j in range(d)) for i in range(d))
    ell2 = sum((cov[i][i] for i in range(d)), F())
    fourth = sum((p*sum((v*v for v in x), F())**2 for x, p in law.items()), F())
    k = fourth-ell2**2-2*sum((cov[i][j]**2 for i in range(d) for j in range(d)), F())
    return cov, ell2, k


def power_fit(training, heldout, p):
    # Fit only one amplitude, no intercept or exponent adjustment on heldout.
    weights = [F(1, 1)/r**p for r, _ in training]
    amp = sum((w*y for w, (_, y) in zip(weights, training)), F())/sum((w*w for w in weights), F())
    se = sum(((amp/r**p-y)**2 for r, y in heldout), F())
    scale = sum((y*y for _, y in heldout), F())
    return dict(exponent=p, amplitude=amp, heldout_relative_squared_error=se/scale)


def spatial_scale_checks():
    rows, fits, checks, enumeration_checks = [], [], 0, 0
    for d in (1, 2, 3, 4):
        for s in (F(1, 2), F(1), F(2)):
            law = axis_law(d, s)
            h = packet(law, d)
            state = MomentState.from_point((0,)*d)
            marginal = {F(-s): F(1, 2*d), F(s): F(1, 2*d)}
            if d > 1:
                marginal[F()] = F(d-1, d)
            innovation_raw = moments(marginal)
            raw = [F(1)]+[F()]*6
            radial_fourth = F()
            series = []
            for n in range(1, 145):
                state = state.then(h)
                m = state.to_matrix()
                assert m[-1][-1] == 1
                assert all(m[i][-1] == 0 for i in range(d))
                assert all(m[i][j] == (F(n, d)*s*s if i == j else 0)
                           for i in range(d) for j in range(d))
                ell2 = sum((m[i][i] for i in range(d)), F())
                # Expand E||R+eta||^4 using independence and isotropic Q.
                radial_fourth += (2+F(4, d))*s*s*(n-1)*s*s+s**4
                k = radial_fourth-(1+F(2, d))*ell2**2
                assert k == -F(2*n, d)*s**4
                c = k/ell2**2
                assert c*ell2 == -F(2, d)*s*s
                raw = [sum((comb(k, j)*raw[j]*innovation_raw[k-j]
                            for j in range(k+1)), F()) for k in range(7)]
                kap = cumulants(raw)
                assert kap[4]/raw[2]**2 == F(d-3, n)
                assert kap[6]/raw[2]**3 == F(d*d-15*d+30, n*n)
                checks += 1
                kroot = isqrt(n)
                if kroot*kroot == n:
                    radius = s*kroot
                    series.append((radius, c))
                    rows.append(dict(family='iid_axis', dimension=d, step=str(s), n=n,
                        radius=radius, radius_squared=ell2, normalized_radial_fourth=c,
                        raw_radial_fourth=k, coordinate_normalized_fourth=kap[4]/raw[2]**2,
                        coordinate_normalized_sixth=kap[6]/raw[2]**3,
                        split='calibration' if kroot <= 4 else 'heldout'))
            fits.append(dict(dimension=d, step=s, candidates=[
                power_fit(series[:4], series[4:], p) for p in (0, 1, 2, 3, 4)]))
            assert fits[-1]['candidates'][2]['heldout_relative_squared_error'] == 0
            assert all(f['heldout_relative_squared_error'] > 0
                       for f in fits[-1]['candidates'] if f['exponent'] != 2)
            # Independent explicit branch convolution, not moment recurrence.
            dist = {(F(),)*d: F(1)}
            for n in range(1, 5):
                dist = independent_step(dist, law)
                cov, ell2, k = radial_statistics(dist, d)
                assert ell2 == n*s*s and k == -F(2*n, d)*s**4
                enumeration_checks += 1
    return rows, fits, checks, enumeration_checks


def branch_controls():
    d, s = 3, F(1)
    axial = axis_law(d, s)
    scalar = {F(-1): F(1, 6), F(): F(2, 3), F(1): F(1, 6)}
    cube = {}
    for x in product(scalar, repeat=3):
        w = F(1)
        for z in x:
            w *= scalar[z]
        cube[x] = w
    rare = {(F(),)*d: F(3, 4)}
    rare.update({x: p/4 for x, p in axis_law(d, 2*s).items()})
    laws = {'axis_6_branches': axial, 'product_27_branches': cube, 'rare_7_branches': rare}
    out, covs = {}, []
    for name, law in laws.items():
        cov, ell2, k = radial_statistics(law, d)
        covs.append(cov)
        m = MomentState.from_point((0,)*d).then(packet(law, d)).to_matrix()
        assert tuple(tuple(m[i][j] for j in range(d)) for i in range(d)) == cov
        out[name] = dict(branches=len(law), covariance=cov, ell_squared=ell2, radial_k4=k)
    assert covs[0] == covs[1] == covs[2]
    assert [out[x]['radial_k4'] for x in laws] == [F(-2, 3), F(), F(7, 3)]
    for axis in range(d):
        marginals = []
        for law in (axial, cube):
            marginal = {}
            for x, p in law.items():
                marginal[x[axis]] = marginal.get(x[axis], F())+p
            marginals.append(marginal)
        assert marginals[0] == marginals[1]
    cube_kappa = cumulants(moments(scalar))
    assert cube_kappa[4] == 0 and cube_kappa[6] == -F(2, 9)
    out['same_axis_marginals_axis_and_product'] = True
    out['product_coordinate_k6'] = cube_kappa[6]
    return out


def dependence_controls():
    rows = []
    for n in (1, 4, 16, 64, 144):
        # One hidden sign selected once: X_n=n*eta, not n independent choices.
        h = packet({(F(n),): F(1, 2), (F(-n),): F(1, 2)}, 1)
        m = MomentState.from_point((0,)).then(h).to_matrix()
        assert m[0][0] == n*n
        assert (F(n**4)-3*m[0][0]**2)/m[0][0]**2 == -2
        # Drift distance from the origin is an independently defined scale.
        drift_radius = F(n, 3)
        c = -F(2, n)
        assert c*drift_radius == -F(2, 3)
        rows.append(dict(n=n, persistent_radius=n, persistent_normalized_k4=-2,
                         drift_radius=drift_radius, iid_normalized_k4=c))
    a, q = F(3, 4), F(1, 16)
    finite_memory = []
    for n in (1, 4, 16, 64, 144):
        var = q*(1-a**(2*n))/(1-a*a)
        kap4 = -2*q*q*(1-a**(4*n))/(1-a**4)
        finite_memory.append(dict(n=n, ell_squared=var, normalized_k4=kap4/var**2))
    # The old A=I BRC packet has zero conditional expected drift everywhere;
    # there is no source-to-probe coupling in its transition law.
    symmetric = packet({(F(-1),): F(1, 2), (F(1),): F(1, 2)}, 1)
    drift_by_position = {}
    for r in (1, 2, 4, 8, 16, 32):
        out = symmetric.evaluate((F(r),))
        expected_displacement = sum((w.total_mass*(y[0]-r) for y, w in out.items()), F())
        assert expected_displacement == 0
        drift_by_position[str(r)] = expected_displacement
    return dict(persistent_and_drift=rows, finite_memory=finite_memory,
                mean_conditional_displacement=drift_by_position)


def observer_order_checks():
    # Non-symmetric innovation with rational standard deviation 2.
    # One and the same process gives several spatial exponents depending
    # on which normalized cumulant is observed.
    innovation = moments({F(-1): F(4, 5), F(4): F(1, 5)})
    kap0 = cumulants(innovation)
    assert kap0[2:5] == [4, 12, 4] and kap0[6] == -1820
    raw = [F(1)]+[F()]*6
    series = {3: [], 4: [], 6: []}
    for n in range(1, 145):
        raw = [sum((comb(k, j)*raw[j]*innovation[k-j] for j in range(k+1)), F())
               for k in range(7)]
        kap = cumulants(raw)
        assert all(kap[j] == n*kap0[j] for j in range(1, 7))
        root = isqrt(n)
        if root*root == n:
            ell = F(2*root)
            for p in series:
                gamma = kap[p]/ell**p
                assert gamma*ell**(p-2) == kap0[p]/kap0[2]
                series[p].append((ell, gamma))
    return dict(innovation_cumulants=kap0, fits={str(p):[
        power_fit(v[:4], v[4:], power) for power in (0, 1, 2, 3, 4)]
        for p,v in series.items()}, exact_exponents={'3':1, '4':2, '6':4})


def local_shell_transport():
    # Finite state-indexed local BRC: every step crosses to the next
    # L-infinity shell, sharing outgoing mass over its local outgoing edges.
    # Unlike the shell-average algebra, this explicitly retains endpoint state.
    rows = []
    for d in (2, 3):
        deltas = [v for v in product((-1, 0, 1), repeat=d) if any(v)]
        state = {(0,)*d: CWM_ONE}
        for r in range(1, 11):
            nxt = {}
            for x, current in state.items():
                neighbors = []
                for delta in deltas:
                    y = tuple(a+b for a, b in zip(x, delta))
                    if max(abs(z) for z in y) == r:
                        neighbors.append(y)
                assert neighbors
                edge = cwm_edge(F(1, len(neighbors)))
                assert edge.total*len(neighbors) == 1
                for y in neighbors:
                    branch = cwm_propagate(current, edge)
                    nxt[y] = cwm_recoalesce(nxt.get(y, CWM_ZERO), branch)
            state = nxt
            n = (2*r+1)**d-(2*r-1)**d
            assert len(state) == n
            mass = sum((v.total for v in state.values()), F())
            assert mass == 1
            corner = state[(r,)*d].total
            assert corner == F(1, (3**d-1)*(3**d-2**d)**(r-1))
            values = [v.total for v in state.values()]
            rows.append(dict(dimension=d, radius=r, endpoint_count=n, total_mass=mass,
                mean_arrival_mass=mass/n, axis_arrival_mass=state[(r,)+(0,)*(d-1)].total,
                corner_arrival_mass=corner, minimum=min(values), maximum=max(values),
                uniform_on_shell=min(values)==max(values),
                total_path_count=sum(v.count for v in state.values())))
        assert rows[-1]['uniform_on_shell'] is False
    return rows


def shell_checks():
    # Moore-neighbor Z^d comparison graph: graph distance is max |x_i|.
    # Counts are derived by exact subtraction; this is not native X6 geometry.
    explicit = 0
    for d in range(1, 5):
        for r in range(1, 4):
            count = sum(max(abs(z) for z in x) == r for x in product(range(-r, r+1), repeat=d))
            assert count == (2*r+1)**d-(2*r-1)**d
            explicit += 1
    rows, fits = [], []
    for d in range(1, 5):
        series = []
        for r in range(1, 65):
            n = (2*r+1)**d-(2*r-1)**d
            histogram = WeightHistogram.from_counts({F(1, n): n})
            assert histogram.total_mass == 1 and histogram.count == n
            mean = histogram.total_mass/n
            series.append((F(r), mean))
            correction_ratio = F(d*2**d*r**(d-1), n)
            leading = F(1, d*2**d*r**(d-1))
            rows.append(dict(dimension=d, radius=r, shell_count=n, mass=1,
                mean_shell_flux=mean, power_scaled_flux=mean*r**(d-1),
                ratio_to_leading_power=correction_ratio,
                leading_power_flux=leading, absolute_model_residual=mean-leading,
                relative_model_residual=(mean-leading)/leading,
                absorbed_mean_flux=F(3, 4)**r/n))
            if d == 3:
                assert n == 24*r*r+2
                assert correction_ratio == 1/(1+F(1, 12*r*r))
                assert (mean-leading)/leading == -F(1, 12*r*r+1)
                assert mean-leading == -F(1, 12*r*r*(24*r*r+2))
        fits.append(dict(dimension=d, candidates=[power_fit(series[7:16], series[16:], p)
                                                 for p in (0, 1, 2, 3, 4)]))
    # A ternary branching graph conserves total mass yet has exponential
    # layer growth, hence exponential mean flux per vertex, not a power law.
    step = WeightHistogram.from_counts({F(1, 3): 3})
    h = WeightHistogram.from_counts({F(1): 1})
    tree = []
    for r in range(1, 17):
        h = histogram_serial(h, step)
        assert h.count == 3**r and h.total_mass == 1
        tree.append(dict(radius=r, vertices=h.count, mean_flux=h.total_mass/h.count))
    # Uniform shell redistribution is extra. Same total mass could live on
    # one ray: shell average agrees, individual sites have flux 1 or 0.
    return rows, dict(shell_enumerations=explicit, power_fits=fits, tree=tree,
        anisotropy_counterexample={'total_mass': 1, 'lit_ray_flux': 1, 'other_sites_flux': 0,
            'shell_mean_in_3d': '1/(24*r*r+2)', 'pointwise_inverse_square': False})


def rational_json(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k:rational_json(v) for k,v in x.items()}
    if isinstance(x, (list, tuple)):
        return [rational_json(v) for v in x]
    return x


def write_csv(path, rows):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def run():
    rows, fits, checks, explicit = spatial_scale_checks()
    shells, shell_summary = shell_checks()
    summary = dict(experiment='BRC_RESIDUAL_SPATIAL_DECAY_20261002_FCA717',
        evidence='EXACT_CONDITIONAL_TOY_MODELS_NOT_GRAVITY_OR_NATIVE_PROMOTION',
        production_moment_checks=checks, explicit_branch_checks=explicit,
        iid_power_fits=fits, branch_controls=branch_controls(),
        dependence_controls=dependence_controls(), observer_order_checks=observer_order_checks(),
        shell_checks=shell_summary, local_shell_transport=local_shell_transport(),
        reuse_resolution='COMPOSE_APPLIED: existing BRC affine transport, weight histogram, and endpoint-indexed CWM',
        source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in [Path(__file__), ROOT/'src/enterprise_math/brc_transport.py',
                      ROOT/'src/enterprise_math/brc_histogram.py', ROOT/'src/enterprise_math/brc_weighted.py']})
    write_csv(HERE/'spatial_residuals.csv', rows)
    write_csv(HERE/'shell_flux.csv', shells)
    write_csv(HERE/'local_shell_transport.csv', summary['local_shell_transport'])
    (HERE/'results.json').write_text(json.dumps(rational_json(summary), ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'production_moment_checks':checks, 'explicit_branch_checks':explicit,
                      'shell_enumerations':shell_summary['shell_enumerations'],
                      'local_transport_layers':len(summary['local_shell_transport']), 'status':'PASS'}))


if __name__ == '__main__':
    run()
