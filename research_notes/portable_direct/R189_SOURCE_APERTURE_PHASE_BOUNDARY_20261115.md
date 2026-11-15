# R189 — Bounded latest-source queries: full-aperture threshold and finite minimax

Date: 2026-11-15. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent portable research; no formal CLAIM, Result or Review.
Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34 (unchanged).
Predecessor: https://github.com/awdawmip/enterprise-math/blob/43366e9337a009acb803ca773b69205e503fd2f1/research_notes/portable_direct/R188_OPTIMAL_UNKNOWN_SUPPORT_PAIR_ORACLE_LIFT_20261115.md

## Exact model and observer

There are k >= 1 named source IDs and an arbitrary, possibly empty, history. We retain the complete typed X6 branch/path provenance, positive rational BRC weights, multiplicity and branch identity on the underlying carrier. The *source-only* observer is the partial permutation s of occurring source IDs, ordered by their last occurrence from oldest to newest. A query of nonempty U, with |U|<=b, returns the last appearing element of U or NONE. Queries are adaptive; support is unknown. Q_b(k) denotes the deterministic minimax number of unit-cost oracle calls to reconstruct s. The effective aperture is min(b,k).

## Theorem R189-A (all k; proved symbolically)

(1) Q_b(1)=1 for b>=1.
(2) Q_1(k)=infinity for k>=2.
(3) Q_b(k)=k for b>=k.
(4) Q_{k-1}(k)=k+1 for k>=3.
(5) More generally Q_b(k)>=k+1 for every k>=3 and 2<=b<k.

Consequently, increasing aperture from k-1 to k saves exactly one worst-case call, whereas at k>=2 aperture one cannot recover order at all.

### Proof of the universal lower bounds

Fix any full-support history s. For every source x, the algorithm must have an oracle query returning x: if x never wins, deleting x from s leaves every answer along the adaptive transcript unchanged, since queries previously won by another source still have the same winner. A correct algorithm must distinguish the two histories. Hence at least k calls are needed for full support, regardless of aperture.

Now assume 2<=b<k. Let U be the algorithm's first informative nonempty query, necessarily a proper subset. Choose x in U and y outside U. Construct a full-support order s with x most recent, y second most recent, all other names earlier. The first query returns x. Swap the adjacent latest two to form s'. Any query omitting one of x,y returns the same answer in s and s': the included member of the pair still wins over all other members, and the remaining members retain their relative order. Thus the algorithm must eventually query a set containing both x and y to distinguish s from s'. The first query cannot contain y; hence a later query returns x again on s. There must still be k distinct winning source IDs among the answers (previous paragraph), and x wins twice, so at least k+1 calls occur on this input. This proves (5).

For b=1 all answers are membership bits and never encode relative last-occurrence order, so two full-support permutations are indistinguishable when k>=2. For k=1 the empty and singleton histories require one membership query.

### Constructive optimal algorithms

If b>=k, query the whole remaining candidate set, record/delete its latest reported ID, and repeat until NONE or exhaustion. It takes at most k calls and full support requires k by the lower bound.

For b=k-1, k>=3, choose t and first query U=T minus {t}. If NONE, a singleton query of {t} determines the entire history. Otherwise let x be the answer (the latest in U), then query {x,t}. Its answer z is the latest in all of T, because x dominates everything in U. Record z, remove it, and repeatedly query the entire remaining candidate set (now at most k-1 names), recording/removing winners and stopping on NONE or exhaustion. Reverse the list of winners to obtain s. At most 2+(k-1)=k+1 queries are used. The proper-aperture lower bound proves optimality.

These conclusions require neither extra spatial dimensions nor P000 modifications. They only concern the declared source-only observation/whole-history concatenation. A richer native X6/BRC observer may not safely discard source chronology, paths, branch IDs, joint provenance, multiplicity, signed residuals or weight spectra.

## R189-B — complete exact finite minimax for k<=5

The state space contains S_k = sum_{r=0}^k k!/(k-r)! partial permutations. For a belief B in these states, each allowable query partitions B by the exact returned label or NONE. The optimal depth satisfies D(B)=0 for a singleton belief; otherwise D(B)=1+min_{queries splitting B} max_{nonempty answer classes B_a} D(B_a). Non-splitting queries can be removed; every retained child is a strict subset, so this exhaustive recurrence terminates. The accompanying verifier tests feasibility at successive depths over all query types and answer groups, then extracts and checks a correct optimal-depth decision tree on every state. Arbitrary-size Python integer bitsets and exact integer arithmetic are used throughout.

| k | b=1 | b=2 | b=3 | b=4 | b=5 |
|---|---:|---:|---:|---:|---:|
| 1 | 1 | - | - | - | - |
| 2 | impossible | 2 | - | - | - |
| 3 | impossible | 4 | 3 | - | - |
| 4 | impossible | 6 | 5 | 4 | - |
| 5 | impossible | 8 | 7 | 6 | 5 |

The value Q_3(5)=7 exceeds the general k+1 lower bound (which is six in this instance). This is an exact finite result, not a claimed all-k closed form. In fact the apparently linear formula Q_b(k)=2k-b, compatible with this small table for b>=2, cannot hold for all k, since the proved R188 pair-oracle law gives Q_2(k)=C_pair(k)+1=Theta(k log k).

## Verification and limits

File R189_source_aperture_minimax_check.py implements the finite decision-tree Bellman solver and full-state decoding checks. R189_verification.json contains finite minimax outcomes, failed smaller-depth checks, decision-tree fingerprints, and complete exhaustive checks of the explicit (k-1)-aperture algorithm on every partial permutation for k=3..8: 16+65+326+1957+13700+109601 = 125665 states, zero failures, with worst-case exactly k+1 on each k.

Finite checks support the proof and are exact for their stated bounded domains; they do not replace the symbolic all-k argument. No native enterprise_math.brc_transport execution, independent review, formal proof checker, speedup claim, physical dynamics assertion or full input/selector/bit-cost benchmark is made.

## Next research

Determine Q_b(k) at fixed b>=3 for growing k, starting from k=6,b=3 or b=4; strengthen lower bounds beyond k+1 and compare exact decision trees to constructive b-way max-sorting algorithms. Run an actual typed BRC source selector against src/enterprise_math/brc_transport.py with positive-rational masses and preserved X6 provenance, accounting for construction and serialization costs.

Source bookkeeping: historical Researcher EM-DIRECT-BF4AD7, SID MCP-46f202db13e64ad6b4c8860e06908245, Activity RA-7A118452894D2600AE7DE5A2. These are provenance, not proof of current execution CLAIM.