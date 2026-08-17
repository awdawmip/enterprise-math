# R059D Stage AG — Proof of the N Beatty/Sturmian Jump Law

Researcher-ID: `EM-R059D-AG-8C2E47`  
Task-ID: `RS-R059D-STAGE-AG-N-BEATTY-PROOF-STURMIAN-JUMP-LAW`  
Taskbook source: `f1dcbd5d26b79be6dc8b2f495c81266a1c41ce9f`  
Frozen source main: `fb5b7880e469c8e16769cf55601da15bb5f96b4f`  
Accepted AF owner head: `9e863cfc89cab71118959deb38187a21fe1e96e1`

## Theorem

Let `J_N(r)` be the N-resolver boundary-excess count frozen by AF. Let `alpha` be the unique positive root of

`3 alpha^2 + 6 alpha - 1 = 0`.

Then for every integer `r>=0`,

`J_N(r) = floor(alpha*r + 1/3)`.

Consequently the jump word `s_r=J_N(r)-J_N(r-1)` is the lower mechanical word of irrational slope `alpha` and intercept `1/3`, hence a Sturmian word. The first radius at which `J_N=m` is

`r_m = ceil((m-1/3)/alpha)`,

and every jump gap is `6` or `7`.

The proof starts from the frozen N resolver and dual-edge support semantics; no classical circle equation, pi, Euclidean curvature, or runtime square root is used.

---

## Lemma AG-L1a — exact dual-vertex support criterion

Write

`q(a,b)=a^2+ab+b^2`.

For an elementary N triangle, use the frozen centroid numerators

- `UP(a,b): (3a+1,3b+1)`,
- `DOWN(a,b): (3a+2,3b+2)`,

and occupancy criterion `q(A,B)<=9r^2`.

A lattice vertex `p=(a,b)` belongs to the edge-supported dual carrier iff at least one of its six incident lattice edges has both incident triangles occupied.

In the canonical first sector `a,b>=0`, put `Q=9q(a,b)`. For the six incident edge directions, the maximum of the two incident centroid q-values is exactly

| edge direction | two-triangle support cost |
|---|---:|
| `+a` | `Q+9(a+b)+3` |
| `+b` | `Q+9(a+b)+3` |
| `-a+b` | `Q+9b+3` |
| `-a` | `Q-9a+3` |
| `-b` | `Q-9b+3` |
| `+a-b` | `Q+9a+3` |

Therefore the minimum possible support cost is

`G(a,b)=Q-9 max(a,b)+3`.

Hence

`p in S_N(r)`

iff

`3q(a,b)-3 max(a,b)+1 <= 3r^2`.                                      (1)

This is an exact integer criterion derived from the N centroid rule.

---

## Lemma AG-L1b — J is the maximum shell excess

Let the sector shell coordinate be

`m=a+b`.

AF proved that the one-sector N boundary word is a Motzkin excursion under the height update

`1 -> +1`, `2 -> 0`, `3 -> -1`

with `#1=#3=J_N(r)`.

The same height is geometrically

`h=a+b-r`.

It remains to show that all `+1` steps occur before all `-1` steps.

In the half-sector `a>=b`, define

`Phi(a,b)=q(a,b)-a+1/3`.

By (1), `Phi<=r^2` is the selection condition there. For fixed `a`,

`Phi(a,b+1)-Phi(a,b)=a+2b+1>0`,                                   (2)

so selected vertices in each column form an initial interval and the outer boundary is its upper envelope.

If `a-b>=2`, then

`Phi(a-1,b+1)-Phi(a,b)=2-(a-b)<=0`.                               (3)

Thus whenever a selected boundary vertex lies strictly before the bisector, the diagonal successor `(a-1,b+1)` is also selected. The upper envelope therefore cannot take a `-a`-only boundary step there. By reflection `a<->b`, after the bisector it cannot take a `+b`-only step.

Hence every Motzkin `+1` occurs before every Motzkin `-1`. Therefore the maximum Motzkin height is exactly the total number of up steps:

`max h = J_N(r)`.

Since `h=a+b-r`, if

`M_r=max{a+b : (a,b) in S_N(r), a,b>=0}`,

then

`M_r-r=J_N(r)`.                                                    (4)

---

## Lemma AG-L1c — exact shell criterion

Fix an integer shell `m=a+b`. By symmetry assume `a>=b`, so `a>=ceil(m/2)` and `b=m-a`.

From (1), shell selection is controlled by

`f_m(a)=q(a,m-a)-a=a^2-(m+1)a+m^2`.

Its first difference is

`f_m(a+1)-f_m(a)=2a-m`.                                           (5)

### Odd shell

If `m=2k+1`, the unique integer minimum is at `(a,b)=(k+1,k)` and

`min f_m = 3k^2+2k`.

The shell exists iff

`3(3k^2+2k)+1 <= 3r^2`,

i.e.

`(3k+1)^2 <= 3r^2`,

equivalently

`(3m-1)^2 <= 12r^2`.                                              (6)

### Even shell

If `m=2k`, the two integer minima occur at `(k,k)` and `(k+1,k-1)` and

`min f_m = 3k^2-k`.

The exact condition is

`9k^2-3k+1 <= 3r^2`.                                              (7)

The putative uniform square condition is

`(6k-1)^2 <= 12r^2`,

equivalently

`9k^2-3k+1/4 <= 3r^2`.                                           (8)

Let

`N=3r^2-9k^2+3k`, an integer.

Condition (7) is `N>=1`; condition (8) is `N>=1/4`. Since `N` is integral, these are equivalent.

Therefore for every integer `m>=0`:

**Shell theorem**

`m occurs in S_N(r)  <=>  (3m-1)^2 <= 12r^2`.                    (9)

---

## Lemma AG-L2 — quadratic threshold

Let `beta` be the positive root of

`3 beta^2 - 4 = 0`.

Both sides in (9) have fixed sign at the maximal positive shell, so (9) is equivalent to

`3m-1 <= 3 beta r`,

hence

`m <= beta r + 1/3`.                                              (10)

Therefore

`M_r=floor(beta r+1/3)`.                                          (11)

Put

`alpha=beta-1`.

Substitution into `3 beta^2-4=0` gives

`3 alpha^2+6 alpha-1=0`.

The polynomial is negative at `0` and positive at `1`, so the positive root obeys `0<alpha<1`. Its discriminant is `48`, not a rational square, so `alpha` is irrational.

---

## Lemma AG-L3 — Beatty floor theorem

Combining (4) and (11),

`J_N(r)=M_r-r`

`=floor((1+alpha)r+1/3)-r`

`=floor(alpha r+1/3)`,

because `r` is integral.

Thus the theorem holds for every integer `r>=0`.

### Independent induction/event form

Let `j=J_N(r-1)`. A new up/down Motzkin pair appears at radius `r` iff shell

`m=r+j+1`

is selected. By (9), this is

`(3r+3j+2)^2 <= 12r^2`,                                          (12)

or

`(3j+2)^2 + 6r(3j+2) - 3r^2 <=0`.                               (13)

Let `y=3alpha`. The polynomial for alpha gives

`y^2+6y-3=0`.

For nonnegative `x`, `x^2+6rx-3r^2` is strictly increasing, and its positive root is `3alpha r`. Hence (13) is exactly

`3j+2 <= 3alpha r`.                                               (14)

Since `0<alpha<1`, the floor can increase by at most one per radius, and (14) is precisely the condition

`floor(alpha r+1/3)=j+1`.

This proves the AF integer recurrence for all radii, independently of any finite lookup.

---

## Lemma AG-L4 — exact jump positions

For `m>=1`, define

`r_m=min{r : J_N(r)=m}`.

The floor theorem gives

`J_N(r)>=m <=> alpha r+1/3 >= m`.

Therefore

`r_m=ceil((m-1/3)/alpha)`.                                       (15)

Let `lambda=1/alpha`. Dividing the minimal polynomial by `alpha^2` gives

`lambda^2-6lambda-3=0`.

Thus

`r_m=ceil(lambda(m-1/3))`.                                        (16)

No tie is possible: if the ceiling argument were integral then alpha would be rational.

---

## Lemma AG-L5 — gap alphabet

The polynomial `x^2-6x-3` is negative at `6` and positive at `7`, so

`6<lambda<7`.

Let `x_m=lambda(m-1/3)`. Then

`r_(m+1)-r_m = ceil(x_m+lambda)-ceil(x_m)`.

Because `x_m` is nonintegral and `6<lambda<7`, every gap is either `6` or `7`.

Both occur infinitely often: otherwise the average gap would tend to `6` or `7`, while from (16)

`r_m/m -> lambda`,

which is irrational and strictly between them.

---

## Lemma AG-L6 — exact mechanical/Sturmian word

Define for `r>=1`

`s_r=J_N(r)-J_N(r-1)`.

Then

`s_r=floor(alpha r+1/3)-floor(alpha(r-1)+1/3)`.                   (17)

With `n=r-1` and `rho=1/3`,

`w_n=floor((n+1)alpha+rho)-floor(n alpha+rho)`.

This is the **lower mechanical word** of slope `alpha` and intercept `rho=1/3`.

Because `0<alpha<1`, `w_n` is binary.

For any block of length `L` beginning at `k`,

`sum_(n=k)^(k+L-1) w_n`
`=floor((k+L)alpha+rho)-floor(k alpha+rho)`,

which is either `floor(L alpha)` or `ceil(L alpha)`. Thus any two equal-length blocks differ in their number of ones by at most one: the word is balanced.

Its limiting density of ones is `alpha`, which is irrational. A periodic binary word has rational density, so this word is aperiodic.

A binary infinite word is Sturmian iff it is balanced and aperiodic. Hence the N jump word is Sturmian.

Equivalent rotation coding:

`s_r=1`

iff

`{(r-1)alpha+1/3} >= 1-alpha`.

---

## Lemma AG-L7 — periodic continued fraction

Let `lambda=1/alpha`. From

`lambda^2-6lambda-3=0`

and `6<lambda<7`,

`lambda-6>0`.

The polynomial identity implies

`1/(lambda-6)=2+1/lambda`.

Therefore

`lambda = 6 + 1/(2+1/lambda)`,

so

`lambda=[overline{6,2}]`

and hence

`alpha=[0; overline{6,2}]`.

The convergents begin

`0/1, 1/6, 2/13, 13/84, 28/181, 181/1170, 390/2521, 2521/16296, ...`

and obey the standard recurrence with periodic partial quotients `6,2`.

This explains why AF's exact discovery interval was squeezed near convergents such as `13/84`; the continued fraction is a theorem consequence of the native quadratic threshold, not an imported fit.

---

## AG-L8 — substitution status

The periodic continued fraction gives an exact periodic S-adic directive for the slope. However Stage AG does not promote a single intercept-specific fixed substitution for the lower mechanical word with intercept `1/3`; that extra morphic conjugacy has not been proved here.

The exact forward generators already established are:

1. the lower mechanical-word formula (17), and
2. the integer-only recurrence (13).

Neither queries occupancy, a jump table, sqrt, or floating point at runtime.

---

## Motzkin consequences

AF proved

`#1=#3=J_N(r)`, `#2=r-J_N(r)`, `|W_r|=r+J_N(r)`.

Therefore AG upgrades these counts to

`#1=#3=floor(alpha r+1/3)`,

`#2=r-floor(alpha r+1/3)`,

`|W_r|=r+floor(alpha r+1/3)`.

As `r->infinity`:

`J_N(r)/r -> alpha`.

Relative to total word length, the exact limiting densities are

- symbol 1: `alpha/(1+alpha)`,
- symbol 3: `alpha/(1+alpha)`,
- symbol 2: `(1-alpha)/(1+alpha)`.

These are count results only. AF's counterexample remains binding: J does not determine B or the internal arrangement of W.

---

## C comparison

Only after the N theorem was established is C reconsidered. AF's frozen finite census through `r<=512` found that every N/C J disagreement was a one-radius `N at r -> C at r+1` delay.

Stage AG does not derive that rule from C semantics, so its status remains:

`FINITE_CENSUS_ONLY`.

It is not used anywhere in the N proof.

---

## Conclusion

All AG-L1 through AG-L7 are proved. AG-L8 is retained at the exact Sturmian/S-adic level without claiming an unproved fixed substitution.

Primary disposition:

`N_BEATTY_STURMIAN_JUMP_LAW_PROVED`.

`STOP_FOR_DRIVER_REVIEW`
