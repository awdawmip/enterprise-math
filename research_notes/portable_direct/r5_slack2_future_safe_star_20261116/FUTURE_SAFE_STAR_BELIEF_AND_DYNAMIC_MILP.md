# R5 — Future-safe radius-one belief theorem at additive slack two

Date: 2026-11-16 (Asia/Shanghai). Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Evidence: AUTHOR_PROVED (general theorem); EXACT_FINITE_INTEGER_MODEL / SCIPY_HIGHS_SOLVER_CROSSCHECKED (k=3..6); NOT_REVIEWED.

## Statement and inherited model

Continue `r5_slack_dynamic_source_20261116/SLACK_SOURCE_COVER_AND_DYNAMIC_BELIEF_THEOREMS.md` at the same immutable input. This is the auxiliary one-dimensional indexed-centre radius-two cycle-of-triangles source-library observer, rather than an assertion about native X6 dynamics.

For k>=3, a raw unavailable-helper mask u belongs to {0,1}^k. Let q(u)=sum_(i mod k) u_i u_(i+1). The proven common-source minimum for a family B of raw masks is 5k+q(OR B), realized by an explicit genuine source-labelled library L(OR B). Set_i(b) overwrites named bit i with b. An internal belief B is a nonempty set of possible raw masks. With slack s=2, B is *future-safe* if for every finite word w in all named Set_i(0/1), the common library can stay within two extra source entries above every raw-state optimum:

    q(OR T_w(B)) - min_{u in B} q(T_w(u)) <= 2.

No step is allowed to relabel a source or substitute a different underlying repair model.

## Theorem 1 — Exact classification of all future-safe beliefs

For every k>=3 and nonempty B subset {0,1}^k, write r=OR B. The following conditions are equivalent:

1. B is future-safe for all finite named-Set words at additive slack 2.
2. Every u in B differs from r at **at most one** coordinate: popcount(r & ~u)<=1.
3. B is contained in the downward Boolean radius-one star S(r)={r} union {r\{i}:r_i=1}.

**Sufficiency.** Every overwrite T commutes with coordinatewise OR. Thus OR T(B)=T(r). If u differs from r at most one bit, T(u) differs from T(r) at most one bit, and on a cycle each single newly unavailable vertex can create at most two incident unavailable-unavailable edges. Therefore q(T(r))-q(T(u))<=2 for all u and all T. The common-source theorem supplies the actual library L(T(r)).

**Necessity.** Suppose r has two distinct 1-bits i,j that are both zero in some u in B. Overwrite every coordinate outside supp(r) to 1, leaving all coordinates of supp(r) unchanged. The OR of the resulting belief is 1^k, whereas the image of u has zero at both i,j. In a cycle of length k>=3, any two distinct vertices meet at least three edges. Hence q(1^k)-q(T(u))>=3, contradicting the slack bound. QED.

This is an exact *future* characterization, not merely a present-time compatibility test. It converts the unrestricted candidate-belief search over 2^(2^k)-1 subsets to a sharply structured family.

## Theorem 2 — Count of possible future-safe beliefs

For each center r with t=popcount(r), a nonempty subfamily of S(r) has OR exactly r in:

    2^(t+1)-t-1

ways: either include r (2^t choices of other members), or omit r and select at least two distinct single-deletion neighbors (2^t-t-1 choices). The formula also handles t=0,1. Distinct centers have distinct OR, so the total number of future-safe beliefs is exactly:

    B_k = sum_{t=0}^k binom(k,t) [2^(t+1)-t-1]
        = 2*3^k-(k+2)*2^(k-1).

Examples: B_3=34, B_4=114, B_5=374, B_6=1202.

## Theorem 3 — Exact smaller integer-program formulation

Associate one binary variable x_B to each of the B_k future-safe beliefs. For any raw mask u impose:

    sum_{B containing u} x_B >= 1.

For every future-safe B and every named command a=Set_i(b), impose:

    x_B <= sum_{C: T_a(B) subset C} x_C.

Minimize sum_B x_B. The optimum equals the minimum number of states of the deterministic source-labelled Moore transducer from the inherited model at full named control and slack two.

**Proof.** A valid transducer's state-beliefs must all be future-safe because its action successors preserve every possible raw mask. Theorem 1 restricts them to the listed B_k candidates. Each raw input must be represented initially (coverage), and each selected state has a deterministic selected successor that contains its image (transition inequalities), giving a feasible binary solution. Conversely a feasible solution lets us choose an initial state containing each raw mask and a chosen successor for every selected state/action. Emit L(OR B) in state B. Theorem 1 verifies the cost and exact-source guarantee for every reachable raw mask, and the inequalities verify deterministic transitions. QED.

**Corollary.** The earlier one-forgotten-coordinate construction gives N_dyn(k,all,2)<=2^(k-1). If a transducer uses fewer than 2^(k-1) states, at least one of its reachable belief sets contains three or more raw masks, necessarily single-deletion variants of the same OR center. Thus any improvement requires genuine location-uncertainty management, not merely pairing raw masks.

## Finite numerical results and validation scope

The accompanying Python program builds the exact integer program with SciPy/HiGHS MILP, zero requested relative gap, and checks its returned selected families independently by exact integer bitset operations. All instances finished with solver status OPTIMAL, primal=dual and reported gap zero.

| k | Raw masks | Future-safe beliefs | MILP constraints | Selected states | Solver bound |
|---|---:|---:|---:|---:|---:|
| 3 | 8 | 34 | 212 | 4 | 4 |
| 4 | 16 | 114 | 928 | 8 | 8 |
| 5 | 32 | 374 | 3772 | 16 | 16 |
| 6 | 64 | 1202 | 14488 | 32 | 32 |

Each selected family passed exhaustive coverage and every named transition under exact integer set containment; all four optima agree with 2^(k-1). The solver's optimality bounds are numerical MILP outputs; a standalone machine-checkable exact lower-bound certificate or uniform symbolic proof for k>=7 is **not yet supplied**. For k=3 the previously saved complete three-state enumeration provides an additional independent exact finite lower bound.

## Provenance and unfinished unit

Sources: `r5_slack_dynamic_source_20261116/SLACK_SOURCE_COVER_AND_DYNAMIC_BELIEF_THEOREMS.md`; `r5_shared_source_helly_20261116/SHARED_SOURCE_HELLY_AND_ROBUST_CONTROLLER_THEOREM.md`; P000 and the current ACTIVE residual-preservation constraints. This note preserves the inherited frozen scientific pin, integer indexing, source labels E0/E1/H0/H4 and distinct source/control authorization. It changes no native X6 scientific input.

Verification command: `python VERIFY_R5_SLACK2_FUTURE_STAR.py 3 4 5 6`. Outputs: `EXACT_R5_SLACK2_FUTURE_STAR_EVIDENCE.json` with complete finite selected beliefs, row counts and numerical objective bounds.

**Next:** Establish or refute the all-k conjecture N_dyn(k,all,2)=2^(k-1), preferably through a purely combinatorial lower bound on transition-closed star families; independently examine k=7 with a bounded scalable exact optimization or a reproducible lower-bound certificate. Do not promote solver agreement at k<=6 into the universal theorem.
