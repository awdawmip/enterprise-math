# Reflection orientation channels collapse modulo two

Status: `FREE_RESEARCH / EXACT MOD-2 FINITE-ALGEBRA THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- odd-denominator primitive orientation factors;
- dyadic orientation folding;
- same-denominator orientation resultant law.

## 1. Two characteristic-zero orientation factors

For odd `d>1`, let

\[
h=\varphi(d)/2
\]

and split

\[
\Psi_d=\Psi_d^E\Psi_d^O.
\]

The two monic integral factors carry the even and odd reflection-orientation primitive modes respectively.

They are distinct over characteristic zero and exchanged by `u -> 4-u`.

## 2. Dyadic folding identity

The exact orientation folding theorem gives

\[
\boxed{
(-1)^h\Psi_d^E(R_2(u))
=\Psi_d^E(u)\Psi_d^O(u).
}
\tag{OM2-1}

The phase polynomial is

\[
R_2(u)=u(4-u).
\]

Modulo two,

\[
\boxed{R_2(u)\equiv u^2\pmod2.}
\tag{OM2-2}

## 3. Frobenius forces the two orientations to coincide mod 2

Reduce (OM2-1) in `F_2[u]`.  The sign disappears and Frobenius gives

\[
\Psi_d^E(R_2(u))
\equiv
\Psi_d^E(u^2)
=
\Psi_d^E(u)^2.
\]

Hence

\[
\Psi_d^E(u)^2
=
\Psi_d^E(u)\Psi_d^O(u)
\]

in the polynomial domain `F_2[u]`.

Cancel the nonzero factor `Psi_d^E`:

\[
\boxed{
\Psi_d^E(u)
\equiv
\Psi_d^O(u)\pmod2.
}
\tag{OM2-3}

Thus the two characteristic-zero reflection channels have exactly the same reduced polynomial support in characteristic two.

## 4. Orientation resultant is the determinant shadow of mod-2 collision

The previously derived same-denominator coupling is

\[
\boxed{
|\operatorname{Res}(\Psi_d^E,\Psi_d^O)|
=2^h.
}
\tag{OM2-4}

Equation (OM2-3) supplies the local algebraic reason: the two factors become identical modulo the unique prime two, and no odd prime is needed for their support collision.

## 5. Element-level unit/two dichotomy

Let

\[
A_d^E:=\mathbb Z[u]/(\Psi_d^E).
\]

From (OM2-3),

\[
\Psi_d^O(u)=\Psi_d^E(u)H(u)+2G(u)
\]

for integral polynomials `G,H`.  Therefore in `A_d^E`,

\[
\boxed{
\Psi_d^O(\bar u)=2\varepsilon
}
\tag{OM2-5}

for some `epsilon in A_d^E`.

The lattice rank is

\[
\operatorname{rank}_{\mathbb Z}A_d^E=h.
\]

The determinant of multiplication by `Psi_d^O(ubar)` is the resultant magnitude `2^h`.  Hence

\[
2^h|\det(m_\varepsilon)|=2^h,
\]

so

\[
|\det(m_\varepsilon)|=1.
\]

Thus `epsilon` is a unit and

\[
\boxed{
\Psi_d^O(\bar u)\sim2
\quad\text{in }A_d^E.
}
\tag{OM2-6}

By symmetry the same statement holds with `E,O` reversed.

## 6. Exact quotient module

Since multiplication by the unit `epsilon` is an integral automorphism,

\[
\Psi_d^O(\bar u)A_d^E=2A_d^E.
\]

Therefore

\[
\boxed{
A_d^E/\Psi_d^O(\bar u)A_d^E
\cong
(\mathbb Z/2\mathbb Z)^h
=
(\mathbb Z/2\mathbb Z)^{\varphi(d)/2}.
}
\tag{OM2-7}

The orientation coupling is one flat layer of two-torsion in every orientation-resolved primitive coordinate.

## 7. Same mechanism as p-adic level coupling

The prime-ray theorem found

\[
\Psi_{mp^a}(\bar u)\sim p
\]

inside the primitive order `A_m`, because distinct p-adic levels collapse modulo `p`.

The present theorem is exactly the orientation analogue:

\[
\Psi_d^O(\bar u)\sim2
\]

inside the `E` orientation order, because the two orientation supports collapse modulo two.

Thus

```text
p-adic level distinction
 -> mod-p Frobenius collapse
 -> one p-torsion layer

reflection orientation distinction
 -> mod-2 Frobenius collapse
 -> one 2-torsion layer
```

Both are instances of the same finite integral-algebra mechanism.

## 8. Typing consequence

Over characteristic zero, `E` and `O` are genuinely distinct primitive channels and carry different endpoint and odd-phase trace data.

Reduction modulo two intentionally recoalesces them.  Therefore the mod-two support cannot be used as evidence that the original orientations were the same carrier.

Freeze:

`E_ORIENTATION != O_ORIENTATION IN CHARACTERISTIC_ZERO`.

`E_ORIENTATION MOD 2 = O_ORIENTATION MOD 2`.

`ORIENTATION_RESULTANT_2_POWER = MOD_2_SUPPORT_COLLISION_SHADOW`.
