# Frobenius factorization of primitive spectral polynomials at good primes

Status: `FREE_RESEARCH / EXACT FINITE-FIELD GALOIS THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- native phase-multiplication Galois action;
- congruence `R_l(u)=u^l mod l` for prime `l`;
- primitive spectral discriminant support.

## 1. Good-prime hypothesis

Fix `d>1` and a prime `ell` satisfying

\[
\boxed{\ell\nmid2d.}
\tag{FFF-1}

The primitive discriminant formula has prime support contained in `2d`.  Therefore

\[
\ell\nmid\operatorname{Disc}\Psi_d.
\]

For odd `d`, the orientation-factor discriminants also have prime support contained in `2d`, so each of `Psi_d^E,Psi_d^O` is squarefree modulo `ell` as well.

Thus the good-prime reductions are separable.

## 2. Phase multiplication equals finite-field Frobenius

For every prime `ell`,

\[
\boxed{R_\ell(u)\equiv u^\ell\pmod\ell.}
\tag{FFF-2}

Let `alpha` be a root of a good-prime reduction in an algebraic closure of `F_ell`.  Then

\[
\boxed{
\alpha^\ell=R_\ell(\alpha).
}
\tag{FFF-3}

The left side is arithmetic Frobenius; the right side is the same phase-multiplication action which defined the characteristic-zero Galois automorphism `sigma_ell`.

Hence

`FINITE_FIELD_FROBENIUS = REDUCED_PHASE_AUTOMORPHISM`.

## 3. Order in the native phase Galois group

Define

\[
G_d=(\mathbb Z/2d\mathbb Z)^\times/\{\pm1\}.
\]

The class of `ell` lies in `G_d` by the good-prime hypothesis.  Let

\[
\boxed{
f_d(\ell):=\operatorname{ord}_{G_d}(\ell).
}
\tag{FFF-4}

Equivalently,

\[
\boxed{
f_d(\ell)
=\min\{r\ge1:\ell^r\equiv\pm1\pmod{2d}\}.
}
\tag{FFF-5}

By (FFF-3), this is exactly the Frobenius orbit length of any root inside one transitive primitive Galois orbit.

## 4. Even denominator factorization

If `d` is even, `Psi_d` is irreducible over `Q` and its primitive roots form one transitive `G_d` orbit of size

\[
|G_d|=\varphi(d).
\]

At the good prime `ell`, every Frobenius orbit therefore has length `f_d(ell)`.  Each orbit is the root set of one irreducible factor over `F_ell`.

Hence

\[
\boxed{
\Psi_d\bmod\ell
\text{ factors into }
\frac{\varphi(d)}{f_d(\ell)}
\text{ distinct irreducibles,}
}
\tag{FFF-6}

all of common degree

\[
\boxed{f_d(\ell).}
\tag{FFF-7}

## 5. Odd denominator orientation factorization

If `d>1` is odd, the two irreducible characteristic-zero orientation factors have degree

\[
\varphi(d)/2
\]

and each is one transitive `G_d` orbit.

Since `ell` is odd, phase multiplication preserves reflection parity.  Therefore Frobenius acts separately on the `E` and `O` root sets.

Each of

\[
\Psi_d^E\bmod\ell,
\qquad
\Psi_d^O\bmod\ell
\]

factors into

\[
\boxed{
\frac{\varphi(d)/2}{f_d(\ell)}
}
\tag{FFF-8}

mutually distinct irreducible factors, all of degree `f_d(ell)`.

The two orientation factors have identical good-prime decomposition type, consistent with their complement-field isomorphism.

## 6. Complete splitting criterion

The good-prime reduction splits completely exactly when the Frobenius class is trivial in `G_d`:

\[
f_d(\ell)=1.
\]

Thus

\[
\boxed{
\text{complete splitting}
\iff
\ell\equiv\pm1\pmod{2d}.
}
\tag{FFF-9

For odd `d`, this criterion applies to each orientation field separately.

## 7. Irreducibility criterion modulo ell

For even `d`, the full good-prime reduction is irreducible iff

\[
\boxed{
f_d(\ell)=\varphi(d).}
\tag{FFF-10}

For odd `d`, each orientation factor is irreducible modulo `ell` iff

\[
\boxed{
f_d(\ell)=\varphi(d)/2.}
\tag{FFF-11}

Such a prime can exist only when the native phase Galois group contains an element of the corresponding full order.

## 8. Unified local-prime behavior

The same phase polynomial `R_p` controls three distinct local regimes.

### good prime p not dividing 2d

\[
R_p\equiv u^p\pmod p
\]

acts as a separable Frobenius permutation of the primitive support.  Factor degrees are orbit lengths in `G_d`.

### denominator prime p|d

Distinct characteristic-zero p-adic levels collapse modulo `p` into Frobenius thickenings of a common support.  The special fiber is nonreduced and p-adic depth becomes nilpotent multiplicity.

### orientation prime p=2 with d odd

The two characteristic-zero reflection components collapse onto the same mod-two support; their resultant is one flat two-torsion layer in every orientation coordinate.

Thus

\[
\boxed{
\text{GOOD PRIME}:\text{ permutation},
\quad
\text{BAD DENOMINATOR PRIME}:\text{ thickening},
\quad
2\text{-ORIENTATION PRIME}:\text{ orientation recoalescence}.
}
\tag{FFF-12}

## 9. Classical compatibility

Under the later real-cyclotomic trace identification, (FFF-5)--(FFF-11) become the familiar splitting laws for maximal real cyclotomic fields.

The proof route here, however, is finite-spectral:

```text
native primitive phase Galois action
+ R_ell mod ell = Frobenius
+ primitive discriminant support
-> exact finite-field factorization degrees
```

No roots-of-unity factorization theorem is required as input.

Freeze:

`GOOD_PRIME_FROBENIUS = PHASE_MULTIPLICATION_BY_ell`.

`FACTOR_DEGREE = ORDER_OF_ell_IN_(Z/2dZ)^x/{+/-1}`.

`BAD_PRIME_THICKENING_AND_GOOD_PRIME_PERMUTATION = TWO_LOCAL_FACES_OF_SAME_R_p`.
