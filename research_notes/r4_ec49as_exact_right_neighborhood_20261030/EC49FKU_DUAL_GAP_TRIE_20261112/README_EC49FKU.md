# EC49FKU — Independent ≤93-prefix exclusion for six-key cases 0 and 3

Date: 2026-11-12. Scope: frozen nine-state BRC model, 24 exact observer demands, ordered signed-X6 microstep prefixes, fixed six-full-cache-key sets 0 and 3 of EC49FKQ/EC49FKS. Frozen scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Author-side finite certificate, pending independent Driver review. No P000/worldview update.

## New finite theorem

For each of the six-key sets K0 and K3, **every complete legal solution satisfying all 24 observer demands has at least 94 distinct nonempty ordered signed-X6 prefixes**. This is an integer lower bound independently verifiable without using HiGHS, branch-and-bound optimization, numerical tolerance or solver-reported optimality. The earlier EC49FKQ 98-prefix witnesses remain available as upper bounds; this certificate proves the ≥94 threshold needed to exclude 93.

K0 and K3 share the four keys (2,1,1),(3,0,1),(3,1,1),(4,2,1). Their extra pairs are K0: (5,4,1),(5,5,1); K3: (6,3,1),(7,3,1).

## Proof by rational dual-gap filtering followed by exact trie DP

The EC49FKS compact certificate gives the exact LP lower bound L = 1105/12, verified by a rational primal/dual pair. Let x_v ∈ {0,1} indicate whether a nonempty literal prefix v occurs, with x_child ≤ x_parent; for each demand i, the sum of terminal indicators belonging to that demand is at least one. The exact rational dual provides nonnegative demand weights a_i and nonnegative parent-directed edge flows f_v. Write c_v = sum_{i: v is a terminal for i} a_i and define the node's reduced cost

r_v = 1 − c_v − Σ_{u child of v} f_u + f_v  ≥ 0,

with f_v = 0 at a root. The dual feasibility/optimality check in EC49FKS reconstructs these flows bottom-up with f_v = max(0,c_v+Σ_child f_u − 1) at every nonroot, and verifies the corresponding root inequalities.

For every feasible integral prefix selection, exact telescoping yields

|S| − L = Σ_v r_v x_v
          + Σ_{u child of v} f_u (x_v − x_u)
          + Σ_i a_i (Σ_{v terminal of i} x_v − 1).

Every term on the right is nonnegative. If |S| ≤ 93, then |S|−L ≤ 93−1105/12 = 11/12. Consequently, **any node v with r_v > 11/12 must have x_v=0**. Any complete word containing one of those nodes is excluded from a hypothetical ≤93 solution.

The exact rational checker, using the full frozen legal-word generator and compact EC49FKS certificates, obtains for EACH of K0 and K3:
- 4,366 legal operation words and 19,962 nonempty signed-X6 prefix trie nodes before filtering.
- 5,231 nodes with r_v > 11/12.
- Exactly 170 complete candidate words not using any excluded node, with six observer demands each restricted to one candidate word.
- The 170 words split by the literal first signed native step into two disjoint prefix trees, first-step byte 05 and 06. Each of the 24 demands occurs in precisely one root component; each component has 12 demands. Component candidate-word counts are 61 and 109 (swapped between K0 and K3).

A second, exact **subset-mask prefix-tree dynamic program** computes the minimum number of distinct nonempty prefixes for each 12-demand component. At a terminal, one may select its demand mask or select nothing. At a branch, combine selected demand masks by bitwise OR and costs by addition; adding a nonempty node costs one, an unselected node costs zero. The full mask contains all 12 demands, so this recurrence enumerates every candidate selection under its component. Each component has 2^12=4096 attainable masks and an exact optimum of **49** nonempty prefixes. Hence every selection of all 24 demands from the 170 surviving words has cost at least 49+49=98.

A hypothetical solution of cost ≤93 would have to use only those surviving words, yet their exact minimum cost is 98. This contradiction establishes the ≥94 theorem for K0 and K3.

The value 98 is the optimum of this *dual-gap-filtered* candidate problem, not claimed as an unconditional global optimum of all original words; the latter exact-98 observation from EC49FKQ retains its original integer-program evidence.

## Reproduction and evidence

Run the attached VERIFY_EC49FKU.py with Python standard library only (no SciPy/HiGHS), alongside the original frozen EC49FGW_RADIUS5_SCREEN.py and EC49FGJ_SEVEN_KEY_94_WITNESSES.json, and the already published EC49FKS_COMPACT_CERT.json and CHECK_EC49FKS_COMPACT.py. Within the full PR #1730 checkout, the script finds the two predecessor folders automatically. No scientific input is regenerated through non-BRC arithmetic; exactly the source-pinned BRC state-machine/path catalogue is used.

Actual author execution, 2026-11-12: both cases passed complete Fraction dual verification, full 4,366-word enumeration, node filtering and two 12-demand exact trie DPs; 49+49 per case. See EXACT_REPORT_EC49FKU.json and the verifier source in this directory.

## Continuation

EC49FKR independently excludes ≤93 for cases 4–8 using its 100-prefix integer-flow certificates. EC49FKU now excludes ≤93 for cases 0 and 3. The remaining **cases 1 and 2** have exact LP lower bound 269/3 and require integrality-sensitive cuts or a different disjunctive certificate; the same r_v > (93−269/3) filter excludes no node under the EC49FKS minimal flow certificate. Continue these two exact six-key sets, and independently pursue the seven-key 93-prefix mother problem.

Status: AUTHOR_EXACT_FINITE_PROOF / SOLVER_FREE_CHECK_EXECUTED / SOURCE_DRAFT; formal CLAIM/Result and mathematical admission remain distinct and require their own current owner/Driver authority.
