# P017×P018 Generation 4 Supplement 05 — large-factor cofactor-sieve phase transition

Status: `PROVED STRUCTURAL REDUCTION / joint large-factor distribution open`

This supplement explains why the latest exact-square-root large-prime-factor
results naturally approach P3 but do not automatically cross the P2/prime
parity boundaries.

## L1. Extracting one large prime factor creates a smaller cofactor problem

Let a square-shell state `n` have

\[
P=P^+(n)>X^\beta,
\qquad X=k^2,
\]

with `beta>1/2`.  Since `P^2>X`, the state has at most one prime factor above
that threshold.  Write

\[
n=P m.
\]

Then

\[
\boxed{m<X^{1-\beta}.}
\]

Put

\[
M=X^{1-\beta}.
\]

The original parity problem has been transported to the factor depth of a
cofactor supported below scale `M`.

## L2. Cofactor root ladder

If the cofactor is sieved so that every remaining prime factor exceeds

\[
z=M^{1/r}=X^{(1-\beta)/r},
\]

then `m` cannot contain `r` prime factors counted with multiplicity, because
their product would exceed `M`.  Hence

\[
\boxed{\Omega(n)\le r.}
\]

Thus the natural large-factor/roughness thresholds are

\[
P_3:\quad \alpha>\frac{1-\beta}{3},
\]

\[
P_2:\quad \alpha>\frac{1-\beta}{2},
\]

\[
P_1:\quad \alpha>1-\beta.
\]

This is the asymptotic version of the finite product-capacity theorem already
recorded in `p017_p018_large_factor_roughness_ladder.py`.

## L3. The same ladder is exactly the linear-sieve s=3,2,1 transition

The cofactor sequence has natural support length `M`.  An ordinary divisor
remainder model cannot gain useful independent level beyond its own support
scale: divisors `d>M` divide no positive cofactor in the sequence, and the
naive `1/d` main model acquires boundary-sized remainders.  Thus the natural
unsigned level is

\[
D\asymp M.
\]

At cutoff `z=M^(1/r)`, the linear-sieve parameter is therefore

\[
\boxed{s=\frac{\log D}{\log z}=r.}
\]

Consequently:

\[
\boxed{P_3\leftrightarrow s=3,}
\]

which lies in the positive lower-linear-sieve range;

\[
\boxed{P_2\leftrightarrow s=2,}
\]

where the lower linear-sieve function satisfies `f(2)=0`;

and

\[
\boxed{P_1\leftrightarrow s=1,}
\]

which is deeper inside the classical parity-forbidden regime.

Thus extracting a very large prime factor does reduce the remaining scale, but
it does **not** remove the parity transition.  It reproduces the same transition
inside the cofactor.

## L4. Current 0.744 exponent and the two apparent numerical gaps

Runbo Li's current August-2026 manuscript *On the largest prime factor of
integers in short intervals IV* states that every sufficiently large interval

\[
[X,X+X^{1/2}]
\]

contains an integer with a prime factor exceeding

\[
X^{0.744}.
\]

For `beta=0.744`, the cofactor exponent is `1-beta=0.256`, so the three root
thresholds are

\[
P_3:\ 0.085333\ldots,
\qquad
P_2:\ 0.128,
\qquad
P_1:\ 0.256.
\]

Two previously observed near-misses now have a structural interpretation:

- Campbell's explicit all-square P3 proof uses pre-sieve exponent `1/8=0.125`,
  only `0.003` below the large-factor cofactor P2 threshold `0.128`;
- the project fourth-root cutoff `1/4=0.25` is only `0.006` below the
  large-factor cofactor prime threshold `0.256`.

Neither gap is a routine precision gap.  Crossing the first moves from `s>2`
to the P2 parity endpoint `s=2`; crossing the second would require full
cofactor primality at `s=1`.

## L5. Why recent large-modulus results do not automatically close the gap

Recent Harman-sieve / large-modulus results can produce prime-distribution
statements with factored moduli beyond the square-root exponent.  Those are
statements about different sequences and different main terms.  One cannot
insert their modulus exponent into the cofactor sequence as if the latter had a
uniform `A_d~A/d` model for `d>M`: the cofactor support itself has already
ended.

A genuine improvement must therefore add **new information on the same
large-factor incidence sequence**, for example a weighted/bilinear parity input
that distinguishes prime cofactors at the `s=2` transition, or a joint theorem
which directly forces large-factor and roughness conditions on one witness.

## L6. Current joint target

The correct hybrid statement is not

> one square-shell state is rough, and some other state has a large prime
> factor.

It is a same-witness theorem.  For instance, with the current `0.744` exponent:

- large factor `>X^0.744` + roughness beyond `X^0.128` on the same state forces
  `P2`;
- large factor `>X^0.744` + roughness beyond `X^0.256` on the same state forces
  a prime.

The first sits exactly at the cofactor linear-sieve parity boundary; the second
is substantially stronger.  This is the `LARGE_FACTOR_COFATOR_PARITY_PHASE`
negative/target boundary for subsequent work.
