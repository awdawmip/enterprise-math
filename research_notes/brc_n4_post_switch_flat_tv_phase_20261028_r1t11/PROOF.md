# Enterprise Math / BRC: exact post-switch N4 common-TV flat phase

2026-10-28 Asia/Shanghai. **AUTHOR_EXACT_PROOF / EXACT_FRACTION_PASS / UNREVIEWED / NOT_ADMITTED**. Author-side portable research only. Native owner query returned `CONTROL_QUOTA`; no canonical CLAIM or independent review is asserted.

**Source pins:** GLOBAL_KNOWLEDGE_V1 `awdawmip/chatgpt-global-knowledge main@5b03e7f250babaf694305861ca991d84fe4cdffc` (normative entries, P000 projection and original blob verified equal, ACTIVE worldview); Enterprise Math `main@4a285e59dbb40ef554edd4a5ef871bbd361fe85b` (AGENTS, native X6 and time, observer preservation, portable research protocol). The mathematical predecessor is `research_notes/brc_n4_lambda_partial_tv_phase_20261028_r1t11/{PROOF.md,VERIFY.py}`. Previous author-side result: for 0≤λ≤26911/39215, d2=1/506, d3=(1−λ)/2000, d23=727/314040−31λ/62808. Its d3 formula extends to all λ∈[0,1].

## New exact theorem

Put λ₀=26911/39215 and λ₁=27483/39215. For **every real λ∈[λ₀,λ₁]** on the same strictly positive N=4 two-law tree, with the same Fλ and three local behavioral strategy classes S2,S3,S23:

```
d2(λ) = d23(λ) = 1/506,
d3(λ) = (1−λ)/2000,
d2+d3−d23 = (1−λ)/2000 >= 2933/19607500 > 0.
```

This is a strictly positive new phase interval, width 52/3565, **after** the predecessor's first support switch. The true common total-variation joint-compression cost has a flat segment despite a positive t3-only cost. This is not a claim that λ₁ is the ultimate switch.

## Exact frozen tree and observer

At t1: A:(q,r)=(1/2,1/2), B:(1/2,3/2). At t2: AU=(1/6,1), AV=(1/3,1/4), BU=(1/4,1), BV=(1/4,2). Every t2 parent branches into Q-mass q/2 children with ratios r(1±e), e=(1/10,0,4/5,0). Every t3 parent branches similarly at t4 with e_AV0=0,e_AV1=3/50, and e=1/20 otherwise. P mass is q*r; both laws conserve mass and all branches are positive. At t1 Fλ continues; at t2 AU and BV STOP P, AV and BU continue; at t3 AV0 STOP Q with probability 1−λ, continue λ, AV1 and BU0 continue, BU1 STOP Q, others STOP P; t4 uses Q iff 100r<2501/100. Equal (t,r) histories must use identical fresh local P/Q/C mixtures at the constrained level(s); no persistent common seed. Observer: both laws' full joint distributions of (T,D) in event order (1P,1Q,2P,2Q,3P,3Q,4P,4Q).

## Constructive upper bound

Define affine occupancy variables:

```
a = (7843 λ + 22989)/72358
s = z = (39215 λ + 44303)/72358
k = 307(181−253 λ)/289432
m = 3(8198−1265 λ)/36179
```

A jointly compressed *behavioral* strategy is: at t1 continue; at t2 AU/BU share (P,Q,C)=(a,0,1−a), AV=(1−s,0,s), BV=P; at t3 AU0/AU1=Q, AV0/AV1 share (0,(s−z)/s,z/s)=(0,0,1), BU0=C, BU1=(0,m/(1−a),1−m/(1−a)), BV0/BV1=P; at t4 r=1/4 uses (P,Q)=(k/z,1−k/z), all other r use the original threshold.

Feasibility inequalities are 0<a<1, 0<z=s≤1, 0≤k≤z, 0≤m≤1−a. Their values are affine, so it suffices to check endpoints. At λ₀, (a,s,z,k,m)=(496/1265,249/253,249/253,307/39215,4767/7843). At λ₁ they equal (498/1265,251/253,251/253,307/78430,4755/7843). Every inequality holds and the denominators stay positive throughout the interval.

The full-history target observations are
```
QF=(0,0,5/12,0,0,7/24−λ/6,1/12,5/24+λ/6)
PF=(0,0,2/3,0,0,4/15−λ/24,53/2400,107/2400+λ/24).
```
Exact propagation of the displayed joint strategy gives the **entire signed difference vectors**
```
Qσ−QF = (0,0,A,0,0,B,0,−1/506)
Pσ−PF = (0,0,−1/506,0,0,0,0,1/506)
A = (27483−39215λ)/289432  >= 0
B = (39215λ−26911)/289432 >= 0
A+B = 572/289432 = 1/506 .
```
One can independently verify them from the following occupancy-flow equations, all affine in (a,s,z,k,m):
```
Q2P=5a/12+(1−s)/3+1/4; Q3Q=(1−a)/6+(s−z)/3+m/8;
Q4P=k/6+z/12+(1−a−m)/8; Q4Q=(z−k)/6+z/12+(1−a)/8.
P2P=5a/12+(1−s)/12+1/2; P3Q=(1−a)/6+(s−z)/12+9m/40;
P4P=k/24+53z/2400+9(1−a−m)/40;
P4Q=(z−k)/24+47z/2400+(1−a)/40.
```
Both sides of the differences are affine in λ, so verifying the two rational endpoints (or comparing affine coefficients) proves every real λ case, not only a grid. Both law-specific TV distances therefore equal 1/506. Since σ∈S23⊂S2, d23,d2≤1/506.

## Global lower bound, all real behavioral policies

The **same** exact S2 dual as in `research_notes/brc_n4_fprime_partial_unmask_strict_subadd_20261028_r1t11/VERIFY.py` is reused and independently re-enumerated in the attached VERIFY.py:
```
wQ=(0,0,25/253,0,3/2024,25/253,25/253,−25/253)
wP=(0,0,−203/506,0,0,−197/506,−197/506,203/506).
```
For L(σ)=EQ[wQ]+EP[wP], osc(wQ)+osc(wP)=1. Grouped exact backward minimization on the full positive tree, enumerating 3²·3³=243 deterministic t1/t2 grouped prefixes, gives min_{σ∈S2} L(σ)=−153/506. The score is multi-affine in independent signature action probabilities (a path can visit a fixed time-signature at most once). Successive simplex vertex replacement makes this finite grouped Bellman minimization **globally valid for all real independent instantaneous randomizations**, rather than only sampled probabilities.

The fixed Fλ satisfies L(Fλ)=−7/23=−154/506 at every λ: moving Q mass λ/6 and P mass λ/24 from (3,Q) to (4,Q) makes precisely canceling changes in the dual score. For every σ∈S2, hence also S23,
```
1/506 ≤ L(σ)−L(Fλ)
      ≤ osc(wQ) TV_Q + osc(wP) TV_P
      ≤ max(TV_Q,TV_P).
```
Thus d2,d23≥1/506; this matches the concrete behavior. The predecessor's independent all-[0,1] formula for d3 establishes the strict gap. The theorem is **specific to this external finite tree and observer**, not a uniform statement over all F or all native dynamics.

## Evidence, BRC, and unresolved work

Actual execution: Python standard-library Fraction rebuilt 2/4/8/16 positive nodes, checked P/Q parent conservation, common (t,r) behavior at t2/t3/t4, full leaf-transport observations, exact endpoint and interior residual vectors, both TV norms, the w2 oscillation and target score, and 243 exact Bellman prefix cases. Run status `PASS_EXACT_FRACTION_N4_POST_SWITCH_FLAT_PHASE`. The affine endpoint argument supplies universal real-λ proof; finite computation alone would not.

Typed BRC reuse is substantive: ordered positive rational branch masses, LR, tagged hidden-source kernels, double-law observer and residual that persists after quotienting histories by (t,r). The new zero-increment phase moves error support between observable coordinates while keeping TV unchanged. It does not discard the path residual or prove it physically absent. The P000 world is native six-axis discrete X6 Cells plus independent time, no native plane. No faithful embedding of this external probability tree into X6 Cell evolution and future operations is established.

**Next precise task:** for λ>27483/39215 determine the first genuine *global* minimax support switch and the next exact piece of d2,d23, with an implementable common behavioral strategy and matching full-class Bellman dual. A sign change for this particular witness is not a proof that no other flat witness exists. Native CLAIM, independent Driver review, Lean and P000 X6 observer-preservation bridge remain pending.
