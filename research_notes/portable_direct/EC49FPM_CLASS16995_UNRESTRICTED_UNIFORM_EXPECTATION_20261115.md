# EC49FPM — Exact unrestricted expected terminal sensing for native BRC class 16995

Date: 2026-11-15. **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.** Independent portable research continuation of [EC49FPL](https://github.com/awdawmip/enterprise-math/pull/2479) and [EC49FPK](https://github.com/awdawmip/enterprise-math/pull/2476).

## Frozen scientific domain and observer

Use exactly the original source pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, original master SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, original native byte-Trie rooted-cost CSV SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. The **complete original** legal-root-domain containing configuration **16995** has 242 source configurations and **112 distinct named-root cost profiles**. There are **324 legal complete-assignment terminal integer-cost queries**. Each query uses the actual original demand incidence, byte-Trie rooted cost and named-root allocation semantics. The prior is uniform over the **112 rooted profiles**, not over the 242 original configurations. All queries have unit cost; a later query may be selected based on the integer responses to earlier queries.

## New theorem — no depth restriction

Over **all finite, exact-response adaptive terminal-query decision trees**, *without imposing any worst-case depth bound*, the least expected number of primitive scalar terminal observations is

\[
\boxed{\inf_{\mathcal T}\mathbb E[N(\mathcal T)]=\frac{238}{112}=\frac{119}{56}=2.125.}
\]

There are precisely **six optimal first-query indices**: `118, 119, 124, 201, 203, 204` in the original zero-indexed 324-terminal-action order. An optimal tree beginning with `T(118)` has **112 distinct singleton leaves**, maximum depth **4**, and depth histogram `{1:9, 2:84, 3:15, 4:4}`, giving `9+168+45+16=238`. Two further optimal roots `T(119)` and `T(204)` have maximum depth **5**, histogram `{1:13, 2:79, 3:15, 4:3, 5:2}`, and the same total 238. These show that the previously proved depth-four optimum of EC49FPL is also the unrestricted global expectation optimum; allowing an extra decision level may tie, but cannot improve, that mean.

| optimal initial query | maximum depth | leaf counts by depth 1,2,3,4,5 | path-length sum |
|---|---:|---|---:|
| 118, 201 | 4 | 9, 84, 15, 4, 0 | 238 |
| 124, 203 | 4 | 10, 84, 12, 6, 0 | 238 |
| 119, 204 | 5 | 13, 79, 15, 3, 2 | 238 |

## Proof: exact well-founded Bellman recursion, all 324 admissible queries

Encode any subset `S` of the 112 rooted profiles by its exact integer bit mask. For each legal terminal query `q`, let `F_q(S)` be the partition into classes of equal exact integer response. A query is *informative* on S when `|F_q(S)|>1`. Let `C(S)` denote the smallest total number of future query observations over all states in S in a successful decision subtree, with each state weighted one. Then

\[
C(S)=
\begin{cases}
0,&|S|\le 1,\\
|S|+\displaystyle\min_{q:\,|F_q(S)|>1}\sum_{G\in F_q(S)}C(G),&|S|>1.
\end{cases}
\]

Every informative q partitions S into **strictly smaller fibers**. Hence the recurrence is well founded under induction on integer cardinality; its minimum considers every legitimate next action. Its proof uses no depth assumption: the current query costs one for each state of S, subsequent fibers are independent because their responses are distinguishable, and a deterministic optimum exists for this finite exact menu. Uninformative queries cannot occur in a least-cost successful tree and are safely omitted. The original profiles are terminal-distinguishable; thus the minimum is finite.

Compute `C(S)` using exact Python integer bit masks and response values. The verifier initializes its search using previously established depth-four `C_4(S,4)`, which is a **valid upper bound** on unrestricted optimum; it then enumerates all 324 queries. Candidate branch-and-bound pruning at `|S| + Σ_{|G|>1}|G| >= current_best` is valid because each nonsingleton fiber requires at least one further query per state. Equal-response partitions can be deduplicated without changing any subtree cost. Enumerating all **324 first queries** yields the exact minimum total **238** and exactly the six minimizing initial indices listed. The executable verifier additionally generates all six complete response-indexed optimal decision trees and independently traverses exact integer responses for every one of the 112 rooted profiles, checking one distinct path per state and the specified weighted totals.

Verified output (exact finite run):

`EC49FPM_UNRESTRICTED_EXACT_PASS 238 112 [118, 119, 124, 201, 203, 204]`.

The same invocation first runs `VERIFY_EC49FPL.py`, which verifies original frozen bytes and reconstructs all 112 rooted profiles and 324 complete legal terminal costs from the original 38,169 configurations. All DP arithmetic is exact integer arithmetic. Local verification produced 17,944 memoized unrestricted subproblems. `VERIFY_EC49FPM.py` writes the complete 324-entry initial-cost sequence and all six complete optimal trees to a machine-readable JSON certificate; the full output and frozen inputs are included in the handoff evidence archive.

## Claim scope, provenance and next research

The theorem is **exact finite** for the declared original native BRC population, query menu, prior and unit-cost model; it gives an unrestricted decision-tree optimum within that experiment. It extends EC49FPK's fixed-query minimum 5 and worst-case adaptive minimum 4. The original 625 domain-class classification remains at its previous frontier of 565 completed and 60 outstanding; this round optimizes class16995 rather than adding a domain.

The scientific report and executable verifier are published as independent portable research, not a shared Task Result/Review. Exact directory lookup for `RS-EC49AS` returned `SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY` at Source `91c58fa3652463df2b95e1e8c32d40715c50c18e`, observed 2026-11-15T05:34:48.950537Z. Mathematical independent admission remains `NOT_REVIEWED`.

**Next question:** repeat exact unrestricted expectation optimization with the nonuniform prior induced by the 242 source configurations, then with heterogeneous terminal and named-root observation costs; investigate sensitivity and possible structural compression preserving the full named-root observer.
