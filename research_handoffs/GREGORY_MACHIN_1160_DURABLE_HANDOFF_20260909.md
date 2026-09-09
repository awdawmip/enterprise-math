# Gregory–Leibniz / Machin #1160 durable research handoff

Status: `SOURCE_HANDOFF / FREE_RESEARCH_LINEAGE / NOT_FOUNDATION`
Date: `2026-09-09`
Origin issue: `#1160 — Gregory-Leibniz and Machin formulas as discrete winding composition`
Source researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Parent objective: `EM-OBJ-1160-GREGORY-MACHIN-DISCRETE-WINDING`

## 1. Purpose

This is the stable entrypoint for researchers who receive a formal successor task after the original #1160 free-research run. Read this file before expanding into predecessor notes. The chat transcript is not required for continuation.

The original issue is a free-research call, not a claimable state-machine task. The successor taskset published on 2026-09-09 formalizes the remaining frontiers without retroactively changing the status of the predecessor mathematics.

## 2. What is already verified and should not be restarted

The following units have durable exact notes/checkers on `main` and are `VERIFIED_COMPLETE` at their stated scopes:

1. **Exact rational-turn carrier and relative-turn law.** In `Q(i)^x / Q_{>0}^x`, Gaussian pair multiplication gives a finite integer/rational rotation certificate before real angle. For integer directions `u,v`, the relative factor is `(u·v, det(u,v))`. This explains Machin's `239` as the dot-product label of the final unimodular correction edge.
2. **Farey/Machin finite refinement.** Unimodular edges carry reciprocal-turn labels, mediant refinement is an exact factorization before analytic completion, and Gregory–Leibniz appears only at the completion layer.
3. **Repeated-turn / one-correction classification.** The bounded five-case census was upgraded to a global Diophantine classification. Fixed-total-work completion and equal-depth refinement are distinct resource regimes.
4. **Gaussian valuation lattice.** The exact endpoint carrier decomposes as a `C8` torsion coordinate plus finitely supported oriented Gaussian-prime valuation coordinates. Multi-correction endpoint recognition becomes integer linear algebra.
5. **Valuation-circuit target theorem.** Rank-`s-1` minimal circuits have primitive integer kernels; the `C8` pairing decides whether a scaling hits the diagonal target.
6. **Blind integer-reciprocal rediscovery.** Exact bounded searches rediscovered Gauss, Størmer, Hwang and, via complete residual surgery, Nimbran without using a numerical target value of pi for endpoint recognition.
7. **Complete rational residual split.** For primitive residual `[A+iB]`, all positive opposite-sign two-reciprocal splits are parametrized by divisors of `A^2+B^2`; the smallest admissible divisor is locally Lehmer-optimal.
8. **Rational complementary/Pell chain.** General primitive rational slopes have an exact complement to the diagonal; the diagonal class has no rational square root. Minimum determinant defect `|Q|=1` gives a Pell/Farey finite-resolution chain.
9. **Unrestricted rational-alphabet no-go.** If every primitive rational slope is treated as a free analytic atom and only generalized Lehmer measure is charged, the infimum is zero. The apparent gain is purchased by exploding atom-coordinate complexity.
10. **Parameter-free resource lower bound.** For `s` distinct strict rational atoms, `mu * B_log >= s^2 log_2(10)`; in particular every nontrivial diagonal formula satisfies `mu * B_log >= 4 log_2(10)`.
11. **Exact generalized support-two baseline.** The complete box `0<a<b<=1000`, `gcd(a,b)=1` contains 304,191 atoms. Exact rank-one grouping leaves 102,186 candidate pairs and 101,706 targetable pairs. The `(mu,B_bits)` Pareto frontier has exactly seven points; its unique generalized-Lehmer leader in the box is `[79+3i]^7[278+29i]^5=tau`, with `mu≈1.722670919899336` and zero winding sheet.

## 3. Canonical predecessor reading order

Use the smallest packet required by the successor task. The principal sources are:

- `research_notes/GREGORY_LEIBNIZ_MACHIN_DISCRETE_TURN_COMPOSITION_20260903.md`
- `research_notes/GREGORY_MACHIN_DIOPHANTINE_CLASSIFICATION_FIXED_BUDGET_20260903.md`
- `research_notes/GREGORY_MACHIN_GAUSSIAN_VALUATION_LATTICE_20260903.md`
- `research_notes/GREGORY_MACHIN_VALUATION_CIRCUIT_TARGET_THEOREM_20260903.md`
- `research_notes/GREGORY_MACHIN_BOUNDED_TRIPLE_PARETO_CENSUS_20260903.md`
- `research_notes/GREGORY_MACHIN_SUPPORT4_NATIVE_REDISCOVERY_20260903.md`
- `research_notes/GREGORY_MACHIN_H7M_SUPPORT6_BLIND_REDISCOVERY_20260903.md`
- `research_notes/GREGORY_MACHIN_COMPLETE_RATIONAL_RESIDUAL_SPLIT_20260903.md`
- `research_notes/GREGORY_MACHIN_RATIONAL_COMPLEMENT_PELL_CHAIN_20260904.md`
- `research_notes/GREGORY_MACHIN_UNRESTRICTED_RATIONAL_ALPHABET_NO_GO_20260904.md`
- `research_notes/GREGORY_MACHIN_GENERALIZED_BIT_PARETO_BOUND_20260904.md`
- `research_notes/GREGORY_MACHIN_RATIONAL_SUPPORT2_H1000_PARETO_20260904.md`

Useful executable baselines include:

- `research_notes/experiments/gregory_machin_gaussian_triple_census_20260903.py`
- `research_notes/experiments/gregory_machin_gaussian_four_circuit_census_20260903.py`
- `research_notes/experiments/gregory_machin_h7m_smooth_support6_census_20260903.py`
- `research_notes/experiments/gregory_machin_h7m_support5_residual_surgery_census_20260903.py`
- `research_notes/experiments/gregory_machin_generalized_alphabet_trivialization_check_20260904.py`
- `research_notes/experiments/gregory_machin_rational_pell_halfturn_check_20260904.py`
- `research_notes/experiments/gregory_machin_rational_support2_h1000_census_20260904.py`

Pinned high-value provenance commits:

- `4542085d3d1bedd05cf83c3aee90938e444c2120` — first exact discrete Gregory–Machin calculus.
- `d1c846a3615411fe67938dce96018d79305e370d` — blind support-four rediscovery.
- `f961aa4f9775d04e986d4beeb375f0673c7204d8` — blind Hwang support-six rediscovery.
- `3b6a3d986c7c9b0b096f53ff5e0a8fca5357005d` — complete rational residual split and blind Nimbran recovery.
- `4f08d1afb0a6b90ce7bb80593721584cf9b9190e` — rational complement/Pell chain.
- `b0b99008beead9a22a6857bea9c3316cca0f00fe` — unrestricted rational-alphabet Lehmer no-go.
- `93df1f4261265f910e48365ddca559a1ca202f2f` — generalized bit-Pareto lower bound.
- `79e3349ccbb16ebd3bf7d40cb3e88bb994ea2b90` — exact H=1000 support-two Pareto frontier.

Issue #1160 contains the public research-return trail; comment `5541184856` is the latest pre-taskset summary from the rational-atom phase.

## 4. Shared semantic boundaries

- The two-coordinate Gaussian/rational-turn carrier is a rotation certificate/readout layer; it is not asserted to replace the full P000 six-dimensional spatial substrate.
- Native endpoint recognition must remain exact integer/rational arithmetic. Real `arctan`, pi and floating logarithms belong only to the explicitly typed analytic-completion/ranking layer.
- Historical formulas and Gaussian unique factorization are prior art; bounded optimality or search-architecture claims must state their exact declared universe.
- Unrestricted generalized Lehmer optimization is already killed by the rational-alphabet no-go. Every later optimization must keep a finite atom/resource budget or retain resource coordinates separately.
- General circuit operations already have project coverage through `T3_TYPED_INCIDENCE_CIRCUIT`; valuation/enumeration also has existing project coverage. Do not create a new global circuit tool merely for #1160. Task-local Gaussian specialization/checkers are allowed where the exact arithmetic is specific to this route.

## 5. Current unfinished frontier

The first verified-unfinished units are:

1. **Complete bounded rational-atom generation without raw coprime-pair scanning.** Replace the `O(H^2)` atom enumeration in the H=1000 baseline by Gaussian-prime direction/exponent generation with an exact completeness and duplicate-control theorem.
2. **Generalized support-three Pareto surface.** Under an explicit finite coordinate/bit budget, perform exact rank-two endpoint/circuit enumeration and retain resource coordinates separately. Compare rigorously against the seven-point support-two baseline.
3. **Resource-tradeoff theory.** Determine sharpness or a stronger endpoint-constrained replacement for `mu B_log >= s^2 log_2(10)`, and classify asymptotic families without arbitrary scalar tradeoff weights.

These are deliberately separate successor tasks so that computational generation, bounded higher-support census, and asymptotic theory can proceed in parallel without duplicating the completed predecessor work.
