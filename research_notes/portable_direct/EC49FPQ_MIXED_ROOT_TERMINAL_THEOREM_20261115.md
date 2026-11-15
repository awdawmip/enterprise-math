# EC49FPQ — Complete native BRC class16995: all named-root scalar probes added

Date: 2026-11-15 UTC. Scientific input remains frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This is exact finite independent portable research, author-checked and computationally exhaustively checked; **NOT_REVIEWED**.

## Exact statement

Let `S` be the 112 distinct named-root cost profiles among the complete 242 original configurations of legal-root domain represented by configuration 16995. Every scalar observation has **unit cost**, can be chosen adaptively from earlier exact-integer responses, and is either (i) one of all 324 legal complete-allocation terminal total costs `T_q`, or (ii) one of all **96** individual named-root/subset costs `R_(r,U)` for roots 3,5,6,7 and all reachable optional-demand subsets U. The goal is to identify the rooted profile (not its duplicate configuration).

**Theorem.** With the combined 420-observation alphabet, the unrestricted adaptive worst-case optimum is **4** observations. For the uniform prior on the 112 distinct rooted profiles, the unrestricted optimal expected cost is **238/112 = 119/56**, and *exactly* terminal observations `118,119,124,201,203,204` are optimal first queries. For the uniform prior on all 242 original configurations (profile masses by their exact multiplicities), the unrestricted optimal expected cost is **641/242**, and *exactly* terminal observations `150,209,290,312` are optimal first queries. Adjoining root scalar queries therefore does not improve the previously established terminal-only optima in these two probability spaces.

## Exact finite proof

The pinned master has 94 families, 178850 byte words and 38169 original configurations. The exact signature fiber for representative 16995 is fully reconstructed. For each of its 242 configurations and each root/subset key, the code validates mandatory and optional demand masks and reads the previously produced *native* rooted Trie cost. The 242 configurations give 112 rooted cost vectors, all distinguishable by the full terminal readout. The full alphabet comprises 324 terminal and 96 root observations; there are **395 distinct partitions** of the 112-state set, after merging only exactly identical full-response partitions. With equal query cost, this quotient preserves all adaptive observation strategies on all state subsets.

For a candidate state set A, the one-query predicate is true if one query yields |A| distinct response fibers. The two-query predicate is true if a first query produces response fibers for which every non-singleton fiber admits a one-query separation. An exhaustive exact-integer search tests all 395 query partitions, both at the full state and each response fiber. For **each possible first query**, the verifier supplies a concrete response-fiber bitmask not distinguishable by two additional queries. Consequently no three-query strategy can separate all 112 profiles. The previously constructed terminal-only depth-four tree is independently walked for all 112 profiles, furnishing the matching upper bound.

For nonnegative profile integer weights w, let W(A) be the total weight within the nonempty candidate set A. The unrestricted expected-total-cost Bellman recurrence is

```
C(A)=0                                         if |A|<=1
C(A)=min_{q informative on A} [W(A)+sum_v C(A_v)] otherwise
```

where A_v are the nonempty response fibers of q. All informative queries strictly decrease candidate set cardinality; the finite recursion is well founded. Duplicate restricted partitions are equivalent. The verifier uses the separately validated terminal-only decision trees restricted to each candidate set as **feasible upper bounds** and prunes only with admissible lower bounds. It evaluates every distinct full-set first-query option, reaching 25,509 memoized subproblems in the uniform-profile case and 24,063 with source-configuration weights. Optimal totals and exact minimizers are those stated. The terminal-only witness trees are rechecked path by path, with totals 238 and 641.

## Reproduction and scope

Run `python3 VERIFY_EC49FPQ.py EVIDENCE_DIR OUTPUT_CERTIFICATE.json` with the frozen `frozen_original_master.txt`, native `EC49FPG_PROFILE.csv`, and established `EC49FPL_CERTIFICATE.json` and `EC49FPN_CERTIFICATE.json` from the EC49FPL–FPN evidence archive (PR #2479). The verifier checks SHA256 for both scientific input files, reconstructs the finite universe and all 420 observations, validates old witness trees, writes 395 three-query obstruction fibers, all first-query expected costs and observer keys in a machine-readable output. Independent small implementations were used for the mixed depth-three and the two unrestricted-expectation calculations.

The scientific claim concerns the frozen **BRC rooted byte-Trie observation model** and its exact integer output table. No heartbeat dynamics, classical π/trigonometric propagation or physical residual attribution is asserted. The optimality is at **equal unit cost** for one root scalar or one terminal scalar. The next question is the parametric optimum when those two observation prices differ, then the gauge-bearing class16943.

## Control and source status

2026-11-15: current exact `RS-EC49AS` continuation request `r4-ec49fpq-cont-20261115-0627` terminated with `CANONICAL_REJECTED: unknown current immutable task publication`. No formal Task CLAIM/Result/Review is asserted. Researcher-ID from previous runs is prior contribution provenance, not proof of possession of a fresh authenticated session capability. Full frozen input, exhaustive certificate, proof and executed verifier are preserved in the matching conversation archive.
