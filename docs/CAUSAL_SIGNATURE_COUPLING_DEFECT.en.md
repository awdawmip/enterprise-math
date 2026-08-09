# Causal Signature Coupling Defect — Deriving Coupling from Failure of Independent Future Signatures

Status: `ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE THEOREMS + EXECUTABLE REFERENCE`

## 1. Goal

Independent composition already satisfies

\[
\Sigma_{A\boxtimes B}=(\Sigma_A,\Sigma_B).
\]

This note asks what minimally appears when that product law fails. Correlation, mutual information, interaction matrices, tensors, and probability are not primitive. The first comparison is between what joint and marginal future signatures can actually distinguish.

## 2. Joint-to-marginal forgetting

Let `Q_A,Q_B` be marginal future-signature classes and `Q_AB` the full joint future-signature classes. Let

\[
R\subseteq Q_A\times Q_B
\]

be the marginal pairs actually reachable in the joint system. Forgetting cross-future information gives

\[
\rho:Q_{AB}\to R.
\]

For `r in R`, define

\[
\boxed{c(r)=|\rho^{-1}(r)|.}
\]

This is the number of causally distinct joint future states that the marginal future language identifies as the same situation.

## 3. CD-01 — Keep two coupling mechanisms typed

Reachability defect:

\[
\boxed{M_{AB}=|Q_A||Q_B|-|R|.}
\]

Signature-split defect:

\[
\boxed{S_{AB}=|Q_{AB}|-|R|=\sum_{r\in R}(c(r)-1).}
\]

Finite signature independence requires both to vanish:

\[
\boxed{M_{AB}=0\quad\text{and}\quad S_{AB}=0.}
\]

They must not be collapsed into one scalar. If only two of four marginal pairs are reachable but each reachable pair splits into two joint classes, then `|Q_AB|=|Q_A||Q_B|=4` while `(M,S)=(2,2)`. A raw cardinality difference falsely reports zero coupling.

## 4. CD-02 — Coupling spectrum is already P011

The forgetting map `rho` is itself a many-to-one causal collapse. Define

\[
\boxed{C_k(A:B)=\sum_{r\in R}\binom{c(r)}k.}
\]

Then

\[
\boxed{C_k(A:B)=J_k(\rho).}
\]

Hence the complete P011 collision spectrum exactly recovers the multiset of coupling multiplicities. In particular, `C_2` counts pairs of joint signature classes that become indistinguishable when cross-future information is forgotten.

Thus no new statistical spectrum is needed:

\[
\boxed{\text{coupling spectrum}=\text{P011 spectrum of cross-future forgetting}.}
\]

## 5. CD-03 — Integer chain law for staged forgetting

For

\[
Q_2\xrightarrow{q_{21}}Q_1\xrightarrow{q_{10}}Q_0,
\]

define

\[
D(q)=|\operatorname{dom}q|-|\operatorname{im}q|.
\]

When each stage is defined on the preceding reachable image,

\[
\boxed{D(q_{10}\circ q_{21})=D(q_{21})+D(q_{10}).}
\]

Higher-order collision changes use P011's exact merge-increment formulas rather than a forced scalar chain rule.

## 6. CD-04 — Pairwise zero does not imply higher-order zero

For three binary subsystems, retain only even-parity states

\[
000,011,101,110.
\]

Every pair realizes all four binary combinations and may have pairwise typed defect `(0,0)`, yet the three-way product has eight theoretical combinations and only four reachable ones:

\[
\boxed{(M_{ABC},S_{ABC})=(4,0).}
\]

This is a genuine three-body causal constraint invisible to every pair interaction summary.

## 7. CD-05 — Causal independence complex

For a coherent family of subsystem restrictions, collect the nonempty subsets whose future signatures factorize independently. Independence is downward closed, so these subsets form an abstract simplicial complex.

The ontology order is

\[
\boxed{\text{signature factorization}\to\text{independent subsets}\to\text{simplicial-complex shadow}.}
\]

The complex is derived, not assumed.

## 8. CD-06 — Irreducible coupling groups

A subsystem set `S` is irreducibly coupled when its signature does not factorize while every nonempty proper subset does. In the derived independence complex these are exactly the minimal nonfaces.

Define

\[
\boxed{\operatorname{ord}_{couple}=\min\{|S|:S\text{ is a minimal factorization failure}\}.}
\]

Order two gives genuine pair coupling; order three can exist while all pair coupling vanishes. A traditional interaction graph is only the order-two shadow, while a hypergraph is a conventional representation of all minimal nonfaces.

## 9. Relation to P011 and LEGO interaction

Two interaction layers are now distinct:

1. local LEGO interaction: a concrete response gets an irreducible extra effect when units coexist;
2. signature coupling: a subsystem group's complete future cannot be reconstructed from proper-subsystem futures.

Their equivalence is not assumed. A bridge theorem remains to determine when nonzero local interaction forces a signature factorization failure and whether the converse holds.

## 10. Linear shadow only

If the integer-linear joint future language contains all marginal probes, a free-rank shadow is

\[
\kappa_{free}=\operatorname{rank}(V_{joint})-\operatorname{rank}(V_{sep})\ge0.
\]

It counts new free independent distinctions but misses finite residue and reachability constraints such as parity coupling. Linear rank therefore remains a shadow, not the coupling ontology.

## 11. Executable assets

- `src/enterprise_math/causal_signature_coupling.py`
- `tests/test_causal_signature_coupling.py`
- `src/enterprise_math/causal_coupling_complex.py`
- `tests/test_causal_coupling_complex.py`

## 12. Next

1. prove or refute a two-way bridge between local LEGO interactions and signature-coupling minimal nonfaces;
2. derive multi-system composition laws;
3. reinterpret dimension contraction as deliberate forgetting of coupling signatures;
4. test whether P011 unifies irreversible collapse and cross-future coupling;
5. do not introduce tensor ontology unless causal composition itself forces a multilinear shadow.
