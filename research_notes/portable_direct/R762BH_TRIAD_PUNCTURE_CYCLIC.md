# R762BH — Sharp 19-probe threshold and cyclic-frame cost for the candidate six-axis triadic observer

Date: 2026-11-15. Research line: RS-X6-TRIADIC-CLOSURE-DYNAMICS (TP2-8B7E13C5904A2D6F1142). Predecessor native checkpoint reported Researcher EM-X6-44BACF and Activity RA-2BFD679DF2B3D27CAA0CB7D5; this independent draft creates no new session/CLAIM. Status: **AUTHOR_PROVED_AND_EXACT_CHECKED / NOT_REVIEWED**.

## Inputs and precise scope

Frozen P000: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`; frozen source `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`. Taskbook: `research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md`; immediate proof predecessor: R762BG PR #2485, immutable `480954c317acfaabe582a7f7f67af84d77627a8f`. Applicable current normative context was read separately.

The theorem concerns R762BF/BG's **conditional candidate** six-bit orientation BRC observer. No P000 native signed TRIADIC_CLOSURE_E Port predicate, V17/V29/V39 admissibility, or physical interpretation is assumed. There are six labeled native axes and twenty candidate named triples `Q={T subset [6]: |T|=3}`. For retained queries `H subseteq Q`, use exact Boolean linear readout `(A_H x)_T = sum_{i in T}x_i mod 2` for `x in F_2^6`. The corruption model is arbitrary substitution of `t` recorded Boolean outputs; it is not a physical noise model.

Define **orientation separation distance** `delta(H)=min_{x != 0}wt(A_H x)` (including zero if orientation signatures collide). Correcting any `t` corruptions between all 64 states is equivalent to `delta(H)>=2t+1`.

## BH1 — Sharp 19-query three-error correction theorem

**Theorem.** Every one of the 20 subsets made by deleting one triple has parameters `[19,6,7]`. Every one of the 190 subsets made by deleting two triples has parameters `[18,6,6]`. Therefore the **minimum number of distinct named triple queries that uniquely correct any three Boolean errors is 19**.

**Proof.** R762BG establishes the full code `[20,6,8]` and enumerator `W_{20}(z)=1+15z^8+32z^{10}+15z^{12}+z^{20}`. Puncturing one coordinate lowers each nonzero word's weight by at most one. The 15 words of weight eight are exactly the images of orientation masks with four set bits. Let `Y=[6]\supp(x)`, of cardinality two. For a triple T, its parity bit is one exactly when `|T intersect Y|` equals 0 or 2; equivalently Y lies wholly inside T or wholly outside T. Exactly `C(3,2)+C(3,2)=6` of the 15 Y have this property for any fixed T. Thus a deleted query appears in a weight-eight word, yielding distance 7. The positive separation distance also implies rank six.

For two distinct triples T,U, put `r=|T intersect U|`. A weight-eight word has a one in both coordinates precisely when Y lies wholly inside or outside *each* triple. Counting such Y by r gives:
* `r=0`: T,U partition the six axes and there are `3+3=6` choices.
* `r=1`: only `Y=T\U` and `Y=U\T` work, giving 2.
* `r=2`: only `Y=T intersect U` and `Y=[6]\(T union U)` work, giving 2.

Hence every pair of deleted queries lies in the support of a weight-eight codeword, so deleting that pair produces weight six. Deletion of two positions cannot reduce an originally nonzero codeword below six. Consequently every 18-query puncturing has distance exactly 6 and retains rank six. All smaller query subsets lie inside an 18-query subset and cannot exceed its separation distance. Since unique three-error correction requires distance at least 7, 19 is necessary and sufficient. QED.

By S6 transitivity the 19-query code has the identical weight enumerator for every omitted T:
`W_{19}(z)=1+6z^7+9z^8+16z^9+16z^{10}+9z^{11}+6z^{12}+z^{19}`.
Of the 190 unordered query pairs, 10 are disjoint, 90 intersect in one axis and 90 intersect in two axes; the shared weight-eight witness counts are respectively 6, 2, and 2.

## BH2 — One extra probe for hypothetical cyclic-frame symmetry

Declare the *candidate*, fixed six-axis cycle `rho=(1 2 3 4 5 6)`. Require the observed query family to be `rho`-invariant. This is an explicit relabeling assumption, **not** a sourced claim that native V17/V29/V39 events implement this cycle.

The 20 triples decompose into exactly four rho-orbits of sizes **2, 6, 6, 6**. Every proper orbit union omits at least two queries. By BH1 its orientation separation distance is at most 6; the full 20-query family has distance 8. **Thus a rho-invariant query family can correct three arbitrary Boolean errors iff it contains all 20 queries.** The 18-query family obtained by omitting the two-element orbit has rank six and distance six, so it corrects two errors.

The constraint imposes a **sharp one-probe symmetry cost** at the three-error threshold: unrestricted minimum 19, rho-invariant minimum 20.

## BH3 — Complete finite cyclic-orbit classification

Build the four orbits by exhaustive action of rho on every triple. For every one of the `2^4=16` orbit unions, calculate binary rank exactly by GF(2) elimination and separation distance over the 63 nonzero orientation masks. The two auxiliary files independently reproduce all 16 rank/distance entries and weight histograms.

| Orbit selector (bits 0..3) | Queries | Rank | Separation distance |
|---|---:|---:|---:|
| 0000 | 0 | 0 | 0 |
| 0001 | 2 | 2 | 0 |
| 0010 | 6 | 4 | 0 |
| 0011 | 8 | 4 | 0 |
| 0100 | 6 | 6 | 1 |
| 0101 | 8 | 6 | 2 |
| 0110 | 12 | 6 | 4 |
| 0111 | 14 | 6 | 4 |
| 1000 | 6 | 6 | 1 |
| 1001 | 8 | 6 | 2 |
| 1010 | 12 | 6 | 4 |
| 1011 | 14 | 6 | 4 |
| 1100 | 12 | 6 | 4 |
| 1101 | 14 | 6 | 4 |
| 1110 | 18 | 6 | 6 |
| 1111 | 20 | 6 | 8 |

The proof of the universal puncturing threshold is combinatorial and applies to every subset, without reliance on this finite classification. The classification makes the restricted cyclic experiment completely reproducible.

## BRC provenance and next source-dependent problem

Population: 64 **named candidate orientation** states. Observer: retained named parity results for H, with up to three arbitrary Boolean errors. Optional operation: rho acting by relabeling the query domain. The 19-query injectivity plus decoding radius supplies an exact observer-specific orientation recovery certificate. It does not erase named Cell/Link/Port paths, multiplicities, or additional provenance for future operations outside this declared language. A positive BRC total is a distinct readout from signed observer parity.

Next: obtain actual Source-authorized P000 triadic Cell/Link/Port incidence H_native, signed action and V17/V29/V39 transport operators at the frozen scientific pin; calculate `delta(H_native)` and verify invariant query families under the *actual* operation semigroup. Conditional candidate observation remains separate from P000's native closure relation.

Companions: `R762BH_TRIAD_PUNCTURE_CYCLIC_VERIFY.js` and `R762BH_TRIAD_PUNCTURE_CYCLIC_EVIDENCE.json`. Author-side proof and exact exhaustive check; independent Driver review NOT_REVIEWED.
