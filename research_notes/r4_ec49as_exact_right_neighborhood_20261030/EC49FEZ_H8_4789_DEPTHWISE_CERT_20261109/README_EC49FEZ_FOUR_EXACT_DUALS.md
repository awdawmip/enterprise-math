# EC49FEZ extension — four exact H8-mixed pooled-key signed-prefix duals

Date: 2026-11-09 (Asia/Shanghai). Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status: author-side exact finite mathematical evidence, pending independent Driver review. This is a same-run extension of the explicit H8/4789 94-edge disjoint-prefix proof already in this directory. All results retain original P000, nine-state automaton, native ordered signed six-axis microsteps, complete positive forward BRC keys, and the <=5 full-key constraint.

## New exact finite theorems

For the 23-word family, H2 is low quartet (1,2,4,8), H3 high pair (16,32), H8 mixed type B (1,8,16), exactly three additional late high-pair horizons (16,32), and the remaining late horizons low quartets. H9 must be a high pair. Allow different paths at one horizon to use different full keys, but at most five distinct full keys in total. Define C_native as the number of distinct nonempty **ordered signed microstep prefixes** across the 23 original words.

| Late high-bearing set (including H8 and H9) | Original type-B signature-feasible full-five-key configurations | Complete pooled-key exact lower bound |
|---|---:|---:|
| 4589 | 1,088 | **110** |
| 4689 | 2,736 | **98** |
| 4789 | 2,508 | **111** |
| 6789 | 5,632 | **105** |
| **Four solved branches** | **11,964** | **at least 98** |

The original exhaustive EC49FEU census gives the same four subsets and counts; additionally, original typed-B signature-infeasible configurations in these branches number 960, 336, 2,100 and 8,192. The established exact BRC operation/key involution gives the identical bounds for the corresponding 11,964 typed-C mirror configurations (type counts need not represent disjoint underlying untyped inventories).

**Two H8 branches remain unresolved** under the <=93 target: 5689 (5,472 feasible typed-B inventories) and 5789 (9,216). The previous complete H8 typed-B feasible total was 26,652; 11,964+5,472+9,216=26,652.

## The exact finite certificate

For each of four high sets S, define K_pool(S) as the H3 key (3,1,1) plus every positive complete BRC key admitting both high labels at the three other high-pair horizons and every key admitting label 16 at H8. The original five-key inventory is contained in this pool. Allowing every of 23 mandatory (h,label) groups to choose its path from **all** eligible pooled-key words only relaxes the original problem. Use all original signed-X6 prefixes, not unsigned counts or terminal-only cells.

Each pooled-key group g has the exhaustive set W_g of original words, with P(w) its nonempty native signed prefixes. The provided **unrounded integer certificate** has nonnegative group/prefix weights T(g,p), positive integer scale Q=1,000,000 and integer group guarantees gamma_g, satisfying:

1. For every signed prefix p, sum over g of T(g,p) <= Q.
2. For every original word w in W_g, sum over p in P(w) of T(g,p) >= gamma_g.
3. Sum_g gamma_g / Q is respectively 110,98,111,105 for S=4589,4689,4789,6789.

Thus for any one-per-group selection, Q*C_native >= sum gamma_g; the lower bounds follow exactly, even after the key-pooling relaxation. No approximate LP objective is used as proof.

The coefficient search uses SciPy/HiGHS to *find* feasible integer weights; independent `VERIFY_DUALS_EC49FEZ.py` runs with Python standard library, reenumerates the exact original words and BRC key pool, checks the original DFA, signed endpoint, all original prefix pairs, every weight capacity and every word inequality with Python integers. The four locally recorded checks all returned `EXACT_INTEGER_PASS`:

| Branch | Pooled group words audited | Group/prefix pairs | Nonzero integer weights | Exact gamma total |
|---|---:|---:|---:|---:|
| 4589 | 70,169 | 399,558 | 265,577 | 110,000,000 |
| 4689 | 68,789 | 390,716 | 267,786 | 98,000,000 |
| 4789 | 54,423 | 312,328 | 237,322 | 111,000,000 |
| 6789 | 50,551 | 291,494 | 229,861 | 105,000,000 |

Local complete unrounded coefficients are preserved in an accompanying four-certificate `EC49FEZ_FOUR_EXACT_DUALS.tar.xz` evidence attachment. SHA-256: `ea4eefc807ab4ed2d139b46b855f45bec43d199506fb84d85682167aae377bcc` (501,224 bytes). **This raw certificate archive is retained as a conversation artifact, not a GitHub file.** GitHub contains the regeneration and exact-audit programs and this complete source and result description; the signed-prefix certificate file for the independent 94-edge H8/4789 proof is also committed here.

## Reproduce

Place `VERIFY_EC49FEZ.py`, `REGENERATE_DUALS_EC49FEZ.py` and `VERIFY_DUALS_EC49FEZ.py` in one directory. With NumPy/SciPy installed, generate each full certificate:

```sh
OPENBLAS_NUM_THREADS=1 python3 REGENERATE_DUALS_EC49FEZ.py 8 4589 120
OPENBLAS_NUM_THREADS=1 python3 REGENERATE_DUALS_EC49FEZ.py 8 4689 120
OPENBLAS_NUM_THREADS=1 python3 REGENERATE_DUALS_EC49FEZ.py 8 4789 120
OPENBLAS_NUM_THREADS=1 python3 REGENERATE_DUALS_EC49FEZ.py 8 6789 120
```

These commands write the four `DUAL_H8_*.json` files in the local evidence directory (the published generator writes into the current working directory; SciPy/HiGHS is used only for coefficient search). Verify independently via `python3 VERIFY_DUALS_EC49FEZ.py /path/to/DUAL_H8_4589.json` and analogously for the other three. The original file names/ordering are deterministic given the original word model, while floating solver candidate selection may vary across implementations; the resulting exact integer checks are the decisive evidence.

## Current frontier and scope

The complete mixed H4, H5 and H6 families have earlier finite lower bounds >=101, >=98, >=98. H7's previous completed four branches and two pending ones remain unchanged. H8 has now four exact dual bounds above 93 and two pending cases 5689,5789; an initial unrestricted pooled LP on 5689 did not return within an execution bound. Next apply a tighter five-key inventory-aware sieve or a split/decomposed dual on those two H8 branches, and the two H7 pending cases. Existing 94-edge 22-word construction remains a valid mother-family upper bound; a <=93 construction remains the open target.

Actual provenance: author-side GitHub PR #1730 source; native researcher session `EM-DIRECT-97C74B`, activity `RA-26A63C8C13F51BDCD2F10771` registered in Source; no active formal CLAIM, Result or independent Driver acceptance is asserted.
