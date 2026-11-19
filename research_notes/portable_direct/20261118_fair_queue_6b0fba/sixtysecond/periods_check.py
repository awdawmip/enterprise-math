"""Rebuild the integer thresholds and distinguish sampled powers by their actual equalities."""
import argparse
from fractions import Fraction
from itertools import combinations
import json
from math import floor, fsum, isqrt, lcm, log, prod
import sys


def primes_to(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[:2] = bytes(2)
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((n-p*p)//p + 1)
    return [p for p in range(2, n+1) if sieve[p]]


def thresholds_by_subsets(q):
    """No assumptions about the shape of optimal reciprocal denominator sets."""
    best = {}
    for k in range(2, q+1):
        for ds in combinations(range(1, q+1), k):
            ell = lcm(*ds)
            for allow in (0, 1):
                key = (k, allow)
                horizon = ell//ds[allow]
                if key not in best or horizon < best[key][0]:
                    best[key] = (horizon, ds, 1)
                elif horizon == best[key][0]:
                    value, witness, ties = best[key]
                    best[key] = (value, witness, ties+1)
    return best


def direct_order_test(q, h, k, allow):
    """Enumerate actual target orders and the one possible outside label."""
    for outside_count in range(allow + 1):
        for inside in combinations(range(1, h+1), k-outside_count):
            if not inside:
                continue
            candidates = range(h+1, q*min(inside)+1) if outside_count else (None,)
            for outside in candidates:
                rs = inside + (outside,) if outside_count else inside
                if lcm(*rs) <= q*min(rs):
                    return True
    return False


def greedy(q, deletions, primes):
    used = 0
    selected = []
    for p in reversed(primes):
        if p <= isqrt(q):
            break
        cost = q//p
        if used + cost > deletions:
            return selected, p
        used += cost
        selected.append(p)
    return selected, 1


def power_blocks(positions, base, modulus):
    groups = {}
    for i in positions:
        groups.setdefault(pow(base, i, modulus), []).append(i)
    return sorted(groups.values())


def arithmetic_examples(native):
    # 5 generates F_97^*, demonstrated by testing all its powers.
    assert len({pow(5, j, 97) for j in range(96)}) == 96
    support = [0, 1, 2, 24, 25, 26]
    periods = [3, 4, 6, 8, 12, 24]
    bases = [pow(5, 96//r, 97) for r in periods]
    blocks = [[0, 24], [1, 25], [2, 26]]
    if native:
        sys.path.insert(0, native)
        from enterprise_math.group_ring_sparse_identifiability import labeled_collision_gcd
    for r, g in zip(periods, bases):
        assert len({pow(g, i, 97) for i in range(r)}) == r and pow(g, r, 97) == 1
        assert power_blocks(support, g, 97) == blocks
        if native:
            c = labeled_collision_gcd(97, g, support, 47)
            assert (c.gcd_multiple, c.observed_atoms, c.residue_buckets, c.repeated_residues) == (24, 6, 3, 3)
    return {"positions": support, "orders": periods, "bases_mod_97": bases, "common_partition": blocks}


def analytic_coefficients(lam):
    # Exact rational comparison assigns the derivative on the right at a corner.
    j, harmonic = 1, Fraction(1)
    while lam > harmonic - Fraction(j, j+1):
        j += 1
        harmonic += Fraction(1, j)
    y = (harmonic - lam)/j
    yf = float(y)
    integral = fsum(((1/i)*log(1/i) - 1/i) - (yf*log(yf)-yf) for i in range(1, j+1))
    return str(y), j, -integral/j


def large_examples():
    rows = []
    for q in (100_000, 1_000_000):
        primes = primes_to(q)
        psi = fsum(log(p) for p in primes)
        # Add higher powers to theta, visiting no composite non-prime-power.
        for p in primes:
            if p > isqrt(q):
                break
            power = p*p
            while power <= q:
                psi += log(p)
                power *= p
        for lam in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(5, 6), Fraction(1), Fraction(2)):
            r = floor(float(lam)*q/log(q))
            selected, next_prime = greedy(q, r, primes)
            y, right, second = analytic_coefficients(lam)
            upper = (psi - fsum(log(p) for p in selected) - log(2))/q
            rows.append({"Q": q, "lambda": str(lam), "r": r, "first_prime_that_exceeds_budget": next_prime,
                         "eligible_large_primes_removed": len(selected), "log_H_over_Q_constructive_upper_approx": round(upper, 8),
                         "y": y, "right_slope_magnitude": right, "second_coefficient_approx": round(second, 8),
                         "two_term_approx": round(float(Fraction(y)) + second/log(q), 8)})
    return rows


def main(native):
    counters = {"denominator_subsets": 0, "order_threshold_comparisons": 0, "exact_formula_comparisons": 0,
                "greedy_interval_checks": 0}
    counterexamples = {}
    exceptional_ties = []
    for q in range(2, 19):
        ps = primes_to(q)
        best = thresholds_by_subsets(q)
        counters["denominator_subsets"] += 2**q - q - 1
        all_lcm = lcm(*range(1, q+1))
        upper_primes = [p for p in reversed(ps) if 2*p > q]
        small_prime_part = 1
        for p in ps:
            if p*p > q:
                break
            a = p
            while a*p <= q:
                a *= p
            small_prime_part *= a
        for (k, allow), (val, ds, ties) in best.items():
            r = q-k
            if q <= 9:
                for h in range(1, 10):
                    assert (val <= h) == direct_order_test(q, h, k, allow)
                    counters["order_threshold_comparisons"] += 1
            if r <= len(upper_primes):
                assert val == all_lcm//((1+allow)*prod(upper_primes[:r]))
                counters["exact_formula_comparisons"] += 1
                if ties > 1:
                    exceptional_ties.append((q, r, 1+allow, ties))
            if q >= 8:
                selected, _ = greedy(q, r, ps)
                factor = prod(selected)
                assert all_lcm <= val*q*small_prime_part*factor
                assert val*(1+allow)*factor <= all_lcm
                counters["greedy_interval_checks"] += 1
            if allow and r == len(upper_primes)+1 and r <= len(ps):
                prediction = Fraction(all_lcm, 2*prod(list(reversed(ps))[:r]))
                if prediction != val:
                    entry = {"Q": q, "r": r, "naive": str(prediction),
                             "exact": val, "optimal_denominators": ds}
                    counterexamples.setdefault("first_all_Q", entry)
                    if q >= 8:
                        counterexamples.setdefault("first_Q_at_least_8", entry)
    assert exceptional_ties == [(3, 1, 2, 2)]
    assert counterexamples["first_all_Q"]["Q"] == 6
    assert counterexamples["first_Q_at_least_8"]["Q"] == 8
    return {"verification_counts": counters, "beyond_upper_half_counterexamples": counterexamples,
            "ties_within_theorem": exceptional_ties,
            "same_labelled_readout": arithmetic_examples(native), "asymptotic_comparisons": large_examples()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--native-src", help="path to the frozen enterprise-math src directory for extra cross-checks")
    print(json.dumps(main(parser.parse_args().native_src), ensure_ascii=False, indent=2))
