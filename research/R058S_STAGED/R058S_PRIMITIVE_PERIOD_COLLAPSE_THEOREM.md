# R058S Primitive-Period Collapse Theorem

Researcher-ID: `EM-R058S-7C91E4`  
Generation: `RS-R058S-EXACT-SQUARE-COLLAPSE-GRAMMAR-DISCOVERY`  
Stage: `D`  
Taskbook source: `95bb81abb49511ff92a610421d106579f76cc7ff`

Epistemic status: **PROOF / EXACT STRUCTURAL ANALYSIS**. No fit, optimizer, new grammar, holdout, or new square prediction is used here.

## 1. Abstract periodic-path theorem

Let `(v_i)_{i\in\mathbb Z}` be an ordered polygonal path in a real Euclidean vector space. Let `m>=1` and let `t != 0` satisfy

`v_(i+m) = v_i + t` for every integer `i`.

Define the `k`-edge whole-chord packet length

`C_k(i) = ||v_(i+k)-v_i||`,

and define the frozen all-period estimator over one fundamental edge period by

`Lhat_(m,k) = (1/k) * sum_(i=0)^(m-1) C_k(i)`.

### Theorem D1.A — period-multiple exactness

For every integer `q>=1`, if `k=q m`, then

`v_(i+q m)=v_i+q t`,

so

`C_(q m)(i)=q ||t||` for every `i`. Therefore

`Lhat_(m,qm) = (1/(qm)) * m * q ||t|| = ||t||`.

This is an exact identity. It uses only translation periodicity and positive homogeneity of the norm. It is a sufficient condition for exactness.

**Status:** `PRIMITIVE_PERIOD_WHOLE_CHORD_THEOREM_PROVED`.

### Theorem D1.B — universal lower bound and exact equality criterion

Write `e_i=v_(i+1)-v_i`. Translation periodicity gives `e_(i+m)=e_i` and `sum_(i=0)^(m-1)e_i=t`.
For arbitrary `k>=1`, put `D_i(k)=v_(i+k)-v_i`. Then

`sum_(i=0)^(m-1) D_i(k)`
`= sum_(r=0)^(k-1) sum_(i=0)^(m-1) e_(i+r)`
`= k t`.

Hence the triangle inequality gives

`Lhat_(m,k) = (1/k) sum_i ||D_i(k)|| >= (1/k)||sum_i D_i(k)|| = ||t||`.

For the Euclidean norm, equality holds exactly when all nonzero vectors `D_i(k)` lie on the same nonnegative ray as `t` (zero vectors are harmless). Thus `m|k` forces equality because then every `D_i(k)=q t`, but equality can also occur without divisibility.

This theorem explains why a periodic whole-chord density can be exact or positively biased, but cannot be below the translation density.

## 2. Carrier specialization

For the frozen Stage-C triangular-lattice/Voronoi straight boundary, one primitive digital boundary cycle has `m` exposed Voronoi edges and lattice translation vector `t`. Stage C exactly verified

`v_(i+m)=v_i+t`

and the frozen physical squared translation length is

`Q(t)=t_a^2+t_a t_b+t_b^2`.

Therefore `||t||=sqrt(Q(t))` in the frozen physical units. Applying Theorem D1.A gives, for every symbolic integer `q>=1`,

`Lhat_(m,qm)=sqrt(Q(t))`.

No decimal comparison is involved; equality is in the same exact radical semantics frozen in Stage C.

**Status:** `STRAIGHT_EDGE_BULK_EXACT_AFTER_PERIOD_COLLAPSE`.

The eight frozen discovery tangent classes specialize as follows:

| Tangent | m | translation t | Q(t) |
|---|---:|---|---:|
| T1 | 2 | `(1, 0)` | 1 |
| T2 | 4 | `(-1, 2)` | 3 |
| T3 | 8 | `(3, 1)` | 13 |
| T4 | 14 | `(-5, 7)` | 39 |
| T5 | 6 | `(2, 1)` | 7 |
| T6 | 10 | `(-4, 5)` | 21 |
| T7 | 10 | `(3, 2)` | 19 |
| T8 | 16 | `(-7, 8)` | 57 |


## 3. Frozen Stage-C finite consistency evidence

The Stage-C frozen range contains only `k=2..8`. Its 56 `(k,tangent)` pairs contain exactly these eight exact-density cases:

`(2,T1), (4,T1), (4,T2), (6,T1), (6,T5), (8,T1), (8,T2), (8,T3)`.

For the frozen primitive edge counts `m=(2,4,8,14,6,10,10,16)`, those eight and only those eight satisfy `m|k`. The complete 56-row byte-frozen audit is in `R058S_PERIOD_DIVISIBILITY_CONSISTENCY_AUDIT.json`.

**Finite status:** `STAGE_C_EXACTNESS_MATCHES_PERIOD_DIVISIBILITY_ON_FROZEN_56_PAIRS`.

This finite agreement is a consistency check of Theorem D1.A. It is **not** evidence for the abstract converse.

## 4. Minimality and converse audit

### Stage-C primitive `m` is minimal in the translational-period sense

For every frozen tangent class, Stage C certified that its translation vector is a primitive generator (up to sign) of the integer kernel of the half-plane normal and that the quotient boundary cycle contains exactly `m` distinct exposed-edge orbits. Stage D additionally checks the frozen direction word itself: for every proper `1<=r<m`, cyclic shift by `r` changes the word. Hence its least positive edge-word period is exactly `m`. Any translational period `v_(i+r)=v_i+t'` would force the edge increments to have period `r`; therefore no positive `r<m` exists.

Thus the Stage-C `m` values are minimal positive **edge/translational periods** of the frozen straight-boundary lifts.

### The abstract converse is false

Take a one-dimensional Euclidean path with alternating positive steps of lengths `1` and `2`:

`v_(2j)=3j`, `v_(2j+1)=3j+1`.

Then `v_(i+2)=v_i+3`, so `m=2`, `t=3`; period `1` is impossible because consecutive increments alternate between `1` and `2`, hence `m=2` is minimal. But for `k=1`,

`Lhat_(2,1)=|v_1-v_0|+|v_2-v_1|=1+2=3=|t|`,

while `2` does not divide `1`.

So the general converse `Lhat=||t|| => m|k` is false.

The exact replacement is Theorem D1.B: equality is equivalent to all `k`-step chord vectors sharing the nonnegative ray of `t`.

## 5. What is proved and what is not

**Proved**

- `PRIMITIVE_PERIOD_WHOLE_CHORD_THEOREM_PROVED`.
- `STRAIGHT_EDGE_BULK_EXACT_AFTER_PERIOD_COLLAPSE` for the frozen straight carrier.
- Stage-C primitive `m` is minimal in the translational-period sense.
- General whole-chord periodic density satisfies `Lhat>=||t||` with the exact Euclidean equality criterion above.
- The abstract converse `rho=1 => m|k` is false.

**Frozen finite evidence**

- `STAGE_C_EXACTNESS_MATCHES_PERIOD_DIVISIBILITY_ON_FROZEN_56_PAIRS`.

**Proposal only; not deployed**

- `POST_STAGE_C_PRIMITIVE_PERIOD_COLLAPSE_OPERATOR_PROPOSAL`: identify aligned complete primitive periods on a finite straight side and collapse each complete period to its endpoint chord, leaving only finite tails/corner layers unresolved.

**Still open**

- a universal finite corner grammar;
- any deployment of symbolic `k=q m` above the frozen empirical `K<=8` range;
- holdout transfer.
