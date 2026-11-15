# EC49FPR — Exact mixed-observation optimum with half-price named-root readouts

Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent portable research (2026-11-15). No formal Task CLAIM, Result or Review.

## Immutable scientific population

Frozen native BRC science pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Original master SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e. Native rooted Trie cost table SHA256: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f. The exact input comes from the prior verified EC49FPQ archive. The original complete legal-root class represented by configuration 16995 has 242 original configurations, 112 distinct rooted cost profiles, 324 full-allocation terminal scalar probes and 96 named-root/optional-demand-subset scalar probes. The 420 actions yield 395 distinct exact-response partitions on 112 profiles.

A policy adaptively chooses the next scalar probe based on exact integer previous responses until its profile is uniquely identified. Its prior is uniform on 112 distinct rooted profiles, with no imposed maximum tree depth. Set a terminal probe price t=1 and a named-root probe price r=1/2.

## Theorem — Global minimum expected price

For this precisely defined finite problem, the minimum possible expected price is **37/28 terminal-price units**. Two globally minimizing initial original-action indices are:

- 346: named root 5, optional-demand subset bitmask 557056;
- 354: named root 6, optional-demand subset bitmask 2228224.

A complete deterministic witness tree has total scaled price 296 over 112 rooted profiles, when each terminal costs 2 and each root probe costs 1. The exact histogram (scaled price, number of profiles) is (1,3), (2,50), (3,47), (4,8), (5,4). Thus the minimum original-price expectation equals 296/(2*112)=37/28. The earlier terminal-only unrestricted optimum was 119/56, so the exact saving is 45/56 terminal-price units.

For a different prior uniform on the original 242 source configurations, the same exact tree is a **feasible strategy** with scaled total 850 and expected original-price cost 425/242. The optimum for this prior remains open.

## Finite exhaustive proof

Index distinct rooted profiles 0 through 111. For a nonempty subset S, let n(S) be its cardinality and let P_a(S) be the partition into the exact integer-response fibers for an available original action a. In scaled units set c_a=1 for rooted/subset probes and c_a=2 for terminal probes. Define C(S) as the minimum *total scaled price*, summed over the candidate profiles in S, of a certain-to-identify adaptive strategy. For every singleton, C({h})=0. For larger S:

    C(S) = min_{a: |P_a(S)|>1} [ c_a*n(S) + sum_{F in P_a(S), |F|>1} C(F) ].

All nonsingleton fibers on the right are proper subsets of S. Induction on |S| proves that the recursion is exact and terminates. Uninformative actions cannot improve any strategy because they charge a positive price without shrinking S. Equal full-domain partitions induce equal restrictions on every S; selecting the cheaper original action is valid. The verifier explicitly deduplicates all 420 action partitions into 395 classes, retaining original action keys and their prices.

The prior valid terminal-only decision tree supplies a valid upper bound for every S. For pruning, a rigorous action lower bound is:

    L_a(S) = c_a*n(S) + sum_{F in P_a(S), |F|>1} n(F).

Each nonsingleton child needs at least one further observation at scaled price at least 1. Candidates with L_a(S) not below the incumbent, or partial exact costs already at least the incumbent, cannot improve it. Exact integer Bellman optimization visited 16,347 subset masks and yielded C(FULL)=296. The verifier checks all initial actions, constructs a minimizing response-labelled tree and explicitly walks every one of the 112 rooted profiles, checking the original integer outcomes, unique leaves, histogram and total price. This supplies a matching global lower and constructive upper certificate.

## Reproduction and next questions

Run: python3 VERIFY_EC49FPR.py <prior_EC49FPQ_EVIDENCE_dir> EC49FPR_HALF_ROOT_MACHINE_CERT.json

The directory contains frozen_original_master.txt, EC49FPG_PROFILE.csv, EC49FPL_CERTIFICATE.json and EC49FPN_CERTIFICATE.json. The verifier checks native input hashes, reparses the original 38,169 configurations and 94 families, reconstructs the complete class and its scalar observations, and writes a complete exact-cost decision tree and every initial-action cost. Calculation uses Python arbitrary-precision integers and original native Trie cost measurements. It introduces no classical propagator or new native-physics interpretation.

Next: exact source-configuration-weighted optimum at root price 1/2, then parametric price breakpoints on 0<r<t. Previously reported classification coverage 565/625 is unaffected by optimizing a class already classified.
