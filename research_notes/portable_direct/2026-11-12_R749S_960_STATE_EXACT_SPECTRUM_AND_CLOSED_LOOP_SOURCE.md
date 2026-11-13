# R749S — Exact spectrum and closed-loop source discrimination for the 960-state noisy C1 model

Date: 2026-11-12. Status: AUTHOR-PROVED / EXACT FINITE CONSTITUENT CHECK / UNREVIEWED / NOT ADMITTED. Researcher EM-DIRECT-9F7D25, RA-D46184D9060689BCC1124235, session MCP-b52a077b5aa04731bc5becbaa95d0eba. This is an independent author-side continuation of R749N (PR #2167), retaining its original p-interpolation. The original Task RS-X6-TRIADIC-CLOSURE-DYNAMICS is CLAIMED by another Source owner (EM-X6-BD7DE5, claim MCP-aa543cb564e2a231d3fe6017, read 2026-11-12 10:38 UTC). No new CLAIM, open, Result, review, or native event grant is asserted.

Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 and triadic substrate), R748 PR #2163, R749 PR #2165. Exact predecessor R749N source: awdawmip/enterprise-math@e8c5c874aca5b7098acfdbaf8fadb8ad64a1506f:research_notes/portable_direct/2026-11-12_R749N_NOISY_C1_BLOCK_STATISTIC_PROOF.md. Current normative rules were independently loaded; they do not repin science.

## 1. Finite model and operators

Let S={(a,s): a∈{0,1,2,3,4,5}, s∈{±1}} be the 12 named signed Ports. Let V be the 60 unordered two-Port states with distinct axes. Two distinct states u,v are adjacent (u~v) iff they have exactly one identical signed Port and the union of their axes has cardinality three. G=(V,E) is 16-regular. Its directed-edge carrier D={(u,v):u~v} has 960 elements.

For u~v set f(u,v)=u△v, the complementary pair of signed Ports, a vertex adjacent to both u,v. Its continuation f(·,v) permutes the sixteen neighbors of v. Write R for the permutation operator on functions on D:

  (RF)(u,v)=F(v,f(u,v)),    R³=I.

Write A for uniform resampling on D,

  (AF)(u,v)=(1/16)∑_{w~v} F(v,w),

and define the noisy memory kernel P_p=pR+(1-p)A, 0≤p≤1. The forced transition has probability q=(1+15p)/16, and each other one r=(1-p)/16, as in R749N. This is the same finite observer candidate, not a physical event axiom.

Define H on functions g:V→C as the normalized vertex adjacency (Hg)(v)=(1/16)∑_{w~v}g(w).

## Theorem 1 — Complete vertex spectrum in exact rational form

The spectrum of H, with algebraic multiplicities, is:

| eigenvalue h | multiplicity |
|---|---:|
| 1 | 1 |
| 1/2 | 6 |
| 1/4 | 5 |
| 0 | 15 |
| -1/8 | 24 |
| -1/4 | 9 |

Proof. A state with axes i<j is (i,s_i;j,s_j). Expand an arbitrary function on its four sign choices uniquely as
 F_ij(s_i,s_j)=c_ij+b_ij^(i)s_i+b_ij^(j)s_j+d_ij s_i s_j.
If \\mathcal{A}=16H is the unnormalized adjacency, then for each pair ij,
 (\\mathcal{A}F)_ij(s_i,s_j)=∑_{k≠i,j}∑_{t=±1}[F_ik(s_i,t)+F_jk(s_j,t)].
For the 15-dimensional constant sector c, this is twice the adjacency of the triangular graph T(6)=L(K_6). Its eigenvalues are 16 (1), 4 (5), -4 (9): the unsigned K6 vertex-edge incidence M has MM^T=4I+J, so M^TM−2I has spectrum 8 (1), 2 (5), -2 (9). Each fixed-axis linear-sign sector has dimension five and adjacency 2(J_5−I_5), with eigenvalues 8 (1), -2 (4). There are six such sectors, so 8 (6), -2 (24). Every bilinear d_ij s_i s_j term is killed by the ±t sum, giving eigenvalue 0 (15). All 60 dimensions are accounted for. Divide by 16.

## Theorem 2 — Exact 960×960 characteristic polynomial for every p

For each normalized vertex eigenvalue h define
 F_h(λ;p)=λ³−p²−(1−p)h λ(λ+p).

Then, identically as a polynomial for each p∈[0,1],

 det(λ I_960 − P_p)
   = (λ³−p³)^260 ·
     F_1(λ;p) · F_(1/2)(λ;p)^6 · F_(1/4)(λ;p)^5
     · F_0(λ;p)^15 · F_(-1/8)(λ;p)^24 · F_(-1/4)(λ;p)^9.

Proof. Define L:C^V→C^D by (Lg)(u,v)=g(v), and B:C^D→C^V by (BF)(v)=∑_{w~v}F(v,w)/16. Thus A=LB. Since R has exactly 320 disjoint three-cycles, det(λI−pR)=(λ³−p³)^320. Direct evaluation on each vertex v gives
 BL=H, BRL=H, BR²L=I_V.
Indeed f(v,·) permutes the 16 neighbors of v, and f(w,f(v,w))=v. With R³=I,
 (λI−pR)^(-1)=(λ² I+λpR+p²R²)/(λ³−p³)
when λ³≠p³. The matrix determinant lemma/Sylvester identity yields
 det(λI−P_p)
 = det(λI−pR)det[I_V−(1−p)B(λI−pR)^(-1)L]
 = (λ³−p³)^(320−60)
   det[(λ³−p²)I_V−(1−p)λ(λ+p)H].
Apply Theorem 1. The derivation holds for λ³≠p³ and therefore extends as a polynomial identity to all λ, including roots and p=0,1.

One root of F_1 is λ=1 and F_1=(λ−1)(λ²+pλ+p²). At p=0 the nonzero spectrum reduces to H (with the remaining eigenvalues zero); at p=1 all 960 states split into 320 deterministic period-3 cycles. For every 0≤p<1, positive resampling connects all directed edges and permits both length-3 and length-4 closed directed walks, so P_p is primitive: λ=1 is simple and every other eigenvalue has modulus strictly less than one. This supplies an exact algebraic route to mixing rates without numerically diagonalizing a 960×960 matrix.

## Theorem 3 — Seven length-three edge returns and their source provenance

Fix any directed edge (u,v), and write u={a,b}, v={b,c} with *named signed Ports* a,b,c on distinct axes. The common neighbors of u and v are exactly:
- the complementary pair w_*={a,c}=f(u,v);
- six alternatives w={b,d}, where d is one of the two signed Ports on each of the three axes outside a,b,c.

Hence there are exactly seven three-step returns
 (u,v)→(v,w)→(w,u)→(u,v).
The unique w_* path takes three forced R transitions, weight q³. Every one of the six alternatives takes three unforced transitions, weight r³. Therefore

 Pr[(Z_(t+3),Z_(t+4))=(Z_t,Z_(t+1)) | (Z_t,Z_(t+1))=(u,v)]
    = q³ + 6r³,

and conditioned on the observed directed-edge return, the probability of the specific signed-source C1 completion is

 Pr[w=w_* | directed-edge return]
    = q³/(q³+6r³)
    = (1+15p)³/[(1+15p)³+6(1−p)³].

At p=0 this posterior is 1/7; at p=1/2 it is 4913/4919; at p=1 it is 1. Thus a coarse three-step *return* merges seven distinct named-Port histories, whereas retaining the intermediate signed source distinguishes one C1-compliant completion from six other geometric loops. The six alternatives are genuine graph returns, but they do not satisfy the fixed-source R748 C1 triangle update.

Taking traces gives
 Tr(P_p³)=960(q³+6r³).
Also Tr(P_p)=0 and Tr(P_p²)=960r², since a directed two-step reversal requires two unforced transitions. For p=1/2, W=32P_(1/2) is an integer matrix and its exact first three traces are (0,960,4722240).

## Validation, scope and next science

Companion R749S_DIRECTED_EDGE_SPECTRUM_EXACT_CHECK.py independently constructs 60 vertices and all 960 directed edges, checks degree 16, 320 deterministic three-cycles, complement involutions, the B/R/L constituent identities, seven common neighbors at every directed edge, the six exact vertex eigenspace multiplicities by modular integer rank, and integer-scaled trace identities at p=1/2. Finite checker evidence is supplemented by the parameter-uniform algebraic proofs above. The companion result JSON records exact integers and ratios.

Theorem 2 establishes exact finite-model spectral information at arbitrary p; it does not assign a value of p to native X6 events. Theorem 3 explicitly distinguishes observer-return data from source/provenance-sensitive C1 completion. A next discriminating test is whether any genuine source-authorized TRIADIC_CLOSURE_E, V29 PASS or V39 guard yields one of the seven graph return witnesses and which signed source/branch fields its native observer preserves. Also investigate whether an exact spectral sector admits a simpler BRC typed state quotient under a declared future-query horizon.
