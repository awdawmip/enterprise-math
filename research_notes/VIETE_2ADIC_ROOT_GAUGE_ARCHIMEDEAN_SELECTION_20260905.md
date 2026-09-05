# Viète compatible root towers: Z_2^× gauge, Archimedean convergence, and unique monotone principal selection

Status: `FREE_RESEARCH / EXACT PROFINITE-TO-ARCHIMEDEAN SELECTION THEOREM / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent: `#1158`

## 1. Finite phase tower

Let

\[
N_m=6\cdot2^m=3\cdot2^{m+1},
\qquad
\Gamma_m=C_{N_m}.
\]

Use the phase-preserving embedding

\[
\iota_m([k]_{N_m})=[2k]_{N_{m+1}}
\]

and the precision projection

\[
p_m([k]_{N_{m+1}})=[k]_{N_m}.
\]

The original half-turn is `[3] in C6`. An `m`-th compatible dyadic root of that half-turn is a pure 2-primary element of order `2^(m+1)`.

## 2. All compatible primitive root towers are Z_2^×

A pure 2-primary primitive element of `Gamma_m` has the form

\[
v_m=[3a_m]_{N_m},
\]

where

\[
a_m\in(\mathbf Z/2^{m+1}\mathbf Z)^\times
\]

is odd.

Root compatibility is

\[
2v_{m+1}=\iota_m(v_m).
\]

Since `iota_m(v_m)=[2v_m]`, this is equivalent to

\[
v_{m+1}\equiv v_m\pmod{N_m},
\]

hence

\[
a_{m+1}\equiv a_m\pmod{2^{m+1}}.
\]

Therefore the compatible sequence `(a_m)` is exactly one 2-adic unit

\[
\alpha\in\mathbf Z_2^\times.
\]

Conversely every `alpha in Z_2^×` defines such a compatible primitive root tower.

Thus

\[
\boxed{
\{\text{compatible primitive dyadic half-turn root towers}\}
\cong\mathbf Z_2^\times.
}
\]

This is the state-side version of the previously observed primitive-character gauge.

## 3. Same precision address, square root after phase embedding

For every compatible tower,

\[
\boxed{p_m(v_{m+1})=v_m}
\]

and simultaneously

\[
\boxed{2v_{m+1}=\iota_m(v_m)}.
\]

Thus a finer root state has two exact meanings:

1. under precision collapse, it is the same projective address;
2. under phase-preserving embedding, it is a square root of the coarse phase.

For the principal tower `alpha=1`,

\[
v_m=[3]_{N_m}
\]

at every level. The residue is constant while the phase denominator doubles.

This is why the native/profinite address need not move toward zero even though its normalized Archimedean phase readout does.

## 4. Least-residue phase distance

Let `r_m` be the least-absolute integer representative of

\[
\alpha\pmod{2^{m+1}},
\]

chosen with

\[
|r_m|\le2^m.
\]

Since `v_m=3a_m`, its normalized Cayley distance to identity is

\[
\delta_m
:=\frac{d_{N_m}(v_m,0)}{N_m}
=\boxed{\frac{|r_m|}{2^{m+1}}}.
\]

Compatibility of the least representatives implies

\[
r_{m+1}=r_m
\quad\text{or}\quad
r_{m+1}=r_m\pm2^{m+1}.
\]

Call the second case a **2-adic high-bit jump**.

If a jump occurs, then

\[
|r_{m+1}|
\ge2^{m+1}-|r_m|
\ge2^m,
\]

so

\[
\boxed{\delta_{m+1}\ge\frac14.}
\]

Thus every newly activated high 2-adic bit creates a macroscopic Archimedean phase excursion.

## 5. Exact criterion for Archimedean approach to identity

Suppose

\[
\delta_m\to0.
\]

Then high-bit jumps can occur only finitely many times, because every jump gives a later distance at least `1/4`.

Hence for all sufficiently large `m`,

\[
r_{m+1}=r_m.
\]

The least representatives therefore stabilize to one fixed odd integer `q`, and

\[
\alpha=q
\]

inside `Z_2`.

Conversely, if `alpha=q` is an ordinary odd integer embedded in `Z_2`, then for sufficiently large `m` the least representative is constantly `q`, so

\[
\delta_m=\frac{|q|}{2^{m+1}}\to0.
\]

Therefore

\[
\boxed{
\delta_m\to0
\iff
\alpha\in\mathbf Z\cap\mathbf Z_2^\times
\iff
\alpha\text{ is an ordinary odd integer.}
}
\]

So a generic 2-adic compatible root tower has no Archimedean near-identity limit. The profinite completion is strictly richer than the continuous phase completion.

## 6. Noninteger 2-adic gauges necessarily have recurrent macroscopic excursions

If

\[
\alpha\in\mathbf Z_2^\times\setminus\mathbf Z,
\]

then the least representatives cannot stabilize. Hence there are infinitely many high-bit jumps, and therefore infinitely many levels with

\[
\boxed{\delta_m\ge\frac14.}
\]

This is a precise sense in which non-Archimedean refinement can keep producing phase oscillation/excursion rather than convergence to identity.

No statement about physical oscillation is made; this is a theorem about the normalized Archimedean readout of a profinite root gauge.

## 7. Strict refinement monotonicity selects only ±1

At the first physical quarter-turn layer `m=1`, every primitive tower has

\[
\delta_1=\frac14.
\]

Assume from this layer onward that every refinement strictly improves normalized phase resolution:

\[
\delta_{m+1}<\delta_m
\qquad(m\ge1).
\]

If any high-bit jump occurred, then at the first such jump

\[
\delta_{m+1}\ge\frac14,
\]

while prior strict decrease gives

\[
\delta_m\le\frac14,
\]

contradiction.

Therefore no jump ever occurs. The least representative remains

\[
r_m=1
\]

or

\[
r_m=-1
\]

for every level. Hence

\[
\boxed{
\text{STRICT ALL-LEVEL PHASE REFINEMENT}
\Longrightarrow
\alpha=\pm1.
}
\]

Conversely `alpha=±1` gives

\[
\delta_m=2^{-(m+1)}
\]

and exact halving at every level.

Thus

\[
\boxed{
\alpha=\pm1
\iff
\delta_{m+1}=\frac12\delta_m\text{ for every }m\ge1.
}
\]

## 8. Chirality fixes the remaining sign

The two all-level shortest towers are inverses:

\[
\alpha=1,
\qquad
\alpha=-1.
\]

The physical C12 gate pair realizes the quarter-turn chirality torsor. Choosing the forward sweep fixes the positive branch and therefore

\[
\boxed{\alpha=1.}
\]

This is exactly the principal Viète tower

\[
\boxed{v_m=[3]_{6\cdot2^m}.}
\]

Reflection/sweep reversal gives the inverse tower `alpha=-1`.

## 9. Interpretation

The selection hierarchy is now exact:

```text
all algebraically compatible root towers
    = Z_2^×

Archimedean near-identity compatible towers
    = ordinary odd integers inside Z_2^×

strictly improving / exact-halving towers
    = {+1,-1}

chosen sweep chirality
    = +1 principal Viète tower
```

Therefore the principal tower is not an arbitrary branch convention. It is the unique chirality-selected compatible tower in which **every added binary precision level actually improves the normalized Archimedean phase instead of introducing a new high-bit excursion**.

## 10. BRC observer meaning

The profinite address `alpha` is information that is erased by a fixed finite phase observer. Two towers can agree through level `m` and differ at a higher 2-adic bit.

The future operation "refine and measure normalized phase distance" is not safe under that finite quotient unless the unresolved higher-bit fiber is retained or a selection theorem such as the all-level monotonicity criterion is imposed.

This is an observer/provenance-loss application; no positive weighted branching is needed.

## 11. Consequence for #1158

The root-choice problem can now be stated globally rather than recursively:

\[
\boxed{
\text{PRINCIPAL VIETE ROOT NORMALIZATION}
=
\text{THE UNIQUE FORWARD-CHIRALITY }\alpha\in Z_2^\times
\text{ WITH STRICT ALL-LEVEL PHASE REFINEMENT.}
}
\]

What remains native is not the algebraic uniqueness of the tower. It is only the semantic status of the higher precision levels beyond the physically realized Cell/gate and balanced-spinor layers.
