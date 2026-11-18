# EC49DS — Complete general ten-step full-rank criterion for positive dual-BRC history observations

**Date:** 2026-11-01. **Evidence status:** AUTHOR_PROOF / EXECUTED_EXACT_CHECKS; PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED.

## Sources and native model

Frozen scientific input pins inherited from EC49DR: GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Existing predecessor commit: `b677db16f8df89f7f4add4f1053288adb8662c22`. Separately verified current behavioral main reads: global `c63187e27ebe3ddc47d2ee16a6e7222c126743ba`, Enterprise Math `b171147eb65e16c1bb9d4f2a2f20a3073897201f`, including P000, ACTIVE worldview and portable research protocol. No worldview or P000 changes.

Work in the fixed native six-axis signed X6 history observation model. A length-10 history ends at raw chart displacement `D=-2E1`, so four steps are positive and six negative. Positive-count vector `p=(p1,...,p6)` satisfies `Σp_i=4`. Positive channel weights are `X(p)=∏x_i^{p_i}`, `Y(p)=∏y_i^{p_i}` for arbitrary **strictly positive real** vectors x,y. Third instrument is unweighted path count. Retain the full signed ordered word and its provenance.

Let A mean adjacent positive steps `(+E1,+E2)`, B mean `(+E2,+E1)`. Following EC49DR, define six history features
`z=(¬A¬B,¬A B,A ¬B,A B,¬A∧last=+E1,¬B∧last=+E2)`.
The actual historical feature row is the 18-vector `M(w)=(X(p)z,Y(p)z,z)`. Auxiliary geometric instrument points below are only algebraic diagnostics; not native 2D ontology or Cell addresses.

## Theorem EC49DS-A — full rank iff an 11×3 instrument matrix has rank three

Define the 11 positive-count vectors
`C={(1,3,0,0,0,0),(2,2,0,0,0,0),(3,1,0,0,0,0)} ∪ {(1,2,e_j),(2,1,e_j):j=3,4,5,6}`,
where `(a,b,e_j)` means p1=a, p2=b and one positive step on off-core axis j. Let `G_C` be the 11×3 matrix with rows `(X(p),Y(p),1)` for p in C. Then, **for every x,y∈(0,∞)^6**,

`rank_R span{M(w): length(w)=10 and displacement(w)=-2E1}=18  ⇔  rank_R(G_C)=3`.

Equivalently, the 11 auxiliary multiplicative points `(X(p),Y(p))` are not all affine-collinear. All rank-defect parameters are cut out precisely by the 165 three-row determinants of this explicit polynomial matrix (before removing redundant minors).

**Sufficiency.** The included stdlib checker enumerates all 126 nonnegative p with total four and all genuinely reachable ten-step states with negative counts `p+2E1`; it finds exactly 333 distinct `(p,z)` pairs. For every one of the 11 vectors p in C it exhibits six real signed native paths having the same linearly independent features `e0,e1,e2,e3,e1+e4,e2+e5` (66 checkable ordered words). The verifier reconstructs all six displacement coordinates, positive multiplicities, both A/B flags and terminal ports. When three rows of G_C are independent, choose these six paths for each of the three p. Their 18×18 matrix is, after ordering, the Kronecker product of an invertible 3×3 instrument matrix and the invertible six-feature basis, with determinant `±(det G_3)^6≠0`.

**Necessity.** A history containing **both** A and B must have at least three positive steps on core axes 1 and 2 (pattern 121 or 212). Four positive steps in total imply that every such history has its count vector among exactly the 11 vectors in C. Therefore the projection of the entire history span onto the three coordinates `(X z3,Y z3,z3)` of the A∧B feature has image rank at most `rank G_C`. If `rank G_C≤2`, this projection cannot be all of R³ and the 18-dimensional history span cannot be full.

## Corollary EC49DS-B — explicit necessary and sufficient parameter classification

Write `u=x1,v=x2,U=y1,V=y2`. **The full history rank is below 18 precisely in the following cases**:

1. `u≠v, U=V`, and **all** y_i=U.
2. `u=v, U≠V`, and **all** x_i=u.
3. `u≠v, U≠V, uV=vU`, and all `y_i=λ x_i` with `λ=U/u=V/v`.
4. `u=v, U=V`, and the five auxiliary points `(u,U),(x3,y3),(x4,y4),(x5,y5),(x6,y6)` are affine-collinear (including vertical/horizontal lines).

**Proof.** The signed area of the three all-core multiplicative points from p=(1,3),(2,2),(3,1) factors as
`uvUV(u-v)(U-V)(vU-uV)` (using the displayed row order). When nonzero, three independent rows already prove full rank. For the zero cases: (1) the distinct core points lie on the horizontal line `Y=U^4`, and off-core points stay on this line exactly when each y_j=U; (2) by channel symmetry, the same argument gives the vertical line `X=u^4`; (3) the distinct core points lie on `Y=λ^4 X`, and each off-core point has `Y/X=λ³ y_j/x_j` so collinearity is equivalent to global proportionality; (4) the eleven points arise from the five stated points by the invertible diagonal linear map `(a,b)→(u³a,U³b)`, with duplicates. These exhaust all zeros of the core determinant, so the cases are necessary and sufficient by Theorem A.

In cases 1–3 the historical rank is **exactly 12**, as one BRC channel is constant or proportional to the other and each of six independent feature directions occurs with two distinct instrument vectors. In case 4, particular collinear nonconstant parameters have rank 17 (EC49DR), and finer defective-rank classification remains open.

**First newly resolved stratum.** If `x1≠x2` and `y1=y2=U`, full rank 18 holds **iff** some `y_j≠U` for j≥3; otherwise rank is 12. The three positive counts `(1,3),(2,2),(2,1,e_j)` give the explicit instrument determinant
`Δ=uv²(v-u)U³(U-y_j)`.
At x=(2,3,1,4,5,6), y=(7,7,11,7,7,7), Δ=-24696 and the constructed 18×18 determinant is -226860925160555001153847296 (=-24696^6). The program also checked all four off-core choices j=3..6 with exact Bareiss determinants using the companion local evidence archive.

## Executed exact checks

The accompanying executable `VERIFY_EC49DS_GITHUB.py` was run with Python standard library; it returned `PASS`, enumerated the 333 genuine states and 66 core path witnesses, and computed exact rational ranks for ten parameter examples: generic=18; y1=y2 but off-core y differs=18; all y equal=12; x1=x2 but off-core x differs=18; all x equal=12; front-channel-proportional but off-core not=18; globally proportional=12; equal core and noncollinear=18; equal core and collinear=17; all equal=6. The author-side full evidence archive additionally contains the independent `VERIFY_EC49DS.py` and `VERIFY_EC49DS_GENERAL.py`, complete JSON witness logs and checksums. Run `python3 VERIFY_EC49DS_GITHUB.py` to regenerate the 66 actual native words and ranks.

Scope: the theorem settles the **length-10 historical 18-feature row span**, with exact native signed path witnesses. The EC49DO six/five-feature **actual returning-future operator factorization**, universal-horizon lifting, and first-saturation minimality remain dependent on independent review. No physics/phase result or Foundation acceptance is asserted.

Gateway 0.6.11 status `research_authority_granted=false`. `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` before dispatch; owner inventory returned `CONTROL_QUOTA` (5/5 active jobs). No authenticated RA, CLAIM, Result or Driver review was written. This is source-backed portable author research in Draft PR #1730. Next question: `NEXT_EC49DT.md`.
