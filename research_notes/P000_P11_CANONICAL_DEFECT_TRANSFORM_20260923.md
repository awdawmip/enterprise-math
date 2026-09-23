# P000 P11 canonical defect transform and lossless k=1 ghost port

Status: `NONCANONICAL_PORTABLE_RESEARCH_NOTE / NO_CURRENT_CLAIM / NOT_SOURCE_CHECKPOINT / NOT_RESULT / UNREVIEWED`

Task: `RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC`

Publication: `TP2-FB7F5A1D6B6C6BCCD62D`

Contributor lineage: `EM-DIRECT-C4D02C`, stable conversation `em-auto-staggered-20260923-r11`, session `MCP-5ff2a3263c5c4ca2b556ebe8e47e5624`.

Research-Activity-ID: `RA-20260923-R11-P11-SCHUR-PFAFFIAN`.

This unit consumes the same-session staged TYPE-4 block form `M=[[C,H^T],[H,0]]`, the canonical torsion relation, the coordinate-free Schur decomposition, and on consecutive cores the exact ghost law `Mz=Delta`. It does not promote those staged inputs to Source theorem status.

## 1. Canonical defect transform

Let `U` be the P/Q selector space and let

`q: U -> U/im(H^T)`

be the quotient map. Define

`Phi: U -> im(H) direct-sum U/im(H^T)`

by

`Phi(z)=(Hz,q(Cz))`.

The source and target have equal dimension:

`rank(H)+(dim U-rank(H))=dim U`.

Moreover

`ker Phi = rad(C|ker H)`.

Indeed `Phi(z)=0` means `z in ker H` and `Cz in im(H^T)=(ker H)^perp`, precisely the radical condition for `C` restricted to `ker H`.

Consequently the coordinate-free nullity formula becomes

`k=dim ker(H^T)+dim ker Phi`.

Since the torsion mask `tau_R` is a nonzero element of `ker(H^T)`,

`k=1 iff ker(H^T)=<tau_R> AND Phi is an isomorphism`.

Thus the canonical Pfaffian bit `Omega=1` exactly when the R-incidence block has only the known torsion left relation and the transverse defect transform loses no P/Q valuation information.

## 2. Consecutive ghost ports are exactly Phi(z_U)

For the consecutive TYPE-4 identity `Mz=Delta`, write `z=(z_U,z_R)` and `Delta=(Delta_U,Delta_R)`. Then

`H z_U=Delta_R`,
`C z_U+H^T z_R=Delta_U`.

Passing the second equation to the quotient kills `H^T z_R`, giving the exact identity

`Phi(z_U)=(Delta_R,[Delta_U])`.

Therefore, for this operation, the exact compressed ghost port is the typed pair

`(Delta_R,[Delta_U] in U/im(H^T))`.

The deleted 3-mod-4 products `P^-`,`Q^-` remain source provenance generating `Delta`; they are not free Selmer coordinates.

## 3. Lossless branch theorem

If `Omega=1`, then `Phi` is an isomorphism. Hence the quotient defect pair uniquely reconstructs the active P/Q valuation vector:

`Omega=1 => (Delta_R,[Delta_U]) uniquely determines z_U`.

In the special subcase `Delta_R=0`, `z_U` lies in `ker H` and `[Delta_U]` is its symplectic dual under `C|ker H`. Thus

`Omega=1 AND Delta_R=0 => ([Delta_U]=0 iff z_U=0)`.

This contains the preceding strengthened obstruction as the singular case: if `z_U!=0` but both `Delta_R=0` and `[Delta_U]=0`, then `z_U` is a nonzero element of `ker Phi`, so `Omega=0`.

The BRC information statement is exact: on the `Omega=1` branch, quotienting `Delta_U` modulo `row(H)` is lossless for recovering `z_U` provided `Delta_R` is retained; outside that branch the information loss is measured exactly by `ker Phi=rad(C|ker H)`.

## 4. First off-boundary face d=2

When the cross-incidence has only the torsion left relation and `d=dim ker H=2`, the restricted alternating form `C|ker H` is either degenerate or symplectic. The whole `k=1` question is therefore the conjunction of:

1. `ker(H^T)=<tau_R>`;
2. `Phi` is bijective, equivalently `C|ker H` is nondegenerate.

This is the basis-free version of the earlier two-channel Pfaffian minor sum.

## 5. BRC boundary and next exact unit

Resolution: `COMPOSE_APPLIED / EXACT_OBSERVER_FACTORIZATION`.

The population remains provenance-labeled P/Q valuation coordinates plus R incidence and deleted-prime provenance. The operation is the `k=1/Omega` observer combined with the consecutive ghost law. The quotient defect pair is safe only under the proved interface; no global provenance collapse is authorized.

Next exact arithmetic unit: on the consecutive `d=2` face, control whether Euclidean-core reciprocity forces `Phi` to be invertible and `ker(H^T)` to be exactly the torsion line, or construct a genuinely proved infinite primitive family with those two properties. Finite examples are not an infinitude proof.
