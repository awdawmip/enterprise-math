# R5 fifth noise chamber — strict one-exchange local maximality at f=8

Date: 2026-11-17 (Asia/Shanghai). Frozen scientific input commit `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Exact original 101x256 integer observer table SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Exact new theorem

Let (C_f(H;\tau)) be the least worst-case cumulative physical query cost to identify an unknown named hypothesis from (H) by finite adaptive queries (k\in\{214,\ldots,314\}), where the integer center at (k) is (N_h(k)), normal real readings satisfy (|y-N_h(k)|\le\tau/2), and up to (f) readings are arbitrary unmarked corruptions.

Fix (f=8), the fifth-chamber left endpoint (L=25845652773852463277015040000), and (H_0=(18,24,82,34,17)). Let (H_{i,h}) replace the (i)-th member of (H_0) with any (h\in\{0,\ldots,255\}\setminus H_0), with (i=0,\ldots,4).

**For all 1,255 ordered single replacements,**
[
 5671\le C_8(H_{i,h};L)\le8326<8335=C_8(H_0;L).
]
Thus (H_0) is a **strict one-exchange local maximizer** of the exact five-state lower-certificate objective. This finite-neighborhood extremality claim is about the left endpoint and five-state restricted games; it does not assert a global optimum over all five-subsets.

| Removed named mask | Maximum over all 251 replacements |
|---|---:|
| 18 | 6455 |
| 24 | 8309 |
| 82 | 6758 |
| 34 | 8326 |
| 17 | 8326 |

The 1,255 exact roots range from 5671 to 8326, with 17 distinct cost values and **32,848,370** total memoized states across independent runs. The smallest strict margin to the original 8335 is **9 budget units**. The exact per-replacement root values, in deterministic order, are losslessly encoded in `RESULTS_COMPACT.json`, with a hash of the extended solver rows.

## Exact finite proof/checker

For every replacement, reconstruct the five integer centers for **every one** of the 101 legal queries from the original pinned table. The inclusion-maximal normal-compatible answer supports are the inclusion-maximal intersections of the centers with a closed real interval of width (L). Enumerating intervals ([c,c+L]) anchored at each observed center and dropping strict subset supports is complete. A support included in another support has no greater adversarial value: the latter leaves at least as many named states with no larger error count.

Each query is reduced to its maximal-support family; identical families induce the same transition game and only the cheapest query is needed. Let (e_i=\min(9,\#\text{ incompatible readings for hypothesis }i)); 9 is the eliminated sentinel. If at most one (e_i\le8), let (V(e)=0). Otherwise the exact Bellman equation is
[
 V(e)=\min_k\left(k+\max_{A\in S_k}V(T_A(e))\right),\qquad
 T_A(e)_i=\min(9,e_i+\mathbf1_{i\notin A}).
]
An action with a self-loop cannot terminate against repeated adversarial answers and is removed. All remaining transitions strictly increase an active mismatch counter. The provided C++17 solver uses exact unsigned four-bit counters and full state equality for memoization, with no float arithmetic or tolerance. Hash collisions do not change correctness.

The Python driver validates the table SHA-256, reconstructs the complete action quotient for all 1,255 games, executes the C++ minimax solver for (f=8), and verifies the decoded compact certificate, value histogram, and extended row digest. Actual completed local execution yielded:
`PASS_R5_F8_ALL_1255_FIVE_STATE_SINGLE_EXCHANGES max=8326 H0=8335 rows=1255`.

Reproduction requires the original frozen `EXACT_R5_ALL_101_BUDGETS.json`, provided with the R5 reproducibility archive and identified by the SHA above. Run:
```bash
g++ -O3 -DNDEBUG -std=c++17 VERIFY_EXACT_SMALL_MINIMAX.cpp -o verify_exact_small
python VERIFY_ALL_SINGLE_EXCHANGES.py
```

## Frontier and provenance

The full 256-state fifth-chamber problem still has (8335\le C_8^*(\tau)\le8343) for (L\le\tau<58182461585441404127941754880), as previously certified. The stronger local-maximality result prioritizes a genuine multi-mask interaction witness (not a one-swap change of (H_0)) or a complete 256-state upper strategy at 8335. Scalar response equivalence only concerns this declared observer; it does not collapse native X6/BRC provenance.

Prior five-state and single-addition evidence: `research_notes/portable_direct/r5_fifth_chamber_f8_six_mask_extension_sweep_20261117/RESEARCH.md` at `a08d1278c07e2d99f0620536531a69da633dbe45`. Verified historical native registration `r5-20261117-2144-turn11-author-session-start-v1`: researcher `EM-DIRECT-AEEFF0`, Activity `RA-B1A5102AD1877F18B4C40118`. No shared TASK CLAIM, independent review, or protected Activity checkpoint is asserted by this branch publication.
