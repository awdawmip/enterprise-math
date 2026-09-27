# Shared-context review of the unit-residual closure

Status: PASS — complete symbolic source review, not executed, not independently admitted. No scientific import, host numerical test or new literature query was used.

Reviewed source: `../UNIT_RESIDUAL_CLOSURE.md`, SHA256 `f1a41cd87293866f14c22b34d066739c129cb600861daed8bd69e4df2573f57d`. Its mixed-reciprocity dependency is `2f2f90d23324c3a672aec67e8ff7783ebfcb511fef6cdfae774e06a106a0949a`, and its ordinary degree-five proof is `1453444f21c113c0d1819328b731031d0fe296e25756caac7e94d9cf628047b6`. No material mathematical defect was found.

## Reduction and signs

The gcd reduction (3) is valid with signed `B`: after Euclidean division `B=g*B0+b0`, the fractional offset `b0/g` is in `[0,1)` and cannot move an integer numerator across a multiple of the integer denominator `r`. Divisibility of `B` by `g` is unnecessary.

For a negative unit residual, `(A*r-1)j+B0` gives `A*j-floor((j+r-1-B0)/r)`. The transformed offset `r-1-B0` is correct, including negative original offsets; reusing `B0` would be wrong. Fixed-power expansion preserves total degree and introduces no new parameter family per exponent. The `r=1` case is affine and separately handled. When `r=2` admits both descriptions, a deterministic convention avoids duplication without changing correctness.

## Two-table terminal identity

Both unit-slope quotient sequences jump by exactly one at integer positions. The retained locations are in `1..N-1`; there is no hidden clamp or jump at the initial sample. At an `A` jump, the left-limit value of `B` is exactly `floor((m*k-c+d-1)/r)`. At a `B` jump, the updated value of `A` is `floor((r*l-d+c)/m)`. Updating `A` first at a tie makes the two product increments telescope to the full increment, also when either quotient is negative.

Each jump affects sample indices `j>=J`. Subtracting its omitted initial weight `S_a(J)` from the endpoint representation gives (7). This proves the identity for `N=1`, coincident jumps at `N-1`, `m=1` or `r=1`, and zero exponents. `Delta_0=0` omits a correction; it does not change the constant-power convention.

Shifting the two jump ranges produces exactly the tuples (8). The polynomial multiplying the remaining floor in the first correction has degree at most `a+b`; the second has degree at most `a+e`. Including the floor power gives at most `a+b+e<=D`. The tuples depend on the fixed input parameters and offsets, not on the exponent triple, so all expanded terms reuse at most two full ordinary tables. Empty or zero-increment corrections need no fabricated table. A combined Faulhaber numerator must be divided exactly; termwise integer division is not justified.

## Scope and cost

This is a terminating algebraic reduction for a sufficient family, not another unproved mixed recursion. With fixed degree, eligibility arithmetic, coefficient expansion and two single-floor Euclidean chains have polynomial bit cost under the stated arithmetic contract. Endpoint and gcd costs, typed source admission, replay and evidence storage remain chargeable. There is no empirical speed claim here.

For `p=2V`, both `R=p-1` and `R=p+1` satisfy the signed-unit condition, with `R=1` handled by the affine branch. This covers arbitrary selected-bit separation within the stated non-top two-bit family. The conservative 14 tables per orientation / 28 for both orientations follows from the preceding spline reduction; it counts parameter-table requests, not primitive calls. Both orientation multiplicities and the original `4^-g` normalization remain intact. The reduced denominator `r` is distinct from a requested modular residue.

The separate split into `m` residue classes is cheap only when `m` is bounded; it does not establish a general bit-polynomial route. Larger residuals remain unresolved by this note, without a hardness or necessity claim. Supplied order and group address are still paid dependencies. This theorem neither evaluates general chronological matrix weights nor closes full Shor sampling.

The implementation continuation in section 6 is appropriate: record eligibility and offset arithmetic, exact ranges, table references and coefficient reconstruction, then test strict fresh replay and preserve rejected paid work. No such implementation or execution is certified by this review.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1 (reviewer-read snapshot; later coordinator/author journal markers are not new reviewer policy reads).
