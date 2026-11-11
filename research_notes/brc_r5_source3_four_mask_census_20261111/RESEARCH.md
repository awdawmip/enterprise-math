# R5: the four-target source-3 stratum consists of exactly three disjoint 12-dimensional exposed faces

Date: 2026-11-11 (Asia/Shanghai). Author-side exact theorem and reproducible finite certificate.
Researcher-ID: EM-DIRECT-5E8923 / TASK_RESEARCH.
Research-Activity-ID: RA-4B4589EA90B89D0578AA49EA.
Native Source registration: enterprise-math commit 76f60817155fd8220a9a0a6300529f8169d743c3.
Original scientific inputs preserved from the prior R5 chain: global a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e; no repinning.
Prior source: PR #2017 physical 30-arc witness, PR #2059 49 sharp edges and source-3 row-only masks; the present work adds a global extension decision for every mask.

## Exact object

This is the frozen auxiliary seven-ratio P/Q–BRC observer fiber, not a native X6 spatial dynamics claim. Let R=(2,10,15,20,25,30,38). The allowed edges are all (i,j) with i in {0,...,6}, j in {1,2,3,5}, plus the fixed positive singleton edges (0,0),(6,6). The reference witness E0 is reproduced as exact rational numbers in VERIFY_FOUR_MASKS.py and comes from PR #2017.

Write F={E >= 0 : CE = CE0}, with C recording seven target marginals, seven source marginals, and seven source first moments. Rank(C)=15 and dim(F)=15. The two singleton arcs are fixed. For the 28 dynamic arcs, let x in Q_+^28, and write A x = b for the seven dynamic target marginals M_i, the four source marginals Q_j, and the four source unscaled first moments T_j. This 15-by-28 system has rank 13.

Source 3 has Q3=1076926147/2548188300 and T3=20 Q3. Its four-target mask is J={i:x_(i,3)>0}. For an allowed mask J, the restricted polytope is

F_J={E in F : E_(i,3)=0 for i not in J}.

## Theorem — complete source-3 minimum-support geometry

**(1)** Every transfer E in F has at least four positive dynamic source-3 edges.

**(2)** Exactly three masks with four positive source-3 edges are realized anywhere in the full physical observer fiber:

- J_A={1,3,4,6};
- J_B={2,3,4,5};
- J_C={2,3,4,6}.

Each F_J is a nonempty exposed face of F, with **exact affine dimension 12**. Each has a fully explicit rational point with all 27 permitted arcs positive (25 dynamic arcs plus the two fixed singletons).

**(3)** The three faces are pairwise disjoint. Hence

{E in F: |supp(E_(.,3))|=4} = F_JA disjoint-union F_JB disjoint-union F_JC

has exactly **three connected components**, each a 12-dimensional compact convex face. A continuous path inside F joining different four-support faces necessarily encounters a transfer with at least **five** positive source-3 edges. The convex straight-line segments between the supplied rational witnesses realize such bridges: between A and B they carry six source-3 positive edges, and between A and C or B and C they carry five.

These are complete statements for this **one fixed physical fiber** and the source-3 row-support observer.

## Proof — local-to-global census

1. Every source-3 allocation obeys 0<=x_(i,3)<=M_i, sum x_(i,3)=Q3 and sum R_i*x_(i,3)=T3. For a support mask J, the extremal first moments under those capacities are obtained by greedily allocating the fixed Q3 mass in ascending/descending order of R_i. This is exact: exchanging a small amount from higher to lower R weakly decreases the moment. Exhausting all size-1, size-2, size-3 masks yields zero compatible candidates. For the 35 four-target masks, nine fail capacity, nineteen fail moment, zero sit on a boundary, and seven pass strict row-only feasibility. They are: {1,2,3,6}, {1,2,4,6}, {1,3,4,6}, {1,3,5,6}, {1,4,5,6}, {2,3,4,5}, {2,3,4,6}.

2. The exact global system A x=b decides the seven local candidates. For each globally feasible J, the checker lists a rational t and 13 pivot-column indices (ordered dynamic columns (i,j) with j=1,2,3,5 and i=0,...,6). Set all twelve nonpivot allowed columns to t and all three forbidden source-3 columns to zero, and solve the 15 exact equations for the 13 pivots by rational Gaussian elimination. The 13 pivot columns have rank 13 and the resulting solution satisfies all 15 equations exactly, with every one of its 25 allowed dynamic coordinates strictly positive. The minimum positive dynamic values are:

| Mask | t for each of 12 free variables | Smallest dynamic mass |
| --- | --- | --- |
| {1,3,4,6} | 1/900 | 701522923/1758249927000 |
| {2,3,4,5} | 1/500 | 2597481/8493961000 |
| {2,3,4,6} | 1/800 | 155682221/156288882400 |

The frozen positive singleton masses complete each exact 30-entry witness.

3. For each of the other four masks, the code supplies an explicit exact 15-component rational Farkas vector y. On **every allowed column** a_k of A, y·a_k>=0, while y·b is strictly negative. Therefore no nonnegative exact solution exists, irrespective of the number or location of additional zero edges among the other sources.

| Excluded mask | Exact y·b |
| --- | --- |
| {1,2,3,6} | -12763881/2972886350 |
| {1,2,4,6} | -9966057/424698050 |
| {1,3,5,6} | -21414133/1486443175 |
| {1,4,5,6} | -359994723/5945772700 |

The complete vectors y and all allowed-column inequalities are checked in VERIFY_FOUR_MASKS.py, with no approximate solver required for verification.

4. For each of the three successful masks, the 21-by-27 restricted observer matrix has exact rank 15. The corresponding 27-arc witness is strictly positive on every allowed arc, so the affine dimension of F_J is 27-15=12. F_J is exposed by the nonnegative linear functional sum_{i not in J}E_(i,3), and is a face of the compact fiber F.

5. Pairwise disjointness: J_A intersect J_B={3,4}; J_A intersect J_C={3,4,6}. All their ratios are >=20 and only label 3 has R_i=20. Source-3 mean exactly 20 would force all mass onto label 3, but

Q3-M3=2330939/8493961>0.

For J_B intersect J_C={2,3,4}, the total capacity is smaller than source-3 mass:

Q3-(M2+M3+M4)=196521/16987922>0.

Hence all three pairwise intersections are empty. Since no valid source-3 support has fewer than four labels, every point of F_J has source-3 support exactly J. The three disjoint nonempty compact convex faces are precisely the four-support locus; each is one connected component. Its complement in the connected ambient fiber necessarily contains a support of at least five on any path switching between components. By convexity, interpolating the explicit witnesses gives constructive bridges.

## Reuse, verification and follow-up

BRC carrier: positive rational masses on all 30 labeled branches, preserving source-target joint provenance. Observer: 21 marginal/moment rows of C. The three 12D faces are observer-fiber alternatives with equal readings; their separation and higher-support bridges are visible only when source-3 branch support is retained. Applied reuse: PR #2017 exact witness, PR #2059 row-mask first-stage census and 15-rank observer. The new independent certificate classifies full-fiber feasibility and connected components; it does not change frozen P000 or physical-world foundations.

Verification: run python3 VERIFY_FOUR_MASKS.py with Python 3 standard library only. All arithmetic and comparisons use Fraction. Assertions check the complete small-mask census, 35 four-mask census, three explicit rational transfers (all 15 constraints and 27 positive arcs), exact 15-rank restricted observer matrices, four full Farkas certificates, and pairwise face disjointness. Last line is PASS_EXACT_R5_SOURCE3_GLOBAL_FOUR_MASK_CENSUS_3_OF_7. The original local program was actually executed in this turn and its output is saved in EXACT_OUTPUT.txt. Proof status: author-side derivation + exact finite verification; independent review and canonical scientific Result admission remain pending.

**Next research unit:** quantify non-sharp edge directions that connect the 49 sharp edges' nine tree components inside F_{2,3,4,5}. In addition, determine the minimum number of BRC six-arc residual atoms required to traverse between the three disjoint source-3 minimum-support faces, and characterize the 5-support transition strata. Avoid claiming an entire 15D vertex census from this 4-support classification.
