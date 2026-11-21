#!/usr/bin/env python3
"""Finite road-model cost probe, not a uniform estimate or interval proof."""
from fractions import Fraction
from pathlib import Path
import json
import math
import mpmath as mp

mp.mp.dps = 50


def factors_and_mu(q):
    factors = []
    n = q
    p = 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            factors.append(p)
            if n % p == 0:
                return [], 0
        p += 1
    if n > 1:
        factors.append(n)
    return factors, (-1)**len(factors)


def positive_integrals(angles, amplitudes, b):
    us = [aa*mp.cot(th/2)/2 for aa, th in zip(amplitudes, angles)]
    mean = mp.fsum(u*t for u,t in zip(us,angles))/mp.pi
    tail_u = mp.fsum(us)
    tail_a = mp.fsum(amplitudes)
    previous = mp.mpf(0)
    es = er = mp.mpf(0)
    for angle, u, amplitude in list(zip(angles, us, amplitudes)) + [(mp.pi,0,0)]:
        es += mp.pi/2*(angle-previous)*(tail_u-mean)**2
        const = tail_a+2*b
        slope = -2*b/mp.pi
        er += mp.pi/8*(const*const*(angle-previous)
                       +const*slope*(angle*angle-previous*previous)
                       +slope*slope*(angle**3-previous**3)/3)
        tail_u -= u
        tail_a -= amplitude
        previous = angle
    return es, er


def main():
    cutoffs = [16,64,256]
    sources = {}
    frequencies = []
    for q in range(2,max(cutoffs)+1):
        factors, mu = factors_and_mu(q)
        if not mu:
            continue
        sources[q] = (factors,mu)
        if q == 2:
            frequencies.append((Fraction(1,2),q,1))
        else:
            for r in range(1,(q+1)//2):
                if math.gcd(r,q)==1:
                    frequencies.append((Fraction(r,q),q,2))
    frequencies.sort()
    angles = {f:2*mp.pi*f.numerator/f.denominator for f,_,_ in frequencies}
    rows=[]
    for a in [mp.mpf('0.5'),mp.mpf('0.25'),mp.mpf('0.1'),mp.mpf('0.05')]:
        ca=1/mp.zeta(1+a)
        betas={q:mu/mp.fprod(mp.power(p,1+a)-1 for p in factors)
               for q,(factors,mu) in sources.items()}
        for cutoff in cutoffs:
            selected=[(f,q,mul) for f,q,mul in frequencies if q<=cutoff]
            xs=[angles[f] for f,q,mul in selected]
            amp=[mul*ca*betas[q] for f,q,mul in selected]
            tail=1-ca*(1+mp.fsum(abs(betas[q]) for q in betas if q<=cutoff))
            anchor=1+ca/2-tail
            es,er=positive_integrals(xs,amp,anchor)
            upper=(mp.sqrt(es)+mp.sqrt(er))**2
            rows.append({"a":mp.nstr(a,12),"q_cutoff":cutoff,
                         "cosine_modes":len(selected),
                         "exact_anchor_tail_numeric":mp.nstr(tail,24),
                         "compensated_constant_port":mp.nstr(anchor,24),
                         "sine_energy":mp.nstr(es,24),"rest_energy":mp.nstr(er,24),
                         "sine_energy_over_a":mp.nstr(es/a,24),
                         "rest_energy_over_a":mp.nstr(er/a,24),
                         "cauchy_upper_over_a":mp.nstr(upper/a,24)})
    data={"precision_decimal_digits":mp.mp.dps,
          "status":"NUMERICAL_FINITE_MODEL_PROBE_NOT_UNIFORM_BOUND_NOT_INTERVAL_CERTIFICATION",
          "formula":"Exact finite-frequency positive integrals, compensated n=1 road anchor",
          "rows":rows}
    path=Path(__file__).with_name('road_certificate_probe.json')
    path.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({"output":str(path),"rows":len(rows)}))


if __name__=='__main__':
    main()
