# T6 p13 q10 split(1,9): negative length-four finite exhaustive exclusion

Date: 2026-11-23; frozen science: `enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`. Mode: portable TASK_RESEARCH author mathematics. This result is not a Native Result or Driver review.

## The precise proposition

Fix maximal prime p=13, p-adic valuation 1, original H0..H6 equality, integer named denominators `13(13q+r)` with q>=1 and 1<=r<=12, and positive and negative original side-mass cap 2331. For vertical total order 10 and signed split (1,9), with the positive side consisting of exactly one q=1 atom and the negative side exactly four atoms, there is **no** distinct-support configuration satisfying the six necessary mixed congruences and both original side budgets, even allowing the exact signed q0 compensation lattice.

## Exact calculation

The six negative q-partitions of 9 into four parts are (1,1,1,6), (1,1,2,5), (1,1,3,4), (1,2,2,4), (1,2,3,3), (2,2,2,3). The negative residues for equal q are nondecreasing; the positive q1 residue ranges over 1..12. These six mutually disjoint ordered q-pattern families contain exactly 53,664 negative rosters and 643,968 original pairs.

A named vertical atom present on both sides is canceled and charged to already saved lower-order scope (75,168 pairs); on the 568,800 remaining pairs the exact 12-dimensional lattice affine coset and Gram–Schmidt test was executed. The lattice has index `13^21`; each search uses the *original* positive and negative side cost `169q+13r-1`, weights `13r-1` for signed q0 compensation, and radius `(2331-cp)^2+(2331-cn)^2`. The smallest exact GS diagonal square exceeds `2(2331)^2`; thus checking `floor(-center)` and its successor at each descending coordinate exhausts every integer within the exact sphere. All four sphere leaves were checked modulo `13^j`, j=1,...,6 and against actual original side masses. None respects the cap.

| Negative q pattern | Raw pairs | Common cancel | GS searches | GS nodes | Sphere leaves | Budget-valid |
|---|---:|---:|---:|---:|---:|---:|
|1116|52,416|11,232|41,184|100,135|1|0|
|1125|134,784|20,736|114,048|279,090|0|0|
|1134|134,784|20,736|114,048|278,573|0|0|
|1224|134,784|11,232|123,552|300,940|2|0|
|1233|134,784|11,232|123,552|301,289|0|0|
|2223|52,416|0|52,416|127,824|1|0|
|**Total**|**643,968**|**75,168**|**568,800**|**1,387,851**|**4**|**0**|

The four residual sphere leaves have original masses `(4424,2964)`, `(2822,4609)`, `(3843,4399)` and `(3113,4350)`. Complete signed q0 vectors, named atoms, canonical roster indices, residues, per-pattern SHA256 pair digests and the exact rational minimum are in [the immutable author certificate](../../research_checks/T6_P13_Q10_SPLIT1_9_NEG_LEN4_AUTHOR_EXACT_CERT_20261123_1402.json). The detailed local combined JSON was additionally checked by a separate exact modular/mass re-evaluation, SHA256 `3be99b6f5c219c76e7491f41fdb21b2eaa9ff09b791be76f1a45b438805819ed`.

Computational method: the prior published exact replay `research_checks/T6_P13_Q10_SPLIT1_9_NEG_LEN1TO3_AUTHOR_EXACT_REPLAY_20261123.py` was reused at its algorithmic interface `particular`, `all_rosters`, `pair_search`, with the negative q partitions changed to these six length-four patterns and source-order diagnostic recording added. Two disjoint batches of three complete patterns were executed locally (not an independently reviewed replay), then combined and cross-checked.

## Relation to the mother objective and next frontier

Combine this exact author result with the previously verified signed split(1,9) negative lengths 1..3: 107,328 raw pairs, 6,264 common cancellations, 101,064 GS evaluations, 250,366 nodes, one sphere leaf, no mass-valid candidates. Consequently, **negative lengths 1..4** account for 751,296 raw pairs; all are excluded at author-evidence strength. The next smallest unfinished slice is signed split(1,9) negative length five, beginning with q-partition (1,1,1,1,5) containing 16,380 negative rosters, 196,560 raw signed pairs. Other length-five patterns together total 186,576 negative rosters/2,238,912 raw signed pairs. Other q10 splits, higher p13 order, lower prime/H0 completion and the T6 global objective remain open.

Preserve Source separate: the canonical Native T6 p17 q14 split(7,7) preflight has another provenance and requires an own real winning CLAIM. The Source continuation read `onhour-20261123-1403-t6-exact-current-cont-ro-v1` was QUEUED/CURRENT_CONTROL_FOLLOW_RETRY at last observation. No current own Native CLAIM, protected PROGRESS or Result is asserted. Research Activity328 historical attribution remains unresolved. This portable result belongs to the source author calculation, not an independent Driver review.

Scientific status: **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.
