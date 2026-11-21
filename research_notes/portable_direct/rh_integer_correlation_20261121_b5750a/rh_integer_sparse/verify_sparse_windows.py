#!/usr/bin/env python3
"""New sparse-window identities and errors, independent of the old test suites.

All actual-road terms n=2,...,floor(Z) and every thickness are evaluated.
The 80-digit numerical checks are NOT interval certificates. A separate
Fraction check certifies the finite triangle-kernel and two-port identities.
"""
from bisect import bisect_right
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 80
TOL = mp.mpf('1e-60')


def J(s, k, x):
    z = mp.log(x)
    if s == 0:
        return z**(k+1)/(k+1)
    if k == 0:
        return x**s/s
    if k == 1:
        return x**s*(z/s-1/s**2)
    return x**s*(z*z/s-2*z/s**2+2/s**3)


def full_primitive(d, b, theta, y):
    p, q, r = 2-2*theta, 1-2*theta, -2*theta
    return (d*d*J(p, 0, y)-2*d*J(p, 1, y)+J(p, 2, y)
            -2*b*d*J(q, 0, y)+2*b*J(q, 1, y)+b*b*J(r, 0, y))


def positive_energy(d, b, theta, l, r):
    if b > 0:
        if b >= mp.exp(d-1):
            return mp.mpf(0)
        z = -b*mp.exp(-d)
        lo, hi = -b/mp.lambertw(z, -1), -b/mp.lambertw(z, 0)
    elif b == 0:
        lo, hi = mp.mpf(0), mp.exp(d)
    else:
        lo, hi = mp.mpf(0), -b/mp.lambertw(-b*mp.exp(-d), 0)
    lo, hi = max(l, mp.re(lo)), min(r, mp.re(hi))
    if lo >= hi:
        return mp.mpf(0)
    return full_primitive(d, b, theta, hi)-full_primitive(d, b, theta, lo)


def linear_primitive(alpha, beta, theta, x):
    return (alpha*alpha*J(2-2*theta, 0, x)
            + 2*alpha*beta*J(1-2*theta, 0, x)
            + beta*beta*J(-2*theta, 0, x))


def linear_positive_energy(alpha, beta, theta, u, v):
    if alpha == 0:
        return (linear_primitive(alpha, beta, theta, v)
                - linear_primitive(alpha, beta, theta, u)) if beta > 0 else mp.mpf(0)
    root = -beta/alpha
    l, r = (max(u, root), v) if alpha > 0 else (u, min(v, root))
    if l >= r:
        return mp.mpf(0)
    return linear_primitive(alpha, beta, theta, r)-linear_primitive(alpha, beta, theta, l)


def green(y, n, u, v):
    return (min(y, n)-u)*(v-max(y, n))/(v-u)


def entropy_arc(y, u, v):
    return ((v-y)*u*mp.log(u)+(y-u)*v*mp.log(v))/(v-u)-y*mp.log(y)


def factor_table(B):
    fs = [[] for _ in range(B+1)]
    for p in range(2, B+1):
        if not fs[p]:
            for n in range(p, B+1, p):
                fs[n].append(p)
    return fs


def chebyshev_nodes(m, amplitude=mp.mpf(3), maximum=mp.mpf('.5')):
    d = m-1
    s = mp.acosh(amplitude)
    t = s/d
    ratio = mp.tanh(t/2)**2
    C, D = maximum*(1+ratio)/2, maximum*(1-ratio)/2
    nodes, weights = [], []
    for j in range(m):
        cj = mp.cos(j*mp.pi/d)
        nodes.append(C-D*cj)
        delta = mp.mpf('.5') if j in (0, d) else mp.mpf(1)
        weights.append((-1)**j*delta*mp.sinh(t)*mp.sinh(s)/(d*(mp.cosh(t)-cj)))
    assert abs(mp.fsum(weights)-1) < TOL
    assert abs(mp.fsum(abs(w) for w in weights)-amplitude) < TOL
    return nodes, weights


def quartic_critical_probe(Y, Z, P, F, AA, BB, D):
    """Reuse the supplied all-integer road; only change mesh and energy weight."""
    theta, q = mp.mpf('.5'), 4
    A, B = int(mp.ceil(Y)), int(mp.floor(Z))
    nodes = sorted(set([Y, Z, mp.mpf(A), mp.mpf(B)]+
                       [mp.mpf(k**q) for k in range(1, int(mp.root(Z, q))+2)
                        if Y < k**q < Z]))
    intervals = []
    for u, v in zip(nodes, nodes[1:]):
        alpha = (F(v)-F(u))/(v-u)
        intervals.append((u, v, alpha, F(u)-alpha*u))
    kq = int(mp.floor(mp.root(Y, q)))
    bq = mp.mpf((kq+1)**q-kq**q)/kq**(q-1)
    cq, dq = bq*bq/8, q*mp.log(1+mp.mpf(1)/kq)
    aq = 1+P*dq
    delta = 2*theta+mp.mpf(4)/q-2
    assert delta == 0
    eps_sq = cq*cq*((aq+P*mp.log(Z))**3-(aq+P*mp.log(Y))**3)/(3*P)
    eps_d_sq = cq*cq*((aq+P*mp.log(A))**2/A+
                      ((aq+P*mp.log(B))**3-(aq+P*mp.log(A))**3)/(3*P))
    E, err_sq = mp.mpf(0), mp.mpf(0)
    for n in range(int(mp.floor(Y)), B+1):
        l, r = max(Y, mp.mpf(n)), min(Z, mp.mpf(n+1))
        if l >= r:
            continue
        d, b = AA[n]+1+mp.euler, BB[n]
        E += positive_energy(d, b, theta, l, r)
        i = min(bisect_right(nodes, (l+r)/2)-1, len(intervals)-1)
        _, _, alpha, beta = intervals[i]
        err_sq += (full_primitive(d-alpha, b+beta, theta, r)
                   -full_primitive(d-alpha, b+beta, theta, l))
    Q = mp.fsum(linear_positive_energy(alpha, beta, theta, u, v)
               for u, v, alpha, beta in intervals)
    kernel_error, envelope_ratio, eps_local_sq = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    for u, v, alpha, beta in intervals:
        ints = list(range(int(mp.floor(u))+1, int(mp.ceil(v))))
        coefficient = 1+P*mp.log(v) if ints else mp.mpf(1)
        eps_local_sq += coefficient**2*(v-u)**5/(120*u**4)
        for part in (mp.mpf('.25'), mp.mpf('.5'), mp.mpf('.75')):
            y = u+(v-u)*part
            correction = mp.fsum(D[n]/n*green(y, n, u, v) for n in ints)
            rec = alpha*y+beta+entropy_arc(y, u, v)-correction
            kernel_error = max(kernel_error, abs(rec-F(y)))
            bound = cq*y**(1-mp.mpf(2)/q)*(aq+P*mp.log(y))
            envelope_ratio = max(envelope_ratio, abs(F(y)-(alpha*y+beta))/bound)
    assert kernel_error < TOL and envelope_ratio <= 1+TOL
    assert -TOL <= err_sq <= min(eps_sq, eps_local_sq)+TOL
    assert abs(mp.sqrt(E)-mp.sqrt(Q)) <= mp.sqrt(max(err_sq, 0))+TOL
    exact_s = mp.fsum(max(F(mp.mpf(n)), 0)**2/mp.mpf(n)**2 for n in range(A, B+1))
    compressed_s, err_d_sq = mp.mpf(0), mp.mpf(0)
    inode = sorted(set([A, B]+[int(x) for x in nodes if A <= x <= B]))
    cells = []
    for i, (u, v) in enumerate(zip(inode, inode[1:])):
        alpha = (F(mp.mpf(v))-F(mp.mpf(u)))/(v-u)
        beta = F(mp.mpf(u))-alpha*u
        end = v if i == len(inode)-2 else v-1
        selected = [n for n in range(u, end+1) if alpha*n+beta > 0]
        if selected:
            H = [mp.fsum(mp.mpf(n)**(-s) for n in selected) for s in (0, 1, 2)]
            mass = alpha*alpha*H[0]+2*alpha*beta*H[1]+beta*beta*H[2]
        else:
            mass = mp.mpf(0)
        direct = mp.fsum(max(alpha*n+beta, 0)**2/mp.mpf(n)**2 for n in range(u, end+1))
        assert abs(mass-direct) < TOL
        compressed_s += mass
        err_d_sq += mp.fsum((F(mp.mpf(n))-(alpha*n+beta))**2/mp.mpf(n)**2
                            for n in range(u, end+1))
        cells.append({'left':u, 'right':v, 'positive_count':len(selected), 'contribution':mass})
    assert err_d_sq <= eps_d_sq+TOL
    assert abs(mp.sqrt(exact_s)-mp.sqrt(compressed_s)) <= mp.sqrt(err_d_sq)+TOL
    return {'evidence':'80-digit non-interval check; reuses the same D and per-thickness ports',
            'theta':theta, 'mesh_power':q, 'delta':delta, 'readout_count':len(nodes),
            'continuous_energy':E, 'sparse_linear_energy':Q,
            'energy_norm_gap':abs(mp.sqrt(E)-mp.sqrt(Q)),
            'actual_interpolation_error_norm':mp.sqrt(max(err_sq, 0)),
            'critical_uniform_error_bound':mp.sqrt(eps_sq),
            'finite_kernel_error_bound':mp.sqrt(eps_local_sq),
            'integer_energy':exact_s, 'sparse_power_sum_energy':compressed_s,
            'integer_energy_norm_gap':abs(mp.sqrt(exact_s)-mp.sqrt(compressed_s)),
            'actual_integer_interpolation_error_norm':mp.sqrt(err_d_sq),
            'critical_integer_error_bound':mp.sqrt(eps_d_sq),
            'maximum_green_identity_error':kernel_error,
            'maximum_point_error_to_power_envelope_ratio':envelope_ratio,
            'sparse_readouts':[{'x':x, 'F':F(x)} for x in nodes],
            'power_sum_cells':cells, 'checks':'all passed'}


def build_case(name, Y_string, theta_string, road=False):
    Y, theta = mp.mpf(Y_string), mp.mpf(theta_string)
    Z, p = Y**mp.mpf('1.5'), 2*theta+1
    A, B = int(mp.ceil(Y)), int(mp.floor(Z))
    factors = factor_table(B)
    Lambda = [mp.mpf(0)]*(B+1)
    for n in range(2, B+1):
        if len(factors[n]) == 1:
            Lambda[n] = mp.log(factors[n][0])
    D = list(Lambda)
    nodes, weights, channel_A, channel_B = [], [], [], []
    eta = mp.mpf(0)
    max_coefficient_error = mp.mpf(0)
    if road:
        nodes, weights = chebyshev_nodes(8)
        m = len(nodes)
        channel_A = [[mp.mpf(0)]*(B+1) for _ in nodes]
        channel_B = [[mp.mpf(0)]*(B+1) for _ in nodes]
        terms = {prime: [-mp.expm1(-a*mp.log(prime)) for a in nodes]
                 for prime in range(2, B+1) if factors[prime] == [prime]}
        for n in range(2, B+1):
            vals = [mp.fprod(terms[q][j] for q in factors[n])/a
                    for j, a in enumerate(nodes)]
            D[n] = mp.fsum(w*x for w, x in zip(weights, vals))
            for j, val in enumerate(vals):
                channel_A[j][n] = channel_A[j][n-1]+val/n
                channel_B[j][n] = channel_B[j][n-1]+val
            max_coefficient_error = max(max_coefficient_error, abs(D[n]-Lambda[n]))
        eta = mp.fprod(nodes)*mp.log(Z)**(m+1)/mp.factorial(m+1)
        assert max_coefficient_error <= eta+TOL
        assert eta*Z**(1-theta)*mp.log(Z) < mp.mpf('.5')
    K, P, M = (mp.mpf(3), mp.mpf(2), mp.mpf(1)) if road else (mp.mpf(1), mp.mpf(1), mp.mpf(0))
    for n in range(2, B+1):
        assert -M*mp.log(n)-TOL <= D[n] <= P*mp.log(n)+TOL
    AA, BB = [mp.mpf(0)]*(B+1), [mp.mpf(0)]*(B+1)
    for n in range(2, B+1):
        AA[n], BB[n] = AA[n-1]+D[n]/n, BB[n-1]+D[n]

    def F(y):
        k = int(mp.floor(y))
        return y*(AA[k]+1+mp.euler-mp.log(y))-BB[k]

    square_nodes = sorted(set([Y, Z, mp.mpf(A), mp.mpf(B)] +
                             [mp.mpf(k*k) for k in range(isqrt(A), isqrt(B)+2)
                              if Y < k*k < Z]))
    event_nodes = sorted(set(square_nodes+[mp.mpf(n) for n in range(A, B+1)
                                          if Y < n < Z and Lambda[n] != 0]))
    sparse_values = {x: F(x) for x in square_nodes}
    intervals = []
    for u, v in zip(square_nodes, square_nodes[1:]):
        alpha = (F(v)-F(u))/(v-u)
        intervals.append((u, v, alpha, F(u)-alpha*u))
    exact_energy = mp.mpf(0)
    full_error_sq = mp.mpf(0)
    for n in range(int(mp.floor(Y)), B+1):
        l, r = max(Y, mp.mpf(n)), min(Z, mp.mpf(n+1))
        if l >= r:
            continue
        d, b = AA[n]+1+mp.euler, BB[n]
        exact_energy += positive_energy(d, b, theta, l, r)
        i = min(bisect_right(square_nodes, (l+r)/2)-1, len(intervals)-1)
        _, _, alpha, beta = intervals[i]
        full_error_sq += (full_primitive(d-alpha, b+beta, theta, r)
                          - full_primitive(d-alpha, b+beta, theta, l))
    sparse_energy = mp.fsum(linear_positive_energy(alpha, beta, theta, u, v)
                            for u, v, alpha, beta in intervals)
    point_identity_error = mp.mpf(0)
    max_point_error_over_bound = mp.mpf(0)
    eps_finite_sq = mp.mpf(0)
    for u, v, alpha, beta in intervals:
        ints = list(range(int(mp.floor(u))+1, int(mp.ceil(v))))
        coefficient = 1+P*mp.log(v) if ints else mp.mpf(1)
        eps_finite_sq += coefficient**2*(v-u)**5/(120*u**(p+2))
        for fraction in (mp.mpf('.25'), mp.mpf('.5'), mp.mpf('.75')):
            y = u+(v-u)*fraction
            correction = mp.fsum(D[n]/n*green(y, n, u, v) for n in ints)
            rec = alpha*y+beta+entropy_arc(y, u, v)-correction
            point_identity_error = max(point_identity_error, abs(rec-F(y)))
            bound = coefficient*(y-u)*(v-y)/(2*u)
            max_point_error_over_bound = max(max_point_error_over_bound,
                                            abs(F(y)-(alpha*y+beta))/bound)
    assert point_identity_error < TOL
    assert max_point_error_over_bound <= 1+TOL
    k0 = int(mp.floor(mp.sqrt(Y)))
    c0, d0 = (2+mp.mpf(1)/k0)**2/8, 2*mp.log(1+mp.mpf(1)/k0)
    a0, r0 = 1+P*d0, 2*theta

    def tail_bracket(x):
        g = a0+P*mp.log(x)
        return g*g+2*P*g/r0+2*P*P/r0**2

    eps_global_sq = c0*c0*Y**(-r0)/r0*tail_bracket(Y)
    assert -TOL <= full_error_sq <= min(eps_global_sq, eps_finite_sq)+TOL
    assert abs(mp.sqrt(exact_energy)-mp.sqrt(sparse_energy)) <= mp.sqrt(max(full_error_sq, 0))+TOL

    # Reconstruct the integer positive-square sum via three deterministic power sums.
    integer_nodes = sorted(set([A, B]+[int(x) for x in square_nodes if A <= x <= B]))
    exact_discrete = mp.fsum(max(F(mp.mpf(n)), 0)**2/mp.mpf(n)**p for n in range(A, B+1))
    compressed_discrete, discrete_error_sq = mp.mpf(0), mp.mpf(0)
    power_sum_cells = []
    for index, (ui, vi) in enumerate(zip(integer_nodes, integer_nodes[1:])):
        u, v = mp.mpf(ui), mp.mpf(vi)
        alpha, beta = (F(v)-F(u))/(v-u), mp.mpf(0)
        beta = F(u)-alpha*u
        end = vi if index == len(integer_nodes)-2 else vi-1
        positive = [n for n in range(ui, end+1) if alpha*n+beta > 0]
        direct_cell = mp.fsum(max(alpha*n+beta, 0)**2/mp.mpf(n)**p for n in range(ui, end+1))
        if positive:
            lo, hi = positive[0], positive[-1]
            assert positive == list(range(lo, hi+1))
            H = [mp.fsum(mp.mpf(n)**(-s) for n in range(lo, hi+1)) for s in (p-2, p-1, p)]
            cell = alpha*alpha*H[0]+2*alpha*beta*H[1]+beta*beta*H[2]
        else:
            lo, hi, cell = None, None, mp.mpf(0)
        assert abs(cell-direct_cell) < TOL
        compressed_discrete += cell
        discrete_error_sq += mp.fsum((F(mp.mpf(n))-(alpha*n+beta))**2/mp.mpf(n)**p
                                     for n in range(ui, end+1))
        power_sum_cells.append({'left':ui, 'right':vi, 'positive_first':lo, 'positive_last':hi,
                                'contribution':cell})
    eps_discrete_sq = c0*c0*mp.mpf(A)**(-r0)*((a0+P*mp.log(A))**2/A+tail_bracket(mp.mpf(A))/r0)
    assert discrete_error_sq <= eps_discrete_sq+TOL
    assert abs(mp.sqrt(exact_discrete)-mp.sqrt(compressed_discrete)) <= mp.sqrt(discrete_error_sq)+TOL

    # Event+square interpolation with the complete entropy arc, and its eta-only repair.
    event_energy, event_error_sq, event_gamma_sq = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    event_identity_error = mp.mpf(0)
    for u, v in zip(event_nodes, event_nodes[1:]):
        alpha = (F(v)-F(u))/(v-u)
        beta = F(u)-alpha*u
        dc = alpha+(v*mp.log(v)-u*mp.log(u))/(v-u)
        bc = -beta-u*v*(mp.log(u)-mp.log(v))/(v-u)
        event_energy += positive_energy(dc, bc, theta, u, v)
        ints = list(range(int(mp.floor(u))+1, int(mp.ceil(v))))
        assert all(Lambda[n] == 0 for n in ints)
        if ints:
            event_gamma_sq += (v-u)**5/(120*u**(p+2))
        for n in range(int(mp.floor(u)), int(mp.ceil(v))):
            l, r = max(u, mp.mpf(n)), min(v, mp.mpf(n+1))
            if l >= r:
                continue
            ac, bconst = AA[n]+1+mp.euler-dc, bc-BB[n]
            event_error_sq += (linear_primitive(ac, bconst, theta, r)
                               -linear_primitive(ac, bconst, theta, l))
        y = (u+v)/2
        reconstructed = y*(dc-mp.log(y))-bc-mp.fsum(D[n]/n*green(y, n, u, v) for n in ints)
        event_identity_error = max(event_identity_error, abs(reconstructed-F(y)))
    assert event_identity_error < TOL
    assert event_error_sq >= -TOL
    assert event_error_sq <= eta*eta*event_gamma_sq+TOL
    assert abs(mp.sqrt(exact_energy)-mp.sqrt(event_energy)) <= eta*mp.sqrt(event_gamma_sq)+TOL
    ports = []
    if road:
        for j, a in enumerate(nodes):
            ports.append({'thickness':a, 'weight':weights[j],
                          'A_left_integer':channel_A[j][A], 'B_left_integer':channel_B[j][A],
                          'A_right_integer':channel_A[j][B], 'B_right_integer':channel_B[j][B]})
    quartic_result = quartic_critical_probe(Y, Z, P, F, AA, BB, D) if road else None
    return {'name':name, 'evidence':'80-digit non-interval numerical crosscheck',
            'Y':Y, 'Z':Z, 'theta':theta, 'lambda':mp.mpf('1.5'),
            'integer_observations':B-A+1, 'square_mesh_observations':len(square_nodes),
            'event_and_square_observations':len(event_nodes), 'weight_l1':K,
            'coefficient_error_bound':eta, 'max_coefficient_error':max_coefficient_error,
            'finite_window_bridge_bound':eta*Z**(1-theta)*mp.log(Z),
            'continuous_energy':exact_energy, 'sparse_linear_energy':sparse_energy,
            'norm_energy_gap':abs(mp.sqrt(exact_energy)-mp.sqrt(sparse_energy)),
            'actual_interpolation_error_norm':mp.sqrt(max(full_error_sq, 0)),
            'finite_mesh_error_bound':mp.sqrt(eps_finite_sq),
            'uniform_error_bound':mp.sqrt(eps_global_sq),
            'integer_energy':exact_discrete, 'sparse_power_sum_energy':compressed_discrete,
            'integer_norm_gap':abs(mp.sqrt(exact_discrete)-mp.sqrt(compressed_discrete)),
            'actual_integer_interpolation_error_norm':mp.sqrt(max(discrete_error_sq, 0)),
            'uniform_integer_error_bound':mp.sqrt(eps_discrete_sq),
            'event_plus_arc_energy':event_energy,
            'event_actual_error_norm':mp.sqrt(max(event_error_sq, 0)),
            'event_eta_error_bound':eta*mp.sqrt(event_gamma_sq),
            'maximum_green_identity_error':max(point_identity_error, event_identity_error),
            'maximum_point_error_to_envelope_ratio':max_point_error_over_bound,
            'sparse_readouts':[{'x':x, 'F':sparse_values[x]} for x in square_nodes],
            'power_sum_cells':power_sum_cells, 'per_thickness_boundary_ports':ports,
            'quartic_critical_reuse':quartic_result,
            'checks':'all passed'}


def fraction_checks():
    u, v, n = 9, 16, 12
    t = Fraction(1, 100)
    perturbation = {n-1:t*(n-1), n:-2*t*n, n+1:t*(n+1)}
    assert sum(perturbation.values()) == 0
    assert sum(d/k for k, d in perturbation.items()) == 0
    outputs = []
    for y in (Fraction(9), Fraction(43, 4), Fraction(23, 2), Fraction(12), Fraction(25, 2), Fraction(16)):
        frac = y-y.numerator//y.denominator
        kernel_total = sum(green(y, k, u, v) for k in range(u+1, v))
        rhs = ((y-u)*(v-y)-frac*(1-frac))/2
        assert kernel_total == rhs
        response = sum(d*max(y/k-1, 0) for k, d in perturbation.items())
        triangular = t*(max(y-(n-1), 0)-2*max(y-n, 0)+max(y-(n+1), 0))
        assert response == triangular
        assert response == -sum(d/k*green(y, k, u, v) for k, d in perturbation.items())
        outputs.append({'y':str(y), 'kernel_sum':str(kernel_total), 'triangle':str(response)})
    clipped = []
    for alpha, beta in ((Fraction(-2), Fraction(19)), (Fraction(3), Fraction(-40)), (Fraction(0), Fraction(-1))):
        selected = [k for k in range(9, 17) if alpha*k+beta > 0]
        H0 = Fraction(len(selected))
        H1 = sum((Fraction(1, k) for k in selected), Fraction(0))
        H2 = sum((Fraction(1, k*k) for k in selected), Fraction(0))
        expanded = alpha*alpha*H0+2*alpha*beta*H1+beta*beta*H2
        direct = sum((max(alpha*k+beta, 0)**2/Fraction(k*k) for k in range(9, 17)), Fraction(0))
        assert expanded == direct
        clipped.append({'alpha':str(alpha), 'beta':str(beta), 'positive_integers':selected,
                        'weighted_positive_square_sum':str(direct)})
    return {'evidence':'exact Fraction arithmetic', 'source_perturbation':{str(k):str(d) for k, d in perturbation.items()},
            'A_port_delta':'0', 'B_port_delta':'0', 'point_checks':outputs,
            'sign_clipped_three_power_sum_checks':clipped, 'checks':'all passed'}


def serial(value):
    if isinstance(value, mp.mpf):
        return mp.nstr(value, 55)
    if isinstance(value, dict):
        return {k:serial(v) for k, v in value.items()}
    if isinstance(value, list):
        return [serial(v) for v in value]
    return value


if __name__ == '__main__':
    output = {'precision_digits':mp.mp.dps, 'scope':'New sparse-readout tests only; no previous suites rerun.',
              'exact_rational_kernel_certificate':fraction_checks(),
              'cases':[build_case('fixed_first_jet', '36.5', '.6'),
                       build_case('actual_chebyshev_full_road', '64.5', '.65', road=True)]}
    dest = Path(__file__).with_name('sparse_window_results.json')
    dest.write_text(json.dumps(serial(output), ensure_ascii=False, indent=2)+'\n')
    for result in output['cases']:
        print(json.dumps(serial({k:result[k] for k in ('name', 'Y', 'Z', 'integer_observations',
              'square_mesh_observations', 'continuous_energy', 'sparse_linear_energy',
              'norm_energy_gap', 'finite_mesh_error_bound', 'integer_energy', 'sparse_power_sum_energy',
              'event_actual_error_norm', 'event_eta_error_bound', 'checks')}), ensure_ascii=False))
        if result['quartic_critical_reuse']:
            q = result['quartic_critical_reuse']
            print(json.dumps(serial({k:q[k] for k in ('mesh_power', 'theta', 'readout_count',
                  'continuous_energy', 'sparse_linear_energy', 'actual_interpolation_error_norm',
                  'critical_uniform_error_bound', 'integer_energy', 'sparse_power_sum_energy', 'checks')}), ensure_ascii=False))
    print('saved '+str(dest))
