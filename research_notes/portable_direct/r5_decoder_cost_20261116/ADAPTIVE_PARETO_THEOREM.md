# R5 addendum — Adaptive three-query Pareto frontier closes at the same three points

Date: 2026-11-16. Frozen input `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Scope: derived 954-indexed-event radius-two integer-count observer, original 28 closure bits, eight effective bits. Existing parent paper: `r5_decoder_cost_20261116/RESEARCH.md`. Status: AUTHOR_PROVED / EXACT_FINITE_INTEGER_CHECKED / NOT_REVIEWED.

## Theorem

Among *all deterministic exact, adaptively selected, three-budget scalar-count decoders*, with worst-case sum-of-center-budgets bounded above by T and uncompressed positive-integer bit counts, the exact minimal worst-case sum of bit lengths for T from 731 through 799 has nondominated cost pairs

| Maximum budget sum | Best worst raw bits | Attaining fixed triple |
|---:|---:|---|
| 731 | 319 | (214,223,294) |
| 798 | 317 | (214,290,294) |
| 799 | 305 | (214,291,294) |

For budget cap 731..797 the optimum worst raw-bit count is 319, at 798 it is 317, and at 799 it is 305. **Adaptive budget choices offer no improvement over the corresponding fixed optimum for this two-resource problem.** For T>799 the fixed 799-budget decoder remains pointwise optimal in bit length, by the parent theorem, so the entire nonnegative-budget Pareto frontier is precisely the three points above. No exact decoder can use fewer than three scalar queries.

## Proof by admissible observer normalization and finite certificate

A correct three-query decision-tree leaf must contain one query from each of three private-bit windows A, B and C. Since A or B cannot observe either C-private bit, its one C query must distinguish all four C local masks; the prior finite classification proves it belongs to K=294..313. The B query must be K=223..291 to see private bit25. The A query must be K=214..221 to see private bit3.

The parent exact finite test proves that for *each* input the count bit lengths at A=214 are no greater than those at any other A budget, and likewise C=294 is no greater than any valid C budget; both also minimize their respective K budgets. Because A=214 uniquely identifies all five local A bits and C=294 uniquely identifies both local C bits, a decoder can **simulate the original A or C readout** in exact postprocessing after the replacement. This preserves every original adaptive branch and B-budget choice, while spending no more center budget or bits. Thus A=214 and C=294 may be fixed without loss in any optimal adaptive strategy.

Their combined K is 508. If total center-budget expenditure is at most T, the B budget lies in [223,min(291,T-508)]. Query A first; it determines the shared bit27, while bit25 remains entirely unknown. The smallest possible worst B count width on a known value r of bit27 is

    b_r(T) = min_{223<=k<=min(291,T-508)} max_{p in {0,1}} bit_length(N_{b=(p+2r)}(k)).

The A bit-length maximum conditional on either r=0 or r=1 is exactly 102; the independent C maximum is exactly 99. Since the C bits are unrelated to A and B and B sees neither, any exact adaptive protocol has the sharp minimax value

    R(T) = 99 + max_{r in {0,1}} [102 + b_r(T)].

It is attained by the explicit strategy: query A=214; decode r; select a B budget attaining b_r(T); query C=294. Its B count distinguishes both possible values of private bit25 at every permitted k. The standard-library integer DP and explicit min-max sweep over all 69 budget caps T=731..799 gives R(731..797)=319, R(798)=317 and R(799)=305, with **zero adaptive-versus-best-fixed gap at every budget cap**. Checking all four B local masks independently supplies the exhaustive finite certificate. QED.

## Evidence

Companion `VERIFY_R5_ADAPTIVE_PARETO.py` reuses the exact frozen reconstruction, closure transform and positive-integer center-count spectrum from `r5_minimum_scalar_queries_20261116/VERIFY_R5_ALL_TRIPLE_DECODERS.py` at immutable scientific source commit `143ada28910f2b0e042d2d0ffcb066fee45d083e`. It checks the needed A and C pointwise domination inequalities, all four B masks at every K=223..291, all 69 budget caps and direct nonadaptive comparison. It returns `PASS_R5_ADAPTIVE_COST_FRONTIER_EXACT`. The JSON file contains all nondominated points and equality of adaptive and fixed optimum.

This result prices **only raw uncompressed count bits and sum of queried K values**, not query signaling, DP evaluation time, source-coordinate encoding, or native X6 path/port semantics. The input event-generator and complete optimizer-observer assumptions are those pinned in the parent R5 work.

## Next

Investigate realistic full computational cost, including generating 954 events, exact DP state count, integer arithmetic bit-complexity and output serialization; analyze adaptive benefits under asymmetric per-query computation penalties. Resume exact min-old/max-new recourse for K214..291 when this new cost frontier has been integrated into an application-level comparison.
