# D25/LIFT — exact information loss of the balanced 2+2 scalar/rank observer

**2026-10-28 · AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.**
This is a new *observer-fiber census* deduced from (and not a repetition of) the previously published author-only balanced 2+2 all-rank orbit theorem. Same author contribution context; **not** an independent review, native H0/B0 execution, or Source Result.

**Parent:** `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` (OPEN).
**Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`.
**Publication:** `TP2-B6F4FC938FF94941C1B7`.
**Frozen scientific Source pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).
**Dependency:** `D25_BALANCED_22_ALLRANK_GAUGE_QUOTIENT_20261028.md` on this same PR.

## Exact mathematical statement

Take an odd prime power `q`, `k=F_q`, distinct `a,b in k`, and the **auxiliary** matrix
`A=diag(a I_2,b I_2)`. A marked source matrix `B in M_4(k)` produces
`K=[B,A]=[[0,X],[Y,0]]`, with `X=(b-a)B12` and `Y=(a-b)B21`.
Every ordered pair `(X,Y)` occurs, and every such pair has exactly `q^8` marked source matrices `B` before imposing any equivalence on the source blocks.

The FULL residual centralizer `G=GL_2(k) x GL_2(k)` acts as
`(P,Q)*(X,Y)=(P X Q^{-1}, Q Y P^{-1})`.
Consider the four-coordinate BRC compression
`O(X,Y)=(rank X,rank Y,trace(YX),det(YX))`.
We count gauge **orbits within a given observer fiber**, not just distinct matrices in that fiber.

**Theorem (all odd prime powers):** `O` has exactly
`M(q)=q^2+2q+5` distinct values, while the preceding all-rank classification gives
`N(q)=q^2+3q+6` G-orbits. Precisely:

- `O=(1,1,0,0)` contains **3 distinct** G-orbits.
- For every `lambda in k^*`, the value `O=(2,2,2 lambda,lambda^2)` contains **2 distinct** G-orbits. These are `q-1` distinct observer values.
- Every other realized value of `O` contains **1** G-orbit.

Therefore there are exactly `q` ambiguous observer values and exactly
`N(q)-M(q)=q+1` lost orbit distinctions; the maximum ambiguity of a single `O` value is three. There are `q^2+q+5` singleton values. This is a classification theorem conditional on FULL G; it is not an original-class or native-gauge count.

## Proof (consuming the prior normal forms, not re-proving them)

**rank X=0.** The remaining action on Y is left/right basis change. Thus rank Y in `{0,1,2}` gives exactly three orbit and observer values, all distinct.

**rank X=1.** Put `X=E11`, write `Y=[[u,v],[w,z]]`. Then `tr(YX)=u` and `det(YX)=0`. For every nonzero `u`, the previous complete stabilizer normal forms say that rank Y=1 versus 2 distinguishes exactly two orbits. Hence `2(q-1)` distinct unambiguous O values. For `u=0`, rank Y=0,1,2 yields 3 observer values: ranks 0 and 2 are each single orbits, but rank 1 has **three** orbits, represented by `Y=E22,E12,E21`. Their ordered composite-rank pairs `(rank XY,rank YX)` are `(0,0),(1,0),(0,1)`. The prior stabilizer calculation proves this exhausts rank1 X, rank1 Y, u=0; in particular it is not permissible to identify forward and reverse arrows using scalar cancellation. In this stratum there are `2q+1` observer values and `2q+3` orbits.

**rank X=2.** Set X=I and C=YX, leaving simultaneous similarity of C. Every monic quadratic polynomial occurs as a characteristic polynomial, yielding `q^2` possible pairs (trace C, det C). When (trace,det)=(0,0), the zero scalar and the nonzero nilpotent Jordan matrix have different ranks, adding one extra O value. Thus there are `q^2+1` O values. For any nonrepeated characteristic polynomial, similarity class is unique; for repeated eigenvalue lambda there are exactly two classes, scalar lambda I and Jordan lambda I+E12. At lambda=0 their ranks differ, but for each `lambda != 0` both have rank2 and the same O. Exactly q-1 double fibers result.

Add the disjoint rank-X strata: `M=3+(2q+1)+(q^2+1)=q^2+2q+5`, and the fiber multiplicity excess is `(3-1)+(q-1)(2-1)=q+1`. Hence the quoted N and complete fiber table. QED.

## Minimal repair relative to the declared gauge-orbit goal

Only in O=(1,1,0,0) retain the ordered pair of flags `(rank XY,rank YX)`, distinguishing three possibilities; a single Boolean cannot suffice. Only in O=(2,2,2lambda,lambda^2), lambda != 0, retain one Jordan bit `1[C != lambda I]`. No new invariant is required on other O-fibers. This is *fiberwise minimal distinguishability* on the **full G quotient**, not a globally minimal native state: smaller actual gauge groups, future non-gauge-invariant operations, and the diagonal source blocks of B can require more information.

## p=373 exact negative certificates and computation

`M(373)=139880`, `N(373)=140254`, total loss `374`: one triple fiber, 372 double fibers, all others singleton. At `X=E11`, the three rank1 matrices `Y=E22,E12,E21` share O=(1,1,0,0) yet have distinct oriented composite flags. At `X=I2`, the matrices `Y=I2` and `Y=I2+E12` share O=(2,2,2,1) but differ in their Jordan bit.

The **actual author-side local Python program** did two checks. (i) Enumerated all Y for canonical X=0,E11,I2 over p=3,5,7,11,13 and confirmed exact multiplicity histogram. (ii) Independently of those normal-form labels, explicitly generated GL2(p)^2-orbits on the **complete** p^8 universes for p=3 and 5, i.e. 6561 and 390625 matrix pairs and 39366 and 2343750 generator transitions respectively, confirming 24 and 46 actual orbits and matching every O-fiber multiplicity. All assertions passed. The companion **short reproducible checker** `d25_balanced22_scalar_observer_fibers_portable_shortcheck_20261028.py` (Git blob `d0f73698c54caa3de55519d85180264d6d252218`) was also executed and passed for the five finite fields and p373 witnesses. These are same-author checks, not independent review; the theorem for all odd q rests on the above proof.

## BRC/source and honest continuation

This argument preserves the ordered signed source arrows X and Y and the declared future multiplication operations XY,YX before taking a quotient. Its 2x2 matrices are **external finite-field auxiliaries**, not a two-dimensional native space or a proof about the three-dimensional native slice. P000's six-axis space, separate time, triadic balance and residual-provenance restrictions remain intact. The original source-bound H0/B0 p373 benchmark still requires actual rank, coefficient `[X]U mod 139129`, Frobenius direction/eta, first-even A, actual gauge H, signed Green/Hesse observer, kappa and Delta_p-R_p. Issue #1559 is PENDING_OWNER; no evaluator or experiment is implied here.

Priority **UR V2 exact original four-file bundle** remains `UNVERIFIED_BYTES`: historical 94687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. The existing mathematics is complete; do not reconstruct/reprove it. This turn searched GitHub hash/size, relevant commit text, Drive name and Library materials, without obtaining an original matching byte stream. Next legal action: obtain original bytes, verify both size/hash, and repair writer/provenance only under real Source authority. Do not count author drafts as predecessor completed research.

Gateway 0.6.11 read-only status: `executor_binding_configured=false`, `research_authority_granted=false`, active control jobs 5/5; source control sync `UPSTREAM_CODE_REVIEW_REQUIRED`. Old request `r40_20261028_0239_task_inventory_read_v1` returns `CONTROL_REQUEST_NOT_FOUND`, own checkpoint list `ACCESS_DENIED`; Sites `static_machine_readonly/write_relay_enabled=false`. No Source recovery_status executable route was exposed, no valid session/claim/run pointer was recovered, and no CLAIM/OPEN/checkpoint/freeze/acceptance occurred. For a future `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS` seed, `frontier_notes.completed_units=[]` pending actual Source predecessor verification. Preserve current draft as staging/do-not-repeat only; continue exact Source continuation before any new dispatch. Frozen source pin and original recurring task settings unchanged.
