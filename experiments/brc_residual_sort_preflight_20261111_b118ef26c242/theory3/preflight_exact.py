#!/usr/bin/env python3
"""Exact finite-population preflight risks. Python 3, standard library only."""
import argparse
import csv
from decimal import Decimal, localcontext
import sys
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def mass(N, K, m):
    """P(X=x), samples without replacement and uniform unordered m-set."""
    if not (0 <= K <= N and 0 <= m <= N):
        raise ValueError((N, K, m))
    den = comb(N, m)
    return [Fraction(choose(K, x) * choose(N-K, m-x), den) for x in range(m+1)]


def upper(p, c):
    return sum(p[max(0, c):], Fraction(0))


def quantile(N, K, m, alpha):
    """Reject X >= c. m+1 denotes no rejection at this sample size."""
    p = mass(N, K, m)
    return next(c for c in range(m+2) if upper(p, c) <= alpha)


@lru_cache(maxsize=None)
def conditional_reject(m1, m, early_pass, early_reject, final_reject):
    """Given total z of m observed misses, count chance of sequential rejection."""
    conditional = []
    for z in range(m+1):
        first = mass(m, z, m1)
        # The two look decision only needs first count and total count.
        conditional.append(sum((p for j, p in enumerate(first)
                                if j >= early_reject or
                                (j > early_pass and z >= final_reject)), Fraction(0)))
    return conditional


def staged(N, K, m1, m, early_pass, early_reject, final_reject):
    if not (0 <= m1 <= m <= N and -1 <= early_pass < early_reject <= m1+1):
        raise ValueError("invalid stage sizes or cutoffs")
    pfirst = mass(N, K, m1)
    ptotal = mass(N, K, m)
    conditional = conditional_reject(m1, m, early_pass, early_reject, final_reject)
    preject = sum((a*b for a, b in zip(ptotal, conditional)), Fraction(0))
    ework = m1 + (m-m1)*sum(pfirst[early_pass+1:early_reject], Fraction(0))
    return preject, ework


def exhaustive():
    cases = 0
    outcomes = 0
    for N in range(3, 11):
        m = min(N, 6)
        m1 = m//2
        for K in range(N+1):
            # Enumerate all positions of K residuals. Under exchangeability the
            # pilot occupies positions [0,m), and the first stage occupies [0,m1).
            counts = []
            for bad_positions in combinations(range(N), K):
                j = sum(pos < m1 for pos in bad_positions)
                z = sum(pos < m for pos in bad_positions)
                counts.append((j, z))
            for a, b, t in ((-1, m1+1, m//2+1), (0, m1, m//2+1),
                            (m1//2, m1+1, m//2), (-1, 1, m)):
                nr = sum(j >= b or (j > a and z >= t) for j, z in counts)
                cost = sum(m if a < j < b else m1 for j, z in counts)
                assert staged(N, K, m1, m, a, b, t) == (
                    Fraction(nr, len(counts)), Fraction(cost, len(counts)))
                cases += 1
                outcomes += len(counts)
    return cases, outcomes


def staged_example(output):
    # An illustrative exact gate, not an elapsed-time benchmark.
    n, s, e, m1, m = 100_000, 1024, 128, 64, 128
    N, Kstar = n-s, n//2-e
    alpha = Fraction(1, 100)
    q64 = quantile(N, Kstar, m1, alpha)
    q128 = quantile(N, Kstar, m, alpha)
    lo, hi = 25, quantile(N, Kstar, m1, alpha/4)
    hi_final = next(t for t in range(m//2, m+2)
                    if staged(N, Kstar, m1, m, lo, hi, t)[0] <= alpha)
    print(f"Example N={N} K*={Kstar} c64={q64} c128={q128} "
          f"early_pass<={lo} early_reject>={hi} final_reject>={hi_final}", file=sys.stderr)
    w = csv.writer(output)
    w.writerow(["n", "training_positions", "training_misses", "full_misses",
                "p_reject_64", "p_reject_128", "p_reject_staged", "E_staged_draws"])
    for total in (10000,25000,35000,40000,45000,47500,49000,50000,50001,51000,52500,
                  55000,60000,65000,70000,75000,90000):
        K = total-e
        pstage, ework = staged(N, K, m1, m, lo, hi, hi_final)
        w.writerow([n,s,e,total, f"{float(upper(mass(N,K,m1),q64)):.12g}",
                    f"{float(upper(mass(N,K,m),q128)):.12g}",
                    f"{float(pstage):.12g}",f"{float(ework):.12g}"])


def capped_draws(n, s, m, attempts):
    """Exact occupancy recursion for capped proposals, state m is absorbing."""
    N = n-s
    ways = [1] + [0]*m
    for _ in range(attempts):
        nxt = [0]*(m+1)
        for j, count in enumerate(ways[:-1]):
            nxt[j] += count*(s+j)
            nxt[j+1] += count*(N-j)
        nxt[m] += ways[m]*n
        ways = nxt
    den = n**attempts
    assert sum(ways) == den
    return Fraction(ways[m],den), Fraction(sum(j*w for j,w in enumerate(ways)),den)


def scientific(value):
    with localcontext() as context:
        context.prec = 9
        return f"{Decimal(value.numerator)/Decimal(value.denominator):.6E}"


def actual_gate(output):
    """Match phase5/probe.hpp, including incomplete draws falling through."""
    w = csv.writer(output)
    w.writerow(["n","training_positions","training_misses","full_misses","probe_count",
                "threshold","p_incomplete","p_early_given_complete","p_early",
                "p_fallthrough","expected_new_membership_tests","min_expected_saved_if_bad"])
    for n in (16384,32768,65536,100000,131072,1000000):
        s,m = 1024,64
        N,t = n-s,n//2
        c = (m*t+N-1)//N+13
        pc, work = capped_draws(n,s,m,4*m)
        totals = [t]
        if n == 100000:
            totals = [25000,40000,45000,50000,50001,52048,52049,52560,52561,
                      55000,60000,65000,70000,75000,80000,90000,95000]
        for e in (0,128,512):
            for total in totals:
                q = upper(mass(N,total-e,m),c)
                pq = pc*q
                low = pq*(t+1)-work
                w.writerow([n,s,e,total,m,c,scientific(1-pc),scientific(q),scientific(pq),
                            scientific(1-pq),scientific(work), scientific(low) if total>t else ""])


def cap_check():
    from itertools import product
    count = 0
    for n,s,m,a in ((4,1,2,4),(5,2,2,4),(5,1,3,5),(3,0,3,2)):
        # Among eligible positions choose K misses. Check factorization of
        # completion probability and every hypergeometric critical tail.
        done = 0
        total_draws = 0
        observed = [[0]*(m+2) for _ in range(n-s+1)]
        for sequence in product(range(n), repeat=a):
            keep = []
            for x in sequence:
                if x >= s and x not in keep:
                    keep.append(x)
                if len(keep) == m:
                    break
            done += len(keep)==m
            total_draws += len(keep)
            if len(keep)==m:
                for K, tails in enumerate(observed):
                    misses = sum(x < s+K for x in keep)
                    for c in range(misses+1):
                        tails[c] += 1
        pc, work = capped_draws(n,s,m,a)
        assert (pc,work) == (Fraction(done,n**a),Fraction(total_draws,n**a))
        for K, counts in enumerate(observed):
            for c, v in enumerate(counts):
                assert pc*upper(mass(n-s,K,m),c) == Fraction(v,n**a)
                count += 1
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--table", help="Write the CSV to this file")
    parser.add_argument("--staged-example", action="store_true",
                        help="Optional 64/128 theoretical design, not the timed kernel")
    args = parser.parse_args()
    cases, outcomes = exhaustive()
    print(f"exact exhaustive checks: {cases} configurations, {outcomes} "
          "binary population/decision-rule pairs", file=sys.stderr)
    print(f"cap checks: {cap_check()} exact rejection probabilities", file=sys.stderr)
    writer = staged_example if args.staged_example else actual_gate
    if args.table:
        with open(args.table, "w", encoding="utf-8", newline="") as f:
            writer(f)
    else:
        writer(sys.stdout)
