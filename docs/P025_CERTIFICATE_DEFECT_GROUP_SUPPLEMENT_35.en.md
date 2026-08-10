# P025 Supplement 35 — Full Smith Signature of the Certificate Congruence Defect

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplement 34  
Hard block: `NONE`

## 1. The saturation index is not enough for multi-certificate languages

Stage 34 defines the complete certificate image

\[
C=H(\Lambda)\subseteq\mathbb Z^q
\]

and its intrinsic saturation index

\[
\delta_H=[\operatorname{Sat}(C):C].
\]

For a scalar certificate this index completely determines the finite quotient, because every finite-index subgroup of `Z` is cyclic.

For `q>1`, equal index does not determine the integral congruence structure.

## 2. P025-D23 — full certificate defect group

Define

\[
\boxed{
\mathcal D_H
=
\operatorname{Sat}(C)/C.
}
\]

This is a finite abelian group whenever `C` has positive rational rank.

Choose any integer generators of `C`. If their rank is `d`, let

\[
\Delta_i
\]

be the gcd of all `i x i` minors of the labelled generator matrix, with

\[
\Delta_0=1.
\]

Standard Smith theory gives invariant factors

\[
\boxed{
s_i=\Delta_i/\Delta_{i-1},
\qquad
s_1\mid s_2\mid\cdots\mid s_d.
}
\]

Then

\[
\boxed{
\mathcal D_H
\cong
\bigoplus_{i=1}^d\mathbb Z/s_i\mathbb Z,
}
\]

with trivial factors `s_i=1` retained when useful for rank bookkeeping.

Its cardinality is only

\[
\boxed{
|\mathcal D_H|
=
\prod_i s_i
=
\delta_H.
}
\]

Thus `delta_H` is the order of the defect group, not its complete structure.

## 3. P025-N08 — same index, different certificate defects

Consider two rank-two labelled certificate images in `Z^2`:

\[
C_1
=
4\mathbb Z\times\mathbb Z,
\]

and

\[
C_2
=
2\mathbb Z\times2\mathbb Z.
\]

Both have index four in `Z^2`:

\[
[\mathbb Z^2:C_1]
=
[\mathbb Z^2:C_2]
=4.
\]

But their Smith signatures are

\[
\boxed{(1,4)}
\]

and

\[
\boxed{(2,2)},
\]

so

\[
\mathbb Z^2/C_1\cong\mathbb Z/4,
\qquad
\mathbb Z^2/C_2\cong\mathbb Z/2\oplus\mathbb Z/2.
\]

Therefore

\[
\boxed{
\text{equal certificate rank + equal saturation index}
\not\Rightarrow
\text{equal integral certificate language}.
}
\]

A multi-certificate precision state that retains only `delta_H` can lose which congruence tests are actually independent.

## 4. Scalar Wronskian is the special cyclic case

For the normalized scalar Wronskian from Supplement 34,

\[
\widetilde W(\Lambda)
=
\eta_{\min}\mathbb Z.
\]

Hence

\[
\boxed{
\mathcal D_{\widetilde W}
\cong
\mathbb Z/\eta_{\min}\mathbb Z.
}
\]

There is only one nonzero invariant factor:

\[
\boxed{(\eta_{\min}).}
\]

So the scalar `eta_min` coordinate is complete for the **group structure** of the normalized-Wronskian congruence defect. This explains why no additional Smith data were needed in Stages 04–06.

## 5. Prime-local obstruction becomes the primary decomposition

Factor every invariant factor into prime powers. Equivalently, for each prime `ell`, retain

\[
\boxed{
\bigl(v_\ell(s_1),\ldots,v_\ell(s_d)\bigr).
}
\]

These vectors give the `ell`-primary decomposition of the finite certificate defect group.

For a scalar Wronskian this reduces to the Stage-06 obstruction spectrum

\[
\{(\ell,v_\ell(\eta_{\min}))\}.
\]

Thus Stage 06 is the rank-one instance of a broader multi-certificate congruence-defect spectrum.

## 6. Precision consequence

There are now three strictly different certificate descriptors:

1. **rational rank** — number of independent certificate directions;
2. **defect-group order** `delta_H` — total amount of finite congruence obstruction;
3. **Smith signature** `(s_1,...,s_d)` — exact independent congruence structure.

The third strictly refines the second for multi-certificate languages.

This is another instance of task-relative precision: a future query asking only for the number of missing residue classes may need `delta_H`, while a future query asking exact labelled congruence membership needs the full Smith/lattice embedding data.

## 7. Prior-art / ownership boundary

Smith normal form, determinantal divisors, invariant factors and classification of finite abelian groups are standard mathematics. No priority claim is made.

P025 contributes only the pressure-test integration: the finite certificate defect produced by relation-conditioned arithmetic witnesses should not be collapsed to one scalar index when the future certificate language is genuinely multidimensional.

## 8. Executable assets

`src/enterprise_math/certificate_image_index.py` now exposes:

- all nonzero determinantal divisors;
- Smith invariant factors;
- saturation index as their product / final determinantal divisor.

`tests/test_certificate_image_index.py` includes the exact equal-index/different-defect-group counterexample.

## 9. Next frontier

Continue with the **radius-dependent** defect group

\[
\mathcal D_R
=
\operatorname{Sat}(C)/C_R
\]

and distinguish its intrinsic terminal quotient from the finite-access kernel.
