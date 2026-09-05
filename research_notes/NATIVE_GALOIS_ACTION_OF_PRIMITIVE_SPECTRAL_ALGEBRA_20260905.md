# Native phase-multiplication Galois action on primitive spectral algebras

Status: `FREE_RESEARCH / EXACT FINITE-GALOIS THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- phase multiplication polynomials `R_a`;
- primitive factor pullback law;
- internal phase quantization;
- odd-denominator orientation splitting.

## 1. Unit phase multipliers induce quotient-algebra automorphisms

Fix `d>1`.  Let

\[
\mathscr A_d=\mathbb Q[u]/(\Psi_d(u))
\]

and write `ubar` for the root class.

Take an integer `a` with

\[
(a,2d)=1.
\]

The primitive pullback factorization of `Psi_d(R_a)` contains `Psi_d` because the divisor-fiber term `g=1` is allowed exactly when `(a,d)=1`.  Hence

\[
\Psi_d\mid\Psi_d(R_a(u)).
\]

Therefore substitution defines a `Q`-algebra endomorphism

\[
\boxed{
\sigma_a:\mathscr A_d\to\mathscr A_d,
\qquad
\sigma_a(\bar u)=R_a(\bar u).
}
\tag{GAL-1}

## 2. Inverse and residue-class dependence

If

\[
ab\equiv\pm1\pmod{2d},
\]

then on every primitive phase root

\[
R_{ab}(u_{r,d})=u_{r,d},
\]

because multiplying the internal phase index by `ab` changes it only by sign and full periods `2d`.

Since the primitive polynomial has simple roots,

\[
R_{ab}(u)\equiv u\pmod{\Psi_d}.
\]

Using `R_ab=R_a o R_b`,

\[
\sigma_a\sigma_b=\operatorname{id}.
\]

Thus every `sigma_a` is an automorphism and depends only on the residue class of `a` modulo `2d`, with `a` and `-a` acting identically because the internal cosine coordinate is even.

Hence there is a group action

\[
\boxed{
G_d:=(\mathbb Z/2d\mathbb Z)^\times/\{\pm1\}
\longrightarrow
\operatorname{Aut}_{\mathbb Q}(\mathscr A_d).
}
\tag{GAL-2}

## 3. Even denominator: transitive action on all primitive roots

Assume `d` is even.  Every residue `r` with `(r,d)=1` is odd, so the primitive root labels are precisely the unit-phase orbit modulo `2d`, quotiented by `r~ -r` because the coordinate `u=2-2C(theta)` is even under phase sign.

Thus `G_d` acts transitively on all roots of `Psi_d`.

For even `d`,

\[
\varphi(2d)=2\varphi(d),
\]

so

\[
\boxed{|G_d|=\varphi(d)=\deg\Psi_d.}
\tag{GAL-3}

The orbit of one root therefore has full polynomial degree.  Its minimal polynomial over `Q` has degree at least this orbit size and divides `Psi_d`; hence it equals `Psi_d`.

Therefore

\[
\boxed{
\Psi_d\text{ is irreducible over }\mathbb Q
\qquad(d\text{ even}).
}
\tag{GAL-4}

Consequently `mathscr A_d` is a field and the constructed automorphism group already has size equal to the field degree:

\[
\boxed{
\operatorname{Gal}(\mathscr A_d/\mathbb Q)
\cong G_d
=(\mathbb Z/2d\mathbb Z)^\times/\{\pm1\}.
}
\tag{GAL-5}

The extension is abelian.

## 4. Odd denominator: orientation components are the transitive orbits

Assume `d>1` is odd.  Then every unit modulo `2d` is odd.  Multiplication by an odd `a` preserves the parity of the canonical mode index `r`.

The primitive factor splits

\[
\Psi_d=\Psi_d^E\Psi_d^O,
\]

where `E` is the even-index orbit and `O` the odd-index orbit.

Now

\[
\varphi(2d)=\varphi(d),
\]

so

\[
\boxed{
|G_d|=\frac{\varphi(d)}2
=\deg\Psi_d^E
=\deg\Psi_d^O.
}
\tag{GAL-6}

The `G_d` action is transitive on each parity orbit separately.  The same orbit/minimal-polynomial argument gives

\[
\boxed{
\Psi_d^E,\Psi_d^O
\text{ are each irreducible over }\mathbb Q.
}
\tag{GAL-7}

Thus

\[
\boxed{
\mathscr A_d
\cong K_d^E\times K_d^O,
}
\tag{GAL-8}

where both components are abelian Galois fields of degree `phi(d)/2` with

\[
\boxed{
\operatorname{Gal}(K_d^{E/O}/\mathbb Q)
\cong G_d.
}
\tag{GAL-9}

## 5. Complement orientation involution

The complement map

\[
\boxed{\kappa(\bar u)=4-\bar u}
\tag{GAL-10}

exchanges `K_d^E` and `K_d^O`.

For odd phase multiplier `a`,

\[
R_a(4-u)=4-R_a(u).
\]

Hence

\[
\boxed{\kappa\sigma_a=\sigma_a\kappa.}
\tag{GAL-11}

So the full odd primitive algebra carries commuting data:

- an abelian Galois action inside each orientation component;
- one central involution exchanging the two orientation components.

This explains why orientation can be preserved as an independent finite type without interfering with the internal phase-multiplication symmetries.

## 6. Character-weighted traces are Galois-character coordinates

The character-weighted primitive mode sums introduced previously used characters of the finite primitive phase-label group.  The present theorem identifies that group intrinsically with the phase-multiplication Galois group `G_d` on each irreducible component.

Therefore the nonprincipal character channels can be read as character coordinates of the native finite Galois action, not merely as externally imposed Fourier weights.

For odd `d`, the extra reflection sign distinguishes the two isomorphic Galois components; forgetting that sign recoalesces them and loses the odd-phase arithmetic trace described in the orientation-resolved Ramanujan theorem.

## 7. Classical cyclotomic compatibility is downstream

Classically, the fields above are compatible with maximal real cyclotomic trace fields under the change of variable `u=2-z-z^{-1}`.  That provides historical identification of the abelian Galois group.

But the finite proof route here uses only:

```text
primitive finite phase labels
+ internal phase multiplication R_a
+ primitive pullback divisibility
+ finite root orbit count
```

so the Galois action and irreducibility can be established before introducing roots of unity as proof input.

## 8. Typing consequence

For even denominator, one primitive factor is one irreducible finite spectral field.

For odd denominator, the full primitive polynomial is reducible for a typed reason: reflection orientation splits the root set into two irreducible Galois orbits, not because the finite spectral construction failed to isolate primitive modes.

Freeze:

`EVEN_d: PSI_d = IRREDUCIBLE ABELIAN GALOIS SPECTRAL FIELD`.

`ODD_d: PSI_d = E_FIELD x O_FIELD WITH EACH FACTOR IRREDUCIBLE`.

`PHASE_MULTIPLICATION_UNITS = NATIVE GALOIS ACTION`.

`REFLECTION_ORIENTATION = SEPARATE COMMUTING C2 EXCHANGE`.
