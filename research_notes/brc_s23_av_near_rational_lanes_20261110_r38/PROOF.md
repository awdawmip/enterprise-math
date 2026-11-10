# R38 — Exact near-rational lane selection for rotation source windows

Date: 2026-11-10. Status: author-side proof and exact computational tests; independent mathematical review pending.

Previous frontier: R37 (PR #1955, `1594ea1d17c876435e8bd166a52ecf9183bb6df9`); R36 owner-labelled last-source/rank formula. Frozen S23/AV scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This note concerns the **auxiliary irrational circle-rotation observer**, not a native X6/BRC dynamic.

## Model
Let `θ` be irrational in `(0,1)`. Sorted historical phases `{kθ}`, `k=0,...,m-1`, define `m` labelled, half-open cyclic arcs `I_i=[a_i,b_i) mod 1` of unwrapped widths `w_i=b_i-a_i∈(0,1]`. The crossing-zero arc uses `b_i>1`. For a source window `[j-N,j)`, the last surviving source of owner `i` is
`τ_i=max{t∈[j-N,j): {tθ}∈I_i}`, or `⊥` when empty.

Choose coprime `0<=p<q`, `q>=2`, and write `θ=p/q+η` with `η>0`, `s=qη∈(0,1)`. In residue lane `t=r+qk` (`0<=r<q`) one has
`{tθ}={rθ+sk}`.
Thus each residue lane is an ascending arithmetic progression prior to reducing modulo 1.

## Lemma R38.1 — one-winding predecessor
Suppose `w=b-a>=s`, and the allowed lane indices satisfy `K_min<=k<=K_max`. Put `c=rθ`, `Y=c+sK_max`, `h=floor(Y-a)`. Define
```
K* = K_max                              if Y < b+h
K* = ceil((b+h-c)/s) - 1                otherwise
```
Then `K*` is the largest integer `k<=K_max` satisfying `{c+sk}∈[a,b) mod 1`. It is allowed by the actual source window iff `K*>=K_min`.

**Proof.** `a+h<=Y<a+h+1`. If `Y<b+h`, the newest source belongs to the arc. Otherwise `Y>=b+h`, and the second formula gives the greatest integer with `c+sk<b+h`. The index interval `[(a+h-c)/s,(b+h-c)/s)` has length `w/s>=1`, hence contains an integer, so that predecessor is still above `a+h`. All previous windings yield smaller indices and all subsequent indices are excluded by the current gap and `K_max`. Intersecting with `[K_min,K_max]` gives the stated result. QED.

## Theorem R38.2 — complete owner-labelled output
If `w_i>=s` for every historical arc, apply R38.1 to every arc and every residue `r=0,...,q-1`; take the maximum returned source per arc (or `⊥`). This computes **all m labelled last sources** using `q*m` lane candidates, following `O(m log m)` historical phase sorting, independent of N in *candidate count*. The bit size of `j,N,θ,p/q` enters exact arithmetic costs.

For a mixed-width partition, apply direct lanes to the good arcs `G={i:w_i>=s}` and independent R36 Floor Sum last-source selection to the narrow arcs `B={i:w_i<s}`. This exact hybrid requires `q|G|` lane candidates plus the `|B|` exact per-arc selections, preserving the original labels including empty arcs.

## Enclosure certificates
For a strict algebraic interval `θ∈[ℓ,u]` with rational endpoints, verify `floor(dℓ)=floor(du)` for `1<=d<m` to fix historical order. Arc endpoints and widths are then affine in θ; test `w_i>=qθ-p` at both endpoints. For each wide arc, compute the winding `h`, branch and integer candidate at both endpoints. Equality certifies all intermediate θ: relevant winding/branch inequalities are affine, and `(b+h-rθ)/(qθ-p)` is monotone linear-fractional with positive denominator. The final source membership inequalities are also affine.

For a narrow arc whose reference last source is `t`, certify its omitted suffix `[t+1,j)` contains no arc source (or the entire `[j-N,j)` when empty). The stated monotone-floor certificate assumes the checked suffix lower endpoint is at least `m-1`, so every `v-z` below is nonnegative; the performed seven tests satisfy this. For earlier source windows, use the signed Floor Sum form or direct endpoint subdivision instead. For each historical index `z∈{0,left_endpoint,right_endpoint}`, require equality of the endpoint sums
`sum_{v=L}^{j-1} floor((v-z)ℓ) = sum_{v=L}^{j-1} floor((v-z)u)`.
Here `v-z>=0`, so every individual summand is nondecreasing in θ; equality of the sums forces every floor term to stay fixed throughout the interval. The R36 arc-count identity then certifies the suffix. Check membership of `t` at both endpoints as well.

## Exact tests
An independently executed Python `Fraction` / integer-square-root verifier compared the last-source vectors against R36's per-arc exact Floor Sum binary-selection oracle over seven tests. Full families and operation counts are in `EVIDENCE.md`; the generated full local code and JSON certificate are separately included in the R38 research bundle. The near-rational R37 hard case with `θ=1/3+sqrt(2)/10^7`, `m=21`, `j=10^9`, `N=10^8` yields all 21 correct labels with 63 lane candidates and zero Floor Sum queries (all-arc reference 581 count queries). The overlapping-cluster test with `m=257` has 45 narrow arcs and uses 636 lane candidates plus 1245 reference count calls (all-arc oracle 7109 calls).

The experiment establishes an operation-count improvement for the declared small-q regimes. General comparison requires accounting for q-selection, enclosures, integer division and bit lengths. The previous trillion-step S23 298-run table was not recomputed in this R38 selector test.

## Next mathematical unit
Share Euclidean/Floor Sum computations among the **narrow** arcs; compare offline cumulative endpoint batching with Ostrowski digit blocks and direct R36 per-arc selection on families with growing q. Keep per-owner provenance and an independent source oracle. See `NEXT_TASK.md`.
