# R762JE — Complete 46→44 Port–Euler terminal reduction and derived k=0 upper bound 45

Date: 2026-11-22 (Asia/Shanghai).
Frozen scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Model scope: composite six-axis Port–Euler observer, with 15 pair-Ports and 20 triple-support types; not native signed X6 Cell/Link/force/rotation/time or residual-faithful path dynamics.
Status: AUTHOR_PROVED / EXACT_FINITE_RECALCULATION / NOT_REVIEWED. Independent review and formal project acceptance remain open.
Antecedent authorship: R762IR immutable commit 74e40c74 (11+ triple support reduction); R762JA immutable f754c3cd (uniform k=0 upper bound 46); R762JB immutable 489e3fa2 (6-triple terminal); R762JC, R762JD (new earlier same-line terminal reductions).

## Definitions and main theorem

Let A={0,1,2,3,4,5}. The 15 Ports are two-element subsets of A and the 20 three-axis support labels are three-element subsets of A. A support {a,b,c} has a local triangle on the Port vertices ab, ac, bc; every occurrence of that support chooses one of the three Port edges, allowing repeated parallel edges. Define N_{p,V}(n)>0 when there exists an all-even-degree connected nonempty Port multigraph with support multiplicities n, exactly the positive-degree Port set V and a designated Euler circuit start p in V.

Let (t,d,s,z) count support labels appearing respectively 3, 2, 1 and 0 times in n; they sum to 20.

**Terminal theorem (new, combined).** If n belongs to {0,1,2,3}^20, its total count is 46, and N_{p,V}(n)>0, then there is a support j with n_j=3 and

    N_{p,V}(n-2e_j)>0,

i.e. a 44-event closed witness preserving exact active Ports V, p, all positive support types, and each support count modulo 2. The proof includes all 24 arithmetically possible 46-event support histograms.

**Derived uniform 45 upper bound.** Subject to the earlier R762JA author-proved uniform-46 predecessor theorem, every k=0 legal composite Port–Euler history with 0<=n_S<=3 admits a witness h<=n with the same active Port set, designated start, support positivity and per-support parity and with at most 45 events. If R762JA gives <=45 already, keep that witness. If it gives exactly 46, apply the terminal theorem to obtain exactly 44. No asserted full signed-P000-history lifting, and no independent mathematical acceptance is implied by GitHub publication.

## Proof: exact histogram partition

For any 46-event n,

    t+d+s+z=20
    3t+2d+s=46
    s=t-6-2z.

The integer constraints d,s,z>=0 yield precisely 24 feasible histograms. Fifteen have t>=11 and nine have t<=10. The already published R762IR theorem reduces any legal configuration with >=11 triple supports, independently of absent supports.

The nine low-t histograms divide into five full-support cases already proved by R762JB, R762JC, R762JD:

    (6,14,0,0)  R762JB
    (7,12,1,0)  R762JC
    (8,10,2,0)  R762JD
    (9,8,3,0)   R762JD
    (10,6,4,0)  R762JD

and exactly four remaining missing-support cases, all proved below:

    (8,11,0,1), (9,9,1,1), (10,7,2,1), (10,8,0,2).

This exhausts all 24, provided the cited predecessor lemmas and published finite verification evidence hold at their exact statements.

## Four new missing-support reductions

For each of the four histograms, let T be its t triple-support labels.

**Case A — a triple support contains an inactive Port.** As the original triple support has positive multiplicity, two of its three Port vertices must be active. All three event copies are forced onto their only available edge. Removing two leaves one, preserves the original positive-even endpoint degrees, keeps the support, and cannot disconnect.

**Case B — all triple triangles fully active, some triangle not component-essential.** Its triangle's three Port vertices stay connected through the complete triangles of the other triple supports. Replace its three events with one and correct the resulting even GF(2) boundary using a path of the retained full-triangle graph; reassign each retained 3-event triangle to a connected three-edge local realization with the required boundary. The unchanged other support allocations and these connected full-triangle realizations preserve original connectivity and exact activity. This is the R762IR nonessential-triangle reduction.

**Case C — all T triangles fully active and component-essential.** The remaining calculation exhausts all 8-, 9-, or 10-triangle all-essential families modulo six-axis permutations S6 (720 relabellings). For an orbit representative T, let U be its uncovered Port vertices. Every possible inactive Port set M must be a subset of U. Enumerate **every** subset M of U, including pairs of inactive Ports sharing an axis (important when support types are absent). Eliminate M only if some positive support triangle has fewer than two active Port vertices: an original legal event is impossible there. Enumerate all choices of z absent-support labels outside T and all choices of s singleton labels outside both T and the absent labels.

For each remaining configuration, attempt all j in T until a 44-event integer edge allocation is found. SciPy/HiGHS is used only to propose allocations. The independent integer checker asserts all 20 exact support counts, sum=44, inactive Ports have zero degree, active Ports have strictly positive even degree, and the positive graph is connected by BFS. In disconnected proposals, an exact cut across a disconnected component is added and a fresh integer candidate is checked. S6 relabelling transports each verified witness to every labelled member of its orbit. All 1,036 representative legal-local configurations generated successful, exactly checked 44-event Eulerian constructions.

| Histogram (t,d,s,z) | All-essential T families | S6 T orbits | Exact witness checks | Labelled configurations covered |
|---|---:|---:|---:|---:|
| (8,11,0,1) | 4,920 | 16 | 301 PASS | 82,980 |
| (9,9,1,1) | 240 | 2 | 330 PASS | 33,000 |
| (10,7,2,1) | 6 | 1 | 360 PASS | 2,160 |
| (10,8,0,2) | 6 | 1 | 45 PASS | 270 |
| **Total** | | | **1,036 PASS** | **118,410** |

In the (8,11,0,1) class another 11 representative (T,Z,M) selections were excluded by the direct necessary condition that a positive support must have two active Port vertices; these are not missing candidates. The other three classes had none excluded. Each of the 1,036 tested allocations passed exact integer checks. The program reports the exact cut-round and inactive-degree subcounts.

## Reproduction

Companion executable: R762JE_REMAINING_AND_UNIFORM45.py, run alongside the prior R762JD_THREE_FULL_SUPPORT_CLASSES.py and R762JC_SEVEN_TRIPLE_46_44.py, using Python, NumPy and SciPy/HiGHS. The full exact integer classifier is specified by the script; a complete packed table of the 1,036 witnesses is not separately published, and solver output is never taken as independent evidence of mathematical correctness. The certificate validation happens after every candidate is generated. The locally executed run of 2026-11-22 gave:

    PASS (8, 11, 0, 1): essential=4920 orbits=16 valid_witnesses=301 labelled=82980 locally_impossible=11 inactive={0: 192, 1: 96, 2: 13} cuts={0: 290, 1: 11}
    PASS (9, 9, 1, 1): essential=240 orbits=2 valid_witnesses=330 labelled=33000 locally_impossible=0 inactive={0: 220, 1: 110} cuts={0: 327, 1: 3}
    PASS (10, 7, 2, 1): essential=6 orbits=1 valid_witnesses=360 labelled=2160 locally_impossible=0 inactive={0: 360} cuts={0: 359, 1: 1}
    PASS (10, 8, 0, 2): essential=6 orbits=1 valid_witnesses=45 labelled=270 locally_impossible=0 inactive={0: 45} cuts={0: 44, 1: 1}
    PASS R762JE: 1036/1036 exact Euler witnesses, four missing-support classes; all 24 length-46 histograms classified by reduction dependencies

This computation and the earlier R762JB/C/D evidence establish the author-side terminal theorem. The resulting overall **45 upper bound** is conditional also on R762JA's 46 upper bound and on earlier unreviewed foundational reductions. The math proof is intended for human/independent review; no Lean formalization or formal Result/Review is claimed.

## Remaining science and scope

Next test all 45-event terminal histograms for possible 45→43 compression, or construct a genuine 45-event lower-bound obstruction. Track the exact observer-fiber residual: Port activity, support-count parity and Euler existence do not retain ordered signed branch/phase/time/Cell transitions. A native TRIADIC_CLOSURE_E or future-observer lift needs its own typed map and proof. The fourfold-support k>0 model has a separate bound and is unaffected. Formal shared Task CLAIM, PROGRESS and Result/Review are independent of portable proof publication.
