# R5: exact phase transition under a history-sensitive positive P/Q kernel perturbation

Date: 2026-11-06 Asia/Shanghai. Researcher-ID: `EM-DIRECT-C399A0`; Research-Activity-ID: `RA-A1EF4B8DCE437AB79704415D`.
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Question and frozen scientific inputs

The R5 mother question asks for a finite strictly positive P/Q stopping BRC with equal FULL_HIST and seedless-LR **complete four-observer convex hulls**, but distinct real-behavior images. This note supplies an **exact one-parameter phase diagram** for strict hull separation in the previously checked four-stage model S; the mother question stays open.

Scientific freeze: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; EM `86149263e38c22292c9def1e0f69092efa1be77e`. Immediate verified precursor: EM `794d893322b77898858c657f90f2674c432eb87d`, `research_notes/brc_r5_pairwise_cone_certificate_20261105_t2350/{RESEARCH.md,VERIFY.py}`. Current P000, ACTIVE Heartbeat World, joint relation/observer preservation and portable research rules are applied as current *behavioral* context, not moved into the frozen science sources. This finite BRC is a typed auxiliary observer experiment; no claim about native X6 rotation dynamics.

## Complete model

Time 1 starts with likelihood ratio r=1. At time 2, ratios `R2=(3/4,5/4)` have Q masses `Q2=(1/2,1/2)`. At time 3, ratios `R3=(1/2,1,3/2)` have Q conditional rows `Q3[0]=(13/20,1/5,3/20)`, `Q3[1]=(1/40,9/20,21/40)`. At time 4, terminal ratios `R4=(1/10,1,19/10)` have Q rows indexed by time-2 history i and time-3 ratio j:

- `Q4[(0,0)]=Q4[(1,0)]=(509,382,9)/900`.
- `Q4[(0,2)]=Q4[(1,2)]=(9,382,509)/900`.
- `Q4[(1,1)]=(67/162,14/81,67/162)`.
- `Q4[(0,1);δ]=(1/90+δ,44/45-2δ,1/90+δ)`.

The only new parameter is `δ` in the last row, within the **entire strict-positivity interval**
[
-rac1{90}<delta<rac{22}{45}.
]
Every Q row sums to 1 and has mean equal to its parent likelihood ratio. Define conditional P probabilities by `P(child|history)=Q(child|history)*r_child/r_parent`; P rows therefore also normalize and are strictly positive throughout the interval. The time/ratio observation keys, including the two-history merger at (time 3,r=1), are unchanged for every δ. Full history still distinguishes i=0 from i=1 at that merger.

At any stopping time choose P or Q declaration. Use the complete observation
[
W=(P[mathrm{declare Q}], Q[mathrm{declare P}],mathbb E_P	au,mathbb E_Q	au),
]
and direction `n0=(-1,-1,-3/25,1/50)`. FULL_HIST may condition actions on all tree history; seedless LR uses only (time, current likelihood ratio), with arbitrary real randomized behavioral actions in both classes.

## Theorem (exact positive-family support diagram)

For every real parameter `-1/90 < δ < 22/45`, define the full and seedless LR support maxima at n0. Then exactly
[
h_{m LR}(delta)=-rac{429}{400}
 +maxleft(0,rac9{100}left(delta-rac{13}{180}ight)ight),
]
[
h_{m FULL}(delta)=-rac{107}{100}
 +maxleft(0,rac9{100}left(delta-rac1{10}ight)ight).
]
Hence the precise history-information support advantage is
[
oxed{quadDelta(delta)=h_{m FULL}(delta)-h_{m LR}(delta)
=minleft{rac1{400},
 maxleft(0,rac9{100}(rac1{10}-delta)ight)ight}.quad}
]

In particular, the gap is 1/400 for `-1/90<δ<=13/180`, decreases linearly on `13/180<δ<1/10`, and is zero for `1/10<=δ<22/45`. The latter is **equality of the support values at n0**, not equality of the complete four-dimensional convex hulls or real-behavior images.

### Proof: affine envelopes and exact endpoint certificates

**Lemma (endpoint affine envelope).** For a fixed finite acyclic tree with a one-dimensional affine perturbation of a single conditional probability row, and fixed strategy information keys, the n-direction expectation of *every deterministic policy* is affine in δ. The support maximum of the finite set is therefore convex and piecewise-affine. If an endpoint pair `δ0<δ1` has support values on an affine line L and one fixed deterministic policy achieves L at both endpoints, then the support equals L throughout their interval: the upper bound is convex interpolation of endpoint maxima, and the fixed policy supplies a matching affine lower bound. This covers the interval's entire continuum, not a parameter grid. Because each path in this acyclic tree meets the perturbed row at most once, each deterministic policy value really is affine in δ, both for P and for Q.

**Exact endpoint evaluations.** The attached Fraction program enumerates all `3 * 3^2 * 3^3 * 2^3 = 5832` deterministic seedless LR policies at each endpoint, including time-1 stop, both declarations, all stop/continue choices and terminal declarations. An independent full-history backwards Bellman recurrence computes the FULL maximum. The exact table is:

| δ | h_LR | h_FULL |
|---|---:|---:|
| -1/90 | -429/400 | -107/100 |
| 13/180 | -429/400 | -107/100 |
| 1/10 | -107/100 | -107/100 |
| 22/45 | -207/200 | -207/200 |

The two outer endpoints have some zero conditional entries and are used only in the closed mathematical extension for interpolation; every interior model in the theorem is strictly positive.

**Fixed witness actions.** Write `B(r,t)` for the declaration maximizing the direction value at likelihood ratio r and stopping time t: choose Q for r<=1 and P for r>1 (ties at r=1 arbitrary). Every witness below continues at time 1, uses B at each stop, stops at all time-3 nodes except the ratio-1 nodes explicitly stated, and uses B at all terminal nodes.

- `LR_LOW`: stop at time 2 on i=0; continue time 2 on i=1, then continue from the single observed time-3 ratio-1 node.
- `LR_HIGH`: continue time 2 on both histories; continue from the common time-3 ratio-1 node.
- `FULL_LOW`: continue time 2 on both histories; at time-3 ratio 1 stop history i=0 and continue history i=1.
- `FULL_HIGH`: continue time 2 on both histories; at time-3 ratio 1 continue for both histories.

The attached program directly evaluates their Q/P-weighted full stop/declaration payoffs. `LR_LOW` yields -429/400 at both -1/90 and 13/180; `LR_HIGH` yields the line `-429/400+(9/100)(δ-13/180)` at 13/180 and 22/45. `FULL_LOW` yields -107/100 at both -1/90 and 1/10; `FULL_HIGH` yields `-107/100+(9/100)(δ-1/10)` at 1/10 and 22/45. Apply the endpoint-affine lemma to these four intervals, obtaining both support formulas. Subtraction gives the boxed gap. QED.

### Interpretation of the thresholds

The varied time-4 row preserves the parent ratio 1, but changes the history-i=0 value of *continuing* from the common time-3 ratio-1 node. At n0 the change in that branch's conditional Bellman reward is exactly `(9/10)δ`, and its unconditioned Q mass is 1/10 when reached. It changes the globally weighted increment by `(9/100)δ`. For `δ<13/180`, the two opposed optimal history-specific decisions yield the fixed 1/400 information advantage. At `δ=13/180`, an additional shared-gate LR policy becomes tied; after it, the LR common-continue policy rises linearly. At `δ=1/10`, even the history-i=0 individual gate becomes indifferent; beyond this threshold both observers can use the common continue choice without support loss at n0.

Thus a **strictly positive, history-nonlumpable P/Q family** exhibits a stable gap plateau, a linear closing window and a zero-gap region **without changing any LR observation key**. This is a parameter-controlled mechanism to study whether full hull equality can be attained while retaining image-level path residuals.

## Verification, exact scope and continuation

Attached `VERIFY.py` uses Python standard-library Fraction. It checks every row's normalization, parent LR mean, endpoint support for 5832 deterministic LR strategies each, independent FULL dynamic programming, four explicit fixed-witness affine lines, and 7 strictly positive interior rational parameters. Actual stdout is in `EXACT_OUTPUT.txt`. The universal real-δ theorem is the envelope proof plus certified finite endpoint bounds; the interior tests are diagnostics. No independent reviewer or canonical Result is asserted.

**Next discriminating problem.** For `1/10<=δ<22/45`, certify all four-dimensional directions, not only n0: build a complete deterministic observation-polytope comparison (rational Carathéodory <=5 per FULL deterministic extreme point, or rational Farkas separation) with history-specific Q4 rows preserved. Independently test actual seedless LR real-policy image membership for a FULL witness if hull equality holds. Test near `δ=1/10` and `δ=1/4` first, retaining exact positivity and unchanged time/ratio keys. Alternatively derive a normal-fan comparison that captures all declaration/tie boundaries.