# PREFIX-764 / R6 — Algebraic mixed-curvature phase and improved exact bounds

Date: 2026-11-14. Scientific input **frozen** at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: `AUTHOR_ANALYTIC_PROOF_AND_EXACT_RATIONAL_FINITE_CHECK / UNREVIEWED / NOT_ADMITTED`.
Scope: external independent two-Gamma-clock BRC auxiliary model, not a native X6 or three-dimensional-slice theorem.
Frontier: PREFIX-760 exact 189-layer Fraction file (24,743 bytes; SHA256 `1a480a9a05c4773f82091037fa8f6b695855ffbb885b21e804d56fdc181d4e76`), PREFIX-763 mixed-curvature factorization.

## Definitions and inherited finite inputs

Let `S_i(x)=Pr(T_x>i)` for `0<=i<=188`, with `T_x<=189`. Each `S_i` is a rational polynomial in `x`, symmetric under `x -> 1-x`, and `S_i'(x)>=0` on `[0,1/2]`. PREFIX-757/758 establish `S_i=1` for `i<25` and
`S_25(x)=1-x^25-(1-x)^25`.
Set
`H_x(t)=exp(-t) sum_{i=0}^{188} S_i(x)t^i/i!`,
`Y(p,z)=max(C_p,C_z)`, `mu=E[Y]`, `V_q=q^2 Var(Y)-q mu`.
The clocks are independent conditioned on their respective first-stop layers.

Define the rational polynomials `a_i(x)=S_i'(x)/(1-2x)`, extending to `x=1/2` by polynomial cancellation. They are nonnegative on the closed half-interval and `a_25(x)>0` throughout it. In particular, **a_i=0 for i<25**. Define `W_x(t)=exp(-t) sum_i a_i(x)t^i/i!` and
`A_0=integral W_p W_z dt >0`,
`B_0=integral t W_p W_z dt`,
`u_0=integral W_p(1-H_z)dt`,
`v_0=integral W_z(1-H_p)dt`.
All integrals are from zero to infinity. PREFIX-763 proved
`partial_p partial_z V_q = q(1-2p)(1-2z)[A_0 - 2q N]`,
where `N=B_0+u_0 v_0-mu A_0`; the identity extends continuously to the boundary.

## Theorem 764.1 — exact polynomial sign oracle

All five objects `A_0,B_0,u_0,v_0,mu` are rational-coefficient bivariate polynomials. The bidegrees are bounded by
`deg A_0,deg B_0 <= (186,186)`,
`deg u_0 <=(186,188)`,
`deg v_0 <=(188,186)`,
`deg mu <=(188,188)`,
and `deg N <=(374,374)`.
Consequently for any **rational q>0**, the sign of every interior mixed derivative of `V_q` is the sign of the explicit rational polynomial
`P_q(p,z)=A_0(p,z)-2q N(p,z)`.
There is no denominator sign decision: `A_0>0` on the closed square.

**Proof.** The finite killed-Pascal probabilities are Bernstein polynomials `S_i` of degree at most `i`. Their symmetric derivatives are divisible by `1-2x`, hence `deg a_i<=i-2<=186`. Integrating products of `W` and `H` amounts to finitely many rational Erlang integrals; thus the displayed polynomials and bidegrees follow by multiplication. The mixed-derivative identity is the exact PREFIX-763 factorization after cancelling `A_0`. At interior points the prefactor `q(1-2p)(1-2z)>0`. QED.

**Exact box method.** For any rational rectangle `[a,b]x[c,d]` inside `[0,1/2]^2`, transform `P_q(a+(b-a)s,c+(d-c)t)` into its bivariate Bernstein basis of bidegree `(374,374)`. Nonnegative (respectively nonpositive) rational Bernstein coefficients give an exact certificate of nonnegative (respectively nonpositive) mixed derivative on the whole box; strictly signed coefficients give a strict interior sign. Exact rational integration of the polynomial identity also gives the rectangular mixed difference. No numerical sampling or variance-monotonicity inference is required. This is a **certificate algorithm**, not an assertion that a previously uncovered grid cell has already passed it.

## Theorem 764.2 — phase threshold is algebraic

Let `Theta=N/A_0`, `Theta_max=max_{[0,1/2]^2}Theta>0` (positivity established in PREFIX-763), and `q_c=1/(2 Theta_max)`. Then **q_c is a positive real algebraic number**.

**Proof.** `Theta` is a continuous rational function on a compact rational rectangle with positive rational-polynomial denominator. Its graph and its maximum set are semialgebraic over the rational numbers. By quantifier elimination for real closed fields, the set of attainable values and its upper endpoint are semialgebraic over `Q`, so the finite endpoint `Theta_max` is real algebraic. Since it is positive, `q_c` is real algebraic. This argument is existential; it does **not** calculate its minimal polynomial or isolate it sharply. QED.

Equivalently the strict feasibility predicate
`exists p,z in [0,1/2]: 2q N(p,z)>A_0(p,z)`
is a complete real-algebraic decision problem for `q>q_c`. The quantified variables `p,z` are continuous real parameters, while every coefficient is rational from the frozen integer recursion.

## Theorem 764.3 — tighter uniform rational bracket

For `25<=i,j<=188`, let `K_ij=binom(i+j,i)/2^(i+j+1)`. The exact minimum on the **actual derivative support** is
`kappa=K_25,188=K_188,25=binom(213,25)/2^214 =
30141887180622283134311072159421 /
3291009114642412084309938365114701009965471731267159726697218048`.
It is the unique minimum up to swapping the indices.

For all `p,z in [0,1/2]` write `alpha=sum_{i>=25} a_i(p)`, `beta=sum_{j>=25}a_j(z)`. Then `A_0>=kappa alpha beta`, `u_0<=alpha`, `v_0<=beta` and `B_0/A_0<=377/2`. Since `mu>0` we obtain
`Theta_max < kappa^(-1)+377/2`, whence
`q_c > 1/(2/kappa+377)` (**strict**).

The previous PREFIX-763 lower bound was `1/(2^190+377)`. The improved bound is approximately `4.5794293073383636e-33`, an increase by approximately `7.186385913043567e24` in the guaranteed lower bound.

**Proof of the kernel minimum.** For fixed `j`, the adjacent ratio `K_(i+1),j/K_i,j=(i+j+1)/(2(i+1))` is above one up to the mode and below one afterwards; the minimum over an integer interval therefore occurs at an endpoint. Apply the same argument to `j`, reducing to the four corners of `[25,188]^2`. Exact comparison of these four rational numbers gives the stated two minima. The remaining bounds are nonnegative-mixture estimates; the `B_0/A_0` estimate is the weighted average of `(i+j+1)/2` over `i,j<=188`. QED.

Let `dvar = Delta_[0,1/4]x[0,1/4] Var < 0` and `dmu = Delta_[0,1/4]x[0,1/4] mu < 0`, whose exact Fractions are recovered by subtracting the two PREFIX-760 rows `z=0,1/4`. Define the exact rational switching point `q_R=dmu/dvar`. For `q>q_R`, this single rectangle has `Delta V_q=q(dvar*q-dmu)<0`, so `q_c<=q_R`. The exact Fraction checker proves
`190005/1000000 < q_R < 190006/1000000`.
Combining gives the rigorous bracket

`boxed( 1/(2/kappa+377) < q_c < 190006/1000000 )`.

The smaller numerical upper endpoint and much stronger lower endpoint both improve PREFIX-763. The exact global optimum `q_c` remains to be isolated.

## Finite computational evidence

Accompanying checker `PREFIX764_R6_PHASE_CERTIFICATE_CHECK.py` requires the original frozen `PREFIX760_R6_EXACT_GAMMA_VARIANCE_RESULTS.json` in the same directory; it verifies the 24,743-byte SHA256, examines **26,896** exact rational kernel pairs on `[25,188]^2`, proves the corner minimum by exhaustive comparisons, calculates the precise rational `q_R` and checks both strict rational inequalities. Local execution: `ALL_CHECKS_PASS PREFIX764`. File `PREFIX764_R6_PHASE_CERTIFICATE_RESULTS.json` holds machine-readable witness summaries.

**Boundaries and next research.** This is a proof in the external Gamma-clock auxiliary model. The algebraicity/degree statements are analytic; the loop is exact finite corroboration of the kernel and rectangle calculations. No new `1/768` grid exclusion is claimed. Next: use exact bivariate Bernstein coefficients of `P_q` on a previously uncertified rational parameter box, or use rational interval subdivision to isolate `Theta_max` further. Preserve distinct native X6/P000 transfer obligations and independent review.
