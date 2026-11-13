# R5 — A genuine two-law finite stopped tree with two serial likelihood-ratio collisions

Date: 2026-11-02 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**.

## Purpose, source pins and scope

This research answers the precise open construction step in the preceding R5 result `awdawmip/enterprise-math@2faf0baa3521aa53db13761ce7503b3512c3aed0:research_notes/brc_r5_two_serial_key_rankfour_compensation_20261102_t2253/{RESEARCH.md,NEXT_TASK.md}`. Its auxiliary source-flow observers were `(x,d,r1,r2)`; it asked whether a *legitimate* two-law finite stopped-path model with time/likelihood-ratio collisions at **both** downstream decision gates could reproduce them by an invertible affine map. **Here the answer is yes**, with strictly positive rational natural kernels. The preceding equality and perturbation separation therefore transfer to genuine `O=(e_P,e_Q,T_P,T_Q)` stopping observables.

Frozen scientific pins, unchanged: account global `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current normative main read separately: global `41469f7a38c888c0cba5a7324b90d92ac2664700`, Enterprise Math `80f47c5080f82e11f23708516aa337f3504ff261`. P000, ACTIVE worldview and project method remain unchanged. This is a classical two-probability-measure stopped-tree construction; no native X6 embedding or independent mathematical admission is claimed.

The mother question remains: find a strictly positive finite two-law tree in which full-history policies and seedless time/likelihood-ratio policies have **equal four-observer convex hulls** but **different actual behavioral images**. This construction does **not** solve that mother question: at its proportional base point both actual images agree, while the source perturbation gives unequal convex hulls.

## Exact two-law tree

Let `P,Q` be probability measures on the same finite path space and let the observable terminal decision be the hypothesis label `P` or `Q`. Define `e_P=P(terminal label P)`, `e_Q=Q(terminal label Q)`, and let `T_P,T_Q` be the expected terminal times under the respective measures. A policy uses the same behavioral probabilities under either measure, conditional on its allowed observations; the measures differ only in the explicitly specified natural kernels.

At time 0 there is **one** upstream behavioral decision `X`: choose a flag `f=1` with probability `x∈[0,1]` and `f=0` with probability `1−x`. **After this decision**, Nature samples one of `C,I,BJ,IJ,D` with probabilities `1/4,1/4,1/8,1/8,1/4` respectively, identically under P and Q. The sample is visible to the FULL policy but not to the LR policy. These group probabilities sum to 1.

* Group `D` always terminates at time 3 after a terminal answer coin. If `f=1`, group `I` or `IJ` terminates at time 3 by the `X` exit. Otherwise group `I` reaches K1.
* At time 2 groups `BJ` (either flag) and `IJ` (only if `f=0`) have a behavioral `J` decision. Continuing probabilities can differ by full history; stopping goes to a group-specific terminal answer coin, with termination at time 3. All paths that continue J reach K1 at time 3. Shorter routes are padded by deterministic neutral transitions so that **all** J decisions occur at time 2 and **all** K1 decisions at time 3; no early exit has a different terminal time.
* At K1 (time 3), the policy chooses to continue with probability `z` (FULL may depend on history). Conditional on continuing, Nature advances to time 4/K2 with probabilities under P
  `alpha=(1/2,2/3,1/2,3/4)` for sources `(C,I,BJ,IJ)` and **exactly half of each** under Q. K1 stopping or failure terminates at time 3 with label P.
* At K2 (time 4), reached only after K1 success, the policy chooses to continue with probability `t`. Conditional on continuing, Nature advances to time 5 with probability `theta_s^P=c+epsilon/beta_B` for `s=BJ` and `theta_s^P=c` otherwise; under Q the conditional probability is exactly half the corresponding P probability. Set `c=2/3`, `beta_B=1/2`, `beta_I=3/4`, and `0≤epsilon<1/6`. K2 stopping or failure terminates at time 4, success at time 5; all these outcomes have terminal label P.
* The terminal answer coin outputs label Q with probabilities (under P, under Q): `D=(1/2,1/2)`; `X=(1/2,1/4)`; `J_B=(beta_B/4,beta_B/2)`; `J_I=(beta_I/4,beta_I/2)`. All these Bernoulli parameters lie strictly between 0 and 1. Terminal label P is their complementary outcome. K exits have the deterministic terminal label P. Every nontrivial natural branch probability is strictly between 0 and 1 for `0≤epsilon<1/6` (including both K gates), while zero/one **policy** decisions remain permitted.

At time 2 each eligible J history has likelihood ratio 1, so a seedless time/likelihood-ratio policy must share **one** J continuation probability `y`. Every eligible K1 history has `(time, dP/dQ)=(3,1)` and must share one K1 probability `z`. Every K2 history reached with positive mass has `(time,dP/dQ)=(4,2)` and must share one K2 probability `t`: P/Q K1-success ratios are identically 2 regardless of source, previous behavioral probabilities cancel, and K2 happens only after that success. The fully observed policy can distinguish source histories and choose independently. The unique X decision has no collision issue. The terminal answer coins are Nature, not discretionary decision kernels. The two K gates are genuinely serial, not simultaneous or independently sampled votes. Source labels remain part of the path space and are only aggregated after proving observer preservation.

## Lemma 1 — exact branch-flow coordinates even for adaptive FULL policies

For an arbitrary FULL real strategy, let `b` be 8 times the total probability of BJ paths reaching K1, and `i` be 8 times that for IJ. They satisfy `0≤b≤1`, `0≤i≤1−x`. The four source masses reaching K1 are precisely

```
w=(1/4, (1−x)/4, b/8, i/8).
d=(beta_B*b+beta_I*i)/8.
```

For fully adaptive K1/K2 controls, let `r1` be total P-mass advancing from time 3 to time 4, and `r2` the total P-mass advancing from time 4 to time 5. Grouping the contributions within each source gives, for effective `z_s,t_s∈[0,1]`,

```
r1 = sum_s w_s*alpha_s*z_s,
r2 = sum_s w_s*(c*alpha_s+epsilon*1_{s=BJ})*z_s*t_s.
```

This is an exact probability-flow identity, not an assumption that full-history controls coincide across root flags. Conditional weighting within each source defines the effective controls whenever its mass is positive; if zero, any value is harmless. Because the K1 P/Q success ratio is 2, and the K2 P/Q conditional success ratio is 2, corresponding Q advancing masses are `r1/2` and `r2/4`.

Direct summation of terminal Q-answer masses yields

```
P(label Q) = 21/128 + (21/128)*x − d/4,
Q(label Q) = 13/64  + (3/64)*x  − d/2.
```

For example, the X exits have total source mass `3x/8`, the J_B exit mass `(1−b)/8`, and the J_I exit mass `(1−x−i)/8`. The answer coins specified above give the displayed formulas. All terminal paths have time at least 3 and only K1/K2 successes add one unit each. Therefore for **every real FULL policy**, without treating P and Q observations as independent rewards,

```
O=(e_P,e_Q,T_P,T_Q)
 = (107/128 − 21*x/128 + d/4,
    13/64   + 3*x/64   − d/2,
    3+r1+r2,
    3+r1/2+r2/4).
```

Write this as `O=O_0+A*(x,d,r1,r2)^T`, with coefficient matrix

```
A = [−21/128    1/4      0    0 ]
    [  3/64    −1/2      0    0 ]
    [     0       0      1    1 ]
    [     0       0    1/2  1/4].
```

Its exact determinant is `−9/512≠0`. The inverse is explicit: if `vP=e_P−107/128`, `vQ=e_Q−13/64`, `u=T_P−3`, `v=T_Q−3`, then

```
x = (−vP/2 − vQ/4)/(9/128),
d = (−3*vP/64 − 21*vQ/128)/(9/128),
r1=4*v−u,     r2=2*u−4*v.
```

Thus the previous auxiliary model is an **invertible affine image of genuine two-law expected-time/terminal-answer observers** for this stopped tree. The same map holds for all permitted epsilon, and preserves exact convex-hull equality, inequality, actual behavioral image membership and full affine rank.

## Theorem 1 — equality of actual four-observer images, with full rank

For epsilon=0, write `H(x)=alpha_C/4+alpha_I*(1−x)/4` and `Amax=H(x)+d>0`. For every FULL strategy, its flows satisfy `0≤r1≤Amax` and `0≤r2≤c*r1`. A seedless LR policy uses `y,z,t∈[0,1]`; its J masses are `b=y`, `i=(1−x)y`. Choose

```
y=8*d/(beta_B+beta_I*(1−x)),
z=r1/Amax,
t=r2/(c*r1) if r1>0, else 0.
```

All parameters lie in `[0,1]` and give exactly the same `(x,d,r1,r2)`, hence exactly the same physical four-observer O. Every LR strategy is a FULL strategy. Therefore **as actual sets generated by all real behavioral policies**,

```
O(FULL)=O(LR)  at epsilon=0.
```

The previous auxiliary LR Jacobian at `(x,y,z,t)=(1/2,1/2,1/2,1/2)` is `71407/28311552>0`. Multiplying by the physical affine determinant gives the exact physical Jacobian `−71407/1610612736≠0`. Consequently both actual images contain nonempty open subsets of the four-observer space. This establishes a **legal time/LR-colliding, strictly positive two-law tree with full four-dimensional rank and equal actual images**.

## Theorem 2 — precise perturbed signed separation in physical coordinates

For every real `0≤epsilon<1/6`, the prior auxiliary linear functional gives the exact support gap

```
n_aux(epsilon)=(c*alpha_I/4−epsilon*beta_I/[8(beta_B+beta_I)],
                −(c+epsilon/(beta_B+beta_I)), 0, 1),
h_FULL(n_aux)−h_LR(n_aux)=epsilon*beta_I/[8(beta_B+beta_I)].
```

For completeness: `r2≤c*(H(x)+d)+epsilon*b/8`. Substitute the normal and simplify. FULL's upper remainder is `[epsilon*beta_I/(8B)]*(b−i−x)` with `B=beta_B+beta_I`, maximized at `x=0,b=1,i=0`, where all K continuations are 1. LR has `b=y`, `i=(1−x)y`, so `b−i−x=−x(1−y)≤0`; the LR upper bound is reached at `x=0,z=t=1`. These bounds cover the **entire continuous** behavioral domains, including adaptive FULL policies.

For the strictly positive rational perturbation `epsilon=1/8`, the physical signed normal, obtained by `A^T*m=n_aux`, is

```
m=(−86/405, 578/405, 2, −4).
```

One FULL strategy takes `x=0`, J_B continuation 1, J_I continuation 0, and both K continuations 1. Its exact physical observer is

```
W=(109/128, 11/64, 2077/576, 7465/2304).
```

The **all-real** support values and distance certificate are

```
h_FULL(m)=−12277/2160,
h_LR(m)  =−49189/8640,
h_FULL(m)−h_LR(m)=3/320>0,
||m||_1 = 3094/405,
dist_infinity(W,conv O(LR)) >= (3/320)/(3094/405) = 243/198016.
```

The explicit natural kernels at K1 under P are `(1/2,2/3,1/2,3/4)` and under Q half those values. At K2 the P kernel is `2/3` except BJ `11/12`, and the Q kernel is `1/3` except BJ `11/24`. All are strictly between zero and one. The affine transfer does not enlarge or shrink the support gap when the normal is transformed contragrediently.

## Exact execution, coverage and remaining work

The adjacent standalone `VERIFY.py` was executed under Python standard-library `fractions.Fraction`; its actual output is `EXACT_OUTPUT.txt` and the PASS marker is `PASS_EXACT_R5_SERIAL_TWO_LAW_COLLISION_EMBEDDING`. It checks the fully specified terminal-path probability flow under both measures (including mass=1 normalization), 200 rational **adaptive FULL** noncorner policies allowing BJ behavior to depend on the root flag, all 2048 reduced FULL and 16 seedless LR deterministic points at two epsilons, the exact equal-case LR lift at all reduced FULL corners, both support values, the physical signed normal, distance and rank determinants. The 2048 count concerns the *reduced source-constant* FULL corner subfamily; the analytic proofs above cover the larger truly history-adaptive FULL class. The exhaustive finite checks are exact regressions, not the proof of all-real statements; the algebra establishes those.

The native owner inventory read returned `CONTROL_QUOTA`, the directed native gateway reports `authority_granted=false`, and the authenticated GitHub user `awdawmip` has repository admin/push access. This work is author-side portable scientific material; it does not claim a canonical Source CLAIM, Result, Review, mathematical adoption, Lean formalization or native X6 transfer. No private credentials appear here.

**Next discriminating unit:** Because the full-rank proportional base model has actual-image equality, and the one-BJ K2 perturbation produces a signed separation, vary genuinely new source-conditioned terminal-answer kernels *after K1/K2* or alter downstream time routing while preserving both predecision collision keys. Compute the resulting physical four-observer vectors and check all FULL deterministic vertices for exact LR convex combinations or exact rational separating normals. Only upon obtaining full signed hull equality should one attempt a certified FULL real observation outside the LR real image. See `NEXT_TASK.md`.
