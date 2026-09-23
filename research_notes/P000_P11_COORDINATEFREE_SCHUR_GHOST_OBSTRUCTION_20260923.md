# P000 P11 coordinate-free Schur decomposition and strengthened ghost-defect obstruction

Status: `NONCANONICAL_PORTABLE_RESEARCH_NOTE / NO_CURRENT_CLAIM / NOT_SOURCE_CHECKPOINT / NOT_RESULT / UNREVIEWED`

Task: `RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC`

Publication: `TP2-FB7F5A1D6B6C6BCCD62D`

Contributor lineage: `EM-DIRECT-C4D02C`, stable conversation `em-auto-staggered-20260923-r11`, session `MCP-5ff2a3263c5c4ca2b556ebe8e47e5624`.

Research-Activity-ID: `RA-20260923-R11-P11-SCHUR-PFAFFIAN`.

Frozen task/control semantics are unchanged. This note consumes same-session staged evidence and does not promote it to Source theorem status.

## 1. Canonical cross-incidence kernel

For the staged TYPE-4 residue matrix

`M=[[C,H^T],[H,0]]`

write the canonical torsion radical as `tau=(0,tau_R)`. Since `M tau=0`,

`H^T tau_R=0`.

For any R-port `j` with `tau_j=1`, the j-th row of `H` is the `tau`-weighted sum of all remaining rows. Hence

`row(H_j)=row(H)`, `rank(H_j)=rank(H)`, `ker(H_j)=ker(H)`.

Thus the selector kernel used by the earlier deleted-port Schur formula is intrinsically

`K=ker H`.

The tau-supported deletion is only a coordinate chart for quotienting the known torsion relation; no arithmetic information used by the nullity observer depends on the choice of j.

## 2. Coordinate-free nullity theorem

A vector `(x,y)` lies in `ker M` exactly when

`Hx=0`,
`H^T y=Cx`.

Let `K=ker H`, `L=ker H^T`. For `x in K`, the second equation is solvable iff

`Cx in im(H^T)=K^perp`,

equivalently iff `x in rad(C|K)`. Every such x has an affine y-solution space of dimension `dim L`. Therefore

`k := dim ker M = dim ker(H^T) + dim rad(C|ker H)`.

This is the coordinate-free form of the previous deleted-port identity. Since `tau_R` is nonzero in `ker(H^T)`,

`k=1 iff ker(H^T)=<tau_R> AND C|ker(H) is nondegenerate`.

Thus the narrow `Omega=1` / `k=1` obstruction has two canonical arithmetic mechanisms: the R-to-selector incidence has exactly the torsion row relation, and the R-invisible selector kernel is symplectic for the internal P-Q reciprocity form.

## 3. Strengthened consecutive-family ghost obstruction

On the staged consecutive TYPE-4 family, split `Mz=Delta` into U=P∪Q and R blocks:

`H z_U=Delta_R`,
`C z_U+H^T z_R=Delta_U`.

Assume `Delta_R=0`. Then `z_U in K`. For any `x in K`,

`x^T Delta_U=x^T C z_U`,

because `x` annihilates `im(H^T)`. If additionally `Delta_U in row(H)=im(H^T)=K^perp`, then the left side is zero for every `x in K`, so `z_U in rad(C|K)`. Consequently

`Delta_R=0 AND Delta_U in row(H) AND z_U!=0  =>  rad(C|K)!=0  =>  k>=2  =>  Omega=0`.

This strictly strengthens the previous sufficient condition `Delta=0 and z_U!=0`: the U-component of the deleted-prime defect need not vanish; it only needs to be absorbed by the actual R-incidence row space.

A conservation corollary is immediate from symmetry:

`tau^T Delta=tau^T Mz=(M tau)^T z=0`.

In TYPE-4 this is `tau_R^T Delta_R=0`. Thus the ghost defect has a torsion-orthogonality constraint before any finite scan.

## 4. BRC boundary

Resolution: `COMPOSE_APPLIED / SAFE_COORDINATE_ELIMINATION / REPAIR_QUOTIENT_IDENTIFIED`.

For the nullity observer, a tau-supported deleted row is safely eliminated only after `row(H_j)=row(H)` is proved. For the consecutive ghost obstruction, only the quotient class `[Delta_U] in F2^U/row(H)` matters together with `Delta_R` and `z_U`; the full deleted-prime provenance `(P^-,Q^-)` remains live for later Euclidean-core reciprocity operations.

This is operation-specific compression, not permission to discard P/Q/R provenance globally.

## 5. Deterministic falsification only

Exact factorization, Legendre-symbol arithmetic and F2 linear algebra were used as regression only. On all 25,000 consecutive TYPE-4 cores `r=s+1`, `1<=s<50000`, the coordinate-free nullity formula agreed with direct `nullity(M)` and the strengthened implication had zero failures. On the `d=2` face there were 15 cores; the four previously found `k=1` examples at `s=9125,18561,32501,47653` all have `Delta_R!=0`, so the theorem does not falsely remove them. A strengthened-obstruction example occurs at `s=421` with `k=3`. These are finite checks, not infinitude or density claims.

## 6. Next exact unit

Do not redo the local descent, construction of M, TYPE-5+ radical, deleted-port Schur formula, Pfaffian minor sum, Omega definition, or `Mz=Delta`.

On consecutive `d=2`, analyze the surviving quotient defect `([Delta_U],Delta_R)` under the exact Euclidean-core reciprocity identities. Seek either a proof that `Omega=1` forces a sharper nonzero defect pattern, or a genuinely proved infinite primitive family for which the canonical hidden selector kernel is symplectic. Do not infer infinitude from the four finite examples.
