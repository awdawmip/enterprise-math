# Stage170 — author exact full-real optimality interval, external ternary N14 IID

**Scientific status (2026-10-26):** Author-side exact proof with two independent computational implementations of the declared model; native Enterprise Math research CLAIM, independent Driver review, Lean formalization, and P000 correspondence **not established**. This file is a full reasoning record, not automatic Foundation promotion.

## Frozen sources, model and target

Global canonical GLOBAL_KNOWLEDGE_V1 `main@5b3f7e5293e021f6717d336b3d15991ec556a445`; Enterprise Math main `b695d1473879c0aaebc4a1949df4d6cdd0242ca0`; immutable Stage169 author result and dual Stage170 candidate `9633df132e69a21069260c9ac1a1ad5a2ef0f43b` under `research_notes/n14_aux_iid_affine_169_r2_author_20261026/`. Distinct control/read and historical proof pins are not interchangeable.

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Consider all randomized stopping and binary-decision policies on **full ordered** ternary IID histories, required to stop by sample 14. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P[tau], tQ=E_Q[tau] and V14(alpha)=min{max(tP,tQ):eP,eQ<=alpha}. This is an external finite probabilistic auxiliary model, not an alternative definition of the six-dimensional native Cell space.

## Exact statement

Define

```text
alpha169 = 882433753904177815735/2530093150022563528704
V169     = 4191297370163761372757/361441878574651932672
eta170   = 152674215625/274532676868767744
S170     = 28504525/56787
alpha170 = 126062165849964145105/361441878574651932672
V170     = 4191196473918241372757/361441878574651932672
```

**Theorem.** For every real delta in [0,eta170], including irrational delta,
`V14(alpha169+delta)=V169-S170*delta`.
For any real alpha>alpha170, the Stage170 affine lower-support line `Hroot-S170*alpha` is **strictly below** V14(alpha). This does not assert any discontinuity or global termination at alpha170.

## Dual derivation: complete 680-state rational Bellman table

At s=(n,a,b), a counts symbol 0 and b counts symbol 1. Its prefix likelihood ratio Q/P is `ell(s)=2^(a+b)/3^a`. With

```text
K=4773735/18929
L=14183320/56787
K+L=28504525/56787
Hroot=290341590799397120042729/1555410727388508585984
```

backward induction uses `H(s)=min(K*ell(s), L, 1+sum_i P_i H(child_i(s)))` (omit continuation at depth 14). For **any full-history** randomized policy, `Hroot<=tP+K*eQ+L*eP`, because identical IID conditional futures permit this lower bound on every ordered prefix, not just count-based strategies. Every feasible policy therefore obeys
`max(tP,tQ)>=Hroot-(K+L)*alpha`.

A Python `Fraction` exhaustive enumeration has exactly `sum_{n=0}^{14} binom(n+2,2)=680` count states. All 1,238 nonwinning action differences are strictly positive, minimum `569/56787`, with zero negative differences. Exactly two ties:
`R=(10,0,1)`: stop Q / continue;
`T=(12,5,2)`: stop P / continue.
This exhaustive finite Bellman certificate is valid for all ordered-history policies by the preceding conditional-suffix argument.

## Primal realization and independent exact path computation

At R, stop Q with probability r; at T, stop P with probability t, and otherwise continue; at every other state take the unique Bellman action. R has zero symbol-0 occurrences at depth 10 whereas T has five by depth 12. Hence neither first-hit prefix cone can contain the other.

The exact independent first-hit path counts/masses are

```text
R:   10 ordered paths; P=9765625/120932352; Q=9765625/60466176
T: 5162 ordered paths; P=8065625/73383542784; Q=8065625/139314069504
```

For all four deterministic coin corners (r,t)=(0,0),(0,1),(1,0),(1,1), two independently structured methods agree *exactly* in all 16 observer entries of `M=(eP,eQ,tP,tQ)`:
(i) rational conditional suffix dynamic programming and
(ii) literal unmerged ordered-history integer-numerator DFS using P=(3,1,20)/24 and Q=(1,1,10)/12, with positive prefix masses preserved separately.

The DFS visits respectively **352333, 321361, 352093, 321121** nodes, total **1,346,908**. Terminal P and Q masses separately equal one for each corner. The cross difference `M11-M10-M01+M00=(0,0,0,0)` proves for this declared observer `M(r,t)=M00+r*dR+t*dT`.

Let `D(M)=eP-eQ`. The unique exact balancing relation is

`r(t) = 8976558429259453/11823616000000000 + (5541407/3694880000)*t`.

For all real t in [0,1], r(t) is in (0,1). Balancing gives a common error alpha(t), strictly increasing affinely from alpha169 (t=0) to alpha170 (t=1); width exactly eta170. The time advantages are

```text
(tP-tQ)(0)=939181182760914408775/2530093150022563528704 >0
(tP-tQ)(1)=134198175358476229825/361441878574651932672 >0
```

At both endpoints, `tP+K*eQ+L*eP=Hroot`, and therefore it holds throughout by affinity. Likewise tP>=tQ throughout. Thus the constructed policy attains `max(tP,tQ)=tP=Hroot-(K+L)*alpha(t)`, which matches the Bellman lower bound. Exact endpoint equality and affine interpolation establish the theorem for the **entire real interval**, not merely tested rational points.

## Strict right-support sharpness

The finite tree of all histories and randomized actions gives a compact finite-dimensional observer polytope, so constrained optima are attained. Were `Hroot-(K+L)*alpha` attained for alpha>alpha170, positivity K,L>0 and the two lower-bound inequalities would force `eP=eQ=alpha`, `tP>=tQ` and Bellman-optimal actions on every reached positive-probability history. Since all symbol probabilities are positive, only R/T may mix.

Coins can depend on individual ordered histories even at the same tied count state. But Q/P prefix likelihood ratios are identical within each count state, and the IID conditional suffix-observer differences are identical. Weighting those coins by their P first-hit masses gives one effective r and t preserving all four observer coordinates. The two first-hit cones are disjoint, so no mixed dependence is lost in this observer-specific reduction. Balance uniquely imposes r=r(t); legal t∈[0,1] entails alpha(t)<=alpha170, contradiction. Hence this particular support line is strictly unattained to the right. No other support lines are classified by this claim.

## Verification scope and live control

The actual executed author verifier `VERIFY_STAGE170.py`, run log, exact certificate, separately executed Stage171 candidate scan, and hashes are in the portable author evidence bundle; the GitHub `VERIFY_STAGE170_REFERENCE.py` is a shorter **reference** reproduction and GitHub file readback does not mean it was remotely executed. All arithmetic of this finite certificate uses exact rationals, no floating-point tolerances. Branch-positive P/Q histories and provenance are retained. Positive BRC-style branch weights are not signed amplitudes. This external model has no proven P000-X6 embedding or typed native Heartbeat/BRC correspondence.

Current GitHub authenticated actor is `awdawmip` with repository push permissions. Native `em_control_tasks` responded `CONTROL_QUOTA`; the actual live Task owner, native CLAIM, Driver review and Source Result remain **unverified/unobtained**. This author evidence is stored on a research branch, not represented as main-merged Foundation truth.

**Next frontier Stage171 (DUAL ONLY):** Ray from K170,L170 with dK=-1, dL=-10592/12501, keep R Q/continue tied and T P fixed. The rational scan first closes at `U=(12,4,3)` Q/continue at step `128035242/28942441`; candidate `K171=378837/1529`, `L171=1128472/4587`, `Hroot=332293501648867121767/1807757198084800512`. Exactly 1,238 other positive gaps (minimum `3442966771823/94671649898496`). **Stage171 primal remains open**. Test its two-coin path observer, legal balanced interval and strict support, or give an exact obstruction.
