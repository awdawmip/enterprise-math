"""Exact finite checks for conditional zero-strip consequences. Python 3.10+."""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from math import gcd, isqrt
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

PIN = "d2984d1a0c5c8221ee103084dd3da68dd039dfaa"


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def quotient(modulus, generators):
    units = [a for a in range(1, modulus) if gcd(a, modulus) == 1]
    subgroup = {1}
    for g in generators:
        assert g in units
        layer = set(subgroup)
        while True:
            layer = {v*g % modulus for v in layer}
            if layer <= subgroup:
                break
            subgroup |= layer
    classes = {tuple(sorted(a*b % modulus for b in subgroup)) for a in units}
    return {a: min(c) for c in classes for a in c}, sorted(min(c) for c in classes)


def order_two_characters(classes, mod):
    """All signs, including the principal, for the two exponent-two examples."""
    reps = sorted(set(classes.values()))
    for bits in product((1, -1), repeat=len(reps)-1):
        sign = dict(zip(reps, (1, *bits)))
        if all(sign[classes[a*b % mod]] == sign[a]*sign[b] for a in reps for b in reps):
            yield sign


def rational_checks():
    results = []
    for q, generators in [(24, ()), (65, (4, 9, 16, 36, 49, 56))]:
        cosets, reps = quotient(q, generators)
        signs = list(order_two_characters(cosets, q))
        k = len(reps)
        assert len(signs) == k
        divisors = [d for d in range(1, q+1) if q % d == 0]
        conductors = []
        for sign in signs:
            def factors(d):
                seen = {}
                return all(seen.setdefault(a % d, sign[c]) == sign[c] for a,c in cosets.items())
            conductors.append(next(d for d in divisors if factors(d)))
        rows = []
        for x,h in [(6,5),(13,11),(25,22),(57,14),(127,60),(250,250)]:
            # Integer samples of (y(1-y))^5, multiplied by h^10.
            bins = {r: 0 for r in reps}
            seen = {r: [] for r in reps}
            for p in range(x+1,x+h):
                if prime(p) and p % q in cosets:
                    r = cosets[p % q]
                    bins[r] += ((p-x)*(x+h-p))**5
                    seen[r].append(p)
            mass=sum(bins.values())
            f = [sum(sign[r]*v for r,v in bins.items()) for sign in signs]
            for r in reps:
                assert k*bins[r] == sum(sign[r]*b for sign,b in zip(signs,f))
            energy=sum((k*v-mass)**2 for v in bins.values())
            assert energy == k*sum(b*b for sign,b in zip(signs,f) if any(s<0 for s in sign.values()))
            rows.append({"x":x,"h":h,"empty":sum(not ps for ps in seen.values()),"primes":sum(map(len, seen.values())), "signed_energy":energy})
        results.append({"modulus":q,"index":k,"conductors":sorted(conductors),"windows":rows})
    return results


def product_coverage():
    modulus=17
    primes=[p for p in range(28,54) if prime(p)]
    pairs=Counter(a*b % modulus for a in primes for b in primes)
    expected=[2,2,2,3,2,6,4,3,4,2,2,4,3,2,5,3]
    assert [pairs[z] for z in range(1,17)]==expected and sum(expected)==len(primes)**2
    return {"modulus":modulus,"open_interval":[27,54],"primes":primes,"ordered_pair_counts":expected}


def polmod(a,b):
    while a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a


def irreducibles(top):
    out = []
    for n in range(1,top+1):
        out.append([f for f in range(1<<n,2<<n) if all(
            polmod(f,g) for ds in out[:n//2] for g in ds)])
    return out


def polynomial_checks():
    primes = irreducibles(13)
    rows = []
    for mod in (0b1011,0b10011,0b1000011):
        d=mod.bit_length()-1
        assert mod in primes[d-1]
        order=2**d-1
        logs={}
        e=1
        for j in range(order):
            assert e not in logs
            logs[e]=j
            e=polmod(e<<1,mod)
        assert e==1
        for k in {3: (7,),4: (3,5,15),6: (3,7,9,21,63)}[d]:
            counts=[]
            for n,layer in enumerate(primes,1):
                bins=Counter(logs[r]%k for f in layer if (r:=polmod(f,mod)))
                exact=sum((k*n*bins[g]-2**n)**2 for g in range(k))
                assert exact <= k*k*(d+2)**2*2**n
                assert all((k*n*bins[g]-2**n)**2<=k*k*(d+2)**2*2**n for g in range(k))
                counts.append(len(bins))
            rows.append({"modulus_bits":bin(mod),"degree":d,"quotient_order":k,"occupied_by_degree_1_to_13":counts,
                         "first_full_degree":next((n for n,c in enumerate(counts,1) if c==k),None)})
    return rows


def typed_checks(repo):
    # Execute the exact four source modules from public git objects, in a temporary package.
    names = ("core","division","exact_arithmetic","brc_logarithm")
    with TemporaryDirectory() as t:
        pkg=Path(t)/"em_frozen"
        pkg.mkdir()
        (pkg/"__init__.py").write_text("")
        for name in names:
            data=subprocess.check_output(["git","-C",str(repo),"show",f"{PIN}:src/enterprise_math/{name}.py"])
            (pkg/f"{name}.py").write_bytes(data)
        sys.path.insert(0,t)
        try:
            from em_frozen.exact_arithmetic import brc_evaluate_division, division
            from em_frozen.brc_logarithm import ln, brc_evaluate_ln
            rows=[]
            for p in (53,59,61,67):
                d=brc_evaluate_division(division(p,5))
                ell=brc_evaluate_ln(ln(division(p,1)),10**3)
                assert d.reconstruct()==p and d.remainder in range(1,5)
                assert Fraction(ell.lower_numerator,ell.lower_denominator) <= Fraction(ell.upper_numerator,ell.upper_denominator)
                assert ell.lower_floor_trace.quotient == ell.upper_floor_trace.quotient == ell.scaled_value
                rows.append({"p":p,"q":5,"quotient":d.quotient,"remainder":d.remainder,
                             "sign":1 if d.remainder in (1,4) else -1,"floor_1000_log_p":ell.scaled_value,
                             "division_trace":d.evaluation_kind,"ln_trace":ell.evaluation_kind})
            signed=[sum(row["sign"] for row in rows if row["p"] in s) for s in ((59,61),(53,67))]
            assert signed==[2,-2]
            return {"git":PIN,"rows":rows,"two_source_histograms_signed":signed}
        finally:
            sys.path.remove(t)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True,help="public enterprise-math Git checkout containing pinned source")
    args=parser.parse_args()
    print(json.dumps({"dirichlet_group_checks":rational_checks(),"function_field_checks":polynomial_checks(),"product_coverage":product_coverage(),
                      "typed_finite_readouts":typed_checks(args.repo)},indent=2,sort_keys=True))
