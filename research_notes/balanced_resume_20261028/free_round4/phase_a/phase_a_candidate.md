# Phase A raw candidate: finite native-neighbour support

Candidate: `CAND-FREE-R4-FINITE-NEIGHBOR-SUPPORT-20261028-870C7C4C`

Researcher: `EM-FREE-870C7C4C`. Mode: `FREE_AXIOM_DISCOVERY`.

This is a raw mathematical candidate, not Working Truth, Foundation, task authority, or a novelty claim. The mandatory substrate disclosed existing downstream material; therefore the discovery status is `ANCHOR_EXPOSED`, not clean independent discovery. The question itself was selected without opening current results, historical work, task menus, tool inventories, or another researcher's question.

## Question and primitive assumptions

The ambient space is Heartbeat World's native six-dimensional Cell torsor over signed `Z^6`. Choose a Cell anchor solely to write six-field raw signed coordinates. No globally distinguished origin or native plane is introduced. Primitive coordinate neighbours differ by exactly one of `+e_i,-e_i`, for `1 <= i <= 6`.

Let `S` be a finite nonempty set of native Cells. Its induced internal coordinate degree is

`d_S(x) = |{(i,epsilon): 1 <= i <= 6, epsilon in {-1,+1}, x+epsilon*e_i in S}|`.

All six axes and both signs participate. Distinct direction pairs give distinct neighbouring Cells. Assume an integer `k >= 0` and the static condition `d_S(x) >= k` for every `x in S`. Call this the declared neighbour-support condition; it is not a force-stability predicate. It contains no force quanta, time evolution, probability, amplitude, branch weighting, or mechanism of actual persistence.

The question is the minimum possible `|S|`, and the structure when the minimum is attained. This is a static spatial question, so no time variable is needed. Coordinates and formulas below are proof coordinates/displacements, not public Cell addresses.

## Candidate theorem

1. A finite nonempty `S` satisfying the condition exists if and only if `0 <= k <= 6`.
2. Whenever it exists, `|S| >= 2^k`.
3. Equality holds if and only if, for a native Cell `a` and a set `I` of exactly `k` distinct native axis indices,

   `S = {a + sum_{i in I} epsilon_i*e_i : epsilon_i in {0,1}}`.

Thus the minimum for `k=6` is exactly 64 Cells, and the only minimizers are translations of the full six-axis unit box. For `k=0` the minimum is one Cell. The formulas with fewer active axes describe a restricted finite set inside the same native X6 world; omitted raw coordinates are fixed, not deleted or inferred from an observer. A sign reversal gives another representation of the same class after changing `a`.

## Proof of the obstruction for k >= 7

In any chosen raw signed chart, select `x in S` maximizing the integer scalar `L(x)=x_1+...+x_6`; this is possible because `S` is finite and nonempty. For each axis `i`, the neighbour `x+e_i` cannot lie in `S`, since its `L` value is larger. At most the six neighbours `x-e_i` remain. Hence `d_S(x) <= 6`. The hypothesis is impossible for `k >= 7`.

The auxiliary scalar is only a finite-set extremal witness. The proof retains the full six-component Cell state and tests every native neighbour; it does not claim that `L` is a sufficient state or a safe quotient.

## Proof of the lower bound and equality classification

We prove simultaneously, by induction on nonnegative `k`, the lower bound and the equality classification for finite subsets of the fixed X6 coordinate graph whenever the degree hypothesis holds.

For `k=0`, nonemptiness gives `|S| >= 1`; equality means a singleton, which is the formula with `I` empty.

Assume the statement established for `k-1`, and suppose `k >= 1`. The degree condition forces at least two Cells. Therefore some raw coordinate `j` takes at least two values on `S`. Choose an integer `t` with nonempty sets

`A={x in S:x_j <= t}` and `B={x in S:x_j >= t+1}`.

These form a disjoint partition of `S`. An `A` vertex has at most one primitive coordinate neighbour in `B`, namely `x+e_j`, and a `B` vertex has at most one in `A`, namely `x-e_j`. Other axis steps do not cross the cut. Thus every vertex of each part has degree at least `k-1` within that part. Induction gives

`|A| >= 2^(k-1)` and `|B| >= 2^(k-1)`, hence `|S| >= 2^k`.

Now assume equality. Both parts have exactly `2^(k-1)` Cells, so induction makes each part a translated unit box using `k-1` distinct native axes. Every vertex in such a box has exactly `k-1` internal neighbours. To satisfy degree at least `k` in `S`, every vertex of both parts must have its one possible cross-cut neighbour.

Consequently every `A` vertex has `j` coordinate exactly `t` and every `B` vertex has coordinate exactly `t+1`; otherwise it could not cross by a unit step. Moreover `B=A+e_j`, since every `A` vertex has that neighbour and the two sets have equal cardinality. Axis `j` is not one of the `k-1` varying axes of `A`, because its coordinate is constant there. Therefore `S=A union (A+e_j)` is precisely a translated unit box using `k` distinct native axes. This proves the necessity of the equality form.

Conversely, in any displayed `k`-axis unit box, each Cell has exactly one internal neighbour along each selected axis and none along unselected axes. Its degree is `k` and its cardinality is `2^k`. Such boxes exist for every `0 <= k <= 6`, proving sufficiency and completing all claims.

## Scope, losslessness, and obvious falsifiers

The finite/nonempty hypotheses, unit signed-axis adjacency, induced degree, and a uniform integer threshold at every Cell are essential. Infinite sets are outside scope: the full native lattice has degree 12. The assertion does not apply to average degree in place of minimum degree, extra channel adjacency, multi-occupancy, force balance, weighted support, or dynamically generated states.

No observation quotient is taken. A/B are exact disjoint subsets retaining complete raw coordinates and all edge tests; they form a proof partition, not a replacement state. The scalar witness is used only to identify a maximizer. The allowed mathematical observations are full set identity, cardinality, and primitive adjacency; there are no future dynamics. The argument commutes with a change of Cell anchor. It does not derive a native angle or a new rotation law.

An explicit finite set of fewer than `2^k` Cells with every degree at least `k`, a non-box equality example, or a finite set with every degree at least 7 would falsify the corresponding claim. The proof states exactly where each would contradict the cut or extremal argument. No computational enumeration is claimed as evidence in Phase A.

## Immediate consequences and disposition boundary

The exact finite support thresholds are `(k,min size)=(0,1),(1,2),(2,4),(3,8),(4,16),(5,32),(6,64)`; thresholds 7 through 12 admit no finite nonempty support set.

The candidate is proved from primitive coordinate adjacency, elementary induction, and finiteness; it does not need an additional axiom. This is the author's provisional derived-theorem classification, pending Phase B comparison and independent review. The proof may reproduce known combinatorics. Neither the local wording nor an X6 application establishes a new method or a new theorem in the external literature.

The finite delegation should close if post-freeze lookup confirms coverage or prior equivalence; duplicate discovery is a legitimate terminal result. The global balanced research objective remains OPEN.
