# P022 — Target-Family Unit Crossing: No Universal Parity Protection

Status: `COUNTEREXAMPLE / NEGATIVE BOUNDARY / EXACT SMALL-FRANEL CERTIFICATE`  
Owner: `program/p022-geometry-v2`  
Affected candidate: `all nonzero target-family crossing coefficients have a common factor >1`  
Unaffected target: exact marker nonvanishing `kappa_p != 0`

## 1. Explicit target prime

Take

\[
\boxed{p=518220701.}
\]

This is prime and

\[
p\equiv5\pmod{24},
\]

so it lies in the selected forced-midpoint composite-boundary family. Put

\[
m=(p-1)/2=259110350.
\]

## 2. A simple Franel zero at index 50

The exact integer

\[
F_{50}=\sum_{k=0}^{50}\binom{50}{k}^3
\]

is divisible by `p` exactly once:

\[
\boxed{v_p(F_{50})=1.}
\]

At the zero boundary `j=50`,

\[
2j-1=99
\]

is composite, while

\[
2j+1=101
\]

is prime.

Thus the only possible boundary edge is the `q=101` edge, with the negative sign in

\[
c_x(j)=w_{2j-1}(x)-w_{2j+1}(x).
\]

## 3. P022-NB — the crossing coefficient is a unit

Exact prime-halving recursion gives

\[
w_{101}(m)=0,
\qquad
w_{101}(p-2)=1.
\]

Therefore

\[
\begin{aligned}
\Delta c_p(50)
&=c_m(50)-c_{p-2}(50)\\
&=(-0)-(-1)\\
&=\boxed{1}.
\end{aligned}
\]

Hence the set of nonzero crossing coefficients contains an integer unit. Whatever other crossings may exist,

\[
\boxed{g_p=1.}
\]

No complete zero-alphabet scan is required for this conclusion: a gcd over a set containing `1` is already one.

## 4. Consequence

The potential global strategy

> selected primes `p=5,23 (mod 24)` have even crossing correction, or at least crossing-lattice modulus `g_p>1`

is false.

Thus the exact marker problem cannot be solved by one universal parity or gcd obstruction.

This sharpens the hierarchy of failed overstrong routes:

1. global support disjointness — false (`p=369581`);
2. global zero transfer correction — false (`p=369581`);
3. fixed `+1` marker — false (`p=369581` gives `-1`);
4. universal nontrivial crossing-lattice modulus — false (`p=518220701` gives `g_p=1`).

The surviving statement remains only

\[
\boxed{\kappa_p=v_p(D_m)\ne0?}
\]

for the selected target family.

## 5. What this does and does not show

A unit **positive** crossing coefficient does not itself make cancellation likely. Since every earlier zero depth is positive, that contribution raises the marker. Other negative crossings could still exist, so this note does not claim the full marker is positive or nonzero.

The point is narrower and exact: **congruence protection can disappear completely inside the target family.** Any global proof of nonvanishing must use signed crossing geometry and positive-depth arithmetic, not only `g_p`.

## 6. Executable assets

- `src/enterprise_math/p022_barlow_target_unit_crossing.py`
- `tests/test_p022_barlow_target_unit_crossing.py`
