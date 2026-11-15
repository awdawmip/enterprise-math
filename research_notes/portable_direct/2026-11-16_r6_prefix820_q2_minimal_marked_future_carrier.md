# PREFIX-820 — Capacity-two one-marked addition: an exact minimal eight-coordinate future observer

Date: 2026-11-16 (Asia/Shanghai). Mode: independently publishable portable TASK_RESEARCH auxiliary mathematics. Frozen scientific input P000 pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Predecessors: PREFIX-817/818/819, especially PREFIX-819 conditional moment carrier. Research lineage: prior portable activity `RA-9B596EB6873BC7BAF237BC3A` / `EM-DIRECT-AB379B`; current native shared CLAIM not asserted. Status: AUTHOR_PROVED, EXACT_INTEGER_REGRESSION, NOT_INDEPENDENTLY_REVIEWED.

## Object and observation scope

Let `m>=4`, capacity `q=2`, a distinguished named branch `j=0`, unmarked branches `1,...,m-1`, removal weights `beta_i>=0` and marked addition weight `a>=0`. Named states are subsets `S` of cardinality at most two. `R` removes any present named branch `i` with weight `beta_i`; `A` adds only branch zero, with weight `a`, when absent and capacity permits. `Q=R+A` sums alternatives with multiplicity. Initial states have arbitrary integer mass (for physical counts, nonnegative mass). At every horizon observe the exact three-component terminal histogram `Y_l=sum_{|S|=l} mass(S)`, `l=0,1,2`. The declared operation language includes all words in `R,A`, hence also `Q^t`; it does not permit selecting an individual unmarked named removal as a separate operation.

This is a BRC auxiliary source-fiber calculation. An explicit compatible X6 representation fixes a native Cell `c` in the HEARTBEAT_WORLD native X6 torsor and attaches the named subset as internal state `(c,S)`; all declared `R,A` operations preserve `c`. Thus no native spatial direction or provenance is erased. Formal word length is an operation horizon, not a native heartbeat elapsed-time calibration or admission of a Cell/Link/Port event.

## Theorem 820.1 — exact eight-coordinate nonnegative integer carrier

Use PREFIX-819's nine conditional elementary-symmetric moments `M_{z,k,h}`: `z` records marked-branch presence, `k` is the number of unmarked present branches, `h=0,...,k`, and `M_{z,k,h}=sum mass(S)e_h(beta_i:i in S except j)`. Set `b=beta_0` and define the eight coordinates, with names chosen to avoid subscripts,

- `x=M_{0,0,0}; y=M_{0,1,0}; z=M_{0,1,1}`;
- `u=M_{0,2,0}+M_{1,1,0}; v=M_{0,2,1}+b*M_{1,1,0}; w=M_{0,2,2}`;
- `p=M_{1,0,0}; r=M_{1,1,1}`.

Their exact one-step recurrence for the combined operator `Q` is

```text
(x',y',z',u',v',w',p',r')
  = (z+b*p, v, 2*w+b*r, a*y, a*b*y, 0, a*x+r, a*z)
Y = (x, y+p, u).
```

This recurrence works for every `m`, every declared integer weight, every initial mass distribution and every finite or arbitrarily long formal-toggle horizon. It has eight coordinates independent of `m`, with no divisions. For nonnegative weights and mass its coordinates and update are nonnegative. It also preserves the more discriminating `R,A` word language through the separately executable maps

```text
R(x,y,z,u,v,w,p,r)=(z+b*p, v, 2*w+b*r, 0,0,0, r,0)
A(x,y,z,u,v,w,p,r)=(0,0,0, a*y,a*b*y,0,a*x,a*z).
```

**Proof.** PREFIX-819's nine-moment recurrence at `q=2` is
`M'_{0,k,h}=(h+1)M_{0,k+1,h+1}+bM_{1,k,h}` and
`M'_{1,k,h}=(h+1)M_{1,k+1,h+1}+aM_{0,k,h}`, with absent coordinates zero. Substituting each of the eight definitions yields the displayed recurrence; the same substitution after separating removal from addition yields the two word maps. The output is the sum over marked presence for each cardinality. Induction over any word length proves the exact assertion. All formulas are sums and products of nonnegative integers on nonnegative input. QED.

## Theorem 820.2 — eight is the exact minimum linear dimension when a>0

Assume at least three unmarked removal weights are pairwise distinct, and `a>0`. Among **rational linear** future-observer carriers for *arbitrary initial named-state mass vectors* which must return all future `Q^t` count histograms, the minimal dimension is exactly **8**. Consequently this also lower-bounds carriers that retain the stronger separate `R,A` word observations.

**Proof, upper bound.** Theorem 820.1 provides an eight-coordinate exact linear carrier.

**Proof, lower bound in the nine-moment space.** Order its standard basis as

```text
(M000,M010,M011,M020,M021,M022,M100,M110,M111).
```

Let `T` be the nine-moment matrix of `Q` in that basis and `C` the three histogram rows. The vector
`k=(0,0,0,-1,-b,0,0,1,0)^T` satisfies `Tk=0` and `Ck=0`. Hence the observability rank is at most eight. In `O_2=[C;CT;CT^2]` (nine rows), delete row 8 (1-based: output `Y_1` at horizon 2) and column 8 (1-based: `M110`). The resulting 8-by-8 minor has determinant **`2a^2`**, independently of `b`. For `a>0` the observability rank is therefore exactly eight.

**Transfer from moments to named states.** The map from named initial masses to all nine conditional moments is rationally onto if three unmarked weights `s,t,u` are distinct. The cardinality-two unmarked pair states provide the three independent rows `(1,s+t,st)`, `(1,s+u,su)`, `(1,t+u,tu)`, with determinant `-(s-t)(s-u)(t-u) != 0`. The unmarked cardinality-one and marked-plus-one blocks span their two moment coordinates because weights differ, and the two cardinality-zero blocks span their one coordinate each. These are disjoint `(z,k)` blocks; their total rank is nine. Therefore the eight-dimensional observable image of the moment system is already attained by actual named-state initial masses. Any rational linear carrier outputting all horizons must have rank at least eight. QED.

For `a=0`, the operation is pure weighted removal and the exact rank for this same nondegenerate named-state family is `T(2)=6`: horizons zero, one and two recover the six independent unconditioned elementary-symmetric moments at sizes 0,1,2, while later horizons vanish. This is the precise boundary between PREFIX-818 and the marked-addition repair.

## Why the discarded direction is safe for this observer

The nine-to-eight map has kernel generated by the vector `k` above. Both individual operation matrices `R` and `A` annihilate `k`, and so does the output matrix `C`. Thus every allowed future word factors through the same quotient: the claimed redundancy has an exact infinite-horizon observer/operation descent certificate. If future operations can address individual named unmarked removals, their preservation must be tested anew; this result makes no such assertion.

This carrier is not the original native X6 state, nor an observer of signed/phase cancellation, and the eight rational-linear dimensions do not constrain the six native spatial axes.

## Exact finite validation and reproducibility

The companion standalone checker `PREFIX820_R6_Q2_MINIMAL_MARKED_CARRIER_CHECK.js` uses exact JavaScript BigInt path enumeration and independently constructs the eight-coordinate recurrence. It tests `m=4..7`, unmarked beta `base,base+1,...` with base in `{1,3,5}`, marked beta in `{0,1,4}`, addition weight in `{0,1,2,5}`, every named basis state, and all `Q` horizons `0..11`. It separately checks all `R,A` words of lengths `0..6` in a fixed positive-weight 4-branch instance. Row-rank checks use exact modular elimination modulo 1009 for each small instance, serving as finite nonzero-minor witnesses; the general rank assertion is proved by the symbolic determinant above. The results JSON records observed comparison counts and parameter coverage.

The implementation run produced: 144 parameter instances, 2,808 basis-state tests, 33,696 exact combined-operation histogram comparisons, 1,397 separate-word comparisons, 144 observability-rank checks and 12 surjectivity checks; all assertions passed.

## Next research unit

For capacity `q>=3`, characterize the exact observer-kernel dimension as a function of `q,a,b` and the nondegenerate named-state moment span. Small exact computations suggest parameter-dependent rank loss beyond the `q=2` one-dimensional kernel; identify invariant subspaces, produce an explicit reduced integer carrier, and separately test source-specific operations that distinguish the quotient. Preserve the frozen native-X6 event correspondence question as an independent task.
