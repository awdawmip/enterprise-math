# R284GD — Exact rational Farkas certificate audit for the all-q two-heavy lemma

Date: 2026-11-24 (Asia/Shanghai). Mode: informed portable TASK_RESEARCH, independent scientific-file publication; no shared CLAIM asserted. Frozen scientific inputs: R284CO → R284FM → R284FP → R284GA → R284GB → R284GC. P000 and ACTIVE Heartbeat-X6 ontology remain unchanged.

Status: **AUTHOR-CHECKED / EXACT RATIONAL FINITE-COVER CERTIFICATES / NOT INDEPENDENTLY REVIEWED**.

## Result

**Theorem (certificate-supported, conditional on R284FM's residual-cut encoding).** For every real number (q\ge5), each (k\in\{8,9\}), and nonnegative real multiplicities (x_1,\ldots,x_7) with
[
\sum_{p=1}^7x_p=4q+k,
]
the following six necessary conditions imply that at least two of (x_3,x_5,x_6) exceed (2q+1): the three nominal distance inequalities for phase pairs (12,13,23), and the three stable residual-source cut disjunctions for pairs (01,02,03), with one-read-flip separation margin (+3).

This **removes reliance on the exact Z3 UNSAT verdict for this intermediate lemma** by furnishing explicit rational linear-inequality contradiction multipliers for every finite disjunct. It does not independently reprove the R284FM mapping between physical histories and its eight-source cut condition or the R284GB prefix lifting argument.

## Finite, complete branch reduction

Normalize the four binary tags as ((0,p\&1,(p>>1)\&1,(p>>2)\&1)) in each nonconstant pattern (p\in\{1,\ldots,7\}). Let (\ell_i(p)) be the last changed edge of pattern (p) before phase (i), retaining separately the four left and four right omission-budget vertices. A nonempty subset (U) of these eight vertices yields a stable necessary alternative:
[
\sum_{p:\,L_{\ell_i(p)},R_{\ell_j(p)}\in U}x_p\ge q|U|+3.
]
For each induced mask retain the **smallest** vertex-set cardinality; exhaustive enumeration of the 255 nonempty subsets gives, for phase pairs (01,02,03), respectively **7, 9, 7** distinct alternatives. The three nominal inequalities are (\sum_{p:c_i(p)\ne c_j(p)}x_p\ge2q+5\) for adjacent phases and (\ge2q+3\) for opposite phases, keeping only (12,13,23).

Failure of the two-heavy property is the union of **three** possibilities, corresponding to choosing two distinct members of (\{3,5,6\}) whose multiplicities both satisfy (x_p\le2q+1). Consequently the entire reduced counterexample search is a union of
[
7\cdot 9\cdot 7\cdot3=1323
]
linear systems for each (k), for **2646 exact systems** across the two widths. These systems retain the full free, unbounded parameter (q\ge5). No finite upper cutoff on (q) is used.

## Exact Farkas proof method

For a selected branch, write every inequality—including (q\ge5), (x_p\ge0), distance, chosen cut and the two light-type constraints—as (a_i\cdot z\ge b_i), with (z=(q,x_1,\dots,x_7)), integral (a_i,b_i). The single affine equality is
[
E\cdot z=k,\qquad E=(-4,1,1,1,1,1,1,1).
]

For each of the 2646 systems, the companion program constructs nonnegative rational multipliers (\lambda_i) and a rational equality multiplier (\mu) satisfying **both**
[
\sum_i\lambda_i a_i+\mu E=0
\quad\text{(all eight coefficients, exactly)},\qquad
\sum_i\lambda_i b_i+\mu k>0.
]
Combining the inequalities and equality would imply (0\ge\sum_i\lambda_i b_i+\mu k>0), a contradiction. This establishes infeasibility over the real numbers for that entire branch, at every possible (q\ge5).

SciPy/HiGHS is used solely to **propose** multipliers. The multipliers are reconstructed as Python `Fraction` values and every coefficient cancellation, sign, and strict positivity comparison is checked with exact rational arithmetic. A floating-point optimizer returning a spurious vector cannot pass these tests. The program can emit the complete per-branch rational witness table as JSON; the correctness test itself is direct rational algebra.

**Example of a two-row certificate.** Any branch selecting the (03) cut (x_6\ge2q+3) and the light constraint (x_6\le2q+1) is refuted directly by adding the two inequalities (each with multiplier (1/2)), obtaining (0\ge1). This is one of the emitted exact certificate types, not an assumption about every branch.

## Local execution evidence

Command:
```bash
python3 research_notes/portable_direct/R284GD_exact_rational_farkas.py --emit R284GD_certificates.json
```

Executed locally on 2026-11-24 using SciPy/HiGHS for proposal and exact `fractions.Fraction` for validation. Actual outputs:

```text
k=8: 1323 exact rational Farkas certificates verified; max-support=8; max-denominator=39
k=9: 1323 exact rational Farkas certificates verified; max-support=8; max-denominator=35
PASS: 2646 exact contradiction certificates for all real q>=5, k=8,9 and every reduced six-condition non-heavy branch
```

The generated JSON contains **2646 rational witness entries** and was checked by the same run; it is optional materialized evidence, not required to trust a floating-point infeasibility judgment. To inspect each certificate, use `--emit`; the exact verifier runs before any entry is emitted. The program source is the reproducible proof artifact.

## Scientific consequences, scope and next questions

1. Together with R284GC's established finite star-cut reduction, this supplies a second proof mechanism for the unbounded-q two-heavy **necessary-condition lemma**. It is an exact finite-cover proof in rational arithmetic, not extrapolation from (q\le14).
2. The earlier all-q capacity derivation (n_{\min}(q,1)=4q+10) still invokes R284FP (lower bound), R284GA (two-heavy classification), R284GB/R284FW (prefix blocking), and R284FE (upper construction). The present proof replaces only the R284GC SMT feasibility step; those inherited components still merit adversarial review.
3. Highest-value next audit: independently reconstruct R284FM's omission-source reachability and all-history bipartite-cut equivalence; then test the R284GB source-slot lifting with minimal exact physical-state witnesses.
4. The integer/real separation is meaningful: exact rational Farkas infeasibility on the real relaxation implies the integer model's infeasibility immediately.

## Sources

- R284GC all-q lemma and original SMT program: `awdawmip/enterprise-math@a505188e6274c24846ffc1aed0db6072f45c4747:research_notes/portable_direct/R284GC_ALL_Q_TWO_HEAVY_COMPLETENESS_AND_SHARP_CAPACITY_20261124.md`.
- R284FM all-history residual cut: `awdawmip/enterprise-math@1d1c5dd412719c7aaf016187b6493b77253cd9f9:research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md`.
- Companion exact witness source: `research_notes/portable_direct/R284GD_exact_rational_farkas.py`.
- This research uses an **auxiliary binary observer model**, not native heartbeat dynamics and no BRC arithmetic was replaced or simulated.

No new task ownership, formal Result, acceptance, or independent review is claimed by GitHub file publication.
