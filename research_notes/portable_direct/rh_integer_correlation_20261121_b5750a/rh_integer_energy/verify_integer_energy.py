#!/usr/bin/env python3
"""New signed-work identities on previously evaluated complete-road windows.

80-digit floating-point arithmetic. This is not an interval certificate.
Prior positive arcs/energy/first moment are read, not recomputed as an old test.
All integer roads through the horizon are reconstructed to evaluate NEW source,
boundary, discrete-gradient and continuous-gradient decompositions.
"""
from pathlib import Path
from math import comb
import hashlib
import json
import mpmath as mp

mp.mp.dps = 80
ROOT = Path(__file__).resolve().parent


def fmt(x):
    return mp.nstr(x, 35)


def prime_data(nmax):
    omega = [0]*(nmax+1)
    primes = []
    for p in range(2, nmax+1):
        if omega[p] == 0:
            primes.append(p)
            for n in range(p, nmax+1, p):
                omega[n] += 1
    return primes, omega


def road_values(a, nmax, primes):
    values = [mp.mpf(0)] + [mp.mpf(1)]*nmax
    for p in primes:
        factor = -mp.expm1(-a*mp.log(p))
        for n in range(p, nmax+1, p):
            values[n] *= factor
    return values


def family(row):
    Y, theta, lam = map(mp.mpf, (row['Y'], row['theta'], row['lambda']))
    if row['label'] == 'chebyshev':
        m = int(mp.ceil(lam*mp.log(Y)))
        A = mp.mpf('0.5')
        b = A*mp.tanh(mp.acosh(3)/(2*(m-1)))**2
        nodes = [(A+b)/2-(A-b)/2*mp.cos(mp.pi*j/(m-1)) for j in range(m)]
        weights = [mp.fprod(-nodes[k]/(nodes[j]-nodes[k])
                            for k in range(m) if k != j) for j in range(m)]
    else:
        m = int(row['label'][1:])
        h = (mp.mpf(m+1)/2)**(mp.mpf(1)/m)*Y**(-lam*(1-theta)/m)/(lam*mp.log(Y))**(1+mp.mpf(2)/m)
        nodes = [j*h for j in range(1, m+1)]
        weights = [mp.mpf((-1)**(j+1)*comb(m,j)) for j in range(1, m+1)]
    return Y, theta, lam, nodes, weights


def moment_vector(r, y):
    logy = mp.log(y)
    values = []
    for nu, k in ((r,0),(r,1),(r,2),(r-1,0),(r-1,1),(r-2,0)):
        if nu == 0:
            val = logy**(k+1)/(k+1)
        elif k == 0:
            val = y**nu/nu
        elif k == 1:
            val = y**nu*(logy/nu-1/nu**2)
        else:
            val = y**nu*(logy**2/nu-2*logy/nu**2+2/nu**3)
        values.append(val)
    return tuple(values)


def gradient_integral(A, P, theta, delta):
    k = 1-theta
    C = k*A-1
    return (C*C*delta[0]-2*C*k*delta[1]+k*k*delta[2]
            +2*theta*P*(C*delta[3]-k*delta[4])+theta*theta*P*P*delta[5])


def compute(row, primes, omega, common):
    Y, theta, lam, nodes, weights = family(row)
    Z = Y**lam
    L, R = int(mp.ceil(Y)), int(mp.floor(Z))
    nmax = R
    D = [mp.mpf(0)]*(nmax+1)
    for a, nu in zip(nodes, weights):
        roads = road_values(a, nmax, primes)
        for n in range(2, nmax+1):
            D[n] += nu*roads[n]/a
    prefixes = [mp.mpf(0)]*(nmax+1)
    reciprocals = [mp.mpf(0)]*(nmax+1)
    q = [mp.mpf(0)]*(nmax+1)
    for n in range(1, nmax+1):
        prefixes[n] = prefixes[n-1]+D[n]
        reciprocals[n] = reciprocals[n-1]+D[n]/n
        q[n] = n*(1+mp.euler+reciprocals[n]-mp.log(n))-prefixes[n]
    u = [max(t,0) for t in q]
    v = [max(-t,0) for t in q]
    w, r, kappa = common['w'], common['r'], common['kappa']
    edge = common['edge']
    ctheta = theta*(1-theta)
    S = mp.mpf(0)
    remainder = mp.mpf(0)
    Hbg = mp.mpf(0)
    Hroad = mp.mpf(0)
    Hpos = mp.mpf(0)
    Hneg = mp.mpf(0)
    coarse_norm2 = mp.mpf(0)
    max_recurrence_error = mp.mpf(0)
    min_gamma = mp.inf
    max_gamma = -mp.inf
    strata = {k: {'nodes':0, 'positive_nodes':0, 'road_work':mp.mpf(0),
                   'background_work':mp.mpf(0), 'signed_work':mp.mpf(0)}
              for k in range(1,max(omega)+1)}
    for n in range(L+1, R):
        sweight = w[n]/(n*n)
        S += u[n]*u[n]*sweight
        potential = 2*w[n]-(edge[n-1]*r[n-1]+edge[n]*r[n+1])/r[n]
        gamma = potential/sweight
        min_gamma, max_gamma = min(min_gamma,gamma), max(max_gamma,gamma)
        assert ctheta <= gamma <= ctheta*(1+1/(2*(mp.mpf(n)**2-1)))
        remainder += (potential-ctheta*sweight)*u[n]*u[n]
        pair_weight = w[n]*u[n]/n
        hb, hd = kappa[n]*pair_weight, D[n]*pair_weight
        Hbg += hb
        Hroad += hd
        f = kappa[n]-D[n]
        Hpos += max(f,0)*pair_weight
        Hneg += max(-f,0)*pair_weight
        coarse_norm2 += max(f,0)**2*w[n]
        item = strata[omega[n]]
        item['nodes'] += 1
        item['positive_nodes'] += int(u[n] > 0)
        item['road_work'] += hd
        item['background_work'] += hb
        item['signed_work'] += hb-hd
        err = abs((q[n+1]-2*q[n]+q[n-1])-(D[n]-kappa[n])/n)
        max_recurrence_error = max(max_recurrence_error,err)
    gradient = mp.fsum(edge[n]*r[n]*r[n+1]*(u[n+1]/r[n+1]-u[n]/r[n])**2 for n in range(L,R))
    contact = mp.fsum(w[n+1]*u[n+1]*v[n]+w[n]*u[n]*v[n+1] for n in range(L,R))
    left_flux = edge[L]*r[L+1]/r[L]*u[L]**2-w[L]*u[L]*q[L+1]
    right_flux = edge[R-1]*r[R-1]/r[R]*u[R]**2-w[R]*u[R]*q[R-1]
    boundary = left_flux+right_flux
    H = Hbg-Hroad
    lhs = ctheta*S+gradient+contact+remainder
    rhs = H+boundary
    error = abs(lhs-rhs)
    assert max_recurrence_error < mp.mpf('1e-65')
    assert error < mp.mpf('1e-60')
    assert rhs >= 0
    coarse_root = (mp.sqrt(coarse_norm2)+mp.sqrt(coarse_norm2+4*ctheta*max(boundary,0)))/(2*ctheta)

    # Continuous energy and positive first moment come from the frozen old run.
    Econt = mp.mpf(row['positive_part_energy'])
    Mcont = -mp.mpf(row['positive_energy_derivative_at_actual_tau'])/2
    atomic_work = mp.fsum(D[n]*u[n]*mp.mpf(n)**(-2*theta)
                         for n in range(int(mp.floor(Y))+1,int(mp.ceil(Z))))
    def q_and_derivative(y, side):
        N = int(mp.floor(y))
        if side == 'left' and y == N:
            N -= 1
        G = y*(1+mp.euler+reciprocals[N]-mp.log(y))-prefixes[N]
        derivative = mp.euler+reciprocals[N]-mp.log(y)
        return G, derivative
    def continuous_flux(y, side):
        G, derivative = q_and_derivative(y, side)
        U = max(G,0)
        return y**(1-2*theta)*U*derivative-mp.mpf('0.5')*y**(-2*theta)*U*U
    bleft = continuous_flux(Y,'right')
    bright = continuous_flux(Z,'left')
    bcont = bright-bleft
    partial = {d['N']:[tuple(map(mp.mpf,arc)) for arc in d['positive_arcs']]
               for d in row['sign_boundary_records']}
    gradcont = mp.mpf(0)
    positive_cells = 0
    moments = common['moments']
    for N in range(int(mp.floor(Y)),int(mp.ceil(Z))):
        left, right = max(Y,mp.mpf(N)),min(Z,mp.mpf(N+1))
        AA, PP = 1+mp.euler+reciprocals[N],prefixes[N]
        if N in partial:
            arcs = partial[N]
        elif AA-mp.log((left+right)/2)-PP/((left+right)/2) > 0:
            arcs = [(left,right)]
        else:
            arcs = []
        if arcs:
            positive_cells += 1
        for ll, rr in arcs:
            mvleft = moments[int(ll)] if ll == int(ll) else moment_vector(2-2*theta,ll)
            mvright = moments[int(rr)] if rr == int(rr) else moment_vector(2-2*theta,rr)
            delta = [bb-aa for aa,bb in zip(mvleft,mvright)]
            gradcont += gradient_integral(AA,PP,theta,delta)
    continuous_error = abs(ctheta*Econt+gradcont-(Mcont-atomic_work+bcont))
    assert gradcont >= 0
    # Prior readouts and sign roots have only 35 printed significant digits.
    assert continuous_error < mp.mpf('1e-27')
    assert positive_cells == row['positive_cell_counts']['full']+row['positive_cell_counts']['partial']
    out = {'label':row['label'], 'Y':fmt(Y), 'Z':fmt(Z), 'theta':fmt(theta),
           'left_integer':L, 'right_integer':R, 'node_count':len(nodes),
           'coercivity_constant':fmt(ctheta), 'interior_positive_square_sum':fmt(S),
           'coercive_square_term':fmt(ctheta*S), 'discrete_gradient_energy':fmt(gradient),
           'nonnegative_contact_cost':fmt(contact), 'positive_potential_remainder':fmt(remainder),
           'signed_source_work':fmt(H), 'background_source_work':fmt(Hbg),
           'road_source_work':fmt(Hroad), 'positive_source_pairing':fmt(Hpos),
           'negative_source_pairing':fmt(Hneg), 'source_absolute_over_signed':fmt((Hpos+Hneg)/abs(H)) if H else None,
           'left_boundary_contribution':fmt(left_flux), 'right_boundary_contribution':fmt(right_flux),
           'actual_boundary_contribution':fmt(boundary), 'source_plus_boundary':fmt(rhs),
           'signed_work_upper_over_actual_square_sum':fmt(rhs/(ctheta*S)),
           'source_positive_Cauchy_upper_over_actual_square_sum':fmt(coarse_root**2/S),
           'gamma_range':[fmt(min_gamma),fmt(max_gamma)],
           'maximum_recurrence_error':fmt(max_recurrence_error), 'discrete_identity_error':fmt(error),
           'factor_strata':[{**{'omega':k},**{kk:(vv if isinstance(vv,int) else fmt(vv)) for kk,vv in d.items()}}
                            for k,d in strata.items()],
           'continuous':{'reused_positive_energy':fmt(Econt), 'reused_positive_first_moment':fmt(Mcont),
                         'atomic_road_work':fmt(atomic_work), 'signed_source_work':fmt(Mcont-atomic_work),
                         'left_flux':fmt(bleft), 'right_flux':fmt(bright), 'boundary_difference':fmt(bcont),
                         'direct_normalized_gradient_energy':fmt(gradcont),
                         'identity_error_with_35_digit_prior_inputs':fmt(continuous_error)},
           'scope':'Finite complete-road identity check; no interval certification or unbounded-window claim.'}
    return out


def main():
    prior_path = ROOT/'prior_window_readouts.json'
    prior = json.loads(prior_path.read_text())
    rows = []
    cache = {}
    nmax = max(int(mp.floor(mp.mpf(c['Y'])**mp.mpf(c['lambda']))) for c in prior['cases'])
    primes, omega = prime_data(nmax)
    logs = [mp.mpf(0)]+[mp.log(n) for n in range(1,nmax+2)]
    kappa = [mp.mpf(0)]*(nmax+1)
    for n in range(2,nmax):
        kappa[n] = n*((n+1)*logs[n+1]-2*n*logs[n]+(n-1)*logs[n-1])
    for row in prior['cases']:
        theta = mp.mpf(row['theta'])
        key = row['theta']
        if key not in cache:
            w = [mp.mpf(0)]+[mp.mpf(n)**(1-2*theta) for n in range(1,nmax+1)]
            r = [mp.mpf(0)]+[mp.mpf(n)**theta for n in range(1,nmax+1)]
            edge = [(w[n]+w[n+1])/2 for n in range(nmax)]
            moments = {n:moment_vector(2-2*theta,mp.mpf(n)) for n in range(1000,nmax+1)}
            cache[key] = {'w':w, 'r':r, 'edge':edge, 'kappa':kappa, 'moments':moments}
        result = compute(row,primes,omega,cache[key])
        rows.append(result)
        print(json.dumps({k:result[k] for k in ('label','theta','interior_positive_square_sum',
                                               'signed_source_work','actual_boundary_contribution',
                                               'signed_work_upper_over_actual_square_sum',
                                               'source_positive_Cauchy_upper_over_actual_square_sum',
                                               'discrete_identity_error')},ensure_ascii=False),flush=True)
    out = {'status':'ALL_SIGNED_INTEGER_AND_CONTINUOUS_IDENTITIES_PASSED',
           'precision_decimal_digits':80,'interval_arithmetic':False,
           'scientific_source_commit':'9fc068244e4f1117f1e75df5eb0285c6697d21d7',
           'previous_artifact_commit':prior['source_commit'],
           'prior_readouts_sha256':hashlib.sha256(prior_path.read_bytes()).hexdigest(),
           'proof':'SIGNED_POSITIVE_ENERGY.md', 'cases':rows,
           'limitations':'The arithmetic signed correlation and endpoint flux remain unproved on arbitrarily distant windows. Every node and factor stratum is retained. Prior positive-window tests were not rerun.'}
    target = ROOT/'integer_energy_results.json'
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'cases':len(rows),'path':str(target)}),flush=True)


if __name__ == '__main__':
    main()
