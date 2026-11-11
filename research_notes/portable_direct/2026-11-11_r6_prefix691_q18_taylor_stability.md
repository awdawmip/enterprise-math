# PREFIX-691-R6 — Exact q=18 crossover localization and narrow-parameter stability

Date: 2026-11-11 (Asia/Shanghai).
Role: independent author-side TASK_RESEARCH.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Mathematical object and exact source

Continue PREFIX-690 (immutable research note `awdawmip/enterprise-math@e1394a13ec0627a579db9414242a3633b773304e`), which established a crossing for every real q from about 11.9969 to 24.0224. Its exact Poissonized 189-layer survivor observer, joint-clock moment kernels and scientific pin remain fixed. Put

[
A(z)=operatorname{Var}(Y(z,z))-operatorname{Var}(Y(0,z)),quad
B(z)=E[Y(z,z)]-E[Y(0,z)],quad F_q(z)=qA(z)-B(z).
]

The difference of sampled variance objective values equals `q F_q(z)` for `q>0`; hence the zeros coincide.

**Immutable predecessor numerical certificate:** `PREFIX680_R6_RESULTS.json` and `PREFIX680_R6_EXACT_THIRD_ORDER_CROSSOVER_CERTIFICATE.py` at commit `2c91711f60aa74d93880780929f532da24140ec0`. Their exact center derivative floors (not rounded nearest decimals) at `b=53/1000`, scaled by `10^8`, are

[
(A_0,A_1,A_2): (44000296,-168056589514,-6667624082229),
]
[
(B_0,B_1,B_2): (789752024,12845959424,-99127959112).
]

For each listed exact derivative `g_j`, the actual `g_j(b)` lies in the half-open interval `[floor_j/10^8,(floor_j+1)/10^8)`. The predecessor supplies globally valid `|A'''|le 218571424275456` and `|B'''|le 69527880576` on the relevant `z` domain. This note checks exact rational *implications* of those inherited inputs; it does not rerun the original survivor recurrence.

## Theorem 691.1: 25-nanounit spatial corridor for q=18

Define exact rational endpoints

[
l=0.053000730,qquad r=0.053000755.
]

There is exactly one root of `F_18(z)=0` in `(l,r)`. Thus

[
oxed{0.053000730<z_{18}<0.053000755.}
]

The bracket has width `25/10^9=2.5×10^{-8}`, whereas the PREFIX-690 common existence interval `(0.0528706,0.0530659)` has width `0.0001953` (a factor of 7812).

## Theorem 691.2: a parameter-stable corridor

For every real `q` in the **entire closed interval**

[
oxed{17.9998le qle18.0002},
]

there is exactly one zero `z(q)in(l,r)`. Throughout the product rectangle, the strict certified inequalities hold:

[
0.4386<A(z)<0.4389,qquad
-32000<F'_q(z)<-29000<0.
]

The root is differentiable (also at endpoints in the one-sided sense), strictly increasing in `q`, and obeys the sharper uniform slope bounds

[
oxed{1.39	imes10^{-5}<z'(q)<1.50	imes10^{-5}.}
]

The bounds are model-internal statements about these two frozen readouts, not an assertion about a native physical-time orbit or a global maximum of the two-parameter objective.

## Exact proof

Let `t=z-b`, `t_l=730/10^9`, `t_r=755/10^9`. For each function `G∈{A,B}`, the rational Taylor inclusion is

[
sum_{j=0}^2 rac{g_j^- t^j}{j!}-M_Grac{t^3}{6}
le G(b+t)<
sum_{j=0}^2 rac{g_j^+t^j}{j!}+M_Grac{t^3}{6},
]

where `g_j^- = floor_j/10^8`, `g_j^+=(floor_j+1)/10^8`, and `M_A=218571424275456`, `M_B=69527880576`. Since `tge0`, every inequality direction is preserved.

Taking `F_{18}=18A-B` and the appropriate interval endpoints, exact rational arithmetic gives

[
F_{18}(l)>0.000101210605,qquad
F_{18}(r)<-0.000120795289.
]

Taylor's derivative formula, `G'(b+t)=G'(b)+G''(b)t+arepsilon` with `|arepsilon|le M_G t^2/2`, gives for every `t∈[t_l,t_r]`:

[
-1742.912<A'<-1618.318,qquad
128.439<B'<128.479.
]

In particular `A'<0`, so the extreme values of `A` on the corridor are bounded by the Taylor interval at `r` (lower) and `l` (upper); direct exact rational comparisons give

[
0.438718436<A(z)<0.438790311.
]

For any `qin[17.9998,18.0002]`, `F_q=F_{18}+(q-18)A`. Evaluating the worst shifts `0.0002A` at both ends yields the fully uniform strict signs

[
F_q(l)>0.00001345254,qquad
F_q(r)<-0.00003303722.
]

Using `F'_q=qA'-B'`, the derivative rectangle is enclosed by exact rational quantities satisfying

[
-31501.241<F'_q<-29257.857.
]

The intermediate value theorem, strict derivative sign and implicit-function theorem prove existence, uniqueness, differentiability and monotonicity. Since `z'(q)=A(z(q))/(-F'_q(z(q)))`, the same rational enclosures give

[
0.00001392702<z'(q)<0.00001499735,
]

which proves the stated simpler strict slope bounds. Every decimal in the proof is a **strict rational inequality**, and the companion JSON gives the underlying exact fractions; no floating-point rounding is used in the checker.

## Verification, sources and next unit

Run `python3 PREFIX691_R6_TAYLOR_Q18_CERTIFICATE.py` using the standard library. The checker verifies exact jet-floor implications, both parameter-uniform endpoint margins, the global derivative enclosure and both derivative bounds. Local execution returned `ALL_CHECKS_PASS PREFIX691-R6`. Numerical and inference evidence is in `PREFIX691_R6_RESULTS.json`. The inherited 189-row certificate remains author-side, unreviewed; no independent review or formal Result is asserted.

**Next discriminating unit:** certify the root count on the *entire* common bridge `0.0528706<z<0.0530659` for `q=12,18,24`, using overlapping exact derivative subintervals (or Sturm/Bernstein). This new `q=18` corridor supplies a precise internal anchor to join the two PREFIX-688 endpoint corridors. Then pursue the PREFIX-675 full boundary-versus-interior variance comparison on `0le ple zle1/2`.
