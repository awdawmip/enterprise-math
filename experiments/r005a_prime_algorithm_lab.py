#!/usr/bin/env python3
"""R005-A exact bounded prime-algorithm research harness.

Research-only, standard-library implementation. This is not a production
primality package and does not create a canonical shared API.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import gcd, isqrt, log2, sqrt
from typing import Callable, Dict, Iterable, List, Mapping, Sequence, Set, Tuple
import json


# ---------------------------------------------------------------------------
# Exact baseline oracle and sieves
# ---------------------------------------------------------------------------

def is_prime_exact(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    d = 3
    r = isqrt(n)
    while d <= r:
        if n % d == 0:
            return False
        d += 2
    return True


def sieve_eratosthenes(limit: int, *, with_counts: bool = False):
    if limit < 2:
        return ([], {"mark_attempts": 0, "new_marks": 0}) if with_counts else []
    a = bytearray(b"\x01") * (limit + 1)
    a[0:2] = b"\x00\x00"
    mark_attempts = 0
    new_marks = 0
    for p in range(2, isqrt(limit) + 1):
        if not a[p]:
            continue
        for m in range(p * p, limit + 1, p):
            mark_attempts += 1
            if a[m]:
                a[m] = 0
                new_marks += 1
    primes = [i for i, v in enumerate(a) if v]
    if with_counts:
        return primes, {"mark_attempts": mark_attempts, "new_marks": new_marks}
    return primes


def wheel_survivors(limit: int, wheel_primes: Sequence[int] = (2, 3, 5)) -> List[int]:
    """Static wheel baseline: candidates coprime to the wheel product.

    This is deliberately only the wheel-filter stage; it is not itself a
    primality decision procedure.
    """
    M = 1
    for p in wheel_primes:
        M *= p
    small = {p for p in wheel_primes if p <= limit}
    return sorted(small | {n for n in range(2, limit + 1) if gcd(n, M) == 1})


def sieve_atkin(limit: int, *, with_counts: bool = False):
    if limit < 2:
        return ([], {"toggles": 0, "square_cleanups": 0}) if with_counts else []
    a = bytearray(limit + 1)
    root = isqrt(limit)
    toggles = 0
    for x in range(1, root + 1):
        x2 = x * x
        for y in range(1, root + 1):
            y2 = y * y
            n = 4 * x2 + y2
            if n <= limit and n % 12 in (1, 5):
                a[n] ^= 1
                toggles += 1
            n = 3 * x2 + y2
            if n <= limit and n % 12 == 7:
                a[n] ^= 1
                toggles += 1
            if x > y:
                n = 3 * x2 - y2
                if n <= limit and n % 12 == 11:
                    a[n] ^= 1
                    toggles += 1

    square_cleanups = 0
    for p in range(5, root + 1):
        if a[p]:
            step = p * p
            for m in range(step, limit + 1, step):
                if a[m]:
                    a[m] = 0
                    square_cleanups += 1

    primes: List[int] = []
    if limit >= 2:
        primes.append(2)
    if limit >= 3:
        primes.append(3)
    primes.extend(i for i in range(5, limit + 1) if a[i])
    if with_counts:
        return primes, {"toggles": toggles, "square_cleanups": square_cleanups}
    return primes


def segmented_primes(lo: int, hi: int) -> List[int]:
    if hi < lo or hi < 2:
        return []
    lo = max(lo, 2)
    base = sieve_eratosthenes(isqrt(hi))
    a = bytearray(b"\x01") * (hi - lo + 1)
    for p in base:
        start = max(p * p, ((lo + p - 1) // p) * p)
        for m in range(start, hi + 1, p):
            a[m - lo] = 0
    return [lo + i for i, v in enumerate(a) if v]


# ---------------------------------------------------------------------------
# Prime-sound observation/support model
# ---------------------------------------------------------------------------

Predicate = Callable[[int], bool]  # True = PASS / prime-like


def rejection_support(domain: Iterable[int], predicate: Predicate) -> Set[int]:
    return {n for n in domain if not predicate(n)}


def pseudoprime_fiber(composites: Iterable[int], predicates: Iterable[Predicate]) -> Set[int]:
    preds = list(predicates)
    return {n for n in composites if all(f(n) for f in preds)}


def is_prime_sound(primes: Iterable[int], predicate: Predicate) -> bool:
    return all(predicate(p) for p in primes)


def witness_cover_is_safe(
    primes: Iterable[int],
    composites: Iterable[int],
    predicates: Iterable[Predicate],
) -> bool:
    preds = list(predicates)
    return all(is_prime_sound(primes, f) for f in preds) and not pseudoprime_fiber(composites, preds)


def decision_signature(n: int, predicates: Sequence[Predicate]) -> Tuple[bool, ...]:
    return tuple(f(n) for f in predicates)


def signature_fibers(domain: Iterable[int], predicates: Sequence[Predicate]):
    out: Dict[Tuple[bool, ...], List[int]] = {}
    for n in domain:
        out.setdefault(decision_signature(n, predicates), []).append(n)
    return out


def minimum_safe_subsets(
    composites: Sequence[int],
    named_predicates: Mapping[int, Predicate],
) -> List[Tuple[int, ...]]:
    """Exact bounded minimum set-cover search over candidate witnesses."""
    names = list(named_predicates)
    rejects = {
        a: {n for n in composites if not named_predicates[a](n)}
        for a in names
    }
    universe = set(composites)
    for k in range(1, len(names) + 1):
        safe: List[Tuple[int, ...]] = []
        for subset in combinations(names, k):
            covered: Set[int] = set()
            for a in subset:
                covered |= rejects[a]
                if covered == universe:
                    break
            if covered == universe:
                safe.append(subset)
        if safe:
            return safe
    return []


# ---------------------------------------------------------------------------
# Root-factor horizon
# ---------------------------------------------------------------------------

def root_factor_pass(n: int, p: int) -> bool:
    return not (p * p <= n and n % p == 0)


def root_factor_basis(N: int) -> List[int]:
    return sieve_eratosthenes(isqrt(N))


def verify_root_factor_basis(N: int) -> Dict[str, object]:
    basis = root_factor_basis(N)
    domain = list(range(2, N + 1))
    primes = [n for n in domain if is_prime_exact(n)]
    composites = [n for n in domain if not is_prime_exact(n)]
    preds = [lambda n, p=p: root_factor_pass(n, p) for p in basis]
    safe = witness_cover_is_safe(primes, composites, preds)
    omission_counterexamples = {}
    for p in basis:
        reduced = [q for q in basis if q != p]
        collision = p * p
        assert collision <= N
        assert all(root_factor_pass(collision, q) for q in reduced)
        omission_counterexamples[p] = collision
    return {
        "N": N,
        "basis": basis,
        "safe": safe,
        "omission_counterexamples": omission_counterexamples,
    }


# ---------------------------------------------------------------------------
# Fermat and Miller-Rabin
# ---------------------------------------------------------------------------

def fermat_probable_prime(n: int, a: int) -> bool:
    if n == a:
        return True
    if n < 2 or gcd(a, n) != 1:
        return False
    return pow(a, n - 1, n) == 1


def miller_rabin_strong(n: int, a: int) -> bool:
    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False
    a %= n
    if a in (0, 1):
        return True
    if gcd(a, n) != 1:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    x = pow(a, d, n)
    if x in (1, n - 1):
        return True
    for _ in range(s - 1):
        x = (x * x) % n
        if x == n - 1:
            return True
    return False


def mr_bounded_experiment(N: int, bases: Sequence[int]) -> Dict[str, object]:
    composites = [n for n in range(3, N + 1, 2) if not is_prime_exact(n)]
    named = {a: (lambda n, a=a: miller_rabin_strong(n, a)) for a in bases}
    pseudo = {a: [n for n in composites if named[a](n)] for a in bases}
    minimum = minimum_safe_subsets(composites, named)
    return {
        "N": N,
        "bases": list(bases),
        "odd_composites": len(composites),
        "pseudoprime_counts": {str(a): len(v) for a, v in pseudo.items()},
        "first_pseudoprime": {str(a): (v[0] if v else None) for a, v in pseudo.items()},
        "minimum_safe_subsets": [list(x) for x in minimum],
        "minimum_cardinality": len(minimum[0]) if minimum else None,
        "witness_evaluations": len(composites) * len(bases),
    }


# ---------------------------------------------------------------------------
# Strong Lucas-Selfridge reference observer
# ---------------------------------------------------------------------------

def jacobi(a: int, n: int) -> int:
    if n <= 0 or n % 2 == 0:
        raise ValueError("Jacobi denominator must be positive odd")
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def matmul2(A, B, mod: int):
    return (
        (
            (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod,
            (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod,
        ),
        (
            (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod,
            (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod,
        ),
    )


def matpow2(M, k: int, mod: int):
    R = ((1, 0), (0, 1))
    while k:
        if k & 1:
            R = matmul2(R, M, mod)
        M = matmul2(M, M, mod)
        k >>= 1
    return R


def lucas_uvq_mod(P: int, Q: int, k: int, n: int) -> Tuple[int, int, int]:
    if k == 0:
        return 0, 2 % n, 1 % n
    M = ((P % n, (-Q) % n), (1, 0))
    Mk = matpow2(M, k, n)
    U_k = Mk[1][0] % n
    U_k1 = Mk[0][0] % n
    V_k = (2 * U_k1 - P * U_k) % n
    return U_k, V_k, pow(Q, k, n)


def selfridge_D(n: int):
    D = 5
    while True:
        g = gcd(abs(D), n)
        if 1 < g < n:
            return None
        if jacobi(D, n) == -1:
            return D, 1, (1 - D) // 4
        D = -(abs(D) + 2) if D > 0 else abs(D) + 2


def strong_lucas_selfridge(n: int) -> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    r = isqrt(n)
    if r * r == n:
        return False
    params = selfridge_D(n)
    if params is None:
        return False
    D, P, Q = params
    if gcd(n, 2 * Q * D) != 1:
        return n in (abs(Q), abs(D))
    d = n + 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    U, V, Qk = lucas_uvq_mod(P, Q, d, n)
    if U == 0 or V == 0:
        return True
    for _ in range(1, s):
        V = (V * V - 2 * Qk) % n
        Qk = (Qk * Qk) % n
        if V == 0:
            return True
    return False


def lucas_bounded_experiment(N: int) -> Dict[str, object]:
    odd_primes = [p for p in range(3, N + 1, 2) if is_prime_exact(p)]
    prime_failures = [p for p in odd_primes if not strong_lucas_selfridge(p)]
    composites = [n for n in range(3, N + 1, 2) if not is_prime_exact(n)]
    pseudo = [n for n in composites if strong_lucas_selfridge(n)]
    mr2 = [n for n in composites if miller_rabin_strong(n, 2)]
    return {
        "N": N,
        "prime_failures": prime_failures,
        "pseudoprime_count": len(pseudo),
        "first_pseudoprimes": pseudo[:20],
        "mr2_intersection": sorted(set(pseudo) & set(mr2)),
        "example_mr2_only_2047": {
            "mr2": miller_rabin_strong(2047, 2),
            "lucas": strong_lucas_selfridge(2047),
        },
        "example_lucas_only_5459": {
            "mr2": miller_rabin_strong(5459, 2),
            "lucas": strong_lucas_selfridge(5459),
        },
    }


# ---------------------------------------------------------------------------
# Tiny exact AKS reference: intentionally small-domain only
# ---------------------------------------------------------------------------

def is_perfect_power(n: int) -> bool:
    if n < 4:
        return False
    for b in range(2, n.bit_length() + 1):
        a0 = int(round(n ** (1.0 / b)))
        for a in range(max(2, a0 - 2), a0 + 3):
            if a ** b == n:
                return True
    return False


def euler_phi(n: int) -> int:
    result = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            result -= result // p
        p += 1
    if x > 1:
        result -= result // x
    return result


def order_exceeds(n: int, r: int, bound: int) -> bool:
    if gcd(n, r) != 1:
        return False
    x = 1
    for _ in range(1, bound + 1):
        x = (x * n) % r
        if x == 1:
            return False
    return True


def poly_mul_cyclic(A: List[int], B: List[int], mod: int, r: int) -> List[int]:
    C = [0] * r
    for i, ai in enumerate(A):
        if ai == 0:
            continue
        for j, bj in enumerate(B):
            if bj:
                C[(i + j) % r] = (C[(i + j) % r] + ai * bj) % mod
    return C


def poly_pow_x_plus_a(a: int, exponent: int, mod: int, r: int) -> List[int]:
    base = [0] * r
    base[0] = a % mod
    base[1 % r] = (base[1 % r] + 1) % mod
    out = [0] * r
    out[0] = 1
    e = exponent
    while e:
        if e & 1:
            out = poly_mul_cyclic(out, base, mod, r)
        base = poly_mul_cyclic(base, base, mod, r)
        e >>= 1
    return out


def aks_reference(n: int) -> bool:
    if n < 2:
        return False
    if is_perfect_power(n):
        return False
    L = max(1, int(log2(n)) ** 2)
    r = 2
    while not order_exceeds(n, r, L):
        r += 1
    for a in range(2, min(r, n - 1) + 1):
        g = gcd(a, n)
        if 1 < g < n:
            return False
    if n <= r:
        return True
    A = int(sqrt(euler_phi(r)) * log2(n))
    for a in range(1, A + 1):
        lhs = poly_pow_x_plus_a(a, n, n, r)
        rhs = [0] * r
        rhs[0] = a % n
        rhs[n % r] = (rhs[n % r] + 1) % n
        if lhs != rhs:
            return False
    return True


# ---------------------------------------------------------------------------
# Pratt certificates
# ---------------------------------------------------------------------------

def factorization(n: int) -> Dict[int, int]:
    out: Dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


@dataclass
class PrattCertificate:
    p: int
    witness: int | None
    factors: Dict[int, int]
    children: Dict[int, "PrattCertificate"]


def make_pratt_certificate(p: int) -> PrattCertificate:
    if not is_prime_exact(p):
        raise ValueError(f"{p} is not prime")
    if p == 2:
        return PrattCertificate(2, None, {}, {})
    fac = factorization(p - 1)
    children = {q: make_pratt_certificate(q) for q in fac}
    witness = None
    for a in range(2, p):
        if pow(a, p - 1, p) == 1 and all(
            pow(a, (p - 1) // q, p) != 1 for q in fac
        ):
            witness = a
            break
    if witness is None:
        raise AssertionError(f"no Pratt witness found for prime {p}")
    return PrattCertificate(p, witness, fac, children)


def verify_pratt_certificate(cert: PrattCertificate) -> bool:
    p = cert.p
    if p == 2:
        return cert.witness is None and not cert.factors and not cert.children
    if p < 2 or cert.witness is None:
        return False
    product = 1
    for q, e in cert.factors.items():
        if q not in cert.children or e <= 0:
            return False
        if not verify_pratt_certificate(cert.children[q]):
            return False
        product *= q ** e
    if product != p - 1:
        return False
    a = cert.witness
    return pow(a, p - 1, p) == 1 and all(
        pow(a, (p - 1) // q, p) != 1 for q in cert.factors
    )


def pratt_stats(cert: PrattCertificate) -> Dict[str, int]:
    seen: Set[int] = set()
    def visit(c: PrattCertificate, depth: int):
        if c.p in seen:
            return depth, 0
        seen.add(c.p)
        max_depth = depth
        max_branch = len(c.children)
        for child in c.children.values():
            d, b = visit(child, depth + 1)
            max_depth = max(max_depth, d)
            max_branch = max(max_branch, b)
        return max_depth, max_branch
    depth, max_branch = visit(cert, 0)
    return {"nodes": len(seen), "depth": depth, "max_branching": max_branch}


# ---------------------------------------------------------------------------
# Structural boundary probes
# ---------------------------------------------------------------------------

def atkin_representations(n: int) -> List[Tuple[str, int, int]]:
    reps = []
    r = isqrt(n)
    for x in range(1, r + 1):
        for y in range(1, r + 1):
            if 4 * x * x + y * y == n and n % 12 in (1, 5):
                reps.append(("4x^2+y^2", x, y))
            if 3 * x * x + y * y == n and n % 12 == 7:
                reps.append(("3x^2+y^2", x, y))
            if x > y and 3 * x * x - y * y == n and n % 12 == 11:
                reps.append(("3x^2-y^2", x, y))
    return reps


def segmented_boundary_example(p: int = 5) -> Dict[str, object]:
    def first_mark(lo: int, hi: int):
        m = max(p * p, ((lo + p - 1) // p) * p)
        return m if m <= hi else None
    return {
        "p": p,
        "segment_A": [10, 14],
        "segment_B": [25, 29],
        "same_L_mod_p": (10 % p) == (25 % p),
        "first_mark_A": first_mark(10, 14),
        "first_mark_B": first_mark(25, 29),
    }


def wheel_future_state_example() -> Dict[str, object]:
    M = 6
    return {
        "modulus": M,
        "n1": 1,
        "n2": 5,
        "both_initially_survive": gcd(1, M) == gcd(5, M) == 1,
        "delta": 2,
        "n1_plus_delta_survives": gcd(3, M) == 1,
        "n2_plus_delta_survives": gcd(7, M) == 1,
    }


def fermat_mr_partition_boundary() -> Dict[str, object]:
    return {
        "341": {
            "fermat2": fermat_probable_prime(341, 2),
            "mr2": miller_rabin_strong(341, 2),
        },
        "9": {
            "fermat2": fermat_probable_prime(9, 2),
            "mr2": miller_rabin_strong(9, 2),
        },
    }


# ---------------------------------------------------------------------------
# Main checkpoint
# ---------------------------------------------------------------------------

def run_checkpoint(
    mr_N: int = 100_000,
    lucas_N: int = 100_000,
    aks_N: int = 120,
) -> Dict[str, object]:
    sieve_checks = {}
    for N in (100, 1_000, 100_000):
        e = sieve_eratosthenes(N)
        a = sieve_atkin(N)
        sieve_checks[str(N)] = {"equal": e == a, "prime_count": len(e)}

    seg = segmented_primes(99_900, 100_100)
    global_ref = [p for p in sieve_eratosthenes(100_100) if p >= 99_900]
    primes_100, era_counts = sieve_eratosthenes(100, with_counts=True)
    _, atkin_counts = sieve_atkin(100, with_counts=True)
    root = verify_root_factor_basis(1_000)
    mr = mr_bounded_experiment(mr_N, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29))
    lucas = lucas_bounded_experiment(lucas_N)
    aks_mismatches = [n for n in range(2, aks_N + 1) if aks_reference(n) != is_prime_exact(n)]

    cert_examples = {}
    for p in (3, 5, 7, 97, 997, 4999):
        cert = make_pratt_certificate(p)
        cert_examples[str(p)] = {
            "valid": verify_pratt_certificate(cert),
            "witness": cert.witness,
            **pratt_stats(cert),
        }

    reps65 = atkin_representations(65)
    result = {
        "status": "R005-A research checkpoint / non-canonical",
        "prime_list_100": primes_100,
        "wheel_survivors_100_for_2_3_5": wheel_survivors(100),
        "baseline": {
            "sieve_cross_checks": sieve_checks,
            "segmented_cross_check": seg == global_ref,
            "eratosthenes_operation_counts_N100": era_counts,
            "atkin_operation_counts_N100": atkin_counts,
        },
        "root_factor": root,
        "fermat_mr_partition_boundary": fermat_mr_partition_boundary(),
        "miller_rabin": mr,
        "lucas_selfridge": lucas,
        "aks": {"N": aks_N, "mismatches_vs_exact_oracle": aks_mismatches},
        "pratt_certificates": cert_examples,
        "negative_boundaries": {
            "pure_divisibility_collision": {
                "2": [2 % 2 == 0],
                "4": [4 % 2 == 0],
                "note": "A raw divisibility bit cannot distinguish p from p^2.",
            },
            "atkin_requires_xor": {
                "n": 65,
                "representations": reps65,
                "toggle_count": len(reps65),
                "is_prime": is_prime_exact(65),
            },
            "segmented_activation_context": segmented_boundary_example(),
            "wheel_output_vs_future_state": wheel_future_state_example(),
        },
    }

    assert all(v["equal"] for v in sieve_checks.values())
    assert result["baseline"]["segmented_cross_check"]
    assert root["safe"]
    assert not aks_mismatches
    assert not lucas["prime_failures"]
    assert all(v["valid"] for v in cert_examples.values())
    assert len(reps65) == 2
    assert result["fermat_mr_partition_boundary"]["341"] == {
        "fermat2": True,
        "mr2": False,
    }
    return result


if __name__ == "__main__":
    print(json.dumps(run_checkpoint(), ensure_ascii=False, indent=2))
