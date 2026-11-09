# PREFIX-625-R6 — Global bivariate BRC variance-optimizer comparative statics

Date: 2026-11-09 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**.
Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Dependencies: PREFIX-610, 613, 621, 622, 623, 624, in particular the exact 189-level first-passage recurrence and coefficient central-unimodality. This is an independent signed-direction/neutral-observer result; the original BRC 96-port graph is not rerun.

## Model and question

A native trial returns `(i,+)` with probability `p_i/q`, `(i,-)` with probability `(1-p_i)/q` for each `i=1,2`, neutral otherwise. The actual slots have `q=12` (slot 0) or `q=24` (slots 1 and 2). The same thinning experiment is defined for real `q>=2`. By sign symmetry restrict to the square `D=[0,1/2]^2`; the edges are a continuous model closure.

Each direction stops at the **first** informative-sign count where the PREFIX-621 exact anytime-confidence width is at most `1/4` with `beta=1/40`. Let `T_q(p_1,p_2)` be the number of original native action trials until both directions finish. Define `J(p)` as a single-direction stopping count, and `s_n(p)=Pr(J(p)>n)=sum_k A_n(k)p^k(1-p)^(n-k)`. From the pinned exact certificate, `s_n=0` for `n>=189`, each `s_n` is symmetric and nondecreasing for `0<=p<=1/2`, and `s_25(p)=1-p^25-(1-p)^25` is **strictly increasing** on this half interval.

## Theorem A — strict coordinatewise Poissonized mean monotonicity

Give each direction its own independent rate-one Poisson clock and sign sequence; let `S_i(p_i)` be the first-passage continuous waiting time, `Y=max(S_1,S_2)`, `mu=E[Y]`, and `W=Var(Y)`. For fixed `p_2 in [0,1/2]`, and every `0<=a<b<=1/2`,

`mu(a,p_2)<mu(b,p_2)`;

likewise in the other coordinate. Both `mu` and `W` are continuous on `D`.

**Proof.** Independent signs and Poisson arrivals yield
`U(t;p)=Pr(S(p)>t)=exp(-t)*sum_(n=0)^188 s_n(p)t^n/n!`.
The inherited coefficient-unimodality checks give `s_n(b)>=s_n(a)`, with a strict inequality for `n=25`; hence `U(t;b)>U(t;a)` for every `t>0`. By independence,

`mu(p_1,p_2)=integral_0^infty [U(t;p_1)+U(t;p_2)-U(t;p_1)U(t;p_2)]dt`.

Subtracting the expressions for `b` and `a` gives
`integral_0^infty (U(t;b)-U(t;a))*(1-U(t;p_2))dt>0`.
The second factor is strictly positive for any `t>0`: a same-sign 25-hit completion has positive probability even at parameter boundaries. The 189-hit cap ensures continuity and integrability. QED.

## Theorem B — global comparative statics without optimizer localization

For any `2<=q_1<q_2` define `A(q)=Argmax_(p in D) Var(T_q(p))`. For **every** `x in A(q_1)` and **every** `y in A(q_2)`,

`mu(y)>=mu(x)`, `W(y)>=W(x)`,

with the stronger sandwich for `d=mu(y)-mu(x)`:

`0<=d`, `d/q_2 <= W(y)-W(x) <= d/q_1`.

**Proof.** Superpose informative Poisson streams each of rate `1/q` and a neutral Poisson stream of rate `1-2/q`. The superposition has unit rate and exactly the original trial label probabilities. The continuous stopping time has law `qY`. Conditional on the discrete trial count `T_q`, the time is a sum of `T_q` independent unit exponential gaps, giving the exact identities

`E[T_q]=q*mu`, `Var(T_q)=q^2*W-q*mu`.

Therefore optimizing variance is equivalent to optimizing `F_q=W-mu/q`. Optimality of `x` for `q_1` and `y` for `q_2` yields

`W(y)-W(x) <= [mu(y)-mu(x)]/q_1`,
`W(y)-W(x) >= [mu(y)-mu(x)]/q_2`.

For `d<0` these bounds conflict, so `d>=0` and then `W(y)>=W(x)`. Compactness assures maximizers exist. QED.

## Theorem C — strict full-square comparison for the two actual slots

For every `x in A(12)` and `y in A(24)`,

`mu(y)>mu(x)` and `W(y)>W(x)`.

In particular the maximizers may remain unlocated and nonunique.

**Proof.** If `mu(y)=mu(x)`, Theorem B forces `W(y)=W(x)`, making both `x` and `y` common global maximizers of `F_12` and `F_24`. At any such common optimizer `z`, an interior coordinate `0<z_i<1/2` would give both first-order conditions `partial_i W(z)-partial_i mu(z)/12=0` and `partial_i W(z)-partial_i mu(z)/24=0`, hence `partial_i mu(z)=0`, contrary to Theorem A (the derivative is strictly positive from `s_25`). Thus a common optimizer can occur only at the corners, up to coordinate permutation: `(0,0)`, `(0,1/2)`, `(1/2,1/2)`.

The companion exact Fraction certificate reconstructs the PREFIX-621 recurrence and verifies the rational witness

`Var(T_12(0,1/8)) > Var(T_12(c))` for all three corner points `c`.

No corner maximizes `F_12`, so no common optimizer exists. Theorem B's bounds now yield both strict inequalities. QED.

## Exact evidence, reuse, and next question

Execute in the `research_notes/portable_direct` directory:
`python PREFIX625_R6_bivariate_global_optimizer_certificate.py`

It imports the previously Source-published `PREFIX621_R6_stochastic_tail_certificate.py`, rechecks 9,025 central-coefficient inequalities, exact rational moments and three strict edge/corner witness inequalities, and the q=12/24 variance-transfer identity. It emits `ALL_CHECKS_PASS` and `PREFIX625_R6_RESULTS.json`. Display-only variances at `q=12`: edge witness `82195.2926`; corners `2535.9938`, `25155.0347`, `17445.4370`. All comparisons use exact rational arithmetic.

The result orders the standardized mean and Poissonized variance of **all full-square global optimizer pairs** when observation thinning changes, while leaving optimizer coordinates as a genuine open question.

Next unit: certify whether every global maximizer of the bivariate variance lies on a boundary face, using exact bivariate Bernstein subdivision; then test coordinatewise optimizer location ordering (as opposed to the now-proved `mu` ordering). The original source pin, observer scope, user P000 and independent review requirements are unchanged.
