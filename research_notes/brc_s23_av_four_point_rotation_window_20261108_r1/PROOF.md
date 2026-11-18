# S23/AV: exact four-point rotation in the second key-inversion window

Date: 2026-11-08. Status: author-side proof with exact arithmetic certificate; independent review pending.

Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Prior theorem: PR #1777, `research_notes/brc_s23_av_disjoint_adjacent_swap_window_20261108_research1/PROOF.md` at `aaf8ea15f257ae5af8bb14421f9dc38008397caa`.
Object: exact ordering of threshold values for the two-point S23/AV auxiliary likelihood-sign observer retaining the joint (1,4) counts and label-3 padding.

## Theorem (sharp second-window correction)

Put
```
r=ln(7)/ln(10/7),  S_H={(v,j) in Z>=0^2 : v+j<=H},
theta(v,j)=r*v-j,
u=(79,431), w=(380295,2074774), M=|w|_1=2455069,
P=2074774, D=380295, K(v,j)=P*v-D*j,
L(v,j)=(K(v,j),-v) ordered lexicographically,
epsilon=79*r-431, eta=P-D*r,
q2=u+2w=(760669,4149979), H0=|q2|_1=4910648,
q3=u+3w=(1140964,6224753), H1=|q3|_1=7365717,
q4=u+4w=(1521259,8299527), H2=|q4|_1=9820786.
```
For **every integer** `H1<=H<=H2-1` (7,365,717 through 9,820,785), let `s=H-H0=M+t`, `t=H-H1`, so `0<=t<M`.

The complete increasing true-`theta` ordering of `S_H` is obtained from the old integer lexicographic ordering `L` by the following mutually disjoint local replacements:

* For each `y in S_t`, the **four consecutive lexicographic entries**
  `[y+w, y, y+q3, y+q2]` become the true-order entries
  `[y+q3, y+w, y+q2, y]`.
* For each `x in S_s\(S_t union (w+S_t))`, the lexicographically adjacent entries `[x,x+q2]` become `[x+q2,x]`.
* All other entries retain their lex positions.

Writing `T(k)=(k+1)(k+2)/2`, the exact counts are
```
four-point blocks   = T(t),
isolated pair swaps = T(s)-2*T(t),
inverted pairs      = T(s)+T(t).
```
Thus the *existing* floor-sum rank/select oracle for `L` can be corrected using a fixed number of integer triangle-membership tests, independent of the number of thresholds.

For each `p in S_H`, the exact rank difference `rank_true(p)-rank_L(p)` is `+2` for `p=y`, `+1` for `p=y+w`, `-2` for `p=y+q3`, `-1` for `p=y+q2` with `y in S_t`; otherwise `+1` for an isolated-swap start `p=x`, `-1` for its endpoint `p=x+q2`, and `0` elsewhere. Apply these cases in the displayed precedence.

The exact *select* correction at a lex index whose old point belongs to a four-block maps `y+w -> y+q3`, `y -> y+w`, `y+q3 -> y+q2`, `y+q2 -> y`. An isolated pair swaps endpoints. An untouched index returns its previous `select_L` value.

The range is sharp for this two-displacement correction: at `H=H2`, `q4` first becomes feasible and creates a new real-order inversion absent from the `q2,q3` inversion list.

## Proof

**1. Inversion classification.** The integer vectors `u,w` form a unimodular basis since `79P-431D=1`. A threshold displacement `d=A*u+B*w` has `K(d)=A` and `theta(d)=A*epsilon-B*eta`. The rigorously bounded logarithm ratio in `VERIFY.py` yields
```
0<eta<epsilon<2*eta, 2*epsilon>3*eta.
```
For `A=0`, the lex tie-break `-v` and `-B*eta` have the same sign. Reverse point order to reduce `A!=0` to `A>0`. For `B<=0`, or `B=1`, the real sign agrees with `A>0`. If `B>=2`, both displacement coordinates are nonnegative; to occur in `S_H` they must satisfy `510*A+M*B<=H<=510+4M-1`. Thus `B<=3`. With `B=2`, the real sign is negative only for `A=1`; with `B=3` it is negative only for `A=1`, since `2epsilon>3eta`. Consequently *every* inverted pair is exactly a `q2` translation starting at `x in S_s` or a `q3` translation starting at `y in S_t`, and all of these really are inversions.

**2. Fiber adjacency.** A fixed-`K` fiber is a sequence `p+k*w`; `L` sorts its feasible points by decreasing `v`. The `q2` endpoints have neighboring first keys differing by one, so a pair `[x,x+q2]` is adjacent in `L` unless `x-w` is feasible (equivalently `x in w+S_t`) or `x+q2+w` is feasible (equivalently `x in S_t`). These are precisely the exceptional `q2` starts declared above.

**3. The four-block.** Fix `y in S_t`. As `t<M`, `y-w` is infeasible, so `[y+w,y]` are the last two points in the `K(y)` fiber. Since `|y+q2+2w|_1>=H2>H`, `[y+q3,y+q2]` are the first two points in the `K(y)+1` fiber. The keys are consecutive integers, hence all four points are consecutive in the total lex ordering. Their exact increasing real order follows from `epsilon-2eta<0`, `epsilon-eta>0` and within-fiber `eta>0`:
```
theta(y+q3) < theta(y+w) < theta(y+q2) < theta(y).
```
The inverted comparisons are the two `q2` pairs starting at `y,y+w`, plus the `q3` pair starting at `y`.

**4. Completeness, disjointness and counts.** Because `t<M`, the sets `S_t` and `w+S_t` do not intersect. Distinct four-block starts cannot overlap: otherwise the difference between two members of `S_t` would equal `w` or a larger positive displacement, impossible because their coordinate sum is at most `t<M`. A `q2` endpoint cannot start another `q2` pair since `H<H2<2H0`. Each `q3` pair belongs to exactly one four-block, and all remaining `q2` pairs are disjoint adjacent swaps. By the complete inversion classification in step 1, the replacements correct every pairwise discrepancy, proving the full order. There are `T(s)` q2 inversions and `T(t)` q3 inversions. Each four-block consumes two q2 pairs and one q3 pair, giving the stated formulas; their finite permutation gives the rank/select corrections.

**5. Sharp endpoint.** The point `q4` lies in `S_{H2}`; it has `K(q4)=1` yet `theta(q4)=epsilon-4eta<0`. This pair with the origin is not of displacement `q2` or `q3`.

## Validation, observer scope and next steps

`VERIFY.py` independently encloses the logarithms by a 45-term atanh rational series with rigorous remainder, checks the only two inversion-producing lattice coordinate pairs, exhaustively compares complete true vs corrected sorting on all `H=0..21` of the scaled unimodular model `u=(1,1),w=(2,3),r=61/44`, then checks giant-H four-block ordering and exact counts at four representative horizons. `RUN_EVIDENCE.txt` is its executed stdout. The universal finite-window result follows from the symbolic proof above. All tests use exact `Fraction` and integer operations.

BRC reuse: the auxiliary observer's **joint label (1,4) count carrier** is preserved, with no factor or branch collapse; the operation is an exact ordered-readout transform (`REUSE_APPLIED`). The original P000/ACTIVE X6 worldview is unchanged. This theorem concerns order/rank/select, not a new plateau of capacity `N(H)` or the lawful six-source/ten-label mother-model bridge.

Next: at `H2=9,820,786`, add `u+4w`; by `2H0=9,821,296` also add the first `2q2` inversion and handle overlapping classes. Independently settle full changed-gap prefix occupancy at `H=2,455,579`, and retain the four-observation minimax `delta_4` question. Independent review remains pending.
