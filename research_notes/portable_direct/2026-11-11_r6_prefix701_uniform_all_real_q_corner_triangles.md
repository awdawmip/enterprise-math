# PREFIX-701-R6 — Uniform corner-triangle exclusion for every real observation slot q >= 2

Date: 2026-11-11 (Asia/Shanghai).
Researcher-ID: `EM-DIRECT-6653A5 / TASK_RESEARCH`.
Research-Activity-ID: `RA-8E29AD2111E41EF38CEF51CA`.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Evidence: `AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED`.
Predecessors: PREFIX-621/625 signed first-stop frozen count model and mean shape, PREFIX-630 global derivative-envelope identities, PREFIX-700 exact rational three-corner witness.

## Theorem 701.1 — Four certified exclusion triangles on the entire real-q ray

On the auxiliary two-informative-direction BRC first-stop observer, let `D=[0,1/2]^2`, `q>=2` real and

```text
mu(p,z)=E[Y(p,z)]
H(p,z)=E[Y(p,z)^2]/2
W(p,z)=2H(p,z)-mu(p,z)^2
V_q(p,z)=q^2 W(p,z)-q mu(p,z).
```

The two coordinates are independent *observer probabilities* for the two separately labelled signed-information directions inside the frozen X6 context; they are not native physical spatial axes or a native two-plane.

Let `e=(0,1/8)`, `rho=1/65536`, `C={(0,0),(0,1/2),(1/2,0),(1/2,1/2)}`, and `T_c={x in D: |x_1-c_1|+|x_2-c_2|<=rho}`.

**For every real q>=2, every c in C, and every x in T_c,**

```text
V_q(e)-V_q(x) > (7356197/65536) q^2 > 112 q^2.
```

Consequently all four positive-area corner triangles are excluded from `Argmax_D V_q` simultaneously for the full continuous parameter ray `q>=2`. Each triangle has area `rho^2/2=1/2^33` in the symmetry-reduced parameter square; the four triangles are disjoint.

## Proof and exact certificate

**Step 1: use the newly computed all-real-q corner certificate.** PREFIX-700's exact 189-row integer/Fraction replay counted 9529 nonzero survivor cells and computed the witness differences

```text
delta_mu(c)=mu(e)-mu(c), delta_W(c)=W(e)-W(c).
```

Its certified strict rational bins of width 1/10^6 are:

| corner | delta_mu range in ticks 1e-6 | delta_W range in ticks 1e-6 |
|---|---|---|
| (0,0) | [48811611,48811612) | [557257209,557257210) |
| (0,1/2) | [-111509701,-111509700) | [386820427,386820428) |
| (1/2,1/2) | [-119288768,-119288767) | [439711044,439711045) |

The missing fourth corner shares the second row by exchanging the two labelled streams. For each corner and every `q>=2`,

```text
(V_q(e)-V_q(c))/q^2 = delta_W(c)-delta_mu(c)/q
                 >= delta_W(c) - max(delta_mu(c),0)/2 > 386.
```

The last inequality is an exact rational implication of the table: c00 has lower margin `532851403/1000000`, c01 has lower margin `386820427/1000000`, and c11 has lower margin `109927761/250000`. All exceed 386.

**Step 2: uniform derivative bound on the full square.** Retain PREFIX-630's exact Poisson-clock moment kernel and prefix-free survival polynomials `s_n` for `0<=n<=188`. Their Bernstein coefficients belong to `[0,1]`, so for any p in [0,1] one has `|s_n'(p)|<=n`. The derivatives of the moment kernels can be written

```text
mu_i = sum_{n=0}^{188} alpha_n(other coordinate) s_n'(own coordinate),
H_i  = sum_{n=0}^{188} beta_n(other coordinate)  s_n'(own coordinate),
0<=alpha_n<=1,  0<=beta_n<=n+1.
```

These inequalities follow from the nonnegative exact negative-binomial kernels. Consequently

```text
|mu_i| <= sum_{n=0}^{188} n = 17766,
|H_i|  <= sum_{n=0}^{188} n(n+1) = 2250360,
0<=mu<=378.
```

Differentiation of `W=2H-mu^2` gives

```text
|W_i| <= 2*2250360 + 2*378*17766 = 17931816.
```

For every real `q>=2`, the normalized variance `G_q=V_q/q^2=W-mu/q` satisfies

```text
|partial_i G_q| <= 17931816 + 17766/2 = 17940699 =: M
```

at every point of the square.

**Step 3: integrate along one straight segment in the convex observer-parameter square.** For `x in T_c`, the fundamental theorem of calculus on the segment from corner c to x gives

```text
|G_q(x)-G_q(c)| <= M*(|x_1-c_1|+|x_2-c_2|) <= M/65536.
```

Therefore

```text
G_q(e)-G_q(x) > 386 - 17940699/65536
                = 7356197/65536 > 112.
```

Multiplication by `q^2>0` yields the asserted uniform strict witness gap. QED.

## Verification, mathematical scope, continuation

The companion standard-library script `PREFIX701_R6_UNIFORM_CORNER_TRIANGLES.py` recomputes the universal derivative-envelope integer sums and exactly checks the rational lower margins for all three corner symmetry classes, including the strict radius inequality. Local result: `ALL_CHECKS_PASS PREFIX701-R6`. The companion `PREFIX701_R6_RESULTS.json` contains exact intervals, the new radius and margin.

The script checks new implications of the existing PREFIX-700 189-row witness and PREFIX-630 moment-kernel facts; it does not repeat the 189-row count construction, and no native heartbeat time/state update or BRC–Shor calculation is performed.

This unit supplies four certified **positive-area** exclusion neighborhoods for the full mother objective on `D` and for all real `q>=2`, without locating the remaining full-square maximizers. It extends the already established corner exclusion by an explicit, nonzero uniform radius.

**Next unit:** combine the global boundary maxima in PREFIX-675 and the strip exclusions PREFIX-629/670/674 to get a signed Bernstein exclusion mesh outside the narrow active boundary band. For an interval of real `q`, a single fixed rational competitor reduces each pointwise comparison after division by q to an affine inequality in q; endpoint certificates can cover the entire real-parameter interval. Preserve original Source owner/review/admission rules.
