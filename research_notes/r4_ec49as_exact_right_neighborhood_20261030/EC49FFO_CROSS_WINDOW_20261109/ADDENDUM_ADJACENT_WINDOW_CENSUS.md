# EC49FFO additional consecutive-window exact census

Date: 2026-11-09. Frozen scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; original ordered signed X6 BRC model from EC49FFJ. This is an exact *finite* integer extension of README_EC49FFO's eight-demand theorem.

For two adjacent observation windows Hh and H(h+1), each requiring four low signatures (1,2,4,8), and with an **unrestricted complete-key budget**, the author executed the same exhaustive candidate enumeration and 8-mask rooted-native-prefix-tree integer DP at the following three adjacent pairs:

| Window pair | Key configurations at each window | Eligible original low words | Trie nodes (including root) | Exact global native prefix optimum |
| --- | --- | --- | --- | --- |
| H4/H5 | 7 / 13 | 176 + 950 = 1,126 | 4,903 | **40** |
| H5/H6 | 13 / 22 | 950 + 4,932 = 5,882 | 24,955 | **44** |
| H6/H7 | 22 / 34 | 4,932 + 25,060 = 29,992 | 125,245 | **48** |

The finite key enumeration covers the entire admissible-key domain at the two windows in every row; no assumption about how many distinct keys the DP may select. DP witnesses were recovered as original full operation words, reexpanded into all signed X6 microstep prefixes, with their union cost checked separately.

**Exact conclusion for h=4,5,6**:
`min C_native(Hh all four low; H(h+1) all four low) = 4*h + 24`
even with unrestricted keys. Each value is achievable using **two keys**: take the EC49FFM single-window four-word (4h+16)-edge construction at Hh with key (4,h-2,1), append one native `g` to each word at H(h+1), now with key (4,h-1,1). It adds eight new signed native prefix edges. This proves equality with the computed global lower bound in the stated finite h interval.

**Reproduction:** the exact readback-verified source `VERIFY_EC49FFO.py` implements this eight-demand DP for (4,5). To reproduce the other rows with the same algorithm, replace the single `HORIZONS=(4,5)` assignment by `HORIZONS=(5,6)` or `HORIZONS=(6,7)`, and change/remove the three final sample-specific assertions on key counts, candidate counts and node count (those assertions protect the H4/H5 base case; all native and observer checks remain enabled). The original locally executed parameter substitutions and result JSON/logs are preserved in the attached turn evidence package. No floating-point optimization is involved.

**Open question:** prove or disprove the candidate unbounded consecutive-window identity `min C_native(Hh,H(h+1))=4h+24` for all integers h>=4 with unrestricted keys. Finite h<=6 supplies evidence, not an infinite-range proof. A structural proof may use the minimum number of new terminal edges relative to a four-low witness at the previous window. The mother project remains constrained by its actual frozen horizon/signature quotas and <=5-key/<=93-edge target.
