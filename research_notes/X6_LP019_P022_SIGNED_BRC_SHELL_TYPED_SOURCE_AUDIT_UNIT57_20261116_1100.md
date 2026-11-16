# X6 Unit57 — P022 simple-cubic shortest-path consumer and native G-shell boundary

Date: 2026-11-16 (Hong Kong morning). Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; exact publication `TP2-B4A441B23DA3159232C2`. Author Researcher `EM-X6-FB6990`; original SID `MCP-082892eb480e45dea6d4b9fcc0491034`. **AUTHOR-SOURCE-AUDIT AND INDEPENDENT EXACT RECOMPUTATION; NOT REVIEWED / NOT ADMITTED.**

## Fixed semantics and source paths

* Frozen P000 V5, native signed six-axis Cell translation and squared component norm: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json`, with relative observer distinct from native identity.
* Frozen six-axis signed path producer `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` at the same frozen input; `shortest_path_multiplicity(z)` uses `T! / prod |z_i|!`, with `T=sum|z_i|`.
* Actual current producer `src/enterprise_math/p022_geodesic_multiplicity.py` Git blob `46373050168d2430b6cb3952aa763f3081284632`: functions `sc_graph_radius`, `sc_geodesic_path_count`, `sc_shell_total_geodesic_paths`. Its scope is simple-cubic **L1 graph shells**. Actual companion tests `tests/test_p022_geodesic_multiplicity.py` blob `ef3da1a789186867c538b604da1b642bf6039591`, including `d=1..3`, `r=0..4` direct recursion tests. Neither file was modified.
* Historical frozen `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md@fd2bcff10ca6e147348b6c1236027fc0d2877df3` blob `6ec0d73a19e28ec586c59a97d24f5798c9119771`, line 33, explicitly excludes signed/amplitude cancellation from historical Boolean BRC. This provides a source-based typed distinction, not identification of a wrong caller.

## Exact consumer theorem

For a selected signed primitive-axis step graph on `Z^d` (the X6 pure-coordinate adjacency is `d=6`, while a fixed signed three-axis slice has `d=3`), for any integer displacement `z`:

`T = sum_i abs(z_i)` and `N_BRC(z) = T! / prod_i abs(z_i)! = sc_geodesic_path_count(z)`.

**Proof.** A shortest path takes precisely `abs(z_i)` unit steps of the required sign on axis `i`, because an opposite-sign step adds at least two events. Distinguishable axis-coordinate step orderings form permutations of a multiset, giving the multinomial. This is valid in both forward and reverse directions. Signed path counts are nonnegative integers; determinant Möbius signs and signed amplitudes are separate operators.

A producer may aggregate endpoints using **graph radius** `T`. P000 also declares `G(z)=sum_i z_i^2`. In general, the `G=m` shell and the `T=r` shell index different endpoint sets. Correct endpoint multiplicities do not make their shell totals interchangeable.

## Exact discriminating counterexample (fixed three-axis slice)

On `Z^3`, `G(z)=25` has exactly 30 signed endpoints: 6 axial endpoints `(±5,0,0)` and permutations, and 24 signed permutations of `(3,4,0)`. Their `N_BRC` total is `6*1+24*35=846`. The non-axial endpoints have `T=7`, the axial endpoints `T=5`.

The `T=5` shell has 102 endpoints and sum `N_BRC=1566`, agreeing with the P022 source formula `sum_{k=1}^min(d,r) C(d,k) 2^k k! S(r,k)` at `(d,r)=(3,5)`. The two endpoint sets intersect in exactly six axial endpoints. Thus applying `sc_shell_total_geodesic_paths(3,5)` to the historical/native `G=25` shell would return **1566 instead of 846**. This is a typed-consumer warning, not a found bad call.

For the native full six-axis `z=(3,0,0,-4,0,0)`, both signed-BRC and P022 per-endpoint formulas return `35`, and `G=25` while `T=7`. This exact witness is retained with named axes and signs.

## Executed verification and scope

Executed independent Python integer-only checker `research_checks/X6_LP019_P022_TYPED_SHELL_CONSUMER_CHECK_20261116_1100.py`: direct complete integer enumeration of both stated `Z^3` shells; independently recursive path-count DP on all **30+102** endpoints; recursive checks on five six-axis samples; direct Stirling recurrence; normal and `-O` both yielded the same JSON `PASS_X6_LP019_P022_TYPED_SHELL_BRIDGE`. Execution file SHA256 `e56adf52ade4b97a98f2f1a8c0e22f76c37f7f9732009e4c540bb84ee239e0b2`; JSON SHA256 `6351c18125e0990dcaa535f6b44950aa10a4dc070c3269d9678fa66e1eec2feb`. This runs the *independent formula checker*, not the remote P022 production module or frozen Source code.

This updates LP-018, LP-019, LP-020 and LP-028 named downstream consumer edge: P022 endpoint primitive-axis formula = `PRESERVE_PATH_BRC` for typed signed cubic adjacency; P022 `L1` shell total = `PRESERVE_TYPED_GRAPH_SHELL`, requiring an explicit predicate before converting to X6 `G`-shell data. No identified incorrect current invocation was modified. The exact historical LP011 wrong signed dominant-axis call and LP019 positive-count signed cancellation call remain `UNRESOLVED_PROVENANCE` after the currently bounded scans; the 28-LP global consumer graph and independent Driver `REQUEST_REVISION` remain open.

Next: inspect non-exhausted current callers of `sc_shell_total_geodesic_paths` and historical typed path imports for actual `G`-shell misuse, then patch only a reproducibly wrong consumer. Preserve original Researcher SID, claim/run and frozen input pins; no new dispatch or maintenance lane write.
