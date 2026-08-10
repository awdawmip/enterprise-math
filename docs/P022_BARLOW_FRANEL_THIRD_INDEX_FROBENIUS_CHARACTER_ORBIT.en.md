# P022 — Frobenius character orbit of the Franel one-third gamma triple

Status: `PROVED_WIP / EXACT CHARACTER-ORBIT DECOMPOSITION`  
Owner: `P022 / program/p022-geometry-v2`  
Depends on: `P022_BARLOW_FRANEL_THIRD_INDEX_GAMMA_TRIPLE.en.md`  
Scope: isolate the exact mu_6 character block carrying the target datum at inert primes

## 1. Starting gamma triple

Use the explicit `N=6` representation

\[
\gamma=(-1,-1,-1,1,1,1,-2,1,1),
\]

\[
\delta=(5,2,2,-6,-6,-6,0,0,3).
\]

For a character label

\[
j\in\mathbb Z/6\mathbb Z,
\]

replace `delta` by `j delta` and reduce the resulting numerator/denominator
root multisets by exact cancellation.  This is precisely the twist operation
appearing in the cyclotomic gamma-triple point-count decomposition.

## 2. P022-TC01 — exact six-character parameter table

The six reduced hypergeometric data are

\[
\begin{array}{c|c|c|c}
 j & \alpha^{(j)} & \beta^{(j)} & \text{rank}\\\hline
0 & (1/2) & (1) & 1\\
1 & (1/3,1/3,5/6) & (1,1,1) & 3\\
2 & (1/2,2/3,2/3,2/3) & (1,1,1,1) & 4\\
3 & (1/2) & (1) & 1\\
4 & (1/3,1/3,1/3,1/2) & (1,1,1,1) & 4\\
5 & (1/6,2/3,2/3) & (1,1,1) & 3.
\end{array}
\]

Thus the original Franel one-third datum is exactly the `j=1` character:

\[
\boxed{
\alpha^{(1)}=
\left(\frac56,\frac13,\frac13\right),
\qquad
\beta^{(1)}=1^3,
}
\]

while its Galois/Dwork conjugate is exactly `j=5`:

\[
\boxed{
\alpha^{(5)}=
\left(\frac16,\frac23,\frac23\right),
\qquad
\beta^{(5)}=1^3.
}
\]

The other four characters are not copies of the target block.  Two collapse
to rank one and the pair `j=2,4` has rank four.

## 3. P022-TC02 — Frobenius acts on characters by multiplication by p

For a prime `p` coprime to six, arithmetic Frobenius acts on sixth roots of
unity by

\[
\zeta_6\longmapsto\zeta_6^p.
\]

Hence the character labels are permuted by

\[
\boxed{j\longmapsto pj\pmod6.}
\]

For the one-third prime class

\[
p\equiv5\equiv-1\pmod6,
\]

this becomes reflection

\[
j\longmapsto-j\pmod6.
\]

Therefore the exact Frobenius character orbits are

\[
\boxed{
\{0\},\qquad
\{3\},\qquad
\{1,5\},\qquad
\{2,4\}.
}
\]

In contrast, at split primes `p=1 mod 6` all six characters are individually
fixed.

## 4. P022-TC03 — the target rank-six closure is the {1,5} orbit

The `j=1` and `j=5` blocks have ranks three and three.  Their combined
numerator parameters are

\[
\left(
\frac16,\frac56,
\frac13,\frac13,
\frac23,\frac23
\right),
\]

with denominator `1^6`.  This is exactly the rational Galois closure already
identified from cyclotomic polynomials.

Hence

\[
\boxed{
\text{rank-six rational closure}
=
\text{the Frobenius orbit of the }j=1\text{ target character}
}
\]

at every inert prime `p=5 mod 6`.

This is stronger than merely observing that the target datum has a Galois
conjugate: the two blocks are singled out by the actual character decomposition
of the explicit sixfold gamma-triple cover.

## 5. Relation to the Dwork dash cycle

The Dwork parameter cycle at the same primes is

\[
\left(\frac56,\frac13,\frac13\right)
\xleftrightarrow{*}
\left(\frac16,\frac23,\frac23\right).
\]

The character decomposition now identifies this as

\[
\boxed{j=1\xleftrightarrow{\mathrm{Frob}_p}j=5.}
\]

Thus three independently derived descriptions coincide exactly:

1. Galois conjugation in `Q(zeta_6)`;
2. period-two Dwork dash on the hypergeometric parameters;
3. Frobenius permutation of the `mu_6` character eigenspaces.

This triple agreement is the main structural reason to expect the classical
truncated obstruction to live in an off-diagonal Hasse--Witt/Frobenius block
rather than in a scalar trace over `F_p`.

## 6. Sharpened Hasse--Witt target

The remaining bridge can now be localized.

One no longer needs to recover the full cohomology or the entire point count
of the toric family.  It is enough to understand the Frobenius action on the
character orbit

\[
\boxed{\{1,5\}.}
\]

Over `F_p` this orbit is exchanged, while over `F_{p^2}` each character is
fixed.  Therefore the relevant mod-`p` Hasse--Witt/Cartier matrix should have a
period-two block structure schematically of the form

\[
\begin{pmatrix}
0 & A_p\\
B_p & 0
\end{pmatrix},
\]

where `A_p` and `B_p` act between the rank-three target and conjugate sectors.

This displayed matrix is a **target form**, not yet a proved identification of
cohomological bases.  What is proved is only the character permutation that
forces any Frobenius-equivariant decomposition to exchange the two sectors.

The next exact theorem target is to show that the classical full truncation

\[
\mathcal H_p
=
{}_3F_2\!\left[
\begin{matrix}-1/6,1/3,4/3\\1,1\end{matrix};1
\right]_{p-1}
\pmod p
\]

is an entry, determinant factor, or rank-loss criterion of `A_p` (equivalently
of the corresponding Cartier/Hasse--Witt map from character `1` to character
`5`).

That would turn

\[
p\mid F_{(p+1)/3}
\iff
\mathcal H_p=0
\]

into a geometric non-ordinary/rank-drop condition for this explicit
Frobenius character orbit.

## 7. Executable assets

`src/enterprise_math/p022_barlow_franel_third_index_gamma_triple.py` now
exposes:

- `gamma_twist_parameters`;
- `all_gamma_twists`;
- `frobenius_character_orbits`;
- `target_character_orbit_closure`.

The companion tests lock the exact six-twist table, inert orbits
`{0},{1,5},{2,4},{3}`, split-prime singleton orbits, and equality of the
`{1,5}` orbit with the previously derived rational rank-six closure.
