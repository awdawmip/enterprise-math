# R059D Stage AN — BRC Pushforward Measure and Persistent Distortion Proof

Researcher-ID: `EM-R059D-AN-4C2B91`

Task-ID: `RS-R059D-STAGE-AN-BRC-PUSHFORWARD-MEASURE-PERSISTENT-DISTORTION`

Status: `THEOREM_PACKET_FROZEN_BEFORE_REPLAY`

## 1. Typed measure carrier

Stage AM already freezes the canonical radial-incidence BRC closed-fiber relation from the orthogonal continuous source circle to the AL canonical Enterprise target elementary turns. Let

`E_r={e_0,...,e_(T_r-1)}`

be that fixed target cycle, where AK/AL prove `T_r=C_E(r)`.

Define native counting measure

`nu_r({e_k})=1`.

Define source pushforward atom

`mu_r({e_k})=Arc_perp(F_(r,k))`.

AM proves the closed fibers cover the source circle, their interiors are disjoint, and only neighboring boundary rays overlap. Boundary rays have zero source arc measure. Hence the closed-fiber relation induces an unambiguous atomic pushforward measure and

`sum_k mu_r({e_k})=Circ_perp(r)`.

If `Delta_(r,k)` is the source angular width, source radius is `r`, so

`w_(r,k):=mu_r({e_k})=r*Delta_(r,k)`.

Thus the same target cycle carries two distinct measures: source pushforward `mu_r` and native counting `nu_r`.

## 2. Weighted and unweighted circumference

Finite additivity gives exactly

`Circ_perp(r)=sum_k w_(r,k)`.

Native circumference is the turn period,

`C_E(r)=T_r=sum_k 1`.

Let the source-typed circumference/diameter constant be `kappa_perp`, so on the accepted orthogonal source realization

`Circ_perp(r)=2*kappa_perp*r`.

Therefore

`bar_w_r := Circ_perp(r)/T_r = 2*kappa_perp*r/T_r`.

Since AI/AL give

`T_r/(2r)->kappa_E`, `kappa_E^2=12`, `kappa_E>0`,

we get

`bar_w_r -> kappa_perp/kappa_E`.

No equality between `kappa_perp` and `kappa_E` is assumed or derived.

## 3. Exact local source-angle formula

Use the source compatibility embedding with basis vectors

`u=(1,0)`, `v=(1/2,sqrt(3)/2)`.

For consecutive target rays `p=(a,b)` and `q=(c,d)`, source dot and oriented area are

`2<p,q>=2ac+2bd+ad+bc`,

`2 det(p,q)=sqrt(3)(ad-bc)`.

Hence

`tan Delta = sqrt(3)(ad-bc)/(2ac+2bd+ad+bc)`.

For `Q=a^2+ab+b^2`, the three primitive turn symbols give

- symbol 1: `tan Delta=sqrt(3)*a/(2Q+a+2b)`;
- symbol 2: `tan Delta=sqrt(3)*(a+b)/(2Q-a+b)`;
- symbol 3: `tan Delta=sqrt(3)*b/(2Q-2a-b)`.

These formulas are source-side comparison geometry only. They never enter target selection.

## 4. Sharp proportionality classification

Proportionality `mu_r=lambda*nu_r` means every target turn has the same source arc width.

### r=1

The target cycle consists of the six D6 axis turns. The source circle is partitioned into six equal sector arcs, so all weights are equal.

### r=2

A canonical sector has rays

`(2,0),(1,1),(0,2)`.

The middle ray is the source sector bisector. Reflection therefore makes the two sector fibers equal, and D6 transports this around the circle. Thus all twelve weights are equal.

### r=3

The canonical sector word is `222`. For the first two turns,

`tan Delta_0/sqrt(3)=1/5`,

`tan Delta_1/sqrt(3)=3/13`.

They are unequal.

### r=4

The canonical sector word is `2222`. For the first two turns,

`tan Delta_0/sqrt(3)=1/7`,

`tan Delta_1/sqrt(3)=1/6`.

They are unequal.

### Every r>=5

AK/AH begin at `(a,b,rho)=(r,0,-4)`. Therefore the first turn is symbol 2. Its residual update gives

`rho_1=-4+3(r-3)=3r-13`.

For every `r>=5`, `rho_1>0`, so the second turn is symbol 1.

The first fiber has

`tan Delta_0/sqrt(3)=1/(2r-1)`.

The second turn starts at `(r-1,1)` and is symbol 1, hence

`tan Delta_1/sqrt(3)=(r-1)/(2r^2-r+3)`.

Equality would require

`(r-1)(2r-1)=2r^2-r+3`,

which simplifies to `r=-1`.

Thus the two weights are unequal for every positive `r`, in particular every `r>=5`.

Combining all cases gives the sharp theorem

`mu_r proportional to nu_r iff r in {1,2}`.

## 5. Axis refinement limit

For the first turn `(r,0)->(r-1,1)`,

`tan Delta_axis(r)=sqrt(3)/(2r-1)`.

Therefore

`r tan Delta_axis(r)->sqrt(3)/2`.

Since `Delta_axis(r)->0` and `tan x/x->1` on the source analytic side,

`r Delta_axis(r)->sqrt(3)/2`.

Thus

`w_axis(r)->sqrt(3)/2`.

## 6. Canonical central-turn sequence

AH constructs the sector word as a left half over `{1,2}`, an optional center symbol 2, and its reflected right half.

Let `M_N(r)=r+J_N(r)`.

All `J_N(r)` symbol-1 events lie in the left half, so once the left half reaches its terminal central turn, its coordinate sum is

`m=a+b=M_N(r)`.

The left recurrence stops with `a-b` equal to 0 or 1.

- If it stops at difference 1, the optional center is symbol 2; choose it. Its start has `d=a-b=1`.
- If it reaches difference 0, the final left-half move must have been symbol 2 from difference 2 to difference 0; choose that move. Its start has `d=2`.

Thus for every radius there is a canonical central symbol-2 turn whose start satisfies

`m=a+b=M_N(r)`, `d=a-b in {1,2}`.

For a symbol-2 turn,

`tan Delta_mid(r)=2sqrt(3)m/(3m^2+d^2-2d)`.

AG gives

`M_N(r)/r -> beta=1+alpha`,

where `3beta^2=4`, `beta>0`. On the source compatibility side this may be displayed as `beta=2/sqrt(3)`.

Since `d` is bounded,

`a/r=(m+d)/(2r)->1/sqrt(3)`,

`b/r=(m-d)/(2r)->1/sqrt(3)`.

Then

`r tan Delta_mid(r)->1`.

Again `Delta_mid(r)->0`, so

`w_mid(r)=r Delta_mid(r)->1`.

## 7. Persistent two-limit distortion

The two canonical limits are

`w_axis -> sqrt(3)/2`,

`w_mid -> 1`.

They differ because `sqrt(3)<2`, equivalently `3<4`.

Therefore the local source pushforward weights do not converge uniformly to one constant.

More strongly, no scalar sequence `lambda_r` can make

`sup_k |w_(r,k)-lambda_r| -> 0`.

Otherwise both the axis and central weights would have asymptotically the same value, contradicting their distinct limits.

This proves persistent metric distortion under radial refinement.

## 8. Defect field

Define

`d_(r,k)=w_(r,k)-bar_w_r`.

Then exactly

`sum_k d_(r,k)=0`.

AM D6 equivariance and reflection imply the defect field is D6-periodic around sectors and reflection-symmetric under reversal.

As `r->infinity`,

`d_axis -> sqrt(3)/2-kappa_perp/kappa_E`,

`d_mid -> 1-kappa_perp/kappa_E`,

and therefore

`d_mid-d_axis -> 1-sqrt(3)/2 >0`.

A positive limiting mean-square variance is not claimed: two distinguished subsequences alone do not prove a positive-density defect set.

## 9. Global renormalization no-go

The only radius-global factor matching total source circumference is

`lambda_r=bar_w_r=Circ_perp(r)/T_r`.

For every `r>=3`, sharp nonproportionality gives at least one turn with `w_(r,k)!=lambda_r`.

Persistent two-limit distortion proves a stronger asymptotic no-go: even allowing an arbitrary radius-dependent scalar cannot make all local weights uniformly equal.

Thus `GLOBAL_MEAN_CONVERSION_FACTOR` is a valid statistic, but `LOCAL_METRIC_ISOMETRY` remains false at every `r>=3` and does not emerge under refinement.

## 10. Semantic firewall

Nothing in this stage changes the target orbit. AL canonicality remains fixed before source weights are evaluated. Source-side square roots, angles and source circumference are compatibility-layer quantities only. `kappa_perp` remains source typed; `kappa_E` remains target native. No claim about standard real pi is added.

## Terminal theorem

The strongest justified disposition is

`BRC_PUSHFORWARD_MEASURE_DECOMPOSITION_PROVED__PERSISTENT_TWO_LIMIT_DISTORTION_ESTABLISHED`.

In addition, the sharper finite-radius theorem

`mu_r proportional to nu_r iff r in {1,2}`

is proved for all integer radii.
