# R5 — Exact classification and minimum total cost of robust fixed scalar queries (2026-11-17)

**Frozen scientific input:** `435e77af0d180eac32bd1f9c4c464bc4010b7551`. **Prior coefficient source:** `compact_stdout.json`, SHA-256 `a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent R5 portable research, with no claim of Task CLAIM, Result, Review or native X6 quotient admission.

## Fixed-query model and new theorem

The frozen 954-event radius-2 indexed-center *derived integer count observer* has eight effective cut switches U=(3,8,9,10,15,17,25,27), masks b=0,...,255, budgets K=214,...,314, and exact optimal path counts N_b(K).

For a fixed set Q of distinct integer query budgets, set

    G(Q) = min_{0<=b<c<256} max_{K in Q} |N_b(K)-N_c(K)|.

Independent adversarial real observations with |y-N_b(K)|<=eta guarantee decoding exactly when 2eta<G(Q), including strict boundary at equality. Reuse prior sharp results D3=1744659037213380157479321600000 (best three-query margin) and D4=1882951873548292168718745600000 (best four/unlimited margin). Here we newly **classify all margin-optimal fixed schedules and minimize additive budget cost** C(Q)=sum(Q). This does not purport to measure CPU time or output bit size.

Let E={214,...,221}, M={223,...,291}, L={293,...,314}.

**Theorem 1 (three calls):** Every fixed three-budget set Q with G(Q)=D3 is exactly

    Q=(217,m,l), 224<=m<=290, 298<=l<=311.

There are 1*67*14=938 such sets. The unique minimum-total-budget set is (217,224,298), total 739. The previously given (217,290,305) totals 812, so the same sharp absolute error threshold eta<D3/2 is attained using 73 fewer budget units.

**Theorem 2 (four calls):** Every fixed four-budget set Q with G(Q)=D4 is exactly

    Q=(217,e,m,l), e in {218,219}, 224<=m<=290, 298<=l<=311.

There are 2*67*14=1876 such sets. The unique minimum-total-budget set is (217,218,224,298), total 957; the earlier (217,218,224,305) totals 964. The smallest largest queried budget among saturated four-query sets is 298.

## Proof and complete exact finite certificate

The prior pinned coefficient representation satisfies N_b(K)=sum_{T subset b} A_T(K). The readout dependency windows are exact: flipping bit 0 (cut 3) affects only E, bit 6 (cut 25) only M, and bit 4 (cut 15) only L. A successful transcript must query all three disjoint windows. Thus a three-query set contains exactly one early, one middle and one late budget.

All 16 masks F={0,...,15} have identical readouts outside E. Define s1(k)=min_{b<c in F}|N_b(k)-N_c(k)|, and s2(k,k')=min_{b<c in F}max(|N_b(k)-N_c(k)|,|N_b(k')-N_c(k')|). Exhausting all 120 pairs in F establishes

    {k in E: s1(k)>=D3} = {217};
    {{k,k'} subset E: s2(k,k')>=D4} = {{217,218},{217,219}}.

Since max_E s1=D3<D4, any four-query set attaining D4 must use two early queries; private middle/late switches then force exactly one M and one L. Thus all relevant fixed schedules are contained in 8*69*22=12,144 triples and choose(8,2)*69*22=42,504 quadruples. The other budgets, such as 222 and 292, cannot substitute for mandatory private-switch window queries at these limits.

For a positive integer D, assign the 32,640 unordered mask pairs positions in an integer bitset and define U_D(k)={(b,c):|N_b(k)-N_c(k)|<D}. Exact equivalence:

    G(Q)>=D  <=>  intersection_{k in Q} U_D(k) is empty.

The Python standard-library verifier reconstructs all 25,856 counts by subset Zeta sums; builds all 101 bitsets for both D3 and D4 with arbitrary-precision integers; exhausts all 12,144 and 42,504 candidate schedules; and asserts that the surviving sets equal **exactly** the rectangular families in Theorems 1 and 2. This proves exclusions and attainability, not just matching sample counts. For the D4 global upper bound, masks 11 and 14 have gap at most D4 over every budget, achieving the maximum uniquely at K=217; the D3 bound is the 16-mask early fiber.

The middle private-cut gap reaches both D3 and D4 precisely on 224..290, and the late four-mask minimum gap reaches both thresholds precisely on 298..311. The full pairwise intersection check establishes that no mixed cross-window state pair adds an exception. Minimizing C(Q) over each finite rectangular family gives both unique stated minimizers.

## Reproducibility and remaining work

Execute `python VERIFY_R5_FIXED_BUDGET_COST.py /path/to/compact_stdout.json`. The input SHA-256 and frozen science pin are checked. The output `RESULTS_EXACT.json` records `PASS_R5_FIXED_QUERY_ABSOLUTE_NOISE_COST_CLASSIFICATION`, 938 and 1876 qualifying sets, and their exact minimum-cost witnesses. This is *exact postprocessing* of a previously verified integer coefficient table, not a new independent 954-event dynamic programming run.

Scope: fixed **nonadaptive** scalar-budget schedules, integer budgets 214..314 and additive sum-of-budgets cost. The next questions are the minimum **adaptive worst-case total budget cost** at these noise thresholds, the path-level explanation for early budget 217 and its 218/219 partner, and the separate indexed-center max-new/min-old center-set replacement distance. All observer provenance and P000 constraints remain at their established scopes.
