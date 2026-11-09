# PREFIX-630-R6 — Off-strip exact variance-gradient witness and certified two-parameter patch

Date: 2026-11-09 (Asia/Shanghai).
Researcher: EM-DIRECT-F055AE / TASK_RESEARCH.
Activity: RA-52877582FE83635F579B93A5.
Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Research question

PREFIX-629 proves a uniformly decreasing inward variance gradient for 0 ≤ p1 ≤ 1/14 and p2 in [37/256,39/256] by a signed Bernstein envelope. The direct degree-187 Bernstein envelope using that earlier fixed coefficient 87 is inconclusive when extended to 1/13: its largest control coefficient becomes positive (exact sign check, displayed value approximately 142.649169). Does the true variance gradient remain negative beyond the certified strip?

This note proves an exact rational witness and a new, disjoint, positive-area gradient exclusion rectangle centered at p1=1/8. It does not assume that the old envelope represents the exact gradient.

## Fixed model and notation

Use the SOURCE-published PREFIX-621 first-passage rule for two signed BRC information directions; informative signs on direction i have probabilities p_i/q and (1-p_i)/q per native action, with other outcomes neutral. The stopping rule is the PREFIX-621 confidence-diameter rule beta=1/40, width=1/4. The first possible direction completion uses 25 informative observations and completion is forced at 189. The probability parameters can be reduced by sign symmetry to [0,1/2]^2. The original 96-port graph remains frozen, as in PREFIX-610/621.

Let T_q be the number of native actions to finish both directions and V_q=Var(T_q). Let Y be the maximum of the independent unit-rate informative Poisson-clock completion times; put mu=E[Y], H=E[Y^2]/2, W=2H-mu^2. By the established PREFIX-622 time change,

$$
V_q(p_1,p_2)=q^2W(p_1,p_2)-q\mu(p_1,p_2),\qquad q\ge2.
$$

For n=0,...,188, let A[n,k] be the exact count of surviving signed length-n words with k positive signs, computed by the published first-passage recurrence. Then

$$
s_n(p)=\sum_{k=0}^n A[n,k]p^k(1-p)^{n-k}.
$$

With w(n,m)=binom(n+m,n)/2^(n+m+1) and z(n,m)=(n+m+1)w(n,m)/2, the finite exact moment laws are

$$
\mu=\sum_ns_n(p_1)+\sum_ms_m(p_2)-\sum_{n,m}w(n,m)s_n(p_1)s_m(p_2),
$$
$$
H=\sum_n(n+1)s_n(p_1)+\sum_m(m+1)s_m(p_2)-\sum_{n,m}z(n,m)s_n(p_1)s_m(p_2).
$$

All sums over n,m run from 0 through 188.

## Theorem: a disjoint certified exclusion rectangle

Put a=37/256, h=2^(-24), p*=1/8, and define

$$
R=[p^*-h,p^*+h]\times[a,a+h]
=[2097151/16777216,2097153/16777216]\times[37/256,2424833/16777216].
$$

For every real q≥2 and every (p1,p2) in R,

$$
\boxed{\partial_{p_1}V_q(p_1,p_2)<-948q^2.}
$$

In particular, for every p2∈[a,a+h] and every p1 with p*-h<p1≤p*+h,

$$
V_q(p_1,p_2)<V_q(p^*-h,p_2)-948q^2[p_1-(p^*-h)].
$$

Thus the open-inward portion of R contains no global maximizer of V_q. Since p*-h>1/14, R is disjoint from the earlier PREFIX-629 exclusion strip.

## Proof

### Step 1. Exact off-strip rational witness

At p1=1/8 and p2=a, the accompanying stand-alone certificate reconstructs each surviving row A[n,k] using the exact PREFIX-621 dyadic test (DEN=2^18). It checks the first stop n=25 and final zero survivor n=189, then computes s_n and s'_n directly by integer-rational formulas. The formula

$$
s_n'(1/8)=\frac{8}{7\,8^n}
\sum_k A[n,k]7^{n-k}(8k-n)
$$

avoids a symbolic differentiation black box. Set

$$
\alpha_n(a)=1-\sum_mw(n,m)s_m(a),\qquad
\beta_n(a)=n+1-\sum_mz(n,m)s_m(a).
$$

Then the exact rational values

$$
\mu=\sum_ms_m(a)+\sum_n\alpha_n(a)s_n(1/8),
$$
$$
U=\partial_1\mu=\sum_n\alpha_n(a)s_n'(1/8),\qquad
J=\partial_1H=\sum_n\beta_n(a)s_n'(1/8)
$$

satisfy, by Fraction comparisons on the full integers,

$$
U>0,\qquad W_1=2(J-\mu U)<-1500.
$$

For orientation only, the rational values display as W_1≈-1516.506597637739 and U≈210.72681977375348. The exact numerators and denominators are emitted by the companion program to PREFIX630_R6_RESULTS.json; its 14,710 assertions passed in this run. Consequently, for all q≥2,

$$
\partial_1 V_q(p^*,a)=q^2W_1-qU<-1500q^2.
$$

### Step 2. Uniform pure-direction and mixed Hessian bounds

The PREFIX-627 exact Bernstein-derivative argument supplies

$$
|\partial_{11}V_q|\le L_{11}q^2,\quad L_{11}=5244748236
$$

throughout the full parameter square. We derive a new mixed bound.

Write N=189, A=sum_{n<N}n=17766, S2=sum_{n<N}n(n+1)=2250360. Every survival Bernstein coefficient lies in [0,1], whence |s'_n|≤n. The exact nonnegative w,z kernels satisfy

$$
\sum_{m\ge0}w(n,m)=1,\qquad
\sum_{m\ge0}z(n,m)=n+1.
$$

Therefore the finite moment formulas imply

$$
|\mu_i|\le A,\quad 0\le\mu\le2N=378,\quad
|\mu_{12}|\le(N-1)A=3340008,
$$
$$
|H_{12}|\le(N-1)S2=423067680.
$$

Since W=2H-mu^2,

$$
|W_{12}|
\le2|H_{12}|+2(|\mu_1\mu_2|+\mu|\mu_{12}|)
\le4002442920.
$$

For q≥2 this yields the exact new universal bound

$$
|\partial_{12}V_q|
\le q^2[4002442920+3340008/q]
\le L_{12}q^2,\quad L_{12}=4004112924.
$$

### Step 3. Extend the witness to the rectangle

For any point (p1,p2) in R, first move p1 from p* to p1 at p2=a, then move p2 from a to p2. The preceding Hessian bounds give

$$
\partial_1V_q(p_1,p_2)
<q^2[-1500+(L_{11}+L_{12})h].
$$

Exact integer reduction gives

$$
1500-(L_{11}+L_{12})2^{-24}
=\frac{1989620355}{2097152}>948.
$$

This proves the claimed gradient bound. Integrating in p1 across the rectangle proves the strict value gap and global-maximizer exclusion. QED.

## Verification and source scope

The companion Python 3 standard-library certificate reconstructs the SOURCE-published recurrence without network operations, uses Fraction for all witness comparisons, checks the new mixed Hessian arithmetic and proves the rational rectangle margin. Completed local execution: ALL_CHECKS_PASS 14710.

The result applies to the exact frozen signed-observer statistical model; neither the original 96-port BRC graph nor physical attribution was rerun. The status is author proof with exact computational checks; independent review/admission remains pending.

## Research continuation

The older fixed-envelope route fails to certify beyond 1/14 even though the exact true gradient remains negative at p1=1/8. The next discriminating problem is to establish a continuous bridge in p1 from 1/14 to 1/8 for the whole p2 bracket using narrower p2 bins and monotone mu lower envelopes, or to locate a precise rational point where the true directional gradient changes sign. Reuse the current PREFIX-621 counts and the uniform mixed Hessian lemma. All task/CLAIM/Result/Review authority remains with current Source, not with this research note.
