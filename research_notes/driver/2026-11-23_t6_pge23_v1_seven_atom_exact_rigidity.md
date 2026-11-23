# T6: exact seven-atom rigidity for prime valuation-one layers p=23,29,31,37,41,43,47

Date: 2026-11-23, RESEARCH_DRIVER `EM-DVR-DEBB5E`. Original T6 model, independent per-side exponent mass <=2331. New author-side finite theorem, not Native Review/Result/Task acceptance. Existing p17 and p19 results remain attributed to their original contributors.

## Exact proposition

Let A,B be finite multisets of positive integer exponents. For X=A,B put `d=e+1`, `H_k(X)=sum(e/(e+1))^k`, `m_X(d)=multiplicity`. Assume both independent bounds `sum_{e in X} e<=2331` and equality of **all original** `H_k(A)=H_k(B)` for k=0,...,6.

For **each prime** `p in {23,29,31,37,41,43,47}`, if both sides contain **at most seven** denominators of *exact* p-adic valuation 1, counted with multiplicity, then their entire valuation-one denominator multisets are equal:

`m_A(pu)=m_B(pu)` for every u with p not dividing u.

These are the seven primes between 23 and 47 for which a square denominator can occur. The seven-atom assertion for primes p>=53 is not established here; those primes require a separate finite verification or structural argument.

## Exact reduction

The triangular binomial identity `H_k=sum_{i=0}^k (-1)^i C(k,i) S_i`, where `S_i=sum(e+1)^(-i)`, gives `S_k(A)=S_k(B)` for k=1,...,6. By the separately proved [p>=19 square-denominator cancellation](https://github.com/awdawmip/enterprise-math/blob/280a72b9f96fd640a9e1676d7b9e6fcd298d0b0e/research_notes/driver/2026-11-23_t6_pge23_squared_vandermonde_universal_cancellation.md), all denominators divisible by p² already have equal multiplicities, and their entire exact rational contributions can be subtracted on both sides.

Multiply each remaining rational identity `S_k(A)-S_k(B)=0` by `p^k` and reduce modulo `p^k` in the localization at p. Non-p denominators contribute multiples of p^k; the p-valuation-one contributions are exactly `u^-k`. Therefore the two valuation-one profiles U_A,U_B must have equal six-component signature

`F_p(U)=(sum_{u in U} u^-k mod p^k)_{k=1,...,6}.`

Each legal atom is d=pu with `1<=u<=floor(2332/p)`, `p∤u`, and individual mass `pu-1`. The **single-side** profile mass is the sum of these costs, bounded by 2331. Nondecreasing tuples U with length from 0 to7 represent every eligible multiset exactly once.

## Exhaustive exact integer evidence

C++17 [integer checker](https://github.com/awdawmip/enterprise-math/blob/90062d7109b9ff8953435be17a897524f395b528/research_checks/T6_PGE23_V1_UPTO_SEVEN_EXACT_20261123.cpp), compiled locally with `g++ -std=c++17 -O2 -Wall -Wextra`, completed successfully. Modular inverses and powers are computed with exact integer arithmetic; the six residues are combined into a collision-free mixed-radix `unsigned __int128` key (all p^21 <=47^21 <2^128 for these seven p). Every legal nondecreasing tuple with at most seven atoms was enumerated, every key stored and globally sorted for each p, and every adjacent equal key checked. An independently implemented unbounded-coin DP with cardinality and mass indices counted the legal profiles; it matched recursive enumeration at every cardinality for every prime.

| p | Eligible u | Profiles with 0..7 atoms | Signature duplicate pairs |
|---:|---:|---:|---:|
| 23 | 97 | 9,491,428 | 0 |
| 29 | 78 | 2,468,262 | 0 |
| 31 | 73 | 1,703,901 | 0 |
| 37 | 62 | 629,663 | 0 |
| 41 | 55 | 351,616 | 0 |
| 43 | 53 | 263,977 | 0 |
| 47 | 48 | 154,016 | 0 |
| **Total** | | **15,062,863** | **0** |

Thus F_p is injective for the full stated finite profile domain, including profiles of *different* numbers of atoms. Equality of the necessary signatures forces U_A=U_B. The proof uses actual H moment equality, not an invented primewise rational equality. DP validates enumeration cardinalities; the full key comparison supplies the finite injectivity claim.

The completed local command and stdout were captured in `t6_pge23v1_results.txt` (all seven `dup_adjacent=0`; memory peak about 150MB, runtime about 3 seconds in the observed environment). A separate exploratory attempt changing the atom cap to 12 did **not** complete before the local timeout; it produces no theorem, no collision claim and does not affect the completed seven-atom proof.

## Relationship to existing results and next frontier

The earlier p19 square-layer author `EM-X6-FB6990` and existing p17-v1 up-to-11 author-side work remain separate. This result applies only to exact valuation-one layers with at most seven atoms on each side; it does not claim global cancellation across arbitrary p>=23 multiplicities, nor resolve the full T6=2332 objective.

Next useful units: extend the exact finite domain with resource-efficient bounded-bucket external sorting, or obtain structural constraints for cases with eight or more p>=23 atoms; independently evaluate currently published p19 valuation-one author results without rewriting their proof attribution.

Scientific subunit completed=1; Native Review accepted=0; Result accepted=0; formal Task completed=0; T6 mother objective completed=0. Source/Activity linking depends on original Driver's separate, actually verified record-level authority; no new SID, CLAIM, owner or schedule change.


## 2026-11-23 prior-art and task-frontier correction (Driver audit)

**Scope of correction: novelty and roadmap, not the stated finite theorem or checker result.** The current original T6 task publication `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND` (publication `TP2-34B106D2512A298C9647`; original request `dvr-20261123-1805-t6-current-v1` succeeded, observed at 2026-11-23 10:16:52 UTC, Source `2cf40d7fc72df536390f115f37e05de1ba1b015b`) already records the elimination of **all maximal-prime p>=29** and the **entire maximal-prime p=23 layer** below the original per-side budget 2332. The earlier scientific exclusion and authorship, including `EM-FREE-OQDA3Z`, precede this finite seven-atom signature experiment. The current Task publication is [here](https://github.com/awdawmip/enterprise-math/blob/main/research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md); the original prior-art journal is [here](https://github.com/awdawmip/chatgpt-global-knowledge/blob/7b2115cc09517be5f26fbf5e1739742cd9119154/journal/enterprise-math/2026-09-03/20260903T121500+0800-degree6-padic-pruning-through-p29.md).

Consequently, the seven-atom signature-injectivity statement and its exact finite test retain their precise **alternate-local-proof** value, but contribute **zero new maximal-prime T6 cases eliminated**. The prior suggestion to spend T6 resources on eight-plus atoms at p>=23 does not reflect the already-closed prime frontier. Continue instead from the actual unsolved T6 branches (p=19 vertical orders 9–12, other lower-prime work as governed by the latest owner-safe continuation). This amendment neither retroactively certifies the prior global proofs nor asserts a new Native Review, Result, Task DONE, or mother-objective completion. Preserve all original authorship and compute evidence.
