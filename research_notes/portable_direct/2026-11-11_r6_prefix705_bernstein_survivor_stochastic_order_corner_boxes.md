# PREFIX-705-R6 — BRC survivor stochastic order and a 900,000-fold larger certified corner exclusion

Date: 2026-11-11 (Asia/Shanghai).
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Dependencies: PREFIX-621/622 first-stop and Poissonized clocks, PREFIX-700 full integer survivor recurrence, PREFIX-701 global derivative and PREFIX-704 earlier corner triangles.
Status: AUTHOR_RECOMPUTED / EXACT_FRACTION_BERNSTEIN_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Object, question and precise observer

The original two independently labelled signed first-stop BRC streams are retained. In one stream, let N_p be its informative sign stopping count: 25<=N_p<=189, with s_n(p)=P(N_p>n) for n=0,...,188, for bias parameter 0<=p<=1/2. The path population and survivor multiplicities are those of the 189-level frozen first-passage recurrence. Given N_p=k, the unit-rate Poisson completion clock T_p has the gamma(k,1) law. For independent T_p,T_z, let Y(p,z)=max(T_p,T_z), mu=E[Y], W=Var(Y), and V_q=q^2 W-q mu for real q>=2. The square D=[0,1/2]^2 is the auxiliary statistical-observer parameter domain, not the native X6 spatial plane.

## Theorem 705.1 — Every survivor tail is monotone on the full bias interval

For every n=0,...,188 and all real 0<=p<=p'<=1/2:

    s_n(p)<=s_n(p').

Thus the exact finite first-stop count family N_p is first-order stochastically nondecreasing in p throughout [0,1/2].

**Exact complete Bernstein certificate.** The existing PREFIX-700 integer recurrence gives s_n(p)=sum_{k=0}^n a[n,k] p^k(1-p)^(n-k), where a[n,k] is the exact count of still surviving signed paths after n informative steps. Define Bernstein control coefficients r[n,k]=a[n,k]/C(n,k), so s_n(p)=sum C(n,k) r[n,k] p^k(1-p)^(n-k). For n>=1 the derivative polynomial has degree n-1 Bernstein coefficients

    d[n,k]=n*(r[n,k+1]-r[n,k]),  k=0,...,n-1.

Restrict that derivative from [0,1] to [0,1/2] by exact de Casteljau subdivision at 1/2. Its n Bernstein coefficients on [0,1/2] are the first values at the n successive de Casteljau levels, beginning with d[n,0]. The accompanying verifier checks all 1+2+...+188=17766 restricted derivative coefficients with exact Python Fraction. Counts: 4513 zero, 13253 strictly positive, **zero negative**. The polynomial Bernstein basis is pointwise nonnegative on its domain and its coefficients are all nonnegative. Therefore s'_n(p)>=0 for all p in [0,1/2], establishing the theorem (n=0 is constant). This finite exhaustive check includes every n and every derivative coefficient; it is a complete algebraic certificate for the frozen finite survivor model, not point sampling.

## Theorem 705.2 — Four macroscopic closed corner boxes uniformly excluded for ALL real q>=2

Set epsilon=1/64 and e=(0,3/20). Let C be the union of the four CLOSED squares of side epsilon at the four corners of D. For all real q>=2, all (p,z) in C:

    V_q(e)-V_q(p,z) > (93/10)*q^2 >0.

In particular, no maximizer of V_q over D can lie in C.

**Step 1: exact individual-clock variance bounds from Theorem 705.1.** For N in [25,189], the unit-rate gamma mixture T has E[T]=E[N] and Var(T)=E[N]+Var(N). As N>=25,

    Var(T)<=E[N^2]-600.

The tail sum identity E[N^2]=sum_{n=0}^{188}(2n+1)s_n(p), and Theorem 705.1, show for every 0<=p<=1/64:

    Var(T_p) <= L = sum_{n=0}^{188}(2n+1)*s_n(1/64)-600
             < 1101/4 = 275.25.

For 31/64<=p<=1/2, write D_p=189-N_p. Then E[N_p]<=189, Var(N_p)=Var(D_p)<=E[D_p^2], and

    E[D_p^2] = sum_{n=0}^{188}(2*(189-n)-1)*(1-s_n(p)).

This expression is nonincreasing in p. Hence on this high-bias interval:

    Var(T_p) <= U = 189+E[D_(31/64)^2] <773/4=193.25.

The checker recomputes all exact rational survivor tail values at p=1/64 and 31/64. In certified millionth ticks, L lies in [275220940,275220941)/10^6 and U in [193171736,193171737)/10^6, verifying the rational bounds.

**Step 2: tensorized variance contraction of maximum.** For independent X,Y and iid independent copies X',Y', the standard Efron–Stein variance inequality gives

    Var(max(X,Y))
      <= (1/2)E[(max(X,Y)-max(X',Y))^2]
       + (1/2)E[(max(X,Y)-max(X,Y'))^2]
      <= Var(X)+Var(Y),

since max is 1-Lipschitz in each input. Each coordinate of every point in C lies either in the low or high interval. Therefore W(p,z) < 2*(1101/4)=1101/2=550.5 throughout C.

**Step 3: a fixed exact comparator, uniform in t=1/q.** Re-evaluate the PREFIX-704 witness e=(0,3/20) using the same exact 189-level rational moment kernel. The exact certificate gives

    W(e)-mu(e)/2 > 2799/5 =559.8,

with its rational millionth-tick enclosure [559812917,559812918)/10^6. For any t in (0,1/2], f_t(x):=W(x)-t*mu(x) satisfies f_t(e)>=W(e)-mu(e)/2>559.8 because mu(e)>0, and f_t(x)<=W(x)<550.5 for x in C because mu(x)>0. Thus

    f_t(e)-f_t(x) > 559.8-550.5 =93/10.

Multiplying by q^2 gives the theorem. The exact computed lower comparison margin (using actual exact L and U) is enclosed in [9371036,9371037)/10^6, so the simple bound 9.3 remains conservative.

## Area and actual gain

The four corner boxes of side 1/64 are disjoint. Their union has exact area

    4*(1/64)^2 =1/1024.

The previous PREFIX-704 uniform corner triangles of L1 radius 1/43251 occupy total area 2/(43251^2). Hence this theorem increases uniformly certified excluded area by the exact factor

    (1/1024)/(2/(43251^2)) = 1870649001/2048 > 900000.

The new shape is a square at each corner rather than a radius triangle, and the gain comes from **retaining the full BRC survivor tail information before comparing clock variances**. It is not a higher-resolution sample of the earlier Lipschitz estimate.

## Verifier, provenance and next scientific unit

Run `python PREFIX705_R6_CORNER_BOX_CHECKER.py` in the same directory as PREFIX700_R6_STRICT_OPTIMIZER_ORDER.py. It runs the established frozen integer recurrence and recomputes all 17,766 rational Bernstein coefficient signs, the two interval clock variance bounds, the witness moment inequality and the excluded-area ratio. Its complete numerical evidence is PREFIX705_R6_RESULTS.json. Local exact check: ALL_CHECKS_PASS PREFIX705-R6, with all 17,766 coefficients nonnegative and strictly positive comparison margin.

The new monotone-survivor-tail theorem is separately reusable: it controls any increasing function of the first-stop count, not only the first two moments. Next test whether the same stochastic ordering produces tighter bounds for the `max` observer on larger corner cells, and use exact conditional variance or Bernstein partition bounds to exclude additional interior regions, while preserving the complete-square PREFIX-675 global-maximization objective. No native heartbeat evolution, independent review or mathematical promotion is asserted.
