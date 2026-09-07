# BRC Error Linearization and Pell/Padé Tail — Round 10

Status: `EXACT DERIVATIVE LINEARIZATION / EXACT BRC FINITE-DIFFERENCE LAW / PROVED PELL-PADE TAIL / FINITE PERFORMANCE BENCHMARK`
Date: `2026-09-07`
Parents: `t0.brc_table_free_tail`, `t0.brc_pairwise_multiplier_transport`

## 1. Question

Quantify the multiplier-predictor error itself and ask whether repeated
differentiation or recursive BRC correction exposes a final linear law.

The answer is yes in three different exact senses.

## 2. Error ODE and the derivative-order linear law

Put

`y(x)=sqrt(1+x)-1`.

Then y satisfies the first-order **linear** differential equation

`2(1+x)y'(x)-y(x)=1`.

Let `P_K` be the degree-K Taylor truncation at x=0 and

`E_K=y-P_K`.

The Taylor coefficients obey the same ODE coefficient recursion, so all powers
below degree K cancel and

`2(1+x)E_K'(x)-E_K(x)=-(2K-1)c_K x^K`

where `c_K=binom(1/2,K)`.  For even K the right side is positive and equals

`2(K+1)c_(K+1)x^K`.

Once the derivative order n exceeds K, the polynomial P_K has disappeared
completely.  Therefore

`E_K^(n)(x)=y^(n)(x)`

and the exact derivative ratio is

`(1+x) E_K^(n+1)(x) / E_K^(n)(x) = 1/2-n`.

The right side is affine in the derivative order n.  This is the first exact
"final linear law".

In particular,

`( E_K^(K+1)(x) / E_K^(K+1)(0) )^(-2/(2K+1)) = 1+x`.

After K+1 differentiations and one fixed inverse-power normalization, the error
is **exactly linear in x**.

## 3. Quantifying the gradually changing truncation error

For even K, write

`c=c_(K+1)>0`, `p=K+1/2`, `x=h/m`.

The alternating tail begins

`E_K(x)=c x^(K+1) - |c_(K+2)| x^(K+2) + c_(K+3)x^(K+3)-...`.

Set

`alpha=(2K+1)/(2K+4)`

and

`beta=(2K+1)(2K+3)/(4(K+2)(K+3))`.

For `0<x<=1`, alternating-series bounds give

`1-alpha*x <= E_K(x)/(c*x^(K+1)) <= 1-alpha*x+beta*x^2`.

Now scale the error to the multiplier-root size:

`H_K(m)=sqrt(mN) E_K(h/m)`.

Its leading law is

`H_K(m) ~ c sqrt(N) h^(K+1) m^(-(K+1/2))`.

Thus the predictor miss is a power law rather than an accumulated drift.
Because every BRC step is corrected back to an exact `(J,R)` state, local
predictor errors **do not compound from one multiplier to the next**.

Define the normalized inverse-power coordinate

`T_K(m) = [ H_K(m) / (c sqrt(N) h^(K+1)) ]^(-1/p)`.

Since `H_K/(c sqrt(N)h^(K+1))=m^(-p) z` with z in the two alternating bounds,

`m(1-alpha*h/m+beta*h^2/m^2)^(-1/p)`
`<= T_K(m) <=`
`m(1-alpha*h/m)^(-1/p)`.

Consequently

`T_K(m)`
`= m + h/(K+2)`
`  - ((K+1)(2K+3)/(4(K+2)^2(K+3))) h^2/m`
`  + O(m^-2)`.

So the inverse-power error coordinate approaches a line of **slope exactly 1**
and universal intercept `h/(K+2)`, with the first curvature correction explicitly
quantified as O(1/m).

This is the second linearization law: the raw error is a power law, while a
fixed inverse-power transform is asymptotically affine in multiplier m.

## 4. Integer BRC correction noise around the analytic error

Let

`sqrt(mN)=J+delta`, `0<=delta<1`,

and let L_K be the lower Taylor predictor.  Put

`rho = frac(J L_K(h/m))`,
`beta_m=sqrt(1+h/m)`.

If q is the exact number of integer root basins missed by the lower predictor,
then

`q = floor( J E_K(h/m) + rho + beta_m*delta )`.

Therefore the integer correction count differs from the smooth analytic quantity
`J E_K` by only bounded phase noise:

`J E_K - 1 < q < J E_K + 1 + beta_m`.

For the short-step regime h<=m, `beta_m<=sqrt(2)`.  Hence before the final tail,
where `J E_K >> 1`, the observed BRC correction count follows the same power law
up to O(1) additive noise.  Close to the tail that bounded phase becomes dominant,
which explains why fitting the raw integer correction sequence is unstable.

## 5. Recursive BRC itself is exactly quadratic

Suppose a lower predictor starts at integer candidate root a with target gap G_0.
After q ordinary BRC basin crossings,

`G_q = G_0 - q(2a+q)`.

Therefore

`Delta G_q = -(2a+2q+1)`,
`Delta^2 G_q = -2`,
`Delta^3 G_q = 0`.

Thus recursive BRC correction has an exact quadratic gap orbit, a linear first
difference, and constant second difference.  No approximation is involved.

This is the third final linear law requested by the error-recursion attack.

## 6. From the linear ODE to a Pell/Padé recursion

The derivative law suggests replacing a long Taylor polynomial by the diagonal
Padé approximation to `sqrt(1+x)`.

Let z=sqrt(1+x).  Expand the odd power

`(1+z)^(2n+1)=P_n(x)+z Q_n(x)`.

Conjugating z -> -z and multiplying gives the exact polynomial norm

`P_n(x)^2-(1+x)Q_n(x)^2 = -x^(2n+1)`.

Hence for x>0,

`P_n(x)/Q_n(x) < sqrt(1+x)`.

For x=h/m, homogenize by

`A_n=m^n P_n(h/m)`,
`B_n=m^n Q_n(h/m)`.

Then the approximation becomes completely integral and satisfies

`(m+h)B_n^2 - m A_n^2 = h^(2n+1)`.

The pair itself obeys the first-order vector recurrence

`A_(n+1)=(2m+h)A_n+2(m+h)B_n`,
`B_(n+1)=2mA_n+(2m+h)B_n`,

with `A_0=B_0=1`.

Eliminating the companion coordinate gives the same second-order **linear**
recurrence for both sequences:

`X_(n+2)=(4m+2h)X_(n+1)-h^2 X_n`.

Initial values are

`A_0=B_0=1`,
`A_1=4m+3h`,
`B_1=4m+h`.

This recursion is evaluated by binary powering in the checked-in reference tool,
so order n costs O(log n) quadratic-field squarings rather than n explicit
Taylor terms.

## 7. Exact error certificate without sqrt-ratio evaluation

Let

`r_n=A_n/B_n`,
`beta=sqrt((m+h)/m)`.

The Pell norm gives

`beta^2-r_n^2 = h^(2n+1)/(m B_n^2)`.

Since `beta+r_n > 2A_n/B_n`,

`0 < beta-r_n < h^(2n+1)/(2m A_n B_n)`.

For an exact source BRC root J, the purely integer condition

`J h^(2n+1) <= m A_n B_n`

therefore implies

`J(beta-r_n) < 1/2`.

For h in {1,2}, m>=h gives beta<=sqrt(2).  Including the <1 flooring loss and
the source phase beta*delta<sqrt(2), the exact target integer root lies at most
two BRC basins above

`floor(A_n J/B_n)`.

Thus the Pell/Padé predictor has a **sqrt-free exact <=2-correction certificate**.

## 8. Finite validation

The research harness checked:

- the derivative-ratio identity symbolically for K=2,4,6,8,16 and several
  derivative orders beyond K;
- Pell identities and the second-order order-recurrence on multiplier grids;
- 2,700 certified random transports spanning 64..2048-bit N and multiple
  multipliers, steps, and Padé orders;
- every certified transport agreed with direct integer square roots and used at
  most two BRC corrections.

Repository regression additionally records the same algebraic invariants and
small/random transport equivalence.

## 9. Tail-onset improvement over the previous Taylor tool

On deterministic probes `N=2^bits-159`, h=2, compare Padé order n with Taylor
degree K=2n, so both have formal error exponent 2n+1.

| N bits | Padé n | Pell first certified m | Taylor K | Taylor first certified m | onset ratio |
|---:|---:|---:|---:|---:|---:|
| 512 | 32 | 7 | 64 | 29 | 4.14x |
| 1024 | 32 | 124 | 64 | 439 | 3.54x |
| 2048 | 64 | 126 | 128 | 471 | 3.74x |
| 2048 | 128 | 8 | 256 | 31 | 3.88x |
| 4096 | 128 | 127 | 256 | 489 | 3.85x |
| 8192 | 256 | 127 | 512 | 500 | 3.94x |

Thus the Pell identity improves the constant in the same asymptotic
`N^(1/(4n+1))` tail exponent by roughly a factor four in these probes.

## 10. Finite CPU result

At the later Taylor onset, so both certificates hold on the same state, the
Pell/Padé transport was approximately:

- 3.61x faster than Taylor at 512 bits / n=32;
- 3.26x faster at 1024 bits / n=32;
- 4.76x faster at 2048 bits / n=64;
- 8.01x faster at 2048 bits / n=128;
- 4.56x faster at 4096 bits / n=128;
- 5.33x faster at 8192 bits / n=256.

It still did not beat direct optimized Python `isqrt` in these single-step
measurements; direct-isqrt / Pell ratios were about 0.35..0.54.  Therefore this
is a major improvement of the **table-free predictor path**, not yet a universal
replacement for direct roots or cached dyadic predictors.

The gap to uncached dyadic sqrt-ratio construction becomes small at larger bit
sizes in auxiliary tests, so a lower-level C/Rust implementation remains worth
future evaluation.

## 11. Interpretation

The user-suggested differentiation/recursive-BRC attack reveals that the apparent
nonlinearity has several nested linear cores:

1. the exact lifted BRC state is already linear in multiplier:
   `J_m^2+R_m=mN`;
2. recursive BRC correction has constant second difference;
3. post-truncation derivatives have affine derivative ratios;
4. the Padé/Pell approximation order obeys a second-order linear recurrence.

The practical consequence is a substantially cheaper, exactly certified,
table-free tail predictor.

## 12. Boundaries and next attack

- The Padé/Pell approximation itself is classical rational-approximation/Pell
  structure; the contribution here is its exact composition with retained BRC
  state, certification, and multiplier-tail execution surface.
- Short-step reference surface remains h in {1,2}.
- No asymptotic factorization speedup, RSA-practical claim, or Foundation
  promotion is made.
- Direct Python isqrt remains faster for isolated target roots.

Next high-value attack: exploit the second-order linear recurrence or its
quadratic-field fast-doubling form across a long **stream of changing m** so that
successive Padé predictors reuse work instead of rebuilding A_n,B_n from
scratch.  If that can be done with O(1) amortized small-state updates, this is the
most plausible path for turning the present error-linearization theorem into a
runtime win.
