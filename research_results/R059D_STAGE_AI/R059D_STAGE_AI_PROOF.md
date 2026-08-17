# R059D Stage AI — Proof of the Algebraic Enterprise Circle Constant

Researcher-ID: `EM-R059D-AI-4F8C2D`  
Task-ID: `RS-R059D-STAGE-AI-ALGEBRAIC-ENTERPRISE-CIRCLE-CONSTANT`  
Taskbook source: `bd4afe69a3c81491c741c79689087835ed197221`  
Frozen source main: `6a0a07f43ede4d1df61525364269492fbc7ca631`

## Theorem

Let `alpha` be the unique positive root of

`3 alpha^2 + 6 alpha - 1 = 0`.

For the accepted N Enterprise circle, define

`kappa_E = lim_{r->infinity} C_N(r)/D_step(r)`

with `D_step(r)=2r`.

Then the limit exists and

`kappa_E^2=12`, `kappa_E>0`.

Equivalently, if `beta=1+alpha`, then `kappa_E=3 beta`.

This is a theorem about the frozen Enterprise N-circle count geometry. It is type-separated from the standard real constant `pi` of classical Euclidean/analytic circle definitions.

---

## AI-T1. Exact circumference and shell formula

AG proves for every integer `r>=0`

`J_N(r)=floor(alpha*r+1/3)`.

AH proves

`C_N(r)=6r+6J_N(r)=6|W_N(r)|`.

Therefore

`C_N(r)=6(r+floor(alpha*r+1/3))`.

Because `r` is integral,

`r+floor(alpha*r+1/3)=floor((1+alpha)r+1/3)`.

Put `beta=1+alpha`. Then

`C_N(r)/6 = floor(beta*r+1/3)`.

Define this integer as `M_r`.

AG also proves the exact maximal-shell criterion

`(3m-1)^2 <= 12r^2`.

There is one literal endpoint issue in the taskbook wording: for `r=0`, the set

`{m>=0 : (3m-1)^2<=0}`

is empty. Hence its maximum is not defined. The totalized shell theorem is therefore:

- `M_0:=0`;
- for `r>=1`, `M_r=max{m>=0 integer:(3m-1)^2<=12r^2}`.

Equivalently, for all `r>=0`,

`M_r=max({0} union {m>=1 integer:(3m-1)^2<=12r^2})`.

To see the equivalence for `r>=1`, first derive in AI-T2 below that `3 beta^2=4`. For every `m>=1`, both `3m-1` and `3 beta r` are positive, and

`(3m-1)^2 <= 12r^2`

iff

`(3m-1)^2 <= (3 beta r)^2`

iff

`3m-1 <= 3 beta r`

iff

`m <= beta*r+1/3`.

Thus the largest admissible integer is exactly

`floor(beta*r+1/3)=M_r`.

For `r>=1`, `m=0` also satisfies the literal threshold because `1<=12r^2`, so the totalized and literal versions coincide there.

Hence the exact shell readout is

`C_N(r)=6M_r`.

No square root is needed in the integer threshold implementation.

---

## AI-T2. Algebraic constant

Start only from the accepted AG polynomial

`3 alpha^2+6 alpha-1=0`.

Set `beta=1+alpha`, so `alpha=beta-1`. Substitution gives

`3(beta-1)^2+6(beta-1)-1=0`,

hence

`3 beta^2-4=0`.

AG gives `alpha>0`, so `beta>1>0`. Therefore `beta` is the positive root of `3x^2-4=0`.

Define

`kappa_E:=3 beta`.

Then

`kappa_E^2=9 beta^2=9*(4/3)=12`.

Also `kappa_E>0`.

The polynomial `x^2-12` is strictly increasing on positive `x`; equivalently a positive square has a unique positive square root. Hence `kappa_E` is the unique positive root of

`x^2-12=0`.

Only after this polynomial derivation may one write the conventional algebraic compatibility form `kappa_E=2*sqrt(3)`. That notation is not used by the canonical generator or certificate.

We also need irrationality for strict finite-radius bounds. If `alpha` were rational, the rational-root theorem applied to `3x^2+6x-1` would force `alpha` to be one of `±1, ±1/3`; direct substitution rejects all four. Thus `alpha` is irrational.

---

## AI-T3. Transition-span ratio and exact finite-radius error

Fix `r>=1` and define the floor slack

`delta_r := alpha*r+1/3-floor(alpha*r+1/3)`.

Since `alpha` is irrational and `r` is a nonzero integer, `alpha*r+1/3` is irrational. Therefore

`0<delta_r<1`.

Write

`J_N(r)=alpha*r+1/3-delta_r`.

Then

`C_N(r)=6r+6J_N(r)`

`=6(1+alpha)r+2-6delta_r`

`=6 beta r+2-6delta_r`

`=2 kappa_E r+2-6delta_r`.

For `D_step(r)=2r`, define

`R_step(r)=C_N(r)/(2r)`.

The exact error is

`R_step(r)-kappa_E=(1-3delta_r)/r`.

Because `0<delta_r<1`,

`-2 < 1-3delta_r < 1`,

so

`-2/r < R_step(r)-kappa_E < 1/r`.

Both bounding functions tend to zero. By squeezing,

`lim_{r->infinity} R_step(r)=kappa_E`.

This is an all-radius proof; no numerical convergence experiment is used.

---

## AI-T4. Endpoint-count convention robustness

The frozen dual-cell diameter count is

`D_cell(r)=2r+1`.

Thus

`R_cell(r)=C_N(r)/(2r+1)`.

Using `C_N(r)=2kappa_E*r+2-6delta_r`,

`R_cell(r)-kappa_E`

`=(2-kappa_E-6delta_r)/(2r+1)`.

Since `0<delta_r<1`,

`-4-kappa_E < 2-kappa_E-6delta_r < 2-kappa_E`.

Therefore

`(-4-kappa_E)/(2r+1) < R_cell(r)-kappa_E < (2-kappa_E)/(2r+1)`.

Since `beta>1`, `kappa_E=3beta>3`, so `2-kappa_E<0`; in particular the cell-count ratio approaches the limit from below. Both endpoints of the displayed interval tend to zero, hence

`lim R_cell(r)=kappa_E`.

More generally fix any integer `epsilon`. For all sufficiently large `r` with `2r+epsilon>0`, define

`R_epsilon(r)=C_N(r)/(2r+epsilon)`.

Then exactly

`R_epsilon(r)-kappa_E`

`=(2-kappa_E*epsilon-6delta_r)/(2r+epsilon)`.

Consequently

`(-4-kappa_E*epsilon)/(2r+epsilon)`

`< R_epsilon(r)-kappa_E`

`< (2-kappa_E*epsilon)/(2r+epsilon)`.

The numerator bounds are constants depending only on fixed `epsilon`, while the denominator diverges. Therefore

`lim R_epsilon(r)=kappa_E`.

Thus the native constant is not an artifact of choosing endpoint cells versus transition span, nor of any other fixed bounded endpoint correction.

A purely rational coarse bound also follows from `3<kappa_E<4` (because `9<12<16`): for the cell convention,

`|R_cell(r)-kappa_E| < 8/(2r+1)`.

---

## AI-T5. Integer-only arbitrary-accuracy certificate

The defining theorem is

`kappa_E>0`, `kappa_E^2=12`.

Since

`3^2<12<4^2`,

start with the rational bracket

`3<kappa_E<4`.

Maintain integers `(L_n,U_n)` with common dyadic denominator `2^n` such that

`L_n/2^n < kappa_E < U_n/2^n`,

and `U_n-L_n=1`.

Initialization:

`n=0`, `L_0=3`, `U_0=4`.

At step `n -> n+1`, let

`M=L_n+U_n`,

which represents the midpoint `M/2^(n+1)`.

Using integers only, compare

`M^2` with `12*2^(2n+2)`.

If

`M^2 < 12*2^(2n+2)`,

set

`L_(n+1)=M`, `U_(n+1)=2U_n`.

Otherwise set

`L_(n+1)=2L_n`, `U_(n+1)=M`.

Equality cannot occur: it would make the positive root of `x^2=12` rational, contradicting that 12 is not a rational square.

The invariant is immediate from monotonicity of `x^2` on positive rationals. Also

`U_(n+1)-L_(n+1)=U_n-L_n=1`,

so the bracket width is exactly

`2^(-(n+1))`.

Thus after `n` steps the certificate brackets `kappa_E` to width `2^-n` using only integer addition, multiplication, exponentiation by 2, and comparison.

No floating point, square root, trigonometry, classical `pi`, or source-circle query occurs.

---

## AI-T6. Integer refinement subsequence invariance

Fix a positive integer `h`. Apply AI-T3 at radius `hr`:

`-2/(hr) < C_N(hr)/(2hr)-kappa_E < 1/(hr)`.

As `r->infinity`, both endpoints tend to zero, so

`lim C_N(hr)/D_step(hr)=kappa_E`.

Likewise AI-T4 at radius `hr` gives

`(-4-kappa_E)/(2hr+1)`

`< C_N(hr)/(2hr+1)-kappa_E`

`< (2-kappa_E)/(2hr+1)`,

so

`lim C_N(hr)/D_cell(hr)=kappa_E`.

Therefore every fixed positive integer refinement subsequence has the same native constant.

---

## Circumference increment theorem

AG proves the jump bit

`s_r=J_N(r)-J_N(r-1) in {0,1}`

and that its order is the lower mechanical/Sturmian word with the frozen slope/intercept.

For `r>=1`,

`C_N(r)-C_N(r-1)`

`=6[(r+J_N(r))-(r-1+J_N(r-1))]`

`=6(1+s_r)`.

Hence every shell circumference increment is exactly one of

`{6,12}`,

and their order is exactly the accepted Sturmian jump order.

Because the corresponding diameter transition span increases by 2 per radial layer, `kappa_E` is the asymptotic circumference growth per unit diameter-transition growth of this purely integer process.

---

## Semantic conclusion

The proved statement is:

`ENTERPRISE_CIRCLE_CONSTANT = kappa_E`,

`kappa_E^2=12`, `kappa_E>0`,

for the accepted N Enterprise circle count geometry and its bounded endpoint-equivalent diameter conventions.

This stage does not identify `kappa_E` with the standard real number `pi`, does not claim standard `pi` algebraic, and does not challenge theorems formulated inside the standard Euclidean/real-analytic definitions. The two constants are deliberately type-separated.

`ENTERPRISE_CIRCLE_CONSTANT_ALGEBRAIC_THEOREM_PROVED__KAPPA_SQUARED_EQ_12`
