# X6 Unit195 — Arbitrary-even-length signed native X6 / lazy A5 / nonlazy A5 exact binomial inversion

**Author scope:** RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2; parent PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Research lane `chatgpt-research-onhour-enterprise-math-20260923`; excluded maintenance `chatgpt-hourly-enterprise-math-20260921`.
**Science pin:** `59538f585d037d09ef687b28715c4bc1a3f9fe03`; **frozen historical comparator:** `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.
**Status:** AUTHOR_PROVED / EXACT_PINNED_PYTHON_EXECUTED / UNREVIEWED / NOT_ADMITTED. Native semantic PROGRESS remains separate and unsubmitted. This is a new non-shortest-length extension of Unit194, not an R063 rerun, new Task, or Result.

## Objects and actual original producers

Six signed X6 primitive coordinate events are `+e_i,-e_i` (`i=1,...,6`), interpreted as P000 raw Cell-displacement steps; native time order is retained. The frozen executable `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` has blob SHA-1 `300a96e3dc24bf6fff73743037a0347a8bc83176`; `endpoint_multiplicity(length,z)` counts all signed primitive words reaching `z`, including backtracks. In contrast frozen `src/enterprise_math/p022_geodesic_multiplicity.py` blob `46373050168d2430b6cb3952aa763f3081284632` supplies `a_geodesic_path_count` for *shortest* A5 root-transfer words. The A5 direction `e_i-e_j` (`i≠j`) is a **composite two-event X6 readout**, not a native primitive or independent Enterprise plane. We define its nonshortest walk kernel below; do not attribute that new function to the frozen P022 module.

For any `z∈Z^6` with `sum(z)=0` and `n≥0`, write:
- `E_{2n}(z)`: exact length-`2n` signed X6 native word multiplicity, all words, not merely geodesics.
- `L_n(z)`: length-`n` **lazy paired-root words**, each alphabet letter a *labeled pair* `(i,j)∈{1,...,6}²` with displacement `e_i-e_j`; `i=j` is one of six labeled zero pairs (not an empty event).
- `A_n(z)`: length-`n` **nonlazy A5 root words**, alphabet `(i,j)` with `i≠j`, displacement `e_i-e_j`. `A_0(0)=L_0(0)=1`.

## Exact theorem: shuffle fiber for every even length

```text
E_{2n}(z) = binom(2n,n) L_n(z).
```

**Proof.** Every signed native word ending at balanced `z` has exactly `n` positive and `n` negative events, since each signed step changes total coordinate sum by ±1. Extract the ordered positive-axis label list `i_1,...,i_n`, the ordered negative list `j_1,...,j_n`, and the binary sign-slot pattern of length `2n`. Pair the k-th labels into a length-`n` lazy A5 word `(i_k,j_k)`. Its net displacement is `z`. Conversely, the paired sequence and a choice of `n` positive slots reconstruct every original ordered native step exactly. Each lazy paired word therefore has precisely `binom(2n,n)` preimages, even when labels repeat or `i_k=j_k`. No sign cancellations are discarded: a zero pair is two real native events in the ordered lift. □

At `n=r=sum_i max(z_i,0)`, all words are shortest; no `i=j` can occur, so `L_r=A_r`. This reduces exactly to Unit194's `E_{2r}=binom(2r,r)*A_r`.

## Exact theorem: nonlazy primitive-root walk extraction

The algebraic pair alphabet obeys
```text
P(x) = (Σ_i x_i)(Σ_j x_j^{-1}) = Q(x) + 6,
Q(x) = Σ_{i≠j} x_i x_j^{-1}.
```
Here coefficients of `P(x)^n` at Laurent monomial `x^z` are `L_n(z)`; those of `Q(x)^n` are `A_n(z)`. The scalar six counts the six **labeled** zero-pair possibilities `i=j`, and is not a deletion of real native events. Binomial expansion and inversion give, for every balanced integer `z` and `n≥0`:
```text
L_n(z) = Σ_{k=0}^n binom(n,k) 6^(n-k) A_k(z)
A_n(z) = Σ_{k=0}^n binom(n,k) (-6)^(n-k) L_k(z)
       = Σ_{k=0}^n binom(n,k) (-6)^(n-k)
             * E_{2k}(z)/binom(2k,k).
```
The divisions are exact integers by the shuffle-fiber bijection. This is a **typed, provenance-preserving extraction of true A5 root words from native X6 even-length endpoint totals**, not a generic subtraction of unrelated BRC populations. For an individual native word the lost data are the sign-slot interleaving and all paired labels, including which zero-pairs were present. Temporal future predicates cannot in general be evaluated from endpoint totals alone.

An alternative direct finite formula uses `a_i=max(z_i,0)`, `b_i=max(-z_i,0)`, `r=Σa_i`, `q=n-r≥0`:
```text
L_n(z) = (n!)² Σ_{t_i≥0, Σ t_i=q}
                     1 / Π_i (a_i+t_i)!(b_i+t_i)! .
```
If `n<r`, both `L_n(z)` and `E_{2n}(z)` are zero. These formulas agree exactly with the frozen signed_brc `endpoint_multiplicity(2n,z)` for balanced `z`.

## Concrete witnesses, including nonshortest

| z | paired n | frozen native E₂ₙ | labeled lazy Lₙ | nonlazy Aₙ |
|---|---:|---:|---:|---:|
| (0,0,0,0,0,0) | 2 | 396 | 66 | 30 |
| (1,-1,0,0,0,0) | 2 | 120 | 20 | 8 |
| (2,-2,0,0,0,0) | 3 | 840 | 42 | 24 |

For origin and `n=2`, `L_2(0)=30+6²=66`; all 396 native four-event returns decompose into 30 nonlazy A5 two-step returns and 36 labeled two-zero-pair words, each lifted by six sign shuffles. This identifies the exact origin-loop residual that a shortest-only A5 comparison misses.

## Actual executable certificate and scope

An exact byte copy of frozen `signed_brc.py` was obtained from the connected GitHub file fetch and matched its Git blob SHA-1 `300a96e3dc24bf6fff73743037a0347a8bc83176` before direct Python `importlib` execution. The research checker separately builds two endpoint DPs from the 36 labeled lazy A5 directions and 30 nonlazy A5 directions, and directly calls the frozen native `endpoint_multiplicity`.

Exhaustively across paired lengths `n=0..5`, it compared **17,088 balanced endpoint/length pairs** (including **5,835 nonshortest** cases). Both universal equalities above hold with **zero mismatches**, and native total mass equals `binom(2n,n) 36^n`; nonlazy mass `30^n`. At `n=5`: 11,253 endpoint states, 60,466,176 lazy pair words, 24,300,000 nonlazy A5 words, 15,237,476,352 balanced native signed-X6 words. Normal/-O/-OO all gave identical JSON results; checks use explicit conditions and exceptions, not optimized-away `assert`.

Reproduce from the immutable repository with:
```bash
git show fd2bcff10ca6e147348b6c1236027fc0d2877df3:experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py > signed_brc.py
python X6_UNIT195_PINNED_SIGNED_A5_LAZY_BINOMIAL_BRIDGE_CHECK_20261120.py
```
Place both files in the same directory. The checker itself verifies the original frozen Git blob. Its output is the accompanying saved JSON certificate. This is an exact finite crosscheck in addition to the all-`n` combinatorial proof; no original R063 native benchmark was rerun. Frozen P022 A5 nonshortest production function is not claimed to exist.

## Task result and strict provenance

This establishes the precise even-length, nonshortest population bridge needed when LP019 compares positive-root and signed native BRC counts. It also prevents treating the labeled zero root pairs or sign interleavings as dispensable during future path-sensitive operations. The historical alleged LP011 wrong native argmax and LP019 invalid subtraction still lack a verified **original offending** `commit:path:line`; do not replace that missing forensic evidence with this typed theorem.

This new standalone author unit remains `UNREVIEWED / NOT_ADMITTED`. No independent Driver review, Native Result or foundation promotion occurs. Retain the existing Native-author frontier (last confirmed Unit174), pending semantic association of Units175–195, historical Units149–152 association, unchanged R063 successful original benchmark, and Research/maintenance identities strictly separate. Next direct scientific action: inspect real frozen source consumers of an *all-walk* A5 or signed-X6 endpoint kernel and trace any LP011/LP019 allegation to exact offending `commit:path:line` if present; preserve ordinary reference-level and typed absence conclusions when absent.
