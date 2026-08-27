# P018 — Ferrers–Minkowski pixel duality and resolution-horizon calculus

Status: `ORDINARY MATHEMATICS PROVED / PRIOR-ART BOUNDARY PARTIALLY IDENTIFIED / LEAN NOT YET VERIFIED`

Scope: P018 quotient-root atlas, powered-floor profile, exact cardinality transport, precision interpretation, and safe-language limit geometry.

## 1. Precision grid model

Fix an integer root order `r>=1`. Define the compact reciprocal-power sequence

\[
E_r:=\{0\}\cup\{t^{-r}:t\ge1\}\subset[0,1].
\]

For an integer grid resolution `n>=1`, define the occupied grid labels

\[
\Gamma_n(E):=\{\lfloor n x\rfloor:x\in E\}.
\]

Then

\[
\Gamma_n(E_r)
=\{0\}\cup\left\{\left\lfloor\frac{n}{t^r}\right\rfloor:t\ge1\right\}.
\]

If

\[
G_{r,n}(t):=\left\lfloor\frac{n}{t^r}\right\rfloor,
\]

and

\[
\mathcal A_{r,n}:=
\left\{R_r\!\left(\left\lfloor\frac nd\right\rfloor\right):1\le d\le n\right\},
\qquad N_r(n):=|\mathcal A_{r,n}|,
\]

then the exact drop duality gives

\[
t\in\mathcal A_{r,n}
\iff G_{r,n}(t)>G_{r,n}(t+1).
\]

Hence

\[
\boxed{N_r(n)+1=|\Gamma_n(E_r)|.}
\]

Thus the P018 state count is literally the number of uniform `1/n` precision cells occupied by the countable reciprocal-power set `E_r`.

The fiber multiplicity has the exact pixel meaning

\[
\boxed{
\#\{d:R_r(\lfloor n/d\rfloor)=t\}
=G_{r,n}(t)-G_{r,n}(t+1).
}
\]

It is the number of grid levels crossed by the gap from `(t+1)^(-r)` to `t^(-r)`.

## 2. Exact reciprocal pixel duality at perfect-power precision

For every integer `m>=1`, put `n=m^r`. For every `d>=1`,

\[
\boxed{
R_r\!\left(\left\lfloor\frac{m^r}{d}\right\rfloor\right)
=\left\lfloor m d^{-1/r}\right\rfloor.
}
\]

Therefore, with

\[
E_{1/r}:=\{0\}\cup\{d^{-1/r}:d\ge1\},
\]

we have the exact set identity

\[
\boxed{
\Gamma_m(E_{1/r})
=\{0\}\cup\mathcal A_{r,m^r}.
}
\]

Combining with the primal grid identity,

\[
\boxed{
|\Gamma_{m^r}(E_r)|
=|\Gamma_m(E_{1/r})|
=N_r(m^r)+1.
}
\]

So one finite quotient-root atlas is simultaneously:

1. the `1/m^r` pixel count of the power sequence `E_r`;
2. the `1/m` pixel count of the reciprocal-exponent sequence `E_{1/r}`.

This is the finite-precision form of the Ferrers transpose: row lengths are `G_{r,n}(t)` and conjugate column heights are the quotient-root profile.

## 3. Resolution horizon as a pixel phase transition

Let

\[
H:=R_{r+1}(rn-1),
\qquad
D:=G_{r,n}(H+1)=\left\lfloor\frac{n}{(H+1)^r}\right\rfloor.
\]

Then the powered-floor gaps have two regimes.

### Dense-resolved head

For every `1<=t<H`,

\[
\boxed{G_{r,n}(t)>G_{r,n}(t+1).}
\]

Thus every consecutive reciprocal-power gap before `H` is resolved by the `1/n` grid.

### Unit-drop tail

For every `t>=H+1`,

\[
\boxed{
0\le G_{r,n}(t)-G_{r,n}(t+1)\le1.
}
\]

Proof: if the difference were at least `2`, the exact denominator fiber for root state `t` would contain two consecutive positive denominators. The state-specific collision-gap theorem would then force

\[
t^{r+1}<rn.
\]

But `t>=H+1` and the defining upper inequality for `H` give

\[
t^{r+1}\ge(H+1)^{r+1}\ge rn,
\]

contradiction.

Therefore `H` is the exact dense-to-sparse resolution crossover:

- below it every adjacent point is separated;
- beyond it one adjacent gap can cross at most one grid level.

## 4. Drop-mass conservation gives a shorter exact count proof

In the tail `t>=H+1`, every strict drop has size exactly `1`. Since

\[
G_{r,n}(H+1)=D,
\qquad
G_{r,n}(t)\to0,
\]

telescoping gives total tail drop mass `D`. Hence the number of tail strict-drop indices is exactly

\[
\boxed{D.}
\]

The head contributes exactly `H-1` strict drops. At the interface `t=H`, define

\[
\kappa:=\mathbf1[G_{r,n}(H)>G_{r,n}(H+1)].
\]

Equivalently, using the existing horizon threshold,

\[
\kappa
=\mathbf1[(D+1)H^r\le n].
\]

Therefore

\[
N_r(n)=(H-1)+\kappa+D,
\]

so

\[
\boxed{N_r(n)+1=D+H+\kappa.}
\]

This yields a shorter formalization route than separately proving and counting high and low image Finsets: count strict drops of one monotone integer profile, using dense-head strictness, unit-tail drop mass, and one interface bit.

## 5. Ternary carry is a pixel balance correction

Let

\[
q:=\left\lfloor\frac Hr\right\rfloor.
\]

At the continuous optimum for the head-tail box count

\[
t+\frac{n}{t^r},
\]

the derivative equation gives

\[
\frac{n}{t^r}=\frac tr.
\]

Thus `q` is the quantized tangent prediction for the tail height when the split is near `H`.

The existing three-point band says

\[
D\in\{q-1,q,q+1\}.
\]

Since both exact count forms hold,

\[
N_r(n)+1=H+D+\kappa=H+q+\tau,
\]

we get the exact interpretation

\[
\boxed{\tau=(D-q)+\kappa.}
\]

The forced-carry lemmas exactly prevent this expression from leaving `{0,1,2}`.

Thus the ternary carry is not a mysterious third state. It is the sum of:

1. the integer tail-height error `D-q` relative to continuous balance;
2. the one-bit head-tail overlap correction `kappa`.

## 6. Global one-cell grid discrepancy

Put

\[
A_r:=(r+1)r^{-r/(r+1)}.
\]

The previously proved inverse-AM–GM localization becomes the grid-count statement

\[
\boxed{
\left|
|\Gamma_n(E_r)|-A_r n^{1/(r+1)}
\right|<1
\qquad(n\ge1).
}
\]

For the reciprocal sequence, taking `n=m^r` in the exact pixel duality gives

\[
\boxed{
\left|
|\Gamma_m(E_{1/r})|-A_r m^{r/(r+1)}
\right|<1
\qquad(m\ge1).
}
\]

So the same coefficient `A_r` controls both reciprocal grid spectra, with a global discrepancy of less than one occupied cell.

## 7. Ferrers–Minkowski exponent duality

Uniform lattice-box counting is an equivalent definition of box dimension. The reciprocal power sequences therefore have

\[
\boxed{
\dim_B(E_r)=\frac1{r+1},
\qquad
\dim_B(E_{1/r})=\frac r{r+1},
}
\]

and hence

\[
\boxed{
\dim_B(E_r)+\dim_B(E_{1/r})=1.
}
\]

The grid-content coefficient is self-dual:

\[
\boxed{A_r=(r+1)r^{-r/(r+1)}}.
\]

The first dimension is the finite-precision growth exponent of powered-floor occupied cells. The second is the finite-resolution complexity exponent of the conjugate quotient-root frontier.

Generic box-dimension formulas for decreasing power-law sequences are prior art. The Enterprise Math content here is the exact P018/Ferrers transport, the matching finite pixel counts, and the operational interpretation; novelty remains unresolved.

## 8. Operational-core limit spectrum

For fixed `r>=2`, let

\[
\alpha_r:=1-2^{-1/r},
\qquad
D_r:=\left\lfloor\alpha_r^{-r}\right\rfloor.
\]

The exact atom-core stabilization theorem gives, eventually,

\[
B_{r,n}\setminus K(B_{r,n})
=\{b_2(n),\ldots,b_{D_r}(n)\}.
\]

The limiting normalized operational spectrum is therefore

\[
\boxed{
E_r^{\mathrm{op}}
:=\{0,1\}\cup\{d^{-1/r}:d\ge D_r+1\}.
}
\]

Equivalently, because `alpha_r^(-r)` is nonintegral,

\[
E_r^{\mathrm{op}}
=\{0,1\}\cup\big(E_{1/r}\cap(0,\alpha_r)\big).
\]

Only finitely many reciprocal-power teeth are removed, so

\[
\boxed{\dim_B(E_r^{\mathrm{op}})=\frac r{r+1}.}
\]

Its reflected safe-shift limit spectrum

\[
\Sigma_r^{\mathrm{safe}}
:=\{0,1\}\cup\{1-d^{-1/r}:d\ge D_r+1\}
\]

has the same box dimension.

Thus the safe-operation world is countable (Hausdorff dimension zero) but has positive finite-resolution box complexity `r/(r+1)`.

## 9. Exact self-pixelization along perfect powers

At `n=m^r`,

\[
b_d(m^r)=\lfloor m d^{-1/r}\rfloor.
\]

Once atom-core stabilization has occurred and the finitely removed top teeth occupy distinct grid cells, we get

\[
\boxed{
K(B_{r,m^r})
=\Gamma_m(E_r^{\mathrm{op}})\setminus\{0\}.
}
\]

Therefore the finite operational core is exactly the positive `1/m` pixelization of its own limiting operational spectrum.

Consequently, eventually,

\[
|\Gamma_m(E_r^{\mathrm{op}})|
=|\Gamma_m(E_{1/r})|-J_r,
\]

where

\[
J_r=D_r-1.
\]

Together with the global reciprocal grid discrepancy,

\[
\boxed{
\left|
|\Gamma_m(E_r^{\mathrm{op}})|
-\big(A_r m^{r/(r+1)}-J_r\big)
\right|<1
}
\]

for all sufficiently large `m`.

## 10. Formalization route

The shortest Lean path now appears to be:

1. kernel-check the existing drop-duality theorem;
2. prove a local theorem `tail_drop_le_one` from the exact fiber theorem plus the existing state-collision gap;
3. express the atlas as a finite strict-drop Finset of `G(t)=n/t^r`;
4. count the head drops directly;
5. count tail drops by telescoping, because every tail drop is `0` or `1`;
6. recover `root_state_atlas_card_binary` through drop-mass conservation;
7. obtain the ternary formula from `tau=D-q+kappa` and the existing three-point band;
8. defer real-number/box-dimension formalization until the integer pixel theorem is kernel-checked.

This route can potentially replace the current long image-union cardinality WIP with a shorter monotone-profile proof.

## 11. Prior-art boundary

Prior art already includes:

- exact cardinalities of the relevant floor-function sets (Heyman; Heyman–Miraj);
- standard box-counting theory and the box dimension of decreasing power-law sequences.

A targeted search at this checkpoint did not locate a source explicitly packaging the P018 quotient-root/Ferrers transpose as the exact reciprocal pixel identity above, nor the combined interpretation of the horizon, carry, reciprocal dimensions, and operational-core limit spectrum. This is not a novelty proof. Keep the package at `NOVELTY_UNRESOLVED` pending dedicated review.
