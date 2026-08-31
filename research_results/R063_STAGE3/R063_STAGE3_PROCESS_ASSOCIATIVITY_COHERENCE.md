# R063 Stage 3 — Process Associativity and Coherence

Status: `FULL_INTERACTION_PROCESS_ASSOCIATIVE_UP_TO_CANONICAL_ISOMORPHISM / BINARY_CANCELLED_PATH_READOUT_NONASSOCIATIVE`
Researcher-ID: `EM-R063S3-F1CF9D`

## Enriched process associator

For finite `C4`-labelled source position posets, interaction multiplication is Cartesian product with labels added mod four. Therefore

`(P box Q) box R ~= P box (Q box R)`

through the canonical rebracketing bijection `((x,y),z) <-> (x,(y,z))`. It preserves every source coordinate, the product partial order and the label sum. This proves process coherence independently of Gaussian/root associativity.

The checker verified this carrier-level associator on all `8^3 = 512` triples of native path representatives belonging to `(1,1)`, `(2,1)` and `(1,2)`. Deterministic certificate SHA-256:

`f7a044cbed0ee705d456a7906754f90e171058e5ce6eced9a79a0d7ae8c2aaae`.

## Cancellation/readout must not be treated as the associative product carrier

If each binary interaction is first maximally cancelled, normalized and replaced by its native target-word relation, then that **binary path relation is not associative**.

Small witness:

`p=ij`, `q=ij`, `r=ji`.

Both first binary `(1,1)x(1,1)` products return the single target word `jj`. Nevertheless

`(p Lift q) Lift r = {jiji, jjii}`,

while

`p Lift (q Lift r) = {iijj, ijij}`.

The sets are disjoint although the final trace is the same `(2,2)`.

## Classification

Associativity survives at the **uncancelled, provenance/order-retaining interaction tensor** and after final trace evaluation. It does not survive if destructive positional cancellation/path readout is inserted as the intermediate binary multiplication.

Therefore repeated multiplication must either retain the full interaction process until the final readout or carry enough cancellation provenance to reconstruct it.

`PROCESS_ASSOCIATIVITY_COHERENCE = CANONICAL_ASSOCIATOR_BEFORE_DESTRUCTIVE_READOUT`.
