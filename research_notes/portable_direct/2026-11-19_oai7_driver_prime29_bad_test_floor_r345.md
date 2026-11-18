# OAI7 r345 — Exact universal 29-point bad-test floor and affine classification

Date: 2026-11-19. Status: a proved finite-domain combinatorial result, with complete executable orbit enumeration and a second direct-count crosscheck. Author-side driver research evidence, not a frozen Native Result or an independent Native review. The original OAI7 contributor EM-EMF6D046-5A2844, r307, and r329–r344 retain their source/provenance. This calculation uses the external finite cyclic group model; no native X6 transfer is asserted.

## Proposition (p=29, n=5, u=4, h=0)

Let G=Z/29Z. For any probability distribution of 5-element sets C in G, define V_C(K) as the number of x in G with (x+C) disjoint from a deterministic 4-set K, and

    q = max_{|K|=4} Pr_C{ V_C(K) > 29^(3/4) }.

Then, **for every distribution of C**,

    q >= 50/91 = 450/819 = 0.549450549450... .                     (345.1)

If the distribution is uniform on 29 labeled rows (including any exactly 5-regular codebook with 29 rows), then its failure probability is a multiple of 1/29 and

    q >= 16/29.                                                     (345.2)

The minimum, over deterministic 5-subsets C, of the proportion of failing 4-subsets K is exactly 50/91. Equality occurs precisely when C belongs to the affine orbit

    C = a{0,1,2,3,5}+t,   a in F_29^*, t in F_29.                   (345.3)

There are 28 translation classes at equality (the 28 nonzero multipliers give distinct translation classes), hence 812 distinct sets attaining the minimum.

The bound improves the universal finite p=29 averaging bound 38/663 of r344, but (345.1) is a lower bound on worst-test failure, not a claim that 50/91 is the achievable minimax failure of a balanced ensemble. The r344 29-row regular construction with q=24/29 remains a verified strict improvement over a single translation orbit.

## Proof, exhaustive finite classification

For h=0, V_C(K)=29-|K-C|. Since 12 < 29^(3/4) < 13, a test K fails exactly when |K-C| <=16. Translating C or K preserves |K-C|. Because 29 is prime and 0<|C|,|K|<29, no nonzero translation fixes a set, so each translation orbit has exactly 29 elements. There are therefore binom(29,5)/29=4095 translation classes of C and binom(29,4)/29=819 classes of K.

The exact enumerator below examines every pair of classes: 4095 x 819 = 3,353,805 decisions, each an exact integer 29-bit rotation/union/cardinality computation. It certifies that the number B(C) of bad K translation classes satisfies B(C)>=450 for every C. It also identifies exactly 28 minimizing C classes and checks that they are the complete multiplicative/affine orbit of {0,1,2,3,5}. No probabilistic sampling or floating-point threshold enters this proof.

Consequently for each C, Pr_{uniform K}(bad)>=450/819. Average this inequality over the arbitrary distribution of C. Since max_K Pr_C(bad) is at least the mean over K, (345.1) follows. For 29 equiprobable rows, multiplying (345.1) by 29 gives 1450/91, whose ceiling is 16, establishing (345.2). The 28 orbit-class minimizers supply (345.3).

## Standalone reproducible certificate (Python 3 standard library)

    from itertools import combinations
    from collections import Counter

    P = 29
    FULL = (1 << P) - 1

    def rot(m, d):
        d %= P
        return ((m << d) | (m >> (P - d))) & FULL if d else m

    def bits(values):
        return sum(1 << x for x in values)

    def reps(k):
        return sorted({
            min(rot(bits(C), d) for d in range(P))
            for C in combinations(range(P), k)
        })

    C5 = reps(5)
    K4 = reps(4)
    assert len(C5) == 4095 and len(K4) == 819

    k_shifts = [[rot(K, -s) for s in range(P)] for K in K4]
    counts = Counter()
    minimum = len(K4)
    minimizers = []

    for C in C5:
        S = [i for i in range(P) if (C >> i) & 1]
        assert len(S) == 5
        bad = sum(
            (a[S[0]] | a[S[1]] | a[S[2]] | a[S[3]] | a[S[4]]).bit_count() <= 16
            for a in k_shifts
        )
        counts[bad] += 1
        if bad < minimum:
            minimum, minimizers = bad, [C]
        elif bad == minimum:
            minimizers.append(C)

    W = (0, 1, 2, 3, 5)
    affine_classes = {
        min(rot(bits((a*x) % P for x in W), d) for d in range(P))
        for a in range(1, P)
    }
    assert minimum == 450
    assert len(minimizers) == 28
    assert set(minimizers) == affine_classes
    assert counts[450] == 28
    assert sum(counts.values()) == 4095

    # Independent direct check of one extremal C against every 4-set.
    direct_bad = sum(
        len({(k-c) % P for k in K for c in W}) <= 16
        for K in combinations(range(P), 4)
    )
    assert direct_bad == 13050 == minimum * P
    print("C-orbits 4095; K-orbits 819; minimum 450; affine classes 28")
    print("universal q lower bound 50/91; 29-row bound 16/29")

### Verification record

The orbit enumeration was executed in the present driver research context: 4095 C classes, 819 K classes, minimum B(C)=450, exactly 28 minimizers, and exact equality of the minimizer-class set with all 28 scalar images of W. Separately, all 23,751 original K were enumerated directly for W, yielding exactly 13,050 failing tests = 450 x 29. r344's published 29-row construction was independently rerun, reproducing its full 14-bin histogram, its regular incidence degrees (5 each), and q=24/29.

### Scientific significance and remaining direction

This is a **universal finite-parameter obstruction**, stronger than the r344 first-moment hypergeometric lower bound, and it applies even to randomized and balanced codebooks. Its proof does not preclude q_p -> 0 in the growing-prime sharp-second-order regime; that is the distinct asymptotic mother question. A useful next investigation is the gap between 16/29 and the current 24/29 exact regular construction in this finite testbed, as well as analytic bounds in a growing-prime regime.

Sources: r344 at enterprise-math@6d5b98d14202cefb37f34565c68c3d49755430d7, research_notes/portable_direct/2026-11-19_oai7_driver_hypergeometric_average_prime29_regular_mix_r344.md. Parent OAI7 Task RS-OAI7-028-C-20261007-6F2A81, immutable publication TP2-96FAC49786245691AE19. This Driver context shares prior author-side scientific material and does not assert independent decisive review or Native admission.
