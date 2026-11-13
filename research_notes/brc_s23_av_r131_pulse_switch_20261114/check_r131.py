#!/usr/bin/env python3
"""R131 exact pulse decomposition and existential/trace cost separation.

Python 3.11+, standard library only. All mathematical comparisons use Fraction.
"""
from fractions import Fraction
from time import perf_counter_ns
from statistics import median
import json
import random


def direct(theta, B):
    assert B >= 2 and 0 < theta < 1
    u = B * theta
    return int(u - (u.numerator // u.denominator) < theta)


def pulse(theta, B):
    assert B >= 2 and 0 < theta < 1
    k = (B * theta).numerator // (B * theta).denominator
    return int(k >= 1 and theta < Fraction(k, B - 1))


def positive_intervals(B):
    assert B >= 2
    return [(Fraction(k, B), Fraction(k, B - 1)) for k in range(1, B)]


def exact_cuts(B):
    return sorted({Fraction(k, B) for k in range(1, B)} |
                  {Fraction(k, B - 1) for k in range(1, B-1)})


def phase_samples(B):
    p = [Fraction(0), *exact_cuts(B), Fraction(1)]
    for i in range(len(p) - 1):
        yield (p[i]+p[i+1])/2
        if i + 1 < len(p) - 1:
            yield p[i+1]


def certificate(pattern, B):
    """Return exact theta or None; pattern is an iterable of 0/1."""
    assert B >= 2
    p = tuple(pattern)
    assert len(p) >= 1 and all(v in (0,1) for v in p)
    if len(set(p)) > 1:
        return None
    if p[0] == 0:
        return Fraction(1, 2*B)
    return (Fraction(1, B)+Fraction(1, B-1))/2


def trace(B):
    # Explicitly emits ordered values at cuts and open intervals.
    cuts = exact_cuts(B)
    endpoints = [Fraction(0), *cuts, Fraction(1)]
    out = []
    for j in range(len(endpoints)-1):
        out.append(direct((endpoints[j]+endpoints[j+1])/2, B))
        if j < len(cuts):
            out.append(direct(cuts[j], B))
    return out


def test_all():
    cases = 0
    phase_count = 0
    total_cuts = 0
    for B in range(2, 161):
        cuts = exact_cuts(B)
        assert len(cuts) == 2*B - 3
        assert len(positive_intervals(B)) == B-1
        # Disjoint pulse intervals; their left boundary is included; right excluded.
        intervals = positive_intervals(B)
        assert all(intervals[i][1] < intervals[i+1][0] for i in range(len(intervals)-1))
        reps = list(phase_samples(B))
        assert len(reps) == 4*B - 5
        for t in reps:
            d, p = direct(t,B),pulse(t,B)
            assert d==p, (B,t,d,p)
            if t in cuts:
                assert d == int(any(a<=t<b for a,b in intervals))
        for m in (1,2,5,17):
            for bit in (0,1):
                theta = certificate((bit,)*m, B)
                assert theta is not None and all(direct(theta,B)==bit for _ in range(m))
            if m>=2:
                assert certificate((0,1)+(0,)*(m-2),B) is None
        cases += 1
        phase_count += len(reps)
        total_cuts += len(cuts)
    return {"checked_B_min":2,"checked_B_max":160,"B_cases":cases,
            "atom_representatives":phase_count,"total_distinct_cuts":total_cuts,
            "patterns_checked_per_B":"all 0/1 for m=1,2,5,17; exactly m-bit mixed for m>=2"}


def test_random():
    rng = random.Random(131)
    n=0
    for _ in range(5000):
        B=rng.randrange(2,1000000)
        den=rng.randrange(2,2_000_000)
        t=Fraction(rng.randrange(1,den),den)
        assert direct(t,B)==pulse(t,B)
        n+=1
    return n


def test_large():
    B=10**150+37
    z=certificate([0]*13,B)
    o=certificate([1]*13,B)
    assert direct(z,B)==0 and direct(o,B)==1
    assert pulse(Fraction(B-1,B),B)==1
    assert pulse(Fraction(1,B-1),B)==0
    return {"B_decimal_digits":len(str(B)), "B":str(B),
            "zero_witness":{"numerator":str(z.numerator),"denominator":str(z.denominator)},
            "one_witness":{"numerator":str(o.numerator),"denominator":str(o.denominator)}}


def scaled_family_check():
    # A = r*e, E=e, d=x=0; domain (0,K/e).
    count=0
    probes=0
    for r in range(2,18):
        for e in (1,2,7):
            for K in (1,2,5):
                starts=[Fraction(n, e)+Fraction(k,r*e) for n in range(K) for k in range(1,r)]
                ends=[Fraction(n,e)+Fraction(k,(r-1)*e) for n in range(K) for k in range(1,r)]
                cuts=sorted(set(starts+ends) - {Fraction(K,e)})
                assert len(cuts)==K*(2*r-2)-1
                points=[Fraction(0),*cuts,Fraction(K,e)]
                for j in range(len(points)-1):
                    for t in ((points[j]+points[j+1])/2, points[j+1]):
                        if not (0<t<Fraction(K,e)):
                            continue
                        phi=e*t
                        u=r*phi
                        d=int((u - u.numerator//u.denominator)<(phi-phi.numerator//phi.denominator))
                        exp=int(any(a<=t<b for a,b in zip(starts,ends)))
                        assert d==exp, (r,e,K,t,d,exp)
                        probes+=1
                count+=1
    return {"cases":count,"exact_parameter_checks":probes,
            "r_range":"2..17","e_values":[1,2,7],"K_values":[1,2,5]}


def benchmark():
    output=[]
    for B in [64,256,1024,4096]:
        a=[];b=[]
        for _ in range(3):
            start=perf_counter_ns();w=trace(B); a.append((perf_counter_ns()-start)/1e6)
            start=perf_counter_ns();w0=certificate([0]*16,B);w1=certificate([1]*16,B); b.append((perf_counter_ns()-start)/1e6)
            assert direct(w0,B)==0 and direct(w1,B)==1
            assert len(w)==4*B-5
        output.append({"B":B,"explicit_positions":4*B-5,"trace_median_ms":median(a),"certificate_median_ms":median(b),
                       "trace_bits":len(w),"witness_decimal_digits_max":max(len(str(w0.denominator)),len(str(w1.denominator)))})
    return output


if __name__ == '__main__':
    results={"schema":"EM_R131_PULSE_CHECK_V1", "exact_exhaustive":test_all(),
             "random_rationals_checked":test_random(),"aligned_scaled":scaled_family_check(),
             "huge_integer":test_large(),"benchmark":benchmark(),
             "result":"R131_PULSE_SWITCH_PASS","arithmetic":"Fraction exact",
             "runtime":"CPython standard library; in-process wall clock medians of three; not calibrated"}
    print(json.dumps(results, ensure_ascii=False, indent=2))
