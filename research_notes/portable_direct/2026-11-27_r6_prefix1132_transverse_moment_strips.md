# PREFIX-1132 — Transverse signed moment strips and exact integer-coordinate exclusion

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

Continuation of PREFIX-1131@a20dc66d0703778cc5825b015da539398a5ae4a2:research_notes/portable_direct/2026-11-27_r6_prefix1131_extra_moment_exclusion.md. Preserve frozen P000 V5 and companion pins at f42f2906d77f24085c123f3ccfe9667d41caa96d; signed reversal -5, 5q cover, O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. All coordinates here are auxiliary algebraic readouts of the existing signed X6 carrier. Inherited carrier correspondence, analytic boundary, root isolation and 8400/8800 command-exit uncertainty remain conditions. Global entry blobs verified unchanged at 3092af0acc00508f3d66d25f69ec6301aa286bea. Own registration r6-20261123-2358-session-start-own-v1 SUCCEEDED, EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322 / TASK_RESEARCH. Owner query r6-20261127-1854-leased-observe SUCCEEDED, error=null, LEASED tasks=[], next_cursor=null, fixed as_of 2026-11-27T10:55:29.831056Z, Source 6cdc7b061d6579d6993f2fbc30d396d9a5c29047. No CLAIM or shared Task mutation.

## 1. Moment-conditioned affine strip theorem

Retain the compact anchor a=a0+W z+diag(dr) e, |z_j|,|e_j|<=1, the frozen root interval T and the old marginal rho interval R. Let M be the additional k=10000 row from PREFIX-1131, with |M a-y|<=eps. Let F_a(t) be the six-column density, G_c0(t)=beta(t) F_a''(t)+(alpha(t)-c0)F_a'(t), with alpha,beta as in PREFIX-1124. True t* is a root, rho=36/t*^2-1 and G_c0(t*)=(c-c0)F_a'(t*). For fixed s,w define the signed observer Q=G_c0-sF_a+w(M a-y). Compute the point interval B at x by summing shared anchor columns before absolute values and then adding |w|eps. Equivalently B encloses Q(x)-w(M a-y) for the true coefficients, but with the extra moment constraint used to bound the combined expression: more precisely B encloses Q(x)-w u for all |u|<=eps, with Q evaluated on the same a. Retaining the extra row in the point evaluation is essential for the tight bound. At u=M a-y, Q(t*)-w u=G_c0(t*). The derivative with respect to t is independent of the constant moment row. Let A enclose F_a'(T) with A_upper<0 and D enclose G_c0'(T)-sF_a'(T), both over the entire shared anchor. By the mean value theorem, the exact root relation t*-x=J(t*) (rho-rho_x), J(t)=-x^2 t^2/[36(t+x)], rho_x=36/x^2-1, gives

    c-c0 in B/A + (D J(T)/A)(rho-rho_x).

Thus for any rational kappa, c-kappa*rho-i belongs to P, with P=B/A+(D J(T)/A-kappa)(R-rho_x), i=c0-kappa*rho_x; moving the midpoint of P into i makes the strip symmetric. All interval operations are outward; no Taylor truncation of the root relation is needed. The root and moment terms vanish with their declared payment only at the true coefficients, and the derivative bound is uniform. No independent-coefficient reboxing replaces the signed columns.

## 2. Actual computation and intersection

Use the common integer normal of PREFIX-1131, s=-n1/n2, w=n3/n2. Reuse the compressed 9600 anchor and the same 301-term Frobenius basis and majorants. The code affine_moment.py uses fixed 10^180 outward arithmetic, with product-rule tail payments through derivative order three and full k=10000 moment error on grid 10^125. The actual result is B approximately [-1.32487648533336e-81,-1.24553277246977e-81], A strictly negative (about -9.56923360094e9), D about 1.02265613419677e12. The new slope kappa1=3.016048916748476... and symmetric strip half-width about 4.145771551435e-93. The old PREFIX-1128 strip has kappa0=4.799830397021008..., half-width about 3.09e-92. The two strips are transverse: subtracting their signed residuals gives rho=(i1-i0+P1-P0)/(kappa0-kappa1). Consequently the new certified rho width is 3.926109306591469e-92 (old 2.7732676e-88), and c width is 1.2670492031468278e-91 (old 1.33105962e-87). The improvement uses already computed moments, not new anchor orders. All quantities are derived from the same true a; no independence of the two strips is assumed.

For standalone verification, floor the two kappa and i values to grid 10^-105; increase each residual interval outward by 24 units beyond outward endpoint rounding. This covers the change in kappa*rho+i because 0<rho<23. Exact rounded constants are embedded in verify_affine.py. That program independently recovers the intersection without using the previous rho and c marginal boxes. It gives widths 3.926109306596967e-92 and 1.2670492031489694e-91.

## 3. Complete integer enumeration

For every dyadic window L>=L0=10^100, a real near-integer pair has primitive relation (q,p,h) with gcd(p,q)=1, q>=q0=544447235321021556325566186117974922693, rho-p/q in [0,K/L0^2], h/q-c in [0,H/L0], E=400000, K=d_upper+2E/q0, H=2*d_upper+4E/q0. Therefore each strip gives h/q-kappa_j*p/q-i_j in P_j+[0,kappa_j*K/L0^2+H/L0]. Intersect both necessary constraints and the marginal intervals from section 2. For any integer row (a,b,e), n=aq+bp+eh=q[a+e*i1+(b+e*kappa1)*p/q+e*Z1]. Evaluate the extrema at all eight box corners; they are exact extrema of a multi-affine function. Choose a unimodular coordinate basis by exact rational LLL (only a search heuristic), then verify its determinant and inverse independently. With Q=3*10^61 the basis V is the integer matrix in verify_affine.py. Its determinant is +1. The full integer coordinate box is [0,1] x [1,3] x [-1,1], only 18 points. Complete reconstruction and filtering leaves exactly two lines:

    (11683574750891413984657341351634642396627294140163853575356389,250496271684704456789864385473555542316596430679353898870073745,1158321406327547828091494440216978860103654272622040749268565997)
    (28144493615342431594866414809513979189292928865838104066721338,603418976590135788771788168814147453537399664183017637106295295,2790273535281900553809121468163949060112834020925997672240824347).

Exact independent Fraction enumeration on the outward-rounded strip constants gives precisely the same two lines, same determinant and same box. The earlier caps 3*10^60 and 10^61 have 0 and 1 coordinate points respectively and no candidates in the unrounded run. The new lower bound q>=q_min=11683574750891413984657341351634642396627294140163853575356389 holds for the entire L>=10^100 tail, conditional on inherited Stage46 premises. No claim that the two surviving lines are attainable is made. Using q^2<4 E L/d for three anomalies and q<=sqrt(L) for close pairs gives the first not-excluded fixed dyadic window starts:

    L3=939417033109533291155792238715734810950273019563327948282916388612883610045843377385479599353907481212773990400000000
    L2=246262538727465495076744000625897586281748370440409041674676833776535761071857566321339164093030722755041424939417600000000.

Each is 16 times the PREFIX-1131 cap-based bound. Earlier windows retain their existing certificates. These are new exclusion bounds, not observed anomalies.

## 4. Evidence and recovery

Actual runs: python affine_moment.py, python scan_moment.py, python verify_affine.py completed normally. Inherited archive PREFIX-1131-execution-evidence.zip manifest was checked successfully. Reuse its inputs by unprefixed names. Core executed files and outputs SHA256:
- affine_moment.py c024add4c1b0f7ec5c5e7a520faaf86e2ff2b2623882294702fe08edb5ebeb64
- affine_moment.json 5766db7668ec49bb231a4095427b9dcbfa03ad71492c8e76549ba6ad0c2b0a6c
- scan_moment.py 4864a906c72833d7ff8ceb83d804dec3a4fc30e52b604fc4eb0858015052ce97
- scan_moment.json f7e45b45c49d7eef4abad0bdda58d14866b2be635e62a00d8032b20647a71569
- verify_affine.py 763f14f917429fe764ae813face75fce64c56f9955a252c8f9124cb72e54cd0b
- verify_affine.log 14c952d850aa2be892f5d645257e09a4a1ee16e236b0c4e0bf55bb2695236892.

Remote executed affine code 21e8b244c2422757b070fced2c57f131587ec54b:research_notes/portable_direct/2026-11-27_r6_prefix1132_affine_moment.py (blob 5a4053088c3933d010a129baf9a78d6fefcddbf3); standalone verifier 238f4e6080a780267a1d70f372e997bef96d18a2:research_notes/portable_direct/2026-11-27_r6_prefix1132_verify_affine.py (blob cee1bad8ebc7fac791ebbe058b9502beb9bc6779). Both exact immutable readbacks matched local Git blob. The full local archive includes all source inputs, outputs, logs and code. Exploratory multiple_moment.py (10400/10800 directions) timed out after basis ready, no new result; retain as incomplete and do not claim it ran. Next: use the two remaining exact lines, test the full shared anchor plus k=10000 moment fiber and then k=10400/10800 if needed; choose cheaply normalized rational coefficients and avoid expensive uncontrolled rational denominators. No need to recompute any high-order anchor. Remaining single integer endpoint m=47247757565973207955345875119021762026915609, unbounded true fixed-spectrum separation and B_fix,odd(32) remain open. Independent review and Activity observation audit pending.
