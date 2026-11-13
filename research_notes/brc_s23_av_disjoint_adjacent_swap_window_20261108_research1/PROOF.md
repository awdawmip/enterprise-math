# S23/AV: exact post-lex ordering by disjoint adjacent swaps through H=7,365,716

Date: 2026-11-08 Asia/Shanghai. Status: author-side exact mathematical theorem, independently reviewable; no independent review claimed.
Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Immediate input: `research_notes/brc_s23_av_sharp_fixed_triangular_key_20261108_r1/PROOF_LEX_EXTENSION.md` and `FIRST_NEW_GAP_EXACT.md` at `d3a6b51fe2e351e6039419baaa5a9a433b1c94c4`. Retain the joint label (1,4) and label-3 padding observation.

## Exact theorem

Let `r=ln(7)/ln(10/7)` and `S_H={(v,j) in Z_{≥0}^2:v+j≤H}`, with threshold `t(v,j)=r*v-j`. Set

- `u=(79,431)`, `w=(380295,2074774)`, `M=|w|_1=2455069`;
- `P=2074774, D=380295`, `K(v,j)=P*v-D*j`;
- `epsilon=79*r-431`, `eta=P-D*r`, so `0<eta<epsilon<2eta` and `2epsilon>3eta`;
- `q=u+2w=(760669,4149979)`, `H0=|q|_1=4910648`;
- `H1=|u+3w|_1=7365717`.

**Theorem (sharp disjoint-swap correction).** For every integer `H0≤H<H1`, write `s=H-H0`. Sort all `S_H` by the integer lexicographic key `L(v,j)=(K(v,j),-v)`. The exact increasing order of `t(v,j)` is obtained by swapping, once each, the **disjoint consecutive lexicographic pairs**

`(x,x+q)`, for every `x∈S_s`.

There are exactly `(s+1)(s+2)/2` such pairs, and **no other inversions**. This covers every one of the 2,455,069 integer horizons `4,910,648≤H≤7,365,716`; the total number of thresholds need never be enumerated.

**O(1) correction of a pre-existing rank/select oracle.** Let `rank_L(p)` be the zero-based rank from the existing integer-key lex oracle. Define

`d_H(p)=1` if `p∈S_s`; `d_H(p)=-1` if `p-q∈S_s`; `d_H(p)=0` otherwise.

Then `rank_t(p)=rank_L(p)+d_H(p)`. For true select at index `i`, first let `z=select_L(i)`. If `z∈S_s`, return `z+q`; if `z-q∈S_s`, return `z-q`; otherwise return `z`. This costs constant extra arithmetic/predicates per query, after the previous floor-sum rank/select oracle.

**Sharp boundary for this correction.** At `H=H1=7365717`, the new displacement `u+3w` is feasible and has `K=1`, but its actual threshold difference `epsilon-3eta<0`. It creates an inversion not included in the listed `q` pairs; thus the correction theorem's stated validity window is sharp.

## Proof

1. `79P-431D=1`. Each integer displacement `(a,b)` has unique coordinates `(a,b)=A*u+B*w`, with `A=P*a-D*b`, `B=79*b-431*a`. It changes `K` by `A` and the real threshold by `A*epsilon-B*eta`. When `A=0`, the lex tie-break `-a=-DB` agrees in sign with `-B*eta`. For `A<0`, reverse endpoints, so consider `A>0`.
2. If `B≤0`, `A*epsilon-B*eta>0`. If `B=1`, the difference is at least `epsilon-eta>0`; if `B=2,A≥2`, it is at least `2epsilon-2eta>0`. For `B=3,A≥2`, it is at least `2epsilon-3eta>0`. The case `(A,B)=(1,3)` requires `|a|+|b|=510+3M=H1>H`, because both coordinates of `A*u+B*w` are positive. For `B≥4,A≥1`, the positive-coordinate sum is at least `510+4M>H1>H`. The only remaining inversion-generating displacement is `(A,B)=(1,2)`, namely `q`, with `epsilon-2eta<0`.
3. Any two points `p,p+q∈S_H` have `p∈S_{H-H0}=S_s`; conversely each `p∈S_s` gives such a pair. There is one inverted unordered pair per `x∈S_s`; all other comparisons agree with `L`.
4. Since `s<M`, no `x∈S_s` admits `x-w∈S_H`. All points of a common integer `K`-fiber differ by multiples of `w`; hence `x` is **last** in its `K(x)` fiber in the `L=(K,-v)` order. Also `x+q+w∉S_H`, so `x+q` is **first** in the next fiber `K(x)+1`. There is no integer key between these consecutive key values. Thus each inverted pair is adjacent in the lex order. The pairs are disjoint because `|x|_1≤s<M<H0≤|x+q|_1`; one point cannot belong to two pairs. Swapping these adjacent pairs therefore corrects every inversion and yields precisely the real order.
5. At `H1`, `u+3w` first appears in the triangle with `K=1`, `t(u+3w)=epsilon-3eta<0`. It is not `q`, and the previous classification excludes this displacement for all smaller `H`. Therefore the stated purely-`q` correction first requires enlargement exactly at `H1`.

All strict inequalities follow from an independent rational enclosure for `r`, with 45-term `atanh` series for `ln2`, `ln(8/7)`, `ln(10/7)` and rigorously bounded positive tails; executable arithmetic certificate is in `VERIFY.py`.

## Concrete boundary/rank certificate

At `H=4910648`, the `K=0` fiber is `2w,w,0`, and the `K=1` fiber starts with `q,u+w,u` in lex order. Their exact order requires swapping just `0` and `q`. The exact count `C_H(0)=#{p∈S_H:K(p)<0}=1,867,691,687,412`, giving zero-based `rank_L(0)=1,867,691,687,414`, `rank_t(0)=1,867,691,687,415`; `rank_L(q)=1,867,691,687,415`, `rank_t(q)=1,867,691,687,414`.

At `H=7365716`, `s=2455068` and the correction is `3,013,683,124,915` disjoint adjacent swaps. This is a symbolic all-points statement, not a direct enumeration of that many pairs.

## Evidence, scope and next question

The `VERIFY.py` source establishes the log enclosure using exact rational arithmetic, checks the lattice inequalities, tests selected swap instances and the exact large boundary rank, and verifies sharp new displacement at `H1`. `RUN_EVIDENCE.txt` stores the actual Python output. The proof above supplies complete quantifiers; finite program checks are independent implementation/calculation checks, not a substitute for the general symbolic proof.

This extends the **order/rank/select** algorithm, not an observation-capacity `N(H)` plateau: exact S23/AV capacity near the previously open `H=2455579` still needs an all-gap occupancy certificate. Next: find a sparse floor-sum way to compute changed-gap occupancy at `H=2455579`, and on the separate order path derive the new corrections beginning at `H1=7365717`. The lawful six-source/ten-label mother-model bridge and minimax `delta_4` remain distinct research units.
