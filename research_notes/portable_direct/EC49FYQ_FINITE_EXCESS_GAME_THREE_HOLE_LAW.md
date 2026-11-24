# EC49FYQ — finite excess game and exact stable three-hole law

2026-11-24. Continuation of frozen BRC16943 support family from [FYP](https://github.com/awdawmip/enterprise-math/blob/022e6a94cf04a549cf6c991f46fba020c31c9dd1/research_notes/portable_direct/EC49FYP_MAXIMAL_OPTIONAL_HOLE_RESIDUAL.md) and [FYO](https://github.com/awdawmip/enterprise-math/blob/3f81ac0627e5e9eb696d3fda4940557219d20345/research_notes/portable_direct/EC49FYO_ZERO_PREFIX_RESIDUAL_OBSTRUCTION.md). Auxiliary Boolean observer only: W(t,j)=1[t in U]1[j not in H], distinct nonempty supports, m>h, |H|<=h, noiseless unit-cost probes. No new native attribution.

## Main result

c_3=5, and Q_3(m)=m+5 for every m>=11. FYO proved Q_3(m)>=m+5 for all m>=4. This work constructs and replays a tree at m=11 on every one of 11600 labeled states, maximum 16 queries. The existing extension lemma Q_h(m+1)<=Q_h(m)+1 extends this construction to every larger m. The transition at m=7..10 remains open; failure of this particular policy there is not impossibility. No new independent review.

## General finite-excess game

Let F be any finite family of f distinct nonempty subsets of r rows. Let c>=0 and h>=1 be fixed integers. Existence of any finite m>h with Q_h(m)<=m+c is equivalent to winning the following finite abstract game. A state has a support set A, a sorted multiset of zero-only touched column row masks M, a flag indicating availability of a known-live column, and e=d-p, where d is used queries and p the number of positively confirmed columns. Trim A to supports forcing at most h holes (b(U)=number of M intersecting U). Start with F, no M, no live, e=0.

Actions: probe a row in a known-live column, a touched unresolved column, or a fresh column (unlimited supply in abstract game). Known-live outcomes filter A and increase e by 1. An unresolved negative adds a row to its M (or introduces a new M) and increases e by 1. An unresolved positive filters A by row membership and disjointness from its existing M, removes its M, sets live and does not increase e. Ignore empty branches. Trim after each transition. Remove constant probes. A fresh positive that preserves A and an already true live flag is an abstract self-loop: a successful strategy may omit that probe and follow its positive continuation. A fresh positive that first sets the live flag is allowed. Retain touched positive moves even when A unchanged.

For each compatible U with b(U)<h, require e-b(U)<=c. Proof: consider target with exactly the b(U) forced holes. Each of the m-p-b(U) remaining live columns needs a positive read to distinguish adding a hole. The path requires at least d+m-p-b(U)=m+e-b(U). Stronger optional-hole/superset bounds from FYO/FYP can be applied, retaining their hypothesis b<h. If A singleton and a low-hole candidate exists, finish by probing one row in U on each unresolved nonforced column; forced holes already known. Total cost <=m+e-b(U). If all compatible supports force exactly h holes, enter saturated terminal: each support has exactly one allowed hole set, and all untouched columns are live for every support. Query one known-live or untouched column to identify U in at most r further queries, then infer H from the forced set. Empty state is impossible branch.

Finiteness: while low-hole states exist e<=c+h-1; upon entry into terminal e<=c+h. Zero and known-live queries increase e. A touched positive removes a mask, of which at most e have ever been created. A fresh positive reduces A strictly except for at most one first live-flag change. Thus a nonredundant abstract path has at most B=2(c+h)+f queries before terminal, independent of m. For m>=B+max(1,r-c) a fresh column always exists through the abstract phase and the saturated finish fits m+c. Singleton finishes fit by the formula above. This proves sufficiency. Necessity: map any finite physical tree into these abstract states, stop when saturated or singleton, and enforce the bound by its low-hole target. Remove constant probes, and omit a fresh positive self-loop by following its positive child (possible for each support, as a fresh column may be live). The positive child's abstract state is unchanged; an already known-live representative supplies any later query to the omitted known-live label. Future fresh column actions use abstract supply and retain only actual touched unresolved masks. The omitted column is simply checked in the final sweep. Since e is unchanged on a fresh positive, the mapped suffix preserves the abstract budget. This eliminates all self-loops and gives a finite winning game. The game is a finite predicate for the stabilized excess, rather than a finite-m search repeated at increasing m.

## Additional fibre normalization used in construction

Instead of M_j use L_j={U in A: U disjoint M_j}. Trim by b<=h. If L_j is empty, that column is universally forced hole: retain its physical label for recovery, remove its fibre, decrement residual h and residual e by one (the credit e-b is unchanged). Repeat trimming; globally known holes do not participate in future queries. If L_j=A, its zero history gives no further restriction on any surviving support; drop its fibre while retaining its query cost e and physical label for the final sweep. For future abstract probing a fresh representative is equivalent. Positive confirmed columns share the same support observer; retain a physical live representative. This quotient preserves low-hole game, using the actual candidate support intersection and forced hole counts, not independent marginal counts. When applying optional-hole bound, for each low-hole U and each maximal optional hole selection, intersect strict supersets with L of retained live columns; an extra negative row must hit every surviving difference. Superset bound used by code skips extra>=3 (a weaker admissible bound, not an assumption of feasibility); search positive result independently replayed.

## Actual construction and labeled replay

C++17 search, budget c=5, residual h=3, returned success in 4,744,482 calls, 886,971 memo entries. An earlier row-mask-only implementation timed out after 30 seconds; no negative conclusion from it. The final replay independently reconstructs A, forced counts and normalized fibres directly from each raw physical transcript, consults the chosen game policy, runs the singleton/saturated completion, and checks exact recovered (U,H) against the input. It enumerates all 50 supports and every hole bitmask of weight <=3. It checks no repeated physical query and does not use the search norm() for replay. Full raw replay results:

```
3,5,1,4744482,886971
replay 8 pass 4258 fail 392 max 13 total 54672 saturatedMax 16
replay 9 pass 6356 fail 144 max 14 total 87648 saturatedMax 16
replay 10 pass 8788 fail 12 max 15 total 129522 saturatedMax 16
replay 11 pass 11600 fail 0 max 16 total 182136 saturatedMax 16
replay 12 pass 14950 fail 0 max 17 total 249428 saturatedMax 16
replay 13 pass 18900 fail 0 max 18 total 334132 saturatedMax 16
replay 14 pass 23500 fail 0 max 19 total 438990 saturatedMax 16
replay 15 pass 28800 fail 0 max 20 total 566944 saturatedMax 16
replay 16 pass 34850 fail 0 max 21 total 721136 saturatedMax 16
```

Failed replay here means the policy exhausts fresh columns or its chosen finish exceeds the given m+5 budget. It is not an exhaustive finite-m negative. The success at m=11 suffices for the exact infinite tail with FYO lower and extension.

## Escape-prefix additional check

FYP's 935 depth-eight all-zero escape prefixes for h=3,c=5 were independently re-enumerated (same layer counts). On each prefix every compatible support forces exactly 3 holes, so each support corresponds to exactly one H. All untouched columns are known live. A complete binary feasibility recursion over the remaining support bitset (all nonconstant probe splits on touched columns plus one fresh representative, capacity pruning only) gives exact residual depths with a fresh representative: depth 3:20, depth 4:519, depth 5:396. Maximum candidate count 30. With only k touched columns, use no fresh representative; some depths increase. For m=4..9, the counts (prefixes with k<=m, completable within m-3 remaining probes) are (1,0),(168,0),(644,0),(899,502),(935,935),(935,935). Thus Q_3(m)>m+5 for m=4,5,6 by FYP low-hole enumeration and these complete saturation checks. This is a finite bound, distinct from the construction. Replay code and a compact escape verifier are provided separately in this research branch.

## Next

The stable constants now c1=3,c2=4,c3=5. Apply the finite-excess game with h=4,c=6, optimize saturation finish and small m transition, preserve the h+2 conjecture for h>=4. Current proof depends on the frozen auxiliary family and parent FYO/FYJ results. Status AUTHOR_PROVED / EXACT_LABELED_INTEGER_REPLAY / PARENT_DEPENDENT / NOT_REVIEWED. Historical Researcher EM-DIRECT-23537B, original registration receipt SUCCEEDED, current private writer binding unconfirmed. Current task receipt r4-20261124-1130-ec49as-read-v1 SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at Source 061e650a326ed66b81f8dc3025e8a51dab728211 (directory observation only, no native owner projection or execution authority). Independent portable note, no shared CLAIM or Result.
