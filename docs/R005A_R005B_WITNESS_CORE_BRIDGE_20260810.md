# R005-A / R005-B — Witness Core and Kernel-Safety Bridge

Status: `PROVED GENERIC STRUCTURE + EXACT BOUNDED CROSS-ROUTE EVIDENCE / LEAN CANDIDATE / LOCAL_LEAN_PENDING / NOT CANONICAL`  
Date: `2026-08-10`  
R005-A owner: `research/r005a-prime-algorithm-lab-20260810`  
R005-B consumed result: Prime–Collapse Field Geometry Draft owner record; no R005-B source is modified here.

## 1. Bridge I — witness cover versus signature-kernel safety

For selected witness family `A`, define `SameSignature` by equality of every selected PASS/FAIL bit.  `SignaturePrimalitySafe` means signature equality never identifies a prime with a composite.

### T-A7.1

For a prime-sound witness language:

`CoversComposites(A) -> SignaturePrimalitySafe(A)`.

No existence-of-prime assumption is needed.

### T-A7.2 — prime-anchor boundary

If the declared domain contains at least one actual prime, then:

`SignaturePrimalitySafe(A) <-> CoversComposites(A)`.

The prime-existence hypothesis is essential for the reverse implication.  On a prime-free domain such as `{4,6}`, the empty signature is primality-safe because the prime/composite label is constantly COMPOSITE, while an empty witness family rejects nothing.

This is an anti-circularity boundary for prime-existence research: quotient/kernel safety alone cannot be used to infer witness coverage and then bootstrap the existence of a prime in a domain that may itself be prime-free.

## 2. Bridge II — forced core and residual hypergraph

A witness is **forced** when it has an exclusive composite collision: some composite is rejected by that witness and passed by every other witness.  Under a full witness universe that covers all composites:

`ForcedWitness(w) <-> MandatoryWitness(w)`.

Let `ForcedBasis` be the set of forced witnesses.  The generic least-basis criterion is:

`least safe family exists <-> ForcedBasis covers all composites`.

Equivalently:

`least safe family exists <-> no ResidualComposite survives the forced core`.

For each residual composite `n`, let its residual hyperedge be the non-forced witnesses that reject `n`.  Then every safe witness family consists of:

`ForcedBasis + a hitting set of all residual edges`.

This separates three notions that must not be conflated:

1. least family under inclusion;
2. inclusion-minimal family;
3. minimum-cardinality family.

## 3. p-power basin divisor-witness specialization

Consume the R005-B universal horizon

`F_p(k)=isqrt((k+1)^p-1)`

for the basin

`k^p < n < (k+1)^p`.

Candidate witnesses are primes `q<=F_p(k)` and `q` rejects `n` iff `q|n`.  For `k>=2`, this is prime-sound inside the basin and the full candidate universe covers every composite by the square-root factor bound.

## 4. Earliest square-basin no-least example

The first exact failure occurs at `k=25`:

`625 < n < 676`, `F_2(25)=25`.

Candidate witnesses:

`[2,3,5,7,11,13,17,19,23]`.

Forced core:

`[2,3,5,11,17,23]`.

The only residual composite is

`637 = 7^2 * 13`,

with residual edge `{7,13}`.

Hence the two inclusion-minimal safe bases are exactly:

- `{2,3,5,7,11,17,23}`;
- `{2,3,5,11,13,17,23}`.

There is no least safe basis under inclusion.

This does not contradict the global bounded root-factor theorem.  On the full interval `2..N`, every required prime witness `q` has the universal exclusive collision `q^2`.  Restricting the state domain to one basin can delete those forcing collisions and create genuine residual witness choices.

## 5. Extended scan corrects the first low-range pattern

The first scan through upper endpoint `500000` found 15 bad square basins; every residual happened to be a two-witness number with factor-exponent pattern `(2,1)`.  That was only a low-range regularity.

The exact scan was extended to

`(k+1)^p-1 <= 4004000`.

### First three-prime residual

At `k=888`:

`790079 = 73 * 79 * 137`,

with residual edge `{73,79,137}`.

So the early `a^2 b` pattern is false globally even inside the scanned square-basin regime.

### First basin with two residual edges

At `k=1781`, the residual edges are:

- `3172511 = 101^2 * 311` -> `{101,311}`;
- `3175339 = 101 * 149 * 211` -> `{101,149,211}`.

The inclusion-minimal residual transversals are exactly:

- `{101}`;
- `{149,311}`;
- `{211,311}`.

Thus `{101}` is the unique minimum-cardinality residual choice, but it is not contained in the other inclusion-minimal choices.  Therefore:

**unique minimum-cardinality safe basis does not imply a least safe basis under inclusion.**

## 6. Exact bounded atlas

Bound: upper endpoint at most `4004000`.

| power p | basins scanned | no-least basins |
|---:|---:|---:|
| 2 | 1999 | 35 |
| 3 | 156 | 0 |
| 4 | 42 | 0 |
| 5 | 18 | 0 |
| 6 | 10 | 0 |
| 7 | 6 | 0 |
| 8 | 4 | 0 |

The 35 square failures occur at:

`25,47,62,123,130,151,157,162,196,217,308,364,365,479,556,888,924,935,1008,1056,1078,1162,1290,1345,1454,1511,1541,1577,1612,1627,1679,1781,1790,1865,1897`.

Across them there are 36 residual composites.  Their distinct-prime exponent patterns are:

- `(2,1)`: 32;
- `(1,1,1)`: 4.

No no-least basin was found for powers `3..8` in this bound.  This is bounded evidence only, not a theorem that higher-power basins always have a least divisor-witness basis.

## 7. Lean candidate update

`EnterpriseMath/Prime/WitnessCover.lean` now also contains:

- `SameSignature`;
- `SignaturePrimalitySafe`;
- `coversComposites_signaturePrimalitySafe`;
- `signaturePrimalitySafe_iff_coversComposites`;
- `ResidualComposite`;
- `coversComposites_iff_forcedCore_and_residual`;
- `forcedBasis_covers_iff_noResidual`;
- `exists_least_cover_iff_noResidual`.

The earlier local definition-order error was corrected before this checkpoint: `ForcedBasis` is declared before `ResidualComposite`.

No root import is added.  This environment has no Lean/Lake compiler, therefore status remains exactly `LOCAL_LEAN_PENDING`, not `LEAN_CHECKED`.

## 8. Layering / ownership boundary

- A2/P023: signature/kernel sufficiency and prime-label preservation.
- A4: residual witness hypergraph is multivalued support/correspondence data; no automatic identification with existing radius-indexed relation support.
- P018/P023 action basis: remains canonical owner of its unique least power-free action theorem; R005-A only extracts the generic exclusive-collision mechanism.
- R005-B: retains p-power basin, factor horizon and carry ownership.  This checkpoint consumes those observables but does not copy or modify the R005-B module.

## 9. Foundation Feedback candidates

### FF-R005A-6 — forced witness / least basis criterion

`least cover exists <-> forced core covers <-> no residual false-state fiber`.

### FF-R005A-7 — prime-anchor boundary

`coverage -> signature primality safety` is unconditional under prime-soundness, but the reverse implication needs a known prime in the domain.

### FF-R005A-8 — domain restriction destroys least-basis transport

A global language may have a unique least basis because universal exclusive collisions exist; restriction to a narrow state domain can delete those collisions and replace the least basis by a forced core plus residual hitting-set problem.

Status for all three: `PROVED GENERIC STRUCTURE / PRIOR-ART NOVELTY UNVERIFIED / CANONICAL PROMOTION NOT YET`.
