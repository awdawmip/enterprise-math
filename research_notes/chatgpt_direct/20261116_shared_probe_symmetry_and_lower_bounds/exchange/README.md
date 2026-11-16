# Replacing classes of the 8,723-read table

For an unordered partition into thirteen classes, the replacement distance is thirteen minus the number of unchanged complete classes. The specified 8,723-read witness is locally optimal through the radius in result.json. The cost threshold for a strict improvement is 8,722.

The replay reconstructs the complete bank of single classes and the 18 possible profiles below 8,723 from the preceding round's three-unit menu model. For each subset of labels to remove and each profile, subtract the contributions of the preserved labels. A negative residual multiplicity makes that choice impossible. The available replacements are the new classes contained in the union of the removed labels. All thirteen original classes are excluded as replacements. Thus a table at distance k enters exactly the branch given by its k genuinely changed classes.

The search branches on an uncovered history or a class type needed once, selecting the condition with the fewest compatible rows. It rejects missing coverage, insufficient candidate multiplicities, and impossible coordinate slice totals calculated using the minimum and maximum contribution for each remaining row type. Every branch satisfying the integer quotas is visited without a node cap. The Python driver also derives the expected set of admissible subproblem identifiers and verifies a complete one-for-one correspondence with the C++ results.

The second calculation compares the 8,723-read and 8,721-read witnesses. In all 12,000 affine alignments, at most one complete class agrees. The best alignment preserves exactly one, for replacement distance 12 between these specific affine orbits.

```sh
python3 replay.py --older /path/to/previous --group /path/to/group --table /path/to/asymmetric/groups.json
python3 overlap.py --group /path/to/group /path/to/asymmetric/groups.json /path/to/asymmetric8721/groups.json
```
