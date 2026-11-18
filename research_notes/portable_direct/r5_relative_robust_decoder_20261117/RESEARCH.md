# R5 — Sharp relative-noise radius for the three-count eight-bit decoder

Date: 2026-11-17 (Asia/Shanghai). Scientific pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. The object is the *derived 954-event indexed-center, radius-two integer observer*; this work postprocesses its verified exact optimal-path counts, without claiming a native X6/BRC dynamical transfer.

## Question and observation model

Previous R5 results establish that every triple `(k1,k2,k3)` with `214<=k1<=219`, `223<=k2<=291`, `294<=k3<=313` uniquely decodes all 256 effective eight-bit closure masks from exact scalar counts `N_b(k1), N_b(k2), N_b(k3)`. There are `6*69*20=8,280` such triples. We now ask which triple maximizes guaranteed mask identifiability when each positive scalar observation may have an independently chosen *real* relative error of magnitude at most `epsilon`.

For any two positive integers `u,v`, their admissible intervals `[u(1-epsilon),u(1+epsilon)]` and `[v(1-epsilon),v(1+epsilon)]` are disjoint exactly when

`epsilon < d(u,v) := abs(u-v)/(u+v)`.

Thus a fixed triple has the **sharp** identification threshold

`rho(k1,k2,k3) = min_{b != b'} max_{j=1,2,3} d(N_b(kj),N_b'(kj))`.

Every `0<=epsilon<rho` guarantees a unique mask from all noisy data, while every `epsilon>=rho` admits an indistinguishable pair in the declared independent-interval model (at equality the intervals touch). These are worst-case real relative errors in the *readouts*, not coefficient-computation error bounds or an error analysis of an approximate DP.

## Exact product reduction and proof

The frozen exact cohort support implies the first count depends only on bits `(0,1,2,3,7)` (effective cuts `3,8,9,10,27`); the second only on `(6,7)` (cuts `25,27`); the third only on `(4,5)` (cuts `15,17`). Partition the complete mask as `b=(s,t)` with `s` containing bits `(0,1,2,3,6,7)` (64 values) and `t` containing `(4,5)` (4 values). Then the observation vector is exactly

`F_{k1,k2,k3}(s,t) = (f_{k1}(s), g_{k2}(s), h_{k3}(t))`.

Let `P(k1,k2)` be the minimum of the maximum of the first two coordinate gaps over distinct `s,s'`, and `T(k3)` the minimum third-coordinate gap over distinct `t,t'`. Then

`rho(k1,k2,k3) = min(P(k1,k2), T(k3))`.

Proof: A pair of different full masks either differs in its `s` component, giving a maximum gap at least `P`, or in `t`, giving a maximum gap at least `T`. Conversely, choose the pair attaining `P` with `t=t'`, and the pair attaining `T` with `s=s'`: their other observation coordinates coincide exactly. Both minima are attained by finite state pairs, establishing equality. The reduction uses *all six first/second union bits*, including shared cut 27, so no source interaction is discarded.

For each of 414 possible first/middle budget pairs we check all `C(64,2)=2,016` unordered pairs, and for each of 20 final budgets all `C(4,2)=6` pairs. This is `834,624+120=834,744` exact rational pairwise evaluations, followed by 8,280 exact minima, with no floating-point comparisons in the decision logic. Every candidate triple has positive radius. Reconstructing the 25,856 count entries from the source cohort coefficient dictionary is also checked against the separate saved complete-count file. As a direct check of the product theorem, five representative triples are independently checked over all `C(256,2)=32,640` full-state pairs each.

## Exact optimization result

The **maximum possible robust radius across all 8,280 fixed decoding triples** is

`rho_* = 535905744549271 / 298161762794076854 ≈ 0.0017973657639`.

Exactly **212 triples** attain `rho_*`, all choosing `k3=302`. One optimal triple with the smallest possible budget sum among these is `(214,230,302)`: budget sum **746**, worst-case raw output width **411 bits**. Among the 212 robust-optimal triples the smallest worst-case raw output width is **384 bits**, attained by `(214,285,302)` (budget sum **801**). The complete list and each one's budget/bit totals are included in the exact JSON evidence.

The upper-bound witness is the pair of masks `16` and `32`, which differ only by cuts 15 versus 17. At final budget `302` their relative separation is precisely `rho_*`, while the first and middle counts coincide. Any robust decoder using the stated budget windows is therefore limited by the best possible final-window separation; the finite search proves that 212 triples reach that bound. The smallest *uniform dyadic* relative-error level below `rho_*` is `2^-10`; `2^-9` is not universally safe for any three-budget choice in this family.

Comparison with the earlier budget/bit Pareto triples:

| Budget triple | Worst-case output bits | Budget sum | Sharp relative-noise radius | Smallest safe `2^-n` |
|---|---:|---:|---:|---:|
| `(214,223,294)` | 319 | 731 | `4022840/4361603107999` | `n=21` |
| `(214,290,294)` | 317 | 798 | `67969704141326/1017143028145251983` | `n=14` |
| `(214,291,294)` | 305 | 799 | `31740930/2614473317491` | `n=17` |
| `(214,230,302)` | 411 | 746 | `535905744549271/298161762794076854` | `n=10` |
| `(214,285,302)` | 384 | 801 | `535905744549271/298161762794076854` | `n=10` |

Thus minimizing the raw count width or total budget does not also maximize robust identification margin in this finite family. Precision here is an observation-accuracy requirement; 411/384/305 bit figures are exact integer output widths.

## Executed verification and provenance

The tested standard-library verifier is `VERIFY_R5_ROBUST_TRIPLE_DECODER.py`. Exact prerequisite files:

* Frozen 101-budget cohort stdout `compact_stdout.json`, SHA-256 `a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`, generated by the earlier saved `r5_all_budget_cohort_hierarchy_20261116/VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py`.
* Previously saved full 101-budget, 256-mask exact count output, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`, used here as an independent full-table cross-check. The compact file can also be regenerated by the verifier in a complete project checkout; `--exact` is an optional extra cross-check.

Reproduction from a full checkout with the two saved outputs supplied:

`python research_notes/portable_direct/r5_relative_robust_decoder_20261117/VERIFY_R5_ROBUST_TRIPLE_DECODER.py --compact /path/to/compact_stdout.json --exact /path/to/EXACT_R5_ALL_101_BUDGETS.json > RESULTS_EXACT.json`

Actual local execution returned `PASS_R5_EXACT_ROBUST_TRIPLE_DECODER`; its complete 212-optimum list is in `RESULTS_EXACT.json`. The proof uses exact integers/Fraction comparisons and finite exhaustive coverage. Structural explanation for why 302 maximizes the final-window gap, extension to adaptive or additional observations, and an independent mathematical review remain open. The `max-new/min-old` center-set recourse question is also still open because count-only data do not retain all center-set intersections.

Formal Task/CLAIM/Result/Review authority and Activity intake are unaffected by this independent research preservation.
