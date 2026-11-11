# R62 — Exact selective latest-source membership and circular anchor transport

Date: 2026-11-11. Frozen S23/AV science pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Direct author continuation from R61 Draft PR #2055, head `358023379ffe8016b8856d83b8440c8bad2ffc0f`; R60 #2054. Scope: exact labelled circle-rotation auxiliary observer, under unchanged P000 and native X6 semantics. Status: author-proved mathematics and finite exact computation, independent review pending.

## R62-A: a selected label needs only its candidate and newer ages certified

Let m >= 1, 0 < theta < 1. Historical boundary b_z(theta) = {z theta} retains original label z (z=0,...,m-1). Arc A_z(theta) is the counterclockwise half-open arc from b_z to its immediate cyclic successor. Let R be a finite set of distinct positive source ages r=j-t, with observed source phase v_r(theta) = {x(theta)-r theta}, and let tau_z(theta)=min{r in R: v_r(theta) in A_z(theta)}, or EMPTY if there is none.

Let I=[p/q,(p+1)/q] in (0,1), q>0. The observer phase is affine x(theta)={alpha+beta theta}, where alpha=A/B is rational, B>0, beta is an integer. Suppose the original historical boundaries have one strict cyclic order throughout I; write h_z for the original index of the successor of z. Choose theta0=(2p+1)/(2q), compute a_z=tau_z(theta0), and define the relevant source ages:

R_z = {r in R: r <= a_z}, if a_z != EMPTY; otherwise R_z=R.

**Theorem.** If for every r in R_z and h in {z,h_z}, the function

    F_(r,h)(theta) = alpha + (beta-r-h) theta

does not equal an integer anywhere on the closed interval I, then

    tau_z(theta)=a_z   for every theta in I.

**Proof.** On a strict fixed circular order of the history boundaries, the continuously moving source v_r can change membership in A_z only by crossing its entry or exit boundary b_z or b_(h_z). Such a crossing is precisely F_(r,h)(theta) in Z. The certified source-age prefix therefore has constant membership in A_z on the connected interval I. If a_z exists, it remains a member and every younger age remains outside, so no older age can improve the minimum. If a_z is EMPTY, the relevant set contains all sources and they remain outside. QED.

**Exact endpoint certificate.** Write d=beta-r-h. Define D=Bq, N0=Aq+Bdp, N1=Aq+Bd(p+1). For d != 0, noncollision on the *closed* I is equivalent to:

    floor(N0/D) = floor(N1/D)
    N0 mod D != 0, N1 mod D != 0.

This follows because F is affine and takes all intermediate values. For d=0, noncollision is alpha not an integer; permanent equality requires its own tie-handling convention and is excluded from the strict certificate. A sufficient common history-order test uses, for each 1<=d<m, r_d=(d p) mod q and min(r_d,q-r_d)>d. This is the R61-C interval-order bound restricted to historical boundary differences.

**Scope and costs.** Once the initial answer, boundary order and source list are available, the certificate requires exactly 2|R_z| integer boundary tests for this queried label, not tests on all older sources. Acquiring a_z, creating the index, parameter enclosure, and constructing/sorting historical boundaries are separate costs. Integer bit lengths depend on log(qB), log(|d|+1), and the numerator sizes; the word-level check count does not itself establish a total bit-runtime speedup. A sparse latest-only quotient is safe for this read; a future arbitrary deletion requires retaining original source identities and the persistent carrier.

## R62-B: exact sparse/full separation within the frozen enclosure

Set p=262204504569236716045286, q=10^24. Choose m=2, j=0, x=0, R={1,q}. For every theta in I, 0<theta<1/2, history arcs are A_0=[0,theta), A_1=[theta,1). Age 1 has phase {-theta}=1-theta in A_1; hence tau_1(theta)=1 uniformly.

Set theta1=(4p+1)/(4q), theta2=(4p+3)/(4q), both strictly interior. Age q has phase {-q theta1}=3/4 in A_1, but {-q theta2}=1/4 in A_0. Therefore the full latest-age vectors are:

    tau(theta1)=(EMPTY,1)
    tau(theta2)=(q,1).

Strict inequalities imply this difference persists in open irrational subintervals. Nonetheless the chosen query for z=1 is certified by **only two source/boundary noncollisions** (age 1 versus indices 0 and 1). This is an exact positive sparse certificate despite an unresolved full-vector phase; it also exposes the necessity of specifying the observer before compressing residual provenance.

## R62-C: algebraic circular anchor transport

For any fixed exact theta and integer anchors a,a', define y_t^(a)={(t-a)theta}. Then

    y_t^(a') = { y_t^(a) + (a-a')theta }.

All source phases undergo the same circle translation. Thus the cyclic order, circular successor relation, equal-phase groups and original timestamp/branch identities are unchanged. Only the seam representing linear sorted order on [0,1) moves. A persistent circular tree that supports moving its seam can reuse the indexed source population after anchor change. This is the proved order-transport identity, **not yet** a proven O(log n)-bit implementation of an immutable AVL split/join. New source comparisons and exact enclosure certification still depend on relative timestamp differences and can fail for unbounded ages (R61-D).

## Executed evidence and research disposition

The full local exact program CHECK_R62.py used Python integers and Fraction (not floating point). Output R62_CERTIFICATE.json has actual run evidence:

- 500 rational-enclosure trials, 2,509 certified queries checked at five parameters each (12,545 exact independent direct oracle comparisons); 15,253 older-source appearances excluded from query-specific collision checks.
- 1,000 near-collision stress trials: 3,885 queries, 1,414 certified, 2,471 conservatively rejected; 2,031 endpoint result differences; every certified query passed 7,070 direct-oracle comparisons.
- 120 huge-absolute-timestamp anchor shifts, 3,736 exact phase identities and 120 cyclic-order checks.
- Frozen m=128,H=225,p/q enclosure: 704 source/history index differences, positive minimum integer slack 1538749354821431426740; all 128 queried labels certified at both endpoints, requiring 21,336 source/boundary checks in aggregate. Three sparse labels 0,31,127 have youngest ages 61,30,98 and need 122,60,196 boundary checks (378 total) after preprocessing.
- The exact age-q witness above is separately reproduced in the executable miniature checker CHECK_R62_MIN.py; this remote program is a focused reproduction of the main locally executed test, not a claim that remote source bytes equal the longer program.

These are author mathematical derivations with finite exact verification, not an independently reviewed Result, formal Lean verification, or native X6 dynamical theorem. BRC application: labelled source/provenance is the carrier, selected youngest-age label is the observer, and future deletion is explicitly retained outside the read-only quotient. Frozen scientific input and P000 remain unchanged.

R63: implement persistent cyclic tree with a movable seam, prove its actual structural and bit operation costs, test duplicate timestamp/branch identity, and compare matched sparse/full/sliding workloads with R49/R56/R58/R59/R60/R61 including precomputation and enclosure precision.
