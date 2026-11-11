# R76 — Persistent winner frontier for S23/AV latest-source interval queries

**Author-side mathematical and algorithmic result, 2026-11-11.** Frozen auxiliary scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. R75 predecessor `686010c8256b83123511593f3480e581352ddee9` (globally ordered phase-class heap); R74 `2021a3ab0aace0ab978bc6395e7d0e5f7bbf87c1` (complete latest-source classifier); R71 `0b5319d7a0caf90dcd210e291152c6c06bbc2828` (group exclusion); R72 `917f62a46d986a757476e0e4bc35ad603eba4fb9` (persistent identity groups). Scope is an auxiliary rational circle-source model, not native X6/BRC, a formal Task CLAIM, Result, review or Foundation admission.

## Exact domain

Finite identities `(t,branch)` with integer time `t`. Reduced rational anchor `theta0=p/q, q>0`, rational observer phase `x`, integer observation time `j`, rational closed parameter interval `I=[L,U]` containing `theta0`. Original-labelled arc `[A(theta),B(theta))` has `A(theta)=a theta-floor(aL)`, `B(theta)=b theta-floor(bL)`, constant boundary floors and `0<=A(theta)<B(theta)<1` across I. An identity is a member iff `{x+(t-j)theta}` lies in that half-open arc. We decide exactly whether the **latest qualifying time** `T(theta)` is identically NONE, identically one time, or changes within I; in the changing case return two rational parameters witnessing unequal latest times. Branch identity remains stored, although membership here depends only on time.

## Three persistent indexes

An immutable height-balanced map (reference implementation: path-copying AVL) maps phase residue `r=(tp mod q)` to a time tree. Each time tree maps distinct source time `t` to an immutable tree of all independently keyed branch identities. A third, global **winner tree** has exactly one key `(max_time(r),r)` for each nonempty residue class. Tree nodes hold exact subtree count, minimum and maximum key, height and child pointers.

**Update invariant.** Insert/delete one source identity in its branch tree. If the last branch at a time vanishes, delete that time; if the class becomes empty, delete the class. Change the affected residue path and replace at most the one old and one new winner entry. By induction on updates, the time/branch trees store exactly the current identities and the winner tree contains precisely one maximum per nonempty class. Paths are copied, preserving old version roots, same-time other branches, and all unaffected classes. With `g` nonempty groups, `n_r` distinct times in the touched class and `b_t` distinct branches at that time, each update costs `O(log(g+1)+log(n_r+1)+log(b_t+1))` AVL comparisons/path-copy nodes in the worst case, plus input-dependent integer comparison bit costs.

## Query algorithm and correctness

Start from the **stored** global winner tree (no per-query heap construction). Repeatedly extract its largest `(t,r)`. On the first encounter of residue class r, apply R71's sound group-wide exclusion certificate over I using exact anchor phase and current group min/max time. If successful, discard its winner and every remaining time from that class. Otherwise apply R74's complete two-oracle classifier to the extracted time:

- `ALL_OUT`: advance only this class to its next lower distinct time by query-local immutable pop-max, and insert its new winner if nonempty.
- `ALL_IN`: return `STABLE(t)`.
- `MIXED`: return `CHANGES(t,theta_yes,theta_no)` with the two exact rational witnesses.
- No winner left: return `STABLE_NONE`.

**Theorem.** The result agrees with global descending full-time R74 classification for *every real theta in I*. Invariant: at each iteration the largest winner is the maximum remaining time over all nonexcluded classes. Earlier discarded times were proven absent either by an all-real R71 exclusion or an all-real R74 `ALL_OUT`. Hence the first non-ALL_OUT time in this procedure is the first in the complete descending order. R74's theorem gives exactly the claimed three-way latest-time answer. Original arc endpoints and equal-time branch identity are preserved. The query's working winner/time roots are copy-on-path temporary objects and never alter a historical stored root.

**Cost scope.** A query visiting `g_v<=g` classes and examining `k` distinct times incurs `O((g_v+k)log(g+1)+sum_visited log(n_r+1))` AVL comparisons/path copies plus `O(g_v+k)` exact rational certificate/oracle calls. There is **no required per-query O(g) heapify** as in R75; constructing/updating the stored winner tree instead costs work at source-update time. Worst-case inspection remains linear in the number of distinct source times; full integer bit costs, update-vs-query trade-offs and memory retention require workload-specific accounting.

## Executed exact verification

Deterministic Python `fractions.Fraction`, seed **761126**: 36 random models, **3,600** persistent insert/delete steps, **720** old-version identity checks, and **512** identical complete all-real interval queries compared with the full globally descending R74 reference. All assertions passed. **200** changing queries had exact rational witnesses checked against the direct latest-time predicate. Sum of query metrics: **574** entire class exclusions; **871** distinct source-time entries skipped by those class exclusions; **476** per-time R74 classifications; **1,040** first-visits to classes. Every constructed AVL tree was checked for height, balance, count, min/max and search-order summaries; all historical identity sets matched an independent Python set.

R71's two-phase family `C_N={(4k,branch_k),(4k-1,other_branch_k):1<=k<=N}` at `theta0=1/4`, `I_N=[1/4-1/(100N),1/4+1/(100N)]`, target `[theta,2theta)` was tested at 32,128,512,1024 identities. All 20 queries at each size certified `STABLE_NONE` with exactly 2 whole-group exclusions and zero per-time checks; full index-build and per-query times are in `verification.json`. The reference scanner shares R74's predicate implementation: this checks the new persistence/ordering/pruning integration, not a second independent proof of the R74 predicate.

## Residual and next problem

This index retains all source times and branches, old-version roots, original arc labels and observer signatures. A new `j,x` reuses classes but recomputes query certificates; changing anchor can change group residues and needs regrouping. It does not transfer to P000's native time or six-axis dynamics without a separately typed mapping.

**R77 next:** Compare this maintained-winner index with R75 per-query heapify on complete matched outputs across update-heavy/repeated-query workloads, measuring rational integer-bit work, per-update path-copy allocations, history memory and query cursor costs; construct an exact original-label boundary partition for target arcs whose order/floor changes, including one-point cells and half-open endpoints.
