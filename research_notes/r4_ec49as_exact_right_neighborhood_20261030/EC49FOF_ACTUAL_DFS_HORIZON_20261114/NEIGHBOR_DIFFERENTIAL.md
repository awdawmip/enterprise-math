# EC49FOF — Exact native root-domain and DFS-priority perturbation observation

Companion to the real DFS horizon proof. Frozen original signed-prefix input SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. All comparisons are exact integer/native trie computations in the specified three configurations.

| K | Seven cache keys | Native deterministic demand order (zero-based label) |
| --- | --- | --- |
| 32279 | 0,4,5,11,37,39,45 | 14,16,18,20,22,23,10,12,4,6,8,9,2,3,0,1,11,5,7,15,17,19,21,13 |
| 32315 | 0,4,5,11,37,39,81 | 10,11,12,14,16,18,20,22,23,4,6,8,9,2,3,0,1,13,5,7,15,17,19,21 |
| 32318 | 0,4,5,11,37,39,84 | 10,11,12,14,16,18,20,22,23,4,6,8,9,2,3,0,1,13,5,7,15,17,19,21 |

For `32279→32315` (single key 45 replaced by 81), demand **11** changes lawful roots `{03,07}→{07}` and demand **13** changes `{03,06,07}→{06,07}`. The exact minimum single-label rooted-cover costs for each of demands **10,11,12,13** increase from 20 to 22. Consequently all **24 demand positions** differ between the native deterministic DFS orders of the two configurations. Replacing key 45 by key 84 (`32279→32318`) yields the same exact perturbations and priority order.

The `32315→32318` contrast has identical root domain for all 24 labels, identical minimum singleton cost for all 24 labels, and exactly identical sorting order, although the two configurations are distinct signed-prefix sets. Thus the source-level differences can be classified into (i) lawful root-set changes, (ii) minimum singleton score changes, (iii) native prefix cost table changes with fixed score/domain, and (iv) induced DFS order changes.

The observed **436 versus 173** DFS visit counts and **7 versus 5** actual-node maximum full-future forcing horizon follow in the original deterministic solver. The recorded perturbation data do not yet isolate a unique causal contribution for each factor; doing so requires lawful counterfactual/cache hybrid checks with preserved native typing.

**Reproduction:** `python VERIFY_NEIGHBOR_DIFF.py master_and_radius3_cases.txt NEIGHBOR_FEATURES.json`, using the published independent `VERIFY_EC49FNY_INDEPENDENT.py`. The script reconstructs all four root-cover tables per case and asserts every reported difference. Local finite author verification: `NEIGHBOR_FEATURES_EXACT_PASS ['32279-32315', '32279-32318', '32315-32318']`.

**Next:** Compare actual DFS branching under controlled root-domain, rooted-cover score and sort-order perturbations; preserve lawful original cache semantics when attributing any effect to a single factor.
