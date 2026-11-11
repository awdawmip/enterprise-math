# R5 — Exact bilateral resonance chambers and asymmetric legal-order losses

**Date:** 2026-11-12 (Asia/Shanghai). **Status:** author-side finite exact mathematical proof with locally executed rational checker. **Subject:** frozen external P/Q–BRC Blackwell 28-mass auxiliary model; not a native-X6 theorem.

## Provenance and fixed science

Frozen original X, fifteen **labeled** elementary kernel moves M₁,…,M₁₅ and D=ΣMₐ: commit `435e77af0d180eac32bd1f9c4c464bc4010b7551`, `research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py`. Preceding one-sided resonance-splitting proof: `f545f3882b16c1b9d5bab60b5c6eb832b2debe36`, `research_notes/brc_r5_resonance_splitting_20261112/RESEARCH.md`. Frozen scientific pins remain GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`.

The complete observer A has 15 linear observation rows. Likelihood numerators are R=(2,10,15,20,25,30,38), ports (1,2,3,5). The rational positive 28-mass initial state X and all moves Mₐ are **reconstructed exactly** by the accompanying checker. Set

`x=X_(0,3)=X_(1,3)=155682221/25142124560000000`.

Define the six-arc observation kernel H by mass increments `(1,3):-23, (2,3):+28, (6,3):-5`, with opposite increments at port 1 and zero elsewhere. The equalities -23+28-5=0 and 10(-23)+15(28)+38(-5)=0 give AH=0. Analyze X(η)=X+ηH using the same fifteen labeled moves.

## New theorem — exact two-sided local chambers

Let

`E=x/100000=155682221/2514212456000000000000`.

For **every rational η satisfying 0<|η|≤E**:

1. X(η) is strictly positive, AX(η)=AX, and the maximal nonnegative endpoint of X(η)+εD remains `ε_max=9/115400000`.
2. The distinct exact positive *first-zero prefix threshold values* in `(0,ε_max)` number **1,147**: the original **1,144** fixed target-0/source-3 subset-sum thresholds plus exactly `t_q(η)=(x−23η)/q` for q∈{15,12,3}, contributed by target-1/source-3. No other new phase values appear.
3. At η=0, t_q(0)=x/q already belongs to the original target-0 set, so the original count is 1,144. On both open half-chambers all three moving values are distinct from the fixed set. Each is a genuine decrease in the number of legal complete 15-atom permutations.
4. The moving thresholds' ranks and drops are **constant within each half-chamber**, but depend on the sign of η:

| Prefix loss q | η>0 rank | η>0 lost orders | η<0 rank | η<0 lost orders |
|---|---:|---:|---:|---:|
| 15 | 607 | **379,780,599,984** | 608 | **379,627,579,392** |
| 12 | 716 | **138,525,464,060** | 717 | **138,461,493,728** |
| 3 | 1041 | **12,916,391,928** | 1042 | **12,891,471,896** |

Hence two states invisible to the same complete observer, differing only by the **sign** of a sufficiently small kernel perturbation, exhibit distinct finite operation-order transition patterns.

## Proof and validation domain

For each labeled subset S⊆{1,…,15}, let P(S)=Σₐ∈S Mₐ. Its first-zero threshold is

`τ_S(η)=min_{k:P(S)_k<0} −(X_k+ηH_k)/P(S)_k`,

with the minimum computed over **all 28 original transfer coordinates**. Every candidate in this finite minimum is affine in η. If the minimum's coordinate index at η=±E also minimizes at η=0, the same affine coordinate remains minimizing throughout that closed half-interval: differences of affine functions cannot become negative strictly between two nonnegative endpoint values.

The accompanying checker enumerates every one of the **2¹⁵=32,768** labeled prefix subsets, forms all integer-scaled move sums, and for each nonempty subset verifies that the minimum-index set at +E and −E is a subset of its minimum-index set at 0 (allowing genuine ties at zero). It also checks the complete observer identities AH=0 and AMₐ=0, both perturbed states' strict positivity, both complete-ray endpoints' nonnegativity, and the unchanged boundary coordinate (target 0, source 2) certifying ε_max remains maximal.

Independently, the integer target-0/source-3 move weights

`(336,184,18,169,64,84,299,126,52,16,−420,−483,−144,−221,−80)`

generate exactly 1,144 distinct original interior threshold values through `ε_h=−36x/h` for relevant negative integer subset sums h. At each signed endpoint the full exact subset-minimum spectrum equals that fixed set union the three moving t_q and the endpoint ε_max. For every fixed t₀ value and for each moving t_q, the checker finds a minimizing witness at the corresponding unchanged physical coordinate. Combined with affine minimum-index stability, this proves the displayed **set equality throughout both half-intervals**, rather than just at two sampled parameter values.

At +E, each t_q is immediately **before** its old coincident target-0 resonance x/q; at −E, immediately **after** it. All fixed phase values and their order stay unchanged, so relative ranks are constant on each half-interval. The checker counts complete legal orders at rational midpoints on both sides of each moving threshold via exact Boolean-lattice dynamic programming:

`ways(S;ε)=1_[X(η)+εP(S)≥0] Σ_(a∈S) ways(S\\{a};ε)`, `ways(∅)=1`.

Legality of every prefix subset and its phase ordering is constant within each half-chamber; consequently the table of six exact losses holds for **every rational point** in each corresponding interval. The checker uses Python standard-library Fraction and integer arithmetic exclusively.

## Reproduction and evidence

The complete standalone Python 3 checker is losslessly stored as `VERIFY_BIDIRECTIONAL_R5.py.gz.b64`. Decode and run in a local copy of this folder:

```bash
base64 -d VERIFY_BIDIRECTIONAL_R5.py.gz.b64 | gzip -d > VERIFY_BIDIRECTIONAL_R5.py
python3 VERIFY_BIDIRECTIONAL_R5.py
```

Expected *decoded* Python script SHA-256: `cf872d4730eb03073506494aa3117ca3c9f5e381b3110bada82fc475877e0420`. Captured local execution: `EXACT_OUTPUT.txt`, SHA-256 `0cea4195f82a2325ef85f7e8eba6f290e61f6b195083f2fa03e7d560cb2b2d71`. Verified local pass marker: `PASS_R5_EXACT_BIDIRECTIONAL_RESONANCE_CHAMBERS`. Independent published-byte execution and mathematical review are next distinct checks.

## Next unit

Determine the **maximal exact endpoints** of the positive and negative η chambers from the first change in 28-coordinate minimizing indices, phase-value ordering, or original-state/endpoint admissibility. The two maximal widths need not coincide. Then investigate whether 15-move optimality remains robust for the corresponding endpoint pairs. This note preserves author-side proof provenance only; formal Source CLAIM, Result, review and native-X6 promotion are separately governed.
