# R5: Uniform action dominance eliminates 93 of 101 physical query budgets

Date: 2026-11-18 (Asia/Shanghai). Mathematical status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Frozen scientific object

Scientific commit: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Exact count table: `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. It provides integer centers `N_h(k)` for all 256 distinct named hypotheses `h=0,...,255` and permitted physical query budgets `k=214,...,314`. A query costs its physical budget `k`.

For known real diameter `tau=2 eta`, a good response under `h` lies in the closed interval `[N_h(k)-tau/2,N_h(k)+tau/2]`; up to any fixed integer `f>=0` responses may be arbitrary unmarked corruptions. The objective is unrestricted adaptive worst-case cumulative physical-query cost, permitting repeated queries and response-dependent stopping. Set:

```
L=25845652773852463277015040000
U=58182461585441404127941754880
```

## Theorem: safe eight-action core for the entire fifth noise chamber

For **every real `L<=tau<U`** and **every nonnegative integer `f`**, there exists an optimal full-256-state adaptive strategy using only

```
Kcore={214,215,216,217,223,294,295,296}.
```

For every one of the other 93 budgets `k`, there is a *single strictly cheaper* `j=j(k)` in `Kcore` that is uniformly at least as informative for the declared adversarial observation model throughout the entire noise chamber. Therefore the 93 actions can be removed from an exact full-state minimax solver without changing its value, for arbitrary finite allowed error count. Eight is the size of the core under this particular **single-cheaper-action dominance** criterion; no claim is made that eight is an absolute minimum across arbitrary multistage query replacements.

### The replacement lemma

For action `k`, let `S_k(y)={h: |y-N_h(k)|<=tau/2}`. Let `F_k(tau)` be the inclusion-maximal nonempty sets among all real-observation supports `S_k(y)`.

If `j<k` and every `S in F_j(tau)` is contained in some `T in F_k(tau)`, then any identifying adaptive policy that queries `k` at a node can query `j` instead and simulate a `k` response: map the observed `j` support to an enclosing member of `F_k(tau)`, using deterministic tie-breaking. A correct `j` response under the true `h` yields a correct simulated `k` response; an incorrect `j` response yields at most one incorrect simulated response. The number of simulated corruptions along the transcript cannot exceed the actual count. Supports empty under all hypotheses (possible for an arbitrary corrupted response) are mapped to an empty-support `k` observation. Thus the old policy's guarantee against at most `f` corruptions is preserved at strictly lower query cost. Iterated substitution produces an eight-action optimum, retaining all per-hypothesis independent error counters.

### Exhaustive certificate for all real tau in the chamber

The exact Python verifier reconstructs every maximal response-support family from two independent algorithms: sorted center windows and closed-interval endpoint sweeps. The family depends on `tau` only through which center gaps `|N_a(k)-N_b(k)|` are at most `tau`. The interval `[L,U)` contains precisely **17 distinct internal center-gap thresholds**, hence **18 signatures** (the initial `L` and all internal thresholds, including equality cases). The following complete internal list is reproduced by the verifier:

```
31733751127607820618301440000
33469190642398873308364800000
34543510342031429735546880000
35645376700628923507015680000
37332609562231335844577280000
37683829464034286984232960000
39667188909509775772876800000
41430175083265765807226880000
42621568083499305947627520000
45392032647559604256815185920
46856866899358422631710720000
48261746506570227190333440000
48344386483465039223193600000
50203785963598309962547200000
53550705027838197293383680000
54156731525066818867691520000
55313691201594187327733760000
```

Every listed threshold stands for the following half-open real interval up to the next threshold; the correct-response intervals are closed, so threshold equality is incorporated. The verifier examines **1,818** complete response-support families (101 actions times 18 signatures) by both independent algorithms. For each discarded action, it verifies an explicit cheaper direct replacement in `Kcore` across all 18 signatures. Each of the eight retained actions has a concrete counter-support witness to single-cheaper-action dominance for every cheaper budget. All arithmetic is exact integer/bitset arithmetic.

Executed result: `PASS_R5_FULL256_UNIFORM_93_ACTION_DOMINANCE_ALL_F` (exit code 0; 3.57 s local run), with proof script `VERIFY_R5_UNIFORM_QUERY_DOMINANCE.py` and result `RESULTS.json`. The finite exhaustive certificate establishes the concrete support containments; the replacement lemma proves the all-`f` cost-optimality transfer.

## Progress and next scientific question

The outstanding fifth-chamber target remains `8335<=C_8^*(tau)<=8343`. The exact full-256 eight-error Bellman recursion may restrict itself to the eight listed actions, preserving all 256 distinct named hypotheses and their independent possible error counts. Next: implement this 8-action recursion and a certified pruning/lower-bound strategy to determine whether the optimum is 8335, 8343, or an intermediate value. The 294/295 response branches may be investigated as potential further reductions, while preserving their actual information.

This is a theorem about the pinned finite scalar observer, not a native-X6 hypothesis quotient or modification of protected P000. Prior zero-error and query-alphabet theorems in existing Draft PR #2427 are reused. Source control request `r5-20261118-1345-inventory-reader-v1` had returned `QUEUED / EVENT_READ_CONTROL_BUSY` as of this research; the new artifact makes no claim to a formal R5 owner/CLAIM, Activity checkpoint, Result or Review. Historical authorship is not a current session capability.
