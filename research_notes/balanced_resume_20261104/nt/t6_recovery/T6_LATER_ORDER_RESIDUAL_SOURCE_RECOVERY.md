# T6 later-order residual: exact source recovery and remaining input gap

Author: `/root/research_nt_1104`. Source snapshot: `39556bf5207aa5ba559a27ec591c1bc1bf43b457`. Date: 2026-11-04 UTC.

This is one bounded, read-only source-recovery unit for `EM-T6-SHAPE-MOMENT-EXACT-THRESHOLD`. It recovers the concrete q14 continuation plan behind the older “later-order residual” placeholder. It does **not** recover an actual later-order local survivor, exact residual moments, or the survivor's remaining side budgets. The recovered plan expressly records that its roster, counts and executable had not been constructed. No scientific enumeration, affine search, moment-cut evaluation or formal state transition was performed in this unit.

## 1. Exact task and accepted frontier

The actual global Task is `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`, publication `TP2-34B106D2512A298C9647`; its parent is `OG-F252ABC3F5BB7B9499E7`. Its taskbook is `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md`. The mother question remains whether the sixth exact shape-moment threshold is 2332 or there is a collision with **each** side exponent mass at most 2331.

The taskbook's original p19 order-9 entry is historical. Later accepted p17 units must be consumed before choosing new work:

| Unit | Immutable Result | Accepted review | Scope consumed here |
| --- | --- | --- | --- |
| q1 | `RR-81586AD70E1CEA1B7140` | `DR-A550BA4AE2C2C51AA899` | 12 admissible affine classes EMPTY, 4 OUTSIDE. The 4 are not asserted to be relaxation-empty. |
| q2 | `RR-AD107A4A930BFF07FAB9` | `DR-B02CEB5F5E99A5D947AE` | All 272 literal systems EMPTY. |
| q3, Gen2 | `RR-9E4EA0B85D8DB82A3607` | `DR-9766FCC689761D44EF3F` | All 3264 literal systems EMPTY. |
| q4 | `RR-FC5B70D043CE518DAD0B` | `DR-8C4DDD770323FD58FC52` | All 30992 literal systems EMPTY, including 10212 admissible and 20780 outside; zero full sphere leaves. |

`SOURCE_BINDING.json` gives exact paths and hashes of all four Result/return/review-record/review-paper chains. This unit rechecked every Result hash named by its accepted review, every return hash named by its Result, and every review-paper hash named by its review record. These are byte/link checks, not reruns or independent mathematical reproofs. Historical “review pending” text in an earlier Result is superseded by its actual later accepted review, not silently edited.

Consequently these four accepted units provide no admissible local survivor on which to apply lower-prime completion cuts. The q4 follow-up `DFU-063C9F1D5465667226E2` creates no successor and leaves the mother open. No automatic q5 ladder is inferred.

## 2. Recovered later-order source

The useful locator is the following Source directory:

`driver_reviews/mcp/MCP-10b3bf1d95f645ce8c0e419e458a2e49/3a113cad9007f35a7c79/`

Its readable `T6_CURRENT_FRONTIER_AND_SINGLE_Q14_DIRECTION.md` has SHA-256 `7af7f3a362fc7d1f2a1681c806eb9d7b2481b229c31a00cf1cc00c0ab41b796e`. Its `T6_Q14_DIRECTION_AND_PAPER_BOUNDARIES_CAPSULE.json` has SHA-256 `3427bf39499df944a3cd65376f7bb6298042abed206b50991f5088c7079952a8`. Decompression recovered and verified all 23 members; four scientific/planning documents were retained under `source_extract/`. `CAPSULE_RECOVERY_RECEIPT.json` records the container and each member's actual byte/hash agreement.

The final, not draft, member `T6_ORDER14_SINGLE_CONTINUATION_EXECUTION_SPEC.json` has SHA-256 `b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24` and 18938 bytes. It selects maximal-p17 total vertical order 14 with split `(7,7)`, in the original global Task. This is a precise generative family, not an actual frozen family roster or a solved affine case.

The source's mathematical input specification is:

* A vertical atom `(q,r)` has denominator `17(17q+r)` and exponent cost `289q+17r−1`, with `1≤q≤7`, `1≤r≤16`, and all prime factors of the cofactor `17q+r` at most 17.
* Each one-sided multiset has positive integer multiplicities, weighted order `Σ m(q,r)q=7`, and exponent cost at most 2331. Repetitions and composite cofactors remain present.
* The complete one-sided roster is lexically ordered. Pairs use `i<j` and disjoint atom supports, quotienting only the whole sign. Common-support cancellation falls into lower orders that remain separate obligations.
* The q0 system retains all 16 signed coordinates at denominators `17s`, weights `17s−1`, and all six exact mixed congruences. Only the common kernel/weights/basis/Gram–Schmidt data can be reused; old R1 right-hand sides, particulars, centers, budgets and radii cannot seed q14.

The source's static bound gives vertical cost at least 2039 on each order-7 side, hence **pre-q0 budgets at most 292 per side** and a necessary sphere bound `R²≤170528`. These are bounds on a family. They are not an actual affine center, q0 solution, residual moment vector or final lower-prime budget.

The capsule explicitly has `q14_roster_cardinality=null`, `q14_primitive_pair_N=null`, `q14_roster_sha256=null`, `q14_executable_created=false`, and `scientific_enumeration_or_affine_execution=false`. The final spec likewise records no generated roster or pair count. Its subsequent `MF1_FROZEN_FINAL_REVISION_READBACK_ADDENDUM.json` resolves a plan-text challenge while explicitly leaving actual code, roster, count and concrete budget admission unproved. The Oct15 static-support intake records actual roster cardinality and whole-budget pass as null. The Oct16 source audit recovers the same plan and does not supply an executed candidate. These are positive source statements of a missing input at those checkpoints; the bounded search below is not a universal absence proof.

## 3. What the old completion tool actually consumes

The earlier exact caller is `driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/7592bca554f5d835bc7c/T6_P17_ORDER1_SMALL_BRANCH_THEOREM.md`. Its interface requires a genuine signed-budget-feasible local solution before forming residual moments. Its then-open q1 search is now superseded by the accepted q1 return.

The following equations merely recompose that same interface for general signed vertical multiplicities; they are not a newly instantiated case or a claim of a new theorem. Let `t_(q,r)∈Z` be the retained vertical multiplicities, let `a_(q,r)=17(17q+r)`, and let `u_s∈Z`, `1≤s≤16`, be the actual q0 vector. With positive and negative parts denoted by `x⁺=max(x,0)` and `x⁻=max(−x,0)`, define

\[
V_\pm=\sum_{q,r}(a_{q,r}-1)t_{q,r}^{\pm},\qquad
P(u)=\sum_{s=1}^{16}(17s-1)u_s^+,\quad
N(u)=\sum_{s=1}^{16}(17s-1)u_s^-.
\]

The required mixed congruences are

\[
\sum_s u_s s^{-k}\equiv-\sum_{q,r}t_{q,r}(17q+r)^{-k}\pmod {17^k},
\qquad 1\le k\le6.
\]

Only after an actual vector passes these congruences and both side budgets do we obtain the completion caller

\[
M_0=\sum_{q,r}t_{q,r}+\sum_su_s,\qquad
M_k=\sum_{q,r}\frac{t_{q,r}}{a_{q,r}^{k}}+
\sum_s\frac{u_s}{(17s)^k}\quad(1\le k\le6),
\]

\[
B_+=2331-V_+-P(u)\ge0,\qquad
B_-=2331-V_--N(u)\ge0.
\]

The remaining atoms are affordable 13-smooth integers `a≥2`, including composites, with cost `a−1`. Their signed multiplicities `c_a` must satisfy `Σ c_a/a^j=−M_j`, `0≤j≤6`, and the separate positive/negative costs bounded by `B_+` and `B_-`. The mixed congruences cancel the p17 denominator obstruction; they do not solve this completion problem.

This distinguishes four different objects that must not be conflated:

1. The old q4 representative modulus `17^6=24137569` is not the residual vector `(M_0,…,M_6)`.
2. A q14 pair's pre-q0 budgets `2331−V_±` are not its post-q0 budgets `B_±`.
3. The family bounds `B_±≤292`, conditional on a valid q14 local survivor, are not exact values for a named candidate.
4. An old portable R1 particular vector or a demonstration moment vector is not a newly recovered local survivor.

## 4. Existing coupled-moment cuts are ready; their caller is absent

The Oct28 author paper `research_notes/balanced_resume_20261028/analysis/T6_COUPLED_MOMENT_COMPLETION_CUTS_AUTHOR.md` and distinct `review/T6_MOMENT_REVIEW.md` already establish the 21 dual budget cuts from

\[
f_{h,k}(x)=x^k\prod_{b=2}^{h+1}(1-bx),\quad h\ge1,\ k\ge0,\ h+k\le6.
\]

For `f=Σq_jx^j`, their existing constant `C=max_a f(1/a)/(a−1)` on the admissible 13-smooth atom dictionary gives

\[
-CB_+\le\sum_jq_jM_j\le CB_-.
\]

The first two are `−B_+/6≤M_0−2M_1≤B_-/6` and `−B_+/18≤M_1−2M_2≤B_-/18`. The source includes budget-specific versions and certified finite constant reductions. This unit does not recompute them or create another cut family. The paper's relaxed separating example is expressly not an actual p17 survivor and is unusable as a practical rejection result. Its `NEXT_ACTION_DECISIONS.json` names the exact missing fields: genuine later-order `M_0,…,M_6`, nonnegative remaining budgets, and the actual caller publication/execution provenance.

Thus no named candidate was rejected or retained here. If a future candidate violates a cut, its classification is **local feasible but lower-prime completion excluded**, not retroactively affine EMPTY.

## 5. Bounded recovery and its limit

`BOUNDED_SEARCH_PATHS.json` preserves fixed-string path discovery for `T6_ORDER14`, `T6_Q14`, `q14_roster`, `later-order residual` and `M0..M6` within the frozen snapshot's research notes, returns, tasks, artifacts, driver reviews, Result records and driver follow-ups. The matching scientific q14 sources and later Oct15/Oct16 status references were inspected. The exact selected 23-member capsule was decompressed and all member bytes verified. Not every compressed member in the repository was recursively searched; this is not a global GitHub or live-MCP absence claim. The inventory's six declared T6 parent leaves give useful task locators, not current ownership or exhaustive unpublished work.

Recovered: exact q14 continuation specification, immutable member bytes, accepted q1–q4 scope, caller equations, and the gap between the q14 plan and the ready Oct28 completion tool. Not recovered: an actual later-order signed vertical pair with accepted q0 vector, its seven exact rational moments and its two exact remaining budgets. The newer Source frontier is therefore **q14 plan exists; actual caller not present in recovered evidence**, rather than simply “look for later-order M”.

## 6. Actionable support request and next scientific decision

`SUPPORT_REQUEST.json` is a local handoff for the parent owner, not an API request or shared-state mutation. First ask the responsible current T6 source custodian, through the parent's authorized workflow, for an immutable actual later-order local-survivor packet if one exists. The exact requested fields are: case ID and order/split; publication and Result/checkpoint provenance; signed vertical atom multiplicities and cofactor admissibility; the 16 signed q0 coordinates; all six mixed-congruence checks; both exact side masses; seven reduced rational moments with the sign convention above; both exact nonnegative remaining budgets; and hashes of the generating input/code/certificate. A bounded path lookup for the real record is sufficient; no historical identity should be reused.

If no actual survivor has been constructed, the recovered q14 plan's first work item is an **author-side roster/preflight**, not completion cuts and not a rerun of q1–q4. Its old declared stop budgets were 120 seconds, 1 GiB and serial concurrency 1; the later affine phase had separate 600-second/2-GiB limits. Those are historical plan limits, not measured usage, promised completion, present execution authority or a new approval requirement created here. The real roster, pair count, exact ordered inputs, code, resource accounting and applicable current execution rules must be established before deciding whether that separate scientific unit is worthwhile. Missing M alone does not justify starting affine enumeration in this source-recovery unit.

Current decision: preserve this recovery and return it to the owner for balanced allocation. No new scientific computation is needed to establish the source facts in this report. Global T6, p17 orders 5–13, the q14 family, lower maximal-prime branches and full H0/lower-prime completion remain open within the stated evidence boundary.

## 7. Execution and attribution disclosure

Operations in this unit were reads, fixed-string filename discovery, JSON field inspection, Base64/gzip/tar source recovery, and SHA-256/Git-blob byte checks. No scientific executable or old checker was invoked. Consequently there is no typed-BRC run, ordinary-arithmetic science run, finite-census outcome or native residual-attribution claim to admit. Any later scientific computation must classify its actual objects and applicable current BRC/portable scope before running; this report grants no execution exception.

The actor is `/root/research_nt_1104`, not any historical T6 author or Driver quoted above. No claim, lease, registration, formal review vote, task status, objective status or shared canonical record was changed. This is source-frontier recovery and a reusable caller contract, not a new threshold theorem or additional completed census.
