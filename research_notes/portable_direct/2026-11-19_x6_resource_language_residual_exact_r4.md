# X6 native-time observer V — exact resource-history residual and minimal future-language repair

Date: 2026-11-19 (Asia/Shanghai). Author-side **conditional finite typed-event model**, with a separate port-memory automaton; no claim of native Cell/Link/Port event admission. Researcher provenance: current same-line issued session `MCP-d467c19ce42d4d7fa65a3901db1cf6b2` / `EM-X6-214D9C` / `RA-545183ADD4EF71C3E4698AEE`, registration request `research2-20261119-0113-native-self-register-v1` actually returned `SUCCEEDED`; registered identity does **not** grant CLAIM, execution or mathematics acceptance. Formal Task line `RS-X6-NATIVE-TIME-DYNAMICS`, immutable task publication `TP2-91D4A7C2F63805BE21A3`; frozen scientific foundation `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.

## Motivation and exact inheritance

Reuse the saved proof `b107eb05fd28b21e0cce0b4315402cc888b99aef:research_notes/portable_direct/2026-11-19_x6_arbitrary_crosslinks_mixed_phase_future_fibers_r3.md`: in an acyclic two-chain *precedence-only* model, the legal count support at rank k is an interval and its phase fiber requires at most `ceil(log2(ceil(W(k)/lcm(pA,pB))))` bits to recover a source-count cut. That argument depends on the fact that the future guard depends only on current event counts. A dynamic shared port or resource may instead remember event order. The precise new question is whether a retained resource-state bit is mathematically necessary **even when all local counts and decorated phases are known**.

P000 context: six signed integer spatial axes remain the primitive X6 space, time is a separate event/order coordinate; single primitive nonzero stable balance requires three actions satisfying `TRIADIC_CLOSURE_E`. The resource controller below is a **conditional candidate observer/guard**, not a derivation of the native triadic admissibility predicate. Its alphabet A/B designates two *already admitted hypothetical* source-event families, not an attempt to replace the three-force rule.

## Definitions: finite labelled BRC carrier with a port controller

Fix a,b >= 1, periods pA,pB >= 1, a finite controller-state set Q, initial state q0 and a partial deterministic controller `delta: Q x {A,B} -> Q`. Optionally add any count-dependent precedence guard. A branch is a legal **source-labelled word**; a state is `s=(i,j,q)`, where i,j are consumed counts of A/B and q records the controller. One guarded append x increases its corresponding count by one, respects upper capacities (a,b) and all declared guards, and changes q by `delta(q,x)`. The total event rank is k=i+j, separate from physical duration.

The Boolean BRC support map from a collection of labelled branches to its set of reachable `(i,j,q)` states commutes exactly with both guarded append operators: the future transition is fully determined by these three retained fields. This assertion is only about Boolean reachability and the source-labelled future interface, not weighted, signed or amplitude observations.

Let `R_k^+` be states reachable by a legal prefix **and coaccessible** to some full (a,b) completion. For s in `R_k^+`, define `L(s)` as its nonempty finite set of complete remaining source-labelled words. The declared observer is

    O(s)=(k, i mod pA, j mod pB).

For each count vector (i,j), define

    N(i,j)=#{ distinct nonempty complete languages L(i,j,q):
                  (i,j,q) belongs to R_{i+j}^+ }.

The count `N(i,j)` counts equivalence classes of *future languages*, not merely raw controller states.

## Theorem I — exact history-sensitive repair formula

Set `P=lcm(pA,pB)`. At fixed rank k, the maximum number of future-distinguishable states sharing a single local phase/count observation is

    M(k)=max_{r in {0,...,P-1}}
              sum_{0<=i<=a, 0<=k-i<=b, i = r (mod P)} N(i,k-i).

The optimal worst-case number of added fixed-length selector bits preserving all full source-labelled future languages is

    b_resource(k)=ceil(log2 M(k)),

where `b_resource(k)=0` for `M(k)=1`. A uniform selector over ranks takes `max_k b_resource(k)` bits.

**Proof.** With fixed k, equality of the two complete local phase readouts is precisely `pA | (i-i')` and `pB | ((k-i)-(k-i'))`, equivalently `P | (i-i')`. At a fixed (i,j), two reachable port states are indistinguishable by the full-completion future observer exactly when their nonempty language sets are equal, so this count vector contributes `N(i,j)` classes. For *different* count vectors with the same k, any full completion from (i,j) has exactly a-i occurrences of A, whereas a full completion from (i',j') has a-i' occurrences; when i != i', these totals differ. Their nonempty completed-word languages are disjoint, hence cannot be the same class. Summing the per-count language-class numbers over one phase residue yields the number of necessary classes in that observer fiber. Maximizing yields M; `ceil(log2 M)` bits are necessary and sufficient by a finite injective index within each observed fiber. QED.

Coaccessibility excludes dead prefixes with no full completion. Since every productive legal finite continuation is a prefix of at least one complete continuation, preserving the declared complete languages also preserves all *productive* partial-future possibilities.

**Exact finite algorithm.** Recursively compute a future-language signature backwards in k, without materializing its potentially exponential word set. For a terminal (a,b,q), let `S=END`. For each nonterminal s, discard transitions whose child has no complete continuation; let `S(s)` be the ordered tuple of pairs `(source label, S(child))` for its remaining productive outgoing transitions, or `NONE` if none. By induction on remaining length and disjoint first-letter decomposition, signatures are identical iff the full completion languages are identical. Hash-consing these finite DAG signatures gives the N(i,j), M(k) and optimal bit counts. Complexity is O((a+1)(b+1)|Q| times two) for constructing/hash-consing the reachable product-state DAG under constant-time guards, apart from dictionary/comparison overhead; the exact checker also enumerates complete words only on its **small bounded test domain**.

When Q is a singleton and every legal count cut is extendible, N(i,j)=1 on the exact legal support, so Theorem I reduces to the previously proved phase-fiber result, rather than contradicting it.

## Theorem II — a one-bit resource residual at arbitrarily long finite horizons

For every integer m >= 2, take a=b=m and pA=pB=m+1. Let Q={INIT,LAST_A,LAST_B}; both sources are initially permitted, and thereafter **only the source different from the last one may append**:

    INIT --A--> LAST_A; INIT --B--> LAST_B
    LAST_A --B--> LAST_B; LAST_B --A--> LAST_A.

All other transitions are undefined. There are exactly two complete labelled paths:

    ABAB...AB  (length 2m), and BABA...BA (length 2m).

At the even interior rank k=2r, 1 <= r < m, both histories have the *same exact* counts (r,r), hence the same phases and total k; however their last-used port differs, and their next permitted source must differ. Their full completion languages are distinct singletons with opposite leading letters. Therefore M(2r)=2 and b_resource(2r)=1.

At odd ranks their A/B counts differ by one; because pA,pB=m+1>m, the local phases distinguish them, giving M(k)=1. Initially there is one state; at final rank 2m both terminal states have the same complete future `{epsilon}`, and may merge safely. Consequently the **exact** memory profile is

    b_resource(k) = 1 if k in {2,4,...,2m-2}; 0 otherwise.

This holds for every m>=2. The corresponding precedence-only count interval has maximum width m+1<=P=m+1, so the old count-only formula gives zero bits for that **different guard class**. Thus a nontrivial port-state residual survives even when there are no count/phase collisions. An instantaneous count quotient `(i,j,q)->(i,j)` is not operation-safe in this family.

**Smallest displayed witness (m=2).** A B A B and B A B A are both completed trajectories. After two events the prefixes AB and BA have identical observation `(k,phiA,phiB)=(2,1,1)` and identical exact counts (1,1), but

    L(AB) = {AB};     L(BA) = {BA}.

The correct lossless future observer needs one additional bit at k=2, and does not need it at the terminal cut.

## Reproducible bounded validation

Companion standard-library checker: `x6_resource_future_language_brc_verify.py`, local executed SHA256 `9ec032a6ad21b80ec3d8c184b56bba4d528b3007419530eedd7d1c012feeee35`. Result: `x6_resource_future_language_brc_results.json`, local executed SHA256 `f0385f77cdd854e0b20a65d002a6f6be646834b20b097ae57499f25b05389e74`. Run `python3 x6_resource_future_language_brc_verify.py > x6_resource_future_language_brc_results.json`.

Checker independently compares recursive signature equality with *all explicitly enumerated complete suffix-word sets* for every reachable productive state-pair of the same rank. It exhaustively enumerates all `3^4=81` partial deterministic controllers with Q={0,1} (each of the 4 source/state transitions is absent or chooses either state), 9 pairs a,b in 1..3, and the four period pairs (2,2),(2,3),(3,3),(3,4): **2,916** model-period cases, **1,404** admitting at least one complete trajectory. In this exact finite test domain, **32** cases have a reachable same-count source-phase observation split by distinct resource future languages; **153** cases have at least one nontrivial observation fiber (including ordinary count collisions). These are model counts, not independent native physical validation.

Additionally, the alternating family m=2,3,4,5 passed the asserted complete memory profiles [0,0,1,0,0] through [0,0,1,0,1,0,1,0,1,0,0]. The infinite-m result is supported by its direct proof, not by extrapolation from four tests. All calculations are exact discrete finite sets/integers; no trigonometry, native spatial projection, physical time calibration or signed amplitude is introduced.

## Immediate native-transfer question

Inspect the frozen original native `TRIADIC_CLOSURE_E` update and actual Cell/Link/Port compatibility predicate. Find two **native-admissible** histories which agree on the observed six-dimensional coordinates, current phase and local source counts but disagree on a future permitted event due to an occupied/released named Port. If such a pair is certified, determine its exact minimal named-port/controller repair; if no pair exists in the native admissible domain, prove the relevant native guard factors through the smaller observer. The present theorem supplies an exact test/decoder once the native permission automaton and source-to-event map are verified.

Project status when authored: original read-only requests `r2-20261119-0206-x6-current-frontier-ro` and `r2-20261119-0206-x6-task-ro` returned `FAILED/SOURCE_TREE_BLOB_SIZE_INVALID`. The formal live owner/CLAIM therefore remained unverified; the science may be saved as portable author-side material, with the independent own Activity and any formal native PROGRESS evaluated separately. No retry of either failed request was submitted.
