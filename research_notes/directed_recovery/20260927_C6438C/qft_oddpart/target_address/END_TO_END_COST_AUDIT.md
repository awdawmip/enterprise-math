# Final end-to-end cost audit

This is administrative extraction from completed actual typed BRC evidence, with no new scientific execution. The paid pipeline pays for order discovery, target recovery, and fresh verification. The bounded results show conditional contraction savings, not a uniform end-to-end speedup.

This audit binds production `paid_aggregator.py` SHA256 `ff7cf4c32d5cd86c68a2602c4991972004762343ecff4de72e735441b1a68768`. The main raw payload SHA256 is `eb566ed690aed646988ed72bb4df1ccd9ff788bf75bea751e0100dc9b5f39b62` (43,453,949 bytes); the separate K=0 payload is `289d5d09041187a72bbff80eec0c65811cacf56dc1a9480cc8e5be2297efc96b` (4,478,985 bytes). The complete extracted ledger is `END_TO_END_COST_ACCOUNTING.json`, SHA256 `13840e51f4fbab2a5ebb789a97c7fb8b48fe991b90a6b30494b3bf31e1770566`; `extract_end_to_end_costs.py` reproduces it without importing scientific implementations.

## Call ownership and units

For each target, initial `discover_address` performs one order discovery and one address recovery, the latter including a fresh order replay. Each ordinary Gamma query and each counted Gamma query independently performs another fresh address/order replay, followed by inherited permutation verification. Index/count arithmetic and the counted route's inverse-table setup and replay are separate. The checker executes both Gamma routes after one initial address construction; initial construction is charged once in that actual checker total. A comparison choosing only one route includes that route's initial construction plus its own Gamma call.

Nested copies of the original order/address certificates are provenance, not additional executions. Explicit factory/table instances and verification receipts are charged according to the actual call graph. Two distinct instances with equal parameters are not deduplicated. The complete alias discovery used as an independent bounded reference is charged separately from either paid route.

The table below counts **typed adder-digit replays**, including setup and verification work. Native core calls, native phase-vector actions and signed-observer operations are different counters and remain separate. These digits do not cover every host operation, arbitrary-width allocation, serialization, phase admission, or all phase/observer work; they are not total runtime or a gate-count conversion.

| Actual work category | Main run | K=0 run |
|---|---:|---:|
| Program initialization: table setup, columns and permutation replay | 28,636 | 2,590 |
| Initial order discoveries | 97,470 | 3,898 |
| Fresh order replay inside initial address recovery | 97,470 | 3,898 |
| Initial address-only work | 87,420 | 4,080 |
| Fresh order replay inside Gamma address verification | 194,940 | 7,796 |
| Fresh address-only work inside Gamma verification | 174,840 | 8,160 |
| Gamma inherited permutation replays | 14,580 | 1,240 |
| Ordinary contraction index arithmetic | 2,006 | 622 |
| Counted contraction index/count arithmetic | 4,987 | 2,371 |
| Count-inverse setup | 518 | 186 |
| Count-inverse computed columns | 0 | 0 |
| Count-inverse permutation replay | 518 | 186 |
| Independent complete alias reference discovery | 36,289 | 1,727 |
| Retained fresh work in rejected tests | 11,633 | 0 |
| Unretained inherited replay charges | 0 | 0 |
| **Total counted adder-digit replays** | **751,307** | **36,754** |
| **Actual native core-call receipts, separate unit** | **901** | **716** |

The main accepted pipeline subtotal is 674,749 digits before program initialization, alias reference discovery and rejected-test work. It includes both routes as actually executed, not a single-route performance estimate.

## Representative comparisons

The standalone N97/b5 order fixture has R=96, q=3 and s=5. Small-odd-part discovery requests 18 columns versus 96 for actual consecutive first return. Its total is nevertheless **26,925 digits versus 16,567**, because it pays for 12 table instances: 12,008 setup digits, 12,008 verification digits, 2,801 column digits and 108 auxiliary digits. Fewer column requests alone do not establish a total advantage. The aggregation fixture at N97/depth2 uses schedule multiplier b=43 with R=24; it must not be described as the R=96 fixture.

For the following table, digit costs include initial order discovery, initial address recovery with its order replay, and one chosen Gamma route with its fresh verification. Common program initialization is excluded from both alternatives. Each row sums the two recorded targets.

| Fixture | Ordinary chosen-route digits | Counted chosen-route digits | Ordinary / counted / alias phase-vector actions | Ordinary / counted / alias signed observers |
|---|---:|---:|---:|---:|
| N21/a2, depth4, h0101, targets 1 and 2 | 36,396 | 38,214 | 192 / 576 / 462 | 24 / 121 / 291 |
| N65/a3, depth4, h0011, targets 1 and 3 | 109,978 | 110,607 | 48 / 54 / 144 | 12 / 6 / 24 |
| N21/a2, depth3, h000, targets 1 and 4 | 21,096 | 20,818 | 0 / 0 / 0 | 14 / 2 / 41 |
| N21/a2, depth3, h101, K=0, targets 1 and 4 | 21,096 | 23,217 | 288 / 384 / 384 | 122 / 116 / 234 |

Counted signed observers include both the parent weighted-suffix observations and all suffix observations. They are not the parent counter alone.

For N21/h0101 the counted route is worse than ordinary period aggregation in every operation count shown, while complete nonzero residual matrix entries remain equal. For N65/h0011 it halves observers relative to ordinary aggregation and reduces phase/observer work relative to alias summation, but uses more digits and phase actions than ordinary aggregation. This is a conditional tradeoff. Those particular N65 matrices have no nonzero residual entries; nonzero residual coverage comes from other fixtures. The all-zero-prefix case shows a small digit reduction. K=0 retains exact matrices with nonzero residual entries and has no prefix-aggregation acceleration; count/preparation overhead is still paid.

No per-case timing ratio or total-memory improvement follows from these distinct counters. Paid discovery and replay remain material even where contraction counts improve. The same recovered order information is available to an equally informed classical comparator; this audit makes no general factoring or simulation complexity claim.

## Superseded receipt gap and final status

The initial adapter `b6aec3c6dc4732e4be2bf19ca0bcc2d52a4e7630356c96abc7be8168b23a51fe` verified the inherited permutation before checking the target address. Three rejected address tests consequently executed an earlier replay without retaining that receipt. The old audit transparently charged 3 times 310 digits from the frozen call graph and matching retained permutation cost. That historical finding and its 752,237-digit ledger remain unchanged in `END_TO_END_COST_AUDIT_OLD_RUN.md`, `END_TO_END_COST_ACCOUNTING_OLD_RUN.json` and `extract_end_to_end_costs_old_run.py`; old science source/results are retained in `../aggregation/prior_validation_run/`.

Production now validates the address first. The replacement main and K=0 checks were actually rerun; the rejected address paths no longer execute those three inherited replays. Accordingly, the final ledger removes exactly 930 digits, without silently erasing the old evidence gap. Successful matrices and operation counts are unchanged. These are shared-context author checks and bounded actual execution, not independent admission.
