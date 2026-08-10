# P022 — Explicit Target-Family Counterexample to Support Avoidance and Flux Balance

Status: `COUNTEREXAMPLE / NEGATIVE BOUNDARY / EXACT INTEGER CERTIFICATE`  
Owner: `program/p022-geometry-v2`  
Affected claims: global support-avoidance; global zero transfer-correction; fixed `+1` half-index marker valuation  
Unaffected target: nonzero marker valuation / multiplicative independence

## 1. The explicit prime

Take

\[
\boxed{p=369581.}
\]

It is prime and

\[
p\equiv5\pmod{24}.
\]

Thus with

\[
m=(p-1)/2=184790,
\]

we are inside the forced-midpoint composite-boundary family:

\[
p\mid F_m,
\qquad
2m-1=p-2\text{ is composite}.
\]

No claim is made that this is the least counterexample by size.

## 2. A very small earlier Franel zero

The eighth Franel number is exactly

\[
\boxed{F_8=739162=2p.}
\]

Therefore

\[
v_p(F_8)=1.
\]

This zero is not an accidental point outside the canonical elimination.  The exact central-binomial relation for `A_m` has

\[
\boxed{\alpha_8=2.}
\]

The complete nonzero relation support is sparse; among the checked support indices below `m-1`, the only Franel p-zero is `j=8`.  The terminal support point `m-1` is also a p-unit because `F_m=0` and adjacent Franel zeros are impossible.

Hence the canonical support really does meet the Franel zero set.

This disproves the global statement

\[
\operatorname{supp}(\alpha_m)\cap Z_p=\varnothing
\]

for every prime in the target residue family.

## 3. The transfer correction is nonzero

In prime-halving flux coordinates,

\[
\Phi_p(m)=-2,
\qquad
\Phi_p(p-2)=0.
\]

Therefore

\[
\boxed{\Phi_p(m)-\Phi_p(p-2)=-2.}
\]

So global flux balance is also false.

The local reason is visible in the prime-halving DAG: the zero boundary at `j=8` is crossed with multiplicity two on the `m` side.

## 4. The midpoint is nevertheless a simple zero

Using the exact Franel recurrence modulo `p^2`,

\[
\frac{F_m}{p}\equiv153310\not\equiv0\pmod p.
\]

Hence

\[
\boxed{v_p(F_m)=1.}
\]

The pure defect valuation is therefore

\[
\begin{aligned}
v_p(D_m)
&=v_p(F_m)+\Phi_p(m)-\Phi_p(p-2)\\
&=1-2\\
&=\boxed{-1}.
\end{aligned}
\]

Thus the empirical rule `v_p(D_m)=+1` is false even inside `p=5,23 (mod 24)`.

## 5. Why this does not damage the identifiability route

A valuation row does not need to be positive.  For multiplicative independence, a marker prime is useful whenever its valuation on the new defect direction is **nonzero** after earlier directions are controlled.

Here

\[
\boxed{v_p(D_m)=-1\ne0.}
\]

So the counterexample kills an overstrong normalization claim while preserving the actual algebraic resource needed by the low-order collision-identifiability strategy.

The research target must therefore be weakened from

\[
v_p(D_m)=1
\]

or

\[
\Phi_p(m)=\Phi_p(p-2)
\]

to the exact necessary condition

\[
\boxed{v_p(D_m)\ne0.}
\]

## 6. Methodological consequence

This example vindicates the signed-flux formulation developed immediately before it:

- set-disjointness was too strong;
- zero flux was still too strong;
- even the sign of a useful marker is not invariant.

What survives is the weaker distinction between **vanishing** and **nonvanishing** defect valuation.

This is a reusable negative boundary for P011/P018/P023 consumers: future-safe arithmetic diagnostics must preserve the signed defect coordinate, not replace it by a binary “support collision happened” flag.

## 7. Executable assets

- `src/enterprise_math/p022_barlow_half_defect_counterexample.py`
- `tests/test_p022_barlow_half_defect_counterexample.py`

The executable certificate checks primality/residue membership through the existing target-family validator, the exact identity `F_8=2p`, the canonical relation exponent `alpha_8=2`, uniqueness of the checked low-support zero, the midpoint quotient modulo `p`, the flux correction `-2`, and the final defect valuation `-1`.
