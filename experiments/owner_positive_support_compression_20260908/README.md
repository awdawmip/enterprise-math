# Positive-support raw compression

This is a bounded executable extension of the existing one-positive consumer,
following [the positive-support compression paper](../../research_notes/OWNER_POSITIVE_SUPPORT_RAW_COMPRESSION_REVIEW_20260908.md).
The paper supplies the finite-mass argument; this certificate records the
specified executable cases and their actual checks. It does not turn finite
examples into a proof for arbitrary inputs.

## Input and preserved quantities

`audit_compression(case_id, mu_atoms, nu_atoms, denominator=1)` accepts two
finite positive populations. Every atom is a canonical `x6_signed.Spatial6`
and a strictly positive integer numerator. Both populations use the same
positive integer denominator, retained as the unevaluated canonical
`DIV(1, denominator)` unit. Boolean, zero, negative, and noninteger weights or
denominators are rejected. Signed coefficients appear only in the auxiliary
difference ledger; they are never negative branch weights in a BRC primitive.

The consumer reuses `population` to aggregate each population, cancels the
shared mass, and derives the actual Jordan positive support S. For nonempty S,
axis i retains its set A_i of positive-site coordinates and sends every other
integer to `max(A_i)+1`. It pushes the finite signed ledger through this map.
For empty S it instead uses the constant map to the origin, without taking
the maximum of an empty set.

Each case checks every original positive site and its individual mass, Jordan
P and N, global L1, and the L1 of every one of the twenty raw three-axis
marginals. D is their sum, not their average or their maximum. Raw tables are
computed by the reused `raw_projection`; the reused `verify_joint_projection`
actually invokes the native slice and reconstruction functions both before
and after compression. Raw addresses may change. The native joint
`(can3, common offset)` representation remains lossless for each current
table; an isolated can3 histogram is a different observation.

The consumer also checks idempotence, recomputation of the same specification,
population pushforward commuting with cancellation, membership in the
symbolic carrier, and
`actual support <= product_i(|A_i|+1) <= (p+1)^6`.
It computes this product of six cardinalities without enumerating the carrier.
For p=0 the chosen carrier has one point; the zero difference occupies none.
No ratio is formed in the new compression ledger, including at D=0.

## Fixed certificate

The saved certificate contains 18 cases and 360 raw tables; every table has
both its original and compressed signed rows and one verified common L1.
Zero-valued raw rows can remain as explicit cancellation evidence.

| Check | Executed coverage |
| --- | --- |
| Initial negative collision | Positive masses 5 and 7; negative masses 3 and 4 merge. P=12, N=7, global L1=19, D=380; support 4 becomes 3; carrier 96. |
| Two positive sites | r=1 through 6 differing axes; carrier `3^r * 2^(6-r)` is 96, 144, 216, 324, 486, 729. Actual support remains 3. Every case includes raw projections with positive/negative cancellation and others with fully separated signs. |
| Aggregation and cancellation | Duplicate atoms and common masses yield exactly the same signed difference, specification, and raw tables as the initial case. |
| Translation | A mixed-sign integral translation commutes with compression for the tested nonempty S, with all twenty raw L1 values preserved. Native displacement is checked. |
| Axis permutation | Canonical `Spatial6.rotate` commutes with compression; all twenty L1 values match the corresponding relabelled slices. |
| Old-consumer compatibility | Nonpositive nonzero, empty zero, cancelled zero, p=1 equal-mass equality, and p=1 general equality cases are compared before and after compression. |
| Large literal mass unit | The 2053-bit denominator `2^2052+1` is retained exactly in DIV nodes for the unit, L1, and D. |
| Changed S | A freshly recomputed map preserves a signed difference that the old-S map would destroy. |
| can3 boundary raw control | The raw norm remains intact in the input used to demonstrate can3-alone loss. |

The old `audit_case` enforces p<=1. This extension invokes it only for the five
explicit p=0/p=1 compatibility cases, before and after compression. These
comparisons retain its twenty table norms, per-table fibre identities, axis
negative masses, `3/20` and equal-mass `1/10` bounds, and distinct equality/zero
statuses. It is never used to certify a two-positive input. No new two-positive
sharp constant is computed or asserted here.

Ten rejection checks cover four invalid weight types/values, four invalid
denominators, a noncanonical cell, and a deliberately wrong expected source
digest. The last check does not edit a source file.

Two additional entries are explicit failure boundaries:

- The map made for S={0} sends both sites of `delta_(2e0)-delta_(3e0)` to e0,
  lowering global L1 from 2 to 0. `validated_compression` rejects that stale
  specification. The low-level `pushforward` alone makes no preservation
  promise for an unrelated specification.
- For `delta_0-delta_(1,2,3,0,0,0)`, the can3-only norm on axes (0,1,2) changes
  from 2 to 0. The equality assertion is expected to fail, while raw L1 is 2
  on both sides and joint reconstruction succeeds.

## Sources and actual native calls

Fourteen exact runtime source pins are in `SOURCE_SHA256` and the certificate:
the old consumer's twelve original pins, the old consumer itself, and the
compression paper. The two added pins are verified before importing the old
consumer by its ordinary module name. That consumer validates its own twelve
pins and canonical module identities; all fourteen are checked again around
the fixed certificate build.

The earlier nineteen-item lookup has the decision `EXTEND_EXISTING_TOOL`.
Its catalog SHA256 is recorded solely as the paper's reuse snapshot. The
catalog is not read or pinned dynamically by this consumer. T6 contributes
only its already stated descent contract; its implementation is not called,
and this work does not reopen a search or alter catalog metadata.

During the fixed build, `sys.setprofile` counts actual calls to the reused
consumer and canonical X6/BRC/exact-arithmetic modules. The build requires
actual calls to population aggregation, raw projection, joint reconstruction,
DIV construction, native slice/reconstruction, axis rotation, and unit steps.
The certificate lists all observed selected counts. Only the old p<=1
compatibility checks call the permitted BRC support-size helper. They do not
call path multiplicity, quotient materialization, roots, or Fraction arithmetic.

This observation starts after canonical imports and ends after the fixed
build. It does not certify import-time behavior, unexecuted paths, every C
operation, or all transitive historical code. The selected new Python source
can also be checked independently with the repository's arithmetic-policy
checker.

Compression is an analysis-level coordinate encoding. It is not a physical
motion, native isometry, new axis, preservation of word/path multiplicity,
reconstruction of erased history, or lossless reduction of every BRC object.

## Reproduce

From the repository root:

```powershell
python -X utf8 -B experiments/owner_positive_support_compression_20260908/check_positive_support_compression.py
python -X utf8 -B tools/check_exact_arithmetic_policy.py experiments/owner_positive_support_compression_20260908/check_positive_support_compression.py
```

The first command recomputes the fixed certificate and requires an exact byte
match. It does not update the certificate. To explicitly regenerate this
directory's certificate after a reviewed change, use:

```powershell
python -X utf8 -B experiments/owner_positive_support_compression_20260908/check_positive_support_compression.py --write
```

The certificate records this checker's SHA256. A changed checker or pinned
source cannot silently reuse a previous successful certificate. The `--write`
option is the only file mutation in the program and targets this directory's
`certificate.json` only.

This auxiliary owner experiment creates no formal Task, Result, claim,
WorkingTruth, catalog entry, or acceptance state. The existing tools and
papers retain their contents and scope.

Global-Knowledge-Sync: main@eb09a0a / GLOBAL_KNOWLEDGE_V1
