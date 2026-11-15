# EC49FPJ — Exact optimal uniform expected native BRC sensing under depth-three constraint

Date: 2026-11-15. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This follows EC49FPH (optimal four **fixed** scalar queries) and EC49FPI (optimal **adaptive worst-case** depth three).

## Scope

Keep the frozen original BRC scientific commit `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, master SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, exact native rooted-cost CSV SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. Consider the complete original legal-root domain of configuration 16943: 310 native configurations, 141 distinct rooted cost states, 139 distinct terminal states, 144 legal complete terminal cost observations and 84 named-root/subset cost observations. There are 228 primitive scalar queries in the exact integer menu.

Equiprobability is on the **141 distinct rooted states**, not on 310 source configurations. A deterministic adaptive decision tree is allowed to choose future scalar queries conditional on already-observed exact integers, and must distinguish all 141 states. Each scalar query has cost one, and worst-case depth is constrained to be **at most 3**.

## New exact theorem

The minimum expected number of scalar queries among all such depth-at-most-three adaptive trees is

[
\boxed{\mathbb E_{\mathrm{uniform}}N_{\mathrm{opt};d\le3}=\frac{296}{141}\approx 2.09929.}
]

Exactly **two** first-query selections attain the minimum: terminal queries `T(32)` and `T(34)` (original zero-based legal-allocation ordering). A constructive optimal tree starting at `T(32)` has 30 first-response integer fibers and the following leaf-depth distribution across all 141 rooted states:

| Query count | Rooted states |
|---|---:|
| 1 | 6 |
| 2 | 115 |
| 3 | 20 |
| **Total** | **141** |

The exact total cost is `6*1 + 115*2 + 20*3 = 296`. Relative to the earlier valid depth-three tree beginning with `T(0)` (322 total queries over all 141 states), the expected cost falls by `26/141` queries per equally likely rooted state while retaining worst-case depth three.

### Exhaustive optimality proof and algorithm

For a subset (response fiber) `S` of the 141 states and each possible exact scalar query `Q`, write `S_{Q,v} = {s in S: Q(s)=v}`. Define the minimal total number of further queries across all states of `S` with at most `h` remaining query levels, `C_h(S)`:

- `C_h(S)=0` for singleton (or empty) `S`;
- `C_0(S)=+infinity` for `|S|>1`;
- `C_h(S)=|S| + min_Q sum_v C_{h-1}(S_{Q,v})` for `h>0`, minimizing over the exact 228 allowed queries that split `S` (an unsplitting query cannot improve a finite-depth solution).

The `|S|` term counts the one query actually performed for every state reaching that node, so minimizing total counts is equivalent to minimizing uniform expected cost. The recurrence is exact by induction over remaining depth; each branch is independent after conditioning on its observed integer value.

For each of all **228** candidate initial queries, the verifier determines its response partition and evaluates the exact minimum `141 + sum_v C_2(S_{Q,v})`. Exactly **63** candidate first queries admit any complete depth-three decision tree. The minimum across all 63 is **296**, achieved only by terminal indexes 32 and 34. The winning `T(32)` decision tree is then reconstructed using attaining `C_2` queries; its exact integer responses and leaves are checked for all 141 original rooted states. The machine-readable summary is in `EC49FPJ_UNIFORM_EXPECTED_SUMMARY_CERTIFICATE.json`, and the independently executable verifier plus complete 141-leaf decision tree are in the verified evidence archive for this PR.

Local exact run: `VERIFY_EC49FPJ.py` executed over the unmodified pinned original master and rooted-cost CSV and printed `EC49FPJ_UNIFORM_DEPTH3_EXPECTATION_EXACT_PASS`. The parent source/independent byte-Trie verification and earlier two exact sensing verifiers also passed. The proof uses integer response equality and bit-set partitions, without floating-point optimization.

**Remaining question:** optimize *unrestricted* uniform expected query count when worst-case depth may exceed three. The exact (296/141) theorem applies to the declared depth-≤3 regime. Also explore heterogeneous terminal-vs-root measurement costs and alternative state priors, retaining root provenance and demand-subset residuals.
