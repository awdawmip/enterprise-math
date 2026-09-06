# RH `H_log3` constant-floor negative-index certificate

Status: `TASK_RESEARCH / VERIFIED FULL-WINDOW FINITE NEGATIVE-INDEX UPPER BOUND / NOT FULL POSITIVITY / NOT AN RH PROOF`
Date: `2026-09-06`
Researcher-ID: `EM-DIRECT-7C1A42`
Scope: `RH / Weil form / H_log3 / full infinite-dimensional window / Birman-Schwinger trace bound / Arb certificate`

## 0. Main result

Let

`H_log3={f in L2(R): supp f subset [-log3,log3]}`

and retain the exact active non-pole scalar multiplier

`a(t)`
`=Re psi(1/4+i t/2)-log pi`
` -2 sum_(m in {2,3,4,5,7,8}) Lambda(m)/sqrt(m) cos(t log m)`.

The boundary shift `m=9` is operator-null because `log 9=2log3` equals the support diameter.

Define

`b(t)=(1-a(t))_+`

and the positive time-frequency operator

`W=P_L F^(-1) b F P_L`, `L=log3`.

A production 192-bit Arb upper-integration certificate proves

`boxed: Tr W < 79.32463645912487 <80}`.

Consequently

`boxed: n_-(Q_nonpole on H_log3) <=79}`.

The pole operator has exactly one negative channel, not two. Therefore

`boxed: n_-(Q_full on H_log3) <=80}`.

This is the first direct finite upper bound on the negative index of the **entire infinite-dimensional `H_log3` Weil form** in this research line.

It does not prove positivity and does not prove RH.

## 1. Constant-floor Birman-Schwinger reduction

Pointwise,

`a(t) >= 1-b(t)`.

After compression to the support window,

`Q_nonpole >= I-W`.

Therefore, by min-max monotonicity,

`n_-(Q_nonpole) <= n_-(I-W)`
`= #{j: lambda_j(W)>1}`.

The function `b` is nonnegative and compactly supported because the multiplier is eventually larger than one. Hence `W` is positive trace class.

For any positive trace-class operator,

`#{lambda_j(W)>1} < sum_j lambda_j(W)=Tr W`.

Thus any strict certificate `Tr W <N` gives

`n_-(Q_nonpole)<=N-1`

for integer `N`.

## 2. Exact trace identity

Under

`f_hat(t)=integral f(x)e^(-itx) dx`,

compression of a nonnegative Fourier multiplier `b` to `[-L,L]` has diagonal kernel

`(1/(2pi)) integral_R b(t) dt`.

Therefore

`Tr W`
`=(2L)/(2pi) integral_R b(t)dt`
`=L/pi integral_R (1-a(t))_+ dt`.

Since `a` is even,

`Tr W=2L/pi integral_0^infinity (1-a(t))_+dt`.

No finite Galerkin basis enters this identity.

## 3. High-frequency tail closure

Reuse the active comb constant

`A_log3=2 sum_(m in {2,3,4,5,7,8}) Lambda(m)/sqrt(m)`
`=6.34259743608709162639498634971...`.

The same Binet bound used in the negative-symbol capacity certificate gives

`a(t)>=LB(t)`

with

`LB(t)`
`=1/2 log(1+4t^2)-log(4pi)`
` -2/(1+4t^2)-1/(3t)-A_log3`.

`LB` is strictly increasing for `t>0`.

The production Arb run certifies

`LB(10000)`
`=1.02983253239641230372048663423949... >1`.

Hence

`boxed: a(t)>1 for every |t|>=10000}`.

Therefore `b(t)=0` identically outside `[-10000,10000]` and the trace integral has no unresolved tail.

## 4. Production Arb upper integration

Production implementation:

- script: `scripts/rh_log3_negative_index_mu_arb.py`;
- workflow: `.github/workflows/rh-log3-negative-index-mu.yml`;
- source head before this note: `12fc105550f6b2dc0be48e72adabe4a47a3d7ecb`;
- workflow run: `34024886403`;
- job: `101463984288`;
- Python `3.13.15`;
- `python-flint==0.9.0`;
- Arb precision: 192 bits;
- finite scan band: `[0,10000]`;
- final contributing-cell width: `2e-4`.

The algorithm recursively evaluates the complete Arb symbol ball on each frequency cell.

- If the whole ball is above `1`, the contribution is rigorously zero.
- Otherwise the cell is refined to width `2e-4`.
- On a final cell, the lower endpoint of the symbol ball gives an upper rectangle for `(1-a)_+`.

The run returned:

- interval evaluations: `1,177,332`;
- certified-zero cells: `43,725`;
- final contributing cells: `564,941`;
- half-line integral upper bound:

`113.41839961156336174569463408875783...`;

- resulting full trace upper bound:

`boxed: Tr W <=79.32463645912486220337738567865591...}`.

Thus `Tr W<80` is rigorously certified.

## 5. Pole channel sharpened from rank two to one negative direction

Let

`u(x)=e^(x/2)`, `v(x)=e^(-x/2)`

restricted to `[-log3,log3]`.

The pole contribution in the current Weil convention is

`R_pole=|u><v|+|v><u|`.

Exactly,

`R_pole`
`=1/2 |u+v><u+v| - 1/2 |u-v><u-v|`.

The vectors `u` and `v` are linearly independent on any nontrivial interval, so `u-v` is nonzero. Hence the pole term has one positive and one negative channel:

`n_-(R_pole)=1`.

Negative inertia is subadditive for Hermitian quadratic forms:

`n_-(A+B)<=n_-(A)+n_-(B)`.

Therefore

`n_-(Q_full)`
`<=n_-(Q_nonpole)+1`
`<=79+1`
`=80`.

This improves the earlier conservative `+2` pole-rank budget.

## 6. Relation to the 32-dimensional positive certificate

The earlier Arb computation certified strict positivity on the 32-dimensional branch-sine space `V_8`.

The present theorem is complementary:

- `V_8` certificate: exact positivity on one declared finite carrier;
- current certificate: finite upper bound on the total number of negative directions in the **whole** `H_log3` space.

The two facts do not imply full positivity. In particular, a positive 32-dimensional subspace need not contain the possible negative subspace.

The correct next step is a response-adapted low-dimensional carrier or a sharper weighted Birman-Schwinger estimate.

## 7. Why the constant floor stops near 80

For a general constant `mu>0`, define

`b_mu=(mu-a)_+`,
`W_mu=P_L F^(-1)b_mu F P_L`.

Then

`n_-(Q_nonpole)`
`<=#{lambda_j(W_mu)>mu}`
`<Tr(W_mu)/mu`
`=L/(pi mu) integral_R (mu-a)_+ dt`.

Floating exploration with the complete high-frequency contribution places the optimum near `mu=1`, with value about `79.2` before rigorous rectangle inflation.

Thus constant floors cannot plausibly drive this route to the 31--32 scale seen in the phase-space capacity and finite `V_8` certificate. A sharper route must retain more of the positive-symbol geometry rather than replacing it by a scalar floor.

## 8. Smallest unresolved unit

The next target is a weighted/Birman-Schwinger complement certificate.

Natural options:

1. replace the scalar floor by a positive reference multiplier/operator that tracks `a_+(t)`;
2. construct the compact weighted obstruction

`A_+^(-1/2) P_L F^(-1) a_-(t) F P_L A_+^(-1/2)`

with a rigorously controlled positive reference `A_+`;
3. build a response-adapted union-band/Slepian carrier and certify the complementary Schur block;
4. exploit higher spectral moments only if they can be certified without losing the spatial-window kernel.

The target is now not merely `finite negative index`, but to shrink the finite danger dimension enough that a finite Schur/Feshbach certificate can plausibly close the window.

## 9. Hard boundaries

- `n_-(Q_Hlog3)<=80 != Q_Hlog3>=0`.
- Finite negative index does not imply RH.
- The 32-dimensional positive certificate does not subtract 32 from the global bound.
- The constant-floor trace bound is deliberately coarse and discards the detailed positive-symbol magnitude.
- Any future weighted inverse must be certified; near-null positive-reference modes may not be silently divided out.

## Provenance

- Predecessor: `research_notes/RH_LOG3_NEGATIVE_SYMBOL_CAPACITY_CERTIFICATE_20260906.md`.
- Production source: `scripts/rh_log3_negative_index_mu_arb.py`.
- Workflow run: `34024886403`, job `101463984288`.
- Researcher-ID: `EM-DIRECT-7C1A42`.
