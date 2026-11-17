# X6 Unit106 — Johnson/BRC snapshot-safe counting is not one-step safe

**2026-11-18 · Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION` · `TP2-B4A441B23DA3159232C2`. **Status:** `AUTHOR-PROVED / EXACT-FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED`.

**Immutable mathematics:** X6 P000 V5 `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical Johnson `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Neither frozen input was modified. Signed primitive step type is a named axis `i in {0,...,5}` and direction `epsilon in {+1,-1}`.

## The operation-aware question

Unit105 established that the observation `K(z)=(rho_J(z),q_orbit(z),L1(z),L_E²(z))` does not always determine `B_min(z)`. It also gave the count-level sufficient correction `F(z)=prod_i |z_i|!`, since `B_min(z)=L1(z)!/F(z)`.

For a **current-snapshot query**, the enlarged packet `P(z)=(K(z),F(z))` does determine native shortest-path multiplicity. Does `P(z)` also determine the shortest-path multiplicity *after a named signed primitive step*, without reading the hidden native Cell coordinates?

**Theorem (exact obstruction).** There is no deterministic function `U_{i,eps}` on the enlarged observation packet, even when it is only asked to return the scalar native shortest-path multiplicity `B_min(z+eps e_i)` for every signed `z in Z^6`. This failure already occurs in the cube `{-1,0,1}^6`.

**Concrete proof.** Let

`a=(-1,-1,-1,-1,-1,+1)`, `b=(-1,-1,-1,-1,+1,-1)`.

The two named signed states share precisely

`rho_J=(0,0,0,2)`, `q_orbit=(-1,-1,3)`, `L1=6`, `L_E²=6`, `F=1`.

Before updating, both have six distinct signed primitive-axis occurrences, so `B_min(a)=B_min(b)=6!=720`. Apply the **same** named primitive operation `T_4^-(z)=z-e_4` (axis index 4, zero-based):

- `T_4^-(a)=(-1,-1,-1,-1,-2,+1)`: length 7 with one doubled occurrence, `B_min=7!/2!=2520`.
- `T_4^-(b)=(-1,-1,-1,-1,0,-1)`: length 5 with five distinct occurrences, `B_min=5!=120`.

Equal input packets and identical allowed operations require different next BRC outputs. This is an explicit global contradiction to deterministic one-step descent.

The obstruction is structural: `F` restores the *current* scalar count but retains neither the signed value of the named coordinate being updated nor enough native axis information to calculate the next count. A compliant downstream transducer must retain a sufficient signed named-axis state (or an exactly proven operation-preserving codec), rather than only the snapshot count and carrier residues. For full path-formal BRC, the ordered word provenance remains a separate requirement.

## Executed exact certificate

Independently enumerate all `3^6=729` signed integer states of `{-1,0,1}^6`, group by the full `P(z)`, verify that each packet has one current `B_min`, then test each of the **12 named signed updates** on each packet. Exact integer results:

| Item | Result |
|---|---:|
| Native starting states | 729 |
| Distinct enlarged packets | 94 |
| Packets with identical current BRC within each fiber | 94 |
| Packet × named signed operation tests | 1,128 |
| Operation tests with multiple possible next BRC counts | 1,032 |
| Packets possessing at least one ambiguous update | 93 |

This complete bounded census complements the global explicit witness. All checks executed with CPython normal, `-O`, and `-OO`; resulting machine JSON was byte identical, SHA256 `8b1a64f2d9dce573dba437d55890c0c37dec3d7097b996feb9f6b0bfd975a033`.

- Actual checker: `research_checks/X6_UNIT106_JOHNSON_BRC_ONE_STEP_DESCENT_CHECK_20261118.py`, commit `9f9ae2ce87b45237104ab6480a744ae96a5aae1d`, Git blob `5fce0547f0c7c1c5009638905ac084e41fd977e0`, file SHA256 `6b37211de80f7bdc6cfafe1f13f21c17de8f36a1f65317cb8fc5672e128cdc2d`.
- Certificate: `research_checks/X6_UNIT106_JOHNSON_BRC_ONE_STEP_DESCENT_RESULTS_20261118.json`, commit `6a5095ba8a5c63fb44eabf951be8cfdf64a0244d`, Git blob `11e3746bb0198579c628e434b0c0b9a362af6995`.

## Task-facing source adjudication

Frozen source `research_checks/P000_SIX_AXIS_JOHNSON_TROPICAL_ARITHMETIC_INTEGRATION_CHECK_20260830.py:82–87` computes a finite carrier observer, while the frozen native `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` supplies the positive integer path count. This unit proves the exact extra information requirement when a **downstream consumer** attempts to update a path count through the Johnson quotient. There is no claim that the source's Johnson checker itself performs that invalid update.

The persistent 28-LP crosswalk should now classify Johnson/FCC consumers along three separate demands: fixed carrier classification, fixed-time native N-BRC count, and stepwise native/path BRC propagation. Unit105 falsifies full fixed-time factorization through `K`; Unit106 falsifies one-step factorization through even `(K,F)`. Only an actual executable downstream misuse with source:line justifies a code fix. The LP011 and LP019 historical wrong-caller allegations remain `UNRESOLVED_PROVENANCE`; the independent Driver `REQUEST_REVISION` remains to be adjudicated.

**Original research identity:** `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-3e221a50dc8818f914e228f6`, RUN `RUN-95866d78d35721116c362956`. Original R063/Helly native benchmarks were not rerun; this unit has its own finite checker. The open Unit104 Native semantic PROGRESS is the original `onhour-20261118-0402-x6-own-unit104-native-progress-v1` and must be reconciled by its original ID before a later same-run native write.

**Next concrete task:** trace existing `commit:file:line` downstream interfaces that retain `rho_J`, `q_orbit`, `F`, or full signed Cell input, and label actual operation/future-observer requirements. Keep the original frozen benchmark and earlier author results as already completed.
