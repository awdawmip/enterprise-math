# BRC N=4/S23: an asymmetric rational box with a strictly positive convex-hull Chebyshev gap

Date 2026-11-01. AUTHOR_ANALYTIC_PROOF / EXACT_QUADRATIC_EXECUTED / UNREVIEWED / NOT_ADMITTED. Continuation of the UNREVIEWED predecessor `enterprise-math@30bdb16507881b9ed0fd4d97a12c804b8c672ebb` (PR #1765). This is the model-local *joint* six-preparation observable, not six independently adjustable centers.

## Exact lawful statistical model

Retain the six distinct BRC positive-source labels `AU0,AU1,AV,BU0,BU1,BV`, the four-stop law `F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c))` and the positive mixing matrix `20M` with rows `(10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)`. The second-stage parameter `b_U` is the SAME legal control on the A and B branches.

As previously, fix `a_B=1/4,b_AV=0,b_BV=1/3` and `c_AU0=c_AU1=c_BU0=c_BU1=c_BV=1/2`. The three remaining legal controls `(a,b,c)=(a_A,b_U,c_AV)` vary over the **asymmetric rational box** `Q=[1/2,7/8] x [1/8,1/2] x [1/2,7/8]`.

Six prepared probability laws, with the original source identities retained, are:

- `AU0=AU1=(a,(1-a)b,(1-a)(1-b)/2,(1-a)(1-b)/2)`;
- `AV=(a,0,(1-a)c,(1-a)(1-c))`;
- `BU0=BU1=(1/4,3b/4,3(1-b)/8,3(1-b)/8)`;
- `BV=(1/4,1/4,1/4,1/4)`.

These row equalities are induced by the *displayed freezes*, not an unrestricted source-merging license. For two six-row observations set `D(P,Q)=max_i TV(P_i,Q_i)` with `TV(p,q)=sum_t |p_t-q_t|/2`. Then

`R_lawful=min_{z in Q} max_{theta in Q}D(P(theta),P(z))`,
`R_hull=min_{V in conv(P(Q))} max_{theta in Q}D(P(theta),V)`.

## Theorem: strict positive gap and irrational lawful optimum

Over **all real parameters** in Q,

`R_hull=3/16`,
`R_lawful=(sqrt(43)-5)/8=:r*`,
`R_lawful-R_hull=(2sqrt(43)-13)/16>0`.

This is a rational-box counterexample to universal exactness of the joint convex-hull Chebyshev relaxation: the symmetric three-control box in the preceding proof is nonconvex yet has zero gap, whereas this asymmetric box has a strictly positive gap.

### Convex-hull lower bound and exact rational upper witness

The AV outcome 1 probability equals a, and its extreme values `1/2` and `7/8` force radius at least half their separation, `3/16`, for **any** center.

A *single joint* convex combination of four complete lawful strategy observations attains this bound:

`V=(4/9)P(1/2,1/8,7/8)+(1/18)P(1/2,1/2,1/2)+(2/9)P(7/8,1/8,7/8)+(5/18)P(7/8,1/2,1/2)`.

The weights sum to one and the resulting rows are

`V_AU=(11/16,1/16,1/8,1/8)`,
`V_AV=(11/16,0,1/4,1/16)`,
`V_BU=(1/4,3/16,9/32,9/32)`,
`V_BV=(1/4,1/4,1/4,1/4)`.

For any two three-atom probability laws TV equals the maximum absolute singleton-coordinate difference. AU has two equal tail atoms and their sum can be treated as one; its three effective coordinate ranges on the entire real box are `a:[1/2,7/8]`, `(1-a)b:[1/64,1/4]`, `(1-a)(1-b):[1/16,7/16]`. Against V their maximum absolute errors are `3/16` each. For AV, the ranges `a:[1/2,7/8]`, `(1-a)c:[1/16,7/16]`, `(1-a)(1-c):[1/64,1/4]` yield exactly the same bounds. BU's risk is `(3/4)|b-1/4|<=3/16`, BV remains fixed. Thus `R_hull=3/16` for every real strategy.

V itself is not lawful: its AV first atom forces `a=11/16` and BU second atom forces `b=1/4`; then lawful AU stage-2 mass would be `(1-a)b=5/64`, whereas V requires `1/16=4/64`, a discrepancy `1/64`. Nonrepresentability alone would not prove a *radius* gap; the next bound does.

### Analytic universal lower certificate for lawful centers

Let `z=(x,y,t)` be any legal center and r its worst six-row TV risk. Three valid observer-event inequalities are

(1) AV first atom at `a=7/8`: `r>=7/8-x`;

(2) AU combined tail event {stops 3,4} at `a=1/2,b=1/8`: `r>=7/16-(1-x)(1-y)`;

(3) BU second atom at `b=1/2`: `r>=(3/4)(1/2-y)`.

The first and third imply `1-x<=1/8+r` and `1-y<=1/2+4r/3`. Since both factors are nonnegative, the second forces

`(1/8+r)(1/2+4r/3)>=7/16-r`,

or equivalently `32r^2+40r-9>=0`. This polynomial is strictly increasing on nonnegative r, with positive root `r*=(sqrt(43)-5)/8`, proving the universal lower bound.

### Constructive lawful center and real-continuum upper certificate

The polynomial has values `-3/8` at `r=3/16` and `7/25` at `r=1/5`, hence `3/16<r*<1/5`. Choose the explicitly legal controls

`x=7/8-r*=(12-sqrt(43))/8`,
`y=1/2-4r*/3=(8-sqrt(43))/6`,
`t=1/[4(1-x)]=2(sqrt(43)+4)/27`.

That rational enclosure proves `x∈[1/2,7/8],y∈[1/8,1/2],t∈[1/2,7/8]`. The quadratic identity gives exact center coordinates

`(1-x)y=2r*-5/16`,
`(1-x)(1-y)=7/16-r*`,
`(1-x)t=1/4`,
`(1-x)(1-t)=r*-1/8`.

For AU the three effective event differences are <=r* uniformly: its first coordinate lies in `[1/2,7/8]` against x, with max error `max(r*,3/8-r*)=r*`; its stage-2 coordinate lies in `[1/64,1/4]` against `2r*-5/16`, with endpoint errors `2r*-21/64<=r*` and `9/16-2r*<=r*`; its grouped tail lies in `[1/16,7/16]` against `7/16-r*`, with errors `3/8-r*<=r*` and `r*`.

For AV the first-coordinate error is the same; time 3 lies in `[1/16,7/16]` around center `1/4` (maximum error `3/16<r*`), and time 4 lies in `[1/64,1/4]` around center `r*-1/8`, with endpoint errors `r*-9/64<=r*` and `3/8-r*<=r*`. BU risk over the whole b interval is `max(r*,9/32-r*)=r*`; BV is unchanged. Therefore each of the six TV risks is <=r* for **all real** `(a,b,c)∈Q`. The lower certificate makes this sharp.

Finally `2sqrt(43)>13` follows by squaring positive quantities, `172>169`, proving a strict gap without floating-point inference. Equality in the lower chain fixes x and y for any lawful minimizer; no uniqueness claim is made for t.

## Actual evidence, admission and transfer boundary

`VERIFY.py` was actually executed with Python standard-library exact `Fraction` arithmetic in `Q(sqrt(43))`, including exact order comparisons. It checks all eight legal vertices and their 48 prepared rows for **both** centers, exact convex weights and joint rows, polynomial identity and the `1/64` nonlawfulness witness. `RUN_EVIDENCE.json` is the actual stdout. The complete real-continuum theorem rests on the above event inequalities/range reasoning, **not** on finite sampling.

This result is confined to positive-source BRC/S23 finite statistics. It proves no native P000 six-axis Cell geometry, independent time, three-dimensional slice, signed-phase relation, future-operation fidelity, S2 causal-information transfer or physics claim. It does not change the full ten-decoder minimax bounds `1/2<=R_beh(k,10)<=2/3` for k=4,6. No native CLAIM/Result, independent mathematical review or project admission was obtained. See `SOURCES.md` and `NEXT_TASK.md` for precise research inheritance.
