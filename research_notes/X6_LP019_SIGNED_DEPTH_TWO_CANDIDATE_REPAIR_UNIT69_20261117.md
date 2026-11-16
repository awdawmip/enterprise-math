# X6 Unit 69 — Two-candidate signed native depth reconstruction from (can3,G,T)

Date: 2026-11-17. Parent: `RS-X6-LEGACY-PLANE-RECONCILIATION`, immutable publication `TP2-B4A441B23DA3159232C2`. Research scope: author-side precise mathematical consequence of Unit68's observer collision; **AUTHOR-EXACT / SCOPED FINITE EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Frozen inputs and typed scope

- Native scientific pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. P000 V5 remains ACTIVE_LOCKED. Current behavioral rules read separately.
- Native observer producer at frozen pin: `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py`, Git blob `ac32f6d82a91db99297e587cf63b0df95cece514`; native positive path counter `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, blob `300a96e3dc24bf6fff73743037a0347a8bc83176`.
- Fix a *registered ordered three-axis native slice* of `Z^6`, with remaining three signed displacement components **known to be zero**. A native displacement in this slice is `z=(z1,z2,z3)` in `Z^3`. Observe its min-zero carrier section `r=can3(z)=z-h(1,1,1)`, `h=min(z)`. Also retain exact native squared norm `G(z)=sum_i z_i^2` and shortest signed-axis path length `T(z)=sum_i |z_i|`. The selected axes and native observer type are part of the input.
- Natural N-BRC shortest-path multiplicity is `N(z)=T(z)!/prod_i |z_i|!`, the restricted original frozen signed-BRC interface.

## Exact theorem: the fiber has cardinality at most two

Let `r=(r1,r2,r3)` be a min-zero nonnegative integer triple, `g>=0` an exact integer squared norm, and `t>=0` an exact integer length. Put `R=r1+r2+r3`, `Q=r1^2+r2^2+r3^2` and `D=R^2+3(g-Q)`.

Every signed native `z` whose observer triple is `r`, norm is `g`, and shortest length is `t`, is uniquely of form `z=r+h(1,1,1)` for one integer `h`. Substitution gives

```text
g=Q+2Rh+3h^2,
D=R^2+3(g-Q)=(R+3h)^2,
h=(-R+sqrt(D))/3 or h=(-R-sqrt(D))/3.
```

Consequently the *complete exact candidate algorithm* is: require `D>=0` to be an integer square; take the at most two integral roots above; retain only roots for which `sum_i |r_i+h|=t`; reconstruct `z_i=r_i+h`. Every candidate matches the declared `r`, `g`, `t`, and every valid native displacement arises in this way. No third distinct candidate exists.

A one-bit branch selector is sufficient for exact reconstruction when two candidates remain, with no selector bit required when the fiber is singleton. **This is a conditional recovery cost with exact `r,g,t` already available, not an end-to-end input encoding bound.** Once `h` is recovered, the raw signed endpoint and its N-BRC mass are reconstructed by the original formula.

## Sharpness and actual multiplicity obstruction

For `r=(3,0,0)`, `g=18`, `t=6`, the formula yields `D=144`, giving two feasible depths `h=-3` and `h=1`. The corresponding signed native displacements are `(0,-3,-3)` and `(4,1,1)`, both embedded with other three coordinates zero. The exact shortest BRC counts are `6!/(3!3!)=20` and `6!/(4!1!1!)=30`, respectively. Thus the one-bit worst-case requirement is sharp for reconstructing the endpoint and even for reconstructing natural N-BRC multiplicity.

This uses the already saved Unit68 collision as a *sharp selector lower-bound witness*. The new conclusion is the **global upper bound of two fibers, explicit discriminant test, and exact recovery algorithm**. The existing frozen `x6_signed.py` already carries the lossless `(r,h)` chart: we derive how far the `h` state can be conditionally compressed when `G` and `T` are retained. No new primitive, no P000 revision, and no cross-slice claim are introduced.

## Independently executed, bounded finite check

The exact Python checker enumerated all **9,261** ordered signed triples in `[-10,10]^3`, grouped by `(r,G,T)`, verified each raw displacement belongs to the two-root candidate set, and checked exact reconstruction. It found **8,801** distinct observed fibers: **8,341 singletons** and **460 doubletons**. Of the doubletons, **180** have unequal natural BRC masses. The old Unit68 witness passed exactly with depths `(-3,1)` and masses `(20,30)`. No violations were found.

This finite census checks the independent universal algebraic proof within the stated box; it is not a rerun of original R063 or Helly native benchmarks. The program's failures raise `ValueError`, independent of Python optimization removal of `assert`.

- [Executed source/checker](../research_checks/X6_UNIT69_SIGNED_DEPTH_TWO_CANDIDATE_EXACT_20261117.py)
- [Machine-readable exact census](../research_checks/X6_UNIT69_SIGNED_DEPTH_TWO_CANDIDATE_RESULTS_20261117.json)

## Downstream consumer and mother-task disposition

This is a **typed adapter/recovery theorem** for LP003–LP005/LP011/LP019/LP023/LP026: on a selected signed native three-axis slice, a current consumer that has exact `(can3,G,T)` can carry a two-element depth candidate set and at most one extra selector bit, then call the existing native BRC interface on reconstructed signed coordinates. It cannot silently pick the positive-depth branch, discard the branch ID, or identify signed branch amplitudes with positive path counts.

The original current `definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md` and `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md` are already typed as relative-observer constructs. No verified erroneous consumer is assigned to them. Their historical `can3` is a quotient section and the current native metric is the raw signed `G`. The actual historical *incorrect signed native argmax caller* alleged by LP011 and the actual historical *incorrect subtraction of positive N-BRC* alleged by LP019 both remain **UNRESOLVED_PROVENANCE** pending exact frozen source line and actual consumed interface. The scoped R063 Stage3 original PR #574 C4 derived signed interaction remains separate; its `assert` optimization guard repair belongs to its owner or authorized reviewer. The other 28-LP actual consumer graph and independent Driver `REQUEST_REVISION` remain open.

## Operational evidence and continuation

Prior original native Source request `onhour-20261117-0017-x6-unit66-68-saved-author-native-progress-v1` was actually read as **SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED**, authenticated; Source commit `1c61053c3b1191f564f99a26405c4b30761d1eea`. Unit69 author evidence here is a new, independently bounded research unit and does **not** assert a new Native Source progress publication or formal review. Latest exact continuation `onhour-20261117-0058-x6-exact-continuation-read-v1` succeeded: as-of 2026-11-16T17:01:34.993Z runtime claim `MCP-579c8e23625448582b421831` was LEASED, and fresh execution permission was not granted by that read. Preserve existing Research SID `MCP-082892eb480e45dea6d4b9fcc0491034`, researcher `EM-X6-FB6990`, run `RUN-fb25028676f9692ab1bacaee`, and this Research lane's stable logical conversation. No maintenance-lane identity is used.

**Next precise action:** reconcile any remaining original native effects, confirm the actual Source owner/lease and authenticated own execution capability before Native checkpoint; integrate this author's verified proof/checker/certificate under the lawful Source path; then audit exact current consumers using `(can3,G,T)` for type-safe reconstruction and finish the unresolved historical LP011/LP019 caller attribution and 28-LP graph before Driver review. Author proof/certificate are not an independent Driver verdict.
