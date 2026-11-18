# S23/AV: exact twentieth capacity plateau by a 194-critical-cell lattice cover

Date: 2026-11-08 (Asia/Shanghai). Status: author-side mathematical proof with exact rational executable certificate; independent mathematical review pending. Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Theorem

In the frozen two-point iid S23/AV auxiliary experiment, with label probabilities (1,3,4) equal to `P0=(1/2,1/4,1/4)`, `P1=(5/7,1/4,1/28)`, and with the exact joint-count likelihood-sign observer retaining label-1 and label-4 counts and neutral label-3 padding, let `N(h)` be the least common padded prefix length needed to hit every bounded open threshold cell and both exterior cells of `T_h={10^i/7^s:0<=i<=s<=h}`. Then **for every integer**

`7,226,985 <= h <= 7,607,279`, `N(h) = 41,880,515`.

## Coordinates and lower bound

Write `r=ln 7/ln(10/7)`, `eps=79*r-431`, `eta=11*r-60`, `gamma=eta-eps`, `d=2074774-380295*r`. The threshold triangle is `D_H={(v,j) in Z^2_{>=0}:v+j<=H}` with ordered reflected-log values `t(v,j)=r*v-j`. An attainable prefix is `E(k,ell)=k-r*ell` with `k,ell>=0`, `k+ell<=n`; neutral label 3 pads it to length `n`.

Reuse the exact scaled-gap first-entry theorem from `research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md` at `85b53d06d6ba775e516c566c1d79828b6ca9bb1f`: for `a_i=floor(i*d/eps)`, `V_i=380295*i+79*a_i`, `K_i=2074774*i+431*a_i`, the translated cell `J_t` first receives a prefix of length `K_i+V_i-t` when `V_(i-1)<t<=V_i`. The rational certificate gives `a19=a20=11`, `(V19,K19)=(7226474,39425447)`, `(V20,K20)=(7606769,41500221)`. Thus at `t=V19+1=7226475` and `h=t+510=7226985`, the exact first-entry obstruction forces

`N(h) >= K20 + V20 - (V19+1) = 41880515`.

## Complete narrow-displacement classification at H20

We establish the matching upper bound at `H=V20+510=7607279`. Let `U=(79,431)`, `W=(11,60)`. They form a unimodular integer basis (`det(U,W)=-1`). Every integral displacement between threshold points has unique representation `(dv,dj)=a*U+b*W`; its positive threshold width is `x=dv*r-dj=a*eps+b*eta`. The exact integer `b` is also `79*x-eps*dv`. If `0<x<eps` and both points lie in `D_H`, then `abs(dv)<=H` and hence `abs(b)<eps*(H+79)<21`. The case `b=0` would make `x` an integer multiple of `eps`, impossible within `(0,eps)`.

For every `b` in `{-20,...,-1,1,...,20}`, the strip `0<a*eps+b*eta<eps` contains at most one integral `a`. `VERIFY.py` uses 45 rational atanh-series terms, a rigorous remainder, and `LO/10^26<r<(LO+1)/10^26`, with `LO=545569623581288298975349314`, to select and verify all forty `a` values. It tests the *minimum triangular embedding cost* `max(dv_+ + dj_+, (-dv)_+ + (-dj)_+) <= H`. Precisely six survive, in `(b,a,dv,dj,minimum H)` order:

```
(-3, 14444, 1141043, 6225184, 7366227)
(-2,  9630,  760748, 4150410, 4911158)
(-1,  4815,  380374, 2075205, 2455579)
( 1, -4814, -380295,-2074774, 2455069)
( 2, -9629, -760669,-4149979, 4910648)
( 3,-14443,-1140964,-6224753, 7365717)
```

Every other positive difference between points in `D_H` has width at least `eps`. The checker compares each witness offset `delta_i=K_i-r*V_i` strictly against each narrow width; exact equality is also recorded as blocking, since the target open cell requires a strict interior point. It certifies `0<delta_i<eps` for `i=1..20`.

## 194-critical-cell universal coverage theorem

For a bounded cell immediately following `p=(v,j)` in `D_H`, the shift `(K,L)` gives the prefix `(k,ell)=(K-j,L-v)`, score `t(p)+delta` with `delta=K-r*L`, and length `K+L-(v+j)`. This prefix lies strictly inside that cell whenever `K>=j`, `L>=v`, `K+L-(v+j)<=M`, and no threshold difference from `p` has positive width `<=delta`.

Use candidate shifts `(K_i,V_i)`, `i=1,...,20`, with `M=41880515`. Since their offsets lie in `(0,eps)`, an obstruction can only be one of the six narrow displacements. For a forward narrow displacement `(dv,dj)` with both entries positive, it can originate at `p` exactly when `s=v+j <= H-(dv+dj)`. For a backward narrow displacement with both entries negative, it can originate exactly when `v>=-dv` and `j>=-dj`. These are *necessary and sufficient* for the translated point to belong to `D_H`.

Partition all integer triples `(v,j,s)` with `0<=v<=V20`, `0<=j`, `s=v+j<=H` by the exact threshold cuts:

- `v`: all `V_i+1`, all `-dv` from backward narrow vectors, and the range endpoints;
- `j`: all `K_i+1`, all `-dj` from backward narrow vectors, and the range endpoints;
- `s`: all `K_i+V_i-M` and all `H-(dv+dj)+1` from forward narrow vectors, and the range endpoints.

After discarding cuts outside the specified domain, the cut arrays have respectively **24, 8, and 8 endpoints**. For each resulting coordinate triple of integer intervals `[vl,vh]`, `[jl,jh]`, `[sl,sh]`, a lattice point satisfying `s=v+j` exists **if and only if**

`max(vl+jl,sl) <= min(vh+jh,sh)`.

This equivalence holds because every integer sum between `vl+jl` and `vh+jh` is attained by integer coordinates in the given boxes. There are **194 nonempty critical cells**. On every such cell, all witness-admissibility predicates (`v<=V_i`, `j<=K_i`, `s>=K_i+V_i-M`) and all six narrow-displacement feasibility predicates are constant by construction. `VERIFY.py` exhausts these **194 complete integer cells**, selecting an admissible candidate whose offset is strictly less than every feasible positive narrow width in each; **zero cells remain uncovered**. Thus all bounded threshold cells with left endpoint `v<=V20` have a prefix within budget `M`. This is a complete finite *symbolic partition proof*, not point sampling of 7.6 million rows or 28 trillion thresholds.

## Top rows and exterior cells

For every left endpoint with `v>V20`, we have `j<=H-v<=509`. In this range every positive outgoing threshold difference is at least `gamma=eta-eps`. Indeed write it `x=a*eps+b*eta` in the unimodular basis. If `0<x<gamma`:

* `b=0` forces `a>=1`, whose sum increase `dv+dj=510*a>509` exceeds remaining triangle slack;
* `b=1` forces `a<=-2`, hence `dj<=-802<-j`;
* `b>=2` and `eta>4800*eps` force `a<=-4800*(b-1)-2`, hence `dj<-509<=-j`;
* `b<=-1` forces `a>4800*abs(b)`, hence `dv>509>=H-v`.

For each such `v`, take the smallest `m` in `1..6` with `L=V20+68+79*m>=v` and put `K=K20+371+431*m`. The exact checker proves `0<K-r*L<gamma`, `K>j` and `K+L-(v+j)<=K20+3498<M`. Since `V20+68+79*6 >=H`, all 510 top rows are covered.

The exterior cells are hit by `(k,ell)=(0,floor(H/r)+1)` and `(floor(r*H)+1,0)`. Strict interval arithmetic certifies their prefix lengths `1,394,374` and `41,503,004`, both below `M`.

Therefore `N(H)<=M`. Together with the exact scaled-gap lower bound at `h=7226985` and monotonicity of `N(h)` in `h`, this proves the theorem for every integer in the stated interval.

## Reproducibility, interpretation, next unit

Execute `python3 VERIFY.py`. It performs only exact integer/Fraction operations, including strict certification of the logarithm enclosure, exhaustive forty-beta check, twenty witness offsets, 194 feasible critical cells, six top-row shifts, and exterior lengths. `RUN_EVIDENCE.txt` contains actual stdout. Source integration is an author-side research artifact in Draft PR #1777, with independent mathematical review and formal Task/Result admission still separate.

This is a scoped result for the iid two-point label-count auxiliary BRC observer; joint label-1/4 counts and label-3 padding remain available. It does not alter protected P000/Heartbeat X6 ontological premises or the frozen source. The next discriminating target is the `i=21` horizon `H21=V21+510`, first classifying its possible `b=±3,±4` displacements and testing whether a new critical-cell witness cover preserves the scaled-gap lower bound. The lawful six-source/ten-label mother bridge and four-observation minimax problem remain independent.
