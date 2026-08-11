# Constrained Modular Sensor Design Contains Minimum Set Cover

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

For a finite local-law codebook, unrestricted arithmetic design is easy: choose one prime larger than every relevant difference. Combinatorial hardness appears only after the **available sensor catalogue and its costs are constrained**.

This note gives an exact polynomial-size reduction from Set Cover to prime-only modular sensor selection, already using only two-point contextual codebooks.

## 1. Set Cover instance

Let

`U={i}`

be a finite universe and let candidate sets be

`S_1,...,S_k subseteq U`.

Assign a distinct prime `p_j` to candidate sensor j.

For every universe element i define one contextual codebook

`L_i={0,d_i}`

with

`d_i = product_(j : i notin S_j) p_j`.

If every candidate set contains i, the empty product gives `d_i=1`.

## 2. One prime sensor encodes one cover incidence

Sensor `p_j` reflects context i exactly when

`p_j does not divide d_i`.

By construction this holds iff

`i in S_j`.

So the prime-divisibility incidence matrix of the codebooks is exactly the original Set Cover incidence matrix, with “sensor separates context” playing the role of “set covers element”.

## 3. Sensor family exactness iff set family covers

Choose a sensor subset J.

The joint modular code reflects context i iff at least one selected prime distinguishes0 from `d_i`:

`exists j in J : p_j does not divide d_i`.

By the incidence theorem this is equivalent to

`exists j in J : i in S_j`.

Therefore

`selected modular sensors reflect every contextual codebook`

iff

`selected candidate sets cover U`.

This equivalence holds for every subset J, not only optimal solutions.

## 4. Minimum-cardinality identity

The feasible subsets on the two sides are literally the same family under sensor-name identification. Hence

`minimum number of allowed prime sensors`

is exactly

`minimum set-cover cardinality`.

The executable owner checks the equivalence for every subset of every 3-element / 3-sensor incidence instance: 512 incidence matrices × 8 sensor subsets.

## 5. Infeasibility is preserved

If one universe element belongs to no candidate set, then its difference is the product of **all** allowed sensor primes.

Every allowed prime divides that difference, so no allowed sensor subset reflects the context.

Thus Set Cover infeasibility maps exactly to constrained precision infeasibility.

## 6. Polynomial-size reduction

The j-th prime has polynomial bit length in k, and every `d_i` is a product of at most k such primes. Therefore the binary length of the encoded codebooks is polynomial in the Set Cover instance size.

The reduction is therefore a genuine polynomial-size complexity reduction, not an exponential integer-encoding trick.

Consequently minimum constrained modular-sensor selection contains Minimum Set Cover, even when:

- every allowed sensor is a prime modulus;
- every contextual codebook contains only two exact integers;
- there is no transition/future-dynamics complexity at all.

The hardness belongs to **precision-resource selection**.

## 7. Weighted sensor costs

Give each candidate sensor an arbitrary nonnegative cost `c_j` and copy the same cost to the corresponding Set Cover candidate.

Because feasible subsets are identical, minimizing total sensor cost is exactly weighted Set Cover.

So heterogeneous sensor prices, energy costs, latency costs or allocated storage costs inherit the weighted covering problem directly.

## 8. Why unrestricted modulus design is not hard for this reason

Do not overgeneralize the reduction.

If arbitrary moduli are available with no catalogue restriction and cost is simply “find some exact modulus”, one can always choose a sufficiently large prime. That problem does not contain the Set Cover choice structure above.

The combinatorial boundary appears when the world says:

- only these sensors/channels are physically or architecturally available; or
- different sensors carry distinct fixed costs/capabilities; or
- one must select a subset from a declared precision basis.

Thus the complexity source is constrained capability selection, not modular arithmetic itself.

## 9. Prime channels and one fused composite channel carry the same arithmetic information

For a selected prime set J, the joint residue tuple is equivalent to one modulus

`L_J=product_(j in J) p_j`

because the primes are distinct.

So the same exact arithmetic code can be deployed in two forms:

### Parallel sensor representation

Keep each prime modulus as its own channel.

Resources include:

- channel count `|J|`;
- parallel execution opportunity;
- synchronization / routing overhead;
- small per-channel arithmetic width.

### Fused scalar representation

Replace the selected channels by one composite modulus `L_J`.

Resources include:

- one channel;
- scalar bit width roughly `log_2 L_J`;
- no independent prime-channel scheduling.

Arithmetic exactness is unchanged.

## 10. Channel-count hardness can disappear under free fusion

If arbitrary composite moduli may be synthesized at unit channel cost, then after choosing enough prime factors one can fuse them into a single sensor. Counting **physical channels only** no longer represents the original Set Cover objective.

This does not invalidate the reduction. It shows that the objective function is part of the precision problem.

The Set Cover theorem applies to the declared prime-sensor catalogue / selection-cost model.

## 11. Bit-width cost survives fusion

For distinct primes,

`log L_J = sum_(j in J) log p_j`.

Therefore a fused composite modulus preserves an additive prime-factor storage-width cost.

If sensor cost is taken as `log p_j` (or another additive per-prime resource), optimizing the fused modulus still becomes a weighted covering problem over the selected prime factors.

Thus fusion trades channel count against scalar width; it does not erase every optimization cost.

## 12. Storage / parallelism Pareto

The same exact precision can therefore occupy multiple implementation points:

- many narrow channels, more parallelism;
- fewer fused channels, larger arithmetic words;
- one fully fused modulus, minimal channel count but maximal scalar width.

This is directly analogous to the project's earlier storage/execution-depth Pareto: an exact law does not determine a unique operational representation.

## 13. Relation to semantic capability joins

The reduction is arithmetic-only, but its structure mirrors the generic semantic-preorder theorem.

Each sensor contributes one subset of semantic distinctions. The declared task requires their union to cover all necessary contexts. Minimum precision-resource selection therefore need not be matroid-like or admit one canonical basis; arbitrary set-system structure is already realizable.

This is the coefficient-sensor counterpart of the earlier action-alphabet monotone universality / Set Cover boundary.

## Owner-local assets

- `src/enterprise_math/constrained_sensor_set_cover.py`;
- `tests/test_constrained_sensor_set_cover.py`;
- this bilingual theorem note.

## Prior art / status

Minimum Set Cover, weighted Set Cover, prime-factor encodings and CRT are standard prior mathematics/CS. P023/A2 retains precision/future-signature ownership. This Draft owns only the explicit constrained modular-sensor reduction and precision-resource interpretation.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
