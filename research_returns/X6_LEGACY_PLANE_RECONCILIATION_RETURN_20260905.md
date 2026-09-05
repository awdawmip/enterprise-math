# RS-X6-LEGACY-PLANE-RECONCILIATION — Research Return

Status: `SUCCESS / TASK-COMPLETE / MAINTENANCE-ONLY / NO FOUNDATION PROMOTION`
Researcher: `EM-X6P-40B5BD`
Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`
Publication: `TP2-B4A441B23DA3159232C2`
Frozen legacy baseline: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`
Centered-signed baseline: `59538f585d037d09ef687b28715c4bc1a3f9fe03`
Latest-main audit snapshot: `3435b1a4e59b029037ee6bdb026091afc1be8d27`

## 1. Terminal result

The legacy three-axis plane research has been reconciled against the centered signed-X6 slice at claim level.

The correction ledger contains 28 claims:

- `SALVAGEABLE_AFTER_RETYPING`: 12
- `ARCHIVE_ONLY`: 16
- `BROKEN_CURRENT_CONSUMER`: 0

No additional live-definition rewrite is required by this maintenance pass. The centered-slice rebase and the subsequent P000/FCC hardening already repaired the named current consumers. Re-editing them from the older task branch would risk overwriting newer Foundation work, so this return adds exact certification and anti-regression instead.

Historical documents remain valuable as provenance. They are not deleted.

## 2. Centered signed-X6 plane semantics used for reconciliation

For a selected three-axis slice, use the affine signed carrier `Z^3` around the actual chosen Cell center:

`O=(0,0,0)`.

Primitive selected directions are

`±e_1, ±e_2, ±e_3`.

For `p,q in Z^3`:

`delta=q-p`.

Intrinsic squared gauge:

`G(delta)=delta_1^2+delta_2^2+delta_3^2`.

Native shortest step count:

`T(delta)=|delta_1|+|delta_2|+|delta_3|`.

Shortest-path multiplicity:

`M(delta)=T(delta)!/(|delta_1|!|delta_2|!|delta_3|!)`.

Endpoint reversal sends `delta -> -delta`, hence preserves `G`, `T`, and `M`.

## 3. Correct typing of the old min-zero chart

The old min-zero map remains useful only as an observer/carrier section:

`rho(z)=z-min(z)(1,1,1)`.

It is not native Cell identity and is not injective.

Define common level

`mu(z)=min(z)`.

Then the repair pair is globally lossless:

`z=rho(z)+mu(z)(1,1,1)`.

Exact collision witness:

- `z1=(2,-1,0)`, `rho(z1)=(3,0,1)`, `mu(z1)=-1`;
- `z2=(3,0,1)`, `rho(z2)=(3,0,1)`, `mu(z2)=0`.

Thus `rho` alone aliases two distinct signed native points.

The algebraic quotient `Z^3/Z(1,1,1)` is therefore retained only as a derived displacement/carrier observer quotient. It is not a native Cell quotient.

## 4. Reversal reconciliation: the old 25 -> 17 effect

Take raw signed displacement

`d=(3,4,0)`.

Legacy min-zero normalization gives

`rho(d)=(3,4,0)`, so the component-square readout is `25`.

The true reverse is

`-d=(-3,-4,0)`.

If the reverse is independently min-zero-normalized, then

`rho(-d)=(1,0,4)`, whose component-square readout is `17`.

This exactly reproduces the historical `25 -> 17` phenomenon.

Under centered signed semantics, however,

`G(d)=G(-d)=25`

and both directions have shortest-path multiplicity `35`.

Therefore `25 -> 17` is an observer-normalization artifact, not intrinsic directional asymmetry. Any unequal bidirectional pair is retained only as an observer diagnostic.

## 5. Exact N=25 shell recomputation

For the full centered signed shell

`x^2+y^2+z^2=25` in `Z^3`,

the exact census is:

- signed endpoints: `30`;
- support size 1: `6`;
- support size 2: `24`;
- support size 3: `0`.

The 24 support-two vectors are the permutations/signs of `(4,3,0)`, each with `35` shortest path words. The 6 support-one vectors are the signed permutations of `(5,0,0)`, each with one shortest path word.

Hence the full shortest-route BRC mass is

`6*1 + 24*35 = 846`.

The historical positive/min-zero section has exactly `9` representatives and route mass `213`. Those numbers remain exact, but only as an observer-section census; they are not the full physical signed shell.

## 6. BRC reconciliation

BRC remains the preferred first-line path/multiplicity layer.

The retyped rule is:

1. retain signed displacement/path provenance;
2. use absolute component counts for shortest path multiplicity;
3. keep BRC coefficients nonnegative/positive;
4. do not interpret opposite displacement signs as coefficient cancellation;
5. do not collapse to min-zero/carrier address before future native operations unless common level or equivalent repair data is retained.

Thus the multinomial route mathematics survives; the legacy endpoint typing does not.

## 7. Dominant branch / line trace / spectrum / quotient dispositions

- Dominant axis: use `argmax |delta_i|`; orientation sign is separate.
- Line-trace quadratic/parity facts depending only on raw signed displacement survive after variable retyping.
- Intrinsic unoriented segment spectrum collapses to `{N,N}` under reversal.
- Unequal legacy forward/reverse readouts are observer diagnostics only.
- `Z^3/Z(1,1,1)` survives as typed derived/carrier observer structure, never as native point identity.
- Historical triple-circle overlap/origin-one ontology is archive-only.
- The structural six-neighbor local fact survives only after recentering on the actual Cell and using `±` selected axes.

## 8. Live-consumer audit

Audited against the latest-main snapshot:

- `definitions/00_CURRENT_NATIVE_FOUNDATION.md`
- `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`
- `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md`
- `definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md`
- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`
- `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`
- `definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md`
- `definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md`

Result: `NO_BROKEN_CURRENT_CONSUMER_FOUND`.

This is why no live definition was rewritten in this task branch.

## 9. Anti-regression certificate

Checker:

`research_checks/X6_LEGACY_PLANE_RECONCILIATION_CHECK_20260905.py`

It verifies:

- global `rho+mu` reconstruction on a finite signed cube;
- an explicit `rho` collision;
- diagonal-shift invisibility of `rho` with common-level repair;
- exhaustive signed reversal symmetry on a finite endpoint grid;
- exact `25 -> 17` legacy observer artifact;
- exact N=25 shell `30 = 6+24`;
- exact signed BRC mass `846`;
- exact old observer-section count/mass `9 / 213`;
- positive reversal-stable BRC multiplicities;
- six centered signed nearest neighbors.

Observed result:

`PASS RS-X6-LEGACY-PLANE-RECONCILIATION rho+mu=lossless reversal=intrinsic-symmetric legacy_25_to_17=observer-artifact N25_signed=30 support=6+24 BRC_mass=846 legacy_observer_N25=9 legacy_mass=213`

## 10. Method/tool reuse resolution

No new research method is introduced.

Reused current Enterprise methods:

- `T0 / BRC` for route multiplicity and provenance;
- `T6 / quotient-kernel-image` for the diagonal observer quotient and lost common level;
- `T8 / relation-collision` for explicit observer aliasing;
- direct exact finite enumeration for anti-regression.

This is a maintenance reconciliation, not a theorem or Foundation promotion.

## 11. Durable outputs

- `research_artifacts/X6_LEGACY_PLANE_RECONCILIATION/claim_ledger.json`
- `research_artifacts/X6_LEGACY_PLANE_RECONCILIATION/recomputation_summary.json`
- `research_checks/X6_LEGACY_PLANE_RECONCILIATION_CHECK_20260905.py`
- this return
- execution/result records under the task ID.

## 12. Residue

Task-local residue: `NONE`.

Parent-program residue remains outside this task: global X6 rotation dynamics, global six-axis-to-all-slice/carrier transport, and any later theorem-level exploitation of the corrected centered plane semantics.
