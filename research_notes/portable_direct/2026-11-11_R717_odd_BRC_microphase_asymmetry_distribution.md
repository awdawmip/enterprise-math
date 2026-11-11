# R717 — Exact law and Gaussian scaling for odd BRC microphase residual asymmetry

Date: 2026-11-11 (Asia/Shanghai). Author-side mathematical derivation, independent review pending.

Parent task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, immutable publication `TP2-8B7E13C5904A2D6F1142`. Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, unchanged. Inputs: R715 @ `ccc019123731b3ef59497c7f064151b0e3c00c7f`; R716/R716b @ `1ed250c30b02e42cc0eb57beded21eed8630df9d`.

## Population, BRC carrier, and observer

Retain the exact five-phase R712–R716 candidate event scheduler. Let the number m of labelled ring edges be odd and at least five. Edge i selects a pair (p_i,q_i) with 1<=p_i<q_i<=5, and adjacent cyclic edges have disjoint pairs, so no Cell joins two basic transfers in one phase. Each edge carries two distinct source-labelled, positive TRANSFER events, whose placement into its selected pair has two possible temporal orders. For j=1,2,3,4, put D_j=#{i:p_i<=j<q_i}. Restrict to the area-minimal family A=sum_j D_j=m+3.

R715 proves every area-minimal profile has a unique triple (r,s,t) of nonnegative integers satisfying r+s+t=k=(m-5)/2:

    D=(2+r+s, 2+t, 2+s, 2+r+t).

Define the nonnegative residual-asymmetry observation

    R=D_1-D_3=D_4-D_2=r.

The full, source-labelled BRC history is preserved as the underlying object. R is a typed temporal-boundary observer, not a signed amplitude or seventh spatial coordinate. Uniform probability below always means finite counting measure on the declared population, never a physical random-mechanism assumption.

## Theorem R717-A: exact asymmetry distribution

For every odd m>=5 and every integer 0<=r<=k=(m-5)/2, the number of fixed-root phase-pair histories with asymmetry r is

    W_m(r)=8m * binom(k+r+1,2r+1).

The number of unoriented, spatially unrooted dihedral bracelet classes at r is

    B_m(r)=4 * binom(k+r+1,2r+1).

If both source-labelled event orderings are retained independently on every edge, multiply each count by 2^m. Hence the uniform distribution on rooted phase-pair words, bracelets, or their fully typed versions is identical:

    P(R=r)=binom(k+r+1,2r+1)/F_(2k+2),

with F_0=0, F_1=1 and F_(n+2)=F_(n+1)+F_n.

**Proof.** R715 provides exactly N_m(r,s,t)=8m binom(r+s,s)binom(r+t,t) rooted histories for each triple. Fix r, let n=k-r and sum over s+t=n. Formal Vandermonde convolution gives

    sum_(s+t=n)binom(r+s,s)binom(r+t,t)
      = [x^n](1-x)^(-2r-2)
      = binom(k+r+1,2r+1).

This proves W. R716 proves the dihedral action on area-minimal phase-pair words is free, with orbit cardinality 2m; R is invariant under that action. Division by 2m gives B. Assigning the two distinct positive source-type labels to the two phases on each physical edge yields exactly 2^m type-orderings, all retaining the same R. R716b shows the total bracelet count is 4F_(2k+2), completing the normalized law. QED.

## Theorem R717-B: bivariate generating function and exact moments

Set

    H_k(u)=sum_(r=0)^k binom(k+r+1,2r+1)u^r.

Then the exact formal generating function and recurrence are

    G(x,u)=sum_(k>=0)H_k(u)x^k=1/(1-(2+u)x+x^2),

    H_0=1, H_1=2+u,
    H_k=(2+u)H_(k-1)-H_(k-2) (k>=2).

In particular H_k(1)=F_(2k+2).

For n=k+1, write F=F_(2n) and L=L_(2n), with Lucas sequence L_0=2,L_1=1,L_(j+2)=L_(j+1)+L_j. The exact finite-population mean and variance are

    E[R] = n*L/(5*F)-3/5,

    Var(R) = 2*n*L/(25*F)-4*n^2/(25*F^2)-2/25.

**Proof.** Summing independently over s,t>=0 for fixed r gives

    G(x,u)=sum_(r>=0)(u*x)^r/(1-x)^(2r+2)
          =1/((1-x)^2-u*x).

For real u>0 let lambda(u)=(2+u+sqrt(u(u+4)))/2; the second characteristic root is lambda(u)^(-1). Therefore

    H_k(u)=
       [lambda(u)^(k+1)-lambda(u)^(-k-1)]/sqrt(u(u+4)).

Put z=log u, gamma(z)=log lambda(exp(z)), delta(z)=sqrt(exp(z)(exp(z)+4)), and K_k(z)=log(H_k(exp(z))/H_k(1)). At z=0:

    gamma'(0)=1/sqrt(5), gamma''(0)=2/(5sqrt(5));
    (log delta)'(0)=3/5, (log delta)''(0)=2/25.

Because lambda(1)=phi^2, with phi=(1+sqrt(5))/2, the even-index Fibonacci/Lucas identities give

    coth(n*gamma(0))=L_(2n)/(sqrt(5)*F_(2n)),
    csch^2(n*gamma(0))=4/(5*F_(2n)^2).

Differentiating K once and twice at zero yields the stated exact rational formulas. QED.

## Theorem R717-C: typical positive linear asymmetry and a Gaussian law

As k tends to infinity,

    E[R]=k/sqrt(5)+O(1),
    Var(R)=2k/(5sqrt(5))+O(1),

and in distribution,

    (R-k/sqrt(5))/sqrt(2k/(5sqrt(5)))
        --> standard Normal(0,1).

**Proof.** For z in a sufficiently small complex neighborhood of 0, lambda(exp(z)) is analytic and its magnitude dominates the reciprocal root. The characteristic-root formula gives, uniformly there for some c<1,

    log(H_k(exp(z))/H_k(1))
       =(k+1)(gamma(z)-gamma(0))
        -(log delta(z)-log delta(0))+O(c^k).

Insert z=i*t/sqrt(2k/(5sqrt(5))), subtract the k/sqrt(5) centering term, and Taylor-expand gamma to quadratic order. The linear terms cancel, the quadratic term tends to -t^2/2, and the analytic remainder tends to zero. Levy's continuity theorem proves weak convergence. The exact moment identities independently give the O(1) error bounds. QED.

An exact lower-tail consequence is

    P(R=0)=(k+1)/F_(2k+2),

    P(R<=1)=[k+1+binom(k+2,3)]/F_(2k+2) (k>=1).

The area-and-peak jointly optimal profiles from R715 have R<=1, whereas a uniformly selected area-minimal history has asymmetry of order m (fluctuation scale sqrt(m)). The R<=1 region is exponentially rare in the area-optimal ensemble.

## Theorem R717-D: how little of the raw BRC history four boundary counts encode

The map (r,s,t)->D in R715 is injective. Thus the exact number of distinct area-optimal boundary vectors is

    P_m=binom(k+2,2)=(m-1)(m-3)/8.

For *any* probability measure on these histories, the four-boundary vector D carries at most log2(P_m)=O(log m) Shannon bits. The exact number of source-typed, fixed-root histories is 2^m*U_m with U_m=8m F_(m-3). By pigeonhole, the largest D-fiber contains at least 2^m*U_m/P_m histories and therefore takes at least ceil(log2(2^m*U_m/P_m)) bits to identify with a fixed-length raw-history code once D is known.

This is an exact raw-history reconstruction bound for the specified observer. A predictive V39 quotient requires a separate observer-equivariance certificate under the frozen allowed future operations.

## Reproducible validation

The accompanying Python verifier `R717_ODD_ASYMMETRY_VERIFY.py` completely enumerates legal rooted cyclic pair words of minimal excess three for odd m=5,7,9,11,13,15,17, recomputing all four D_j for every word and checking the whole histogram of R against W_m(r). The enumerated rooted totals are respectively 40, 168, 576, 1,848, 5,720, 17,280, 51,272.

Separately for k=0,...,500 (501 exact integer parameter checks, m up to 1005), it compares the binomial coefficient distribution with integer Fibonacci/Lucas recurrences and an independent exact recurrence for the first two H_k derivatives at u=1, including both rational moment identities. All assertions passed in a local Python standard-library run: `R717_ODD_RING_ASYMMETRY_EXACT_PASS`. The companion JSON records output counts and selected rational examples. Finite checks corroborate, but do not replace, the proofs for all odd m.

**BRC method resolution:** COMPOSE_APPLIED (R715 labelled event provenance and exact profile fibers, R716 free dihedral action). The compressed R observer retains only the explicitly stated boundary contrast. Scientific pin remains unchanged. The five-phase inventory/Cell scheduler is the previously declared candidate; the full native Link/Port and V39 observer mapping is the next separate research question.

## Next executable research question

For a fixed, source-verified native Link/Port/V39 future-operation interface, test whether two source-typed histories with the same (m,A,D) can yield different relation output. A witnessed difference supplies the precise additional BRC repair coordinate; a proof that all allowed future operations descend through the given quotient permits predictive-state compression under the certified horizon.