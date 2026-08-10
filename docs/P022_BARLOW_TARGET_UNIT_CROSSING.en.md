# P022 — Target-Family Unit Crossing with an Unconditionally Positive Marker

Status: `PROVED WIP / NEGATIVE BOUNDARY + POSITIVE MARKER CERTIFICATE`  
Owner: `program/p022-geometry-v2`  
Affected candidate: `all nonzero target-family crossing coefficients have a common factor >1`  
Positive conclusion: `g_p=1` can coexist with an exact positive half-defect marker.

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

At the zero boundary `j=50`, `2j-1=99` is composite while `2j+1=101` is prime.

Exact prime-halving recursion gives

\[
w_{101}(m)=0,
\qquad
w_{101}(p-2)=1,
\]

so

\[
\boxed{\Delta c_p(50)=1.}
\]

Thus the crossing set contains an integer unit and therefore

\[
\boxed{g_p=1.}
\]

This disproves any global target-family parity or `g_p>1` strategy.

## 3. P022-LI43 — all transfer-boundary zero candidates are explicitly resolved

A Franel zero can affect the transfer only at an endpoint of one of the two finite prime-halving DAGs rooted at `m` and `p-2`.

For this prime there are exactly 21 left-side boundary candidate indices. The largest is

\[
\boxed{2591104.}
\]

Advancing the exact Franel recurrence modulo `p` only to that endpoint gives

\[
\boxed{
\{j:\ j\text{ is a transfer-boundary candidate and }p\mid F_j\}
=\{50\}.
}
\]

The executable certificate uses an integer modular-inverse recurrence and sparse checkpoint reads; it does not enumerate the full midpoint interval.

Therefore `j=50` is not merely one unit crossing among unknown corrections. It is the **only** earlier zero boundary that contributes to this defect.

## 4. P022-LI44 — the full marker is positive without knowing midpoint depth

Let

\[
z_m=v_p(F_m).
\]

The forced-midpoint theorem gives

\[
z_m\ge1.
\]

Since `v_p(F_50)=1` and the unique crossing coefficient is `+1`, the exact marker is

\[
\boxed{
\kappa_p=v_p(D_m)=z_m+1>0.
}
\]

No modulo-`p^2` calculation at the enormous midpoint is required. Even if the midpoint were an exceptional higher-depth zero, the conclusion only becomes stronger.

Thus this example simultaneously proves:

1. crossing-lattice congruence protection can disappear completely (`g_p=1`);
2. signed coefficient geometry plus positivity of p-adic zero depths can still certify the marker unconditionally.

## 5. Updated boundary hierarchy

The half-index marker route has now falsified several attractive but excessive invariants:

1. global support disjointness — false (`p=369581`);
2. global zero transfer correction — false (`p=369581`);
3. fixed `+1` marker — false (`p=369581` gives `-1`);
4. universal nontrivial crossing-lattice modulus — false (`p=518220701` gives `g_p=1`).

But the exact target

\[
\boxed{\kappa_p\ne0}
\]

survives both explicit target-family collisions examined so far:

- `369581`: negative marker `-1`, protected already by positive-depth load / parity;
- `518220701`: positive marker `z_m+1`, despite `g_p=1`.

The out-of-target control `p=157` still shows that exact cancellation can occur, so global nonvanishing is not formal or automatic.

## 6. Precision interpretation

For this prime, the future query “is the marker nonzero?” does **not** require the exact midpoint depth. The smaller state

\[
(\text{unique boundary coefficient }+1,\ z_m>0)
\]

already decides the query.

This is strictly stronger than the crossing-lattice quotient, which is completely inconclusive at `g_p=1`.

## 7. Executable assets

- `src/enterprise_math/p022_barlow_target_unit_crossing.py`
- `tests/test_p022_barlow_target_unit_crossing.py`
