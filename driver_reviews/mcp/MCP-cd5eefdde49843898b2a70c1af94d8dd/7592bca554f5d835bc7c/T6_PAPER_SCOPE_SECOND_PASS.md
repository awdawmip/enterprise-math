# T6 frozen Result: bounded independent paper second pass

Scope: RR-C428294CF760BD8D99AA / RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND / TP2-34B106D2512A298C9647.

Source observation: `2f257c02d95b9cd630c23284bea2516a1be3f853`, from ROOT_RECEIPT_278_FINAL.json. Prior BYTE_PIN_AUDIT.json independently binds all 28 formal outputs and all 33 saved Source artifact pins without drift.

This pass read PROOF.md and RETURN.md completely, and only necessary static JSON. No author Python source was inspected or executed; no producer, checker, enumeration campaign, remote call, identity, claim, Source write, mathematical acceptance or promotion was performed. A second read-only agent independently reviewed the p19 split/cancellation argument. All arithmetic arrays and classical number-theoretic arguments retain their external auxiliary-model type; no HEARTBEAT_X6 native geometry is promoted or changed.

## Paper findings

### p17 valuation-two support and mass guard is sound

PROOF.md lines 247–254 state the guard correctly. Its abbreviated Vandermonde step can be expanded without a computation campaign:

1. Every denominator is at most 2332. Valuation three at 17 requires at least 4913, so only valuations zero, one and two are possible. The valuation-two atoms are exactly `a=289m`, `1<=m<=8`.
2. After global common-atom cancellation, the signed multiplicity satisfies `|z_m|<=8<17`, since nine atoms of even the cheapest valuation-two weight 288 exceed a single side budget 2331.
3. Multiply the reciprocal moment equations for `k=1,...,6` by `17^(2k)` and reduce modulo 17. Valuation-zero/one terms vanish, leaving `sum z_m m^(-k)=0`.
4. Put `x_m=m^(-1) mod17`. Any support of size `s<=6` has an invertible first-`s)-row matrix `(x_m^k)_{k=1,...,s}`: its determinant is `(product x_m) product_(i<j)(x_j-x_i)`, a nonzero field element. A nonzero vector therefore needs at least seven support positions.
5. Because nonzero integer coefficients cannot vanish modulo 17 under `|z_m|<17`, integer and modular support coincide. Every supported position uses at least one atom in the combined positive/negative mass. The cheapest seven distinct positions cost `sum_(m=1)^7(289m-1)=8085>2*2331=4662`.

This uses the combined budget, not seven atoms on one side. No support or sign loophole was found.

### p19 splits and common-atom cancellation are paper-complete

Each side has vertical order at most six because `7*361+18>2331`. Up to global sign, orders 9–12 therefore consist exactly of:

| Total order | Splits |
| --- | --- |
| 9 | (3,6), (4,5) |
| 10 | (4,6), (5,5) |
| 11 | (5,6) |
| 12 | (6,6) |

PROOF.md lines 38–39 normalize by cancelling all common exponent atoms before choosing the maximal prime. This preserves every observer equality and decreases both side costs. Thus globally normalized primitive configurations cannot contain a shared vertical atom. In equal-order blocks, `j>i` removes global sign duplication; identical states are nonprimitive because their vertical atoms are common. No split or cancellation coverage omission was found.

An original collision whose 19-atoms all cancel belongs to a lower maximal-prime problem after normalization; it is not ruled out by the primitive-p19 result alone. This is consistent with the explicitly OPEN global T6 target.

### Static numerical inequalities agree with serialized JSON

Using arbitrary-precision integer cross-comparisons only:

- All 16 serialized p17 Gram-Schmidt squared lengths exceed `10867122=2*2331^2`.
- All 18 serialized p19 lengths exceed both `4052900=4*(869^2+508^2)` and `6138036=4*(1230^2+147^2)`.

These comparisons check the displayed inequalities against saved rational entries. They do not independently reconstruct Gram-Schmidt values, lattice saturation, basis congruences, state generation or candidate rejection from the basis. The highest-nonzero-coefficient q0 argument in PROOF.md lines 256–263 is valid conditional on that exact basis/certificate construction.

## Review boundaries and allowable progress strength

1. **Orders 0–8 are consumed verified frozen inputs, not a newly identified mathematical gap.** PROOF.md lines 233–237 and coverage_p19.json declare them task-authorized and previously verified, consumed without replay. The Source-pinned dossier belongs to the 33-pin packet; the parent has read its exact Global-Knowledge prior-input commit provenance. This bounded second pass did not reverify those inputs and does not request their replay. The six-block ledger supplements, rather than reproves, the frozen inputs.

2. **The census has not been independently reexecuted in this pass.** The `70,285,694` primitive instances and null kernels are byte-bound authored outputs. No Python source was read, so this pass did not establish that actual state generators, nearest-coordinate choices, floor bounds and final budget checks implement the paper algorithm without omission. PROOF.md lines 226–231 itself requires completeness proof plus producer review/replay, not metadata aggregation alone.

3. **Certificate reconstruction is distinct from this paper pass.** Its static inequality and the conditional q0 proof are checked above; this pass did not regenerate determinant, congruences, saturation or Gram-Schmidt data. The saved consumer PASS is preserved as authored execution evidence, not relabeled as our execution. The parent separately reports one bounded independent determinant/congruence/Gram-Schmidt/projector/mu/98-representative reconstruction PASS; this report does not duplicate that work or request more calculation.

Permitted conclusion for this pass:

`BYTE_PINS_VERIFIED / PAPER_REDUCTION_AND_COVERAGE_FRAMEWORK_REVIEWED / SERIALIZED_SCALAR_BOUNDS_CHECKED / PRIOR_0_TO_8_CONSUMED_AS_VERIFIED_FROZEN_INPUT / AUTHOR_RESEARCHER_CENSUS_PROGRESS_PRESERVED_WITH_INDEPENDENT_CENSUS_BOUNDARY`.

It does not grant independent full-p19 census verification, Driver acceptance, Working Truth, Foundation status or global T6=2332. The full-census boundary remains explicit; no repeat campaign or replay of frozen prior work is requested by this report.

The recorded next prospective mathematical unit remains maximal p17 vertical order one, split (0,1), within the same existing task. That bounded unit has mathematical value without requiring the whole T6 target to be satisfied first. NEXT_FRONTIER.json explicitly reports failure of the sufficient unique-nearest-plane gate; a future executor must use an exact multi-candidate method or a separately proved stronger reduction. No live execution or authorization is inferred from this recommendation.

## Source locations

Reviewed artifact directory:

`/workspace/em-owner-resume-20261011/new-round-20261011/geo6-atomic-repair-current-20261011/validation-root/research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/`

Complete paper inputs: `PROOF.md`, `RETURN.md`.

Necessary static JSON: `p17_q0_certificate.json`, `p17_validation.json`, `input.json`, `coverage_p19.json`, `coverage_4_5.json`, `block_4_6.json`, `block_5_5.json`, `block_5_6.json`, `block_6_6.json`, `audit_3_6.json`, `NEXT_FRONTIER.json`, `RUN_MANIFEST.json`, `control_dependency.json`.
