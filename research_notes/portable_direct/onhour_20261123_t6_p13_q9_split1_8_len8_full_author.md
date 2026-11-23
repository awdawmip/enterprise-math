# T6 p13 vertical q-order 9, signed split (1,8): full negative length-eight exclusion

Date: 2026-11-23, author exact finite calculation. Frozen scientific task: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca:research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md`. Evidence strength: `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`.

## Exact statement and domain

Assume both exponent-shape masses at most 2331 and equality of the original H_0,...,H_6. Reuse the prior higher-13-valuation cancellation and saturated 12-dimensional q0 congruence lattice (index 13^21), without altering the full composite denominators. For maximal prime 13, 13-valuation one, signed vertical q-order split (1,8), the positive vertical side contains one named atom (1,r), 1<=r<=12, and the negative vertical side has eight atoms of q=1, with multiset residues r in 1..12. Each actual denominator is 13(13+r), with exponent mass 168+13r. There is **no admissible original-budget collision** in this complete length-eight case.

## Complete search and proof of coverage

There are C(19,8)=75,582 canonical eight-residue multisets, each paired with 12 named positive residues, hence 906,984 raw signed pairs. The 381,888 pairs containing the same vertical name on both sides are canceled into the already excluded lower q-order7 case. For the disjoint pairs, negative vertical mass is 1344+13*sum(r), so a mass greater than 2331 is impossible; precisely 15,299 disjoint pairs are excluded this way. This leaves **509,797** exact disjoint budget-eligible signed pairs.

Every remaining pair obeys the original six necessary mixed congruences
```
sum_(r=1..12) u_r*r^(-j) + (13+r_positive)^(-j)
    -sum_(r in eight-negative-multiset) (13+r)^(-j) = 0 (mod 13^j),
j=1,...,6.
```
The pre-existing saturated q0 lattice, exact rational Gram–Schmidt basis and exact particular residue lift are reused. For each signed pair, the weighted q0 vector necessarily lies in a sphere of squared radius R^2=(2331-c_plus)^2+(2331-c_minus)^2, where c_plus=168+13*r_positive and c_minus=1344+13*sum(r_negative). In this domain R^2 <= 5,402,189. The previously computed exact smallest GS diagonal-square is

```
78577530278042129705264382752517501995032553011464356025
----------------------------------------------------------------
4243983974238642688103181306691645151538473248349
```

which exceeds 18,515,039 and therefore strictly dominates all necessary radii. At every coordinate there can be at most two nearest integer choices. The exhaustive exact rational GS tree, with no float comparisons, visited **1,226,211 recursion nodes and zero full sphere leaves**. Thus no q0 integral correction can satisfy the necessary sphere and all six congruences in any of the 509,797 pairs. This proves the stated exclusion without assuming the absence of 13-free lower-prime denominators.

Reproducibility: `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN8_AUTHOR_EXACT_REPLAY_20261123_1026.py` reads the prior committed exact q0 source and accepts --start/--end half-open canonical roster index ranges; it returns each segment's exact counts and residue-roster SHA256. The full author execution used a local GMP-rational C++17 implementation of the same search and a separately computed Python combinatorial count/digest. A Python Fraction independent arithmetic spot check covered 40 disjoint pairs, 97 GS nodes, and zero leaves. The newly published full Python checker has not been run after publication.

Full canonical-roster SHA256: `683a103772eda5ef86981dda7e0f8d3bf319f8e9a92b5b7419ae9ef446800f73`. The exact certificate is `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN8_AUTHOR_EXACT_CERT_20261123_1026.json`.

## Boundary and next frontier

This completes the final still-open negative-length case of signed p13 q-order9 split (1,8). Previous negative lengths1..7 and split (0,9) are preserved as independent earlier author results, not rerun. The next smallest research scope is signed p13 q-order9 split (2,7), first the positive one-atom q2 side against the smallest still-open negative q7 subfamilies, respecting both mass caps. Then splits (3,6) and (4,5), lower-prime completion and full T6 threshold remain open. Formal Native T6 Source's p17 q14 (7,7) roster-cost preflight and its ownership/review remain separate. No Native CLAIM, PROGRESS, Result or independent review is asserted.
