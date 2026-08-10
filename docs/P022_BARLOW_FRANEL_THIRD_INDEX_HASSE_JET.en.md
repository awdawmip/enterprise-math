# P022 — The Franel one-third obstruction is a canonical Hasse first-jet condition

Status: `PROVED_WIP / EXACT CONTIGUOUS REDUCTION + ORDINARY-LOCUS SEPARATION`  
Owner: `P022 / program/p022-geometry-v2`  
Depends on: fixed full-truncation one-third datum; cyclotomic gamma/Dwork route  
Scope: identify the Franel congruence inside the canonical rank-three period jet

## 1. Two contiguous hypergeometric series

For the monodromy-normalized rank-three datum, define

\[
A_k=
\frac{(5/6)_k(1/3)_k^2}{(k!)^3}.
\]

These are the coefficients of the canonical local period

\[
F_\alpha(z)
={}_3F_2\!\left(
\frac56,\frac13,\frac13;1,1;z
\right).
\]

The fixed one-third Franel obstruction instead has coefficients

\[
C_k=
\frac{(-1/6)_k(1/3)_k(4/3)_k}{(k!)^3}.
\]

The parameters differ only by integral contiguous shifts, but the two finite
truncations are not the same scalar Hasse factor.

## 2. P022-TJ01 — exact Gosper reduction

The elementary coefficient ratios are

\[
\frac{C_k}{A_k}
=-\frac{3k+1}{6k-1},
\]

and

\[
\frac{A_{k+1}}{A_k}
=
\frac{(6k+5)(3k+1)^2}{54(k+1)^3}.
\]

Define

\[
\boxed{
R_k=\frac{324k^3}{6k-1}.
}
\]

Then direct rational simplification gives the exact identity

\[
\boxed{
\frac{C_k}{A_k}
=
-5-27k
+R_{k+1}\frac{A_{k+1}}{A_k}
-R_k.
}
\]

Equivalently,

\[
\boxed{
C_k
=(-5-27k)A_k
+\bigl(R_{k+1}A_{k+1}-R_kA_k\bigr).
}
\]

This is a genuine Gosper telescoping certificate, not a guessed recurrence.
It is valid over `Q` for every `k>=0`.

## 3. P022-TJ02 — the Franel obstruction is a first jet of the canonical period

Let

\[
p=6M-1
\]

be prime.  The numerator of `A_M/A_(M-1)` contains

\[
6(M-1)+5=6M-1=p,
\]

so

\[
A_M\equiv0\pmod p.
\]

Set

\[
\boxed{
P_p(z)=\sum_{k=0}^{M-1}A_kz^k\in\mathbb F_p[z].
}
\]

Writing

\[
\theta=z\frac d{dz},
\]

and summing the exact Gosper certificate through the Franel truncation, the
terminal boundary vanishes modulo `p`.  Hence the fixed one-third obstruction
satisfies

\[
\boxed{
\mathcal H_p
\equiv
-\bigl(5P_p(1)+27\theta P_p(1)\bigr)
\pmod p.
}
\]

Since the previous Bailey/integer bridge gives

\[
p\mid F_{(p+1)/3}
\iff
\mathcal H_p=0,
\]

we obtain

\[
\boxed{
p\mid F_{(p+1)/3}
\iff
5P_p(1)+27\theta P_p(1)=0.
}
\]

The Franel condition is therefore a first-jet condition on the canonical
period polynomial, not the vanishing of the canonical scalar period.

## 4. P022-TJ03 — Picard--Fuchs closure at z=1

The canonical period satisfies

\[
\boxed{
\left[
\theta^3
-z\left(\theta+\frac56\right)
 \left(\theta+\frac13\right)^2
\right]F_\alpha=0.
}
\]

Because `A_M=0 mod p`, the truncated polynomial `P_p` satisfies the same
operator modulo `p`.

At `z=1`, the two `theta^3` terms cancel.  Clearing denominators gives

\[
\boxed{
81\theta^2P_p(1)
+36\theta P_p(1)
+5P_p(1)=0.
}
\]

If the Franel obstruction vanishes as well, the two linear relations force

\[
\boxed{
\bigl(P_p,\theta P_p,\theta^2P_p\bigr)(1)
=
P_p(1)
\left(1,-\frac5{27},\frac5{243}\right).
}
\]

Thus the complete two-jet direction is already fixed by the one-third
condition.

## 5. P022-TJ04 — scalar Hasse zeros are simple

The indicial polynomial of the canonical Picard--Fuchs operator at `z=1` is

\[
\boxed{
\rho(\rho-1)\left(\rho-\frac12\right).
}
\]

Now

\[
\deg P_p=M-1=\frac{p-5}{6}<\frac p2.
\]

Suppose `P_p(1)=0` and let `m` be its positive integer root multiplicity at
`z=1`.  The indicial equation modulo `p` gives

\[
m(m-1)(m-1/2)=0\pmod p.
\]

Within the degree range `1<=m<p/2`, the only possible integral solution is

\[
\boxed{m=1.}
\]

Therefore

\[
\boxed{
P_p(1)=0
\Longrightarrow
P_p'(1)\ne0.
}
\]

So every scalar-Hasse zero of this canonical polynomial is simple.

## 6. P022-TJ05 — Franel zeros strictly avoid the scalar-Hasse zero locus

If both

\[
P_p(1)=0
\]

and

\[
\mathcal H_p=0
\]

held, the first-jet formula would give

\[
\theta P_p(1)=0.
\]

At `z=1`, `theta P_p=P_p'`, contradicting the simple-zero theorem above.
Hence

\[
\boxed{
\mathcal H_p=0
\Longrightarrow
P_p(1)\ne0.
}
\]

This is a strict conceptual correction to the tempting supersingularity
language: a one-third Franel zero is **not** a zero of the canonical scalar
Hasse factor.  It lies in its nonvanishing/ordinary locus.

Consequently the one-third condition may be divided by `P_p(1)`:

\[
\boxed{
\frac{\theta P_p(1)}{P_p(1)}
=-\frac5{27}
\pmod p.
}
\]

Thus the obstruction is a fixed logarithmic-derivative condition on the
canonical period polynomial.

## 7. P022-TJ06 — nondegenerate critical-point form

Define the pulled-back polynomial

\[
\boxed{
Q_p(x)=x^5P_p(x^{27}).
}
\]

Then

\[
Q_p'(1)=5P_p(1)+27\theta P_p(1).
\]

Therefore

\[
\boxed{
\mathcal H_p=0
\iff
Q_p'(1)=0.
}
\]

A second differentiation gives

\[
Q_p''(1)
=20P_p(1)+243\theta P_p(1)+729\theta^2P_p(1).
\]

Using the fixed jet direction of Section 4, every Franel zero with `p>5`
satisfies

\[
\boxed{
Q_p''(1)=-10P_p(1)\ne0.
}
\]

Hence the pulled-back Hasse polynomial has a **nondegenerate critical point** at
`x=1`, rather than a zero there.

## 8. The complementary examples p=107 and p=149

These two primes make the distinction exact.

For `p=107`,

\[
P_{107}(1)=0,
\qquad
\theta P_{107}(1)=39,
\]

and

\[
\mathcal H_{107}=17\ne0.
\]

So `107` is a scalar-period zero but not a one-third Franel zero.

For `p=149`,

\[
P_{149}(1)=91,
\qquad
\theta P_{149}(1)=88,
\]

while

\[
\mathcal H_{149}=0.
\]

Moreover

\[
Q_{149}''(1)
=-10\cdot91
\equiv133\not\equiv0\pmod{149}.
\]

Thus `149` is the clean primitive Barlow witness already identified at
`r_149=50`, but geometrically it belongs to the ordinary fixed-jet locus, not
the scalar-Hasse zero locus.

## 9. Prior-art boundary and the next Frobenius target

Prior art supplies the hypergeometric Picard--Fuchs operator and the general
Dwork principle that, for `beta=1^n`, canonical truncated hypergeometric
periods give the first p-adic digits of unit-root/Frobenius data in the
ordinary range.  Modern Frobenius-structure work packages these periods and
their derivatives into a matrix-valued horizontal intertwiner.

The exact contiguous Gosper certificate, its specialization to the Franel
one-third obstruction, and the strict scalar-Hasse disjointness theorem are
the P022 results recorded here.  Historical novelty remains
`NOVELTY_UNVERIFIED`.

The next bridge is now narrower than "identify a Hasse invariant":

> identify the fixed logarithmic derivative
> `theta P_p(1)/P_p(1)=-5/27` with the corresponding connection coefficient of
> the period-two `j=1 <-> j=5` Dwork/Frobenius character orbit.

Because Frobenius exchanges those two rank-three sectors at `p=5 mod 6`, this
is naturally an off-diagonal connection/jet question rather than a scalar
trace or supersingularity question.

## 10. Executable assets

Added:

- `src/enterprise_math/p022_barlow_franel_third_index_hasse_jet.py`;
- `tests/test_p022_barlow_franel_third_index_hasse_jet.py`.

They independently verify the rational Gosper identity, finite telescoping,
canonical coefficients and jets, the Picard--Fuchs relation at `1`, simplicity
of scalar-Hasse zeros, strict disjointness from Franel zeros, and the
nondegenerate critical-point specialization at `p=149`.
