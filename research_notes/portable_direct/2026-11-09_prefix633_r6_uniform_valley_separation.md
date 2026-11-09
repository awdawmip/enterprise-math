# PREFIX-633-R6 — Uniform positive separation of BRC q=12 and q=24 variance valleys

Date: 2026-11-09 Asia/Shanghai.
Researcher-ID: EM-DIRECT-23F213 / TASK_RESEARCH.
Research-Activity-ID: RA-C7D075E0C0D860ED02903F38.
Status: AUTHOR_PROVED / EXACT_ARITHMETIC_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen science: f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Exact theorem

Use the PREFIX-621/622 signed two-direction first-passage model. Fix any p2 in [37/256,39/256]. Denote I=[3/20,1/6], V_q(p1)=Var(T_q(p1,p2)), mu(p1)=E[Y(p1,p2)], and W(p1)=Var(Y(p1,p2)). For every

    a in Argmin_I V_12, b in Argmin_I V_24,

the strict ordering from PREFIX-632 can be sharpened to an explicit, p2-uniform rational inequality:

    a - b > 9/(4*10^15).                                   (1)

All quantities are real-model parameters. The constant is deliberately conservative; this is a rigorous strictly positive separation of *all* minimizing pairs without assuming uniqueness.

## Proof

PREFIX-632 proves that b<a, that both are interior to I, and that F_q=V_q/q^2=W-mu/q has F_12'(a)=F_24'(b)=0. Thus

    F_24'(a) = mu'(a)*(1/12-1/24) = mu'(a)/24 > 0.          (2)

The global exact second-derivative envelope from PREFIX-627, valid on the entire parameter square for q>=2, is

    |F_24''(p1)| = |V_24''(p1)|/24^2 <= L = 5244748236.

The mean-value theorem on [b,a] therefore gives

    L(a-b) >= F_24'(a)-F_24'(b)=mu'(a)/24.                 (3)

It remains to obtain a strictly positive uniform lower bound for mu'(a). By the finite survivor law (PREFIX-621/625),

    mu'(p1,p2) = sum_(n=0)^188 alpha_n(p2) s_n'(p1),

with all alpha_n(p2)>0 and all s_n'(p1)>=0 for p1 in (0,1/2). In particular,

    mu' >= alpha_25(p2)*s_25'(p1).

The exact negative-binomial weights and first-passage event give

    alpha_25(p2)
     = sum_(m=0)^infty w(25,m) Pr_(p2){J<=m}
     >= w(25,25)*(p2^25+(1-p2)^25)
     >= (C(50,25)/2^51)*(217/256)^25.

Furthermore on I, where p1<=1/6,

    s_25'(p1)=25*((1-p1)^24-p1^24)
             >=25*((5/6)^24-(1/6)^24).

Define the fully explicit positive rational

    m0 = (C(50,25)/2^51)*(217/256)^25
         *25*((5/6)^24-(1/6)^24).

Combining with (3) gives

    a-b >= m0/(24*5244748236).

The accompanying standard-library Fraction certificate checks the exact strict rational inequality

    m0/(24*5244748236) > 9/(4*10^15).

This establishes (1) for all p2 in the stated interval and all minimizing pairs. QED.

## Exact verification

Execute 'python PREFIX633_R6_uniform_valley_gap_certificate.py'. The script performs the integer-combination and rational-power computation, the strict rational margin comparison, and writes PREFIX633_R6_RESULTS.json. Executed output: ALL_CHECKS_PASS a-b > 9/(4*10^15). The constructed rational gap lower bound displays approximately 2.2511382411906136e-15; the simpler bound in (1) is 2.25e-15.

The proof analytically reuses PREFIX-627's global Hessian bound and PREFIX-632's interval minimum/strict order theorem, both under the immutable BRC signed-observer stopping model. It is not an independent rerun of the original 96-port graph or an assertion that stationary points are unique.

## Next research unit

Improve the quantitative separation by certifying the restricted-interval Hessian rather than reusing PREFIX-627's deliberately coarse global bound; try exact Bernstein second-derivative interval sign to certify uniqueness and stable minimizer branches over p2 in [37/256,39/256]. The separate two-dimensional global MAXIMUM variance problem remains open.
