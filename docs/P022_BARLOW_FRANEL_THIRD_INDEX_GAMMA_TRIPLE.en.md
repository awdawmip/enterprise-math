# P022 — Cyclotomic gamma triple and period-two Frobenius route for the Franel one-third obstruction

Status: `PROVED_WIP / EXACT CYCLOTOMIC PACKAGING + EXTERNAL GEOMETRIC INTERFACE`  
Owner: `P022 / program/p022-geometry-v2`  
Depends on: `P022_BARLOW_FRANEL_THIRD_INDEX_FIXED_HYPERGEOM.en.md`  
Scope: replace the isolated fixed truncation by its cyclotomic hypergeometric datum and Dwork parameter cycle

## 1. Starting datum

The one-third Franel route has already reduced, for primes

\[
p=6M-1,
\]

the divisibility question

\[
p\mid F_{2M}
\]

to the full mod-`p` truncation at `1` of the fixed hypergeometric datum

\[
\alpha=\left(\frac56,\frac13,\frac13\right),
\qquad
\beta=(1,1,1).
\]

The use of `5/6` rather than `-1/6` is the monodromy-normalized parameter in
`(0,1]`; the classical series itself may of course be written with `-1/6`.

The purpose of this note is to identify the exact cyclotomic and Frobenius
structure of this datum.  It does **not** yet identify the classical truncated
sum with a specific entry of the resulting Frobenius matrix.

## 2. Prior-art interface

Asem Abdelraouf, *Hypergeometric Motives from Toric Hypersurfaces*,
arXiv:`2509.17624` (2025), introduces gamma triples

\[
(\gamma,\delta,N)
\]

for hypergeometric data defined over cyclotomic fields, extends the associated
finite hypergeometric sums to appropriate prime powers, and proves geometric
point-count realizations for the half-integral monodromy case.

The inputs used here are all prior art:

- the gamma-triple definition and representation theorem;
- Proposition 2.15, which supplies a representation with
  `sum(delta)=0 mod N` whenever `sum(alpha-beta)` is a half integer;
- the toric-hypersurface realization of such data;
- Dwork's dash operation on p-adic parameters.

A convenient modern statement of the dash operation is Wang--Ni,
*A supercongruence related to Whipple's 5F4 formula and Dwork's dash
operation*, arXiv:`2602.13001` (2026), which writes

\[
x^*=\frac{x+\langle-x\rangle_p}{p}
\]

and records that the dash period of a rational `c/d` at primes
`p=s mod d` is the multiplicative order of `s mod d`.

P022-specific content is the exact specialization of these general interfaces
to the Franel one-third obstruction and its Barlow role.

## 3. P022-TG01 — field of definition is the Eisenstein cyclotomic field

The numerator polynomial of the monodromy quotient is

\[
(T-\zeta_6^5)(T-\zeta_3)^2,
\]

while the denominator is

\[
(T-1)^3.
\]

The numerator is not rational, and its coefficients lie in

\[
\boxed{K=\mathbb Q(\zeta_6)=\mathbb Q(\sqrt{-3}).}
\]

Complex/Galois conjugation sends

\[
\boxed{
\left(\frac56,\frac13,\frac13\right)
\longmapsto
\left(\frac16,\frac23,\frac23\right).
}
\]

Thus the natural rank-three datum is genuinely cyclotomic rather than a
rational hypergeometric datum.

## 4. P022-TG02 — an explicit geometric gamma triple

The following `N=6` triple represents exactly the datum above:

\[
\boxed{
\gamma=(-1,-1,-1,1,1,1,-2,1,1),
}
\]

\[
\boxed{
\delta=(5,2,2,-6,-6,-6,0,0,3).
}
\]

Indeed, the first six factors give

\[
\frac{(T-\zeta_6^5)(T-\zeta_6^2)^2}{(T-1)^3},
\]

and the final three are an empty block

\[
\frac{T^2-1}{(T-1)(T+1)}=1.
\]

Hence after cancellation

\[
\boxed{
\frac{
\prod_{\gamma_j<0}(T^{-\gamma_j}-\zeta_6^{\delta_j})
}{
\prod_{\gamma_j>0}(T^{\gamma_j}-\zeta_6^{-\delta_j})
}
=
\frac{(T-\zeta_6^5)(T-\zeta_3)^2}{(T-1)^3}.
}
\]

The balancing conditions are exact:

\[
\sum_j\gamma_j=0,
\qquad
\sum_j\delta_j=-6\equiv0\pmod6.
\]

Moreover the gcd of all `2 x 2` minors of the matrix with rows `gamma` and
`delta` is one.  Thus this is already in the primitive lattice posture used in
the reverse-engineering theorem.

The half-integral condition is also explicit:

\[
\boxed{
\sum_i(\alpha_i-\beta_i)=-\frac32.
}
\]

So the datum falls directly inside Abdelraouf's geometric-realization
hypothesis.

## 5. Concrete toric family at the special value

The triple has length nine, hence `d+2=9`.  Abdelraouf's construction starts
from nonzero homogeneous coordinates `w_1,...,w_9` and a torus coordinate
`z`, with

\[
w_1+\cdots+w_9=0,
\]

\[
\frac{w_4w_5w_6w_8w_9}{w_1w_2w_3w_7^2}=t,
\]

and

\[
\frac{w_1^5w_2^2w_3^2w_9^3}{w_4^6w_5^6w_6^6}=z^6.
\]

For this gamma vector,

\[
\boxed{\gamma^\gamma=-\frac14.}
\]

The point-count theorem uses the finite hypergeometric argument
`t/gamma^gamma`.  Therefore the classical special value at hypergeometric
argument `1` corresponds to the geometric parameter

\[
\boxed{t=-\frac14.}
\]

This produces an explicit toric geometric host for the arithmetic datum.  The
point-count formula also contains companion gamma-twist terms; no claim is
made here that the desired trace is the entire point count by itself.

## 6. P022-TG03 — inert primes force a period-two Dwork parameter cycle

Now impose the Franel one-third prime class

\[
p\equiv5\pmod6.
\]

Dwork's dash operation sends

\[
\frac56\mapsto\frac16,
\qquad
\frac13\mapsto\frac23,
\]

and one more dash returns the original values.  Therefore

\[
\boxed{
\left(\frac56,\frac13,\frac13\right)
\xleftrightarrow{\ *\ }
\left(\frac16,\frac23,\frac23\right)
}
\]

is an exact period-two dash orbit.

This is simultaneously the Galois-conjugation orbit over
`Q(zeta_6)`.  Thus the independently observed facts

- `p=5 mod 6` is inert in `Q(sqrt(-3))`;
- Frobenius exchanges the two cyclotomic parameter blocks;
- Dwork dash exchanges those same blocks;

are one and the same two-cycle at the parameter level.

The first residue-field size satisfying

\[
6\mid(q-1)
\]

is consequently

\[
\boxed{q=p^2.}
\]

This is exactly what one expects for the norm of an inert prime ideal in the
quadratic cyclotomic field.

## 7. P022-TG04 — exact rational rank-six Galois closure

Adjoining the conjugate block gives

\[
\boxed{
\alpha_{\rm cl}
=
\left(
\frac16,\frac56,
\frac13,\frac13,
\frac23,\frac23
\right),
\qquad
\beta_{\rm cl}=1^6.
}
\]

Its monodromy quotient is rational:

\[
\frac{\Phi_6(T)\Phi_3(T)^2}{\Phi_1(T)^6}.
\]

Using

\[
\Phi_6\Phi_3^2
=
\frac{(T^6-1)(T^3-1)(T-1)^6}{T^2-1},
\]

we obtain the gamma-vector identity

\[
\boxed{
\frac{\Phi_6(T)\Phi_3(T)^2}{\Phi_1(T)^6}
=
\frac{(T^6-1)(T^3-1)}{(T^2-1)(T-1)^7}.
}
\]

Hence a rational closure gamma vector is

\[
\boxed{
(-6,-3,2,1,1,1,1,1,1,1).
}
\]

This rank-six closure is an exact cyclotomic-algebra statement.  Calling it an
induced motive, restriction of scalars, or a particular Frobenius block
decomposition would require additional theorem-level justification and is not
done here.

## 8. Two tempting shortcuts are ruled out

### 8.1 Direct EHMM modularity cannot currently be imported

The published EHMM sufficient theorem for certain length-three/four data
requires

\[
\gamma(HD)=n-2+q_n-\sum_i r_i\ge1.
\]

For the present length-three datum,

\[
\boxed{
\gamma(HD)=2-
\left(\frac56+\frac13+\frac13\right)
=\frac12.
}
\]

So that sufficient theorem does not directly apply.  This is a route-boundary
statement, not evidence of non-modularity.

### 8.2 The truncation residue is not directly an elliptic trace

A quick Hasse-bound hypothesis is also false.  At `p=41`, the fixed full
truncation has centered residue

\[
\boxed{13},
\]

whereas

\[
13>2\sqrt{41}.
\]

Thus one cannot identify the residue itself with the Frobenius trace of an
elliptic curve over `F_41`.  The correct arithmetic object must retain more of
the cyclotomic/rank-three or rank-six structure.

## 9. New exact bridge target

The remaining problem is now sharply typed.

We have on one side the classical Hasse-like obstruction

\[
\mathcal H_p
=
{}_3F_2\!\left[
\begin{matrix}
-1/6,1/3,4/3\\
1,1
\end{matrix};1
\right]_{p-1}
\pmod p,
\]

with

\[
p\mid F_{(p+1)/3}
\iff
\mathcal H_p=0.
\]

On the other side we now have an explicit cyclotomic gamma triple, a period-two
Dwork parameter orbit, an `F_{p^2}` finite-hypergeometric trace, and an exact
rational rank-six closure.

The next theorem target is therefore **not** "find another hypergeometric
transformation".  It is:

> identify `mathcal H_p` as the relevant Hasse--Witt/Frobenius entry, minor, or
> unit-root obstruction for the period-two gamma-triple system at the special
> value `t=1` (equivalently geometric parameter `-1/4`).

If this bridge is obtained, the isolated congruence `p|U_M` becomes a geometric
ordinary/supersingular-type condition and the prime-distribution problem can be
attacked with the arithmetic of the corresponding Frobenius system.

## 10. Executable assets

Added:

- `src/enterprise_math/p022_barlow_franel_third_index_gamma_triple.py`;
- `tests/test_p022_barlow_franel_third_index_gamma_triple.py`.

They certify the exact gamma representation, balancing and minor gcd, the
value `gamma^gamma=-1/4`, the period-two dash orbit at `p=5 mod 6`, the first
allowed residue-field size `p^2`, the exact rational rank-six closure, and the
EHMM `gamma=1/2` boundary.
