# Prospective total-order-3 input challenge

Disposition: **PASS_STATIC_PROSPECTIVE_INPUT_ONLY**. The actual frozen JSON has the stated 3,264 complete cancellation-normalized primitive descriptors modulo global sign, with correct factor-domain flags, fixed-atom arithmetic, all six mixed targets, both budgets and radii. The common homogeneous basis and exact weighted Gram–Schmidt data support the stated prospective cost bound. This is an input/arithmetic review; no order-3 case feasibility, lattice enumeration or classifier was run, and no EMPTY assertion is made.

This review is **DIRECTED / NONBLIND**: the supplied scope, expected totals/pins, builder, frozen input and common portable Source artifact were available. The checking program was independently written and neither imports nor executes the builder. Native reviewer identity is **UNKNOWN**; no native session, identity, activity, review record or Source write was created. Construction authors remain **Driver EM-DVR-4CF7AF** (input builder) and **Root EM-DVR-FBF223** (direction/static cost); this challenge does not confer construction or scientific-result authorship on the checker.

## Descriptor completeness and domain

The only partitions of normalized vertical order 3 are 3, 2+1 and 1+1+1. Quotienting overall sign fixes the single q3 atom positive; fixes the q2 atom positive in 2+1; and leaves all-positive or two-positive/one-negative q1 triples. On mixed triples the negative atom cannot equal either positive atom, because opposite identical atoms cancel. Same-side repetitions remain, including a triple of one atom whose multiplicity gcd is 3: “primitive” means cancellation-normalized, not gcd-one.

The independent checker also constructs every weight-3 atom multiset, assigns all signs, cancellation-normalizes, quotients global sign, and compares this set exactly with the JSON. It finds no duplicate orbit and no missing or extra descriptor.

| Family | Derivation | Count | Admissible | Outside domain |
|---|---:|---:|---:|---:|
| q3 single | 16 | 16 | 9 | 7 |
| q2/q1, same and opposite | 2·16² | 512 | 240 | 272 |
| Same-sign q1 triple | C(18,3) | 816 | 364 | 452 |
| Mixed q1 triple, disjoint signs | 16·15 + C(16,2)·14 | 1,920 | 792 | 1,128 |
| Total | | 3,264 | 1,405 | 1,859 |

The admissible cofactor sets, obtained by actual prime factorization with all prime factors at most 17, are:

- q1: {18,20,21,22,24,25,26,27,28,30,32,33}, size 12.
- q2: {35,36,39,40,42,44,45,48,49,50}, size 10.
- q3: {52,54,55,56,60,63,64,65,66}, size 9.

Thus admissible family counts are 9, 2·10·12=240, C(14,3)=364, and 12·11+C(12,2)·10=792, totaling 1,405. The checker retains every descriptor in the frozen full family, including the 1,859 flagged outside-domain cases and all composite cofactors.

## Targets, budgets and radii

For every occurrence of atom (q,r), the checker independently verifies cofactor a=17q+r, denominator 17a, cost 17a−1, and its prime factors. With fixed positive/negative multisets V+/V− it recomputes

\[
T_k=\left(-\sum_{(q,r)\in V_+}(17q+r)^{-k}
+\sum_{(q,r)\in V_-}(17q+r)^{-k}\right)\bmod 17^k,
\quad k=1,\ldots,6,
\]

using independent Bezout inverses. Every one of the 19,584 stored target entries matches. The six exact moduli are 17, 289, 4,913, 83,521, 1,419,857 and 24,137,569; the q0 weights are 17j−1 for j=1,…,16.

The two budgets are separately B±=2331−Σ(V±)(17(17q+r)−1). Every stored budget is nonnegative and matches, as does R²=B+²+B−². For a signed q0 vector, the separate weighted side-mass bounds imply its weighted squared Euclidean norm is at most R².

- Maximum: **7,530,265**, at `q3-single-01`, budgets (1448,2331), targets (16,101,4198,38062,1012621,2613443).
- Minimum: **4,663,465**, at `q3-q1triple-mixed-16-16-vs-15`, budgets (1211,1788), targets (10,232,344,65532,755406,4296990).

## Common-kernel and prospective cost link

The checker uses only the homogeneous basis and weights from the exact common portable bytes. For A[k,j]=j^(−k) mod 17^k, all 16 unweighted basis rows satisfy all six homogeneous congruences. The first-six-column 6×6 minor has determinant 15 modulo 17, hence is invertible modulo 17⁶. The mixed modular map is therefore onto \(\bigoplus_{k=1}^6\mathbb Z/17^k\mathbb Z\), whose order is 17²¹. The basis determinant is −69,091,933,913,008,732,880,827,217=−17²¹. Containment plus equal index proves that the supplied rows span the full mixed-congruence kernel, rather than a proper sublattice.

Each weighted row equals its unweighted row multiplied coordinatewise by 17j−1. An exact rational LDL decomposition of the row Gram matrix reproduces all 16 squared Gram–Schmidt lengths and all 256 stored mu entries. The minimum is the 12th squared length, with exact numerator/denominator:

```text
8350069911612335617606677214061177705401058080646556447012234889468081355909
480650972868542992444263969893692042421717754534280313801217347854273
```

It exceeds 2·7,530,265=15,060,530. The exact positive difference has numerator 1111211515196457823610066367558131889747505186950391752599586985588367211219 and the same denominator.

For a future exhaustive GS-coordinate traversal using any correct affine lift/centers, a coordinate interval has radius at most sqrt(maxR²/Dmin)<1/sqrt(2), so it contains at most two integers. Designate the closest integer the near choice, breaking ties consistently; any second/far choice is at distance at least 1/2 and contributes at least Dmin/4. Two far choices would contribute more than maxR², so every surviving prefix has at most one far choice. At depth d there are at most d+1 prefixes. Testing at most two choices per prefix through 16 dimensions gives 2·Σ(d=0,…,15)(d+1)=**272** coefficient admissibility checks per case and 3264·272=**887,808** across the full literal family. These are conditional prospective completeness/cost bounds. No affine lift, order-3 center or q0 candidate was constructed or tested by this challenge.

## Actual bytepins and verification

Common Source linkage supplied for this review: repository `awdawmip/enterprise-math`, commit `953db05d78bd0f175a99d0406f850691d479ae26`, path `research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/portable_input.json`. The local bytes match the exact supplied Source SHA and git-blob pin. The review did not authenticate a new remote/native session or refetch commit ancestry.

| Artifact | Actual bytes | SHA-256 |
|---|---:|---|
| Frozen total-order-3 JSON | 1,704,986 | `c7a2624f7b9fbb9437b0b1756b323a879926ff138f82b816c6de60790a36371a` |
| Builder inspected, not executed | 5,546 | `311e3722459efb938aa6e36c23907f2347082630a40e398d3c63976b322326ff` |
| Common portable JSON | 32,208 | `7060ee638986a5c71a9775093e6b7f03ff3d5ff205ed438e3f5fa5aa93ca62ce` |
| Independent checker | 15,761 | `9aedfaf4af49a6e9f8c6702051064e6a53e15d4ee62a7b0575a35587a9624e07` |
| Checker result JSON | 4,392 | `5b4a2069a52e1caafc4a24a0e60ed886edd85eb1b3fbaa7b7f119a150b1ab3d7` |

Common portable git-blob SHA-1: `654212795533a51039bab2b752095ab19b649535`. Frozen input git-blob SHA-1: `f615f79df601665c03bf5655fe1680d454e780f4`.

Reproduction: run `python check_order3_input.py` within this `input-challenge` directory. It reads the frozen inputs, performs static descriptor/arithmetic/matrix checks, and writes only `CHECK_RESULT.json` here. The frozen input, builder and Source snapshot were not modified. `BYTEPINS.json` additionally pins this report and the other challenge artifacts.
