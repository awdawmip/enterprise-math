# R056 Stage B — Exact finite-local escape and minimality

Researcher-ID: `EM-R056-BEC623`

Generation: `R056`

Scope: Stage B only. Holdout remains closed.

## 1. Candidate family

For every integer `r>=7`, let

`u=(r,0)` and `v=(r-2,3)`,

and let

`C'= (H_r \ {u}) union {v}`.

We prove that this is an admissible `D(1,3)` strict descent.

### 1.1 `u` is an occupied boundary site

For `u=(r,0)`,

`max(|r|,0,|r+0|)=r`,

so `u in H_r`. Its nearest neighbor `(r+1,0)` is outside `H_r`, hence `u` is on the occupied boundary.

### 1.2 `v` is outside

For `v=(r-2,3)`,

`(r-2)+3=r+1`.

Therefore

`max(|r-2|,3,|r+1|)>=r+1>r`,

so `v notin H_r`.

### 1.3 Exact support diameter

`v-u=(-2,3)`, hence

`d_L(u,v)=max(2,3,|-2+3|)=3`.

Since this is a one-cell replacement, the changed-site support is `{u,v}`, so its support diameter is exactly `3`.

### 1.4 Connectivity

`H_r \ {u}` is connected. Indeed `d_L(0,x)` is the triangular-lattice graph distance. Every nonzero `x` has a nearest neighbor with graph distance one smaller. Starting from any `x != u` in `H_r`, repeatedly taking such an inward neighbor produces a path to `0`; after the first step from a radius-`r` point the radius is at most `r-1`, so the path cannot visit the removed point `u`, whose radius is `r`.

The new site `v` has, among others, the two nearest neighbors

`w_1=(r-3,3)` and `w_2=(r-2,2)`.

For `r>=7`,

`max(|r-3|,3,|r|)=r`

and

`max(|r-2|,2,|r|)=r`,

so `w_1,w_2 in H_r \ {u}`. Thus `v` attaches to the connected remainder, and `C'` is connected.

### 1.5 Hole-freeness

Let `E = Lambda \ H_r`. Every point of `E` has an infinite path staying in `E`: choose any violated support inequality among

`a>r`, `a<-r`, `b>r`, `b<-r`, `a+b>r`, `a+b<-r`

and repeatedly step in a nearest-neighbor direction that increases that violation. Hence `E` has no finite empty component.

The six neighbors of `v=(r-2,3)`, in cyclic nearest-neighbor order, are

`(r-1,3)`,
`(r-2,4)`,
`(r-3,4)`,
`(r-3,3)`,
`(r-2,2)`,
`(r-1,2)`.

The middle two `(r-3,3)` and `(r-2,2)` lie in `H_r`. The other four lie in `E`, because their `a+b` coordinate is respectively `r+2,r+2,r+1,r+1`. Those four exterior neighbors form one consecutive path around the neighbor cycle of `v`. Consequently any exterior path that used `v` can be rerouted locally around `v`; removing `v` from `E` creates no finite exterior component.

After deleting `u` from the occupied set, `u` becomes empty and is itself adjacent to `(r+1,0) in E\{v}`. Therefore

`Lambda \ C' = (E \ {v}) union {u}`

still has no finite empty component. Under the frozen R055/R056 topology convention, `C'` is hole-free.

### 1.6 Exact energy descent

`Q(u)=r^2`.

Also

`Q(v)=(r-2)^2+3(r-2)+9=r^2-r+7`.

Hence

`DeltaQsum=Q(v)-Q(u)=7-r`.

Moreover

`DeltaS=v-u=(-2,3)`

and

`Q(DeltaS)=4-6+9=7`.

Because `H_r` is centered, Stage A gives

`DeltaG=N_r*DeltaQsum-Q(DeltaS)`,

so exactly

`DeltaG=N_r*(7-r)-7`.

At `r=7`,

`DeltaQsum=0`,
`DeltaS=(-2,3)`,
`Q(DeltaS)=7`,
`DeltaG=-7<0`.

For every `r>=8`, `7-r<=-1`, hence

`DeltaG<=-N_r-7<0`.

Therefore the family is an admissible `D(1,3)` strict descent for every `r>=7`.

## 2. Target A is false

The claimed bounded-support obstruction said that for every fixed finite `(m,rho)` sufficiently large centered shells admit no strict descent. The fixed pair

`(m,rho)=(1,3)`

has a strict descent for every `r>=7`.

Therefore

`BOUNDED_SUPPORT_STRICT_DESCENT_OBSTRUCTION = FALSE`

by an exact infinite counterexample family.

## 3. Exact lower bound for every one-cell replacement with support at most 2

Let `u in H_r`, `v notin H_r`, and let `d=v-u` satisfy `d_L(0,d)<=2`.

The hexagon `H_r`, the quadratic form `Q`, and the graph metric are invariant under the dihedral symmetry `D6`. The nonzero displacements of graph length at most two split into exactly three `D6` orbits:

1. `d=(1,0)` with `d_L=1`, `Q(d)=1`;
2. `d=(2,0)` with `d_L=2`, `Q(d)=4`;
3. `d=(1,1)` with `d_L=2`, `Q(d)=3`.

It is therefore enough to treat these three representatives.

### Orbit 1: `d=(1,0)`

Write `u=(a,b)`. Then

`Q(u+d)-Q(u)=2a+b+1`.

Since only `a` and `a+b` increase, `v` can leave `H_r` only if either `a=r` or `a+b=r`.

If `a=r`, then `b>=-r`, so

`2a+b+1>=r+1`.

If `a+b=r`, then `b=r-a<=r` forces `a>=0`, so again

`2a+b+1=a+r+1>=r+1`.

Thus this orbit has increase at least `r+1`.

### Orbit 2: `d=(2,0)`

Now

`Q(u+d)-Q(u)=4a+2b+4`.

The point `v` can leave only if `a>=r-1` or `a+b>=r-1`.

If `a>=r-1`, then `b>=-r`, and

`4a+2b+4>=4(r-1)-2r+4=2r`.

If `s=a+b>=r-1`, then `b=s-a<=r` gives `a>=s-r>=-1`. Therefore

`4a+2b+4=2a+2s+4>=-2+2(r-1)+4=2r`.

Thus this orbit has increase at least `2r`.

### Orbit 3: `d=(1,1)`

Here

`Q(u+d)-Q(u)=3(a+b+1)`.

The point `v` can leave only if `a=r`, or `b=r`, or `a+b>=r-1`.

If `a+b>=r-1`, the increase is at least `3r`.

If `a=r`, then `b>=-r`, so `a+b>=0` and the increase is at least `3`. The case `b=r` is symmetric.

Hence this orbit has increase at least `3`.

Combining the three cases, for every `r>=7`,

**`Q(v)-Q(u) >= 3`.**

Thus the requested stronger inequality `DeltaQsum>=3` holds for every one-cell inside-to-outside replacement whose support diameter is at most two.

## 4. Exact law `rho_1(r)=3` for all `r>=7`

The family in Section 1 proves `rho_1(r)<=3`.

For a one-cell replacement with support diameter at most `2`, Section 3 gives

`DeltaQsum>=3`.

Stage A gives `Q(DeltaS)<=rho^2<=4`. Therefore

`DeltaG=N_r*DeltaQsum-Q(DeltaS)>=3N_r-4>0`.

Such a move cannot be a strict descent, irrespective of connectivity or hole-freeness.

Therefore

**`rho_1(r)=3` for every `r>=7`.**

## 5. No `rho<=2` cooperative strict descent for frozen `m<=3`

Let

`|U|=|V|=k<=3`

and

`diam_L(U union V)<=2`.

Choose any bijection `U={u_i}` to `V={v_i}`. Because every pair of changed sites is at distance at most two,

`d_L(u_i,v_i)<=2`.

Each `u_i` is in `H_r` and each `v_i` is outside, so Section 3 applies separately:

`Q(v_i)-Q(u_i)>=3`.

Summing,

`DeltaQsum>=3k`.

Stage A gives, for `rho<=2`,

`Q(DeltaS)<=k^2 rho^2<=4k^2`.

Hence on a centered shell

`DeltaG>=3k N_r-4k^2 = k(3N_r-4k)`.

For `r>=7`, `N_r>=169`, and for `1<=k<=3`,

`3N_r-4k >= 507-12 = 495 > 0`.

Therefore

**no support-diameter `rho<=2` strict descent exists for any `m in {1,2,3}` and any `r>=7`.**

This is a theorem-level exclusion; no cooperative subset enumeration is needed.

## 6. Minimality and classification

Within the frozen `m<=3` range:

- a one-cell move works with support diameter exactly `3`;
- no one-, two-, or three-cell move can work with support diameter at most `2`.

Therefore:

- minimal moved-cell count = `1`;
- minimal established support radius = `3`;
- no cooperative multi-cell move is required.

Primary classification:

**`FINITE_LOCAL_COOPERATIVE_ESCAPE_FOUND`.**

The strict holdout remains unopened. No `m`, `rho`, locality definition, Stage-0 artifact, or Stage-A artifact is modified.
