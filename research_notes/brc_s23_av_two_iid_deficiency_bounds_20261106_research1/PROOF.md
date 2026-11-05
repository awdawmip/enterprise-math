# S23/AV: exact two-iid-trial reverse-deficiency interval with a sharp product-kernel bound

Date: 2026-11-06. Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`, source `research_notes/brc_n4_s23_asymmetric_hull_gap_sqrt43_20261101_research1/PROOF.md`. This continues the **author-side** one-trial theorem in PR #1777; status AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Exact experiment and quantifiers

The original frozen model has six separate tagged sources AU0, AU1, AV, BU0, BU1, BV and the *shared* lawful second-stage control `b`. Only the **conditional AV row** is used here. Fix any lawful common `b∈[1/8,1/2]`. For `a,c∈[1/2,7/8]` write `z=(1-a)c` and define three-stop and binary laws

`A_(a,c)=(a,z,1-a-z)` on (stop1,stop3,stop4);
`B_(a,c)=(z,1-z)` on (yes=stop3,no=otherwise).

Two trials are conditionally independent given the *same* unknown `(a,c)`. Thus `A2_(a,c)=A_(a,c)⊗A_(a,c)` on nine ordered outputs, and `B2_(a,c)=B_(a,c)⊗B_(a,c)` on four binary ordered outputs.

A reconstruction kernel `L` is **one** 4×9 row-stochastic matrix independent of `(a,b,c)`; it may jointly use both binary results. Define

`δ₂ = inf_L sup_(a,b,c)∈Q TV(A2_(a,c), B2_(a,c)L)`, `Q=[1/2,7/8]×[1/8,1/2]×[1/2,7/8]`, `TV(P,Q)=Σ|P_i-Q_i|/2`.

## Main theorem: rigorous new two-sample bounds

For all real lawful parameters,

**423/2468 ≤ δ₂ ≤ 18549/78400**,

i.e. approximately `0.1713938411 ≤ δ₂ ≤ 0.2365943878`.

More precisely, the universal product kernel `L=K⊗K`, with
`K(yes)=(0,1,0)`, `K(no)=(88/105,0,17/105)`,
has the **exact**, attained maximum reconstruction error

`sup_Q TV(A2_(a,c), B2_(a,c)(K⊗K)) = 18549/78400`.

This improves the earlier generic independent-coupling upper estimate `1-(1-9/70)^2=1179/4900` by the exact amount `9/2240`.

### Upper certificate valid over the full continuum

Let `C_(a,c)=B_(a,c)K=(v(1-z),z,(1-v)(1-z))`, `v=88/105`. Each component of `A_(a,c)` and `C_(a,c)` is **affine separately** in `a` and `c`.

Temporarily give the two trials independent formal parameters `(a₁,c₁),(a₂,c₂)∈[1/2,7/8]^2`, and form their nine-component signed difference

`F(a₁,c₁,a₂,c₂)=A_(a₁,c₁)⊗A_(a₂,c₂) - C_(a₁,c₁)⊗C_(a₂,c₂)`.

Every coordinate of `F` is separately affine in each of the four scalar parameters. Thus `F` at any real point in the 4D rectangle is a nonnegative convex combination of its 16 four-dimensional corner vectors, with product barycentric weights summing to one. Convexity of the total-variation norm yields

`TV(A_(a₁,c₁)⊗A_(a₂,c₂), C_(a₁,c₁)⊗C_(a₂,c₂)) ≤ max_(16 corners) TV(corner pair)`.

The 4×4 table of *exact* corner distances, with corner order `(1/2,1/2),(1/2,7/8),(7/8,1/2),(7/8,7/8)`, is

| first / second | (1/2,1/2) | (1/2,7/8) | (7/8,1/2) | (7/8,7/8) |
|---|---:|---:|---:|---:|
| (1/2,1/2) | 513/2450 | 19/140 | 241/1568 | 27333/156800 |
| (1/2,7/8) | 19/140 | 517/9800 | 677/6272 | 11367/78400 |
| (7/8,1/2) | 241/1568 | 677/6272 | 125/784 | 4941/25088 |
| (7/8,7/8) | 27333/156800 | 11367/78400 | 4941/25088 | **18549/78400** |

Every entry is at most `18549/78400`. The maximum occurs with *equal parameters in both trials*, `a=c=7/8`, so that vertex lies on the actual diagonal parameter subfamily. Restricting the proven 4D bound back to `(a₁,c₁)=(a₂,c₂)=(a,c)` proves the asserted exact full-real maximum for `K⊗K`.

### Lower certificate: two lawful hypotheses and one binary Bayes problem

Choose one common lawful `b=1/8`. Take `H₀:(a,c)=(1/2,1/2)` and `H₁:(a,c)=(7/8,7/8)`. Their single-trial conditional laws are
`A₀=(1/2,1/4,1/4)`, `A₁=(7/8,7/64,1/64)`;
`B₀=(1/4,3/4)`, `B₁=(7/64,57/64)`.

At the exact prior `t=P(H₁)=256/617`, the Bayes 0-1 risk `R(P₀,P₁;t)=Σ_i min{(1-t)P₀(i),tP₁(i)}` gives

`R_A2=R(A₀⊗A₀,A₁⊗A₁;t)=601/2468`,
`R_B2=R(B₀⊗B₀,B₁⊗B₁;t)=256/617`,
`R_B2-R_A2=423/2468`.

For any joint kernel `L`, put `e=max_{h∈{0,1}} TV(A_h⊗A_h,(B_h⊗B_h)L)`. Applying `L` followed by the optimal full-observation binary rule changes expected bounded loss under each hypothesis by at most `e`. Therefore `R_B2 ≤ R_A2+e`. Every candidate `L` has `sup_Q TV ≥ e ≥423/2468`, proving the universal lower bound. The displayed prior also maximizes the Bayes-risk gap for these two fixed hypotheses: the gap is continuous piecewise linear and all breakpoints `t=p/(p+q)` from the two product experiments are checked exactly in `VERIFY.py`.

## Meaning, evidence, next question

The result strictly strengthens the *lower bound* relative to the one-trial `9/70` and slightly improves the universal **product-kernel** two-trial upper bound. The exact optimal jointly-randomized `δ₂` remains the next problem. All 16 endpoint comparisons and exact Bayes calculations were executed using Python `Fraction`: 59 assertions passed. The all-real statement follows from the separately affine vector interpolation, not a finite parameter scan.

BRC carrier/observer audit: AV preparation identity and lawful common `b` remain typed; stop1/stop4 are collapsed by binary stop3 projection; two successive trials retain ordered trial identity and the common hidden parameter; the declared downstream operation is finite, hypothesis-independent decision-side randomization. The construction is source-conditional and remains distinct from the full ten-label lawful S23 policy/decoder minimax objective `R_beh(k,10)`. No change to mother bounds is asserted.

See SOURCES.md, VERIFY.py, RUN_EVIDENCE.txt, NEXT_TASK.md. Formal task CLAIM, external independent review, and canonical theorem admission were not obtained in this author-side unit.
