# R5 fifth-chamber f=8: exactly five distinct physical query-budget values suffice and are necessary on H12

Date: 2026-11-18 (Asia/Shanghai).
Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scope: frozen R5 **scalar integer-center observer only**; this is not an identification of native P000/X6 residual states or a formal Task Result.

## Input and statement

Frozen semantic/scientific source: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Exact 101 × 256 count table `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.
The unchanged original input is carried by earlier R5 portable reproduction packs. These input bytes were checked before the new calculation.

Let `H12=(18,24,82,34,17,0,1,2,3,144,208,255)`, and consider physical query costs `k=214,...,314`. A normal observation for h at k belongs to `[N_h(k)-tau/2,N_h(k)+tau/2]`; up to `f=8` responses may be arbitrary, unmarked errors. A strategy must identify the named state, minimizing its worst-case **sum of physical query costs**. Write

```
L = 25845652773852463277015040000
U = 58182461585441404127941754880
L <= tau = 2 eta < U
```

**Theorem (cardinality-constrained optimality, entire chamber).** Let `C8^{<=q}(H12;tau)` be the infimum worst-case cost of strategies using at most `q` *distinct physical budget values*, repetitions and adaptive choices allowed. Then, throughout `[L,U)`,

```
C8(H12;tau) = 8335,
C8^{<=4}(H12;tau) >= 8343,
C8^{<=5}(H12;tau) = 8335.
```

Consequently **exactly five distinct physical query-budget values are necessary and sufficient to attain the unrestricted optimum 8335**. One sufficient set is `{214,215,216,223,296}`.

The quantitative gap of at least 8 for four-value protocols is a *budget diversity constraint*; it does **not** assert the full 256-hypothesis game has cost 8335. That larger problem retains `8335 <= C8^*(tau) <= 8343`.

## Exact finite proof

For any fixed k and tau, merge identical exact integer centers, and form the family `F_k(tau)` of inclusion-maximal hypothesis subsets compatible with a single normal real answer: all named centers lying in an interval of width tau. They are obtained by scanning intervals starting at every distinct center and deleting proper-subset supports. Arbitrary corruptions are counted by per-hypothesis mismatch counters `e_h`, saturated at `f+1=9`. Given response support S, update `e_h <- min(9,e_h+1[h not in S])`; stop when at most one `e_h<=8`. This gives a finite, acyclic Bellman minimax recursion after useless self-loop actions are discarded. A query yielding a full-set support with no progress is not optimal in a positive-cost worst-case game.

Two physical budgets sharing the same maximal-support family are information-equivalent for this game; the cheapest representative never increases cost. Thus any at-most-four-physical-budget strategy may be replaced with at most four distinct cheapest family representatives.

**Four-budget lower bound at the easier left endpoint L.** Across all 101 physical budgets there are exactly ten cheapest maximal-support families on H12. One is the uninformative full-support family. The nine informative cheapest representatives are:

`214,215,216,221,222,223,294,295,296`.

There are `C(9,4)=126` four-family sets. For **117** sets, some pair of distinct hypotheses remains compatible with a common ordinary observation at every selected budget (`|N_h(k)-N_g(k)|<=L` for every k), so identification is impossible at any finite error bound. For the remaining **nine** sets, complete exact Bellman calculations give:

| Four cheapest representatives | Exact f=8 cost at L | Bellman states |
|---|---:|---:|
| 214,215,223,296 | 10244 | 1214930 |
| 214,216,223,296 | 8343 | 1253965 |
| 214,221,223,296 | 8444 | 1220965 |
| 215,216,223,296 | 8343 | 1251356 |
| 215,221,223,296 | 8444 | 1199755 |
| 216,221,223,296 | 8343 | 1071136 |
| 216,222,223,296 | 8343 | 1151417 |
| 216,223,294,296 | 8343 | 1065569 |
| 216,223,295,296 | 8343 | 1220732 |

Every at-most-three-budget strategy is covered as well, since adding a fourth available budget cannot worsen its optimum. Hence `C8^{<=4}(H12;L)=8343`; by monotonicity under noisier normal observations, `C8^{<=4}(H12;tau)>=8343` for the entire chamber.

**Five-budget upper bound at the harder right endpoint.** At `tau=U-1`, the same exact solver restricted to the *five* physical budgets `{214,215,216,223,296}` returns

```
EXACT_RESTRICTED n=12 f=8 V=8335 states=3539792 actions=5
```

As all 256-state count centers are integers, for real `tau<U` their compatibility relation is contained in the one at `U-1`; the five-budget policy remains valid. Prior frozen H0 evidence establishes `C8(H0;L)=8335`, with `H0={18,24,82,34,17}` included in H12. Hypothesis-set and noise monotonicity yield the unrestricted lower bound 8335 everywhere. Thus upper and lower match, completing the proof.

## Reproduction, limitations, next scientific question

The actually executed input-checking verifier `VERIFY_R5_H12_F8_MINIMAL_FIVE.py` reconstructs all 101 maximal-support families, proves all 117 four-budget failures by explicit uncovered pairs, performs the nine finite four-budget Bellman calculations at L, and the five-budget Bellman computation at U-1. `RESULTS_MINIMAL_FIVE.json` includes every computed value/state count and machine stdout. Its solver is the unchanged `VERIFY_EXACT_SMALL_MINIMAX.cpp` from the earlier R5 finite-solver certificate at Git commit `8acd30cbf9312afde72d0da39cbf57107c14ad48`.

Reproduce with `g++ -std=c++17 -O3 -DNDEBUG VERIFY_EXACT_SMALL_MINIMAX.cpp -o exact_small`, supply the SHA-pinned input table in this directory, and execute `python3 VERIFY_R5_H12_F8_MINIMAL_FIVE.py`. The run printed

`PASS_R5_H12_F8_MINIMAL_FIVE_QUERY_BUDGET_TYPES left_four_subsets=126 pairwise_impossible=117 four_finite=9 left_four_min=8343 right_five=8335 right_five_Bellman_states=3539792`.

This is a reproducible finite proof for the stated named H12 problem, not an independent external review. No formal CLAIM/Result/Review/Task completion is asserted.

**Next:** test whether a similar five-budget strategy attains 8335 on larger populations, and whether any 13+ named subset forces more than 8335 at f=8. If not, seek an analytic decomposition of the 256-hypothesis lie-counter game rather than an unbounded full-state search.