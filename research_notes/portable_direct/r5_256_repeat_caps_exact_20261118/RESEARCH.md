# R5: 256-state repetition-cap capacity and exact capped fixed-batch optima

Date: 2026-11-18 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

Frozen science: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. Exact 101-budget / 256-mask count table `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. Costs are the physical query budgets `k=214,...,314`. This is the derived scalar center-count observer with named state identities; it makes no native-X6, signed-provenance, path or future-operation quotient.

## Theorem 1 — exact error capacity under per-budget caps, including adaptive protocols

For each named pair `a<b` and real noise diameter `tau=2eta`, define its separating-budget set
```
D_ab(tau) = { k : abs(N_a(k)-N_b(k)) > tau }.
```
A good real readout under state h at budget k is any y with `abs(y-N_h(k)) <= tau/2`; at most `f` readings may be unmarked arbitrary corruptions. If budget k may be queried at most `q_k` times on **each adaptive execution path**, guaranteed identification exists if and only if
```
  min_{a<b} sum_{k in D_ab(tau)} q_k >= 2*f+1.                 (1)
```

**Necessity:** choose a pair violating (1). At any nonseparating query, the two closed good-response intervals intersect, so the adversary supplies a shared correct value. At a separating query, choose a value intact for one state and incompatible with the other, balancing the two states' accumulated mismatches. There are at most `2f` separating occurrences on any path, so both candidates remain compatible with at most f corruptions. The learner observes the same transcript and cannot identify the true one, regardless of its adaptive query selection or stopping. This online balancing argument uses the declared per-budget caps, not a predeclared query order.

**Sufficiency:** query every k exactly q_k times in a fixed batch. If two states both fit the resulting transcript with at most f corrupted readings, each disjoint-interval position forces a mismatch for at least one of them. Their combined mismatch count is thus at least the LHS of (1), which exceeds 2f. Therefore exactly one state survives. This proves the sharp capacity criterion even for fully adaptive protocols. It does not equate adaptive and batch *costs*.

For a selected fixed-batch multiplicity vector `0<=n_k<=q_k`, the same proof gives the exact finite covering criterion
```
sum_{k in D_ab(tau)} n_k >= 2f+1  for every a<b,            (2)
```
with cost `sum_k k*n_k`.

## Theorem 2 — all fifth-chamber signatures have one five-set antichain

Let
```
L = 25845652773852463277015040000
C = 53550705027838197293383680000
U = 58182461585441404127941754880
```
For every real `L<=tau<U`, the 32,640 named pair-separation sets among all 101 budgets have **exactly five inclusion-minimal members**. They are:

| Group | `L<=tau<C` | `C<=tau<U` | actual representative pair |
|---|---|---|---|
| A | 214–219 inclusive | 214–218 inclusive | (9,12) |
| B | {214,216,217,218,219,220,221} | same | (1,2) |
| C | {215,216,217,218,219,220,221} | same | (2,8) |
| D | 223–290 inclusive | same | (0,64) |
| E | 296–312 inclusive | same | (16,32) |

The 17 exact internal center-gap thresholds create 18 half-open real observation signatures. An integer-only exhaustive checker regenerates these thresholds from all 25,856 pinned centers, constructs all 32,640 separation sets at **each of the 18 signatures**, and checks the antichain above at every threshold, including equality. At (9,12), the budget-219 center difference is exactly C, so that query ceases to separate the pair at `tau=C`. The full antichain has no other phase transition.

Consequently the minimum number of separating *distinct* physical budgets is
```
d_min(tau) = 6 for L<=tau<C; 5 for C<=tau<U.
```
When every budget may be used at most q times per path, the **exact largest correctable number of unmarked arbitrary errors** and required minimum cap are
```
f_max(q,tau) = floor((q*d_min(tau)-1)/2), q>=1;
q_min(f,tau) = ceil((2*f+1)/d_min(tau)).
```
In particular, no-repeat use (`q=1`) corrects at most **two** errors throughout the fifth chamber, and the fixed schedule using each of the 101 physical budgets once attains two. To tolerate **eight** arbitrary errors requires maximum per-budget multiplicity at least **3** below C or **4** at/above C; the full q-fold 101-budget batch attains feasibility.

## Theorem 3 — unique minimum-cost fixed batches at the minimum feasible f=8 repetition caps

All pairwise inequalities (2) are equivalent to the **five group constraints** above, since every pair-separation set contains one of the five inclusion-minimal ones. Group A/B/C involves only budgets 214..221; groups D and E are disjoint intervals with strictly increasing positive physical costs. Thus the exact integer optimization decomposes into three blocks.

**Early phase** `L<=tau<C`, `f=8, q=3`:
- low: 214,215,216,217,218,219 each 3 times; 220 twice (cost 4337)
- middle: 223,224,225,226,227 each 3 times; 228 twice (cost 3831)
- high: 296,297,298,299,300 each 3 times; 301 twice (cost 5072)
- **unique optimum: 54 readouts, cost 13240**.

**Late phase** `C<=tau<U`, `f=8, q=4`:
- low: 214,215 each 3 times; 216,217,218 each 4 times; 219 twice (cost 4329)
- middle: 223,224,225,226 each 4 times; 227 once (cost 3819)
- high: 296,297,298,299 each 4 times; 300 once (cost 5060)
- **unique optimum: 54 readouts, cost 13208**.

The lower-priced feasible query occurrences in D/E must be used first by a strict exchange argument, giving unique sorted greedy schedules. The low block is certified by **complete exhaustive enumeration** of its eight integer multiplicities `n_214,...,n_221` over `0..q`. The checker inspects `4^8=65536` vectors for q=3 and `5^8=390625` for q=4, tests the three exact inequalities, and finds a **unique** minimum-cost low vector in each case. Independent direct verification then checks each complete candidate optimal schedule on **all 32,640 named pairs** at both phase endpoints (integer `C-1` and `U-1`). Every phase has the same five-set antichain, proving the stated costs for all real tau in that phase.

The larger-noise subchamber has a marginally lower optimal batch cost **under a larger minimum repetition cap** (q changes 3 to 4). These capped fixed-batch optima sit above the previously published unrestricted-repetition full-256 fixed-batch value 12495 for f=8. The unrestricted full-adaptive eight-error bound stays `8335 <= C_8^*(tau) <= 8343`.

## Reproduction and next question

Execute the standard-library verifier against the frozen input:
```sh
python3 VERIFY_R5_REPEAT_CAP.py EXACT_R5_ALL_101_BUDGETS.json > RESULTS_R5_REPEAT_CAP.json
```
Expected `PASS_R5_256_REPEAT_CAP_BATCH_18_CHAMBERS_EXACT`; the verifier checks input SHA-256 and emits all 18 exact phase results, threshold census, five-set antichain, low-block enumerations, optimal budgets and direct pairwise coverage. The original frozen count table is present in the earlier R5 complete reproduction packages. The present author proof/exact calculations require independent review (`NOT_REVIEWED`).

**Next:** solve adaptive minimum cumulative cost *under these sharp per-budget caps*, retaining the full 256 named-hypothesis error counts and comparing against 13240/13208. Separately continue the unrestricted `f=8` gap `8335..8343`. No CLAIM, formal Result, independent review or P000 change is asserted by this scientific note.
