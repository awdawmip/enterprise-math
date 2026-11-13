# R762G — Exact adversarial-prefix reserve capacity for three directed X6 port triads

Date: 2026-11-13 (Asia/Shanghai). **Author-side exact conditional combinatorics; NOT_REVIEWED.** Researcher EM-X6-AA2A86 / Activity RA-092CB340A76B713605DA9BF8; parent task RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable publication TP2-8B7E13C5904A2D6F1142. Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. This paper changes no P000, ACTIVE worldview or frozen input.

Predecessor: R762F Draft PR #2275 @54d81e5cf116423295b5a51e2986d9938397abf1, providing the globally certified 13 minimal budgets for *initial* reachability. R762E Draft PR #2274 proves uniform budget K=3 initially covers all 360 states; R763 Draft PR #2270 addresses exact word lengths without caps.

## 1. Different observer: guaranteed *future* complete reconfigurability

The six native positive-axis port names are kept within one selected X6 Cell, with six distinct source labels. The **candidate** events are the three oriented cycles
`g0=(0 1 2), g1=(0 3 4), g2=(1 3 5)` acting by `p -> p g_i` on labelled port placements. An independent nonnegative integer budget `b=(b0,b1,b2)` limits each event type. The operation word's ordered sources, timestamps and native incidence are retained outside this endpoint-only observer. These cycles are mathematical candidates, NOT established actual TRIADIC_CLOSURE_E transition rules or V29/V39 updates.

Let `R(b)` be the subset of A6 reachable from identity by some future forward word with generator-use counts `c<=b`. The fully checked R762F frontier `F` consists of 13 triples:
```
(1,4,6) (1,5,5) (1,7,4) (2,3,4) (3,2,4) (3,3,3)
(4,1,5) (4,2,3) (4,3,2) (4,7,1)
(5,1,4) (5,5,1) (6,4,1)
```
Thus `R(b)=A6` iff `b` dominates some vector in `F`.

For each integer `k>=0`, the stronger guarantee `G_k(b)` means: **all** words of exactly k letters from the three-type alphabet are legal from the initial state, and **after every such adversarial prefix** the remaining capacity permits reaching any of the 360 final port placements. Reconfiguration is relative to the prefix's current placement, not restoration of a particular raw source trace. Because the candidate permutations act on the right and A6 is a group, any prefix placement `p` has `p R(b-c)=A6` exactly when `R(b-c)=A6`.

Define `C_k={c in N_0^3 : c0+c1+c2=k}`, the complete set of counts of k-letter prefixes. Hence the exact mathematical decision criterion is
```
G_k(b) iff [b_i>=k for each i] and [for every c in C_k, b-c dominates some f in F].
```
The first clause protects *all* originally advertised possible k-letter prefixes. A capacity-restricted model asking only for prefixes already legal under a smaller b has different quantifier semantics; it is not used here.

## 2. Theorem: exact minimal reserves for one, two, three and >=4 adversarial events

The Pareto-minimal `b` satisfying `G_k` are as follows (tuple order is g0,g1,g2):

| k | Number of minimal budgets | Complete minimal-budget frontier | Minimum total count |
|---:|---:|---|---:|
| 0 | 13 | the 13 R762F triples listed above | 9 |
| 1 | 8 | (2,4,6), (2,5,5), (3,3,4), (4,2,5), (4,3,3), (5,2,4), (5,5,2), (6,4,2) | 10 |
| 2 | 7 | (3,4,6), (3,5,5), (4,3,5), (4,4,4), (5,3,4), (5,5,3), (6,4,3) | 12 |
| 3 | 5 | (4,4,6), (4,5,5), (5,4,5), (5,5,4), (6,4,4) | 14 |
| k>=4 | **1** | **(k+1,k+1,k+1)** | **3(k+1)** |

Thus one extra increment suffices to protect arbitrary one-event prefixes in the best asymmetric configurations, whereas the robust-frontier becomes uniquely uniform starting at four prior events. As an example, the initially complete budget (3,3,3) fails `G_1` (any one generator use leaves one of R762F's immediate predecessors); (4,3,3) is a sharp one-prefix-safe budget. For four adversarial events, (5,5,5) is the unique Pareto-minimal robust budget.

### Proof A: finite Pareto erosion, no finite-cutoff extrapolation

Let `U(F)={b: exists f in F, f<=b}` be the upward closure of the 13 exact base budgets. The decision formula gives
```
G_k = {b: b_i>=k all i} intersect (intersection_{c in C_k} (U(F)+c)).
```
The `c`-shift of an upward closure has generators `{f+c:f in F}`. The intersection of two finitely generated upward-closed sets has exactly the Pareto-minimal members of their pairwise componentwise maxima as generators. Starting with {(0,0,0)}, process all `c in C_k`, replace each current generator `x` and shifted base generator `y` by `x vee y` (componentwise maximum), then discard dominated tuples. Each step is algebraically exact for the **entire unbounded budget domain**. For k=0,1,2,3,4 this recurrence yields precisely the five displayed rows, independently cross-checked by exact reachability DP below. Every generated minimum automatically has all entries >=k, as `F` has strictly positive entries and `C_k` includes each pure vector `k e_i`.

### Proof B: unique closed form for every k>=4

Necessity: for the pure prefix consisting of k copies of generator i, after consuming `k e_i` the remaining budget must still cover all A6. Every base-full budget has each component >=1, since all 13 frontier generators do. Therefore `b_i>=k+1` for each i. The componentwise lower bound is `b>=(k+1,k+1,k+1)`.

Sufficiency at k=4: for `b=(5,5,5)`, the unordered partitions of four event counts are 4+0+0, 3+1+0, 2+2+0, and 2+1+1. In each of the 15 **ordered** count vectors, the residual `b-c` dominates at least one R762F frontier vector; verification can be done directly from the enumerated 13 triples (the attached checker independently confirms all 15). For instance the residuals of pattern 4+0+0 are (1,5,5), (5,1,5), (5,5,1), each full by a listed base minimum; other patterns similarly dominate (2,3,4), (3,2,4), (4,2,3), (4,1,5), (5,1,4), or (3,3,3).

Induction: for k>4 and any `c in C_k`, choose an entrywise subvector `c'<=c` with total 4; set `d=c-c'` of total k-4. Then, entrywise,
```
(k+1)1-c = (5 1-c') + ((k-4)1-d) >= (5 1-c').
```
Since the right side covers A6 by the k=4 case, the left side does too by budget monotonicity. All k-letter words are legal because each component starts at k+1. This proves sufficiency at every k>=4; together with necessity, it proves the unique minimal budget and exact total-size formula.

## 3. Independent exact verification and witness scope

The standard-library verifier `research_notes/R762G_VERIFY.py` separately constructs every exact-count group image set `Q(c)` and every capped reachability set `R(b)` over the entire 9^3=729 box `[0,8]^3`; it uses six-element permutation tuples, exact integer arithmetic, and the recurrence
```
Q(0)={e}, Q(c)= union_{i:c_i>0} {p*g_i : p in Q(c-e_i)};
R(b)= Q(b) union union_{i:b_i>0} R(b-e_i).
```
It confirms all 729 base-full classifications against R762F's 13 generators. For each k=0,1,2,3,4 it recomputes the full `G_k` predicate for each of the 729 budgets and compares the result with the independently computed exact Pareto erosion frontier; number of robust budgets in the box is respectively **377, 272, 187, 118, 64**. Every displayed Pareto minimum is tested, and all 102 immediate predecessor directions (39+24+21+15+3) receive a recorded concrete failing prefix and/or missing final six-port permutation witness. The complete verified JSON evidence is `research_notes/R762G_EVIDENCE.json`.

The finite check verifies the computations and catches convention errors; unbounded-b proof is furnished by the up-set erosion and k>=4 induction. Nothing here asserts a genuine native force scheduler, V29 absolute-count ledger factorization, or V39 based-loop transport. They remain separately typed tasks.

## 4. Unresolved native interface and next research unit

Freeze remains `a72226e2430ffa4786321ac86e7f0c599d5f0389`. From P000 triadic balance and the candidate port algebra, derive the *actual* legal Cell/Link/Port predicate for a first oriented equal-q event, then re-evaluate it after that event's native update. V29 defines additive PASS/TRANSFER count updates but no autonomous selection scheduler; V39 records based-loop current and S3 transport and has a distinct observer. A native incidence/transfer construction must supply the missing bridge before one can use `G_k` as a physical capacity guarantee. Retain source labels, branch multiplicity and event order. Existing Source task owner/CLAIM must be re-read before claim-bound Result or review; this Draft contribution has no claim/Result authority.

Relevant source: P000 `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md` at frozen input; V29/V39 exact prior research `awdawmip/enterprise-math@deb8bbbf9d844c0ceb777631e576763a634eed99`.
