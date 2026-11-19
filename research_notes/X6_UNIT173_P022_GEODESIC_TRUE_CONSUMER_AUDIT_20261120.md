# X6 Unit173 — frozen P022 geodesic producer-to-consumer typed audit

Date: 2026-11-20. Parent: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task: RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2.

**Status: SOURCE-TYPED / FINITE EXACT CHECK EXECUTED / AUTHOR OBSERVATION / UNREVIEWED / NOT_ADMITTED.** This unit advances the required 28-LP **real production consumer** crosswalk; it is not presented as a newly invented theorem or a completed original R063 native benchmark.

## Exact source identity and caller chain

Frozen historical comparison commit: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. The exact same two Git blobs were verified on current main:
- Producer `src/enterprise_math/p022_geodesic_multiplicity.py`, blob `46373050168d2430b6cb3952aa763f3081284632`. Entry points: `a_geodesic_path_count` at line 61, `sc_geodesic_path_count` at line 86; shell accumulation `a_shell_total_geodesic_paths` line 170 and `sc_shell_total_geodesic_paths` line 205; A3/SC3 closed forms lines 220/228.
- True executable test consumer `tests/test_p022_geodesic_multiplicity.py`, blob `ef3da1a789186867c538b604da1b642bf6039591`. Recurrence comparisons lines 108–127, full endpoint-to-shell sums lines 129–138, named 3D checks lines 140–147. These are actual imports and calls, not filename-only matches.

The producer explicitly defines two **derived intrinsic graph** types: root lattice `A_p` with transfers `e_i-e_j`, and simple cubic `SC_d` with signed coordinate steps. Its path counts are **positive noncancelling integer multiplicities**. No subtraction of native six-axis N-BRC path counts, or incorrect signed native argmax, occurs in the examined implementation or tests. A historical alleged LP019 or LP011 offending caller is therefore **not established at these paths**. The observation says nothing about uninspected consumers.

## Mathematical typed bridge and discriminating sentinel

For a root-lattice displacement `v` with coordinate sum zero, write `r=sum(v_i>0?v_i:0)`. Every shortest path is a sequence of `r` transfers from negative to positive coordinates; pairing an ordered list of sources with an ordered list of destinations gives

`B_A(v)=(r!)² / [prod_{v_i>0} v_i! prod_{v_j<0} (-v_j)!].`

For a simple cubic signed displacement `z` with `r=sum |z_i|`, its shortest-path multiplicity is

`B_SC(z)=r!/prod_i |z_i|!.`

Their shell formulas sum these distinct endpoint populations. The latter with `d=6` is the exact *combinatorial signed-axis shortest-path interface* of the current X6 Cell-coordinate representation; importing `A_3` (12 primitive root moves) as if it were `SC_6` (12 signed primitive directions) would change the allowed steps and count. At shell radii `r=0,1,2,3,4,5`:

| Radius | P022 derived A3 | X6 six-signed-axis graph count |
|---|---:|---:|
| 0 | 1 | 1 |
| 1 | 12 | 12 |
| 2 | 84 | 132 |
| 3 | 420 | 1,332 |
| 4 | 1,812 | 12,372 |
| 5 | 7,332 | 106,452 |

The first discriminating witness is already `r=2`. Equal local degree 12 does not transfer graph multiplicity. The shell formulas and their distinction have been established in existing P022 and X6 work (including Unit161); **this unit's increment is source-attested producer/consumer typing and independent coverage**, not a priority claim on the established formulas.

## Actual bounded validation

An independently written Python checker enumerated every `A_p` shell for `p=1,2,3` and every `SC_d` shell for `d=1,2,3,6`, radii `0..4`. For every endpoint it recursively removed one valid primitive step to compute shortest-path counts, then summed and compared the independent sum to the frozen producer's closed-form law. Totals: **35 family/radius comparisons, 1,847 enumerated endpoints, zero discrepancies**. Normal, `python -O`, and `python -OO` returned byte-identical JSON (SHA256 `2ed94e34d2c7f8e10d1f1e0fb7f46086202b6243cdb79e8f9d8970a27553d1fe`). The independent local Python checker's SHA256 is `4a95d2c486cdf6e26e0e09608fdcb779c4612db268f0f9edfc406709b5667d8e`. The repository's original test suite and original R063 benchmark were **not** re-executed in this run. These checks certify the bounded integer comparisons only; the general formula follows by the stated combinatorial argument.

## Disposition for the mother task

1. Append this actual frozen producer→test-consumer chain as **KEEP / CORRECTLY_TYPED_P022_DERIVED_GRAPH_AND_SC_CARRIER** to the 28-LP crosswalk.
2. Do not attribute LP011 historical wrong native argmax or LP019 historical improper cancellation to this correct producer. Their precise offending `commit:path:line` remains `UNRESOLVED_PROVENANCE`.
3. Do not replay completed original R063 17/17 and 512/512 native cases or existing Units1–172.
4. Continue a different unaudited **true production consumer** from the frozen crosswalk, preferentially one that actually imports the suspected signed-native or BRC calculation. Current and historical independent Driver review/admission remain pending.

Frozen scientific-input pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical comparison pin unchanged. P000/ACTIVE HEARTBEAT_WORLD signed X6 ontology unchanged; root-lattice A3 counts are not promoted to native physical geometry. This is author evidence only; it grants no CLAIM, Native PROGRESS, Result or review.
