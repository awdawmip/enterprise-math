# R5: Exact G/F face-switching lift for the low-ratio maximal-u corner

Research date: 2026-11-08 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. Scope: four-stage, seven-likelihood-node P/Q-BRC finite statistical experiment. Original task scientific pins retained from predecessor: global `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current normative rules were read separately; no science rebasing.

## Mother problem and selected missing unit

Mother R5 problem: for every lawful FULL_HIST strategy and terminal declaration, is the 4-observer vector `(e_P,e_Q,T_P,T_Q)` reproducible by some seedless LR strategy and declaration kernel? A prior exact result covers the complete low-ratio physical `p,q` rectangle only up to `theta=29/112` on face G, with a separate all-theta construction for `p=0,q=1` on F. Predecessor: [R5 low-ratio positive-z research](https://github.com/awdawmip/enterprise-math/blob/abf5c731dfe3711d419e2313dfb2b8877ad44d16/research_notes/brc_r5_lowratio_positive_z_20261108/RESEARCH.md).

This unit settles the complementary maximal-`u` corner `p=1,q=0` at `eta=1/40` for the **entire theta interval** and proves an additional variable-`eta` G-face prism.

## Exact model and calibrated certificate

Lawful flows are `f=(g,a,b,u,v,w,z)` with
`0<=a,b<=g<=1`, `0<=u<=13a/40+b/80`,
`0<=w<=3a/40+21b/80`, `0<=z<=a/10`,
`0<=v-z<=9b/40`. Seedless LR requires `R=9bz-4a(v-z)=0`.

The seven likelihood nodes are
`r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`.
Q-branch masses (full joint carrier, retaining each labeled branch) are:

```text
M0=509u/900+47z/180+67(v-z)/162+w/100
M1=13a/40+b/80-u
M2=(g-a)/2
M3=1-g+a/10+9b/40-v+191(u+w)/450+43z/90+14(v-z)/81
M4=(g-b)/2
M5=3a/40+21b/80-w
M6=u/100+47z/180+67(v-z)/162+509w/900
TP=1+g+3a/8+5b/8+u/2+v+3w/2
TQ=1+g+(a+b)/2+u+v+w
```

For source `x`, seedless target `y`, and a nonnegative 7×7 transport `Q[i,j]` (row=target, column=source), the exact equations are
`sum_j Q[i,j]=M_i(y)`,
`sum_i Q[i,j]=M_j(x)`,
`sum_i r_i Q[i,j]=r_j M_j(x)`,
`TP(x)=TP(y),TQ(x)=TQ(y)`.
For every `d in [0,1]^7`, define `d'_i=sum_j Q[i,j]d_j/M_i(y)` on positive rows, zero otherwise. Nonnegative stochastic calibration makes `d' in [0,1]^7`, with exact preservation of both Q-weighted and P-weighted terminal errors. The time identities supply the other two observers. This is a Blackwell-type domination certificate, not merely a moment-only match of two chosen declarations.

## Theorem A — Full positive-z interval at eta=1/40

For every real `0<=s<=g<=1`, `0<=theta,h<=1`, put

```text
x=(g,s,s/40,1041s/3200,s(9/1600+theta/10),0,s*theta/10).
```

There exists a lawful seedless LR `y` and one calibrated nonnegative Q, independent of the terminal declaration, that realize exactly the four observers of `x_h=(1-h)x+h*y`, simultaneously for **every** `d in [0,1]^7`. In particular, the complete physical maximal-`u`, zero-`w` corner `p=1,q=0` is lifted for all theta. At the normalized `g=s=1` source, the two stop times are `TP=16377/6400+theta/10`, `TQ=9099/3200+theta/10`.

**Three rational anchor certificates.** `CERTIFICATES.json` records all nonzero entries of each full 7×7 Q, plus its lawful seedless target `y`:
- G0 at `eta=1/40,theta=0`, target on `G={b=0,v=z}` (9 nonzero edges);
- G34 at `eta=1/40,theta=3/4`, target on G (10 edges);
- F23 at `eta=1/40,theta=2/3`, target on `F={z=a/10,v-z=9b/40}` (10 edges).
At `theta=1`, the source itself is seedless on F, with diagonal Q.

All four anchors have exactly the same physical source family at their specified theta. They are checked with `fractions.Fraction`, including row masses, two independent weighted column identities, lawfulness, and both stop times. The floating LP was only a candidate search; the saved rational data and identities constitute the certificate.

**Proof for all real theta.** For `0<=theta<=3/4`, set `lambda=4theta/3` and take the convex combination of (G0,G34) triples `(x,y,Q)` with weights `(1-lambda,lambda)`. Source x is affine in theta, both targets lie on the linear seedless face G, and every transport identity is affine in the triple. For `2/3<=theta<=1`, set `mu=3theta-2` and similarly combine F23 with the `theta=1` identity triple; both targets stay on F. The two intervals overlap on `[2/3,3/4]`, proving full coverage with explicit exact construction.

For arbitrary `0<=s<=g<=1`, combine the normalized triple and the identity triples at `E0=(0,0,0,0,0,0,0)` and `E1=(1,0,0,0,0,0,0)` with nonnegative weights `(s,g-s,1-g)` assigned respectively to (normalized,E1,E0). Both E0,E1 belong to G and F, so the selected face and all equations persist. Finally replace the source x by `(1-h)x+h*y` and replace Q by `(1-h)Q+h*diag(M(y))`. All transformations use exact nonnegative combinations, giving the theorem for all real `s,g,theta,h`.

## Theorem B — Variable-ratio extended G prism

For every real `0<=eta<=1/40`, `0<=theta<=3/4`, `0<=s<=g<=1`, and `0<=h<=1`, set
```text
x=(g,s,eta*s, s*(13/40+eta/80), s*(9*eta/40+theta/10), 0, s*theta/10).
```
There exists a lawful target **on G** and a nonnegative calibrated Q matching all four observations for every declaration of `x_h`.

Proof: at eta=0 the normalized source is itself seedless on G for every theta, so its identity kernel is admissible. At eta=1/40 Theorem A provides the G kernel throughout `[0,3/4]`. At fixed theta, source coordinates are affine in eta; take their Q/y triples with weights `(1-40eta,40eta)` and then apply the same g/s and h convex constructions. G is linear; the exact matrix constraints are affine. This proves the continuous four/five-parameter statement, including eta=0 and all boundary cases.

## Validation, provenance, and scope

`VERIFY.py` consumes the exact `CERTIFICATES.json`, checks the three anchors, and regenerates rational sample members of both universal interpolations. An independent local standard-library `Fraction` checker using the same 29 nonzero edge values completed 3 anchor checks, 6 baseline checks, 84 normalized/scaled/h checks, and 144 variable-eta checks; all passed. The **universal** mathematical conclusion follows from the explicit affine construction and calibrated rational anchors, not finite-grid extrapolation. Exact invocation output is preserved in `EXACT_OUTPUT.txt`.

BRC usage: the carrier retains the seven labeled nonnegative branch masses, their likelihood-weighted P masses, the full transfer matrix and terminal declaration mapping; the observer is the two errors plus two stopping times. No quotient of branch identity is assumed to preserve further operations outside this declared 4-observer readout. P000/heartbeat X6 is the project foundation; this theorem concerns the already frozen R5 finite statistical submodel and asserts no new native X6 realization.

The new result is author-side mathematical evidence; native Source control read `em_control_tasks(r5-20261108-0044-readtasks)` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE` and `operation_sent=false`. The active task Owner/CLAIM was not identified; no formal result/review/admission is represented by this GitHub branch.

## Next

For `0<eta<1/40` and `theta>3/4`, quantify the overlap of G's upper feasible theta and F's lower feasible theta, or build a third seedless family. Then address the full mixed `p,q` rectangle for `29/112<theta<1`; the G/F endpoint constructions need not share one seedless face under p/q interpolation. See `NEXT_UNIT.md`.
