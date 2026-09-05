# Viète native spinor saturation: the distinguished C24 root is native, C48+ are not rational component spinors

Status: `FREE_RESEARCH / EXACT ALGEBRAIC SATURATION THEOREM / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent: `#1158`
Uses merged `#1170` segment-spinor identity and the canonical integer component algebra `A_E=Z[J]/(J^2+1)`.

## 1. Root tower and indexing

Let

\[
U_0=-1,
\qquad U_1=J,
\qquad U_{m+1}=\beta(U_m),
\]

with

\[
\beta(U)=\frac{1+U}{\sqrt{2+U+U^{-1}}}
\]

on the forward branch. Then

\[
U_{m+1}^2=U_m,
\qquad
\operatorname{ord}(U_m)=2^{m+1}.
\]

In the finite phase tower this corresponds to

\[
U_m\in C_{6\cdot2^m}
\]

at the distinguished residue-three state:

- `U_0`: C6 half-turn/reversal;
- `U_1`: C12 quarter-turn gate character;
- `U_2`: C24 eighth-turn distinguished root;
- `U_3`: C48 sixteenth-turn distinguished root;
- etc.

## 2. Native component spinor map

For a nonzero native integer component pair `(a,b)`, define

\[
S[a:b]=\frac{a+bJ}{\sqrt{a^2+b^2}}
\]

and its projective character

\[
\mathcal C[a:b]=S[a:b]^2
=\frac{(a^2-b^2)+2abJ}{a^2+b^2}.
\]

The merged #1170 theorem proves

\[
\beta(\mathcal C[a:b])=S[a:b]
\]

for the forward sector `a>0`.

## 3. The C24 distinguished root is exactly the balanced native spinor

For the balanced component pair `(1,1)`,

\[
\mathcal C[1:1]=J=U_1.
\]

Therefore

\[
S[1:1]
=\beta(J)
=U_2.
\]

Explicitly,

\[
\boxed{
U_2=\frac{1+J}{\sqrt2}=S[1:1].
}
\]

Hence the distinguished order-eight root used by the Viète tower has an exact native component-segment realization even though the **full C24 phase carrier** is not realized by the twelve one-step Cell/gate objects.

This separates two notions:

\[
\text{one distinguished root has a native spinor representative}
\]

from

\[
\text{the complete cyclic phase shell is physically realized}.
\]

The former holds at C24; the latter does not follow.

## 4. Quadratic-field obstruction to any deeper rational component spinor

Assume a rational projective component pair `(a,b)` with `a,b in Q`, not both zero, satisfies

\[
S[a:b]=U_m.
\]

Squaring gives

\[
\mathcal C[a:b]=U_{m-1}.
\]

But

\[
\mathcal C[a:b]
=\frac{a^2-b^2}{a^2+b^2}
+\frac{2ab}{a^2+b^2}J
\in\mathbf Q(J).
\]

The field `Q(J)` with `J^2=-1` is quadratic over `Q`. Its roots of unity are exactly

\[
\{\pm1,\pm J\},
\]

so every torsion element has order dividing four.

For `m>=3`, however,

\[
\operatorname{ord}(U_{m-1})=2^m\ge8.
\]

Therefore `U_(m-1)` cannot lie in `Q(J)`. Contradiction.

Thus

\[
\boxed{
 m\ge3
 \Longrightarrow
 U_m\text{ IS NOT }S[a:b]\text{ FOR ANY RATIONAL, HENCE ANY INTEGER, COMPONENT PAIR }(a,b).
}
\]

In particular:

\[
\boxed{
U_3\in C_{48}\text{ HAS NO EXACT INTEGER-COMPONENT SPINOR REPRESENTATIVE.}
}
\]

This is a pi-free cyclotomic-degree obstruction.

## 5. Sharpness

The obstruction is sharp at the previous level:

- `U_1=J` is the character `C[1:1]`;
- `U_2=S[1:1]` is the normalized balanced native segment itself;
- `U_3` and every deeper `U_m` fail the rational-component spinor test.

So the current two-component native algebra has exact dyadic depth

\[
\boxed{
\text{CHARACTER DEPTH THROUGH C12, SPINOR DEPTH THROUGH DISTINGUISHED C24, NO RATIONAL-COMPONENT DEPTH AT C48+.}
}
\]

## 6. Relation to the Cell/gate saturation theorem

The merged Cell/gate theorem says the full one-step local incidence set has exactly twelve typed states and therefore cannot faithfully realize the complete C24 cycle.

The present result does not contradict that theorem. It refines it:

1. full spatial Cell/gate cycle realization saturates at C12;
2. one special C24 phase has an independent native component-spinor representative;
3. no analogous rational/integer component-spinor representative exists at C48 or deeper.

Thus the first undeniably non-spatial/history-only distinguished Viète root occurs at C48, not C24.

## 7. BRC/path-multiplicity boundary

The canonical path-valued square-root operator can attach large multipath fibers to a fixed integer component pair, and BRC may retain Boolean support, multiplicity, positive weights or richer provenance downstream.

None of those positive branch summaries changes the underlying deduplicated component ratio `(a:b)`. Therefore they do not evade the quadratic-field obstruction above.

In particular, path multiplicity cannot be silently reinterpreted as a signed/complex amplitude that manufactures the missing C48 phase. Such an amplitude bridge would be a new typed theorem.

BRC resolution:

`REUSE_APPLIED = COMPONENT/PROVENANCE SEPARATION + SIGNED/PHASE BOUNDARY`.

## 8. Updated smallest unresolved spatial/process bridge

The Viète distinguished-root chain now has the following exact provenance:

```text
C6  : endpoint reversal on ordered-neighbor shell
C12 : actual pivot gate + quarter-turn character J
C24 : normalized balanced native component spinor (1,1)/sqrt(2)
C48+: no rational/integer two-component spinor realization
```

Therefore any G0/native-process continuation beyond C24 must use at least one genuinely new carrier:

- higher transition/history state;
- a richer multi-axis/native 6D realization;
- an explicitly proved amplitude/interference carrier;
- or another structure not reducible to a rational two-component native segment.

No such promotion is made here.
