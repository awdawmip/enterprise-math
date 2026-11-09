# PREFIX-624-R6 — Strict ordering of the two BRC edge-variance maximizers

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Previous exact model/proof inputs: PREFIX-610, 613, 621, 622, 623. This paper continues PREFIX-623, preserving its BRC signed-label observer, native action-count semantics and fixed stopping rule. No new physical dynamics or classic trigonometric propagation is computed.

## Question and model

On the asymmetric compact-closure face p1=0, let p=p2 in [0,1/2]. At each native BRC observation the two signed directions each have mass 1/q; q=12 for the slot-0 binary label and q=24 for slot-1 or slot-2. Within direction 2 the sign probabilities are p and 1-p. Each direction stops upon reaching exact anytime confidence width at most 1/4, with beta=1/40. Let T_q(0,p) denote the total native-action count needed for both directions, and V_q(p)=Var(T_q(0,p)).

The first direction requires exactly 25 informative observations. The second direction has surviving signed-word counts A_n(k) for n informative observations with k positive signs; these are the corrected exact first-passage recurrence of PREFIX-621, with no survivors after n=189. Define

  s_n(p) = sum_{k=0}^n A_n(k) p^k(1-p)^(n-k),   0<=n<=188.

The previous exact Poissonized moment representation gives rational constants

  alpha_n = 1 - sum_{m=0}^{24} binom(m+n,m)/2^(m+n+1) > 0,
  mu(p) = 25 + sum_{n=0}^{188} alpha_n s_n(p),

and a second-moment auxiliary H(p) with

  V_q(p) = q^2(2H(p)-mu(p)^2)-q mu(p).
  V_24(p) = 4 V_12(p) + 24 mu(p).                 (1)

These identities and the strict endpoint comparisons V_q(1/8)>V_q(0), V_q(1/2) for q=12,24 were verified in PREFIX-623; the companion PREFIX-624 certificate independently reruns the exact survivor recurrence and proves its coefficient shape.

## New theorem

For any a in Argmax_{0<=p<=1/2} V_12(p) and any b in Argmax_{0<=p<=1/2} V_24(p), one has the strict inequality

                         a < b.                  (2)

In particular, the two argmax sets are disjoint and ordered even if either variance polynomial has more than one global maximizer. Neither uniqueness of a stationary root nor exhaustive isolation of all roots of the degree-at-most-376 polynomials is required.

## Proof

1. Conditional central unimodality. Let b_{n,k}=A_n(k)/binom(n,k). The exact signed-observer recurrence yields b_{n,k}=b_{n,n-k} and

  b_{n,0} <= b_{n,1} <= ... <= b_{n,floor(n/2)}

for every n=0,...,189. These are finitely many exact integer cross-product inequalities. The standalone certificate checks all 8,930 interior monotonicity comparisons, 9,120 symmetry comparisons, and the corrected 357,260 dyadic confidence-threshold comparisons. This is a finite rigorous certificate for the stated stopping rule, not a numerical fit.

2. Monotone survivor probabilities. By symmetry and central unimodality, b_{n,k} is a nonnegative linear combination of a constant and indicators of centered bands {a<=k<=n-a}. If K~Bin(n,p), then for a>=1,

  d/dp Pr(a<=K<=n-a)
  = n*binom(n-1,a-1)*p^(a-1)*(1-p)^(a-1)
      * [(1-p)^(n-2a+1) - p^(n-2a+1)] >= 0

for 0<p<=1/2. Consequently s_n'(p)>=0 for 0<p<1/2.

3. Strict increase of mu. The recurrence gives A_25(k)=binom(25,k) for 1<=k<=24 and A_25(0)=A_25(25)=0. Hence

  s_25(p)=1-p^25-(1-p)^25,
  s'_25(p)=25[(1-p)^24-p^24] > 0   for 0<p<1/2.

All alpha_n are strictly positive (the omitted positive terms of a negative-binomial probability mass), so mu'(p)>0 throughout (0,1/2). In particular, mu is strictly increasing on [0,1/2].

4. Ordering of maximizers. PREFIX-623 established V_q(1/8)>max(V_q(0),V_q(1/2)), so any global maximizer of either V_q over [0,1/2] is interior. Let a maximize V_12 and b maximize V_24. If b<a, then by (1), V_12(b)<=V_12(a) and mu(b)<mu(a) imply V_24(b)<V_24(a), contradiction. If b=a, the interior first-order condition yields V'_12(a)=0; (1) gives V'_24(a)=24 mu'(a)>0, contradicting b's maximality. Thus a<b. QED.

## Verification and status

The certificate uses only native BRC observer-derived signed-word count recurrences, integer products and exact rational coefficient comparisons. All checks passed: 357,260 dyadic comparisons, 8,930 shape comparisons, 9,120 symmetries, 189 strictly positive alpha coefficients. The original 96-port BRC graph from PREFIX-565 is reused through the prior verified model; this run does not claim to rerun that graph. Boundaries, source support and future operations remain those of the signed-direction/neutral observer and confidence-width stopping time.

This argument also yields a general comparative-static lemma: if f and h are differentiable on a compact interval, h is strictly increasing, and both f and c f+d h (c,d>0) have interior global maxima, then every maximizer of c f+d h lies strictly to the right of every maximizer of f. Its present BRC specialization has c=4, d=24.

Next discriminating question: use exact multivariate Bernstein subdivision to locate the global maximum of Var(T_q(p1,p2)) over the full square, including whether it lies on p1=0/p2=0 and whether the two-q strict ordering admits a bivariate analogue. Track the original native-service session and activity receipts separately; pending source control is not a mathematical impediment.
