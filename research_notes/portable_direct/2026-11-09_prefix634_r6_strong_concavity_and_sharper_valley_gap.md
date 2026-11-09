# PREFIX-634-R6 — Uniform quantitative valley order and strong concavity in inverse BRC thinning

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Role: independent TASK_RESEARCH mathematical note; no formal CLAIM/Result/Review asserted.
Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Scope: exact signed two-information-direction first-passage *statistical observer* of PREFIX-621/622; native thinning q=12 and q=24, extended to real q>=12. The original 96-port native graph is a frozen dependency.

## Definitions and theorem

Fix p2 in B=[37/256,39/256], p=p1 in I=[3/20,1/6]. Write Y for the maximum of two independent unit-rate informative Poisson stopping times, mu(p)=E[Y], W(p)=Var(Y). The native-trial stopping-time variance satisfies V_q(p)=q²W(p)-q mu(p), so its interval-I minimizers are M(q)=Argmin_I F_q, where F_q(p)=W(p)-mu(p)/q.

Define exact positive rationals

```
L=5244748236
C=1/2 + binom(50,25)/2^51
m=C*(217/256)^25*25*((5/6)^24-(1/6)^24)
kappa=m*m/L
```

**Theorem 1.** For all p in I and p2 in B, partial_p mu(p,p2)>m. This is a 9.9066885965-fold stronger explicit lower bound than PREFIX-633's one-term bound.

**Theorem 2.** For all real 12<=q1<q2, and *every* a in M(q1), b in M(q2),

```
a-b >= (m/L)*(1/q1-1/q2)>0.
```

In particular for native q1=12, q2=24,

```
a-b > 1/50000000000000 = 2*10^(-14),
```

improving the previous uniform `9/(4*10^15)` separation.

**Theorem 3.** With t=1/q in (0,1/12], define Phi(t)=min_(p in I){W(p)-t*mu(p)}. Then Phi(t)+(kappa/2)t² is concave. This is a global strong-concavity modulus in inverse thinning, valid without uniqueness of the valley minimizer.

## Proof

PREFIX-621's first-stop survivor polynomials s_n(p)=P(J(p)>n), n=0,...,188 satisfy s_n'(p)>=0 for p in [0,1/2] and s_25'(p)=25((1-p)^24-p^24), decreasing on I. PREFIX-632's exact Poisson-clock formula gives

```
mu'(p,p2)=sum_n alpha_n(p2)*s_n'(p)
alpha_n(p2)=sum_(r>=0)w(n,r)P(J(p2)<=r)
w(n,r)=binom(n+r,n)/2^(n+r+1).
```

The first 25 signs of direction 2 all being negative forces J(p2)<=25, and that event has probability (1-p2)^25 >=(217/256)^25. Hence

```
alpha_25(p2) >= (217/256)^25 * sum_(r>=25) w(25,r).
```

For two independent rate-one Poisson arrival streams, the number M of second-stream arrivals before the 26th first-stream arrival has law w(25,r). Among the first 50 combined arrivals each stream label is a fair coin. Thus, exactly,

```
sum_(r>=25) w(25,r)
 = P(Binomial(50,1/2)<=25)
 = 1/2+binom(50,25)/2^51 = C.
```

The remaining nonnegative s_n' contributions, and strictly positive additional J-completion events with later r, give mu'(p,p2)>C*(217/256)^25*s_25'(1/6)=m. This proves Theorem 1.

By PREFIX-631/632, for every q>=12 all M(q) are interior, and for q1<q2 every b in M(q2) lies strictly left of every a in M(q1). At these stationary minimizers, F_q1'(a)=0 and F_q2'(b)=0, so

```
F_q2'(a)=mu'(a)*(1/q1-1/q2)>=m*(1/q1-1/q2).
```

The global bound of PREFIX-627 is |F_q''|<=L on the full relevant parameter square, for q>=2. Hence by the mean value inequality over [b,a],

```
L*(a-b)>=F_q2'(a)-F_q2'(b)>=m*(1/q1-1/q2).
```

Exact Fraction comparison in the companion certificate establishes m/(24L)>1/50000000000000. This proves Theorem 2.

For t1<t2, let b be any minimizer for Phi(t1), a any minimizer for Phi(t2). From Theorems 1 and 2,

```
mu(a)-mu(b)>=m*(a-b)>=m²*(t2-t1)/L=kappa*(t2-t1).
```

Phi is the infimum of affine functions of t, hence concave. Its superdifferential consists of convex combinations of slopes -mu(p) for minimizers p. The displayed inequality holds for every active pair and for their convex hulls, so any supergradients g1 at t1 and g2 at t2 satisfy g1-g2>=kappa*(t2-t1). Therefore supergradients of Phi+(kappa/2)t² are nonincreasing, proving its concavity. QED.

## Certificate, reuse, next unit

Run the companion `PREFIX634_R6_uniform_q_valley_strong_concavity_certificate.py` with the Python standard library. It independently checks the 25-term rational negative-binomial tail, exact binomial identity, strict improvement of the lower bound, strict q12/q24 gap, and positivity of kappa. Executed locally 2026-11-09: `ALL_CHECKS_PASS`; digest stored with the script. Approximate display only: m≈0.00280715610728466, gap≈2.2301325543270082e-14, kappa≈1.5024792527840162e-15.

Reuses PREFIX-621/622/625/627/631/632/633 at their precise published proof scopes; the certificate checks the new rational arithmetic, not independent admission of its upstream results. Next: bound the Hessian on I by exact Bernstein intervals to sharpen L, certify uniqueness of the local valley, and continue the separate two-dimensional global-maximum variance question.
