# P018 — Quotient-root / floor-power duality and inverse extremal form

Status: `ORDINARY MATHEMATICS PROVED / PRIOR-ART CORRECTION RECORDED / LEAN NOT YET VERIFIED`

Scope: P018 quotient-root atlas cardinality, ternary carry refinement, inverse precision threshold.

## 1. Canonical objects

For integers `r >= 1`, `n >= 1`, define the positive quotient-root atlas

\[
\mathcal A_{r,n}:=\left\{R_r\!\left(\left\lfloor\frac nd\right\rfloor\right):1\le d\le n\right\},
\qquad N_r(n):=|\mathcal A_{r,n}|.
\]

Also define

\[
Q_{r,n}(t):=\left\lfloor\frac{n}{t^r}\right\rfloor,\qquad t\ge1,
\]

and the extended powered floor set

\[
\widetilde S_r(n):=\{Q_{r,n}(t):t\ge1\}.
\]

The extension to all positive `t` is deliberate: it always includes the terminal value `0`.

## 2. Exact drop duality

For every `t >= 1`, the exact denominator-fiber theorem gives

\[
t\in\mathcal A_{r,n}
\iff
Q_{r,n}(t+1)<Q_{r,n}(t).
\]

Thus quotient-root states are exactly the strict drops of the nonincreasing floor-power sequence `Q_{r,n}`. Consequently

\[
\boxed{N_r(n)+1=|\widetilde S_r(n)|.}
\]

For `r >= 2`, `Q_{r,n}(n)=0`, so the finite set with `1 <= t <= n` already contains zero. For `r=1`, the classical finite floor-quotient set omits zero and has cardinality exactly `N_1(n)`.

This is a structural duality, not merely a numerical coincidence: positive quotient-root fibers are the jump locations of the powered floor-function sequence.

## 3. Prior-art correction

The exact cardinality itself is not a new Enterprise Math theorem.

- Randell Heyman, *Cardinality of a floor function set*, Integers 19 (2019), arXiv:1905.00533, gives the exact `r=1` floor-quotient cardinality.
- Randell Heyman and MD Rahil Miraj, *On Some Floor Function Sets*, arXiv:2309.16072v4 (2024), Theorem 1, gives an exact cardinality formula for

\[
S_t(X)=\left\{\left\lfloor\frac{X}{k^t}\right\rfloor:1\le k\le X\right\},\qquad t>1.
\]

For integer `t=r>=2`, the drop duality identifies their cardinality with `N_r(n)+1`.

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

For nonintegral `a=(rn)^{1/(r+1)}`, one has `H=floor(a)`, and the Heyman–Miraj overlap correction is exactly the same binary carry `kappa` after rewriting their adjacent floor values. When `a` is integral, `H=a-1`; the endpoint/divisibility carry supplies the corresponding boundary correction.

The stronger P018 ternary normalization

\[
N_r(n)+1
=H+\left\lfloor\frac Hr\right\rfloor+\tau,
\qquad \tau\in\{0,1,2\},
\]

therefore remains useful as an arithmetic normal form of the known exact cardinality, not as the first exact count.

## 5. Horizon-cell endpoint theorem

For a fixed horizon value `h >= 1`, put

\[
L_h=\left\lfloor\frac{h^{r+1}}r\right\rfloor+1,
\qquad
U_h=\left\lfloor\frac{(h+1)^{r+1}}r\right\rfloor,
\]

so `H=h` exactly on `L_h <= n <= U_h`. Let `q=floor(h/r)` and

\[
A_h=\max\{q(h+1)^r,(q+1)h^r\},
\qquad
B_h=(q+1)(h+1)^r.
\]

Then

\[
L_h\le A_h\le U_h,\qquad A_h<B_h,
\]

and the second threshold satisfies the sharper endpoint law

\[
\boxed{B_h\le U_h\iff r\mid(h+1).}
\]

Whenever it lies in the cell,

\[
\boxed{B_h=U_h.}
\]

Hence `tau=2` is never a positive-width subinterval of a fixed horizon cell: it is a single terminal state, appearing exactly for `h = -1 mod r`.

Boundary note: `h=0` is exceptional; the displayed `L_h <= A_h` statement is asserted only for `h>=1`.

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

then the residue-split birth formulas collapse to the uniform expression

\[
\boxed{
T_r(m)=\max\{q(h+1)^r,(q+1)h^r\}.
}
\]

Equivalently, setting `M=m+1`,

\[
\boxed{
T_r(m)=\max_{0\le j\le M} j(M-j)^r.
}
\]

Proof of the second form: the real function `x(M-x)^r` is increasing up to `M/(r+1)` and decreasing afterwards, so its integer maximum is attained at the two adjacent lattice points. These are precisely `j=q` and `j=q+1` in the uniform formula. In the exact-divisibility case `M=(r+1)k`, the unique continuous maximizer is integral and gives

\[
T_r((r+1)k-1)=r^r k^{r+1}.
\]

## 7. Anti-diagonal collapse-field geometry

Define the discrete monomial sublevel region

\[
\mathcal R_{r,n}:=\{(d,t)\in\mathbb N_0^2:d\,t^r\le n\}.
\]

The inverse threshold theorem is equivalent to

\[
N_r(n)\ge m
\iff
\{(d,t):d+t=m+1\}\subseteq\mathcal R_{r,n}.
\]

Thus `N_r(n)` is the largest anti-diagonal depth completely swallowed by the anisotropic collapse region `d t^r <= n`.

This is the geometric content behind the threshold formula and is a candidate Enterprise Math contribution/interpretation. Novelty is not yet certified by a complete literature search.

## 8. Exact min–max duality

The anti-diagonal formulation is equivalent to the variational forward formula

\[
\boxed{
N_r(n)+1
=
\min_{t\ge1}\left(t+\left\lfloor\frac{n}{t^r}\right\rfloor\right).
}
\]

Indeed, the anti-diagonal `d+t=M` lies in `d t^r <= n` exactly when

\[
M-t\le \left\lfloor\frac{n}{t^r}\right\rfloor
\]

for every relevant `t`, i.e. exactly when `M` is no larger than the displayed minimum.

The two formulas

\[
N_r(n)+1=\min_t\left(t+\left\lfloor n/t^r\right\rfloor\right),
\qquad
T_r(m)=\max_j j(m+1-j)^r
\]

are exact discrete inverse duals.

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

with equality exactly when `r+1` divides `m+1`. Conversely, with `q=floor(m/(r+1))` and `h=m-q`, the candidate `(q+1)h^r` gives

\[
T_r(m)>C_r m^{r+1}.
\]

Therefore, if `N_r(n)=m`, then

\[
\boxed{m<X_r(n)<m+2},
\]

or equivalently

\[
\boxed{|N_r(n)+1-X_r(n)|<1.}
\]

Hence the exact discrete cardinality is globally one lattice state away from the continuous weighted-AM–GM prediction, not merely asymptotic to it.

## 10. Validation and formalization status

Exact integer brute-force validation was run for `r=1..7`, `n=1..1199` (8,393 states):

- quotient-root atlas cardinality;
- inverse threshold equivalence `N_r(n)>=m iff n>=T_r(m)`;
- extremal formula `T_r(m)=max_j j(m+1-j)^r`;
- unit-jump staircase consequences;

with no counterexample in that range.

This finite validation is not a proof.

The existing P018 Lean branch contains structural lemmas and a written Finset cardinality theorem unit, but those files remain **NOT YET LEAN-VERIFIED**. The new duality/min–max theorems in this note are ordinary mathematics only; do not upgrade their Lean status without kernel evidence.

## 11. Next theorem units

1. Formalize the drop duality `t in atlas <-> Q(t+1)<Q(t)` from `quotient_root_fiber_iff`.
2. Derive a finite powered-floor-set cardinality equivalence; preserve the `r=1` terminal-zero boundary explicitly.
3. Recast the existing Finset atlas cardinality theorem as a formal transport/refinement of known floor-power cardinality, not novelty.
4. Formalize the horizon-cell endpoint law `B_h<=U_h iff r | h+1`, `B_h=U_h` when active.
5. Only after the discrete theorem layer is stable, consider the real weighted-AM–GM localization theorem.

## 12. Prior-art boundary

Current literature check establishes prior art for the raw exact cardinality. It does **not** establish novelty for the quotient-root jump duality, anti-diagonal interpretation, exact min/max pair, ternary carry normal form, or unit-width localization. Those remain `NOVELTY_UNRESOLVED` until a dedicated source search says otherwise.
