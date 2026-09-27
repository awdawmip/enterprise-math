# Superseded initial end-to-end cost audit

This administrative audit reads completed evidence only. It imports no scientific implementation and performs no new scientific calculation. It applies to the initial adapter `paid_aggregator.py` SHA256 `b6aec3c6dc4732e4be2bf19ca0bcc2d52a4e7630356c96abc7be8168b23a51fe`, before the parent corrected the ordering of inherited-permutation and target-address verification. The original implementation and evidence are retained by the parent in `prior_validation_run/`; this audit is historical, not the replacement run's ledger.

The complete extracted ledger is `END_TO_END_COST_ACCOUNTING_OLD_RUN.json`, SHA256 `6a2032bbc50b8897c99999a7b93c6a1e3aa5acec6430cd0303d566538f4e7540`. Its recorded payload hashes bind both the main 14-case run and the separate K=0 boundary run. `extract_end_to_end_costs_old_run.py` records the exact administrative extraction logic.

The accounting follows explicit actual calls, not a recursive walk of every nested certificate. Each initial `discover_address` pays once for order discovery and again for the order replay inside address recovery. Each ordinary Gamma query and each counted Gamma query then pays its own fresh address/order verification and inherited permutation replay. Historical certificate copies embedded within those records are not new calls. Index/count arithmetic and the count-modulus inverse's construction and verification are separate. Phase-vector and signed-observer operations are separate units from adder-digit work.

| Main-run work category | Typed adder-digit replays |
|---|---:|
| Program initialization | 28,636 |
| Initial order discoveries | 97,470 |
| Order replay inside initial address recovery | 97,470 |
| Initial address-only work | 87,420 |
| Order replay inside Gamma address checks | 194,940 |
| Address-only work inside Gamma checks | 174,840 |
| Successful Gamma inherited permutation replays | 14,580 |
| Ordinary contraction index arithmetic | 2,006 |
| Counted contraction index/count arithmetic | 4,987 |
| Count-inverse setup / verification | 518 / 518 |
| Independent complete alias reference discovery | 36,289 |
| Retained fresh work in rejected tests | 11,633 |
| Unretained failed inherited replays, source-derived | 930 |
| **Total counted** | **752,237** |

The last 930 digits are three times 310. In the old adapter, `wrong_address`, `forged_membership` and `wrong_source` each execute the N21/b4 inherited permutation replay before failing address verification. The address failure retains its fresh replay, but that earlier inherited receipt is not attached to the exception. The charge is therefore derived explicitly from the frozen call graph and matching retained permutation's arithmetic cost, **not described as three retained failure receipts**. The parent elected to fix this concrete evidence gap and rerun affected checks; the new interface validates the address first.

The separate K=0 boundary run totals 36,754 adder digits and has no such negative-test gap. Neither total includes all host operations, arbitrary-width allocation, serialization, full native phase admission, or phase/observer execution as if those were adder digits. Source-bound native CALLS remain their own complete run measure.

Important comparisons are unchanged by this receipt-order correction:

- In the standalone N97/b5 order fixture, R=96 and q=3. Discovery uses 18 requested columns versus 96 for actual consecutive first return, but costs 26,925 adder digits versus 16,567 once table setup and replay are included. The aggregation fixture at N97/depth2 uses the different schedule multiplier b43 of order24; these are not the same order experiment.
- N21, h0101, two targets: the counted method uses 576 phase-vector actions and 121 signed-observer operations versus ordinary period aggregation's 192 and 24. Initial discovery/address plus a single chosen route costs 38,214 adder digits counted versus 36,396 ordinary (shared program setup excluded from both). Complete alias summation uses 462 phase actions and 291 observer operations. The counted route has no advantage over ordinary aggregation in these reported operation counts.
- N65, h0011, two targets: counted uses 54 phase actions and 6 observer operations; ordinary uses 48 and 12; alias summation uses 144 and 24. Counted improves some contraction counts over alias summation and cuts observers relative to ordinary aggregation, but its initial-plus-chosen-route digit total is 110,607 versus ordinary's 109,978. It is a conditional tradeoff, not a uniform end-to-end speedup.

No timing ratio or total-memory claim follows from these separate counters. The final audit must bind the replacement execution's payload and remove the three obsolete source-derived failed-replay charges rather than silently overwriting this historical audit.
