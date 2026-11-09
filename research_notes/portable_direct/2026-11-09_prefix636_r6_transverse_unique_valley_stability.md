# PREFIX-636-R6 — Certified two-parameter stability of unique BRC variance valleys

Date: 2026-11-09 (Asia/Shanghai). Scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged). Status: AUTHOR_DERIVED_FROM_PREFIX635 / EXACT_RATIONAL_BOUND_CHECKED / UNREVIEWED / NOT_ADMITTED. Independent direct TASK_RESEARCH note; formal shared CLAIM/Result/Review are not asserted.

## Exact theorem

In the finite signed two-information-direction BRC first-passage statistical observer of PREFIX-621/622, let Y be the maximum of two unit-rate informative Poisson stopping times; put mu=E[Y], W=Var(Y), F_q(p1,p2)=W(p1,p2)-mu(p1,p2)/q. Then Var(T_q)=q^2 F_q; actual thinning parameters are q=12 and q=24. The 96-port original BRC graph remains the frozen scientific dependency, not a computation performed in this note.

Set a=4/25, b=161/1000, p*=19/128, delta=1/8589934592=2^(-33) and R=[a,b] x [p*-delta,p*+delta]. For **every real 12<=q<=24 and (p1,p2) in R**, the following hold:

1. 299 < partial_1 mu < 311, and 22000 < partial_11 F_q < 51000.
2. partial_1 F_q(a,p2) < 0 < partial_1 F_q(b,p2). Hence the function p1 -> F_q(p1,p2) has a **unique** critical point c(q,p2) in (a,b), which is its unique global minimizer on [a,b]. Locally in (q,p2), c is real analytic, also at the stated parameter endpoints by extension.
3. partial_q c = -partial_1 mu/(q^2 partial_11 F_q) < 0, and uniformly in the new nonzero-width p2 interval,
   
   **299/1224000 < c(12,p2)-c(24,p2) < 311/528000.**

4. Transverse sensitivity satisfies |partial_2 c| < 13887753264/22000. Consequently, the shift from the central-slice minimizer has magnitude smaller than 13887753264*delta/22000.

This is a theorem about a two-parameter statistical observer; these two variables are not asserted to give a complete native spatial slice of the X6 world.

## Proof

**Precise predecessor input.** PREFIX-635, proved with a 189-level exact Bernstein/integer-interval certificate at enterprise-math commit ec03483204af911eef75785bcdaf610d24519ab2, establishes on p2=p* throughout p1 in [a,b], for every q in [12,24]:

- 300 < partial_1 mu < 310;
- 23000 < partial_11 F_q < 50000;
- 168247/2^20 < c(12,p*) < 168248/2^20 and 167883/2^20 < c(24,p*) < 167884/2^20.

The new exact rational certificate tests transverse interpolation bounds and relies on those prior fixed-slice facts as explicit lemmas, rather than rerunning the original 189-level generator.

**Survivor and negative-binomial bounds.** Let N=189, M=N-1=188. The survival polynomials s_n for 0<=n<=M have Bernstein control coefficients equal to conditional survival probabilities, lying in [0,1]. Thus 0<=s_n<=1, |s_n'|<=M and |s_n''|<=2M^2 on [0,1]. Define w(n,m)=binom(n+m,n)/2^(n+m+1). The infinite sequence in m is negative-binomial, with sum_m w=1 and sum_m m*w=n+1; finite truncations preserve the corresponding upper bounds.

Put alpha_n=1-sum_{m=0}^M w(n,m)s_m(p2) and beta_n=n+1-sum_{m=0}^M (n+m+1)w(n,m)s_m(p2)/2. The infinite weights give 0<=alpha_n<=1, 0<=beta_n<=n+1<=N, |partial_2 alpha_n|<=M, |partial_2 beta_n|<=NM. In the exact PREFIX-622/635 moment reduction,

mu=sum_m s_m(p2)+sum_n alpha_n s_n(p1),
U=partial_1 mu=sum_n alpha_n s_n'(p1), U2=partial_11 mu=sum_n alpha_n s_n''(p1),
J=partial_1 H=sum_n beta_n s_n'(p1), J2=partial_11 H=sum_n beta_n s_n''(p1),
W=2H-mu^2.

The displayed bounds imply everywhere on [0,1]^2:

0<=mu<=2N, |U|<=NM, |U2|<=2NM^2,
|partial_2 mu|<=2NM, |partial_2 U|<=NM^2, |partial_2 U2|<=2NM^3,
|partial_2 J|<=N^2 M^2, |partial_2 J2|<=2N^2 M^3.

Now F'_q=2(J-mu U)-U/q and F''_q=2(J2-U^2-mu U2)-U2/q. Expanding their p2 derivatives using the product rule yields, for q>=12,

|partial_2(partial_1 mu)| <= K0=NM^2=6680016;
|partial_2(partial_1 F_q)| < K1=11 N^2 M^2=13887753264;
|partial_2(partial_11 F_q)| < K2=25 N^2 M^3=5933858212800.

Indeed, the upper envelope for the second displayed derivative is 2(1+2+2)N^2M^2+NM^2/q <11N^2M^2. For the third it is 2(2+2+4+4)N^2M^3+2NM^3/q <25N^2M^3. These are elementary global polynomial derivative estimates.

**Integration from the fixed slice.** The exact certificate verifies K0*delta<1 and K2*delta<1000. Integrating the p2 derivative along the transverse parameter segment gives 299<partial_1 mu<311 and 22000<F''_q<51000.

At p2=p*, strict convexity plus PREFIX-635's two rational root isolations give uniformly at each q endpoint q=12,24:

F'_q(a,p*) < -m_left, with m_left=23000*(167883/2^20-a)=318665/131072;
F'_q(b,p*) > m_right, with m_right=23000*(b-168248/2^20)=205827/16384.

Since F'_q is affine in 1/q, the inequalities remain true for all intermediate real q. The exact arithmetic certificate checks K1*delta < m_left and K1*delta < m_right. Thus integrating the transverse derivative preserves both gradient endpoint signs throughout R. The intermediate value theorem, F''_q>22000, and the analytic implicit-function theorem prove existence, uniqueness, and analytic stability of c.

Implicit differentiation of F'_q(c(q,p2),p2)=0 gives partial_q c=-partial_1 mu/(q^2 F''_q), which lies strictly between -311/(22000q^2) and -299/(51000q^2). Integrate from q=12 to 24, using integral_12^24 q^(-2) dq=1/24, to obtain the displayed strict uniform valley gap. Similarly partial_2 c=-partial_2 F'_q/F''_q gives the transverse sensitivity.

## Verification and next open problem

The companion Python standard-library Fraction certificate verifies ten exact rational inequalities and reports ALL_CHECKS_PASS 10. The JSON results include the exact constants and declared dependencies. PREFIX-635's fixed-slice certificate, the signed finite observer's model semantics, and the frozen native source pin are preserved as dependencies. This note does not claim an independent full 96-port rerun or formal review.

Next: use two-variable Bernstein subdivisions to enlarge the p2 radius toward the entire [37/256,39/256] interval. Separately certify endpoint-flank gradient signs on p1 in [3/20,4/25] and [161/1000,1/6] to extend uniqueness to the full earlier valley window. The full two-dimensional global maximum variance remains open.
