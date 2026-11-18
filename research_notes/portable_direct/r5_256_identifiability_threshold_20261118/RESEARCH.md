# R5 — Sharp 256-state identification threshold and near-critical four-query theorem

**Date:** 2026-11-18. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

**Scientific model.** Freeze source at 435e77af0d180eac32bd1f9c4c464bc4010b7551, exact counts SHA256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. There are exactly 256 named hypotheses h=0,...,255, and exactly 101 allowed future scalar readout budgets k=214,...,314. A correct real readout under hypothesis h lies in [N_h(k)-eta,N_h(k)+eta]; up to f observations may be arbitrarily corrupted without markers, tau=2eta>=0. Costs of queries are their integer budgets. Only this frozen scalar observer is modeled; native signed X6 path, joint relation and provenance are retained outside the declared observer quotient.

## Theorem 1. Sharp finite-identifiability boundary for all f

Let

D = 1882951873548292168718745600000
  = min_{0<=a<b<256} max_{214<=k<=314} |N_a(k)-N_b(k)|.

For **every f>=0 (integer)** and **every real tau>=0**, a finite guaranteed 256-state identification strategy with up to f unmarked arbitrary corruptions exists **if and only if tau<D**. Adaptive querying is permitted in this statement.

**Proof.** For tau<D, every pair of distinct hypotheses is separated by at least one legal budget: their correct real-reading intervals are disjoint. Ask every one of the 101 budgets q=2f+1 times. A common transcript compatible with both a and b within f corruptions would need >=q separated observations charged to <=2f errors, impossible. Thus the fixed batch guarantees identification. For tau>=D, take any pair attaining D. Every one of their 101 correct-reading intervals intersects; an adversary answers each requested query with a point of intersection. The same transcript is then consistent with both hypotheses using zero errors, even under adaptive scheduling, so guaranteed identification is impossible. The checker exhaustively establishes D over all 32,640 unordered pairs and 101 budgets.

Exactly **eight** pairs attain D:
(11,14), (27,30), (43,46), (59,62), (75,78), (91,94), (107,110), (123,126).
For each, at the gap threshold D, only budget 217 separates it.

## Theorem 2. Final chamber: unique cheapest zero-error fully prepaid fixed batch

Let

T = 1876919155234970890319953920000
  = max{ |N_a(k)-N_b(k)| : a<b, k legal, |N_a(k)-N_b(k)|<D }.

For every real tau with **T<=tau<D**:

1. A fully prepaid observation-independent fixed identification batch at f=0 needs **at least four distinct physical query budgets**, and four suffice.
2. The **unique cheapest batch up to ordering** is (217,218,224,298), with total cost **957**.
3. Budget 217 is compulsory in any successful identification design in this chamber. Every fixed batch tolerating f unmarked errors uses **at least 2f+1** repetitions of budget 217.
4. Repeating each of 217,218,224,298 exactly 2f+1 times guarantees identification for any f, giving the constructive upper bound 957(2f+1). No optimality for f>0 is claimed by this upper bound.

**Proof.** All observed integer gaps below D are <=T, and there are no observed gaps in (T,D). Hence for tau in [T,D), exactly the gaps >=D give separated correct-reading intervals. The eight critical pairs can be separated only by 217. Build a 32,640-bit pair-separation bitset for each of 101 budgets. All C(100,2)=4,950 candidate triples containing 217 fail full pair coverage. Exactly **1,876** of the C(100,3)=161,700 candidate four-budget sets containing 217 cover every pair. The unique minimum total budget among them is (217,218,224,298), sum 957. Five or more prepaid queries always cost at least 5*214=1070>957, and repeats do not help at f=0, proving global cheapest-batch uniqueness. The usual pair-distance criterion d(a,b)>=2f+1 proves the fixed-batch claims for f>0.

**Reproducibility.** The accompanying standard-library Python checker accepts the unchanged frozen 256x101 integer source EXACT_R5_ALL_101_BUDGETS.json as its only argument. It checks its SHA256; every pair/budget gap with arbitrary-precision integers; D, T, all eight critical pairs, sole separating budget 217, all 4,950 triples, all 161,700 four-budget candidates, uniqueness and cost. Recorded local exit code 0; stderr PASS_R5_SHARP_IDENTIFIABILITY_THRESHOLD_AND_NEAR_CHAMBER. The separate RESULTS_IDENTIFIABILITY.json contains the exact measured output. The 954-event source-to-count derivation is inherited from frozen pin and not recomputed.

**Previous frontier preserved.** Fifth noise chamber L<=tau<U (L=25845652773852463277015040000, U=58182461585441404127941754880) retains the earlier fully prepaid fixed-batch theorem 735(2f+1) with 216,223,296. The present result is a different, more noisy chamber and the global information limit for the specified scalar observer.

**Next question.** Solve the exact multicover fixed-batch optimum for general f in [T,D), and the earliest tau at which no three-budget identifying set exists. Independently review the frozen-count provenance and independent proof.
