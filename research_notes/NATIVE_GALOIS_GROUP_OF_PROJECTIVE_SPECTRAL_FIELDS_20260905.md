# Native Galois group of the projective primitive spectral fields

Status: `FREE_RESEARCH / EXACT FINITE SPECTRAL GALOIS THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- native irreducibility of `Omega_d`;
- primitive projective root indexing;
- integer decimation semigroup `R_n`;
- native discriminant and Frobenius congruence.

## 1. Primitive projective spectral field

Fix `d>2` and let

\[
\Omega_d(v)\in\mathbf Z[v]
\]

be the monic irreducible projective primitive spectral factor of degree

\[
\boxed{h_d=\varphi(d)/2.}
\]

Choose one primitive root

\[
\alpha_d:=v_{1,d}
\]

and define

\[
\boxed{K_d:=\mathbf Q(\alpha_d).}
\]

By irreducibility,

\[
[K_d:\mathbf Q]=h_d.
\]

---

## 2. Every primitive root already lies in the root field

For every integer `r` with

\[
\gcd(r,d)=1,
\]

the integer decimation polynomial satisfies

\[
\boxed{
R_r(\alpha_d)=v_{r,d}.
}
\tag{GA-1}

Since `R_r` has integer coefficients,

\[
R_r(\alpha_d)\in K_d.
\]

As `r` runs through the unit classes modulo `d`, modulo the projective pairing

\[
r\sim-r,
\]

the values `v_(r,d)` run through all `phi(d)/2` distinct roots of `Omega_d`.

Therefore **all roots of `Omega_d` lie in `K_d`**.

Hence

\[
\boxed{K_d\text{ is the splitting field of }\Omega_d.}
\tag{GA-2}

Because characteristic zero implies separability,

\[
\boxed{K_d/\mathbf Q\text{ is Galois}.}
\tag{GA-3}

---

## 3. Decimation automorphisms

For every unit class `r mod d`, define

\[
\boxed{
\sigma_r(\alpha_d):=R_r(\alpha_d).
}
\tag{GA-4}

Since `R_r(alpha_d)` is another root of the irreducible minimal polynomial `Omega_d`, the assignment extends uniquely to a `Q`-embedding

\[
\sigma_r:K_d\to K_d.
\]

A finite-dimensional field endomorphism is injective and hence surjective, so each `sigma_r` is an automorphism.

The semigroup law

\[
R_{rs}=R_r\circ R_s
\]

gives

\[
\boxed{
\sigma_r\sigma_s=\sigma_{rs}.
}
\tag{GA-5

Thus the spectral decimation maps themselves realize the Galois action.

---

## 4. Kernel is exactly the complement sign

The projective primitive roots satisfy

\[
v_{r,d}=v_{s,d}
\iff
r\equiv\pm s\pmod d.
\]

In particular,

\[
\sigma_r(\alpha_d)=\alpha_d
\iff
r\equiv\pm1\pmod d.
\]

Therefore the map

\[
(\mathbf Z/d\mathbf Z)^\times
\longrightarrow
\operatorname{Gal}(K_d/\mathbf Q),
\qquad
r\mapsto\sigma_r,
\]

has kernel `{±1}` and induces an injection

\[
\boxed{
(\mathbf Z/d\mathbf Z)^\times/\{\pm1\}
\hookrightarrow
\operatorname{Gal}(K_d/\mathbf Q).
}
\tag{GA-6

The source has order

\[
\varphi(d)/2=[K_d:\mathbf Q],
\]

which equals the order of the full Galois group.  Hence the injection is an isomorphism:

\[
\boxed{
\operatorname{Gal}(K_d/\mathbf Q)
\cong
(\mathbf Z/d\mathbf Z)^\times/\{\pm1\}.
}
\tag{GA-7

Classification: `EXACT_NATIVE_FINITE_SPECTRAL_GALOIS_THEOREM`.

---

## 5. Actual arithmetic Frobenius

The native projective discriminant formula shows that every rational prime ramified in `K_d` divides `d`.

Thus if

\[
p\nmid d,
\]

then `p` is unramified in `K_d`.

The prime decimation congruence is

\[
\boxed{
R_p(v)\equiv v^p\pmod p.
}
\tag{GA-8

But the Galois automorphism `sigma_p` is defined by

\[
\sigma_p(\alpha_d)=R_p(\alpha_d).
\]

Therefore modulo any prime of `K_d` above `p`,

\[
\boxed{
\sigma_p(\alpha_d)
\equiv
\alpha_d^p.
}
\tag{GA-9

Since `alpha_d` generates the field, this identifies `sigma_p` with the arithmetic Frobenius element at `p`:

\[
\boxed{
\operatorname{Frob}_p
=\sigma_p
\leftrightarrow
[p]\in
(\mathbf Z/d\mathbf Z)^\times/\{\pm1\}.
}
\tag{GA-10

Thus the earlier term “denominator Frobenius” is not merely structural: on the primitive projective spectral field, prime decimation *is* the actual Frobenius action.

---

## 6. Splitting and residue degree from spectral decimation

For `p\nmid d`, the residue degree of `p` in the Galois extension is the order of its Frobenius element.

Hence

\[
\boxed{
f_p
=
\operatorname{ord}_{(\mathbf Z/d\mathbf Z)^\times/\{\pm1\}}(p).
}
\tag{GA-11

Equivalently, `f_p` is the least positive integer `f` such that

\[
\boxed{
p^f\equiv\pm1\pmod d.}
\tag{GA-12

Therefore:

- `p` splits completely in `K_d` iff `p congruent ±1 mod d`;
- more generally the factor degrees of `Omega_d mod p` are all equal to the least `f` with `p^f congruent ±1 mod d`.

So finite spectral decimation directly predicts finite-field factorization degrees.

---

## 7. Prime-power local ramification fits the same picture

For `d=p^a>2`, the prime-power spectral factor `Omega_d` is `p`-Eisenstein.

Hence the unique prime `p` dividing the conductor-scale denominator is totally ramified in the local extension, while every `q\nmid d` is unramified and acts through

\[
\operatorname{Frob}_q=\sigma_q.
\]

Thus the finite spectral theory independently reconstructs both sides of the arithmetic behavior:

```text
prime divides denominator d
  -> Eisenstein / ramification

prime coprime to denominator d
  -> R_p(v)=v^p mod p
  -> Frobenius automorphism sigma_p
```

---

## 8. Oriented spectral factors

The oriented primitive factor obeys

```text
d even:
  Psi_d = Omega_(2d), irreducible

d odd:
  Psi_d = Omega_d * Omega_(2d), two irreducible sheets.
```

Therefore the oriented spectral fields have Galois groups

\[
\operatorname{Gal}(K_{2d}/\mathbf Q)
\cong
(\mathbf Z/2d\mathbf Z)^\times/\{\pm1\},
\]

with the additional `Omega_d` sheet when `d` is odd.

This makes the previously retained orientation/complement sheet an exact field-theoretic decomposition, not only a root-label convention.

---

## 9. BRC meaning

For a BRC module in the declared rational rotation sector, projective primitive repetition singularities produce `Omega_d` root blocks.

The theorem now says:

- each such block is a Galois field block;
- every atlas-compatible integer repetition `r` acts on the block by the explicit polynomial automorphism `R_r`;
- good-prime reduction turns the same operation into arithmetic Frobenius.

So one finite algebraic operation has three simultaneous readings:

```text
BRC module repetition
spectral decimation
Galois/Frobenius action on the primitive root block
```

Hard boundary: this does not assert that an arbitrary BRC root block is abelian/Galois; it applies to the identified projective spectral division-polynomial family.

---

## 10. Relation to classical cyclotomic fields

A later compatibility theorem identifies `K_d` with the corresponding maximal real cyclotomic trace field.  Under that identification, (GA-7)-(GA-12) become familiar cyclotomic facts.

But the proof above requires only:

- native irreducibility;
- finite root indexing;
- integer decimation maps;
- native discriminant prime support;
- the congruence `R_p(v)=v^p mod p`.

Thus the Galois group and Frobenius action are reconstructed internally from the finite spectral system before roots of unity are named.

Freeze at free-research strength:

`PROJECTIVE_SPECTRAL_ROOT_FIELD = ITS_OWN_SPLITTING_FIELD`.

`GAL(K_d/Q) = UNITS_MOD_d / PLUS_MINUS_ONE`.

`PRIME_DECIMATION_R_p = ACTUAL_ARITHMETIC_FROBENIUS_AT_p_FOR_p_NOT_DIVIDING_d`.
