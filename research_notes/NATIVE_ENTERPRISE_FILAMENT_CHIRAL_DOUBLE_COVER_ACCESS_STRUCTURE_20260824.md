# Native Enterprise filament codes: chiral double-cover access structure

Status: `FREE_RESEARCH_EXACT_ACCESS_STRUCTURE / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_GLOBAL_PRIME_ISLAND_AFFINE_MDS_CODE_SPECTRUM_3_TO_9_20260824.md`;
- `NATIVE_ENTERPRISE_GLOBAL_ISLAND_DUAL_MDS_TRIPLE_CHECKS_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_CHIRALITY_REVERSAL_AND_BOUNDARY_FLUX_20260824.md`.

## 1. Two affine sheets

For an island window of size

`k in {3,4,5,6,7,8,9}`

and an odd prime

`q>max(3,k-1)`, define

`epsilon_j=0` for even j and `epsilon_j=1` for odd j,

`eta_j^chi=(3*j^2+chi*epsilon_j)/2`,

with `chi in {+1,-1}`.

The two curvature-mode families are

`C_k,q^chi = eta^chi + {(a+b*j)_{j=0}^{k-1}: a,b in F_q}`.

Their union has `2*q^2` words.  The two sheets are disjoint for `k>=3`, but their low-coordinate projections overlap strongly.

## 2. Exact projection criterion

Let `S` be a subset of coordinate positions.

A plus-sheet word and a minus-sheet word agree on S exactly when there exists an affine function

`f(j)=A+B*j`

such that

`f(j)+epsilon_j=0`

for every `j in S`.

Because all positions `0,...,k-1` are distinct modulo q, this gives a complete classification.

### Unauthorized / ambiguous sets

Cross-sheet ambiguity exists when

1. `|S|<=2`; or
2. every position in S has the same parity.

For `|S|<=2`, an affine function interpolates the required parity values.

For a one-parity set, `epsilon_j` is constant and a constant affine function gives the ambiguity.

### Authorized / injective sets

The projection of the two-sheet union to S is injective exactly when

`|S|>=3`

and S contains at least one even and at least one odd position.

Indeed, such an S contains two positions of the same parity.  An affine function taking the same value at those two distinct positions must have zero slope; it then cannot take the opposite parity value at the third position.

Freeze:

`CHIRALITY + FULL WORD ARE RECOVERABLE FROM S`

`IFF |S|>=3 AND S MEETS BOTH PARITY CLASSES`.

## 3. Perfect two-probe hiding on the carrier

Choose `(chi,a,b)` uniformly from the `2*q^2` carrier states.

For every one- or two-coordinate observation, the conditional distribution of the observed residues is identical for `chi=+1` and `chi=-1`.

More generally, observing any number of positions from only one parity class gives exactly the same projected code image and the same uniform distribution under both chiralities; the constant sheet offset is absorbed by the free affine intercept a.

Thus the chirality bit is perfectly hidden from

- every pair of Cell residues;
- every all-even observation set;
- every all-odd observation set.

It is a relational bit between the two parity sublattices, not a value stored on either sublattice separately.

This is a carrier-level information statement.  Actual prime packets are not assumed uniformly distributed.

## 4. Explicit parity-bridge syndrome

Define

`Y_j=2*V_j-3*j^2`.

Then

`Y_j=A+B*j+chi*epsilon_j`.

Take two same-parity positions `u<v`, let their common parity be e, and take a third position w of the opposite parity.  Define

`Omega_(u,v;w)`

`=(v-u)*Y_w + (w-v)*Y_u - (w-u)*Y_v`.

The affine part cancels exactly, leaving

`Omega_(u,v;w)=chi*(v-u)*(-1)^e`.

Since `v-u` is invertible modulo q,

`chi=(-1)^e * Omega_(u,v;w)/(v-u)`.

Therefore any parity-mixed triple supplies a direct shell/location-independent chirality readout.

Once chi is known, any two observed coordinates recover the affine parameters `(a,b)` and therefore the complete packet.

## 5. Erasure hierarchy

For known chirality, the `[k,2,k-1]` affine MDS sheet recovers from any two surviving coordinates, so it tolerates `k-2` erasures.

When chirality is forgotten, exact recovery from a surviving set S follows the access criterion above.

Hence:

- many three-coordinate survivor patterns already recover the full packet;
- three same-parity survivors do not;
- worst-case guaranteed recovery requires more than `ceil(k/2)` surviving coordinates;
- equivalently the two-sheet union guarantees correction of `floor(k/2)-1` arbitrary erasures, matching its distance `floor(k/2)`.

For the sharp nine-Cell packet, any parity-mixed triple reconstructs all nine residues, while the five even positions alone still leave a two-sheet ambiguity.

## 6. Native interpretation

The alternating curvature mode behaves like one hidden C2 phase.

`ONE PARITY SUBLATTICE`

`-> MODE BLIND`,

`TWO RESIDUE PROBES`

`-> MODE BLIND`,

`PARITY-MIXED THIRD PROBE`

`-> EXACT MODE SYNDROME`,

`MODE + TWO VALUES`

`-> COMPLETE MDS RECONSTRUCTION`.

This is a non-Boolean multi-Cell readout: it uses relative prime values/residues across the two native parity layers, and it cannot be reconstructed from the prime/composite indicator of any individual Cell.

## 7. Boundary

Affine Reed-Solomon codes and access structures are classical.  The research-specific result is that the native alternating-curvature filament selects this exact two-sheet parity access structure before primality is tested.
