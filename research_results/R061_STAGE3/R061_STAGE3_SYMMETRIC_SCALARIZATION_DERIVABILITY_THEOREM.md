# R061 Stage 3 — Symmetric Scalarization Derivability

Researcher-ID: `EM-R061S3-2F9622`

## General construction lemma

Let `ell` be the frozen Stage 2 directed line gauge. For points `X,Y` define

`v(X,Y)=(ell(X->Y), ell(Y->X)) in R_+^2`.

Let `Phi` be any norm on `R^2` satisfying coordinate-swap symmetry `Phi(x,y)=Phi(y,x)` and componentwise monotonicity on `R_+^2`.

Then

`d_Phi(X,Y)=Phi(v(X,Y))`

is a symmetric metric.

### Proof

Stage 2 gives both directed triangle inequalities:

`ell(X->Z) <= ell(X->Y)+ell(Y->Z)`

and

`ell(Z->X) <= ell(Z->Y)+ell(Y->X)`.

Therefore componentwise `v(X,Z) <= v(X,Y)+v(Y,Z)`. Monotonicity followed by the norm triangle inequality gives

`Phi(v(X,Z)) <= Phi(v(X,Y)+v(Y,Z)) <= Phi(v(X,Y))+Phi(v(Y,Z))`.

Swap symmetry gives endpoint symmetry, and positivity follows because both directed gauges vanish simultaneously only at equal endpoints. No carrier Euclidean metric is used.

## Concrete valid symmetric metrics

The following are exact metrics: `d_max=max(ell_f,ell_r)`; `d_sum=ell_f+ell_r`; `d_mean=(ell_f+ell_r)/2`; `d_2=sqrt(ell_f^2+ell_r^2)`; more generally every `l_p`, `p>=1`, and every other symmetric monotone norm.

These are classification constructions, not native canonical promotions.

## Nonuniqueness survives unit calibration

Normalize two valid metrics so the positive-axis unit segment has scalar value `1`:

`d_max^u = d_max/sqrt(2)`

and

`d_2^u = d_2/sqrt(3)`.

Both remain symmetric, translation invariant, homogeneous metrics.

On the reversal-symmetric segment `D=(2,1,0)`, whose spectrum is `{sqrt(5),sqrt(5)}`,

`(d_max^u)^2 = 5/2`

while

`(d_2^u)^2 = 10/3`.

Since `5/2 != 10/3`, even metric axioms + translation invariance + homogeneity + unit calibration do not select a unique scalar.

## Derivability verdict

The frozen Enterprise structure forces the bidirectional trace pair and bidirectional length spectrum. It does not contain a norm `Phi` on that two-entry spectrum, nor an invariant principle selecting one.

`MULTIPLE_SYMMETRIC_METRICS_EXIST_BUT_NONE_IS_CANONICALLY_DERIVED = true`.

`CANONICAL_SYMMETRIC_NATIVE_METRIC_DERIVED = false`.

The valid scalar metrics above are `CONDITIONAL_DERIVED` on an added scalarization choice.
