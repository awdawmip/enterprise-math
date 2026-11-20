# Stage327-B — An earlier exact two-source competitor and an algebraic slope jump

**Date:** 2026-10-31. **Classification:** `PORTABLE_AUTHOR_PROOF_AND_COUNTEREXAMPLE / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED`. **Scientific scope:** auxiliary three-future-visit, two-source positive Bernoulli BRC observer only; this is not a P000-native X6 theorem.

## Actual frozen provenance and permission state

- Same current canonical global snapshot for this author turn: `awdawmip/chatgpt-global-knowledge main@970b5c00edacde19d0a8c5b6a6660e77d9877f57` (read from remote GitHub `main` on 2026-10-31); governing entry `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, Enterprise Math project bootstrap, P000 original, ACTIVE worldview and math/code/BRC research policies were read at this pin.
- Project canonical control source: `awdawmip/enterprise-math main@d93aeaece6d8d0916680c5de40ad66a7fbeaa18b`, with its `docs/PORTABLE_RESEARCH_PROTOCOL.md` and continuation guidance. The Stage325-B author note is located at immutable `71e1c73f8ff8c97ffaf2ff73c89e95ea4b9ed48a`. Stage326-B is a noncanonical local handoff (`enterprise_math_stage326b_portable_20261031.zip`), complete but previously not published to a GitHub branch.
- The native `em_control_tasks` owner query returned `CONTROL_QUOTA`. `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` with `auth_mode=static_machine_readonly`, `operation_sent=false`. Thus this author turn has **no native session, verified Task owner, CLAIM, Result, Driver review or Foundation admission**. No other person's identity was assumed.
- Inherited Stage307-B.2 author claims give the unique minimizer `(x*,y*)`, satisfying `r0=r1=0`, in the brackets stated below. Those global-optimality claims and Stage324-B's endpoint theorem remain author-only and were **not independently re-audited**. The new finite inequality/derivative checks below are exact within their declared brackets.

## Model, units and inherited minimizer brackets

For `k=0,1,2,3` let

\[
B_k(z)=z^k(1-z)^{3-k},\qquad p=(61,21,9,9)/160,\qquad
r_k(x,y)=\tfrac45B_k(x)+\tfrac15B_k(y)-p_k.
\]

The single-group public TV budget and source-tagged loss are

\[
d(x,y)=\tfrac12\sum_{k=0}^3\binom3k|r_k(x,y)|,\quad b(x,y)=\tfrac5{16}d(x,y),
\]

\[
D_3(a,z)=\tfrac12\sum_{k=0}^3\binom3k|B_k(a)-B_k(z)|,
\quad c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

The inherited eight-parameter reduction takes the form

\[
P=b(x,y)+b(x',y'),\qquad T=33/1024+c(x,y)+c(x',y').
\]

Retain the Stage307-B.2 rational enclosures

\[
\frac{231083940855521}{10^{15}}<x_*<\frac{231083940855522}{10^{15}},\quad
\frac{555508857277}{10^{12}}<y_*<\frac{555508857278}{10^{12}},
\quad \beta_*=b(x_*,y_*),\quad P_{\min}=2\beta_*.
\]

These are **finite real auxiliary probability parameters**, not X6 coordinates or native three-axis slice components. Labeled source provenance is retained until the declared public observer quotient.

## Theorem 1 — A strictly earlier rational symmetric two-group competitor

Define the rational rate `X=24001/100000=0.24001`; there is a unique `Y\in(58/100,59/100)` such that `r_1(X,Y)=0`. Set the rational competitor

\[
q=\left(\frac{2354398}{10^7},\frac{5688542}{10^7}\right).
\]

On the increasing rightward `r1=0` branch from `(x*,y*)`, write `\varepsilon_w=b(X,Y)-\beta_*`. Then the following **strict** inequalities hold:

\[
0.002863<\varepsilon_w<0.002864,
\]

\[
\underbrace{b(x_*,y_*)+b(X,Y)-2b(q)}_{\text{public budget slack}}>2\times10^{-8},
\]

\[
\underbrace{c(x_*,y_*)+c(X,Y)-2c(q)}_{\text{tagged cost improvement}}>5\times10^{-8}.
\]

Thus the two identical groups `(q,q)` have *strictly lower* public TV budget and *strictly lower* tagged loss than the proposed single-group continuation `((x*,y*),(X,Y))`. This single-group continuation therefore is **not globally optimal at this particular budget**; its formula is obstructed at some budget no greater than the displayed `\varepsilon_w`. Compared with Stage326-B's author-certified bound `<0.003014`, this is a strictly earlier witness. It does *not* prove that `(q,q)` is globally optimal, nor locate the **first** global optimizer switch.

**Exact verification.** `\partial_y r_1(X,y)=(1/5)(1-y)(1-3y)<0` on `(0.58,0.59)` and rational endpoint signs are opposite. Ninety-six exact-rational bisection steps enclose `Y`. For each `B_k(z)` on a rational interval, the program evaluates endpoints and the possible interior critical point `k/3`, with rational arithmetic only. Composing interval enclosures through each signed word discrepancy and then the TV absolute values gives the following strict intervals in units of `10^{-12}`:

| Quantity | Exact-rational certified enclosure (units 10^-12) |
| --- | --- |
| `epsilon_w` | `(2863295202,2863295203)` |
| public budget slack | `(25536,25537)` |
| tagged cost improvement | `(64622,64623)` |

Open interval conventions are justified by the strict algebraic root brackets; reported floor/ceil endpoints are conservative. All four Bernoulli word counts are retained. No sampled real grid, float root, or signed-phase cancellation is used as proof. The executable is `REPRO_STAGE327B.py`; run output is `REPRO_STAGE327B_EXECUTED_STDOUT.txt`.

## Theorem 2 — Exact positive upward kink in the **candidate** tagged cost slope

Define

\[
y_\dagger=\frac{1+\sqrt{13}}8, \quad
r_1(x_\dagger,y_\dagger)=0,\quad
0.237806902<x_\dagger<0.237806904.
\]

The real root is unique because `r1_x>0` and `r1_y<0` here. The `k=2` tagged discrepancy has the exact factorization

\[
B_2(3/4)-B_2(y)=\frac{(4y-3)(16y^2-4y-3)}{64}.
\]

It crosses zero transversely at `y=y_\dagger`, and **all other** `B_k(a)-B_k(z)` terms occurring in `c` are strictly nonzero in the stated narrow rational rectangle. The public residuals at this point satisfy `r0<0`, `r1=0`, `r2>0`, `r3<0`; hence along the right branch in a neighborhood,

\[
b(x,y(x))=\frac{15}{16}r_2(x,y(x)),\qquad \frac{db}{dx}>0.
\]

Set `g(z)=z(2-3z)` and `h(z)=(1-z)(1-3z)`. The implicit derivative and the *positive* one-sided slope jump are

\[
y'=\frac{dy}{dx}=-\frac{4h(x)}{h(y)}>0,\quad
b'=\frac{15}{16}\left(\frac45g(x)+\frac15g(y)y'\right)>0,
\]

\[
\boxed{\left[\frac{dc}{db}\right]_{+}-\left[\frac{dc}{db}\right]_{-}
=\frac{21}{256}\frac{g(y_\dagger)y'(x_\dagger)}{b'(x_\dagger)}>0.}
\]

Only the `7D_3(3/4,y)/256` term contributes the jump: the derivative of `|f(y)|` gains `2|f'(y)|` at a transverse zero; its multiplicity is `\binom32=3`, and `D_3` contributes half that multiplicity. Exact rational interval propagation on

\[
\frac{575693909432998}{10^{15}}<y_\dagger<\frac{575693909432999}{10^{15}},\qquad
\frac{237806902}{10^9}<x_\dagger<\frac{237806904}{10^9}
\]

certifies

\[
\boxed{0.11665548<\Delta(dc/db)<0.11665549.}
\]

This is an **upward corner of the old candidate single-group branch**, not an assertion that the complete Pareto optimum inherits that corner. The Stage326 tagged sign transition occurs at `0.00218<\varepsilon_\dagger<0.00219`, strictly before the witness of Theorem 1; existence of a tagged sign transition does *not* establish a global optimizer transition.

## Reproducibility, scope, and next discriminating problem

Executed `python REPRO_STAGE327B.py` with exit code 0; the actual stdout ends with `STAGE327B_EARLIER_WITNESS_AND_TAGGED_CUSP_EXACT_PASS`. Rational interval arithmetic uses Python `fractions.Fraction`; no scientific numerical inference depends on a floating-point input. No historical 253/290-leaf global Pareto certificate was rerun. Theorem 1's reference to the Pareto continuation is **conditional** on the inherited reduction and minimizer brackets. Theorem 2's tagged-word kink, sign chamber and derivative identity are proved locally without an inherited global-optimality claim.

Next task **Stage328-B**: compute lower global exclusion bounds across all public-TV and tagged-TV sign chambers on `0.0002<\varepsilon<0.002864`, using rational KKT or complete interval sign partitions. At minimum distinguish (a) loss of optimality within one group, (b) asymmetric two-group allocation, (c) symmetric two-group allocation and (d) the `y_\dagger` tagged chamber boundary. Any exact *first* switch statement requires positive global exclusion evidence against all other competitors, not merely a witness. Native P000 bridge remains separately open: ordered signed X6 steps, explicit three-dimensional slice with third-coordinate semantics, triadic closure, independently ordered time and registered lossless six-nonnegative-field Cell addresses.
