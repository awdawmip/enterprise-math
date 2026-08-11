# Contextual Local-Law Reflection and Modular-Only Decoding

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

The bounded-local-law theorem has three useful precision levels. A global finite alphabet gives a clean class-wide guarantee, while the exact split-content spectrum gives a sharp one-world answer after following the realized refinement trajectory. Between them lies an important semantic layer: **contextual codebooks**.

A residue collision is harmless when the two exact values occur in semantic coordinates that the future language already distinguishes. Precision therefore needs injectivity only inside values that can actually compete for the **same coordinate**.

## 1. Weighted signature coordinates already carry side information

For a finite integer-weighted relation family and initial observation `O`, every later partition refines the initial observation.

A local weighted transition coefficient is therefore tagged by at least:

`(action, source initial-observation class, target initial-observation class)`.

Call such a triple a semantic coordinate c.

For one coordinate c, collect every exact target-block aggregate that can arise when the target block is further refined inside its initial observation class. This gives a finite admissible codebook

`L_c subset Z`.

## 2. Contextual reflection theorem

Let `rho_M(z)=z mod M`.

If `rho_M` is injective on every `L_c` separately, then the complete mod-M weighted refinement sequence equals the exact integer refinement sequence.

### Proof idea

At any later partition P:

- a source block lies inside one initial source-observation class;
- a target block lies inside one initial target-observation class;
- therefore the exact coefficient in a fixed action/source-block/target-block coordinate belongs to one fixed codebook `L_c`.

If two states in the same current source block have equal modular signature vectors, coordinatewise injectivity inside `L_c` forces equality of their exact signature vectors. Hence one modular refinement step equals one exact step. Induction gives equality through stability.

## 3. Cross-coordinate collisions are harmless

A global alphabet can demand unnecessary numeric precision.

Example:

- action a uses admissible local values `{0,1}`;
- action b uses `{0,4}`.

Modulo3, exact values1 and4 collide globally. But they occur under different action labels, so the signatures never compare them as alternatives for one slot.

mod3 is injective on each action codebook separately and reproduces the exact weighted refinement.

The same phenomenon occurs when values are separated by source-observation or target-observation context.

## 4. Context is part of precision, not metadata after the fact

The correct decoding question is not

`does residue r identify one global integer?`

but

`does (semantic coordinate c, residue r) identify one admissible integer in L_c?`

This is finite decoding with side information.

It is another concrete reason that task-relative precision cannot be summarized by one raw modulus or one global value alphabet.

## 5. Three nested precision guarantees

### Class-uniform primitive sumset

Given primitive set P and at most d local contributions, require injectivity on the universal bounded sumset `S_d(P)`.

This guarantees exact reflection for every world in that class.

### Fixed-world contextual codebooks

Use the actual action and initial observation structure to split the admissible alphabet into contextual codebooks `L_c`.

Injectivity is required only inside each `L_c`. This can strictly lower the guaranteed modulus while remaining static and pre-execution.

### Realized split-content spectrum

Follow the exact refinement trajectory and keep only strict state-split differences that actually occur.

The existing split-content theorem gives the exact bad-modulus set for that one world.

Thus:

`universal class precision >= contextual guaranteed precision >= realized one-world precision`

in strength of assumptions / conservatism, not necessarily as a single numeric chain in every representation family.

## 6. Modular-only decoder removes a verification circularity

A genuine reflection compiler must not recover exact quotient weights by first consulting those same exact weights.

The contextual decoder therefore accepts only:

- exact state/edge incidence structure;
- primitive edge weights as canonical mod-M residues;
- a quotient partition refining the observation;
- semantic context labels;
- the finite exact admissible codebook `L_c` for every coordinate.

It does **not** inspect exact primitive integer weights.

For each action/source quotient block/target quotient block it:

1. sums primitive residues modulo M;
2. verifies that all source representatives have the same modular block-weight vector;
3. resolves the coordinate c;
4. uniquely decodes the residue inside `L_c`.

The decoded integer vectors form the exact weighted quotient matrices.

## 7. Sharp modular-only witness

Take one action with two source states in the same source observation class:

- x sends weight1 into target observation class T1;
- y sends weight4 into different target observation class T2.

Modulo3 both primitive weights are stored as residue1.

The decoder receives no exact primitive weight. It nevertheless recovers:

-1? No: in the T1 coordinate residue1 has admissible lift1;
- in the T2 coordinate the same residue1 has admissible lift4.

Thus one residue acquires different exact meanings from explicit semantic side information without ambiguity.

## 8. Reflect before compose remains unchanged

Contextual decoding only lowers the precision required to recover the local exact machine.

After recovery, future composition proceeds in the exact integer algebra and may generate values much larger than M.

If one instead stays inside `Z/MZ`, those derived values can still collide. Contextual local reflection does not turn the finite quotient into a globally exact execution algebra.

## 9. Structural scope boundary

The decoder assumes edge incidence / primitive contribution identity is retained as a separate structural channel. Only the integer primitive weights are quotient-coded.

If coefficient collapse also erases edge/support/witness structure, a separate support/RELATION reflection theorem is required. Coefficient exactness cannot reconstruct structure that was never retained.

## 10. Arithmetic interpretation

For one finite codebook S,

`mod M is injective on S`

iff M divides none of the nonzero differences `u-v`, `u!=v` in S.

With several contextual codebooks, only **within-context** difference spectra matter. Cross-context differences disappear from the bad-modulus condition.

This gives the next arithmetic frontier: design the smallest modulus or CRT family that avoids the contextual difference-divisor spectrum rather than paying for one global interval width.

## Owner-local assets

- `src/enterprise_math/contextual_local_law_decoder.py`;
- `tests/test_contextual_local_law_decoder.py`;
- this bilingual companion note.

The parent bounded-local-law generation owns the generic class-uniform and realized split-content theorems.

## Prior art / status

Finite-alphabet decoding with side information, modular residue coding and context-dependent codebooks are standard prior concepts. P023/A2 retains generic precision/future-signature ownership. This note owns only the Enterprise Math contextual-reflection routing and modular-only decoder specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.
