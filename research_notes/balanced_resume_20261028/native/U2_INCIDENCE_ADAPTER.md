# U2 finite-prefix incidence and source-readout adapter

Author: EM-NATIVE-A8C19E. Activity: RA-BALANCE-NATIVE-20261028-A8C19E.
Date: 2026-10-28 (Asia/Shanghai).
Status: EXECUTED_TARGETED_TOOL_EXTENSION; independent review pending. No new theorem, formal Task/Result, Driver acceptance or native action law.

## Existing interface debt addressed

The October library's `CELL-U2-PACKET-FIELD` and `U2-INCIDENCE-BRIDGE` refer to the same conditional packet-circuit interface. Their source `INTERFACE_CERTIFICATE.md` identifies I1 (the original field solver hardwires the default incidence) and I2 (returned material-port summaries merge source identities). Both remain distinct from the G1–G5 native-event, response, reaction/storage, time/boundary and occupancy obligations.

This adapter addresses I1/I2 for explicitly finite relation depth and a fixed material layout. It accepts one complete anchored incidence family for every incoming port at each labelled material, executes the unchanged positive BRC packet/leg primitives, and returns every path leaf plus source × target-material × incoming-port CWMs. It does not modify or supersede the old default solver, whose previous results remain valid at their stated scope.

## Exact dependencies and interface

- `research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/packet_router.py`, Git blob `7465f5aa16cbb8fba61ba4be80f8a6884b879c53`.
- `src/enterprise_math/brc_weighted.py`, Git blob `3f205696709e847909958a153f8fe10d3f6b70f0`. The original router checks this pin and removes only its two unused relative imports while verifying unchanged function/class ASTs.
- Prior accepted conditional interface: `research_artifacts/mcp/RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007/MCP-1a6e3bae74c6436bae9f2b466e7042ba/94bd4acc4df02dacf568/INCIDENCE_TRANSFER.md`, Git blob `39b6461383e08cef312b69546e40da32d05cab06`.
- The companion `INTERFACE_CERTIFICATE.md`, Git blob `254296463ebd3b54f028ca4ca306116d0725e19c`.

The two mathematical source documents and router were fetched at current immutable source `1a553d4d28a105230ecebd5a555dc8adbab8ee28`. The BRC implementation's actual local blob matched the above dependency pin; no changed kernel was substituted.

The new `u2_incidence_prefix.py` exposes:

    load_kernel(repo_root)
    validated_families(R, families)
    transfer_interface(R, families)
    field_prefix(R, cells, incidence_by_material,
                 depth=2, rho=1/4, max_leaves=1000000)

`cells` are distinct labelled raw signed X6 Cell charts. Each `families[p]` is a nonempty finite family of distinct triples containing p and using three different axes. A coherent global hypergraph is allowed but not assumed; arbitrary anchored families do not inherit the global-hypergraph component-degree regularity equivalence.

`transfer_interface` preserves the destination-row convention

    K[q][p] = total output at q from unit input p,

and explicitly supplies the source-row bridge `W[p][q]=K[q][p]`, hence `W=K^T`. This is checked on a genuinely nonsymmetric example so an accidental missing transpose is detectable.

`field_prefix` retains each leaf's source identity, initial signed input, current Cell and incoming port, ordered edge history, complete chosen packet tag/three-port membership, and positive CWM. It does not merge leaves before propagation. Its additional source/target/input summaries are declared observers of those retained leaves. Packet siblings are recognizable by a common tag, and the underlying unchanged `Packet` constructor retains the shared budget/leg interface.

Inputs are explicitly validated. Canonical sorting makes reordered copies of one triple count as duplicates, rather than different incidence choices. A leaf-resource cap raises an error instead of returning a silently truncated field. An absent material family cannot fall back to default forty-triple incidence.

## Correctness inherited from the existing conditional circuit

At a material Cell, `R.packets` partitions each parent CWM into its declared uniform packet alternatives and three legs. The adapter then uses `R.serial` for the fixed attenuation rho; at an empty Cell it uses the twelve inherited bulk edges of weight rho/12. It keeps distinct path leaves, and only the observer summaries use `R.total`/positive recoalescence. These are actual calls into the pinned scientific functions, not a parallel rational matrix propagator.

By induction on finite depth, each returned leaf is exactly one path of that declared grammar, including its source and packet provenance. Every parent produces exactly the grammar's legal successors with the inherited serial weights; no other source or packet is identified. Thus the retained finite leaves are correct at every completed finite depth. Each layer's total is N rho^ell, independently of row balance. The global omitted-total bound N rho^(L+1)/(1-rho) applies to total positive response only. It is not an all-depth branch-count, dominant-history, finite-memory or joint-state closure.

For the two-edge source-labelled observer the already proved formula remains

    R_a^(2)=lambda^2 [12+3 sum_{q in N_a} r_a(q)],
    r_a(q)=sum_p K_a(q,p),  lambda=rho/12.

The source material's row mass controls this formula; a different receiving material kernel contributes its anchored diagonal 1/3. The implementation checks three distinct assignments: both materials irregular, only the first irregular, and only the second irregular. This exercises material-specific incidence rather than merely accepting an unused parameter.

## Actual validation

Run from a checkout containing the exact dependencies:

    python u2_incidence_prefix.py --repo-root /path/to/enterprise-math

Optionally add `--full-trace /path/to/trace.json` to serialize every retained leaf. `u2_adapter_validation.json` stores per-case canonical trace hashes and byte lengths, exact own-return CWMs, the source row mass, dependency pins and actual call counts. Canonical case hashes refer to each complete compact JSON result before the optional combined trace wrapper, not to the combined file.

The new targeted run passed all three different-material assignments, rejected four invalid/resource-limited cases, and checked the nonsymmetric transpose bridge. Actual scientific calls were 459 `cwm_edge`, 39,797 `cwm_propagate`, and 48,891 `cwm_recoalesce`. These counts are observations of this adapter run only; the old 97/3329/25074 checks were not replayed or counted as progress.

## Reuse, scientific status and remaining work

Method resolution: `T0_BRC / t0.weighted_brc_cwm` REUSE_EXECUTED, task-specific EXTEND_EXISTING_TOOL for finite incidence injection and labelled output; T6 observer-preservation constraints REUSE_APPLIED. This is a tool candidate for the existing family, not a new family or mathematical novelty claim. It is independent source implementation work, not an independently signed formal theorem review.

The project substrate remains the full native signed X6 torsor with no native plane. Relation depth is separately typed from physical time. Triple syntax, fractional response and three packet legs are not native signed triad admission or third-action provenance. All G1–G5 remain UNKNOWN. No material motion, force law, physical clock, reaction or storage law is supplied. Gates or other joint-sensitive future operations require the retained packet/path carrier and their own semantics; the unary marginal summaries alone do not authorize them.

The next integration action is a nonauthor review of family forwarding, packet/source retention, dependency pins and the actual trace. No further deepening of the same default finite example is justified merely to increase check counts.

Researcher-ID: EM-NATIVE-A8C19E / TASK_RESEARCH
