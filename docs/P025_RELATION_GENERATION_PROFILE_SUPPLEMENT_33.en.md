# P025 Supplement 33 — Finite Rank/Index Profile of Relation Generation

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-shared-access-stage30`  
Depends on: P025 Supplements 31–32  
Hard block: `NONE`

## 1. `rho_gen` is only the endpoint of a finite response

For a relation lattice `Lambda`, define

\[
\boxed{
\Gamma_R
=
\langle Z_R(B)\cap\Lambda\rangle.
}
\]

Because

\[
Z_R(B)\subseteq Z_{R+1}(B),
\]

one has a nested subgroup chain

\[
\boxed{
\Gamma_R\subseteq\Gamma_{R+1}\subseteq\Lambda.
}
\]

Stage 32 defines `rho_gen` as the first radius where `Gamma_R=Lambda`. The intermediate subgroups carry additional exact precision information.

## 2. P025-T90 — generated rational rank is nondecreasing

Let

\[
r_R=\operatorname{rank}_{\mathbb Q}\Gamma_R.
\]

Nested subgroups give

\[
\boxed{r_R\le r_{R+1}.}
\]

Define the **full-rank radius**

\[
\boxed{
\rho_{\rm rank}
=
\min\{R:r_R=\operatorname{rank}\Lambda\}.
}
\]

This is the first radius at which currently accessible relation states span every rational relation direction.

It can still be too early for integral generator completeness.

## 3. P025-T91 — finite indices form a divisibility chain

For `R>=rho_rank`, define

\[
\boxed{
I_R=[\Lambda:\Gamma_R]<\infty.
}
\]

Since

\[
\Gamma_R\subseteq\Gamma_{R+1}\subseteq\Lambda,
\]

ordinary subgroup-index multiplication gives

\[
I_R
=
[\Lambda:\Gamma_{R+1}]
[\Gamma_{R+1}:\Gamma_R].
\]

Therefore

\[
\boxed{I_{R+1}\mid I_R.}
\]

In particular finite indices are nonincreasing, but the stronger statement is divisibility rather than mere numerical order.

The endpoint is

\[
\boxed{I_{\rho_{\rm gen}}=1.}
\]

## 4. P025-D21 — strict rank/index profile

Before full rank, use `I_R=infinity`. Record a radius only when the pair

\[
\boxed{(r_R,I_R)}
\]

changes.

This yields a finite strict-change profile from the first nonzero relation state through generator completeness.

The profile separates four possible stages:

1. no nonzero relation state;
2. nonzero but rationally rank-deficient subgroup;
3. full rational rank with finite index `>1`;
4. full integral generator completeness, index `1`.

Some systems skip one or more stages.

## 5. P025-T92 — finite bound on the number of index drops

Suppose the first full-rank layer has index

\[
I_0>0.
\]

Every strict later finite-index change replaces the current index by a proper positive divisor. A proper positive divisor of `n` is at most `n/2`.

Hence the number of distinct finite-index levels is at most

\[
\boxed{\operatorname{bitlength}(I_0).}
\]

This is only a finite combinatorial bound on the number of strict index states. It is not a complexity bound for constructing the reachable layers.

## 6. Exact arithmetic example `1+22=23`

Take the unit relation basis

\[
\boxed{g=(0,1,1).}
\]

At radius two, the accessible common derivative scales are `0,±2`. Therefore the generated coordinate subgroup is

\[
2\mathbb Z.
\]

So the relation rank is already full:

\[
\boxed{\rho_{\rm rank}=2,}
\]

but

\[
\boxed{I_2=2.}
\]

Radius three does not change the subgroup.

At radius four, scale `3` is also accessible; together scales `2` and `3` generate `Z`. Thus

\[
\boxed{I_4=1,\qquad\rho_{\rm gen}=4.}
\]

The strict profile is therefore

\[
\boxed{
(2;\ r=1,I=2)
\longrightarrow
(4;\ r=1,I=1).
}
\]

This is a real arithmetic relation where full rational information appears strictly before integral generator completeness.

## 7. `1+8=9` skips the finite-index intermediate layer

At radius two the primitive common derivative step itself is already accessible. Therefore

\[
\boxed{
\rho_{\rm rank}=\rho_{\rm gen}=2,
\qquad
I_2=1.
}
\]

The strict profile contains one nonzero point only.

## 8. Rank-two `2+3=5` also completes immediately

The two standard relation basis vectors are already accessible at radius one, so

\[
\boxed{
\rho_{\rm rank}=\rho_{\rm gen}=1,
\qquad
I_1=1.
}
\]

Again there is no finite-index defect layer.

## 9. Architecture consequence

The generation-completeness state should not be summarized by rank alone.

A more faithful discrete precision ladder is

\[
\boxed{
\text{accessible relation states}
\to
\text{rational span rank}
\to
\text{integral subgroup index}
\to
\text{index-one completeness}.
}
\]

Rank asks whether all rational directions are visible. Index asks whether the accessible states have also resolved the remaining finite integral congruence obstruction.

This mirrors several earlier Enterprise Math distinctions between:

- rational/free-rank information and torsion/congruence detail;
- support existence and exact witness multiplicity;
- coarse span completeness and exact integer-state completeness.

## 10. Prior-art / ownership boundary

Nested subgroup indices, divisibility of finite indices, and maximal-minor lattice index are standard algebra.

P025 does not claim them. The project-side result under test is the radius-indexed finite precision profile induced by arithmetic derivative-image access.

This should be relayed to A3/P023 as a worked relation-precision coordinate, while generic subgroup-index theory remains prior art.

## 11. Executable assets

Added:

- `src/enterprise_math/relation_generation_profile.py`
  - strict rank/index profile;
  - monotonicity/divisibility assertions;
  - first nonzero, full-rank, and generator radii;
  - finite index-drop count bound.
- `tests/test_relation_generation_profile.py`
  - `1+22=23` full-rank/index-two intermediate state;
  - `1+8=9` immediate completeness;
  - rank-two abc immediate completeness;
  - long-basis invariance;
  - shared-prime rank-one boundary.

## 12. Next frontier

No hard block exists. Continue with:

1. seek a higher-rank arithmetic example with `rho_rank<rho_gen`;
2. identify finite quotient data that represents the index defect without storing all accessible states;
3. compare this index profile with A3 quotient-module torsion coordinates;
4. study whether certificate rank gain should be paired with a finite certificate-image index defect;
5. freeze Stage30–33 for a checkpoint before opening a separate next-generation research branch.
