# Order-four restrictions for twelve-label tables

The archive checks the absence of a twelve-label table of total price at most 10,130 under each listed order-four symmetry. The generators are specified by the encoded images of the three coordinate basis vectors in result.json. Their linear conjugates and affine translates have the same bound, since order four is invertible modulo five and every affine order-four element has a fixed point.

A message class in a symmetric partition is in an orbit of one, two, or four classes. For one or two classes, the program exhaustively generates seed rows as unions of residue classes of the point cycles and checks every added triple against the original one-read model. For each orbit length and support, it retains a minimum-cost orbit; replacement on the same support preserves coverage and label count.

For four-class orbits, a seed of size s and price c must satisfy 4c + L(125-4s,8) ≤ 10130. Here L is the unrestricted additive relaxation from the single-class size minima. Only sizes 8 through 13 can meet this necessary condition, and the respective ceilings are 461, 641, 824, 1008, 1188, 1371. An exhaustive native enumeration of row seeds with cutoffs at least these values, expanded under the cost-preserving group, gives 46,696 translation representatives. The last cutoff is raised explicitly in replay.py before compilation. Generating all 125 translates and retaining those whose orbit rows are disjoint builds a complete candidate bank, in which redundant higher-cost choices are discarded.

The final search works on the history orbits as exact-cover atoms. It tries every compatible candidate through a least-covered atom, rejecting when no candidate can cover an atom or the remaining budget is below the sum of individual class-size minima. The replay checks that every archived search ended strictly below its node cap.

```sh
python3 -B replay.py --older /path/to/round2/delivery --group /path/to/round3/group --previous /path/to/round3/delivery
```
