# P018 — Quotient-root / floor-power duality and inverse extremal form

Status: `ORDINARY MATHEMATICS PROVED / PRIOR-ART CORRECTION RECORDED / LEAN NOT YET VERIFIED`

Scope: P018 quotient-root atlas cardinality, ternary carry refinement, inverse precision threshold.

## 1. Canonical objects

For integers `r >= 1`, `n >= 1`, define

\[
\mathcal A_{r,n}:=\left\{R_r\!\left(\left\lfloor\frac nd\right\rfloor\right):1\le d\le n\right\},
\qquad N_r(n):=|\mathcal A_{r,n}|,
\]

\[
Q_{r,n}(t):=\left\lfloor\frac{n}{t^r}\right\rfloor\quad(t\ge1),
\qquad
\widetilde S_r(n):=\{Q_{r,n}(t):t\ge1\}.
\]

The extension to all positive `t` is deliberate: `\widetilde S_r(n)` always contains the terminal value `0`.

## 2. Exact drop duality

For every `t >= 1`, the exact denominator-fiber theorem gives

\[
\boxed{
t\in\mathcal A_{r,n}
\iff
Q_{r,n}(t+1)<Q_{r,n}(t).
}
\]

Thus quotient-root states are exactly the strict drops of the nonincreasing floor-power sequence. Consequently

\[
\boxed{N_r(n)+1=|\widetilde S_r(n)|.}
\]

For comparison with the standard finite powered floor set

\[
S_r(n):=\{Q_{r,n}(t):1\le t\le n\},
\]

the terminal-zero boundary is:

- `r=1`, any `n>=1`: `0` is absent from `S_1(n)`, so `|S_1(n)|=N_1(n)`;
- `r>=2`, `n>=2`: `Q_{r,n}(n)=0`, so `S_r(n)=\widetilde S_r(n)` and `|S_r(n)|=N_r(n)+1`;
- `n=1`, any `r>=1`: `S_r(1)={1}` while `\widetilde S_r(1)={1,0}`, hence `|S_r(1)|=N_r(1)=1` and `|\widetilde S_r(1)|=2`.

This is a structural duality, not merely a numerical coincidence: positive quotient-root fibers are the jump locations of the powered floor-function sequence.

## 3. Prior-art correction

The raw exact cardinality is not a new Enterprise Math theorem.

- Randell Heyman, *Cardinality of a floor function set*, Integers 19 (2019), arXiv:1905.00533, gives the exact `r=1` floor-quotient cardinality.
- Randell Heyman and MD Rahil Miraj, *On Some Floor Function Sets*, arXiv:2309.16072v4 (2024), Theorem 1, gives an exact cardinality formula for

\[
S_t(X)=\left\{\left\lfloor\frac{X}{k^t}\right\rfloor:1\le k\le X\right\},\qquad t>1.
\]

For integer `t=r>=2` and `n>=2`, the drop duality identifies their finite-set cardinality with `N_r(n)+1`; `n=1` is the explicit terminal-zero exception above.

Therefore P018 must classify **exact atlas cardinality** as prior-art-equivalent after transport through the quotient-root / floor-power duality. Enterprise Math contributions must be stated as refinements, transport theorems, formalization, or new structural consequences rather than as discovery of the raw cardinality formula.

## 4. Relation to the P018 horizon formula

Let

\[
H=R_{r+1}(rn-1),\qquad
D=\left\lfloor\frac{n}{(H+1)^r}\right\rfloor,
\qquad
\kappa=\mathbf 1[(D+1)H^r\le n].
\]

The P018 binary atlas decomposition gives

\[
N_r(n)+1=D+H+\kappa.
\]

For nonintegral `a=(rn)^{1/(r+1)}`, one has `H=floor(a)`, and the Heyman–Miraj overlap correction is the same binary carry `kappa` after rewriting adjacent floor values. When `a` is integral, `H=a-1`; the endpoint/divisibility carry supplies the boundary correction.

The stronger P018 ternary normalization

\[
N_r(n)+1
=H+\left\lfloor\frac Hr\right\rfloor+\tau,
\qquad \tau\in\{0,1,2\},
\]

therefore remains useful as an arithmetic normal form of the known exact cardinality, not as the first exact count.

## 5. Horizon-cell endpoint theorem

For fixed `h>=1`, put

\[
L_h=\left\lfloor\frac{h^{r+1}}r\right\rfloor+1,
\qquad
U_h=\left\lfloor\frac{(h+1)^{r+1}}r\right\rfloor,
\]

so `H=h` exactly on `L_h<=n<=U_h`. Let `q=floor(h/r)` and

\[
A_h=\max\{q(h+1)^r,(q+1)h^r\},
\qquad
B_h=(q+1)(h+1)^r.
\]

Then

\[
L_h\le A_h\le U_h,\qquad A_h<B_h,
\]

and

\[
\boxed{B_h\le U_h\iff r\mid(h+1).}
\]

Whenever active,

\[
\boxed{B_h=U_h.}
\]

Hence `tau=2` is never a positive-width subinterval of a fixed horizon cell: it is a single terminal state, appearing exactly for `h=-1 mod r`.

Boundary note: `h=0` is exceptional; `L_h<=A_h` is asserted only for `h>=1`.

## 6. Exact inverse precision threshold

Define

\[
T_r(m):=\min\{n\ge1:N_r(n)\ge m\},\qquad m\ge1.
\]

If

\[
q=\left\lfloor\frac{m}{r+1}\right\rfloor,
\qquad
h=m-q=\left\lceil\frac{rm}{r+1}\right\rceil,
\]

then

\[
\boxed{
T_r(m)=\max\{q(h+1)^r,(q+1)h^r\}.
}
\]

Equivalently, setting `M=m+1`,

\[
\boxed{
T_r(m)=\max_{0\le j\le M}j(M-j)^r.
}
\]

The real function `x(M-x)^r` is increasing up to `M/(r+1)` and decreasing afterwards, so its integer maximum is attained at the adjacent lattice points corresponding to `j=q,q+1`. In the exact-divisibility case `M=(r+1)k`,

\[
T_r((r+1)k-1)=r^r k^{r+1}.
\]

## 7. Anti-diagonal collapse-field geometry

Define

\[
\mathcal R_{r,n}:=\{(d,t)\in\mathbb N_0^2:d\,t^r\le n\}.
\]

Then

\[
\boxed{
N_r(n)\ge m
\iff
\{(d,t):d+t=m+1\}\subseteq\mathcal R_{r,n}.
}
\]

Thus `N_r(n)` is the largest anti-diagonal depth completely swallowed by the anisotropic collapse region `d t^r<=n`.

This geometric interpretation is a candidate Enterprise Math contribution; novelty is not yet certified.

## 8. Exact min–max duality

The anti-diagonal formulation is equivalent to

\[
\boxed{
N_r(n)+1
=\min_{t\ge1}\left(t+\left\lfloor\frac{n}{t^r}\right\rfloor\right).
}
\]

Together with

\[
\boxed{
T_r(m)=\max_{0\le j\le m+1}j(m+1-j)^r,
}
\]

this gives an exact discrete inverse min–max pair.

## 9. Unit-width continuous localization

Let

\[
C_r=\frac{r^r}{(r+1)^{r+1}},
\qquad
X_r(n)=\left(\frac{n}{C_r}\right)^{1/(r+1)}
=(r+1)r^{-r/(r+1)}n^{1/(r+1)}.
\]

Weighted AM–GM gives

\[
T_r(m)\le C_r(m+1)^{r+1},
\]

with equality exactly when `r+1 | m+1`. Conversely the explicit lattice candidate `(q+1)h^r` gives

\[
T_r(m)>C_r m^{r+1}.
\]

Therefore, if `N_r(n)=m`,

\[
\boxed{m<X_r(n)<m+2},
\]

or

\[
\boxed{|N_r(n)+1-X_r(n)|<1.}
\]

So the exact discrete cardinality is globally within one lattice state of the continuous weighted-AM–GM prediction, not merely asymptotic to it.

## 10. Validation and formalization status

Exact integer brute-force validation was run for `r=1..7`, `n=1..1199` (8,393 states), checking the direct quotient-root atlas, inverse-threshold equivalence, extremal formula, and unit-jump consequences, with no counterexample in that range.

This finite validation is not a proof.

The existing P018 branch contains structural lemmas and a written Finset cardinality theorem unit, but those files remain **NOT YET LEAN-VERIFIED**. The duality/min–max theorems here are ordinary mathematics only.

## 11. Next theorem units

1. Formalize `t in atlas <-> Q(t+1)<Q(t)` from `quotient_root_fiber_iff`.
2. Derive a finite powered-floor-set transport theorem with both terminal-zero exceptions explicit: all `r=1`, and `n=1` for `r>=2`.
3. Recast the existing Finset cardinality theorem as formal transport/refinement of known floor-power cardinality, not novelty.
4. Formalize `B_h<=U_h iff r | h+1` and endpoint equality.
5. Only after the discrete theorem layer is stable, consider the real weighted-AM–GM localization theorem.

## 12. Prior-art boundary

Current literature check establishes prior art for the raw exact cardinality. It does **not** establish novelty for the quotient-root jump duality, anti-diagonal interpretation, exact min/max pair, ternary carry normal form, or unit-width localization. Those remain `NOVELTY_UNRESOLVED` until a dedicated source search says otherwise.
