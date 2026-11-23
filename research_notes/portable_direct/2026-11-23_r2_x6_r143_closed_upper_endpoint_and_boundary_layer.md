# X6 R143 — closed upper endpoint of the uniform BRC near-direction tube

Date: 2026-11-23 (Asia/Shanghai). Status: **author exact rational proof/certificate PASS; independent mathematical review pending**.

## Frozen scientific scope and sources

Continue R140–R142 without changing the four-positive-weight, six-pair BRC observer, P000 V5, the ACTIVE Heartbeat World or the original task input pins. The scientific input pins remain `awdawmip/enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd` (R121 exact optimizer) and `@0687aa24f5402da3b35f914dd6907967a9805b94` (R122 exclusion). Reuse R138 at e8e20fdfce40d5415e2f02b51983c7c5928d30ce, R140 at 32d116d425dcc7fe23563aafa7a1eb9278a47428, R141 at the same commit and R142 at c1f42b907be3ec3e6617184ce7a8049887e34475 (all in `research_notes/portable_direct/`).

The Port is the integer 10. For a nonzero integer direction `a=(x,y,z)` with `q(a)=max(sum positive coordinates, sum absolute negative coordinates)<=10`, identify `a` with `-a` but do not identify other multiples. There are exactly 1,935 such unoriented directions. Define

- `h(a)=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)`;
- `g(a)=(|h_j-h_i| : 0<=i<j<=3)`, ordered by the six pairs;
- `s(B,D)=(136+B,312,136+D,B+176,B+D,176+D)`;
- `F_D(a)=max_j(g_j(a)/s_j(B,D))`, `eta_D(B)=min_a F_D(a)`;
- `N_D(B)={a modulo ±: 2 F_D(a)<3 eta_D(B)}`.

All of these are a conditional six-pair observer on a declared centered-three-axis slice; none asserts a theorem about the full native six-dimensional physical dynamics.

## New theorem: the previously open upper endpoint is attained for every positive B

Let `C={(1,0,0),(5,-4,1),(5,-1,0),(9,-5,1)}/±`. Then

**For every real B>0 and every real D with 448<=D<=528, the complete strict-near set is exactly C.**

R140 proved `472<D<528` uniformly in B; R141 sharpened the lower side to `448<=D<=500`. The new result is the **closed upper face D=528**. The largest *uniform* upper expansion remains 28 because any upper enlargement loses a direction at some small positive B (R140).

There is a meaningful distinction between a uniform limit and a pointwise limit: the only equality obstructing the R140 insider margin occurs at `B=0`, which lies outside the positive-weight domain. At the boundary extension `(B,D)=(0,528)`, which is **not** an admissible positive weight, the exact optimizer is `eta=1/88` and the near set is `C\{(9,-5,1)}`. Thus the upper face is included at every allowed B>0 but the near set does not extend continuously to the excluded zero-weight corner.

## Proof of the closed upper face

Write `F_0=F_500`, `eta_0=eta_500(B)`. The exact seven R138 optimizer chambers partition B>=0 at

`0, 316/7, 320/7, 46, 556/7, 796/7, 136, +infinity`.

On the successive chambers `eta_0=K/(L0+L1 B)`, with triples

`(6,500,1), (7,636,0), (2,136,1), (6,500,1), (7,676,0), (3,176,1), (1,104,0)`.

R140's exact integer-direction certificate (reproduced by the companion verifier) establishes for every B>=0:
1. `F_0(a)>=8 eta_0/5` for each of the 1,931 outsiders `a notin C`.
2. For each of the four insiders, `F_0(a)<=125 eta_0/88`. The 168 affine pairwise inequalities are `H(a,j,B)=125K*s_j(B,500)-88*g_j(a)*(L0+L1 B)>=0` on each of seven chambers.

**Strictness refinement:** inspect the 168 affine inequalities at both ends of all six bounded chambers and at the last ray's finite endpoint and recession slope. They are nonnegative everywhere, and the only equality at a finite point is

`B=0, a=(9,-5,1), j=(1,2)`, the fourth capacity `s_4=B+176`.

On the first B-chamber this equality polynomial is exactly `H=486 B`, so it is strict for every B>0. The remaining chamber endpoints are strictly positive; any zero recession slope has a strictly positive endpoint value. Therefore, for **all B>0** and **all a in C**,

`F_0(a)/eta_0 < 125/88`.

For `500<=D<=528`, every changed denominator is increased by D-500, and for every gap/denominator channel the distortion ratio obeys

`500/D <= s_j(B,500)/s_j(B,D) <=1`.

Taking maxima and minima yields `(500/D) F_0(a)<=F_D(a)<=F_0(a)` and `(500/D) eta_0<=eta_D<=eta_0`. Hence outsiders satisfy

`F_D(a)/eta_D >= (500/D)*(8/5) >=50/33>3/2`;

insiders satisfy

`F_D(a)/eta_D <= (D/500)*(F_0(a)/eta_0) < (528/500)*(125/88)=3/2`.

Both inequalities are strict at D=528 for every B>0. Combine with the independently proved R141 lower interval to obtain the full closed strip.

At the **excluded** B=0,D=528, `eta>=500 eta_0/528=1/88`; `a=(1,0,0)` attains `F=1/88`. The direction `(9,-5,1)` has `F=3/176=3eta/2`, so it is excluded. The other three insiders and all outsiders are classified by the preceding strict bounds; the exact near set is the asserted three-direction set.

## Quantified boundary-layer conditioning

The earlier R136–R137 theorem already gives for `0<B<=20`, on the upper face `D=528`:

`eta_528(B)=6/(B+528)`, `F_528(9,-5,1)=3/(B+176)`.

Thus its normalized strict-nearness slack is **exactly**

`3/2 - F_528(9,-5,1)/eta_528(B) = B/(B+176)`.

This tends to zero linearly as B tends to 0 from above. In that same already-classified B-range, the first upper loss occurs at `D=528+2B`: the direction `(9,-5,1)` exits at equality. The novelty here is the proof that D=528 itself is included **uniformly in its D coordinate**, despite the complete lack of a uniform positive membership margin as B tends to zero.

## Reproducibility, provenance and next question

The standalone `x6_r143_upper_closed_endpoint_verify.py` enumerates all 1,935 directions, checks the seven-chamber optimizer lower and attaining witnesses (13,545 rows), excludes all outsiders (13,517 rows), checks 168 insider margin inequalities with exact affine endpoint/recession arithmetic and identifies the **unique zero** at B=0. It also verifies the limiting point and four rational positive-B boundary-layer examples using `fractions.Fraction`.

Local result: `R143 UPPER CLOSED ENDPOINT CERTIFICATE PASS`; no floating-point evidence is needed. These are author calculations and proofs; independent review remains pending. Scientific Source publication, Activity checkpoint, formally authenticated CLAIM/Result/Review and account journal are distinct statuses.

**Next scientific question:** classify the exact *first upper loss wall* `D_*(B)` and its direction labels for all B>20 (R137 covers 0<B<=20). Determine the first external-direction entry and any nonmonotone member changes beyond the wall; do not assume the B<=20 formula extrapolates.
