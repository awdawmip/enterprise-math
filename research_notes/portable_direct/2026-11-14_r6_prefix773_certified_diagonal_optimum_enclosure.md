# PREFIX-773 / R6 — Certified rational enclosure of the Gamma diagonal minimum

Date: 2026-11-14 (Asia/Shanghai).
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: `AUTHOR_EXACT_INTEGER_AND_INHERITED_INTERVAL_LEMMA / UNREVIEWED / NOT_ADMITTED`.
Model: the **external** independent two-Gamma-clock 189-layer first-stop BRC auxiliary. This note does not modify native X6, P000, or the historical 1/768 comparison-cell tally.

## Definitions and inherited continuous theorem

Set `Y(p,z)=max(C_p,C_z)`, `mu=E[Y]`, `W=Var(Y)`, and `Q(p,z)=A(p,z)/D(p,z)` with `A=-partial_pz mu` and `D=-partial_pz W>0`. Along the diagonal write `f(u)=Q(u,u)`.

PREFIX-772 established that over the entire closed rational interval

\[
I=\left[\frac{502971451}{10^{10}},\frac{502971452}{10^{10}}\right]
\]

the denominator is positive, `4<f''(u)<5`, and exactly one stationary point `u_*` exists. The latter is the strict local two-parameter minimum identified in PREFIX-772. We reuse this specific continuous theorem, with its original frozen scientific input.

## Exact rational first-jet evaluation

Take two new rational witnesses

\[
u_0=\frac{5029714515}{10^{11}},\qquad
u_1=\frac{502971451537}{10^{13}}.
\]

Reconstruct the 189 killed-Pascal survivor rows using the exact frozen integer width predicate. There are exactly 9529 surviving positions, and row 189 is empty. Compute the survivor polynomials and their first two derivatives as integers over one common denominator. For

\[
K_{ij}=\binom{i+j}{i}2^{-(i+j+1)},\qquad
L_{ij}=(i+j+1)K_{ij},
\]

all Gamma contractions are integer sums after multiplication by a common power of two. At a diagonal point, let `m=2 sum(s)-s^T K s`, `v=sum(d)-d^T K s`, `A=d^T K d` and `B=d^T L d`. Then

\[
D=B+2v^2-2mA,\quad
A'=2e^TKd,\quad
B'=2e^TLd,
\]

\[
v'=\sum_i e_i-e^TKs-A,\quad
D'=B'+4vv'-4vA-2mA',
\]

and

\[
f'(u)=\frac{A'D-AD'}{D^2}.
\]

The complete standard-library verifier evaluates all these quantities with integers, asserts `D>0` at both witnesses, and establishes

\[
f'(u_0)<0<f'(u_1).
\]

At `u_1`, the displayed values (not used for sign decisions) are

\[
f(u_1)\approx 0.02851859116285760930846368814316697103306983168,
\]

\[
g=f'(u_1)\approx 3.63362523707479010709\times10^{-14}.
\]

## Theorem 773.1 — sharply localized unique stationary point

For every twice-differentiable real function with one stationary point `u_*` in `I`, with `4<f''<5` everywhere on `I`, and with `g=f'(u_1)>0`, the mean-value integral gives

\[
4(u_1-u_*)<g<5(u_1-u_*).
\]

Thus

\[
u_1-\frac g4<u_*<u_1-\frac g5.
\]

Exact integer multiplication at the rational witness proves the outward-rounded rational enclosure

\[
\boxed{
0.05029714515369091593<u_*<
0.05029714515369273275.
}
\]

The width of this explicit interval is `1.81682e-15`, improving the previously certified width `1e-10` by more than 55000-fold.

## Theorem 773.2 — certified local minimum value

The same strict second-derivative bounds give the strong-convexity/smoothness inequalities

\[
f(u_1)-\frac{g^2}{8}<
\min_{u\in I}f(u)=f(u_*)<
f(u_1)-\frac{g^2}{10}.
\]

The exact integer certificate produces the outward-rounded enclosure

\[
\boxed{
0.02851859116285760930846368797812
< \min_{u\in I}Q(u,u) <
0.02851859116285760930846368801114.
}
\]

Its width is `3.302e-29`. This is a bound on the **diagonal interval minimum**, not an assertion that this is the minimum on the full parameter square.

## Theorem 773.3 — improved global critical-phase upper bound

PREFIX-763 defines the global mixed-curvature threshold `q_c`. A point where `D>0` gives `q_c\le A/D`. Integer cross multiplication at `u_1` proves

\[
q_c\le Q(u_1,u_1)<
\boxed{\frac{2851859116285760930847}{10^{23}}
=0.02851859116285760930847}.
\]

The previous PREFIX-772 upper bound was `0.028518591162857609310`.

## Reproduction and next question

Run `python3 research_notes/portable_direct/PREFIX773_R6_EXACT_DIAGONAL_LOCAL_BOUNDS.py` with the Python standard library. The tested exact script returned `ALL_CHECKS_PASS PREFIX773`; the companion JSON holds the reported rational enclosures and provenance. The executable file and JSON were checked by Git blob against the original locally executed and produced files. The arithmetic consists of finite exact integer sums, positive-denominator tests, and cross products; decimal rounding is outward by floor/ceiling. The only inherited nontrivial analytic premise is PREFIX-772's continuous `4<f''<5` certificate.

Next scientific question: determine whether any off-diagonal or boundary point of `[0,1/2]^2` with `D>0` gives a smaller value of `Q(p,z)`; apply verified interval comparison to unresolved original Gamma cells. A coarse independent floating-point survey is exploratory only and is not used in the present exact certificate.
