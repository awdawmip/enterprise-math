# P000 P11 — fixed-2-twist Galois eigenspace no-transfer

Status: `PORTABLE_RESEARCH_NOTE / NO_CURRENT_CLAIM / NOT_SOURCE_CHECKPOINT / NOT_RESULT / UNREVIEWED`

Task: `RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC`
Contributor lineage: `EM-DIRECT-C4D02C`
Stable session: `MCP-5ff2a3263c5c4ca2b556ebe8e47e5624`
Frozen task/source pin consumed: `73c755c7754e29246afd48f992f6b1c905a7b580`

This note consumes without promotion the same-session staged target model
\[
E:W^2=X(X-P^2)(X-Q^2)
\]
and the preceding portable all-core theorem that
\[
E^{(2)}:y^2=x(x-2P^2)(x-2Q^2)
\]
has the infinite-order rational point
\[
R_2=(4C^2,4PQC).
\]

Let `K=Q(sqrt(2))` and let `sigma` be its nontrivial Galois involution. Over `K`,
\[
\psi:E_K\to E^{(2)}_K,\qquad (X,W)\mapsto(2X,2\sqrt2 W)
\]
is an isomorphism.

Define
\[
E(K)^+=\{P:\sigma P=P\},\qquad E(K)^-=\{P:\sigma P=-P\}.
\]
Then
\[
E(K)^+=E(Q),
\]
and `psi` identifies `E(K)^-` exactly with `E^(2)(Q)`: the sign change on `sqrt(2)` cancels the sign change of the anti-invariant `W` coordinate. The intersection is
\[
E(K)^+\cap E(K)^-=E(Q)[2].
\]

The inverse image of `R_2` is
\[
S_2=(2C^2,\sqrt2\,PQC)\in E(K)^-,
\]
and has infinite order. Hence for every nonzero integer `n`,
\[
\boxed{nS_2\notin E(Q)}.
\]
Indeed, rationality would give `sigma(nS2)=nS2`, while anti-invariance gives `sigma(nS2)=-nS2`; then `2nS2=O`, contradicting infinite order. Moreover
\[
\boxed{\operatorname{Tr}_{K/Q}(nS_2)=nS_2+\sigma(nS_2)=O}.
\]
Thus neither integer multiples nor Galois trace transfer the uniform twist direction into the rational target port.

After tensoring with `Q`, the involution is diagonalizable and the exact plus/minus identifications give
\[
E(K)\otimes Q=(E(Q)\otimes Q)\oplus(E^{(2)}(Q)\otimes Q),
\]
so
\[
\boxed{\operatorname{rank}E(K)=\operatorname{rank}E(Q)+\operatorname{rank}E^{(2)}(Q)}.
\]
The preceding theorem therefore guarantees only
\[
\operatorname{rank}E(K)\ge\operatorname{rank}E(Q)+1,
\]
not positive rank on `E(Q)`. This is fully compatible with same-session staged target cores for which the target 2-descent forces rank zero: the guaranteed extension direction is purely anti-invariant.

BRC consequence: the Galois eigencharacter is a required repair coordinate. Forgetting it merges the rational/invariant and twist/anti-invariant Mordell-Weil directions and is unsafe for the P11 rational-point observer.

This note makes no claim about a deeper relation between the two 2-Selmer groups. The next exact unit is to normalize the common full-2-torsion Galois module and compare local Kummer images at `2`, `P`, `Q`, and `R=oddpart(AB)` without identifying coordinate triples across the twist before the cohomological normalization is proved.
