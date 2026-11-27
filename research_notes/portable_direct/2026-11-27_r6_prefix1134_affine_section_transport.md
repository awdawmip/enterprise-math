# PREFIX-1134 — Candidate-to-global affine section transport, with all three extra moments

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Inputs and scope

Continue PREFIX-1133 at 47059ee2c766e0d0975a1019db8c91408fdce201:research_notes/portable_direct/2026-11-27_r6_prefix1133_two_moment_exclusion.md; use PREFIX-1132 at eab9003f04bde31248d82d1a05ea90660d680819 and its uniform derivative certificate. Preserve frozen P000 V5 and companions at f42f2906d77f24085c123f3ccfe9667d41caa96d, signed reversal -5, 5q cover, O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. All coordinates in this note are auxiliary algebraic readouts of the existing signed X6 carrier. No new native axes, CT computation, anchor order, moment evaluation or Frobenius evaluation. The inherited Stage46 carrier correspondence, analytic boundary, root isolation and historical 8400/8800 process exit uncertainty remain conditions.

Global canonical entry blobs verified unchanged at 17c936b17643e4c8cbdaa361ec22bbcd805d68ee; Source continuation and portable protocol read on main. Actual LEASED inventory request r6-20261127-2052-leased-read SUCCEEDED/error=null, as_of 2026-11-27T12:53:51.526383Z, Source 40df4ee57c1e39f6c1faf6a668e031b60e50ff94, empty tasks and next_cursor=null. Historical registration receipt r6-20261123-2358-session-start-own-v1 SUCCEEDED; historical Activity RA-0ABD84561C86E53067DB0322 / EM-DIRECT-780BBE / TASK_RESEARCH read with 75 checkpoints (last PREFIX-1132). The current private session binding is unconfirmed. Independent continuation only; no new CLAIM, no borrowed identity, no task mutation. PREFIX-1133 and this note are not yet associated to Activity.

## 1. Transport theorem: a candidate enclosure is a reusable global observation

Let the true shared coefficient vector a belong to the frozen compact anchor. Let F=F_a and G_c(t)=beta(t)F''(t)+(alpha(t)-c)F'(t). At the true root t*, F(t*)=0 and G_c0(t*)=(c-c0)F'(t*), where c0 is the old fixed reference constant. Let A enclose F'(T) and D enclose G_c0'(T)-s1 F'(T), uniformly on the full shared anchor and old root interval T (as certified in PREFIX-1132). Define DG=D+s1 A, an enclosure of G_c0'(T). A is strictly negative. Let R,C be the refined PREFIX-1132 parameter intervals.

Choose one of the old candidate lines (q,p,h), set r=p/q and u=h/q and x=sqrt(36/(1+r)); x belongs to T by exact squared endpoint comparison. The PREFIX-1133 observer certificate encloses F(x), G_u(x) for every shared a at this fixed x,u: its uniform candidate rectangle includes the endpoint rho=r,c=u. Exclusion of the candidate does not invalidate that pointwise observer certificate. In particular the certificate can now be used for the actual a even when the actual rho,c are elsewhere in R,C. Append the three already certified rows for k=10000,10400,10800, retaining the same twelve shared columns. For true a the vector (F(x),G_u(x),0,0,0) belongs to the resulting outer zonotope Z=m+sum_j[-1,1]C_j+[-e,e], because the moment residual inequalities were included in e. No independence of moments and density observers is asserted. The units of m,C_j,e are 10^-125.

The exact root difference identity is t*-x=J(t*,x)(rho-r), J(t,x)=-x^2 t^2/[36(t+x)]. Both arguments are positive, and x^2 t^2/(t+x) is increasing separately in x and t, so J is contained in J_T=[-T_upper^3/72,-T_lower^3/72]. By the mean value theorem, for some A_1,A_2,A_3 in A and D_1 in DG,
    F(x)=-A_1 J(t*,x)(rho-r),
    G_u(x)=(c-c0)A_2-(u-c0)A_3-D_1 J(t*,x)(rho-r).
The second equality follows from G_u(x)=G_c0(x)-(u-c0)F'(x). This does not require a derivative bound with u changed; DG is the same frozen G_c0' certificate.

Take a0=mid(A), aJ=mid(A J_T), dJ=mid(DG J_T). Write the affine map
    L(rho,c)=(-aJ(rho-r), a0(c-u)-dJ(rho-r),0,0,0).
The two coordinate errors in replacing the original observation by L are bounded by
    E_F=mag(A J_T-aJ) mag(R-r),
    E_G=mag(A-a0) [mag(C-c0)+|u-c0|] + mag(DG J_T-dJ) mag(R-r).
The estimates are triangle inequalities on actual shared values. Hence L(rho,c) belongs to Z+[-E_F,E_F]e_1+[-E_G,E_G]e_2 for every admissible true parameter pair in R,C. Add ceil(10^125 E_F),ceil(10^125 E_G) to the existing two integer error radii before any further operation. Both payments are exactly one integer grid unit in this computation, including the independent outward-rounded verifier. This theorem avoids evaluating a new density polynomial at the midpoint or computing new derivatives: it converts existing candidate enclosures into uniform global affine constraints.

## 2. Complete section of the five-observer outer zonotope

For any integer n, the necessary condition becomes
    |10^125 n dot L(rho,c) - n dot m| <= sum_j |n dot C_j| + sum_i |n_i| e'_i.
All constraints are affine inequalities on the two auxiliary parameter coordinates (rho,c). The positive coordinate error axes make the enclosing zonotope full dimensional in the five observation coordinates. Every facet is supported by a normal orthogonal to four linearly independent generators, since an exposed face is a translate of the zonotope generated by the generators orthogonal to its normal. Thus signed primitive nonzero cofactor normals of four generator rows cover every facet. Enumerating additional normals is harmless. This gives the exact affine section of the stated outer model, not a claim of realizability in the original anchor or native dynamics.

Intersect the two old affine strips and the R,C box with the halfspaces for both former candidate reference enclosures. The 12 shared directions and five error axes are retained. The calculation is performed in centered parameter coordinates to avoid cancellation, using exact rational line/edge intersections. All 2380 four-row combinations per reference are inspected; 1995 are nonzero and 1086 are distinct primitive normal directions after orientation normalization. With the original exact input, the first reference produces 28 cuts and the second 14 cuts; the final convex polygon has 28 vertices. (The number of effective cuts depends on traversal order.) The exact-rational computation and the separately written cofactor-determinant verifier on outward rounded inputs both produce the same final vertex count and integer candidates.

Actual unrounded section marginal widths:
    rho: 3.46256873487984e-92 (previous 3.926109306591469e-92),
    c:   1.0445740869836953e-91 (previous 1.2670492031468278e-91).
Width of a thin normalized c-kappa*rho direction, kappa approximately 3.0160489167484763, is 2.464187835470509e-95. Previous single-moment band width 8.29154310287e-93: about 336.5 times tighter. The actual marginal gains are modest (1.1339 and 1.2130); the principal improvement is preservation of the joint direction. A simpler two-moment, single-normal transfer separately gave width 2.477843955965063e-95, identical integer survivor and dyadic starts. The three-moment section is the stronger outer model; the residual difference between these widths is small and no claim of further complete feasibility is made.

## 3. Exact integer-coordinate enumeration using the full parameter polygon

For all L>=L0=10^100 use inherited necessary inequalities (rho-p/q) in [0,K/L0^2], (h/q-c) in [0,H/L0], primitive gcd(p,q)=1, q>=q0, gap>=q. Constants q0=544447235321021556325566186117974922693, E=400000, K=d_upper+2E/q0 and H=2*d_upper+4E/q0 are as before. Therefore (p/q,h/q) belongs to the Minkowski sum of the certified parameter polygon and [-K/L0^2,0] x [0,H/L0]. Compute this sum exactly as the convex hull of each parameter vertex plus every rectangle corner (linearity/convexity proves equality). For an integer row (a,b,e), the coordinate n=aq+bp+eh=q(a+b*p/q+e*h/q); extrema on q in [q0,Q] and the convex polygon occur at the two q endpoints and polygon vertices. LLL only chooses a convenient basis; determinant and inverse are checked exactly, so complete coverage does not rely on LLL correctness. The V matrix and all numerical inputs are embedded in the standalone verifier.

At Q=3*10^61 the full integer box is [0,0] x [0,0] x [0,-1], hence empty. At Q=10^62 it is [0,0] x [0,0] x [-2,-1], exactly two points. Recover each integer triple using the unimodular inverse; test q range, primitive gcd and every edge inequality of the expanded convex polygon. Exactly one triple remains:
    q=39842427926119417299262046818826239782916070158838139476777507
    p=854223117766075752740545225414351655926157527291751525026511332
    h=3950018562885944348193743729715096500004840471989124645725608269
Consequently every true pair in any L>=10^100 window has gap>=q>=39842427926119417299262046818826239782916070158838139476777507. This is a necessary bound, not a constructed anomaly. With inherited sharp curvature q^2<4 E L/d for triple anomalies, and q<=sqrt(L) for close pairs, the first not-excluded fixed dyadic starts (base 10^8) are
    L3=15030672529752532658492675819451756975204368313013247172526662217806137760733494038167673589662519699404383846400000000
    L2=1970100309819723960613952005007180690253986963523272333397414670212286088574860530570713312744245782040331399515340800000000.
Both are 2 times the PREFIX-1133 bounds. Earlier windows retain their inherited coverage.

## 4. Verification and next problem

Verified manifests PREFIX1133_SHA256SUMS and PREFIX1132_SHA256SUMS for inherited artifacts. Executed cross_anchor.py, optimize_reference.py, affine_section.py and verify_section.py. The standalone verifier uses only Python standard library, independent recursive determinant (instead of inherited Bareiss), fixed integer coordinate basis (instead of LLL), outward rounded 10^-105 derivative/parameter intervals, 10^-125 strip payments, and embedded exact reference columns from the inherited compact certificate. It obtains 1086 distinct normals per reference, 28 section vertices per reference, the same two-point integer box and sole surviving line, with all assertions passing. This is an independent recalculation of the affine/section/enumeration layer conditional on inherited observer inputs, not an independent regeneration of the original BRC basis or anchor. Remote standalone verifier at a26d0589bb05b8c5fb07371840976426b27aa512:research_notes/portable_direct/2026-11-27_r6_prefix1134_verify_section.py, blob 904afd5377b70df5da82f38be8f55b0c3640c800 (matches local executed file).

Actual SHA256:
- verify_section.py d6a706f0d4f763e189a86f1f1eaf714d46e42145477a7a70d7a4de5e18e1d392
- verify_section.log ec4eeeb268e620a53aad6adddbc87a965ffb71cc8c1f850cd6e8aeaad6b9d245
- affine_section.py 94c5d720d78b7b5906b68413554bfc640edbb7fb70c064ce8418b2d6a8c45799
- affine_section.json 194c887fb2a1c58752d20ce83d302c23625916aaef66b8377e5eae726f0b2bf6
- affine_section.log c607ad080d0ecd1a2171c9975754cf72b6acf604d706e99e5cafc452fa0fa244
- cross_anchor.py af73cf992237199efbf1dc75f92d51b9cf97bc8bb05bf17f438eae35faf0be78
- cross_anchor.json e8fca033bd64f4d0d0d31399d96e5d40d6dae3d6e0067e98ed093cb1c813dd9b
- cross_anchor.log 5e66a9e1e6509ed5af94488e4c4b31929a4fd894b8ab461d09ad5085d53787ce

Next: test the one surviving triple in the actual shared-coefficient fiber, using the already computed extra moment rows together with a root- or higher-jet-specific observer. Establish feasibility or strict separation, rather than repeating the same five-observer outer section. The exact affine section model can guide a new original moment selection. Single endpoint m=47247757565973207955345875119021762026915609, true fixed-spectrum unbounded separation and B_fix,odd(32) remain open. No new finite endpoint certificate, independent review, or formal Task/Result claimed.
