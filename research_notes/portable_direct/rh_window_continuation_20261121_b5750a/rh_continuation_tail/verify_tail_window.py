#!/usr/bin/env python3
"""Finite checks for the exact centered-tail and window-Gram identities.

All numerical checks use 80-digit mpmath floating point, not interval arithmetic.
The accompanying manuscript supplies the general proofs. Infinite road energy
or the RH-equivalent O(a) estimate is never inferred from these computations.
"""
from pathlib import Path
from math import comb, floor
import json
import mpmath as mp

mp.mp.dps = 80


def road_values(a, nmax):
    values = [mp.mpf(0)] + [mp.mpf(1)] * nmax
    sieve = [True] * (nmax + 1)
    for p in range(2, nmax + 1):
        if sieve[p]:
            factor = -mp.expm1(-a * mp.log(p))
            for n in range(p, nmax + 1, p):
                values[n] *= factor
                if n > p:
                    sieve[n] = False
    return values


def family(a, nmax):
    z = mp.zeta(1 + a)
    c = 1 / z
    cp = -mp.diff(mp.zeta, 1 + a) / z**2
    kappa = (mp.euler - 1) * c + cp - 1
    values = road_values(a, nmax)
    cumulative = [mp.mpf(0)]
    for v in values[1:]:
        cumulative.append(cumulative[-1] + v)
    return {"a": a, "c": c, "cp": cp, "kappa": kappa,
            "values": values, "sum": cumulative}


def primitive_u(f, y):
    """Integral_1^y (S_a(t)-1-c_a*t)/t^2 dt, from a finite road sum."""
    return (mp.fsum(f["values"][n] * (mp.mpf(1)/n - 1/y)
                    for n in range(2, int(mp.floor(y)) + 1))
            - f["c"] * mp.log(y))


def groad(f, y):
    return (mp.fsum(f["values"][n] * (y/n - 1)
                    for n in range(2, int(mp.floor(y)) + 1))/f["a"]
            - y*mp.log(y) + (1+mp.euler)*y)


def intervals(y, z):
    cuts = [y]
    cuts += [mp.mpf(n) for n in range(int(mp.floor(y))+1, int(mp.ceil(z)))
             if y < n < z]
    cuts.append(z)
    return list(zip(cuts[:-1], cuts[1:]))


def fmt(x):
    return mp.nstr(x, 35)


def verify():
    laurent = []
    for a in map(mp.mpf, ["0.1", "0.5", "2"]):
        f = family(a, 2)
        rows = []
        for eps in map(mp.mpf, ["1e-4", "1e-6", "1e-8"]):
            finite_part = (mp.zeta(1+eps) / mp.zeta(1+a+eps)/(1+eps)
                           - f["c"]/eps)
            error = abs(finite_part - (f["kappa"]+1))
            rows.append({"epsilon": fmt(eps), "absolute_error": fmt(error)})
        assert error < mp.mpf("1e-6")
        laurent.append({"a": fmt(a), "kappa": fmt(f["kappa"]), "checks": rows})

    finite_tail = []
    for a in (mp.mpf(2), mp.mpf(3)):
        f = family(a, 1024)
        e_bound = mp.zeta(a) + 2**a/a
        for horizon in (256, 1024):
            error = abs(f["kappa"] - primitive_u(f, mp.mpf(horizon)))
            bound = (e_bound+1)/horizon
            assert error <= bound
            finite_tail.append({"a": fmt(a), "horizon": horizon,
                                "moment_tail_absolute_error": fmt(error),
                                "proved_unconditional_bound": fmt(bound)})

    cell_count = 0
    worst_cell_bound_slack = mp.inf
    for a in map(mp.mpf, ["0.1", "0.5", "2"]):
        f = family(a, 200)
        c = f["c"]
        for n in range(1, 201):
            aa = f["sum"][n] - 1
            b = aa - c*(n+mp.mpf("0.5"))
            qcell = aa**2/(n*(n+1)) - 2*c*aa*mp.log1p(mp.mpf(1)/n) + c**2
            unweighted = b**2 + c**2/12
            lo, hi = unweighted/(n+1)**2, unweighted/n**2
            assert lo - mp.mpf("1e-65") <= qcell <= hi + mp.mpf("1e-65")
            worst_cell_bound_slack = min(worst_cell_bound_slack, qcell-lo, hi-qcell)
            cell_count += 1

    gram = []
    for m in (1, 2, 3):
        h = mp.mpf("0.07")
        fs = [family(j*h, 8) for j in range(1, m+1)]
        weights = [mp.mpf((-1)**(j+1)*comb(m,j)) for j in range(1,m+1)]
        coeff = [w/j for j,w in enumerate(weights, start=1)]
        assert mp.fsum(weights) == 1
        harmonic = mp.fsum(mp.mpf(1)/j for j in range(1,m+1))
        assert abs(mp.fsum(coeff)-harmonic) < mp.mpf("1e-75")
        ccombo = mp.fsum(co*f["c"] for co,f in zip(coeff,fs))
        bcombo = mp.fsum(w*(f["c"]/f["a"]-1) for w,f in zip(weights,fs))
        dcombo = mp.fsum(w*(1+mp.euler+f["kappa"]/f["a"])
                        for w,f in zip(weights,fs))
        y, z = mp.mpf("2.5"), mp.mpf("7.5")
        pieces = intervals(y,z)
        flux = mp.fsum(co*(f["kappa"]-primitive_u(f,z))
                      for co,f in zip(coeff,fs))

        def tail(t):
            return mp.fsum(co*(f["kappa"]-primitive_u(f,t))
                           for co,f in zip(coeff,fs))

        identity_errors = []
        for t in (y, mp.mpf("3.2"), mp.mpf("5.1"), z):
            direct = mp.fsum(w*groad(f,t) for w,f in zip(weights,fs))
            reconstructed = t*(bcombo*mp.log(t)+dcombo)-t*tail(t)/h
            error = abs(direct-reconstructed)
            assert error < mp.mpf("1e-65")
            identity_errors.append(error)

        for theta in (mp.mpf("0.6"), mp.mpf("0.75")):
            r = 2-2*theta
            def a_weight(t):
                return (t**r-y**r)/r

            def j_primitive(aa,t):
                return (aa*t**(r-1)/(r-1) - ccombo*t**r/r
                        + y**r*aa/t + y**r*ccombo*mp.log(t))/r

            def l_primitive(aa,t):
                return (aa**2*t**(-2*theta)/(-2*theta)
                        -2*aa*ccombo*t**(1-2*theta)/(1-2*theta)
                        +ccombo**2*t**(2-2*theta)/(2-2*theta))

            prefix = mp.mpf(0)
            kernel_double = mp.mpf(0)
            local_weighted_energy = mp.mpf(0)
            for left,right in pieces:
                n = int(mp.floor((left+right)/2))
                aa = mp.fsum(co*(f["sum"][n]-1) for co,f in zip(coeff,fs))
                base = prefix
                jp_left = j_primitive(aa,left)
                kernel_double += 2*mp.quad(
                    lambda t: (aa-ccombo*t)/t**2
                    * (base+j_primitive(aa,t)-jp_left), [left,right])
                prefix += j_primitive(aa,right)-jp_left
                local_weighted_energy += l_primitive(aa,right)-l_primitive(aa,left)

            direct_tail_energy = mp.fsum(mp.quad(lambda t:t**(r-1)*tail(t)**2,[l,u])
                                         for l,u in pieces)
            local_integral_energy = mp.fsum(mp.quad(lambda t:t**(r-1)*(tail(t)-flux)**2,[l,u])
                                            for l,u in pieces)
            flux_energy = flux**2*a_weight(z)
            cross = 2*flux*prefix
            reconstructed_energy = flux_energy+cross+kernel_double
            kernel_error = abs(direct_tail_energy-reconstructed_energy)
            assert kernel_error < mp.mpf("1e-65")
            assert abs(local_integral_energy-kernel_double) < mp.mpf("1e-65")
            hardy_upper = local_weighted_energy/(1-theta)**2
            assert local_integral_energy <= hardy_upper+mp.mpf("1e-65")
            gram.append({"m":m,"h":fmt(h),"theta":fmt(theta),"Y":fmt(y),"Z":fmt(z),
                         "harmonic_constant_port":fmt(harmonic),
                         "boundary_flux":fmt(flux),"flux_energy":fmt(flux_energy),
                         "signed_boundary_cross_term":fmt(cross),
                         "local_gram_energy":fmt(kernel_double),
                         "total_tail_energy":fmt(direct_tail_energy),
                         "hardy_local_upper":fmt(hardy_upper),
                         "gram_identity_absolute_error":fmt(kernel_error),
                         "max_groad_tail_identity_error":fmt(max(identity_errors))})

    drift = []
    for m in (1,2,3,4):
        weights = [mp.mpf((-1)**(j+1)*comb(m,j)) for j in range(1,m+1)]
        for h in map(mp.mpf,["0.01","0.005","0.0025"]):
            fs = [family(j*h,2) for j in range(1,m+1)]
            b = mp.fsum(w*(f["c"]/f["a"]-1) for w,f in zip(weights,fs))
            d = mp.fsum(w*(1+mp.euler+f["kappa"]/f["a"])
                       for w,f in zip(weights,fs))
            drift.append({"m":m,"h":fmt(h),"b_over_h_to_m":fmt(b/h**m),
                          "d_over_h_to_m":fmt(d/h**m)})

    return {"status":"PASS","precision_decimal_digits":80,"interval_arithmetic":False,
            "general_proof":"CENTERED_TAIL_AND_WINDOW_ENERGY.md",
            "laurent_constant_checks":laurent,"unconditional_finite_tail_checks":finite_tail,
            "unit_cell_checks":cell_count,"minimum_cell_inequality_slack":fmt(worst_cell_bound_slack),
            "exact_window_gram_checks":gram,"fixed_order_drift_scaling_observations":drift,
            "unproved":"Uniform road energy, local-window flux/energy bounds, and RH are not established by these finite checks."}


if __name__ == "__main__":
    result = verify()
    target = Path(__file__).with_name("tail_window_results.json")
    target.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":result["status"],"unit_cell_checks":result["unit_cell_checks"],
                      "window_gram_cases":len(result["exact_window_gram_checks"]),
                      "result_path":str(target)}))
