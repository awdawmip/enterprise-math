# P025 Supplement 02 — Canonical Exterior Signature of the Witness Flag

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P025 Supplement 01; P023 quotient/minimal repair  
Mathematical background: rational linear algebra, saturated integer lattices, exterior algebra/Plücker coordinates are prior mathematics  
Novelty status: `ARCHITECTURE NOVELTY_UNVERIFIED`

## 1. Problem

P025 Supplement 01 produced the relation-conditioned witness flag

\[
T^\circ\subsetneq T\subset\mathbb Z^S,
\]

with

\[
T=\ker_{\mathbb Z}\alpha,
\qquad
T^\circ=\ker_{\mathbb Z}\alpha\cap\ker_{\mathbb Z}\beta.
\]

After primitive sign normalization, `alpha` is a canonical normal for `T`.

But the raw pair `(alpha,beta)` is not a canonical state of the flag, because for any `lambda neq 0` and `mu`,

\[
\beta'=\lambda\beta+\mu\alpha
\]

has the same zero set as `beta` on `T=ker(alpha)` and therefore defines the same `T^circ`.

The precise question is:

> What finite integer object represents this nested witness flag exactly without retaining meaningless shear/scaling freedom in `beta`?

## 2. Exterior product removes the shear

Consider

\[
\alpha\wedge\beta\in\bigwedge^2\mathbb Z^S.
\]

If

\[
\beta'=\lambda\beta+\mu\alpha,
\]

then

\[
\alpha\wedge\beta'
=\lambda(\alpha\wedge\beta),
\]

because

\[
\alpha\wedge\alpha=0.
\]

Thus, after dividing the Plücker coordinates of `alpha wedge beta` by their gcd and fixing global sign, its primitive projective class removes both

- the shear `beta -> beta + mu alpha`, and
- nonzero overall scaling `beta -> lambda beta`.

Write this canonical two-form as

\[
\widehat\Pi(\alpha,\beta).
\]

## 3. P025-T07 — complete finite signature of the saturated witness flag

Fix one finite labelled coordinate set `S`. Let `alpha,beta` and `alpha',beta'` satisfy:

- `alpha,alpha'` are primitive and nonzero;
- `beta` is not in `Q alpha`;
- `beta'` is not in `Q alpha'`.

Define the saturated flags

\[
F(\alpha,\beta):
\ker_{\mathbb Z}\alpha\cap\ker_{\mathbb Z}\beta
\subset
\ker_{\mathbb Z}\alpha
\subset
\mathbb Z^S.
\]

Then

\[
\boxed{
F(\alpha,\beta)=F(\alpha',\beta')
}
\]

if and only if

\[
\boxed{
\widehat\alpha=\widehat\alpha'
\quad\text{and}\quad
\widehat\Pi(\alpha,\beta)
=
\widehat\Pi(\alpha',\beta').
}
\]

### Proof

Equality of the first integer kernels is equivalent by P025-T06 to equality of the primitive normals:

\[
\widehat\alpha=\widehat\alpha'.
\]

Fix this first row. The second layer `T^circ` is the intersection of `Z^S` with a codimension-one rational hyperplane inside `ker(alpha)`.

Two such saturated integer sublattices agree exactly when the corresponding rational subspaces agree, equivalently when the rank-two row spaces

\[
\operatorname{span}_{\mathbb Q}\{\alpha,\beta\}
\]

and

\[
\operatorname{span}_{\mathbb Q}\{\alpha,\beta'\}
\]

are equal.

The projective Plücker coordinates of a rank-two row space are precisely determined by the nonzero exterior product

\[
[\alpha\wedge\beta].
\]

Primitive sign normalization gives the unique integer representative of the same rational ray. Hence equality of the second layers is equivalent to

\[
\widehat\Pi(\alpha,\beta)
=
\widehat\Pi(\alpha,\beta').
\]

This proves the claim.

## 4. Canonical witness-flag state

For the P025 abc witness define

\[
\boxed{
\Sigma_{\rm flag}(a,b,c)
=
\left(
S,
\widehat\alpha,
\widehat\Pi(\alpha,\beta)
\right).
}
\]

Here:

- `S=supp(abc)` retains the prime-coordinate labels;
- `hat alpha` determines the additive witness lattice `T`;
- `hat Pi` determines the Wronskian-degenerate sublattice `T^circ` inside `T`;
- the `L_infinity` norm is inherited from the same labelled ambient coordinate system.

Thus `Sigma_flag` determines the complete normed flag

\[
T^\circ\subset T\subset\mathbb Z^S
\]

and therefore every finite witness ball

\[
\mathcal W_k=(T\setminus T^\circ)\cap[-k,k]^S
\]

and the critical witness precision `mu`.

## 5. Layered P023 minimal repair

This gives a clean hierarchy at the P025/P023 interface.

### Recover only the additive witness lattice

Future observable:

\[
h_1(x)=T(x).
\]

The coarsest canonical signature is

\[
\Sigma_{\rm add}=(S,\widehat\alpha).
\]

### Recover the complete non-degenerate witness flag

Future observable:

\[
h_2(x)=\bigl(T^\circ(x)\subset T(x)\bigr).
\]

The coarsest canonical signature is upgraded to

\[
\Sigma_{\rm flag}
=(S,\widehat\alpha,\widehat\Pi).
\]

### Decide only whether a small witness exists

Future observable:

\[
h_{3,K}(x)=1_{\mu(x)\le K}.
\]

Here `Sigma_flag` is sufficient but generally need not be coarsest. The actual P023-minimal repair remains to be computed for each selected `K`.

A strict research ladder has therefore appeared: weaker future tasks may permit further collapse of the required signature.

## 6. Interface with A4

A4 studies multivalued admissible support. P025 now provides a natural object that should not be forced into a single-valued map:

\[
x\mapsto\mathcal W_k(x).
\]

But `Sigma_flag` shows that a multivalued witness family can have compact generator data: one rank-one normal plus one primitive projective two-form suffices to reconstruct the entire flag and then generate the finite witness family at a chosen radius.

A possible general direction is therefore

\[
\boxed{
\text{generator signature}
\to
\text{admissible relation family}
\to
\text{task-relative finite slice}.
}
\]

Whether this architecture goes beyond established relation/lattice/automata theory still requires prior-art audit.

## 7. Executable assets

New assets:

- `src/enterprise_math/abc_witness_flag.py`
  - exterior two-form;
  - primitive projective normalization;
  - canonical witness-flag signature;
  - invariance under `beta -> lambda beta + mu alpha`;
  - saturated-flag equality checker.
- `tests/test_abc_witness_flag.py`
  - exterior coordinates;
  - shear/scaling invariance;
  - flag separation for distinct additive normals;
  - canonical signature sample for `5+27=32`;
  - dependent-row rejection.

## 8. Current conclusion

P025 has now compressed an abc application into a more general finite-state candidate:

\[
\boxed{
\text{relation-state}
\to
\text{primitive normal / exterior signature}
\to
\text{normed saturated witness flag}
\to
\text{finite witness precision}.
}
\]

The key feature is that it does not restore the entire forgotten fine state. It restores only the invariants required to generate the certificate space for the active task.

This is exactly what should next pressure-test P023's question “how little information must be restored?” But until a general theorem and prior-art search are complete, the architecture remains `NOVELTY_UNVERIFIED` and must not be promoted into canonical Foundation.
