# PREFIX-626-R6 — Uniform inward-gradient theorem for BRC stopping-time variance

Date: 2026-11-09 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Dependencies: PREFIX-610, 613, 621–625; in particular corrected PREFIX-621 signed-first-passage counts and PREFIX-623 exact stationary bracket. Native original 96-port graph is inherited as a pinned source; it was not rerun in this research.

## Objective, carrier, and observer

PREFIX-623 located an edge-restricted variance maximum on p1=0, with p2 in I=[37/256,39/256]. Does allowing p1>0 destroy that local optimality? The frozen BRC signed-direction observation trial returns (i,+) with probability p_i/q, (i,-) with (1-p_i)/q for i=1,2, and neutral otherwise. The q values are 12 for slot 0 and 24 for slots 1/2. Each direction stops at the first informative-sign count whose exact anytime-confidence interval width is at most 1/4 (beta=1/40). T_q is the number of original actions until both directions stop, on parameter closure [0,1/2]^2. The observer retains signed direction, slot and neutral action count; no new quotient of the native state or change in future-operation scope is made.

Write s_n(p)=sum_k A_n(k)*p^k*(1-p)^(n-k), where A_n(k) is the exact PREFIX-621 survivor-word count and s_n=0 for n>=189. PREFIX-622 defined the independent-Poisson standardization mu=E[Y], H=E[Y^2]/2 and W=2H-mu^2, with

Var(T_q)=q^2 W-q mu.

## Theorem (uniform inward decrease and full-square boundary local maxima)

For all p in [37/256,39/256] and all q>=2,

partial_1 Var(T_q)(0,p) < -332*q^2 < 0.

In particular, for each actual slot q=12 and 24, there exists p_q* strictly between 37/256 and 39/256 such that (0,p_q*) is a STRICT LOCAL MAXIMUM of the variance on the complete feasible two-parameter square. This local statement leaves global maximization open.

## Proof

Define the rational positive weights

w(n,m)=binom(n+m,n)/2^(n+m+1),
z(n,m)=(n+m+1)*w(n,m)/2.

The corrected 189-level first-passage recurrence gives the finite exact identity

s'_n(0)=A_n(1)-n*A_n(0)=25 for n=25,...,33,
and zero for all other n=0,...,188.

Thus only nine survivor layers contribute to the inward derivative. Put U(p)=partial_1 mu(0,p) and J(p)=partial_1 H(0,p). Differentiation of the finite PREFIX-622 Poisson sums gives

U(p)=25 sum_{n=25}^{33} [1-sum_{m=0}^{188}w(n,m)*s_m(p)],
J(p)=25 sum_{n=25}^{33} [(n+1)-sum_{m=0}^{188}z(n,m)*s_m(p)].

For every n, sum_{m>=0}w(n,m)=1, and the omitted m>=189 mass is positive. Since 0<=s_m<=1, every U-bracket is positive. By PREFIX-624's verified finite Bernstein shape lemma, each s_m(p) is nondecreasing on [0,1/2]. Therefore U and J are nonincreasing, while mu(0,p) is strictly increasing.

Set a=37/256 and b=39/256. The accompanying exact-Fraction certificate checks, with the corrected original first-passage recurrence and integer inequalities,

mu(0,a)>87;
U(b)>4;
J(a)<182.

Hence, uniformly for all p in I,

partial_1 W(0,p) = 2 J(p)-2 mu(0,p) U(p)
<= 2 J(a)-2 mu(0,a) U(b)
< 2(182-87*4) = -332.

Since partial_1 Var(T_q)=q^2 partial_1 W-q U and U>0, the stated strict bound follows.

Separately, PREFIX-623 proved that the edge polynomial V_q(0,p) has derivative >0 at a and <0 at b, for q=12,24. Its maximum over [a,b] is therefore interior. Being a nonconstant polynomial, every such isolated interior maximizer is a strict local maximum along that edge. The uniform strict inward derivative is continuous, so sufficiently small feasible p1>0 decreases V_q uniformly near that point. This combines the tangential and normal directions into a strict local maximum of the full square. QED.

## Verification / limits / recovery

Run python PREFIX626_R6_boundary_normal_variance_certificate.py beside the Source-published PREFIX621_R6_stochastic_tail_certificate.py. It tests the 189 exact derivative-support rows, 8930 Bernstein coefficient shape inequalities, positive cross-weight brackets and all rational witness inequalities. Console returns ALL_CHECKS_PASS. Approximate display: mu(0,a)=87.31364593314114; U(b)=4.248199959435103; J(a)=181.3781658317787; the exact uniform upper witness for partial_1 W is approximately -379.0953225590449. All decisions are exact rational comparisons.

The theorem is within the frozen BRC signed-label statistical model; author proof and computation do not assert review, formal task claim, Source Result or physical-native unrestricted equivalence. The original PREFIX-565 96-port graph was not re-executed.

Next research unit: pursue bivariate Bernstein/interval subdivision to determine whether the certified edge local maxima also maximize variance globally. A strict rational interior witness above a certified boundary value would falsify the boundary-global hypothesis; an exact uniform interior exclusion would establish it. Reuse the nine-layer normal derivative and already verified survivor coefficients.
