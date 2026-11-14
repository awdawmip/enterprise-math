# PREFIX-779 / R6 — Sharp two-noise robustness frontier for approximately reflected Gamma readouts

Date: 2026-11-14 (Asia/Shanghai). Research lane: 进取数论研究6. Previous recorded researcher: `EM-DIRECT-E77192`; original SID: `MCP-d9aca4ec6e00440eba66035326ea5a4e`. Status: `AUTHOR_ALGEBRAIC_PROOF_WITH_RATIONAL_REGRESSION / UNREVIEWED / NOT_ADMITTED`.

**Scientific pin:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Input theorem: PREFIX-778 (`research_notes/portable_direct/2026-11-14_r6_prefix778_reflection_equivariant_sharp_radius.md`); exact four-cell Gamma coefficients from its frozen 189-layer killed-Pascal, two independent unit-rate Gamma clocks. The following is a new exact algebraic consequence of those verified coefficient inequalities, not an additional original-comparator experiment.

## Precise scalar observer problem

Take base squares `R1=[38,39]^2/768`, `R2=[39,40]^2/768` and their reflections in the second parameter `R1#=[38,39]x[729,730]/768`, `R2#=[39,40]x[728,729]/768`. For `V_q=q² Var(Y)-q E[Y]`, set
`A_i=-Delta_Ri E[Y]>0`, `B_i=-Delta_Ri Var(Y)>0`, `x_i(q)=A_i-q B_i`.
PREFIX-778's exact integer kernel establishes `0<B1<B2` and `D=A2 B1-A1 B2>0`. Hence each base mixed increment is `q x_i` and each reflected increment is `-q x_i`.

A prospective scalar readout `Vhat_q` at the **14 vertices** is allowed two independent, nonnegative error budgets:

1. Amplitude: `|Vhat_q(v)-V_q(v)| <= q epsilon` for every vertex.
2. Reflection defect: `|Vhat_q(v#)-Vhat_q(v)| <= q delta` for every one of the seven reflected pairs. The reference `V_q` is itself exactly invariant under this reflection.

Both bounds hold at the selected `q>0`; the observer need not arise from a native comparator. Reflection error is an observer-pair bound, not a spatial axis, signed-Port, or event-time identity.

Write `d=min(delta,2 epsilon)`, `K=2 B1+4 B2`, and `G=D-K epsilon-B1 d`.

## Theorem 779.1 — two-sided quantitative certificate

For every real `q>0` and every readout satisfying the two budgets,

`max_{R in {R1,R2,R1#,R2#}} Delta_R Vhat_q >= q G/(B1+B2)`,

`min_{R in {R1,R2,R1#,R2#}} Delta_R Vhat_q <= -q G/(B1+B2)`.

Thus **if `G>0`, the four fixed cells simultaneously display a strictly positive and a strictly negative mixed increment**. The bounds are uniform in `q>0`.

### Exact proof

Let `e_v=(Vhat_q(v)-V_q(v))/q` for base vertices and `f_v=(Vhat_q(v#)-V_q(v#))/q` at their reflections. Then `|e_v|,|f_v|<=epsilon`, `|e_v-f_v|<=delta`, hence also `|e_v-f_v|<=d`. The two adjacent base squares have exactly one common vertex `c=(39,39)/768`; its mixed-difference coefficient is `+1` in **both** cells. All other six corners are private (three per square).

Let `L_i` be the signed four-corner mixed-difference functional on base square i. Normalized increments, ordered as base/mirror, are
`y_i=x_i+L_i e`, `z_i=-x_i-L_i f`.
The key q-elimination identity is
`B2 x1-B1 x2=-D`.

Among all allowed errors, the exact support-function bound is
`B2 L1 e-B1 L2 f <= K epsilon+B1 d`.
Indeed, the six private terms contribute at most `3(B1+B2)epsilon`. At the common corner, maximize `B2 e_c-B1 f_c`; with `B2>B1`, its maximum is `(B2-B1)epsilon+B1 d`, reached at `e_c=epsilon`, `f_c=epsilon-d`. Adding yields `K epsilon+B1d`. Exchanging e and f gives the same bound for `B2 L1 f-B1 L2 e`.

Consequently,
`B2 y1+B1 z2=-D+B2 L1e-B1 L2f <= -G`;
`B2 z1+B1 y2=D-B2 L1f+B1 L2e >= G`.
A weighted mean of two real numbers with strictly positive weights `B2,B1` lies between them. Divide each inequality by `B1+B2` to obtain both claimed extrema.

## Theorem 779.2 — exact *sharp* tradeoff (necessity as well as sufficiency)

Fix any `delta>=0`. Define
`C=D/(B1+B2)` (the PREFIX-777 four-cell margin), and

`epsilon_crit(delta)=(D-B1 delta)/(2(B1+2B2))` for `0<=delta<=C/2`;

`epsilon_crit(delta)=C/4` for `delta>=C/2`.

Then every `0<=epsilon<epsilon_crit(delta)` forces both strict signs for all `q>0`, while at `epsilon=epsilon_crit(delta)` an admissible readout exists at a positive `q` for which **all four increments are nonnegative**. Thus the radius is the largest uniform strict-sign guarantee for this declared 14-corner observer class.

### Constructive sharpness proof

The continuous increasing function `F(e)=K e+B1 min(delta,2e)` satisfies `F(0)=0`. Its unique solution `F(e)=D` is exactly the above piecewise `epsilon_crit`; the regime switch occurs at `delta=C/2=2(C/4)`.

Put `e=epsilon_crit(delta)`, `d0=min(delta,2e)` and `q0=(A1+4e)/B1>0`. Then `x1(q0)=-4e` and, using `D=K e+B1d0`, `x2(q0)=2e+d0`.

Choose the common base/reflected errors `e_c=e`, `f_c=e-d0`. On each of R1's three private vertices give both e and f the signed values that contribute `+3e` to `L1`. On each of R2's three private vertices give both e and f the signed values that contribute `-3e` to `L2`. Every vertex has amplitude at most e and the only nonzero reflection defect is d0 at the shared vertex. The four normalized increments are explicitly

`(y1,z1,y2,z2)=(0,d0,d0,0)`.

This has no strictly negative increment, so the strict two-sign conclusion fails at the threshold. For `epsilon>epsilon_crit`, the same witness still satisfies the looser amplitude bound.

**Endpoint consistency.** At `delta=0`, `epsilon_crit=D/[2(B1+2B2)]`, the exact PREFIX-778 equivariant radius. At `delta>=C/2`, the radius is `C/4`, the exact PREFIX-777 unrestricted-corner radius. For intermediate defects the optimal radius decreases linearly with slope `-B1/[2(B1+2B2)]`. The worst-case asymmetry can be concentrated at the **single shared corner**, a concrete target for observer fidelity tests.

## Verification and scope

The companion Python checker uses SymPy exact symbolic identities plus `fractions.Fraction` on three independent rational coefficient sets. It checks positivity of q0, the piecewise switch, the exact endpoint construction for four delta regimes, and strict interior gaps; it prints `ALL_CHECKS_PASS PREFIX779 SHARP_TWO_NOISE_TRADEOFF`. This is a proof-checking regression for the universal algebraic reduction; the model-specific integer inequalities `B2>B1>0,D>0` are inherited from PREFIX-778's saved 189-layer checker and immutable paper. No floating-point data are required for this theorem.

For the frozen Gamma cells, PREFIX-778 already gives `epsilon_crit(0)≈9.02075853734e-8`, PREFIX-777 gives `C≈2.7096259882e-7`, and thus the saturation radius `C/4≈6.7740649705e-8`. The transition defect is `C/2≈1.3548129941e-7`. These decimals are contextual displays; the symbolic formula in exact inherited A_i,B_i is the certificate.

**Native research boundary:** This is a theorem for the external scalar Gamma observer on four defined grid cells. The original typed X6/BRC comparator's reflection/readout error budgets must be measured or proved before applying this result there. Historical original-comparator exclusion count change: 0. Shared CLAIM, formal Result and independent review: none.

## Unfinished discriminating unit

At the 14 corresponding native observations, recover typed Cell/Link/Port, signed source, branch and time identity; estimate amplitude `epsilon` and paired reflection defect `delta` with an explicit observation map. The new sharp phase line `K epsilon+B1 min(delta,2epsilon)=D` then decides four-cell robustness on a certified parameter range.