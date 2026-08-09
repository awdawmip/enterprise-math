# A3 Guard-Image Lattice Supplement 09 — Hidden Scalar Band Predicates, Residue Certificates, and Asymmetric Support Precision

Status: `RESEARCH WIP / EXACT SCALAR SUBGROUP BAND THEOREM + A3-TO-A4 CONSEQUENCE`

## 1. Problem

Many future relation queries are finite bands rather than one-sided thresholds:

\[
\boxed{|z|\le R.}
\]

The A3-generated A4 pairwise radius-support predicate has exactly this form, with `z` a weighted relation and `R` an integer radius budget multiplied by capacities.

The question is whether a coarse fiber can answer the band predicate exactly while the scalar relation itself remains hidden.

The answer is asymmetric: a hidden nonzero scalar fiber can be exactly **false**, but it cannot be exactly **true** over the full integer fiber.

## 2. Scalar hidden image

Let

\[
z(c)=w^Tc+b
\]

be an integer linear scalar observable. For a coordinate partition `A`, hidden variation is a subgroup of `Z`:

\[
w(K_A)=q\mathbb Z,
\qquad q\in\mathbb N_0.
\]

- `q=0`: the scalar observable descends exactly;
- `q>0`: one coarse fiber contains exactly
  \[
  \boxed{z_0+q\mathbb Z.}
  \]

For coordinate partitions, `q` is the gcd of the within-block coefficient differences.

## 3. A3-G34 — Least absolute residue

For `q>0`, define

\[
\boxed{\rho_q(z_0)=\min_{t\in\mathbb Z}|z_0+qt|.}
\]

If `r=z_0 mod q`, `0<=r<q`, then

\[
\boxed{\rho_q(z_0)=\min(r,q-r).}
\]

Thus the progression intersects `[-R,R]` iff

\[
\boxed{\rho_q(z_0)\le R.}
\]

## 4. A3-G35 — Hidden finite-band exactness theorem

Consider

\[
P_R(z):=[|z|\le R],
\qquad R\in\mathbb N_0.
\]

If `q=0`, the scalar is coarse-readable and the predicate has its ordinary exact value.

If `q>0`, the progression `z_0+qZ` is unbounded in both directions, so every finite band misses some points of the fiber. Therefore the predicate can never be uniformly true on a nontrivial hidden fiber.

Supported points exist iff `rho_q(z_0)<=R`. Hence

\[
\boxed{
q>0:\quad
P_R\text{ is exact}
\iff
\rho_q(z_0)>R,
}
\]

and the only exact hidden value is

\[
\boxed{P_R=\mathrm{False}.}
\]

If `rho_q(z_0)<=R`, the same coarse fiber contains both supported and unsupported fine states, so the predicate does not factor through the quotient.

## 5. Difference from one-sided thresholds

For a one-sided threshold `z>=0`, every nonzero hidden arithmetic progression reaches both signs. A finite band has finite width, so one residue class can miss it entirely.

Thus

\[
\boxed{
\text{hidden scalar relation}
\not\Rightarrow
\text{every predicate requires refinement}.
}
\]

Task precision depends jointly on predicate geometry and hidden subgroup residue.

## 6. A3-G36 — Exact-false residue certificate

When

\[
q>0,
\qquad
\rho_q(z_0)>R,
\]

the integer tuple

\[
\boxed{(z_0\bmod q,\ q,\ \rho_q(z_0),\ R)}
\]

is a finite exact-false certificate proving

\[
\forall t\in\mathbb Z,\qquad |z_0+qt|>R.
\]

No exact fine scalar or branch/witness identity is needed.

## 7. Refinement can turn ambiguity into exact false

If refinement changes the scalar hidden subgroup from `qZ` to `q'Z`, with `q'` a positive multiple of `q`, the child fiber keeps only one parent residue class. The quantity `rho_(q')(z_0)` can exceed `rho_q(z_0)`.

When

\[
\boxed{\rho_{q'}(z_0)>R,}
\]

the predicate becomes exact false even though the scalar relation may remain hidden. This is the scalar-band form of the residue precision separation from Supplements 05 and 06.

## 8. A3-to-A4 radius-support corollary

The A3-generated A4 support family uses

\[
\boxed{|Z_{ij}|\le r\,m_i m_j.}
\]

Let

\[
R=r\,m_i m_j.
\]

Suppose a coarser partition hides the exact relation so one coarse fiber has

\[
Z_{ij}\in z_0+q\mathbb Z.
\]

- If `q=0`, support truth is ordinary exact relation evaluation.
- If `q>0` and `rho_q(z_0)>R`, every fine lift is unsupported, so support safely descends as `False` without exact relation visibility.
- If `q>0` and `rho_q(z_0)<=R`, the same coarse fiber contains both supported and unsupported fine lifts, so support truth itself does not factor through the quotient.

In particular, under the full-integer-fiber assumption, a nontrivially hidden `Z_ij` cannot certify that **all** fine lifts are support-true.

This is consistent with the earlier bridge cancellation counterexample and strengthens it with an arithmetic residue criterion.

## 9. Ownership boundary

The generic scalar-band theorem belongs to A3 future precision. The A3-to-A4 support statement is only a downstream specialization; formal bridge ownership remains on `research/core/relation-support-bridge`. A3 should relay the corollary rather than duplicate bridge implementation.

## 10. Implementation

Added:

- `src/enterprise_math/hidden_band_predicate.py`;
- `tests/test_hidden_band_predicate.py`.

Main APIs:

- `scalar_hidden_step`;
- `least_absolute_residue`;
- `hidden_band_profile`;
- `hidden_band_profile_for_partition`;
- `HiddenBandProfile`.

Tests cover the gcd hidden-step law, exact least-absolute residues, exact-false hidden fibers, impossibility of hidden exact-true finite bands, visible scalar behavior, direct progression pressure checks, and a partition that answers false exactly while the scalar remains hidden.

## 11. Boundary

The theorem assumes the full affine integer fiber `z_0+qZ` and finite radius `R`. If an application restricts fine states to a finite ball or another admissible subset, the existence of unsupported states must be re-proved in that application. Do not transplant the full-integer-fiber corollary mechanically to a restricted physical domain.

## 12. Next

1. relay the support corollary to the A3-to-A4 bridge;
2. evaluate the bridge's cancellation example through the hidden-step/residue lens;
3. analyze staged support / split-completeness as multiple finite-band obligations;
4. connect the scalar-band certificate to P018 task precision profiles;
5. derive all-state coarse-program conditions symbolically rather than by state sampling.
