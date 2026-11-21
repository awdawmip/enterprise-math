#!/usr/bin/env python3
"""Positivity-aware finite road-window computation, with matched thicknesses.

The proof is in ONE_SIDED_WINDOW_INTERFACE.md. This program uses 80-digit
floating point and explicit cell antiderivatives; it is not interval arithmetic.
Every road coefficient in the finite window horizon is retained.
"""
from pathlib import Path
from math import comb
import json
import mpmath as mp

mp.mp.dps = 80


def primes_to(nmax):
    sieve = [True] * (nmax+1)
    out = []
    for p in range(2,nmax+1):
        if sieve[p]:
            out.append(p)
            for n in range(p*p,nmax+1,p):
                sieve[n] = False
    return out


def road_values(a,nmax,primes):
    values = [mp.mpf(0)] + [mp.mpf(1)]*nmax
    for p in primes:
        factor = -mp.expm1(-a*mp.log(p))
        for n in range(p,nmax+1,p):
            values[n] *= factor
    return values


def weights_equispaced(m,Y,theta,lam):
    logz = lam*mp.log(Y)
    h = (mp.mpf(m+1)/2)**(mp.mpf(1)/m)*Y**(-lam*(1-theta)/m)/logz**(1+mp.mpf(2)/m)
    nodes = [j*h for j in range(1,m+1)]
    weights = [mp.mpf((-1)**(j+1)*comb(m,j)) for j in range(1,m+1)]
    return nodes,weights


def weights_chebyshev(Y,theta,lam):
    logz = lam*mp.log(Y)
    m = int(mp.ceil(logz))
    A = mp.mpf("0.5")
    b = A*mp.tanh(mp.acosh(3)/(2*(m-1)))**2
    nodes = [(A+b)/2-(A-b)/2*mp.cos(mp.pi*j/(m-1)) for j in range(m)]
    weights = [mp.fprod(-nodes[k]/(nodes[j]-nodes[k])
                        for k in range(m) if k!=j) for j in range(m)]
    assert abs(mp.fsum(weights)-1) < mp.mpf("1e-65")
    assert abs(mp.fsum(abs(w) for w in weights)-3) < mp.mpf("1e-65")
    for power in range(1,m):
        assert abs(mp.fsum(w*a**power for w,a in zip(weights,nodes))) < mp.mpf("1e-65")
    return nodes,weights


def moment(nu,k,y):
    l = mp.log(y)
    if nu == 0:
        return l**(k+1)/(k+1)
    if k == 0:
        return y**nu/nu
    if k == 1:
        return y**nu*(l/nu-1/nu**2)
    return y**nu*(l*l/nu-2*l/nu**2+2/nu**3)


def moment_vector(r,y):
    return (moment(r,0,y),moment(r,1,y),moment(r,2,y),
            moment(r-1,0,y),moment(r-1,1,y),moment(r-2,0,y))


def subtract(a,b):
    return tuple(x-y for x,y in zip(a,b))


def cell_moments(A,P,d):
    weight = d[0]
    first = A*d[0]-d[1]-P*d[3]
    second = A*A*d[0]-2*A*d[1]+d[2]-2*P*(A*d[3]-d[4])+P*P*d[5]
    return weight,first,second


def phi(A,P,y):
    return A-mp.log(y)-P/y


def crossing(A,P,left,right):
    fl = phi(A,P,left)
    fr = phi(A,P,right)
    assert fl*fr < 0
    tol = mp.mpf("1e-44")*max(1,abs(left),abs(right))
    while right-left > tol:
        mid = (left+right)/2
        fm = phi(A,P,mid)
        if fm == 0:
            return mid
        if fl*fm > 0:
            left,fl = mid,fm
        else:
            right,fr = mid,fm
    return (left+right)/2


def positive_arcs(A,P,left,right):
    cuts = [left]
    if left < P < right:
        cuts.append(P)
    cuts.append(right)
    out = []
    for l,u in zip(cuts[:-1],cuts[1:]):
        fl,fu = phi(A,P,l),phi(A,P,u)
        if fl >= 0 and fu >= 0:
            out.append((l,u))
        elif fl <= 0 and fu <= 0:
            continue
        else:
            root = crossing(A,P,l,u)
            out.append((l,root) if fl > 0 else (root,u))
    merged = []
    for l,u in out:
        if merged and merged[-1][1] == l:
            merged[-1] = (merged[-1][0],u)
        else:
            merged.append((l,u))
    return merged


def fmt(x):
    return mp.nstr(x,35)


def compute_case(label,Y,theta,lam,nodes,weights,grid,primes):
    Z = Y**lam
    nmax = int(mp.floor(Z))
    # n=1 is the anchor: the full derivative stencil gives D(1)=0.
    D = [mp.mpf(0)]*(nmax+1)
    Cbg = mp.mpf(0)
    dbg = mp.mpf(0)
    for a,w in zip(nodes,weights):
        road = road_values(a,nmax,primes)
        for n in range(2,nmax+1):
            D[n] += w*road[n]/a
        zeta = mp.zeta(1+a)
        c = 1/zeta
        cp = -mp.diff(mp.zeta,1+a)/zeta**2
        kappa = (mp.euler-1)*c+cp-1
        Cbg += w*c/a
        dbg += w*(1+mp.euler+kappa/a)
    bbg = Cbg-1
    prefixes = [mp.mpf(0)]*(nmax+1)
    reciprocal = [mp.mpf(0)]*(nmax+1)
    for n in range(2,nmax+1):
        prefixes[n] = prefixes[n-1]+D[n]
        reciprocal[n] = reciprocal[n-1]+D[n]/n
    r = 2-2*theta
    whole = subtract(moment_vector(r,Z),moment_vector(r,Y))
    W = whole[0]
    full_energy = mp.mpf(0)
    first_moment = mp.mpf(0)
    pos_energy = mp.mpf(0)
    pos_first = mp.mpf(0)
    pos_weight = mp.mpf(0)
    local_residual_energy = mp.mpf(0)
    sampled_error = mp.mpf(0)
    n_full,n_empty,n_partial,n_arcs = 0,0,0,0
    pmin,pmax = mp.inf,-mp.inf
    partial_records = []
    for idx,(left,right,d) in enumerate(grid):
        N = int(mp.floor((left+right)/2))
        P = prefixes[N]
        A = 1+mp.euler+reciprocal[N]
        _,f,e = cell_moments(A,P,d)
        first_moment += f
        full_energy += e
        local_residual_energy += P*P*d[5]-2*P*Cbg*d[3]+Cbg*Cbg*d[0]
        vals = [phi(A,P,left),phi(A,P,right)]
        if left < P < right:
            vals.append(phi(A,P,P))
        pmin,pmax = min(pmin,*vals),max(pmax,*vals)
        arcs = positive_arcs(A,P,left,right)
        n_arcs += len(arcs)
        is_full = len(arcs)==1 and arcs[0][0]==left and arcs[0][1]==right
        if is_full:
            n_full += 1
            pos_weight += d[0]
            pos_first += f
            pos_energy += e
        elif not arcs:
            n_empty += 1
        else:
            n_partial += 1
            partial_records.append({"N":N,"positive_arcs":[[fmt(l),fmt(u)] for l,u in arcs]})
            for l,u in arcs:
                dp = subtract(moment_vector(r,u),moment_vector(r,l))
                wp,fp,ep = cell_moments(A,P,dp)
                pos_weight += wp
                pos_first += fp
                pos_energy += ep
                # Independent quadrature is used on actual sign-boundary arcs.
                quad = mp.quad(lambda t:t**(r-1)*phi(A,P,t)**2,[l,u])
                sampled_error = max(sampled_error,abs(quad-ep))
        if idx in (0,len(grid)//2,len(grid)-1):
            quad = mp.quad(lambda t:t**(r-1)*phi(A,P,t)**2,[left,right])
            sampled_error = max(sampled_error,abs(quad-e))

    mean = first_moment/W
    variance = full_energy-W*mean**2
    single_side_moment_upper = variance+W*max(mean,0)**2
    phiZ = phi(1+mp.euler+reciprocal[nmax],prefixes[nmax],Z)
    tau = bbg*mp.log(Z)+dbg-phiZ
    drift_energy = bbg*bbg*whole[2]+2*bbg*dbg*whole[1]+dbg*dbg*whole[0]
    old_separate_upper = (mp.sqrt(drift_energy)
                          +mp.sqrt(local_residual_energy)/(1-theta)
                          +abs(tau)*mp.sqrt(W))**2
    tol = mp.mpf("1e-48")
    assert variance >= -tol
    assert -tol <= pos_energy <= single_side_moment_upper+tol <= full_energy+2*tol
    assert pos_energy <= old_separate_upper+tol
    assert sampled_error < tol
    return {"label":label,"Y":fmt(Y),"Z":fmt(Z),"theta":fmt(theta),"lambda":fmt(lam),
            "node_count":len(nodes),"nodes":[fmt(a) for a in nodes],
            "minimum_thickness":fmt(min(nodes)),"maximum_thickness":fmt(max(nodes)),
            "weights":[fmt(w) for w in weights],
            "weight_l1":fmt(mp.fsum(abs(w) for w in weights)),
            "derivative_coefficient_l1":fmt(mp.fsum(abs(w)/a for w,a in zip(weights,nodes))),
            "weighted_window_mass":fmt(W),"weighted_mean_Phi":fmt(mean),
            "weighted_variance_Phi":fmt(variance),"full_squared_energy":fmt(full_energy),
            "positive_part_energy":fmt(pos_energy),
            "one_sided_mean_variance_upper":fmt(single_side_moment_upper),
            "old_separated_drift_local_boundary_upper":fmt(old_separate_upper),
            "old_upper_over_positive_energy":fmt(old_separate_upper/pos_energy) if pos_energy else None,
            "weighted_positive_fraction":fmt(pos_weight/W),
            "positive_cell_counts":{"full":n_full,"empty":n_empty,"partial":n_partial},
            "positive_arcs":n_arcs,"sign_boundary_records":partial_records,
            "min_Phi":fmt(pmin),"max_Phi":fmt(pmax),
            "actual_normalized_boundary_flux_tau":fmt(tau),
            "free_full_square_optimal_tau_offset":fmt(mean),
            "positive_energy_derivative_at_actual_tau":fmt(-2*pos_first),
            "positive_energy_second_derivative_at_actual_tau":fmt(2*pos_weight),
            "boundary_error_for_ten_percent_root_energy_change":fmt(mp.mpf("0.1")*mp.sqrt(pos_energy/W)),
            "maximum_independent_quadrature_error":fmt(sampled_error),
            "formal_scope":"Finite real-road comparison; no infinite-window or RH conclusion."}


def make_grid(Y,theta,lam):
    Z = Y**lam
    r = 2-2*theta
    cuts = [Y] + [mp.mpf(n) for n in range(int(mp.floor(Y))+1,int(mp.ceil(Z))) if Y<n<Z]+[Z]
    vals = [moment_vector(r,y) for y in cuts]
    return [(l,u,subtract(b,a)) for l,u,a,b in zip(cuts[:-1],cuts[1:],vals[:-1],vals[1:])]


def main():
    lam = mp.mpf("1.5")
    rows = []
    for Y,theta,modes in [(mp.mpf(100),mp.mpf("0.6"),["m1"]),
                          (mp.mpf(1000),mp.mpf("0.6"),["m1","m2","chebyshev"]),
                          (mp.mpf(1000),mp.mpf("0.9"),["m1"])]:
        grid = make_grid(Y,theta,lam)
        primes = primes_to(int(mp.floor(Y**lam)))
        for mode in modes:
            if mode == "chebyshev":
                nodes,weights = weights_chebyshev(Y,theta,lam)
            else:
                nodes,weights = weights_equispaced(int(mode[1:]),Y,theta,lam)
            row = compute_case(mode,Y,theta,lam,nodes,weights,grid,primes)
            rows.append(row)
            print(json.dumps({"label":mode,"Y":fmt(Y),"theta":fmt(theta),"positive_energy":row["positive_part_energy"],
                              "full_energy":row["full_squared_energy"],
                              "old_upper_ratio":row["old_upper_over_positive_energy"],
                              "cell_counts":row["positive_cell_counts"]}),flush=True)
    result={"status":"PASS","precision_decimal_digits":80,"interval_arithmetic":False,
            "cases":rows,"proof":"ONE_SIDED_WINDOW_INTERFACE.md",
            "limitations":"All windows are finite. Free boundary shifts are diagnostics, not authorized changes to the actual road observable. Chebyshev bridge parameters are supplied by the parent proof; this script checks their finite algebra and evaluates their actual road window."}
    target=Path(__file__).with_name("one_sided_window_results.json")
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":"PASS","cases":len(rows),"result_path":str(target)}),flush=True)


if __name__=="__main__":
    main()
