# D25/LIFT — Rank-three repeated-eigenvalue gauge orbit theorem and all-rank Burnside certificate
2026-10-28. Status: AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. This is an **auxiliary finite-field** result, NOT a native H0/B0 experiment, original-class LIFT proof, Source checkpoint, or independent review.

## Carrier, source, and prior mathematical dependency
Reuse the previously author-proved commutator/trace-duality result Im(ad_A)=Z(A)^\perp and the full/proper rank-two gauge classifications. The original H0/B0 operator rank and permitted gauge group remain unknown at native Issue #1559.

Let k=F_q for any odd prime power q, A=diag(a,a,b) in M_3(k), a!=b, and K=[B,A]=BA-AB for a **source-marked** matrix B. All realized K are uniquely parameterized by X in k^2 (upper-right 2x1 block) and Y in (k^2)^* (lower-left 1x2 block):
$$K(X,Y)=\begin{pmatrix}0&0&x_1\\0&0&x_2\\y_1&y_2&0\end{pmatrix}.$$
The block-diagonal kernel of B->K is M_2(k) ⊕ M_1(k), dimension 5, hence each K has exactly q^5 source preimages. The image contains q^4 K. The **full** centralizer H=GL_2(k)x k^* acts as (P,t):(X,Y)->(PX/t,tYP^{-1}). The effective group is GL_2(k) acting (GX,YG^{-1}).

## Theorem A — complete (2+1)-block orbit classification
Define s=YX in k. The orbit of K under H is uniquely and completely classified by the marked/signed joint observer
$$(\mathbf{1}_{X\ne0},\mathbf{1}_{Y\ne0},s).$$
There are **q+3** orbits, with the following exhaustive disjoint types and exact sizes:

| type | number of orbits | size of each |
|---|---:|---:|
| X=Y=0 | 1 | 1 |
| X!=0, Y=0 | 1 | q^2-1 |
| X=0, Y!=0 | 1 | q^2-1 |
| X!=0, Y!=0, s=0 | 1 | (q^2-1)(q-1) |
| s in k^* | q-1 | q(q^2-1) |

Proof: Zero/nonzero of X and Y are invariant. GL_2 acts transitively on any nonzero X or nonzero Y alone. For both nonzero, first map X to e_1. Its stabilizer can send Y=(s,u) to (s,0) when s!=0 (shear), or Y=(0,u) to (0,1) when s=0 (nonzero diagonal rescaling). These transformations preserve s, and converse invariance is immediate. Given X!=0 there are q admissible Y for each s!=0; there are q-1 nonzero Y annihilating X when s=0. The orbit sizes sum to q^4. The B-source multiplicity follows from the five free diagonal-block entries. QED.

Crucially tr(K^2)/2 = s, so the scalar trace is complete **only on s!=0**. At s=0 it merges four distinct full-gauge orbits, erasing upper/lower source orientation and a nonzero-nilpotent joint relation. For a=0,b=1, the four explicit distinct auxiliary jets (X,Y)=(0,0),(e1,0),(0,e1*),(e1,e2*) all have s=0. They are not native Frobenius readings.

## Theorem B — partial scalar gauge and rank-independent exact counting
If the permitted gauge subgroup is restricted to scalar blocks diag(lambda I_2,t), with effective scalar ratio subgroup R={lambda/t}<=k^*, of order h dividing q-1, it acts freely on each nonzero (X,Y). Hence
$$N(A,H_{\rm scalar})=1+(q^4-1)/h.$$
For the maximal scalar ratio h=q-1, this leaves q^3+q^2+q+2 orbits instead of q+3 for full GL_2. Neither subgroup may be substituted for the other without a real source-normalization certificate.

For **arbitrary** r>=1, A in M_r(k), H<=Z_{GL_r(k)}(A), put z=dim_k Z_{M_r(k)}(A) and
$$\rho_g=\operatorname{rank}_k\bigl(B\mapsto [[B,A],g]\bigr).$$
The number of H-conjugation orbits on V=Im(B->[B,A]) is the exact integer
$$\boxed{N(A,H)={1\over |H|q^z}\sum_{g\in H}q^{r^2-\rho_g}.}$$
Proof: Since every g in H centralizes A, it preserves V under conjugation. The preimages in M_r(k) of fixed K in V are exactly ker(B->[[B,A],g]); each K has q^z B-preimages. Rank-nullity gives |Fix_V(g)|=q^{r^2-\rho_g-z}. Burnside's lemma yields the formula. No semisimplicity, abelian H, or rank-1/2 hypothesis is needed. This is an exact orbit-*count* certificate, not an individual signed representative or recovery of B. QED.

## Exact p=373 arithmetic and author checks
Conditional on the **auxiliary** rank-three (2+1) model: q^4=19,356,878,641 marked K; q^5=7,220,115,733,093 source B per K; full gauge 376 orbits; maximal scalar effective gauge 52,034,621 orbits. These large numbers come from universal formulas, **not** exhaustive p373 computations.

The attached standard-library checker ran and returned PASS: complete full-GL2 orbit partitions of F_p^4 for p=3,5,7,11,13,19 (176,630 states); complete scalar subgroup partitions for p=3,5,7,13; 720 deterministic source B commutator and trace checks including p373; and independent explicit double-commutator rank/Burnside sums at p=3,5,7 (GL2 orders 48/480/2016). Exhaustive finite checks prove only those finite cases; general claims rest on the preceding algebraic proofs. These are same-author validations, not an independent reviewer.

## BRC / native-world preservation and exact next source gate
BRC COMPOSE_APPLIED at the signed provenance level: retain (B,A,X,Y,K,H), apply the earlier commutator image and trace-dual map, and quotient to K/H **only** for the declared H-invariant observers and H-equivariant future operations. A merely positive weighted-mass BRC total is not the signed odd-square port. If actual fixed-class H0/B0 observes source-marked B or operations not descending to the quotient, keep the missing signed/source coordinate.

Issue #1559 remains PENDING_OWNER for authentic same-original-class p373 H0/B0 [X]U mod p², rank, normalized A, actual H, Frobenius, signed Green/Hesse and Delta_p-R_p. Once obtained, use this formula for that exact A,H; use the (2+1) theorem only if that type is actually verified. No proof of a native X6 state/readout bridge is supplied; ACTIVE P000 6D discrete Cell space plus independent time and native-plane prohibition are unchanged.

UR V2 remains a separate provenance task: original four-file bundle expected 94,687 bytes and SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 has not been byte-verified; no re-proof or declaration of published original. No current winning Source CLAIM/OPEN/checkpoint or independent mathematical admission is asserted.
