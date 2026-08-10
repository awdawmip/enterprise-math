# P025 Supplement 88 — Cover-Resonance Precision and Saturation Boundary

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplement 87  
Hard block: `NONE`

## 1. Resonance is a finite ratio state

For an odd cover prime

\[
r\ge3
\]

and lower exponent `m>=2`, Stage 87 shows that support resonance is the equation

\[
x^m=1
\]

for a difference cover, or

\[
x^m=-1
\]

for a sum cover, inside

\[
\mathbf F_r^\times.
\]

The next question is exact:

> How many prime-ratio classes make the exponent normalization disappear?

## 2. P025-T190 — difference resonance class count

Let

\[
N:=r-1,
\qquad
g:=\gcd(m,N).
\]

The multiplicative group

\[
\mathbf F_r^\times
\]

is cyclic of order `N`. The kernel of the map

\[
x\mapsto x^m
\]

has size `g`.

Therefore

\[
\boxed{
\#\{x\in\mathbf F_r^\times:x^m=1\}=g.
}
\]

The exact unit-ratio density is

\[
\boxed{
\delta^-_{m,r}
=\frac{\gcd(m,r-1)}{r-1}.
}
\]

## 3. P025-T191 — sum resonance solvability and class count

For the sum branch we solve

\[
x^m=-1.
\]

Choose a generator of the cyclic group. This becomes the linear congruence

\[
mt\equiv\frac N2\pmod N.
\]

It is solvable exactly when

\[
g\mid \frac N2,
\]

or equivalently

\[
\boxed{
\frac{r-1}{g}\text{ is even}.
}
\]

When solvable, the congruence has exactly `g` solutions. Hence

\[
\boxed{
\#\{x:x^m=-1\}
=
\begin{cases}
g,&(r-1)/g\text{ even},\\0,&(r-1)/g\text{ odd}.
\end{cases}}
\]

and

\[
\boxed{
\delta^+_{m,r}
=
\begin{cases}
\displaystyle\frac{g}{r-1},&(r-1)/g\text{ even},\\[2mm]
0,&(r-1)/g\text{ odd}.
\end{cases}}
\]

## 4. P025-T192 — difference resonance can saturate

Difference resonance fills the entire unit-ratio space exactly when

\[
g=r-1.
\]

Equivalently,

\[
\boxed{r-1\mid m.}
\]

Thus the difference resonance condition is **not automatically sparse**.

Define the saturation set

\[
\boxed{
\mathcal S_m
:=
\{r\ge3\text{ prime}:r-1\mid m\}.
}
\]

For every

\[
r\in\mathcal S_m,
\]

all unit prime ratios are support-resonant.

However such primes satisfy

\[
\boxed{r\le m+1,}
\]

so the saturation set is finite and determined by the divisor structure of the lower exponent.

## 5. P025-T193 — sum resonance never saturates

If the sum equation is solvable, then

\[
\frac{r-1}{g}
\]

is even, so in particular

\[
g\le\frac{r-1}{2}.
\]

Therefore

\[
\boxed{
\delta^+_{m,r}\le\frac12.
}
\]

The sum support-resonance observation always removes at least half the unit ratio states whenever it is nonempty.

## 6. P025-T194 — large cover primes have small resonance density

For either sign,

\[
g=\gcd(m,r-1)\le m.
\]

Thus

\[
\boxed{
\delta^{\pm}_{m,r}
\le
\frac{m}{r-1}
}
\]

whenever the sum branch is solvable, and automatically on the difference branch.

In particular, if

\[
\boxed{r>m+1,}
\]

then difference resonance cannot saturate, and for both signs

\[
\boxed{
\delta^{\pm}_{m,r}\le\frac{m}{r-1}<1.
}
\]

For fixed lower exponent, support resonance becomes progressively more selective as the cover prime grows.

## 7. P025-T195 — finite height incidence

Fix an integer height

\[
P\ge1.
\]

Let `C` be the exact resonance class count from P025-T190 or P025-T191.

There are at most

\[
P-\left\lfloor\frac Pr\right\rfloor
\]

choices of `q<=P` that are units modulo `r`.

For each such `q` and each allowed ratio class, the corresponding nonzero residue class for `p` contains at most

\[
\left\lceil\frac Pr\right\rceil
\]

integers up to `P`.

Therefore the number of ordered integer pairs in the resonance classes is at most

\[
\boxed{
C
\left(P-\left\lfloor\frac Pr\right\rfloor\right)
\left\lceil\frac Pr\right\rceil,
}
\]

capped of course by `P^2`.

Primality and the ordering `p>q` can only reduce this envelope.

## 8. Cover-level congruence-or-residual routing

Stage 87 proves

\[
\Lambda_{m\to rm}\ge1
\Longrightarrow
\text{resonance}
\ \lor\
m(Q_{m,r})\ge r.
\]

Stage 88 now quantifies the first branch.

Thus a non-attenuating odd-prime cover lies in the union of:

1. a finite ratio state of density `delta_{m,r}`;
2. a quotient value state with multiplicity residual at least `r`.

For large `r>m+1`, the two costs move in opposite coordinates but both strengthen with `r`:

\[
\boxed{
\delta_{m,r}\le\frac{m}{r-1},
\qquad
m(Q)\ge r\text{ off resonance}.
}
\]

This is the **large-cover dual-pressure law**.

## 9. Negative boundary: do not always pay for congruence precision

If

\[
r\in\mathcal S_m,
\]

on the difference branch, the resonance observation is saturated on unit ratios and has no filtering value.

In that regime, computing the ratio class is wasted precision: it does not distinguish states.

Therefore the adaptive policy must begin one step earlier:

1. inspect the cheap pair `(m,r)`;
2. determine the exact resonance class count;
3. only observe the prime ratio modulo `r` if the resulting quotient is genuinely nontrivial.

This is a direct precision-saturation boundary analogous to Stage 80's modulus horizon, but now the saturation is caused by the **operation/exponent pair**, not the numerical observation window.

## 10. Architectural meaning

The useful precision for an odd-prime cover is conditional on metadata already present in the operation language.

The sequence is

\[
\boxed{
(m,r,\pm)
\to
\text{class-count test}
\to
\text{ratio congruence if informative}
\to
\text{quotient residual if nonresonant}.
}
\]

So a precision compiler should not blindly request every available observable. It should first test whether that observable has already saturated under the declared operation parameters.

## 11. Prior-art / novelty discipline

Cyclic finite groups and the root-count formula for `x^m=a` are standard mathematics. The finite residue-class incidence estimate is elementary.

P025 claims none of those ingredients individually.

The project-side candidate is their use as the exact precision cost of the Stage-87 pressure transport, including the operation-induced saturation boundary and the resulting adaptive observation order. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 12. Executable assets

Added:

- `src/enterprise_math/abc_cover_resonance_precision.py`;
- `tests/test_abc_cover_resonance_precision.py`.

The executable layer checks the exact root counts by finite enumeration, difference saturation, empty and half-density sum cases, Stage-87 resonance fixtures, and the height-window incidence envelope.

## 13. Next frontier

No hard block exists. Continue with:

1. classify the finite saturation set `S_m` efficiently from the divisor structure of `m`;
2. derive a cover-normal form separating saturated small cover primes from sparse large cover primes;
3. investigate the quotient-residual branch `m(Q)>=r` using cyclotomic support congruences;
4. combine dyadic orbits with odd-cover resonance signatures into one exponent transport normal form;
5. then produce a Foundation Feedback Packet for task-relative transport precision.
