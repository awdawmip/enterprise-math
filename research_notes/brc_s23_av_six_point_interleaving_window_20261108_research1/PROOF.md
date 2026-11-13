# S23/AV: exact six-point interleaving in the third inversion window

Date: 2026-11-08. Status: author-side exact proof/certificate; independent review pending.
Scientific input **unchanged**, frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Parent provenance: PR #1777; exact preceding four-point theorem at `c43c0279fb4b53b7b7e0d53b1ae4836994fa382b`, `research_notes/brc_s23_av_four_point_rotation_window_20261108_r1/PROOF.md`.
Object: exact order/rank/select of joint-count-preserving, two-point S23/AV auxiliary likelihood-sign observer thresholds; no change to its population, labels (1,4), or label-3 padding.

## Definitions

Let `S_H={(v,j):v,j integers >=0, v+j<=H}`, `r=ln(7)/ln(10/7)`, `theta(v,j)=rv-j`. Write
```
u=(79,431), w=(380295,2074774), M=|w|_1=2455069,
q2=u+2w=(760669,4149979), H0=|q2|_1=4910648,
q3=u+3w=(1140964,6224753), H1=|q3|_1=7365717,
q4=u+4w=(1521259,8299527), H2=|q4|_1=9820786,
H3=2|q2|_1=9821296.
K(v,j)=2074774*v-380295*j, L(v,j)=(K(v,j),-v) lexicographic.
epsilon=79*r-431, eta=2074774-380295*r,
T(n)=(n+1)(n+2)/2 for n>=0.
```
The predecessor's rigorous rational bounds, independently checked in `VERIFY.py`, yield `0<eta<epsilon<2eta` and `2epsilon>3eta`.

## Theorem (third-window exact order, sharp boundary)

**For every integer H with 9,820,786 <= H <= 9,821,295**, put
```
s2=H-H0=2M+z, t3=H-H1=M+z, z=H-H2, 0<=z<=509.
```
The exact increasing `theta` ordering of all `S_H` is obtained from the lexicographic order `L` by three **pairwise disjoint** local operations:

1. **Six-point interleaving** for each `x in S_z`. The six consecutive old entries
```
[x+2w, x+w, x, x+q4, x+q3, x+q2]
```
are replaced by the following six entries, in exact increasing `theta` order:
```
[x+q4, x+2w, x+q3, x+w, x+q2, x].
```
2. **Four-point rotation** for every `y in S_t3 \ (S_z union (w+S_z))`, by the predecessor's map
```
[y+w,y,y+q3,y+q2] -> [y+q3,y+w,y+q2,y].
```
3. **Isolated adjacent swap** for every `a in S_s2 \ (S_t3 union (w+S_t3))`:
```
[a,a+q2] -> [a+q2,a].
```
All other entries keep their old position. In particular, existing exact `L` rank/select can be corrected using a fixed number of integer triangle-membership tests.

The operation counts and total inversion count are exactly
```
six-point blocks       = T(z)
four-point blocks      = T(M+z)-2*T(z)
isolated pair swaps    = T(2M+z)-2*T(M+z)+T(z) = M^2 = 6027363794761
inverted point pairs   = T(2M+z)+T(M+z)+T(z).
```
On the six-block, the rank correction `rank_theta-rank_L` for the points in the **old order** is `(+1,+2,+3,-3,-2,-1)`; `select_theta` at these six old lex slots returns, respectively, `(x+q4,x+2w,x+q3,x+w,x+q2,x)`.

The interval's endpoint is sharp for this **q2,q3,q4-only inversion classification**: at `H=9,821,296=2|q2|_1`, displacement `2q2=2u+4w` first becomes feasible, has `K=2` yet true sign `2epsilon-4eta<0`, and is not in the three prior classes.

## Proof

**I. Complete discrepancy classification.** Since `det(u,w)=79*2074774-431*380295=1`, each integer displacement has a unique representation `d=A*u+B*w`, with `K(d)=A` and `theta(d)=A*epsilon-B*eta`. A zero-first-key pair is ordered correctly by `-v`. Reverse endpoints to assume `A>0`. For `B<=0` the true sign agrees with the key; `B=1` also agrees because `epsilon>eta`. For a discordant pair `B>=2` and `A>=1`, the displacement is componentwise nonnegative and its feasible size is `510A+MB<=H<H3`. Thus `B<=4`; when `B=4` necessarily `A=1` because `2*510+4M=H3`. For `B=2`, only `A=1` has negative true sign (`2epsilon>2eta`). For `B=3`, only `A=1` has negative sign (`2epsilon>3eta`). For `B=4`, `A=1` is negative. Hence **all and only** reversed point pairs have displacements `q2,q3,q4`, with starts `a in S_s2`, `y in S_t3`, `x in S_z`, respectively.

**II. Six consecutive integer-key positions.** Fix `x in S_z`. Since `z<510<M`, the last three entries of the key-`K(x)` fiber are `x+2w,x+w,x` (there is no `x-w`). The first three entries of the next key fiber are `x+q4,x+q3,x+q2` (there is no feasible `x+q4+w`); these fibers have adjacent integer keys. Their true increments relative to `theta(x)` are, respectively,
```
-2eta, -eta, 0, epsilon-4eta, epsilon-3eta, epsilon-2eta.
```
Because `3eta/2<epsilon<2eta`, the correct strict order is `epsilon-4eta < -2eta < epsilon-3eta < -eta < epsilon-2eta < 0`, giving the six-point interleaving. It consists of three `q2`, two `q3` and one `q4` inverted pair.

**III. Four consecutive entries elsewhere.** For `y in S_t3`, the four-point predecessor block has its old endpoints consecutively adjacent exactly when `y-w` is infeasible **and** `y+q4` is infeasible. These two failures are equivalent to `y not in w+S_z` and `y not in S_z`. Otherwise `y=x` or `y=x+w` for `x in S_z`; these are precisely the two four-point fragments absorbed in the six-point block above. Every remaining four-block contributes exactly two `q2` inversions and one `q3` inversion.

**IV. Other swaps and disjointness.** The `q2` start set is `S_s2`. A `q2` pair is not an isolated adjacent pair exactly when its start belongs to `S_t3 union (w+S_t3)`, and its endpoints are then in a six- or four-block. Since `S_t3 intersect (w+S_t3)=w+S_z`, the isolated count is `T(s2)-2T(t3)+T(z)`. Distinct six-blocks cannot share an entry: a difference of their starts in `S_z` cannot equal a nonzero displacement among `u,w` or their relevant combinations, because every such feasible positive displacement has coordinate sum at least 510 while `z<510`; opposite-sign combinations cannot equate the nonnegative offsets in these neighboring key fibers. All remaining four-blocks and isolated pairs are similarly disjoint by the extremal-key-fiber criterion of III, and there are no chained `q2` endpoints since `H<2H0`. Therefore each of the three classes is a disjoint local permutation and resolves every inverted pair from I. The resulting order is exact.

**V. Counts, constant swap number, boundary.** There are `T(z)` six-block starts. Four-block starts comprise the `T(t3)` starts minus two disjoint translates `S_z` and `w+S_z`; thus `T(t3)-2T(z)`. The isolated swap count simplifies by the quadratic second finite difference of `T` to `M^2`. Three `q2`, two `q3`, one `q4` inversions per six-block; two `q2`, one `q3` per four-block; one `q2` per isolated swap gives the stated total. At `H3`, `2q2` is feasible and its sign disagrees with `K=2` since `epsilon<2eta`: it is a new class. QED.

## Evidence and scope

`VERIFY.py` (Python 3 standard library, exact `Fraction`) rigorously encloses `r` with a 45-term atanh series, confirms the complete finite inversion type set at `H3-1`, exhaustively compares old-key correction against true sort for every H in the third window in **two different unimodular scaled models**, and validates six-block inequalities/counts at three actual large-H endpoints. `RUN_EVIDENCE.txt` contains the actual program output. Universal finite-window correctness is the symbolic argument above, not extrapolation from scaled model tests.

BRC use: retain the joint label-(1,4) observer carrier, source/branch identity and label-3 padding; the transformation is an exact observer order readout (`REUSE_APPLIED`). The P000/ACTIVE X6 native model and original frozen science remain unchanged. The observer's capacity `N(H)` and six-source/ten-label mother-model link are separate unsolved units. Independent mathematical review pending.
