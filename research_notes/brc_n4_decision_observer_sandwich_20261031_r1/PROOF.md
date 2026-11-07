# BRC N=4: decision-only exact coding staircase and universal observer sandwich

2026-10-31. Portable author-side analytic proof; independently unreviewed, not admitted to Working Truth/Foundation, and not a native CLAIM/Result. The finite statistical carrier is not a derived physical X6 dynamics law.

## Frozen model and exact target

The P/Q laws each have 16 strictly positive leaves (S,J,K), where S is AU, AV, BU or BV, J and K are binary, and K is independent fair. Per individual K leaf the P/Q numerators over 240 are:

| S | Q J=0,1 | P J=0,1 |
| --- | --- | --- |
| AU | 10,10 | 9,11 |
| AV | 20,20 | 5,5 |
| BU | 15,15 | 3,27 |
| BV | 15,15 | 30,30 |

Eight preparations (S,P/Q) remain in the scoring maximum, though AV_P=AV_Q and BV_P=BV_Q as future conditional laws. On six distinct prepared rows AU_Q, AU_P, AV, BU_Q, BU_P, BV and columns AU0, AU1, AV, BU0, BU1, BV, the exact likelihood-ratio-class channel is

~~~text
M = (1/20) [
 [10,10, 0, 0, 0, 0],
 [ 9,11, 0, 0, 0, 0],
 [ 0, 0,20, 0, 0, 0],
 [ 0, 0, 0,10,10, 0],
 [ 0, 0, 0, 2,18, 0],
 [ 0, 0, 0, 0, 0,20]]
~~~

The six P/Q likelihood ratios are 9/10, 11/10, 1/4, 1/5, 9/5, 2, all distinct. The future H ranges over all lawful S23 or S2 causal stopping/terminal-decision policies, including stochastic and adaptive policies. Full public record O=(T,Decision,Z_BU) uses the established BU-only sensor (with presence/absence), with sensor error real epsilon in [0,1/2], respecting the existing stage-two early-stop semantics.

A single row-stochastic encoder E maps each prepared input to at most k symbols before H is chosen. The decoder D_H may depend on H and randomize, but never reads the true prepared input, J or K. For any observer Y define

R_k(Y,F;epsilon) = inf_E sup_(H in F) inf_(D_H) max_x TV(L(Y_H|x), (E D_H)(Y_H|x)).

Y may be an H-dependent *source-independent* stochastic postprocessing of O, with Decision recoverable deterministically from Y. This covers Decision alone, (Decision,Z_BU), (T,Decision) and O. Reconstructed paths need not be the originally realized paths.

## Theorem

For every such observer Y, both F=S23 and F=S2, and every real epsilon in [0,1/2], the unrestricted stochastic minimax error is exactly

| k | R_k(Y,F;epsilon) |
| --- | --- |
| 2 | 1/2 |
| 3 | 1/2 |
| 4 | 1/5 |
| 5 | 1/40 |
| 6 or more | 0 |

For Decision-only Y, also R_1=1/2. For general eligible Y, 1/2 <= R_1(Y,F;epsilon) <= 3/4; both endpoints occur, respectively for Decision-only and full O. In particular **R_4(no T, with BU sensor and presence)=1/5** and **R_4(Decision-only)=1/5**, closing the immediate open four-code unit. The same invariance for R_5 was not previously explicit.

## Observer sandwich

For source-independent postprocessings O -> Y -> Decision, with the last map deterministic, total-variation data processing gives

R_k(Decision,F) <= R_k(Y,F) <= R_k(O,F).

It applies separately to each actual H, even though decoders can vary across H. It therefore suffices to exhibit full-record upper bounds and lower bounds that use only the Decision marginal.

## A lawful 64-policy lower-bound family

For any Boolean vector b in {0,1}^6, define H_b: continue at stage two everywhere, stop at stage three, set terminal Decision=P on class j exactly when b_j=1. These 64 policies are lawful S23 and S2; they respect equal-likelihood-ratio actions, tie AU/BU stage-two continuation, and never inspect future K. The Decision=P probability vector over the six preparations is exactly M b.

Fix E with at most k columns, and choose nonzero w with w^T E=0. Since E is row-stochastic, sum_i w_i=0. For each b, the decision marginal of D_(H_b) is a column d_b in [0,1]^k. If its maximum rowwise TV error is at most delta then |w^T M b| <= delta ||w||_1. Set r=w^T M; it sums to zero. Among all 64 b, max |r b|=||r||_1/2. Thus

(1)  delta >= ||w^T M||_1 / (2||w||_1).

This lower bound applies to every Decision-retaining Y, without a common decoder across different policies. Any approximation of decoder infima is handled by an arbitrary positive eta then eta->0.

## k <= 3

Use the four prepared rows AU_Q, AV_Q, BU_Q, BV_Q and the 16 H_b that independently assign a constant Boolean Decision to each of their four sources. For k<4 any 4 by k encoder has a nonzero left-null w, which sums to zero. Let b_i=1 precisely where w_i>0. Then w^T b=||w||_1/2 while w^T E d_b=0; hence delta>=1/2. A constant fair-Bernoulli decoder proves Decision-only error <=1/2, including k=1.

For every full O, two codes also suffice at error <=1/2: encode AU/AV as L, BU/BV as R and sample the six-class reference

F_L=(19/80,21/80,1/4,0,0,0),
F_R=(0,0,0,1/10,2/5,1/2).

Every source prepared row has total variation exactly 1/2 from its reference (on the source provenance fiber the pointwise dominated overlap is exactly 1/2). Independently sampling fair K, the sensor and then running any lawful H are the same stochastic kernel for the actual and reference futures. Therefore full-record TV <=1/2 for every H and epsilon. The sandwich closes k=2 and k=3.

## k=4, arbitrary stochastic E

A six-by-four E admits a nonzero w=(a,a,b,c,d,e) with w^T E=0, because there are four column equations plus the single condition w_1=w_2 on six unknowns. Row stochasticity implies 2a+b+c+d+e=0. Set s=c+d and B=2|a|+|b|+|e|. Then B>=|s|, and exact multiplication by M gives

||w^T M||_1
 = B+|c/2+d/10|+|c/2+9d/10|
 = B+max(|s|,4|d|/5)
 >= B+4|d|/5.

Also ||w||_1=B+|s-d|+|d| <=2B+2|d|. Thus ||w^T M||_1 >= (2/5)||w||_1. The w=(0,0,0,1,-1,0) witness gives equality. Formula (1) yields delta>=1/5 for **all** row-stochastic encoders, cross-source sharing included.

For the full-record upper bound, encode only source class S with four deterministic codes AU,AV,BU,BV. Decode J=1 using respectively 21/40, 1/2, 7/10, 1/2; then sample fair K, sensor and H. True P/Q J=1 parameters are AU 1/2 and 11/20; BU 1/2 and 9/10; AV/BV are 1/2. The largest reference TV is max(1/40,1/5)=1/5, preserved as an upper bound by any future stochastic map. So R4(O)=1/5, and by the sandwich every eligible observer has R4=1/5.

## k=5, arbitrary stochastic E

For any six-by-five E choose nonzero w in its left nullspace; sum w=0. Write r=w^T M. The exact inverse row action w=A r has columns

v1=(11,-10,0,0,0,0),
v2=(-9,10,0,0,0,0),
v3=(0,0,1,0,0,0),
v4=(0,0,0,9/4,-5/4,0),
v5=(0,0,0,-1/4,5/4,0),
v6=(0,0,0,0,0,1).

All 15 column-pair L1 distances are <=40, and ||v1-v2||_1=40. Because sum r=0, write r=t(p-q) where t=||r||_1/2 and p,q are probability vectors. Then Ap and Aq lie in the convex hull of the inverse columns, so

||w||_1=||A r||_1 <=40t =20||r||_1.

Formula (1) gives delta>=1/40. The inverse bound is sharp at w=(1,-1,0,0,0,0).

Achieve the full-record upper bound with five codes AU*,AV,BU_Q,BU_P,BV. Only AU_Q/AU_P are merged, with J=1 midpoint 21/40; all other conditional preparations are reproduced exactly. True-future TV <=1/40, hence all public outputs under all lawful H have error <=1/40. The sandwich closes k=5.

## k>=6; scope and validation

Exactly encode the six distinct prepared conditional laws, sharing only identical AV and BV rows, then reconstruct the entire future distribution. This gives full-record and every eligible observer error zero for k>=6.

The standard-library Fraction script VERIFY.py was actually executed. It rebuilt P/Q (16 positive leaves per law, each normalized to 240), the six conditional rows and distinct LR classes, checked 2400 exact integer points on the k4 dual subspace and sharp witness, the full 15-pair inverse diameter and sharp k5 witness, six-row reference TV for k4/k5, and 64 lawful terminal assignments times six input rows (384 exact Decision comparisons). The 64 binary policies are a **witness subfamily**; every real E, arbitrary lawful adaptive H, epsilon continuum and every eligible Y are handled by the analytic inequalities and TV data processing, not by finite-grid extrapolation.

The result is a scoped worst-policy *distributional coding radius invariance*, not a statement that T or Z is informationally redundant for every individual policy, all future operations, or P000 native dynamics. Source provenance, likelihood classes, branch multiplicity and frozen future-policy language remain explicit. P000's native six-dimensional Cell torsor and independently typed time have no proved dynamical observer-preserving bridge to this finite experiment. All scientific claims remain author-side pending independent review.