# Twelve labels with an affine symmetry of order six or twelve

The minimum under an order-six affine symmetry is **10,224 reads**, attained by the twelve rows in groups.json. No admissible twelve-label partition has an order-twelve affine symmetry at any price. These statements use the full order-12,000 affine cost-preserving group of the three-unit common identity/doubling model and concern unordered labels.

For either order m, an affine transformation has a fixed point. In characteristic five, average the orbit of any point by multiplying its sum by the reciprocal of m. Translation by that fixed point conjugates the transformation to its linear part. An explicit calculation in the 96-element linear group finds exactly four cyclic subgroups of each order and shows that they are conjugate for each specified order. It suffices to fix one subgroup and any of its generators.

For order six, the orbits on histories have lengths 1, 2, 2 and twenty copies of 6. For order twelve, they have lengths 1, 4 and ten copies of 12. The label containing the origin is fixed. Thus the remaining label orbits in a twelve-label partition have lengths in {1,2,3,6} or {1,2,3,4,6}, respectively. At most one has length six.

Suppose a class C has orbit length r. Its translates are disjoint, so every history orbit O which meets C is split into r phase classes. In any ordering along the generator cycle, C intersects O in exactly one residue class modulo r. Conversely, choosing one such phase from each selected history orbit gives a valid r-class orbit whenever C contains no forbidden triple. The image cost is r times the read count of C. Rotating C fixes its phase on the first selected history orbit, eliminating r duplicate phase choices.

For r below six the verifier generates all possible supports with their minimum costs. Distinct classes with equal support and r are interchangeable with respect to the uncovered histories and remaining label quota. It first checks covers using only these shorter orbits. For covers containing a six-class orbit it fixes the class orbit through the origin, assembles all remaining shorter orbits and retains the cheapest partial cover of each resulting complement. It enumerates the remaining phase selections directly. Cost pruning uses only the independently proved minima for individual class sizes. The order-twelve cap 31,250 equals the total number of input scenarios. The order-six cap 10,224 is the cost of the supplied witness.

For a fixed order-six subgroup, four unlabeled partitions attain the minimum. The verifier tracks the number of minimizing choices per support and sums them over feasible completions. The full group has order 12,000, the subgroup normalizer has order 24, and the witness stabilizer is precisely the six-element subgroup. Consequently its four normalizer images account for all four fixed-subgroup optimizers. All the order-six symmetric optima form a single affine orbit of 2,000 unlabeled partitions across 500 conjugate affine subgroups.

The replay independently constructs the forbidden triples and pair menus, recomputes the full orbit searches, checks the saved groups as a complete partition and verifies the 31,250-scenario result using original per-service program receipts plus stratified runs of whole three-unit paths.

```sh
python3 -B replay.py --older /path/to/round2/delivery --group /path/to/round3/group --original /path/to/original
```
