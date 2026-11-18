"""Exact checks for finite profiled road energies; optionally specify the frozen tree."""
import argparse
import hashlib
import json
import subprocess
import sys
from fractions import Fraction as F
from functools import cache
from math import factorial, gcd, isqrt
from pathlib import Path

import sympy as sp


VERIFIER = Path("research_handoffs/COMPOSITE_ROAD_RH_20260909/stage2_verify.py")
SOURCE_DIGEST = "df49a8cd07f84375466ff9e003ac7c96044936e5b9e5b5a73cb62165bb1ae436"
OUTPUT_DIGEST = "0680ff7f9d2bd5d1ad4c7a4a9a8196d485ccf21c9a4ea4a3d7e83139e8ea4f5b"


def replay(repo):
    source = repo / VERIFIER
    if hashlib.sha256(source.read_bytes()).hexdigest() != SOURCE_DIGEST:
        raise ValueError("Frozen source digest mismatch")
    result = subprocess.run([sys.executable, str(source)], capture_output=True, check=True)
    assert hashlib.sha256(result.stdout).hexdigest() == OUTPUT_DIGEST
    return {"verifier_sha256":SOURCE_DIGEST, "stdout_sha256":OUTPUT_DIGEST,
            "exit_code":result.returncode, "stdout_json":json.loads(result.stdout)}


def log_unit(v):
    """Positive rational interval for log(v), 1 <= v <= 2, via atanh."""
    u = (v - 1) / (v + 1)
    z = u
    total = F(0)
    for i in range(22):
        total += 2*z/(2*i+1)
        z *= u*u
    return total, total + 2*z/(45*(1-u*u))


@cache
def log_integer(n):
    b = n.bit_length() - 1
    lo, hi = log_unit(F(n,2**b))
    lo2, hi2 = log_unit(F(2))
    return b*lo2 + lo, b*hi2 + hi


def check_road():
    # True a=1 arithmetic. Formula 1 uses elementary phi(n)/n from gcd counts.
    # For formula 2 independently compute the masses from their Euler products.
    limit = 36
    mass = {n:F(sum(gcd(j,n) == 1 for j in range(1,n+1)),n) for n in range(2,limit+1)}
    primes = [n for n in range(2,limit+1) if all(n%d for d in range(2,isqrt(n)+1))]
    euler = {}
    for n in range(2,limit+1):
        euler[n] = F(1)
        for prime in primes:
            if n % prime == 0:
                euler[n] *= 1 - F(1,prime)
    assert euler == mass
    P = sp.symbols("L0:"+str(len(primes)))
    prime_symbol = dict(zip(primes,P))
    logs = {1:sp.S.Zero}
    for n in range(2,limit+1):
        p = next(p for p in primes if n % p == 0)
        logs[n] = logs[n//p] + prime_symbol[p]
    moment = sp.S.Zero
    prefix = F(0)
    integral = sp.S.Zero
    samples = {}
    for N in range(1,limit):
        if N >= 2:
            prefix += euler[N]
            moment += euler[N] * logs[N]
        def primitive_at(x):
            return -(prefix**2+(prefix*logs[x]-moment)**2)/x
        integral += primitive_at(N+1)-primitive_at(N)
        end = N+1
        direct = sum(mass[m]*mass[n]*(F(1,max(m,n))-F(1,end))
                     for m in range(2,end+1) for n in range(2,end+1))
        T = sum(w*(logs[end]-logs[m]) for m,w in mass.items() if m <= end)
        # Cancel incrementally; coefficients are in Q[log primes].
        integral = sp.expand(integral)
        assert sp.expand(integral-direct+T*T/end) == 0
        if end in (2,3,8,16,32,36):
            loX, hiX = log_integer(end)
            lo = sum(w*max(F(0),loX-log_integer(m)[1]) for m,w in mass.items() if m<=end)
            hi = sum(w*(hiX-log_integer(m)[0]) for m,w in mass.items() if m<=end)
            lower = max(F(0),direct-hi**2/end)
            upper = direct-lo**2/end
            scaled = 10**12
            samples[end] = {"lower_floor_1e12": (scaled*lower).__floor__(),
                            "upper_ceil_1e12": (scaled*upper).__ceil__()}
    return {"thickness":1, "last_horizon":limit, "exact_symbolic_identities":limit-1,
            "profiled_energies":samples}


def pole_models():
    # Laplace variable y=log(x) for the normalized wave W=x^sigma*y^(k-1)/(k-1)!.
    # Check Mellin derivatives, the limiting Gram matrix, and sharpness on this wave.
    e, y, alpha = sp.symbols("e y alpha",positive=True)
    records = []
    for k in range(1,5):
        r = k-1
        der = (-1)**r * sp.diff(e**(-k),e,r)
        assert sp.simplify(der*e**(2*k-1)) == F(factorial(2*r),factorial(r))
        # Closed moments of exp(-e*y); the elementary recurrence is exact.
        gram = factorial(2*r)/(e+3*sp.I)**(2*r+1)
        assert sp.limit(e**(2*r+1)*gram,e,0) == 0
        b = sum((-1)**j*sp.factorial(2*r)/sp.factorial(2*r-j)*y**(2*r-j)/alpha**(j+1)
                for j in range(2*r+1))
        assert sp.simplify(sp.diff(b,y)+alpha*b-y**(2*r)) == 0
        lead = sp.expand(b).coeff(y,2*r)/factorial(r)**2
        assert sp.simplify(lead-1/(alpha*factorial(r)**2)) == 0
        critical = F(1,(2*k-1)*factorial(r)**2)
        assert sp.diff(sp.Rational(critical.numerator,critical.denominator)*y**(2*k-1),y) == y**(2*r)/factorial(r)**2
        records.append({"order":k,"coefficient_times_alpha":str(F(1,factorial(r)**2)),
                        "critical_coefficient":str(critical)})
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,help='Enterprise Math tree with the pinned verifier')
    args = parser.parse_args()
    if args.repo is not None:
        repo = args.repo
    else:
        candidates = [Path.cwd(), *Path(__file__).resolve().parents, Path('/workspace/enterprise-math')]
        repo = next((root for root in candidates if (root/VERIFIER).is_file()), None)
        if repo is None:
            parser.error('supply --repo PATH pointing to the frozen verifier tree')
    print(json.dumps({"original_unchanged_replay":replay(repo), "independent_road":check_road(),
                      "sharp_synthetic_poles":pole_models()},indent=2,ensure_ascii=False))


if __name__ == "__main__":
    main()
