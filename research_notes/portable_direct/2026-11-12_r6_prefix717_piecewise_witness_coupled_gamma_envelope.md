# PREFIX-717-R6 — Exact piecewise-witness certification for the coupled Gamma envelope

Date: 2026-11-12 (Asia/Shanghai).
Scientific input pin (unchanged): awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Parent objective: PREFIX-675. Continuation: PREFIX-713, PREFIX-715, PREFIX-716.
Status: AUTHOR_PROVED / EXACT_FRACTION_TOY_CHECKED / UNREVIEWED / NOT_ADMITTED.
Model scope: the auxiliary two-parameter BRC statistical observer, D=[0,1/2]^2; no claim about an unconstructed native X6 plane.

## Problem and typed interface

For two independent conditional Gamma completion clocks T_p and T_z from the frozen 189-level survivor recursion, let Y(p,z)=max(T_p,T_z), mu(x)=E[Y(x)], M2(x)=E[Y(x)^2], W(x)=M2(x)-mu(x)^2 and f_t(x)=W(x)-t*mu(x). Here t=1/q and q>=2, so t is in [0,1/2].

Fix a closed candidate rectangle R=[a,h] and assume the coordinatewise stochastic ordering and the moment-coupling certificate previously established in PREFIX-713/716. Put m=mu(a)>=0, w=W(a), delta=mu(h)-mu(a)>=0, B=M2(h)-M2(a)>=0. The existing exact coupled influence-ratio bound supplies rational C=C_R>0 so that each x in R satisfies:

  d=mu(x)-m in [0,delta],
  0 <= M2(x)-M2(a) <= min(B,C*d).

The resulting uniform cell upper bound is

  f_t(x) <= E_R(t)
         := w-t*m + max_{0<=d<=delta} { min(B,C*d)-(2*m+t)*d-d^2 }.

Preserve the exact Gamma-clock joint moments. The maximum of stopping counts is not the Gamma maximum.

## Theorem 717.1 — the coupled optimizer has a closed rational formula

Under m>=0, delta>=0, B>=0, C>0 and t>=0, define

  k=min(delta,B/C),
  d_t= min(k,max(0,(C-2*m-t)/2)).

Then the preceding bound equals

  E_R(t)=w-t*m + C*d_t-(2*m+t)*d_t-d_t^2.

In particular, for rational input moments and rational t, E_R(t) is rational. As a function of t, E_R is convex and piecewise rational-quadratic (linear when the maximizing d_t is pinned).

Proof: for 0<=d<=k, min(B,C*d)=C*d, and the objective in braces is a strictly concave quadratic whose vertex is (C-2*m-t)/2. Over this interval, its maximizer is d_t. If k<delta, the remaining segment has constant first term B and derivative -(2*m+t)-2*d<=0. Thus no d>k improves the value at k. The closed formula follows, including B=0 and delta=0. Convexity also follows directly because E_R is a supremum of functions affine in t, one per fixed d. QED.

## Theorem 717.2 — finitely many rational witness switches suffice

Let I=[alpha,beta] be any compact rational interval in [0,infinity). Let e_1,...,e_s be actual feasible parameters with rational exact moments, giving affine lower witnesses L_i(t)=W(e_i)-t*mu(e_i). Write P(t)=max_i L_i(t). Let K contain alpha,beta and every pairwise intersection of nonidentical/nonparallel witness lines inside I. Then

  min_{t in I} [P(t)-E_R(t)]
   = min_{t in K} [P(t)-E_R(t)].

Consequently, the finite strictly-positive rational margin eta on K certifies

  max_{y in D} V_q(y)-V_q(x) >= q^2 * eta > 0

for every x in R and every finite q with t=1/q in I. When I=[0,1/2], t=0 is the continuous q-to-infinity limiting objective and the conclusion for all finite real q>=2 follows.

Proof: on each interval between consecutive members of K the same witness line is active in P. Therefore P-E_R is concave there, because the active witness is affine and E_R is convex. Every concave function is bounded below by the smaller of its values at the two endpoints. Apply this to each consecutive interval and use continuity at all switch points. Since K is contained in I, the reverse inequality is immediate. Rationality follows from the closed expression in Theorem 717.1 and exact rational crossings. Finally H(t)>=P(t) and f_t(x)<=E_R(t), and V_q=q^2*f_(1/q). QED.

For exactly two witnesses crossing once inside I, certification requires only three distinct parameter checks: alpha, the crossing, and beta. A nonpositive margin identifies only insufficiency of the chosen bounds/witnesses.

## Exact rational test demonstrating a strict gain from switching

This is a self-contained toy instance satisfying the envelope algebra; the numbers below are not measurements from the 189-level frozen BRC recursion. Set

  m=2, w=10, C=5, B=5, delta=1,
  L_A(t)=21/2-(7/2)*t,
  L_B(t)=51/5-2*t,
  I=[0,1/2].

By Theorem 717.1, d_t=(1-t)/2 and

  E_R(t)=10-2*t+(1-t)^2/4.

The witness lines cross at t*=1/5. Exact endpoint/crossover gaps:

  L_A(0)-E_R(0)     = 1/4,
  L_A(1/5)-E_R(1/5) = 1/25,
  L_B(1/5)-E_R(1/5) = 1/25,
  L_B(1/2)-E_R(1/2) = 11/80.

Thus min_{0<=t<=1/2} [max(L_A,L_B)-E_R]=1/25. Either witness alone fails uniform certification: L_B(0)-E_R(0)=-1/20, and L_A(1/2)-E_R(1/2)=-5/16.

The published Python Fraction checker compares the closed formula against the complete finite candidate evaluation at 101 exact rational t values and checks the displayed margins. Its observed local return is ALL_CHECKS_PASS PREFIX717-R6. The theorem's universal conclusion is established by the proof, not inferred from those 101 samples.

## Relationship to present frozen Gamma frontier

PREFIX-715 gave an affine multi-witness/multi-upper-line certificate. PREFIX-716 instead used one witness against the stronger *convex coupled* box upper bound and checked t=0,1/2. This result combines the exact convex coupled upper bound with *several switched witnesses*, and provides a rational finite decision rule. In the frozen model the two feasible previously certified witnesses e_A=(0,149/1000) and e_B=(0,146/1000) have an exact rational crossing t_* in (23/100,24/100) (PREFIX-713-R6), so future exact cell checks require the three points 0,t_*,1/2 rather than a continuous t scan.

The current inherited author-level certified area remains at least 138868/147456=34717/36864 for q>=2 from PREFIX-716. This work did not rerun all remaining 8,588 fine-cell equivalents or assert additional counted cells. Existing active owners, Task CLAIM, formal Result/Review and theorem admission were not modified.

## Next discriminating computation

Use the precise frozen Γ-clock 189-row kernel and exact e_A/e_B moments to evaluate Theorem 717.2 at 0,t_*,1/2 for the PREFIX-716 currently uncertified fine cells, combining their existing coupled bound C_R with the exact three-point witness switch. Reconcile the returned list against the PREFIX-716 certified set and any concurrently published stronger set, and count only new disjoint cells. For survivors, split boxes or test interval derivatives/stationary points toward the actual PREFIX-675 global optimizer.
