# Typed modular alias source review

Status: FINAL SOURCE-SPECIFIC STATIC REVIEW / SHARED CONTEXT / NOT ADMITTED.
No scientific computation, ordinary modular reference execution, new query
or remote write was performed by this reviewer. Existing source and raw
author evidence were read; only files in `review/` are edited here.

## Sources and existing evidence

- `modular_alias/typed_aliases.py` SHA-256:
  `da19ef459e722ccf03326c77e4e67bd2597c7c5c3deb9fde75879f2cef79bfa1`.
- `modular_alias/check_typed_aliases.py` SHA-256:
  `0ceebafccd4cc5da6468218b3bca65dcd8a2795a1928a5920e4f71f20640f5c9`.
- Inherited `lazy_modular.py` SHA-256:
  `08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4`.
- Existing result payload SHA-256:
  `0f4b8618ca2cf7a8ebdfe37cc7a56e48ae857a25d4eb992b28b573653ed305c4`.
- Existing result gzip SHA-256:
  `bb6c6b0cd9ec678ac0239bc318e735ecb5b4ee011b133ad584a0b44260d52c07`.

The author evidence has twelve positive fixtures, twelve rejected negative
controls and 244 actual core calls. These counts and hashes were checked
against the archive without importing or running the scientific modules.

## Completeness and cost

For each target the implementation covers both signs of displacements
using consecutive typed baby powers and giant shifts by the certified
inverse of b^B. It retains every baby exponent sharing a residue, rather
than just one representative. Every nonnegative d<L has one decomposition
d=kB+u with 0<=u<B; the typed sum and comparison reject only the final
block's overflow. The inverse-target pass covers negative d, and its zero
is removed exactly once. Duplicates are rejected after collection.

The program multiplier, inherited table and actual complete permutation
replay are bound. Unit checks and fresh tables use the inherited typed
integer/long-division evidence. Depth zero has only the basis displacement
and does not invent a multiplier. A discovered early return is recorded
as additional information; it does not replace the complete enumeration
with an unproved period promise.

The source and notes charge baby/giant work, all J output displacements,
fresh-table setup and verification, typed digit replays, host bit wiring,
actual core calls and retained evidence separately. A B+L/B+J query bound
does not imply polynomial cost in log N or log L. Baby-map slot counts are
not total live memory, and equal multipliers on different table instances
do not make their setup receipts disappear. No general classical factoring
advantage follows from this enumeration.

The existing N21/depth4/B3 fixture already reports one discarded final-block
candidate. Together with repeated baby residues, nonidentity targets,
negative displacements and depth zero, this covers the important finite
boundaries; no additional tail fixture was required.

## Fixed verifier defect

The first reviewed canonicalizer silently converted dictionary keys to
strings. A map containing integer 1 and string "1" could therefore hide a
modified integer-key alias list during semantic comparison. The revised
source rejects collisions among stringified keys before constructing the
normalized map, and the checker now includes `mixed_key_alias_shadowing`.
The negative evidence preserves typed key entries, avoiding JSON itself
silently merging the attempted adversarial map.

The inherited permutation request is also preserved before verification,
and an obvious changed certificate digest is rejected before costly replay.
This makes the current failed-proof control's evidence/cost accounting
consistent. Source-specific static rereading found no remaining arithmetic
or completeness defect on the declared fresh-output path.

## Remaining API scope

`verify_alias_result` is a semantic-content replay, not a strict independent
JSON type-schema validator. Python numeric equality can equate 0.0 or False
with integer zero. Fresh discovery emits integer labels, and the carry
consumer strictly requires actual integers, so this does not silently alter
the bounded execution reviewed here. Future use with arbitrary external
certificates should add strict schema checking or retain that strict
consumer validation. This observation did not justify changing the source
already bound to the author's active execution.

The verifier returns a newly reconstructed replay, including its metrics;
the original top-level metrics are not independently authoritative. Shared
process cache warmth and replay ordering also preclude reading core-call
deltas as a cold-runtime or total-bit-operation speedup.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1
