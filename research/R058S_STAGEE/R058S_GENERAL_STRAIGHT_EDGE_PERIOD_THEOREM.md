# R058S General Straight-Edge Period Theorem

Researcher-ID: `EM-R058S-7C91E4`  
Generation: `RS-R058S-EXACT-SQUARE-COLLAPSE-GRAMMAR-DISCOVERY`  
Stage: `E`  
Taskbook source: `424835a56a00406c62c02d3f3ce31b3a3766c6c6`

Epistemic status: **PROOF / EXACT STRUCTURAL ANALYSIS**.  No fit, optimizer, square-loss search, holdout, R057 fitted prior, or empirical `K>8` square prediction is used.

## 1. Carrier algebra for a primitive tangent

Let `t=(a,b) in Z^2`, `t != 0`, with `gcd(|a|,|b|)=1`.  Put

`Q(a,b)=a^2+a b+b^2`,

`beta((x1,x2),(y1,y2))=2 x1 y1+x1 y2+x2 y1+2 x2 y2`,

and use the exact unreduced perpendicular

`n0=(a+2b, -(2a+b))`.

A direct expansion gives

`beta(t,n0)=0`

and, for every `x=(x1,x2)`,

`beta(x,n0)=3(b x1-a x2)`.

Define the integer height `lambda(x)=b x1-a x2`.  Since `gcd(|a|,|b|)=1`, Bezout gives integers `u,v` with `b u-a v=1`; hence `lambda(Z^2)=Z` and

`beta(Z^2,n0)=3 Z`.

Moreover `lambda(x)=0` means `b x1=a x2`.  Primitivity of `(a,b)` implies `x=r(a,b)` for some `r in Z` (including the cases `a=0` or `b=0`, when the nonzero coordinate is necessarily `+/-1`).  Therefore

`ker_Z beta(.,n0)=ker lambda=Z t`.

Thus the primitive lattice translation preserving every digital half-plane `{beta(x,n0)<=h}` is exactly `+/-t`.

## 2. Exact exposed-edge orbit count

Use the frozen six nearest-neighbor directions

`e0=(1,0), e1=(0,1), e2=(-1,1), e3=(-1,0), e4=(0,-1), e5=(1,-1)`.

Put `w_j=beta(e_j,n0)` and `s_j=w_j/3`.  The six exact integer increments are

`(s0,s1,s2,s3,s4,s5)=(b,-a,-(a+b),-b,a,a+b)`.

For a rational threshold `h`, let `r=floor(h/3)`.  A center `x` contributes an exposed Voronoi edge of type `j` precisely when

`lambda(x)<=r < lambda(x)+s_j`.

If `s_j<=0` there is no occupied-to-unoccupied edge of that oriented type.  If `s_j>0`, the allowed heights are exactly

`r-s_j+1, ..., r`,

so there are exactly `s_j` height classes.  Because `lambda` induces a bijection

`Z^2 / Zt  ->  Z`,

each height class is exactly one translation orbit modulo `t`.  Hence

`N_j(t)=max(w_j,0)/3=max(s_j,0)`.

Summing the six orbit counts gives

`m(t)=sum_j N_j(t)`
`=max(b,0)+max(-a,0)+max(-(a+b),0)+max(-b,0)+max(a,0)+max(a+b,0)`
`=|a|+|b|+|a+b|`.

For the three reals `a,b,-(a+b)` whose sum is zero, the magnitude of the unique-sign term (or tied zero-degenerate limit) equals the sum of magnitudes on the opposite sign.  Therefore

`|a|+|b|+|a+b| = 2 max(|a|,|b|,|a+b|)`.

So, with `H_hex(t)=max(|a|,|b|,|a+b|)`, 

`m(t)=2 H_hex(t)`.

**Status:** `TRIANGULAR_VORONOI_STRAIGHT_PERIOD_LENGTH_THEOREM_PROVED`.

## 3. One quotient cycle, endpoint displacement, and minimality

Quotient the triangular lattice by the primitive translation subgroup `Zt`.  The height map `lambda` identifies quotient center orbits with the integer line `Z`.  Nearest-neighbor moves change height by the symmetric generating set

`S={+/-a,+/-b,+/-(a+b)}`.

Its gcd is one.  The induced Cayley graph on `Z` is connected, and each half-line `(-infinity,r]` and `[r+1,infinity)` is connected: take any finite full-graph path, translate it far enough into the chosen half-line by repeated steps of one nonzero generator, traverse the translated path, and translate back without crossing the endpoint level.  Hence the occupied and unoccupied center-cell unions in the quotient cylinder are both connected.

At every Voronoi vertex exactly three cells meet.  If all three have the same occupancy there is no boundary edge there; otherwise exactly two of the three pairwise interfaces separate occupied from unoccupied.  Thus every quotient boundary vertex has degree two.  The finite quotient boundary is therefore a disjoint union of cycles.  A contractible component would isolate a component of one side, and two or more essential components would split the cylinder into alternating bands and disconnect one side.  Since both sides are connected, the quotient boundary is exactly one essential simple cycle.

An embedded essential simple cycle in a cylinder represents a primitive generator of its fundamental group, so one lift changes by `+/-t`.  With the frozen occupied-left orientation and the unreduced normal `n0`, the sign is `+t`: in the frozen physical embedding, `n0` points to the right-normal side of the oriented tangent, while `{beta(.,n0)<=h}` lies on its left.  Consequently one oriented primitive boundary cycle lifts from `v_0` to

`v_m=v_0+t`.

The minimal nonzero lattice translation preserving the half-plane is `+/-t`, already proved from `ker lambda=Zt`; hence the translational period is primitive.

To prove minimal **edge-word** period, suppose the oriented direction word of its `m` edges had a proper cyclic period `p<m`.  The minimal such `p` divides `m`; write `m=s p` with `s>=2`.  Equal edge codes at positions `i` and `i+p` mean the corresponding parallel Voronoi edges have the same relative hexagon-edge type.  Therefore the displacement `delta=v_p-v_0` is a translation between two centers of the triangular lattice, so `delta` is a lattice vector.  Repeating the `p`-edge word `s` times gives

`t=v_m-v_0=s delta`,

contradicting primitivity of `t`.  Thus no proper cyclic word period exists and the minimal edge-word period is exactly `m(t)`.

**Statuses:** `TRANSLATIONAL_PERIOD_LENGTH_PROVED`, `EDGE_WORD_MINIMAL_PERIOD_PROVED`.

## 4. Adaptive exact whole-chord law

Stage D proved the abstract identity: if a periodic polygonal path satisfies `v_(i+m)=v_i+t`, then for every integer `q>=1`, whole-chord packets of length `k=q m` obey

`v_(i+k)-v_i=q t`

and the frozen all-period estimator equals `||t||` exactly.

For the present carrier, Sections 1--3 prove that the primitive straight period has

`m(t)=|a|+|b|+|a+b|`

edges and endpoint displacement exactly `t`.  In the frozen physical units `||t||^2=Q(t)`.  Therefore an aligned primitive period collapses by whole chord to

`sqrt(Q(t))`

exactly, and for every symbolic `q>=1`, `k=q m(t)` gives the same exact period density.

**Status:** `ADAPTIVE_PRIMITIVE_PERIOD_WHOLE_CHORD_STRAIGHT_EDGE_LAW_PROVED`.

The condition `m|k` remains a sufficient condition inherited from Stage D.  No carrier-specific converse is claimed here; Stage D already proved that divisibility is not necessary for an arbitrary periodic polygonal path.

## 5. D6 covariance and primitive reduction

The corrected spatial D6 action is generated on axial coordinates by

`R(a,b)=(-b,a+b)`, `F(a,b)=(a+b,-b)`.

Under either generator, the unordered absolute triple

`{|a|,|b|,|a+b|}`

is merely permuted.  Hence `H_hex` and `m=2 H_hex` are invariant.  Also

`Q(t)=(a^2+b^2+(a+b)^2)/2`,

so `Q` and the endpoint chord length `sqrt(Q)` are invariant.  Reflection reverses orientation but the frozen occupied-left traversal restoration returns the same positive length; reversal `t -> -t` likewise preserves all scalar quantities.

For a nonprimitive `u=(A,B)`, let `g=gcd(|A|,|B|)>0` and `t=u/g`.  The primitive carrier period is the one associated with `t`, not the unreduced value `m(u)`.  Algebraically `m(u)=g m(t)` and `Q(u)=g^2 Q(t)`: `u` represents exactly `g` repetitions of the primitive translation.

## 6. Raw digital density corollary

Every exposed Voronoi edge has frozen length `1/sqrt(3)`.  One primitive period therefore has raw digital length

`L_raw(t)=m(t)/sqrt(3)`.

Its straight teacher translation length is `sqrt(Q(t))`.  Hence the exact raw anisotropy factor is

`rho_raw(t)=m(t)/sqrt(3 Q(t))`.

This factor is D6 invariant but not orientation independent.  For example, primitive tangents `(1,0)` and `(1,1)` give respectively `2/sqrt(3)` and `4/3`.  The adaptive primitive-period whole-chord law does not fit a reciprocal coefficient; it removes the raw staircase excess structurally by replacing one complete primitive period with its exact endpoint chord.

**Status:** `RAW_DIGITAL_STRAIGHT_DENSITY_FORMULA_PROVED`.

## 7. Frozen eight-tangent back-check

Applying the theorem formula to the frozen Stage-C/D tangents

`(1,0), (-1,2), (3,1), (-5,7), (2,1), (-4,5), (3,2), (-7,8)`

gives exactly

`m=(2,4,8,14,6,10,10,16)`.

The separate Stage-D frozen 56-row record remains a finite consistency observation: within `k=2..8`, exact Stage-C whole-chord density occurred exactly when these `m` values divided `k`.  It is not used as proof of the general period formula or as a converse theorem.

## 8. Undeployed consequence and open boundary

The proved carrier law supports the semantic proposal `ADAPTIVE_PRIMITIVE_PERIOD_WHOLE_CHORD`: detect a carrier-intrinsic primitive straight-boundary period, reduce its translation to primitive `t`, and collapse exactly `m(t)` aligned edges to their endpoint chord.  Stage E does **not** deploy this operator on the square corpus or any holdout.

Still open: a universal corner generator and any theorem extending this straight-edge operator to arbitrary non-straight shape boundaries.
