# R749STX — A local provenance window and bounded POP have an additive exact memory radius

**Date:** 2026-11-18 (+08:00). **Evidence:** AUTHOR_EXACT_NOT_REVIEWED. **Mode:** independent portable TASK_RESEARCH; no shared Task CLAIM or native event admission.

**Predecessor:** R749STW, immutable commit 2f0f17bcf0709b6f6b3bc8eeffff856a13999528. Frozen scientific input pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This research does not change P000, ACTIVE worldview, or the scientific pin.

## Exact question and scope

R749STW showed that at a fixed raw endpoint, if the only history-revealing operation is at most r lifetime POP calls, the last min(r,ell) source labels are sufficient and optimally minimal. We investigate whether adding a read-only, local source-order guard changes that quotient.

Keep the native ambient six signed X6 axes, an anchor Cell, separate time type, and the five *named* positive-step sources A,B,C,D,E of scalar weights (1,1,2,3,6). Sources use raw axes 1,...,5 in this selected symbolic adapter; axis 6 is fixed at raw zero relative to the chosen anchor but not removed from native spatial ontology. Each path is a composite sequence of primitive signed axis steps. No physical triadic event, rotational dynamics, phase cancellation or installed native Port guard is assumed.

For fixed source-composition vector n=(n_A,...,n_E), ell=sum n_i, let W(n) be all ordered source words with counts n. Every word has the same endpoint and scalar total. On a positive path-formal BRC branch [w] permit:

* APPEND_i([w])=[wi], publicly selected i;
* POP([wi])=(i,[w]), outputting the removed named source, with at most r calls throughout the entire adaptive experiment;
* PEEK_t([w]) = the ordered last min(t,|w|) source labels, where t is fixed. PEEK may be invoked after every operation, costs no POP budget, and does not mutate the path.

Readouts include the raw endpoint, scalar total, POP labels, PEEK windows, and operation legalities. There is no cloning, budget reset, direct hidden-history access beyond PEEK, or other history oracle. This is an *explicitly defined candidate provenance Port interface*, not a claim that PEEK_t is a native physical Cell/Link/Port event.

## Main theorem — additive radius

For any nonnegative integers t,r, let s=min(ell,r+t). Then two words of W(n) are indistinguishable by **every** allowed future experiment, including adaptive interleavings of public APPEND, POP and PEEK, **if and only if their last s original source labels coincide**.

Define the feasible suffix count:

\[
N_s(\mathbf n)=
\sum_{\substack{0\le a_i\le n_i\\ \sum_i a_i=s}}
\frac{s!}{\prod_{i=1}^5 a_i!}.
\]

The precise number of future-observation classes is N_s(n). The sharp additional fixed-width memory, given composition and full raw endpoint, is

\[
\boxed{b_{r,t}(\mathbf n)=\lceil\log_2 N_{\min(\ell,r+t)}(\mathbf n)\rceil.}
\]

**Distinguishability.** If two last-s suffixes differ at depth d from the right, where d<=s, for t=0 POP d times (d<=r). For t>0, PEEK at once if d<=t; otherwise POP d-t<=r times and then PEEK. Earlier diverging POP outputs already establish distinguishability. Shared length means this sequence is legal for both candidates.

**Non-distinguishability.** Run any adaptive experiment in parallel from words sharing their last s labels. Every APPEND letter is publicly chosen, so newly appended letters are equal while observations agree. Of at most r POPs, at most r can remove *original* labels; removing appended letters spends rather than replenishes the budget. A PEEK accesses at most t original labels below the deepest removed original label. Thus no output or legality can inspect an original letter deeper than r+t from the original end. All accessible original letters coincide (or the whole word is saved when r+t>=ell). Induction on the action sequence gives identical future endpoints, labels, PEEK results, resource budgets, and legalities; hence all adaptive choices coincide.

**Minimal code.** A length-s suffix with counts a_i is feasible exactly when a_i<=n_i and sum a_i=s. Summing multinomials gives N_s. A b-bit code has at most 2^b values, giving the lower bound. Lexicographic feasible-suffix rank and unrank attain it. The exact subtree count is F(c,0)=1 and F(c,u)=sum_{i:c_i>0} F(c-e_i,u-1); scanning the source alphabet and skipping preceding subtree sizes yields a bijection with integers [0,N_s-1]. This constructs an optimal fixed-width residual carrier for the declared interface.

## New information loss and capacity

| Composition n | t | r | POP-only classes / bits | PEEK+POP classes / bits |
|---|---:|---:|---:|---:|
| (2,1,1,1,1) | 2 | 1 | 5 / 3 | **72 / 7** |
| (2,2,2,2,2) | 3 | 2 | 25 / 5 | **2220 / 12** |

The effective lookback is r+t, **not max(r,t)**. If each source count is at least s, N_s=5^s, so the bit bound saturates at ceil(s log_2 5). For a mixed composition of length ell, r+t>=ell-1 suffices to distinguish every complete history, because the omitted leading letter is then determined by the known counts.

**Minimal falsification of an unqualified R749STW transfer:** The words AB and BA have identical raw X6 endpoint and scalar total. With r=0, the old endpoint/POP-only interface does not distinguish them. Adding just PEEK_1 gives outputs B and A. Thus the old r=0 quotient is not a congruence for this *enlarged* operation alphabet. R749STW itself remains correct under its original observer. This difference is a genuine source-order residual, not an extra spatial dimension or a signed-amplitude cancellation.

## Native BRC Port boundary

The established positive-rational recurrent BRC Port theorem WBRC-T31 in definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md allows boundary-context extensions by visible port/external edges and forbids connections to, or mutations of, hidden internal state. Its Schur collapse preserves precisely that port-boundary observer. PEEK_t exposes internal ordered provenance and is **not** among WBRC-T31's licensed contexts. The AB/BA witness consequently does not refute WBRC-T31 or establish an actual X6-native triadic Port event.

To transfer this paper to a native event, first identify the actual Cell/Link/Port guard, resource predicate, causal ordering, and signed/phase provenance readouts; prove that each permitted operation descends to the proposed suffix-state quotient. A weaker Boolean guard could have strictly fewer classes than N_{r+t}; the full-window result is not automatically sharp for it.

## Verification

The accompanying Python standard-library checker computes only integers. **Author execution: PASS.** It exhaustively enumerated all five-source words of length 0 through 7 (97,656 words), 792 fixed composition fibers, and 12,672 (composition,t,r) cases for t,r=0,...,3. A separate observation-signature oracle records every intermediate PEEK window and emitted POP label. Across every case, its classes matched feasible suffix classes, a recursive count and an independent multinomial sum; it performed 423,392 exact rank/unrank checks. These tests are finite regression evidence; arbitrary interleaved APPEND and unlimited lengths rely on the proof above. Complete machine results: R749STX_WINDOW_PEEK_POP_RESULTS.json. Executable: R749STX_WINDOW_PEEK_POP_CERT.py.

**Strength:** exact author proof and reproducible integer checks, not independently reviewed; no native physical BRC operation executed, no formal Result/Review or shared CLAIM asserted. No probabilistic or floating-point approximations.

## Next frontier

Select an *actually licensed* native source-sensitive Port event and derive its exact permitted future observer; determine whether it factors through PEEK_t for a proven finite t, through a smaller source-guard automaton, or needs unbounded provenance memory. For a native Boolean guard, calculate its coarsest future-stable quotient instead of treating the present full-label bound as exact.

Sources: R749STW (immutable 2f0f17bcf0709b6f6b3bc8eeffff856a13999528), P000 V4/V5 and ACTIVE residual-fidelity worldview, definitions/00_CURRENT_NATIVE_FOUNDATION.md, definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md, definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md and project observer-preservation contract.