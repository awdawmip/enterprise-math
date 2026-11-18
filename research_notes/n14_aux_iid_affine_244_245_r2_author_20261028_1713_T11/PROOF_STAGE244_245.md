# Stage244–245: two exact all-real N=14 IID minimax segments

**Research status:** AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. Original author-side parent: Stage243, commit 0c522c040132b11794adea98967f97a6f51506af, existing draft PR #1571. External auxiliary IID model only; no native P000/X6 transfer, canonical Source CLAIM/Result or Driver mathematical acceptance.

## 1. Statement

Let N=14 and let each observation take values 0,1,2 independently under two hypotheses, with P=(3,1,20)/24 and Q=(2,2,20)/24. A possibly randomized sequential rule may inspect the complete ordered history and must output P or Q by time N. Write eP=P(output Q), eQ=Q(output P), tP=E_P τ, tQ=E_Q τ, and

V14(α) = inf{ max(tP,tQ): eP≤α and eQ≤α }.

The previous Stage243 endpoint is

α243 = 4372969427965/11702381838336,
V243 = 10415008236599/1462797729792.

**Stage244 theorem.** For **every real** 0≤δ≤1765157155/11702381838336,

V14(α243+δ) = V243 − (201435849912/1765157155)δ.

The right endpoint is α244 = 136710455785/365699432448 and V244 = 324682148605/45712429056.

**Stage245 theorem.** For **every real** 0≤δ≤47846585971/1828497162240,

V14(α244+δ) = V244 − 88δ.

The right endpoint is α245 = 2/5, V245 = 24/5.

Neither theorem asserts the formula outside its interval; Stage245's time-dominance inequality becomes equality at α=2/5.

## 2. Universal Bellman dual lower bound

For count state s=(n,a,b), a=#symbol 0 and b=#symbol 1, every history w with this count has Q(w)/P(w)=r_s=2^(a+b)/3^a.

For positive rational λP and λQ, compute exactly the finite-horizon Bellman recursion

B(s) = min{λQ r_s, λP, 1 + Σ(j=0..2) P_j B(s+j)},

where the continuation action is omitted at n=14. This is a scalar Lagrangian certificate for tP+λP eP+λQ eQ. Because its lower bound holds pathwise after mass weighting and finite induction, it covers all stopping/output policies, including full-history-dependent randomization. Let H=B((0,0,0)); then

max(tP,tQ) ≥ tP ≥ H − λP eP − λQ eQ ≥ H − (λP+λQ)α.

At Stage244 the exact dual is

λP=96950297784/1765157155,
λQ=104485552128/1765157155,
H=57363048204634793377/1152708874580404224.

Exhaustive Fraction Bellman computation checks **all 680 states**, exactly **14 binary ties** (P/C at (n,1,0), n=1..13; Q/C at (2,1,1)), and **1226 positive action gaps**, minimum 34069364/1765157155. The slope magnitude is λP+λQ=201435849912/1765157155. It is strictly below Stage243's 33611704152/292565255 by 15872371200000000/20656946126705981>0.

At Stage245 the dual is

λP=40, λQ=48, H=40.

Again all 680 Bellman states are checked. Exactly **27 binary ties** occur: Q/C at the root and at (n,0,0), n=1..13, and P/C at (n,1,0), n=1..13. There are **1213 positive gaps**, minimum 296/6561. The slope magnitude 88 is strictly smaller than the Stage244 slope. The Stage245 support equals V244 at α244 exactly.

## 3. Full-history scope and legal convexification

Both hypotheses put a positive mass on every finite ordered word. Given the same count state and survival to that state, the conditional law of the ordered histories is the same under P and Q: Q(w)/P(w)=r_s, and the survival factor from the policy multiplies both likelihoods identically. Hence averaging a full-history policy's action at a state over these histories can be done consistently under both hypotheses. The resulting Markov randomized rule preserves the four joint observations (eP,eQ,tP,tQ) at the declared finite horizon. A direct alternative for the *lower bound* is to use the exact count-dependent Bellman potential along each original history, without quotienting histories at all.

A count state is visited at most once along any sample path (n increases). For any finite horizon, every randomized Markov policy is a convex combination of deterministic action tables. Stage244 can therefore check the complete polytope by enumerating the 2^14 tied-action tables. At Stage245, a complete recursive two-dimensional *projection* certificate replaces 2^27 naive table enumeration, retaining the original full-observation witnesses wherever time comparisons are needed.

This sufficiency statement applies to this external finite IID model, not to P000 X6 residual dynamics or generic BRC provenance quotient.

## 4. Stage244: exact 16,384-corner primal certificate

Let D=24^14; for each deterministic Bellman-optimal tie table let

X=D(eP−eQ), Y=D eP.

The executed STAGE244_EXACT_REPRO.py computes (D eP,D eQ,D tP,D tQ) independently by (i) exact integer suffix DP, and (ii) **unmerged full-ordered-history integer P/Q branch-mass DFS**, for all 2^14=16,384 tied-action tables. The two implementations match on every one of **1,441,798 traversed ordered-prefix nodes**. They all satisfy the exact Lagrangian equality tP+λP eP+λQ eQ=H. There are 12,280 distinct (X,Y) integer points; their exact convex hull has 4 vertices.

For a segment with endpoints u=(x1,y1),v=(x2,y2) sorted by X, define M_uv(X,Y)=(Y−y1)(x2−x1)−(y2−y1)(X−x1). Exact integer comparison across **all 16,384** policies proves two global supporting inequalities:

Lower: A=(-2972925671028817920,6586558925383925760);
B=(3250719450805043200,9253835406169866240);
M_AB(X,Y) ≥ 0.

Upper: C=(-3210930030792146944,6487730030792146944);
E=(3268357523094110208,9264567553886257152);
M_CE(X,Y) ≤ 0.

Intersecting these global supports with X=0 proves the **complete** balanced error interval [α243,α244] of this dual face, not merely selected examples.

The lower endpoint is a mixture of tie-table masks 5 and 16383 with weights 620025530015/1187066101424 and 567040571409/1187066101424. Its exact error is α243, time tP=V243, and tP−tQ=1535520971813/2925595459584>0.

The upper endpoint mixes masks 0 and 16379 with weights 194809289163/386195633047 and 191386343884/386195633047. Its exact error is α244, time tP=V244, and tP−tQ=47846585971/91424858112>0.

An independent forward P/Q mass computation checks all four endpoint tables. Convexly mixing these two endpoint randomized policies at the **root**, with any real probability, achieves eP=eQ=α and tP≥tQ throughout [α243,α244], thus attains the dual lower bound for every real α.

## 5. Stage245: exact projected-error-polytope induction with provenance repair

There are 27 Bellman ties at this support, so enumerating 2^27=134,217,728 deterministic action tables is unnecessary. The key theorem is an exact recursion for the conditional **two-dimensional error feasible polygon** K_s of all Bellman-optimal policies at state s, represented by integer numerators with denominator 24^(14−n).

For a stop P action the pair is (0,24^(14−n)); for a stop Q action it is (24^(14−n),0). For a continuation action the exact child contribution is the Minkowski sum

K_s^C = diag(3,2)K_(s+0) + diag(1,2)K_(s+1) + diag(20,20)K_(s+2).

Set K_s = conv( all pairs from Bellman-minimizing actions ). This is an **induction over all randomized suffix policies**: after the next observed symbol, each child policy can be selected independently; randomization is convexification. Linear maps commute with convex hull, and conv(A)+conv(B)=conv(A+B), so replacing each child candidate set by its full exact convex hull loses **no** possible error pair. Consequently a finite vertex-only Minkowski recurrence computes the complete error projection of the much larger optimal-policy polytope. Only integer addition, multiplication and 2D determinant signs are used.

The crucial **observer repair**: this 2D projection is only certified for the error-pair observer, *not* for tQ. Each retained vertex also carries its four original integer observations and a nested ordered-prefix policy tree; among duplicate error vertices, retaining a lower-tQ witness is sufficient for construction, though not an assertion that the entire four-observation fiber is preserved. All retained vertices satisfy tP+40eP+48eQ=H.

The exact implementation STAGE245_EXACT_POLYTOPE.py processes all 680 count states. The complete root error polygon has 16 vertices (max intermediate polygon size also 16); 419 raw Minkowski candidate pairs are tested across the recurrence, each passed through exact integer convex hull. Both global support edges crossing eP=eQ are:

Lower: (-3210930030792146944,6487730030792146944) to (3268357523094110208,9264567553886257152), giving α244.

Upper: (-3210930030792146944,6487730030792146944) to (21035720123168587776,21035720123168587776), giving α245=2/5.

Both are certified by integer determinant inequalities at **every root hull vertex**. The lower witness agrees exactly with the Stage244 upper witness and has tP−tQ>0. The upper witness mixes the ordered two hull-vertex policies with weights 313456656384/361303242355 and 47846585971/361303242355, yielding

eP=eQ=2/5, tP=tQ=24/5.

A separate **unmerged ordered-history** DFS follows each of the four endpoint origin policy trees, traversing 403 ordered nodes in total, and agrees in every (D eP,D eQ,D tP,D tQ). Convexly mixing the two endpoint rules at the root covers every real α in [α244,2/5], preserving eP=eQ and tP≥tQ; it attains the universal lower bound H−88α, proving Stage245.

**Do not extrapolate:** tP=tQ at α=2/5 is a genuine potential active-constraint transition. The one-time tP-only Lagrangian may not support the next interval.

## 6. Verified execution evidence, BRC boundary, and task continuation

Actual local runs (Python Fraction plus exact integers):

STAGE244_EXACT_AUTHOR_PASS 16384 ordered_nodes 1441798
STAGE245_EXACT_POLYTOPE_PASS 16 ties 27 candidates 419 DFS_nodes 403.

Complete executable sources: STAGE244_EXACT_REPRO.py and STAGE245_EXACT_POLYTOPE.py, each producing a detailed exact JSON certificate. Full generated certificates and original stdout are contained in the accompanying portable author archive, with SHA256 manifest. A GitHub source blob is a source/readback, **not a claim that GitHub executed code**.

BRC method: preserve exact positive P and Q path mass separately with ordered provenance. Count-state compression is only allowed after the declared IID/four-observer future-operation sufficiency proof. Stage245's error-only polytope projection retains the full four-observation origin witnesses as a repair coordinate. This is BRC-compatible reuse (REUSE_APPLIED), **not a claim that native typed BRC executables ran**. There is no asserted X6 embedding, native Cell transition, three-dimensional layer, P000 physical assertion or prediction.

Fixed scientific inputs: GLOBAL_KNOWLEDGE_V1 verified main 646b7d31d3ff72bc25b6acce385d37cf772b65e9; Enterprise Math main c7f79d39ca57cc242320915f6d92ae244492b5d4; Stage243 parent 0c522c040132b11794adea98967f97a6f51506af. Native gateway v0.6.11 reports research_authority_granted=false and bounded owner query returned CONTROL_QUOTA. No Source-native session, active CLAIM, frozen Result, independent Driver mathematical admission or Foundation status is asserted.

**Stage246:** right of α245=2/5, reconstruct a mixed-time Bellman dual θtP+(1−θ)tQ+λP eP+λQ eQ, 0≤θ≤1; prove a nonzero all-real next segment using time-balance constraints or supply a finite exact rational obstruction. A pure 2D error projection is not necessarily enough; retain four observations and time-difference information. Preserve earlier author Stage244/245 frontiers unchanged and avoid duplicate claims.
