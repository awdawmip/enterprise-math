# A thirteen-label table with 8,723 native reads

The ordered rows in groups.json partition histories numbered 25x + 5y + z for x,y,z in {0,1,2,3,4}. Every row is a label in the three-unit common identity/doubling model. Seven nine-point rows cost 557 reads each, five ten-point rows cost 744 each, and the unique twelve-point row costs 1,104. Their total is 8,723 over the 31,250 equally weighted scenarios.

The original observation model independently reconstructs forbidden triples and class costs. The thirteen rows avoid every forbidden triple. Testing the full 12,000-element cost-preserving affine action on the unlabeled partition gives trivial stabilizer and 12,000 distinct affine images.

The replay then calls the original component program for the supplied codebook, covering all 31,250 inputs by composition of real per-service receipts and stratifying complete three-service executions from preparation by the public action, active set and read coordinate. The receipt and whole-path records are in result.json.

Run from this directory. Compare the standard output with result.json.

```sh
python3 -B replay.py --older /path/to/previous --group /path/to/group --original /path/to/original
```

The search fixed the unique twelve-point class, used its order-48 stabilizer to identify 28 possibilities for the row containing its center, and fixed one more row through a least-covered point. The saved table was found by exact cover with coordinate-slice pruning in first-anchor orbit 13, second-anchor case 41 (indexing from zero). Rechecking the short positive certificate only requires the given table.
