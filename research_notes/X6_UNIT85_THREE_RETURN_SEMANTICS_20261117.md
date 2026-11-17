# X6 Unit85 — first native-versus-relative signed BRC return split at length six

Date: 2026-11-17. Parent objective: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; immutable publication `TP2-B4A441B23DA3159232C2`.

**Scientific classification:** AUTHOR-EXACT / ORIGINAL-X6-SOURCE-TYPED / INDEPENDENT-EXACT-INTEGER-EXECUTED / UNREVIEWED / NOT_ADMITTED. This author-only GitHub evidence is **not** an original-owner-authenticated Source PROGRESS, Research Activity checkpoint, Result, Driver review or original R063/Helly native benchmark. No historical LP011/LP019 wrong caller is asserted.

## 1. Three distinct return predicates in the frozen signed native X6

Work in the P000 V5 signed six-axis displacement chart `Z^6`, with twelve distinct primitive labels `+e_i,-e_i`, one selected Cell anchor `0`, and the **derived** min-zero observer `rho(z)=z-min(z)*1`. Keep unit-word order and every nonnegative BRC path count. Let `A_L(z)` be the number of signed primitive words of exactly `L` steps from the anchor to signed raw displacement `z`.

Three typed counters must not be interchanged:

- `N_cell(L) = A_L(0)`: genuine signed native Cell return at the chosen anchor.
- `N_rel_signed(L) = sum_{h in Z} A_L(h*1)`: all signed native paths whose endpoint has **relative min-zero return** `rho(z)=0`. This is the all-horizon quotient kernel of Unit84 evaluated on the observation `0`, not a native Cell identity.
- `N_rel_positive(L) = 0` unless `6|L`; if `L=6m` it is `(6m)!/(m!)^6`: relative return when the path alphabet is restricted to the **six positive** labels, as in the current derived V7 coordinate completion.

**Exact all-horizon coefficient formula:** For every `L>=0` and every `h in Z`,
```text
A_L(h*1)
 = L! * sum_{a_i,b_i>=0, a_i-b_i=h (all i), sum_i(a_i+b_i)=L}
               1 / prod_i(a_i! b_i!).
```
The sum is finite and a nonnegative integer because it counts signed labeled words. This is a source-typed combinatorial identity, not an additional world axiom or signed-amplitude cancellation.

**Sharp first-separation theorem.** For all `0<=L<6`, `N_rel_signed(L)=N_cell(L)`: if `rho(z)=0` then `z=h*1`; any nonzero `h` needs at least `6|h|` primitive signed steps. At `L=6`, exactly `h=0,+1,-1` are possible. Both `h=+1` and `h=-1` have exactly `6!=720` ordered shortest words. Thus
```text
N_cell(6)         = 19,920
N_rel_signed(6)   = 19,920 + 720 + 720 = 21,360
N_rel_positive(6) = 720.
```
Consequently, signed native return and signed relative return first differ at **exactly six steps**; positive-only relative return and signed-relative return already differ at **two steps** (`0` versus `12`). Same relative endpoint and time length do not identify which of these three **typed transition languages/observers** is intended. This is precisely a structural-residual/provenance distinction.

The native six-step zero count is independently checkable by the partition of three opposite-direction pairs: all three on one axis `6*20=120`; two on one axis and one on a second `6*5*180=5,400`; all three on distinct axes `C(6,3)*6!=14,400`. Sum `19,920`. The entire relative fiber gains the two additional diagonal endpoints.

## 2. Independent exact integer execution and source-specific consumers

An independent Python integer dynamic program enumerated all native signed endpoints for `L=0..12`, compared the diagonal-endpoint mass against a **separately computed six-axis multinomial convolution**, checked total word mass `12^L` at every horizon, and verified the stated closed positive-sector return formula. Real execution under default Python, `-O` and `-OO` yielded byte-identical JSON SHA256 `b3cdb86fd12c576e94d0a95aa361709ec04394dcd6f425064cd5767605ea94e0`. There were **39 checked diagonal-depth fibers**, **553,995 cumulative reachable-state entries** across all horizons and **zero failures**. The executable code and all exact integer outputs are saved separately in `research_checks/X6_UNIT85_THREE_RETURN_SEMANTICS_CHECK_20261117.py` and `research_checks/X6_UNIT85_THREE_RETURN_SEMANTICS_RESULTS_20261117.json`. Their content-verified Git blob IDs are respectively `0398b8aa14821853c7a1e8060ccc1c09f864bdf9` and `e470ca44e8d1c5b5d830f07570c06437e3f0df88`.

| L | Signed native Cell zero | Signed min-zero relative zero | Positive min-zero relative zero |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 2 | 12 | 12 | 0 |
| 4 | 396 | 396 | 0 |
| 6 | 19,920 | 21,360 | 720 |
| 8 | 1,281,420 | 1,523,340 | 0 |
| 10 | 96,807,312 | 127,652,112 | 0 |
| 12 | 8,175,770,064 | 11,823,167,664 | 7,484,400 |

**Actual executable consumer boundary, separately source-read (not guessed):** Current `experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py`, blob `9738543aace13f8a72af577e9ad8964c5fd40de8`, at lines 197–242 explicitly labels `brc_endpoint_multiplicity` and `positive_return_count` as **six-positive-word min-zero relative** counts. Its real current `check_x6_coordinate.py`, blob `d562df4cedf3aa54fd3ca5db5ee0d17ff873a752`, lines 186–205 independently names both positive relative return `720` and signed **native Cell** six-step return `19920`. The third quantity, signed min-zero relative return `21360`, is a distinct observable, **not** an error in either code. The present code correctly types its two results; **no patch was warranted**. This source/operation table closes one specific executable LP003/LP005/LP019/LP022/LP023 return-observer edge, not every caller or any admission requirement.

Further focused historical-source inspection used exact archived commit `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, including nine old definition bodies (e.g. `definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md` blob `82c8877888f8da43a85eb8148b0d0d47a9e59d42`, lines 60–62 explicitly requiring typed bridge/fiber semantics; `ENTERPRISE_VECTOR_NORM_ENDPOINT_REVERSE_GEODESIC_SEGMENT_20260817.md` blob `f7d24f2b69d02fcd50e11cc02d0bb9e65a8b1d0f`, lines 21–28 separating path multiplicity and scalar length). The bounded evidence does not identify a genuine **historical LP011 native singleton argmax** or **LP019 illicit cancellation of natural positive BRC mass**. Retain `UNRESOLVED_PROVENANCE`, rather than mislabel correctly typed current code.

## 3. Task frontier and handoff

- Frozen signed P000 scientific input: `59538f585d037d09ef687b28715c4bc1a3f9fe03`; old reference corpus: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`; original native signed BRC blob: `300a96e3dc24bf6fff73743037a0347a8bc83176`. Current behavioral rules and Source ownership were independently read; these do not repin the science.
- Reuse prior author-verified Unit64–84 proofs, frozen original R063/Helly native benchmarks, Unit82 historical bounded audit, Unit84 all-horizon strong lumpability and existing 28-LP crosswalk. **Do not rerun** already completed work.
- Current historical Research SID `MCP-082892eb480e45dea6d4b9fcc0491034`, original CLAIM `MCP-579c8e23625448582b421831`, RUN `RUN-fb25028676f9692ab1bacaee`, Activity `RA-5E3FE1E761E4963EC461A892` (last verified 106) are **provenance only, not a current writer capability**. Original GitHub Chat read receipts [#6994](https://github.com/awdawmip/kimi-query-bridge/issues/6994) and [#6995](https://github.com/awdawmip/kimi-query-bridge/issues/6995) are already terminal `SUCCEEDED`, and #6995 projects `execution_authorized=false` with `PREPARE_TYPED_CONTINUATION_WITH_EXACT_PREDECESSOR_AND_FRONTIER`. The D25 Sites Researcher profile is another subject; never use it for X6.
- Remains: exact LP011 and LP019 historical bad-caller path:line or justified independent Driver `REQUEST_REVISION`; remaining real 28-LP downstream consumer graph; original-owner-authenticated native semantic/Activity association of pending author units; separate formal independent review/admission. No unverified claim of completed native execution or original-run revival.
- **Next discriminating action:** trace an actual remaining consumer that passes the relative return histogram to a *native Cell return* or a signed path accumulator, preserving the exact function signature/argument/observer and source SHA; patch only a demonstrated wrong caller. Separately provide these bounded negative provenance findings for independent Driver resolution. If no source-supported wrong caller is found, classify the 28-LP attribution for authorized revision instead of adding speculative auxiliary theory.

**Disposition:** Scoping-limited exact author research; `UNREVIEWED / NOT_ADMITTED`. Formal Result, native PROGRESS, active X6 CLAIM, Driver revision and protected worldview are unchanged.
