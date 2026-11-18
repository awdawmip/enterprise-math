# X6 Unit114 — exact LP028 fixed-positive sector residue input-type gate, with original-source optimization regression

**Date:** 2026-11-18. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`; parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. **Status:** `AUTHOR-SOURCE-EXECUTED / EXACT-INTEGER-VALIDATED / UNREVIEWED / NOT_ADMITTED`.

## Exact source-level finding

At immutable frozen historical `fd2bcff10ca6e147348b6c1236027fc0d2877df3` and observed canonical `main`, the unchanged original executable `experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py` has the identical Git blob SHA-1 `643b2bac659a445891dcb5588b647972977104e0`. Actual lines 77–82, 85–88 and 91–98 show `sector_ball(R)`, `residue(point,m)`, `first_collision(points,m)`. The generator `sector_ball` returns only `(a,b,0)` with nonnegative `a,b`. The original `residue` unpacks `(a,b,c)`, checks the fixed plane with `assert c == 0` at **line 87**, then returns `(a%m,b%m)`. It never tests the sign of `a,b`. The original caller `check_spatial` at lines 101–129 supplies proper fixed-positive inputs, so these are **callable-boundary defects** rather than a demonstrated bad in-domain call in the existing original experiment.

Under CPython `-O` or `-OO`, the line-87 `assert` is deleted. Thus for `m=3` the original `residue((1,0,0),3)` and **out-of-chart** `residue((1,0,1),3)` both return `(1,0)`. `first_collision([(1,0,0),(1,0,1)],3)` then reports a collision between two different native signed selected-slice cells; in ordinary mode it rejects the off-plane point with `AssertionError`. Those signed displacements have native shortest path counts `B_min=1` and `B_min=2`, respectively. Hence **no native endpoint identity or BRC multiplicity conclusion follows from this fixed-chart residue alias**.

Separately, the original function admits the negative-coordinate input `(-1,0,0)` in all three modes, and `residue((-1,0,0),3)=(2,0)=residue((2,0,0),3)`. The two signed native displacements have different squared lengths 1 and 4 and different shortest primitive lengths 1 and 2. Modulo congruence itself is valid arithmetic; the defect is the **missing fixed-positive input type gate** if a downstream caller presents such a residue as a native Cell address or a certified fixed-positive chart point.

## Typed correction and executable evidence

The separately published opt-in `strict_sector_residue(point,m)` accepts only exact integer `m>0` and `point=(a,b,0)` with `a,b>=0`. It raises `ValueError` on off-plane, negative, non-exact/Boolean, or nonpositive modulus inputs. `strict_first_collision` carries the same gate before building any collision certificate. The original frozen/current checker remains byte-for-byte unchanged and is **not** superseded.

Independent source-pinned program `research_checks/X6_UNIT114_R063_SECTOR_RESIDUE_TYPE_GATE_CHECK_20261118.py` checks the Git blob of the **actual unchanged original module** before loading it. Actual executions in standard CPython, `-O`, and `-OO` verified:

- **5,225 valid chart residue comparisons per mode** against the original `residue` for radii 0..9 and moduli 2..20;
- **190 valid chart first-collision comparisons per mode** against the original `first_collision`;
- both original invalid-input witnesses with exactly the mode behavior stated above;
- **seven invalid input classes per mode** rejected by the opt-in strict adapter and invalid two-point collision rejected in every mode.

All three modes exited 0 and emitted machine-readable JSON. The executed program SHA-256 is `382704a6005aedfd5e690b216aa9761f25c91175b7dff55cea909848bdf51a4a`, its source matches the published GitHub source, and the unchanged original loaded source has Git blob `643b2bac659a445891dcb5588b647972977104e0`. Exact results and output SHA-256 for each mode are in `research_checks/X6_UNIT114_R063_ORIGINAL_SECTOR_TYPE_GATE_RESULTS_20261118.json`.

**Mathematical type:** the original fixed-positive two-generator modular-sector argument and PathSqrt theorem are retained at their declared sector scope. Under frozen P000 V5 signed Cell geometry (`59538f585d037d09ef687b28715c4bc1a3f9fe03`), off-sector points have distinct native coordinate and path semantics. The repair is an explicit adapter/input gate, not a change of P000, a native signed-axis projection, or evidence that the R063 native C3/C4 benchmark has been run or passed.

## Source and control continuation

Mother source ledger: `research_notes/X6_LP28_SOURCE_CONSUMER_ACTION_CROSSWALK_20261112_ONHOUR_1400.md`, original source blob `2c7c4794a90df294cf3d158cb63ba29886c7babd`; specifically LP028 plus LP003/LP017/LP019/LP023. Previously saved Unit110–111 concerned LP011/LP019 strict native validators; Unit112–113 concerned `rho,G` fibers. Unit114 instead exposes an exact **unchanged 2026-08-22 executable input type gate** and tests that source directly.

Researcher/lane claim provenance (read-only last verified): `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-3e221a50dc8818f914e228f6`, RUN `RUN-95866d78d35721116c362956`. The prior Units110–111 Native PROGRESS original request `onhour-20261118-0821-x6-own-units110-111-native-progress-v1` returned `SUCCEEDED`. The Units112–113 request `onhour-20261118-0852-x6-own-units112-113-native-progress-v1` was last observed `RUNNING/error=null`; it is **not resubmitted**. Source GitHub author evidence and Research Activity are independent of Native semantic PROGRESS.

**Next exact source task:** trace whether any *current* LP028/LP023 caller passes native signed/off-plane or untyped 3D points to the original `residue` or assumes its modulo-sector collision means native Cell/BRC identity. Pin exact `commit:path:line` and show input provenance before patching a live consumer. LP011/LP019 old signed-dominance / positive N-BRC cancellation purported wrong callers remain `UNRESOLVED_PROVENANCE`; deliver bounded negative evidence to independent Driver's `REQUEST_REVISION`. R063 original native benchmark support Issue #2416 remains a separate exact execution item with its unchanged C3/C4 target and gates.

**Author evidence scope:** only this source-boundary experiment is executed. No independent Driver admission, no altered immutable scientific input and no original native C3/C4 replay.
