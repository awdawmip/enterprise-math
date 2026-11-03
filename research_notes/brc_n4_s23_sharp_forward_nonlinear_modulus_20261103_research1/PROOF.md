# BRC N=4 S23: exact global forward TV modulus for every constant-overwrite bank

Date: 2026-11-03. Status: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Source and scope

Frozen scientific input (unchanged): `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Direct predecessor: the unequal overwrite inverse-modulus theorem in `research_notes/brc_n4_s23_unequal_overwrite_sharp_moduli_20261103_research1/` at `690454aad6735fab2cbfb4063fc36dce2f12b1f8`. Preserve six labeled causal sources (i=0,...,5), four ordered outcomes, the shared eleven coordinates and the fixed nonuniform mixer; no projection onto unlabeled total mass. The application is a static stochastic observation problem, not a claim about native heartbeat-space physics or time evolution.

Write z=(z_0,...,z_10) in [0,1]^11 and

`A=(0,0,0,1,1,1)`, `B=(2,2,3,2,2,4)`, `C=(5,6,7,8,9,10)`.

For source i, define the ordered first-success distribution

`b(p,q,r)=(p,(1-p)q,(1-p)(1-q)r,(1-p)(1-q)(1-r))`

with p=z_{A_i}, q=z_{B_i}, r=z_{C_i}. The six labeled observable rows are

`P_j(z)=sum_i (M_{ji}/20) b(z_{A_i},z_{B_i},z_{C_i})`,

where

```text
M = [ [10,10, 0, 0, 0, 0],
      [ 9,11, 0, 0, 0, 0],
      [ 0, 0,20, 0, 0, 0],
      [ 0, 0, 0,10,10, 0],
      [ 0, 0, 0, 2,18, 0],
      [ 0, 0, 0, 0, 0,20] ].
```

Each mixing row is nonnegative and sums to 20. Let U_v apply any coordinate-constant overwrite of the first five coordinates, with constants fixed in advance and common to both inputs (different views may use different constants). Include baseline view v=0, U_0(z)=z; the two extra views of the four optimal masks (3,31), (7,27), (11,23), (15,19) are examples. Define

`d_V(z,w)=max_{v in V} max_{0<=j<6} TV(P_j(U_v z),P_j(U_v w))`

with TV(x,y)=1/2 sum_{k=0}^3 |x_k-y_k|, and `eps=||z-w||_infinity`.

## Theorem (sharp global nonlinear forward modulus)

For any finite bank V containing the baseline and any fixed overwrite masks/constants, and **every real eps in [0,1]**,

`max_{z,w in [0,1]^11: ||z-w||_infinity <= eps} d_V(z,w) = 1-(1-eps)^3 = 3eps-3eps^2+eps^3.`

Consequently, the **sharp global forward Lipschitz constant** is

`sup_{z != w} d_V(z,w)/||z-w||_infinity = 3.`

The statement applies simultaneously to all four minimum-two-probe masks and all independent overwrite constants beta_N,beta_E in [0,1], including endpoints. Unlike the inverse modulus, this forward modulus is independent of the overwrite design. For any fixed positive eps, the nonlinear bound improves on 3eps by `eps^2(3-eps)>0`.

## Proof — universal upper bound by an exact coupling

Consider an arbitrary source with branch parameters (p,q,r) and (p',q',r'). Independently maximally couple each pair of Bernoulli variables. A Bernoulli pair with success probabilities a,a' admits a coupling whose two bits agree with probability 1-|a-a'|, including both endpoints. Take the product of these three pair couplings. Both ordered first-success outputs are deterministic functions of the resulting respective three-bit triples. The two outputs coincide whenever the full triples coincide; hence the coupling characterization of TV gives

`TV(b(p,q,r),b(p',q',r')) <= 1-(1-|p-p'|)(1-|q-q'|)(1-|r-r'|).`

For any shared coordinate-constant overwrite U_v, its corresponding coordinates have difference zero, and other coordinates have difference at most eps. Thus each of the three branch differences is bounded by eps, and for every raw source

`TV(b_i(U_v z),b_i(U_v w)) <= 1-(1-eps)^3.`

For each labeled mixer row j, nonnegative weights M_ji/20 sum to one, so TV convexity under **common-weight** mixing yields

`TV(P_j(U_v z),P_j(U_v w)) <= sum_i M_ji/20 TV(b_i(U_v z),b_i(U_v w)) <= 1-(1-eps)^3.`

Taking the maximum over finitely many views and six labeled outputs proves the upper bound. This argument retains source labels, ordered outcomes and all shared parameters; it uses no source-independence assumption across the six observable rows (the coupling is constructed separately for each raw source).

## Proof — exact lower bound at every scale

Let z be the all-zero eleven-vector. For any eps in [0,1], form w by setting exactly coordinates `(0,2,5,6)` to eps and leaving all other coordinates zero. Then `||z-w||_infinity=eps`. For raw sources i=0,1 we have (p,q,r)=(0,0,0) at z and (eps,eps,eps) at w, because both share A_i=0, B_i=2, while C_0=5 and C_1=6. The baseline row j=0 is their 1/2–1/2 mixture. Thus its pair of observed distributions is exactly

`P_0(z)=(0,0,0,1)`, `P_0(w)=b(eps,eps,eps)`.

Their TV equals `1-b_3(eps,eps,eps)=1-(1-eps)^3`. As the baseline is included in V, the bank distance is at least this value. Equality holds for each eps by the upper bound.

For eps>0, divide by eps to obtain `3-3eps+eps^2`, which tends to 3 from below as eps tends to zero; the upper bound gives no larger ratio. Hence the sharp Lipschitz constant is 3. The supremum need not be achieved by a distinct pair at positive distance; sharpness is approached at infinitesimal scale. QED.

## Verification and logical reach

`VERIFY.py` uses Python standard-library `Fraction` to reconstruct all six source rows from the frozen A/B/C/M data. It checks 84 exact extremizers over 4 mask pairs, 3 overwrite-constant pairs and 7 rational radii, plus 1200 seeded rational input pairs, with 21600 labeled-view/row inequalities. `RUN_EVIDENCE.json` records the actual executed output. This finite test independently checks the formulas and implementation; the proof above covers the entire real parameter cube and all fixed masks/constants.

Reusable result: the exact modulus is an observer/coupling statement for a depth-three first-success causal branch, provided the bank includes a baseline containing a row mixing two sources that can simultaneously realize identical three-gate perturbations. The generic upper bound survives without such a witness; the particular equality uses the frozen S23 wiring.

Next problem: under an explicitly declared bounded-noise or finite-sample observation model, compare inverse stability and measurement cost of the three-view overwrite bank with single-view multiplicative attenuation, using this sharp forward modulus. A separate exact direction is to determine the sharp forward modulus for **overwrite-only** banks where the baseline is unavailable; that can depend on the masks/constants.

## Authority

This is an author-side mathematical theorem in the frozen S23 stochastic model; Source publication is not a native authenticated CLAIM/Result, independent mathematical review, theorem admission, P000 modification, or physical implementation claim. Tool reuse: `REUSE_APPLIED` for the predecessor's branch/mixer/frozen proof definitions; `COMPOSE_APPLIED` for the established total-variation coupling and overwrite observation map. No new shared BRC family is proposed.
