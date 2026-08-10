# P025 Supplement 80 — A `P^(7/4)` Residual-Split Tail for the Prime-Cube Difference Shell

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplements 75, 79  
Hard block: `NONE`

## 1. Count the prime-cube shell in its own natural height

Use centered coordinates

\[
B=\frac{p+q}{2},
\qquad
A=\frac{p-q}{2},
\]

and work in a dyadic center-height range

\[
\boxed{P/2<B\le P.}
\]

The cube-difference projective atom from Stage 75 is

\[
\rho_-
=
\frac{\varepsilon_Ag_A m(A)m(D)}{6B},
\qquad
D=A^2+3B^2.
\]

Since `epsilon_A g_A<=6`, threshold activation

\[
\rho_-\ge T
\]

implies

\[
\boxed{m(A)m(D)\ge TB>TP/2.}
\]

This relation alone already gives a power-saving count inside the two-dimensional `(A,B)` universe.

## 2. P025-D22 — elementary large-residual integer count

For an integer `n`, let `q_2(n)` be the positive square-divisor root

\[
q_2(n)=\prod_p p^{\lfloor v_p(n)/2\rfloor}.
\]

Then

\[
q_2(n)^2\ge m(n).
\]

Therefore if

\[
m(n)\ge Y,
\]

then `n` is divisible by some square `d^2` with

\[
d\ge\lceil\sqrt Y\rceil.
\]

For `n<=N`, the union bound gives

\[
\boxed{
\#\{n\le N:m(n)\ge Y\}
\le
\sum_{d\ge\lceil\sqrt Y\rceil}^{\lfloor\sqrt N\rfloor}
\left\lfloor\frac N{d^2}\right\rfloor.
}
\]

In particular, for fixed positive `Y` in the nontrivial range,

\[
\boxed{
\#\{n\le N:m(n)\ge Y\}
=O\left(\frac N{\sqrt Y}\right).
}
\]

This is elementary and does not use de Bruijn.

## 3. Split the projective pressure

Choose an integer horizon

\[
H\ge1.
\]

From

\[
m(A)m(D)>TP/2
\]

one has the dichotomy

\[
\boxed{m(A)\ge H}
\]

or

\[
\boxed{m(D)>\frac{TP}{2H}.}
\]

### Radius branch

There are

\[
O\left(\frac P{\sqrt H}\right)
\]

possible values of `A` with `m(A)>=H`. For each `A`, there are at most `P` possible centers `B`. Thus

\[
\boxed{
N_{\rm radius}
=O\left(\frac{P^2}{\sqrt H}\right).
}
\]

### Quadratic-factor branch

On the dyadic range,

\[
D=A^2+3B^2<4P^2.
\]

The large-residual count therefore leaves

\[
O\left(
\frac{P^2}{\sqrt{TP/H}}
\right)
=
O\left(P^{3/2}\sqrt{H/T}\right)
\]

candidate values of `D` before accounting for representations.

## 4. Classical Eisenstein representation bound

The quadratic form has the Eisenstein norm identity

\[
\boxed{
A^2+3B^2
=N\bigl((A+B)+2B\omega\bigr),
}
\]

where

\[
\omega^2+\omega+1=0.
\]

The Eisenstein integers form a UFD. The number of elements of norm `D` is bounded by a constant times the divisor function `tau(D)`. Hence the number of integer representations of

\[
A^2+3B^2=D
\]

is

\[
\boxed{O_\varepsilon(D^\varepsilon).}
\]

for every fixed `epsilon>0`.

This is classical prior mathematics. P025 uses it only to reconstruct centered pairs from the residual-counted integer `D`.

Consequently

\[
\boxed{
N_{\rm quad}
\ll_\varepsilon
P^{3/2+\varepsilon}\sqrt{H/T}.
}
\]

Primality of `B-A` and `B+A` can only reduce the count and is not used.

## 5. P025-T155 — balanced shell tail

Choose

\[
\boxed{H\asymp\sqrt{TP}.}
\]

For an exact integer choice one may take

\[
H=\lceil\sqrt{TP}\rceil.
\]

Then the two branches have the same power scale:

\[
\frac{P^2}{\sqrt H}
\asymp
P^{7/4}T^{-1/4},
\]

and

\[
P^{3/2}\sqrt{H/T}
\asymp
P^{7/4}T^{-1/4}.
\]

Therefore, in the natural nontrivial threshold range and after absorbing small boundary cases into the constant,

\[
\boxed{
N_{(3,3),-}(P,T)
\ll_\varepsilon
P^{7/4+\varepsilon}T^{-1/4}.
}
\]

This counts all centered integer pairs in the dyadic region satisfying the projective residual pressure. The prime-pair subset is no larger.

## 6. Why this is a genuine shell-specific gain

The ambient centered-pair universe has size

\[
\Theta(P^2).
\]

P025-T155 saves a factor

\[
P^{1/4}
\]

at threshold one without using prime distribution.

This should **not** be compared directly to ordinary abc exceptional exponents in `c`-height. The natural object here is the low-capacity `(3,3)` prime-base shell, whose geometry is two-dimensional in `(A,B)`.

The theorem says that projective activation occupies a power-sparse subset of that shell.

## 7. Relation to Stages 77–79

Stage 79 routes pressure into radius residual or cyclotomic modulus. Stage 80 deliberately uses only the weaker residual product

\[
m(A)m(D)\ge TB
\]

because it supports a clean global split and a standard quadratic-form reconstruction.

The cyclotomic congruence modulus remains additional information that may sharpen the second branch later. P025-T155 is therefore a baseline shell tail, not the endpoint of the cyclotomic route.

## 8. Executable assets

Added:

- `src/enterprise_math/abc_prime_cube_difference_tail.py`;
- `tests/test_abc_prime_cube_difference_tail.py`.

The executable layer contains:

- exact `ceil_sqrt` arithmetic;
- the finite square-divisor union bound;
- the balanced integer split horizon;
- the formal exponent profile `(7/4,-1/4)`.

It does not encode the classical Eisenstein/divisor-function asymptotic as if that were a computational proof.

## 9. Prior-art / ownership boundary

Eisenstein UFD arithmetic, norm representation counts and `tau(n)=O_epsilon(n^epsilon)` are classical prior mathematics. The square-divisor union bound is elementary.

P025 owns the projective residual-pressure reduction and its composition with those tools in this specific low-capacity cube-difference shell. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 10. Next frontier

No hard block exists. Continue with:

1. use Stage-79/78 congruence modulus to improve the quadratic-factor branch beyond the divisor-bound baseline;
2. derive an analogous shell-specific tail for cube sums, where all threshold pressure already lies in `Phi_6`;
3. compare the shell tail with exact finite enumeration before claiming any sharpness;
4. keep ordinary abc exceptional-set benchmarking separate from this prime-base shell count.
