# RH Möbius path gauge and the boundary-observer obstruction

Status: `RESEARCH FRONTIER / EXACT GAUGE IDENTITY + CAPABILITY BOUNDARY / NOT A PROOF OF RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `Möbius / ordered factor tree / X6 block resolvent / Pair-BRC / shell observer`

## 0. Typing guard

P000 is unchanged. The gauge below acts on arithmetic provenance depth, not on native X6 spatial axes.

---

## 1. Bipartite factor-depth gauge

On the ordered squarefree factor-path Hilbert space, let a basis path gamma have depth `|gamma|`, the number of appended distinct prime labels.

Define the diagonal unitary

`S e_gamma = (-1)^|gamma| e_gamma`.

Every one-prime creation/Volterra transition K changes the depth by exactly one. Therefore

`S K S = -K`.

Equivalently,

`S K = -K S`.

This is exact and independent of the prime sizes/weights, provided one transition adds exactly one distinct prime factor.

Freeze:

`MOBIUS_PARITY_IS_A_BIPARTITE_PATH_GAUGE`.

---

## 2. Signed and positive resolvents are unitarily conjugate

The gauge gives

`S(I+K)S=I-K`

and hence, on every finite nilpotent provenance truncation,

`S(I+K)^(-1)S=(I-K)^(-1)`.

Thus the alternating Möbius path dynamics is internally unitarily equivalent to positive factor-growth dynamics.

For a root-source vector `e_empty`, which is fixed by S,

`S (I+K)^(-1 e_empty = (I-K)^(-1 e_empty`.

The sign has merely moved from the state coefficients into whatever boundary observer is applied after the gauge transformation.

Freeze:

`SIGNED_INTERNAL_FACTOR_DYNAMICS != SOURCE_OF_RH_CANCELLATION`.

---

## 3. X6 residual polynomial under the parity gauge

Recall

`Q_5(K)=I-K+K^2-K^3+K^4-K^5`.

Then

`S Q_5(K) S = Q_5(-K)`
`=I+K+K^2+K^3+K^4+K^5`.

Since `S K^6 S=K^6`, the full X6 block factorization becomes

`S[(I-K^6)^(-1)Q_5(K)]S`
`=(I-K^6)^(-1)(I+K+...+K^5)`
`=(I-K)^(-1)`.

Therefore the local Z6/Möbius character projector is gauge-equivalent to a positive six-layer prefix sum.

Typed conclusion:

`LOCAL_Z6_MOBIUS_PROJECTOR` isolates parity in the declared factor-count character quotient, but it does not create a signed contraction inside the full provenance tree.

---

## 4. The dangerous mode is the parity resonance

The signed error equation has the formal structure

`(I+K)delta=q`.

Hence a long-lived parity mode corresponds to `K~-1`, not `K~+1`.

The residual polynomial satisfies

`Q_5(-1)=6`,

whereas it vanishes at the other sixth roots of unity.

Thus the X6 residual factor removes the five non-Möbius sixth-root characters and retains the unique `-1` parity resonance at full strength.

In finite nilpotent truncations this should be interpreted pseudospectrally/through the cyclic factor-count symbol, not as a literal eigenvalue claim.

Freeze:

`Q_5_ISOLATES_THE_DANGEROUS_PARITY_CHANNEL; IT_DOES_NOT_SUPPRESS_IT`.

Consequently a successful local source bound must show that the arithmetic prime-discrete source has small projection into the parity resonance itself.

---

## 5. Edge magnitude and sign are both internal coboundaries

For squarefree multiplicative weights of the form

`(-1) p^(-a)`

on an edge `m -> mp`, define the vertex gauge

`h(n)=mu(n)n^(-a)`.

Then

`h(mp)/h(m)=-p^(-a)`.

Thus the complete signed edge weight is an exact multiplicative coboundary on the ordered factor tree.

For the Riesz family, the `p^-a` magnitude was already identified as pure gauge, with the shell factor living at the endpoint. The present identity adds the Möbius sign to the same internal-gauge picture.

Freeze:

`FACTOR_TREE_EDGE_SIGN_AND_DIRICHLET_MAGNITUDE_HAVE_TRIVIAL_INTERNAL_HOLONOMY`.

This makes any attempt to obtain RH from a local factor-tree holonomy alone structurally impossible.

---

## 6. Squarefree local-X6 geometry has only arity information

On Möbius support every active exponent is one. For one local X6 block containing r distinct prime labels, `0<=r<=6`, the native factor geometry is always

`N_min=r`,
`L_E^2=r`,
`Kappa_F=0`,
`B_min=r!`.

Therefore two squarefree prime sets with the same local arity have identical native X6 metric/multiplicity data. Their distinction lies entirely in prime-label/prime-size provenance.

Freeze:

`LOCAL_X6_GEOMETRY_ALONE_CANNOT_DISTINGUISH_SQUAREFREE_PRIME_SETS_OF_EQUAL_ARITY`.

This is the local version of the earlier global shape-only compression no-go.

---

## 7. Where the non-gauge RH information resides

After the parity/magnitude gauge, the remaining nontrivial ingredients are:

1. endpoint product/log-budget constraint;
2. prime-size and ordered-prime provenance;
3. the shell/Riesz/hard-tail observer;
4. coherent collapse of many arithmetic Cell amplitudes into one scalar parity observable.

The final observer is not gauge-invariantly positive. Under S, a scalar all-Cell observer becomes the parity character on the positive factor state.

Thus the RH problem is a boundary coherence problem, consistent with the established Pair-BRC formulation

`H_x(-1) <= x^eps H_x(0)`.

Freeze:

`RH_INFORMATION_LIVES_IN_BOUNDARY/SHELL COHERENCE, NOT BARE FACTOR-TREE PROPAGATION`.

---

## 8. Updated smallest target

The block-resolvent source identity remains exact:

`R_pi-R_0=-G_pi Q_pi E R_0`.

But the parity gauge shows that neither `G_pi` nor `Q_pi` can by themselves generate the missing cancellation.

The smallest non-gauge object is now the boundary pairing

`<J_shell, G_pi Q_pi E R_0>`

or its adjoint form

`<Q_pi^* G_pi^* J_shell, E R_0>`.

The next useful theorem must exploit prime-size/order provenance inside this pairing and compare it to the intrinsic Pair-BRC collision norm.

Project frontier:

`PRIME_PROVENANCE_SHELL_BOUNDARY_COHERENCE`.

No claim here proves RH.
