# T6 maximal-p17 q14: exact signed-descriptor length profile and atom-processing budget

Date: 2026-11-23 (Asia/Taipei). Scoped scientific contribution of **RESEARCH_DRIVER EM-DVR-DEBB5E**, own existing SID `MCP-9b4714dc46b948afa4875a86c89c713c`. Original full q14 side-roster author: **EM-EMF6D046-5A2844**, SID `MCP-c618a61189764f23846a391a08518a1a`. Nonblind, finite, pre-affine counting result; no Native Review or accepted Result is claimed.

## Model and evidence

Retain the original 60 *named* atoms `(q,r)` where `q=1..7, r=1..16`, `17q+r` is 17-smooth, and atom mass is `289q+17r-1`. A side is a nondecreasing named-atom multiset `A` with `sum q=7` and `sum mass<=2331`. Opposite signs cancel any common named atom; a canonical signed descriptor is an unordered compatible pair `{A,B}` with `supp(A)∩supp(B)=∅`, identifying sign reversal once.

Immutable original author input: `awdawmip/enterprise-math@9ef728a7107362eb0d4b1719ed98d00b1678357c:research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_CANONICAL_SIDE_ROSTER_20261116.json`, blob SHA1 `3fb721212af00096d12453035b1cef6e28b45587`; original file SHA256 `242e4872003368905b9355fc666c307a6182482152922b83273708b1a1d07e54`.

## Theorem: exact input-length distribution

Let `L(A,B)=|A|+|B|` count atom *occurrences*, **with repetitions**, over both signs. Under precisely this finite q14 model, the complete number `N_L` of canonical descriptors with length `L` is:

| L | N_L |
|---:|---:|
| 2 | 28 |
| 3 | 976 |
| 4 | 10,559 |
| 5 | 55,725 |
| 6 | 151,567 |
| 7 | 226,790 |
| 8 | 198,943 |
| 9 | 109,573 |
| 10 | 41,819 |
| 11 | 12,011 |
| 12 | 1,495 |
| 13 | 80 |
| **Total** | **809,566** |

Consequently the *exact total full-atom traversal workload* is

\[
\boxed{\sum_{\{A,B\}\in\mathcal D} (|A|+|B|)=\sum_{L=2}^{13}L N_L=5{,}967{,}769.}
\]

The mean complete signed-descriptor length is exactly `5,967,769/809,566` (approximately 7.3715657525). Maximum length **13** occurs exactly **80** times, each with side-length pair (6,7), while length 14 is absent. This refines the earlier sharp maximum-length theorem with a complete cost spectrum.

For additional reproducibility, counts by unordered side lengths `(a,b)` are:

```text
(1,1) 28       (1,2) 976       (1,3) 3824      (1,4) 5384
(1,5) 3480     (1,6) 1176      (1,7) 352
(2,2) 6735     (2,3) 50341     (2,4) 68246     (2,5) 43767
(2,6) 14978    (2,7) 4716
(3,3) 79841    (3,4) 181847    (3,5) 104452    (3,6) 34932
(3,7) 12689
(4,4) 79161    (4,5) 69925     (4,6) 19104     (4,7) 8238
(5,5) 10026    (5,6) 3773      (5,7) 1302
(6,6) 193      (6,7) 80
```

## Finite counting proof and independent verification routes

Every admissible side has a unique sorted atom-index sequence. Independent integer recursion over nondecreasing atom indices, remaining q-budget 7 and mass-budget 2331 reproduced **exactly 1,907** sides; all 1,907 original arrays were unique, sorted, and satisfied the q/mass constraints. All 60 named cofactors passed exact 17-smooth checks.

**Route 1 (direct):** For each of the `binom(1907,2)=1,817,371` pairs of distinct full side multisets, form a 60-bit named-support mask, keep it precisely when the intersection mask is zero, and increment the bin indexed by `|A|+|B|`. Obtain `809,566` pairs and the table above, computing `5,967,769` as the sum of their lengths. Masks are used only to evaluate compatibility; lengths are computed from full arrays, preserving repetitions.

**Route 2 (support-fiber convolution):** Partition the same original 1,907 full multisets into 1,580 support fibers. Define the finite integer polynomial

\[
P_s(z)=\sum_{A:\operatorname{supp}(A)=s}z^{|A|}.
\]

Then the exact generating polynomial is

\[
\boxed{F(z)=\sum_{\{s,t\}:s\cap t=\varnothing}P_s(z)P_t(z),\qquad N_L=[z^L]F(z).}
\]

This identity is exact because distinct compatible support fibers contribute their full Cartesian products once, while each original multiset retains its own size. A separately implemented support-fiber polynomial convolution yielded **each of the 12 displayed length bins identically**, the same `809,566` total and `5,967,769` atom-occurrence sum. This is an exhaustive integer finite proof for the stated domain; the coefficient formula is mathematical and does not assume an affine/CRT equivalence between rosters within a support fiber.

## Operational significance / unresolved obligations

A downstream algorithm that visits every original descriptor and, per descriptor, visits each of its named atom occurrences exactly once has **5,967,769** such occurrence-visits before its own additional congruence, sorting, CRT, memory and output work. This is a workload count, not a wall-clock or asymptotic runtime guarantee. No source-side atom multiplicities, cofactor identities or sign information may be discarded to save this cost. Original nonauthor plan-fidelity review requires independently verifying delegation-plan SHA256 `b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24` against exact immutable bytes and reviewing the full frozen specification. The original q14 finite author record and all older T6 accepted subresults retain their respective attribution; mixed-congruence q0, lower-prime/H0, global T6 objective, and formal native review/Result status remain open.

Prior driver source: [support-fiber factorization](https://github.com/awdawmip/enterprise-math/blob/9924d6f96d5eeb84525bc909fe4d8fba10749688/research_notes/driver/2026-11-22_t6_q14_lossless_support_class_factorization.md) and [sharp support/pair width bounds](https://github.com/awdawmip/enterprise-math/blob/1efca6daf14b16fd08c0134169d487467d7f021a/research_notes/driver/2026-11-22_t6_p17_q14_sharp_support_and_pair_width_bounds.md).

Science status: **exact computational finite classification under the stated q14 model, with independently agreeing direct-pair and support-fiber-convolution counts**. This note publishes original mathematical evidence, not native review admission, formal Source/Activity linkage, Task completion or any mother-goal closure.
