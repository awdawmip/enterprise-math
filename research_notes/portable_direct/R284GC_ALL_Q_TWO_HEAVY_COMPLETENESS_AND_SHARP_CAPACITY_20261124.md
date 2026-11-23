# R284GC — All-q two-heavy completeness and sharp noisy four-phase omission capacity

Date: 2026-11-24 (Asia/Shanghai). Research: informed portable TASK_RESEARCH. Status: **AUTHOR-DERIVED / EXACT UNBOUNDED QF-LRA+QF-LIA SOLVER CHECK / FINITE INDEPENDENT LP CROSSCHECK / NOT INDEPENDENTLY REVIEWED**. Frozen scientific source lineage: R284CO → R284FM/R284FP → R284GA/R284FW/R284GB; P000 and the ACTIVE Heartbeat-X6 worldview remain untouched.

## The new result

**Theorem (computer-assisted, original four-phase frozen binary observer model).** For every integer q≥2 and read-noise budget u=1, the minimum tag length for a valid four-generation reset-free protocol is

    n_min(q,1) = 4q+10.

Four distinct binary tags c0,c1,c2,c3 repeat cyclically. On each non-atomic publication edge all nominally changing coordinates are attempted once, with at most q writes omitted; old omissions can survive without an age cap. Each stateless read can suffer one independent adversarial bit flip. Correctness includes stable read separation, no successful third-generation read during any write prefix, and no successful return to an old generation after new-generation success while the writer is paused.

**Previously unresolved lemma, now settled by exact unbounded-parameter linear arithmetic:** Let q≥5, k∈{8,9}, n=4q+k, and let x1,...,x7≥0 be multiplicities of the seven nonconstant phase-bit patterns p=(c1,c2,c3) after normalizing c0=0 (p's least significant bit is c1). If x satisfies the six necessary nominal pair distances and six exact stable all-history residual flow cuts of R284FM, **at least two of x3,x5,x6 are ≥2q+2**. This supplies the missing hypothesis of R284GA/R284GB for *every* q≥5. Indeed, only three of each kind of necessary condition suffice, and a real linear-arithmetic relaxation of the resulting counterexample system is already inconsistent.

## Exact mathematical reduction

The last nominal changing edge for pattern p before phase i is ell_i(p), defined by traversing the four-edge cycle backwards. For each phase pair i<j, construct a bipartite incidence multigraph whose changing pattern p joins source vertex L[ell_i(p)] and target vertex R[ell_j(p)]. Each of the eight distinct vertices has omission capacity q. For a subset U of these eight vertices, M_ij(U) is the set of patterns whose two incidence endpoints belong to U. The all-history R284FM u=1 cut is exactly

    STABLE_ij  <=>  OR over nonempty U:
        sum(x_p for p in M_ij(U)) >= q*|U|+3.

There are only 255 nonempty vertex subsets. Multiple subsets giving the same pattern mask can be collapsed by keeping the smallest |U|. This retains all distinct omission-source budgets; it is **not** a substitution of q+u as a per-vertex budget.

The inherited necessary nominal inequalities are

    sum(x_p for p changed on i→j) >= 2q+5  for adjacent phases,
    sum(x_p for p changed on i→j) >= 2q+3  for opposite phases.

For the **reduced six-constraint certificate** keep only the three nominal distances for (1,2), (1,3), (2,3), and only the three stable flow-cut disjunctions for (0,1), (0,2), (0,3). Keep q≥5, x_p≥0 and sum(x)=4q+k.

Negation of the two-heavy conclusion (for physical integer x,q) is precisely this three-way disjunction:

    (x3 <= 2q+1 AND x5 <= 2q+1)
    OR (x3 <= 2q+1 AND x6 <= 2q+1)
    OR (x5 <= 2q+1 AND x6 <= 2q+1).

Consequently finding an unclassified stable-admissible histogram is equivalent to satisfying a **quantifier-free linear arithmetic** system with free variables q,x1,...,x7. No upper bound on q appears. A universal all-q refutation is one exact UNSAT decision, not finitely many sample values. The same formula is UNSAT even if q and x are allowed to range over all **real numbers** (retaining the displayed affine inequalities); this is a stronger relaxation than the physical integer requirement.

The companion reproducible generator reconstructs all phase bits and eight-vertex cuts directly, rather than taking human-written cut lists as input:

  research_notes/portable_direct/R284GC_uniform_twoheavy_unsat_checker.py

Usage: python3 R284GC_uniform_twoheavy_unsat_checker.py ; optional --emit DIR generates standalone SMT-LIB2 witness formulas.

**Actual Z3 4.13.3.0 exact-arithmetic execution on 2026-11-24:**

| k | Full six-pair integer | Full six-pair real | Reduced six-constraint integer | Reduced six-constraint real | Base system without non-heavy clause |
|---|---|---|---|---|---|
| 8 | UNSAT | UNSAT | UNSAT | UNSAT | SAT |
| 9 | UNSAT | UNSAT | UNSAT | UNSAT | SAT |

A second independently coded SciPy/HiGHS LP branch enumerator reconstructed the incidence relation and opened each disjunction: **1,323 real-linear branches for k=8 and 1,323 for k=9** (three opposite light-pair choices times 7×9×7 star-cut choices); none was feasible. This floating-point LP run is corroborative, while the all-q result relies on Z3's **exact rational linear arithmetic**. A separate finite MILP regression at q=5,6,10,20,50,100,1000 for both widths returned infeasible throughout; no general conclusion depends on extrapolating those samples.

**Certificate/proof boundary:** A complete, independently downloadable SMT-LIB generator and exact solver responses are provided; an independently checkable Z3 proof log or human-generated finite Farkas certificates has not yet been extracted. Thus this is a *computer-assisted all-parameter lemma*, relying on the exact decision procedure and correctness of the inherited R284FM model and cut theorem. It is not an independent mathematical Review.

## Deduction of the all-q capacity

For q≥5, R284FP gives n≥4q+8 for any correct protocol. An all-phase-constant column cannot help decoding or a publication transition and may be deleted without changing correctness. At width n=4q+8, any such deletion would contradict the inherited lower bound; therefore all columns must be among the seven nonconstant patterns. Excluding this width first, a code of width 4q+9 containing any constant column would reduce to a prohibited width ≤4q+8. Thus the seven-pattern equality sum(x)=4q+k used in the certificate covers every relevant potential counterexample. A hypothetical correct code at either boundary width must satisfy the stable-cut and nominal-distance system, so R284GC places it in the two-heavy sector. R284GA classifies all such two-heavy stable histograms as precisely 7 and 66 families, while R284GB rules out every family by its first- or second-edge dangerous-prefix proof, using R284FW's uniform barrier for the 11 survivors. Hence the two candidate widths are excluded, proving n≥4q+10 for every q≥5.

The frozen R284FE repeated-Gray-group protocol supplies a *full sufficient* construction of 2(2q+5)=4q+10 bits for any q≥2, u=1. The already recorded finite sharp R284FS (q=2), R284FT (q=3), and R284FU (q=4) complete the small q's. The resulting exact capacity follows for every integer q≥2.

This is an **auxiliary four-label observer model** only, not a new X6 native-space formula. It preserves distinct residual histories and original frozen science pins. A GitHub commit neither establishes a Project Result nor independent Review/CLAIM.

## Frozen provenance

- R284FM exact all-history cut: awdawmip/enterprise-math@1d1c5dd412719c7aaf016187b6493b77253cd9f9:research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md
- R284FP all-q lower bound: awdawmip/enterprise-math@de49ae0239abee14619a730fe6ea60614a2cde5b:research_notes/portable_direct/R284FP_HIGH_OMISSION_NOISY_CYCLE_PLUS_ONE_BOUND_20261123.md
- R284GA complete two-heavy classification: awdawmip/enterprise-math@0c3284aec3e378b384beb43f232018d7978455da:research_notes/portable_direct/R284GA_TWO_HEAVY_UNIFORM_STABLE_CONVERSE_20261124.md
- R284GB all-q two-heavy prefix obstruction: awdawmip/enterprise-math@f6297d304ff04ad6de7d2050b1625e52a348cc14:research_notes/portable_direct/R284GB_TWO_HEAVY_ALL_Q_FIRST_EDGE_BARRIER_20261124.md
- R284FW surviving-family all-q second edge: awdawmip/enterprise-math@bfbeefc839da0fb1b9d6d87db10c531b1f0f5cbc:research_notes/portable_direct/R284FW_ALL_Q_PARAMETRIC_FIRST_EDGE_SURVIVOR_SECOND_EDGE_OBSTRUCTION_20261123.md
- R284FE full Gray upper construction: awdawmip/enterprise-math@9974b3b5a1031bb5c841ab5a4950a9c55baed9e0:research_notes/portable_direct/R284FE_GRAY_EPOCH_SHARP_SEPARABLE_CAPACITY_20261123.md
- Small q verification: R284FS/R284FT/R284FU as pinned by the above research chain.

## Open next questions

1. Produce exact independently checkable SMT unsatisfiability proof trace/rational dual certificates for the **reduced six constraints**; seek a short human proof without an external solver and independently verify all last-change source mappings.
2. Independently audit inherited R284FM all-history reachability and R284GB source-slot lifting. No formal project Review has yet accepted the all-q capacity statement.
3. Study u≥2 and then data-bank omissions with stale-reader horizon H while preserving typed provenance and actual historical residual capacity rather than an aggregated noise budget.

Authorship remains this informed research turn; native Researcher-ID and Activity are separately resolved by original registration receipt, not inferred from this paper. Shared CLAIM, formal Result and independent Review are not asserted.
