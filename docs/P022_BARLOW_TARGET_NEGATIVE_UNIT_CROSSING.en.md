# P022 — Target-Family Negative Unit Crossing

Status: `COUNTEREXAMPLE / NEGATIVE BOUNDARY / POCKLINGTON-CERTIFIED`  
Owner: `program/p022-geometry-v2`  
Affected candidate: any universal target-family sign orientation for unit crossings  
Boundary: this note does not evaluate the enormous midpoint marker itself.

## 1. Exact target prime

Let

\[
\boxed{P=8895267426781770496852703.}
\]

The executable asset carries a classical Pocklington certificate chain proving that `P` is prime. In particular a certified prime factor

\[
11223923079997\mid P-1
\]

is combined with the factors `2` and `13` to give a known factor of `P-1` larger than `sqrt(P)`, with explicit Pocklington witnesses. The large supporting primes required by the q=97 ancestry chain are certified similarly or by exact trial division at feasible size.

Moreover

\[
P\equiv23\pmod{24},
\]

so this lies in the same selected forced-midpoint composite-boundary family.

Set

\[
m=(P-1)/2.
\]

## 2. A simple zero at `j=49`

The exact Franel number

\[
F_{49}=\sum_{k=0}^{49}\binom{49}{k}^3
\]

has

\[
\boxed{v_P(F_{49})=1.}
\]

At `j=49`,

\[
2j-1=97
\]

is prime and

\[
2j+1=99
\]

is composite. Therefore only the `q=97` edge can contribute to the zero-boundary coefficient, now with the positive sign inside each individual transfer

\[
c_x(49)=w_{97}(x).
\]

## 3. P022-NB — exact negative unit crossing

The midpoint factorization and recursive prime-halving tree give

\[
w_{97}(m)=0.
\]

For `P-2`, an exact certified chain is

\[
P-2
=3R_0,
\]

with `R_0` prime, and after successive prime-halving/factor steps the branch reaches the prime `645049`; its half

\[
(645049+1)/2=322525
\]

has prime factor `97`. All sibling branches are checked to have zero q=97 multiplicity. Hence

\[
w_{97}(P-2)=1.
\]

Therefore

\[
\boxed{
\Delta c_P(49)
=w_{97}(m)-w_{97}(P-2)
=-1.
}
\]

Thus the target family contains a **negative unit crossing**.

## 4. Combined with the positive-unit example

P022 now has exact target-family examples of both signs:

\[
\Delta c_{518220701}(50)=+1,
\]

and

\[
\Delta c_P(49)=-1.
\]

Consequently none of the following can be a global invariant of the selected residue family:

- all crossings are even;
- all nonzero crossings have gcd greater than one;
- all unit crossings have the same sign;
- crossing sign is fixed by `p mod 24` alone.

The global marker problem is therefore genuinely a **signed positive-depth** problem.

## 5. Why this is not yet a marker counterexample

A negative coefficient `-1` is the most dangerous local geometry when the midpoint depth is one, because a single earlier depth-one zero could cancel it. But the full marker also receives every other nonzero boundary contribution, and the midpoint depth at this enormous prime has not been evaluated here.

Therefore this note proves only the local unit crossing and its sign. It does **not** claim

\[
v_P(D_m)=0.
\]

The exact cancellation question remains

\[
z_m+\sum_jz_j\Delta c_P(j)=0.
\]

## 6. Methodological consequence

After the explicit `369581`, `518220701`, and present `P` examples, the surviving hierarchy is:

1. support incidence alone is insufficient;
2. signed flux is required;
3. gcd/parity alone is insufficient;
4. coefficient sign alone is not uniform across the family;
5. positive p-adic depths and their exact signed linear combination are the remaining arithmetic state.

This is precisely the boundary at which the affine-semigroup classification becomes the correct coefficient-only quotient.

## 7. Executable assets

- `src/enterprise_math/p022_barlow_target_negative_unit_crossing.py`
- `tests/test_p022_barlow_target_negative_unit_crossing.py`

The source includes the compact Pocklington verifier and all concrete certificate data needed for the large prime claims; no probable-prime assumption is used by the regression.
