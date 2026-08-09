# P025 Supplement 11 — Sharp Integrality-Access Defect for Two-Variable Certificates

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P025 Supplement 10  
Hard block: `NONE`

## 1. Generic problem extracted from the abc specialization

Supplement 10 reduces a structured floor-access problem to

\[
A u+B v=N,
\qquad
A,B,N\in\mathbb N_{>0}.
\]

Assume the equation is solvable in integers. Define

\[
\nu(A,B;N)
=
\min_{Au+Bv=N}
\max(|u|,|v|)
\]

and the continuous triangle lower bound

\[
\boxed{
L(A,B;N)
=
\left\lceil\frac{N}{A+B}\right\rceil.
}
\]

The **integrality-access defect** is

\[
\boxed{
\Gamma(A,B;N)=\nu(A,B;N)-L(A,B;N)\ge0.
}
\]

This supplement gives an exact modular zero-defect criterion and a sharp universal coefficient-only upper bound.

## 2. P025-T31 — exact modular criterion for `Gamma=0`

Let

\[
g=\gcd(A,B),
\qquad
A'=A/g,
\quad
B'=B/g,
\quad
N'=N/g.
\]

Then `gcd(A',B')=1`. Put

\[
L=\left\lceil\frac{N'}{A'+B'}\right\rceil.
\]

A solution with

\[
|u|,|v|\le L
\]

must have

\[
-L\le u\le L
\]

and, from `|v|<=L`,

\[
N'-B'L
\le A'u\le
N'+B'L.
\]

Therefore the allowed integer interval for `u` is

\[
\boxed{
I_L
=
\left[
\max\left(-L,
\left\lceil\frac{N'-B'L}{A'}\right\rceil\right),
\min\left(L,
\left\lfloor\frac{N'+B'L}{A'}\right\rfloor\right)
\right]\cap\mathbb Z.
}
\]

At the same time the equation requires

\[
\boxed{
A'u\equiv N'\pmod{B'}.
}
\]

Hence

\[
\boxed{
\Gamma=0
\iff
I_L\text{ contains the required residue class modulo }B'.
}
\]

This is an exact finite test using one modular inverse and one bounded interval.

## 3. P025-T32 — sharp universal defect bound

Define the reduced maximum coefficient

\[
\boxed{
M=\max(A',B').
}
\]

Then

\[
\boxed{
0\le\Gamma(A,B;N)
\le
\left\lfloor\frac{M-1}{2}\right\rfloor.
}
\]

Moreover this coefficient-only upper bound is sharp over the class of positive solvable two-variable integer equations.

### Proof of the upper bound

The reduced equation is

\[
A'u+B'v=N'.
\]

Over the reals, the minimum `L_infinity` norm is attained at the balanced point

\[
(u,v)=(t,t),
\qquad
 t=\frac{N'}{A'+B'}.
\]

Indeed any real pair with `max(|u|,|v|)<=B` satisfies

\[
N'\le(A'+B')B,
\]

and equality at `B=t` is realized by `(t,t)`.

All integer solutions lie on one affine parameter lattice with primitive direction

\[
(B',-A').
\]

Let `k_*` be the real parameter corresponding to the balanced point. Choose an integer `k` with

\[
|k-k_*|\le1/2.
\]

The resulting integer solution differs from `(t,t)` by at most

\[
B'/2
\]

in the first coordinate and

\[
A'/2
\]

in the second. Hence

\[
\nu\le t+M/2.
\]

Because `nu` is an integer:

- if `t` is an integer, `(t,t)` itself is an integer solution and `Gamma=0`;
- if `t` is not an integer,
  \[
  \nu\le\lfloor t+M/2\rfloor.
  \]

Write `M=2h` or `M=2h+1`. A direct fractional-part check gives

\[
\lfloor t+M/2\rfloor-\lceil t\rceil
\le
\begin{cases}
h-1,&M=2h,\\
h,&M=2h+1,
\end{cases}
\]

which is exactly

\[
\left\lfloor\frac{M-1}{2}\right\rfloor.
\]

Thus the claimed bound follows. ∎

## 4. P025-T33 — sharpness families

The bound from P025-T32 is attained for every reduced maximum coefficient `M>=2`.

### Even `M=2h`

Take

\[
A=M,
\qquad
B=1,
\qquad
N=h.
\]

Then

\[
L=1.
\]

The congruence

\[
v\equiv h\pmod{2h}
\]

forces `|v|>=h`, while `(u,v)=(0,h)` is a solution. Hence

\[
\nu=h
\]

and

\[
\boxed{
\Gamma=h-1
=
\left\lfloor\frac{M-1}{2}\right\rfloor.
}
\]

### Odd `M=2h+1`

Take

\[
A=2h,
\qquad
B=2h+1,
\qquad
N=3h+1.
\]

Again

\[
L=1.
\]

Modulo `2h`, one has

\[
v\equiv h+1\pmod{2h}.
\]

The two nearest residue representatives lead respectively to `|v|=h+1` or `|u|=h+1`; the explicit solution

\[
(u,v)=(-h,h+1)
\]

shows

\[
\nu=h+1.
\]

Therefore

\[
\boxed{
\Gamma=h
=
\left\lfloor\frac{M-1}{2}\right\rfloor.
}
\]

So no smaller bound depending only on the reduced maximum coefficient can hold in general.

## 5. Consequence for `1+qr=p^m`

In Supplement 10,

\[
A=r,
\qquad
B=q,
\qquad
N=m p^{m-1},
\]

and `q,r` are coprime primes. Thus

\[
M=\max(q,r).
\]

The exact family defect

\[
\Gamma_{\rm int}
=\nu-
\left\lceil\frac{m p^{m-1}}{q+r}\right\rceil
\]

satisfies

\[
\boxed{
0\le\Gamma_{\rm int}
\le
\left\lfloor
\frac{\max(q,r)-1}{2}
\right\rfloor.
}
\]

This does not claim that the generic sharpness families from P025-T33 themselves satisfy the prime-power relation. It gives a rigorous universal upper bound for every actual triple in the P025 family.

## 6. Examples

### `1+15=16`

The modular interval contains the required residue at the triangle lower bound, so

\[
\Gamma_{\rm int}=0.
\]

### `1+511=512`

Here

\[
q=7,
\qquad
r=73,
\qquad
L=29,
\qquad
\nu=33,
\]

so

\[
\Gamma_{\rm int}=4.
\]

The universal coefficient-only bound is

\[
\left\lfloor\frac{73-1}{2}\right\rfloor=36,
\]

so the exact defect is much smaller than the worst case allowed by the coefficient size.

This leaves room for stronger bounds using the special prime-power structure rather than generic Diophantine geometry.

## 7. Architectural meaning

The new defect has a precise interpretation:

\[
\boxed{
\text{continuous resource bound}
+
\text{finite integrality correction}
=
\text{exact certificate access precision}.
}
\]

The correction is not arbitrary. In the two-variable setting it is always bounded by a finite coefficient-scale term, and it vanishes exactly when one residue class intersects one explicit interval.

This is a useful model of how Enterprise Math can treat discreteness:

> do not replace a discrete problem by a continuous estimate and call the gap “noise”; identify the exact finite arithmetic obstruction left after the continuous bound.

## 8. Prior-art discipline

The theorem uses elementary/standard material:

- affine parameterization of linear Diophantine equations;
- nearest-integer rounding;
- modular inverses;
- floor/ceiling arithmetic.

P025 does not claim historical priority for this generic optimization inequality. Its role here is as an exact calibration theorem for certificate-access precision.

## 9. Executable assets

`src/enterprise_math/abc_absorption_two_variable.py` now also contains:

- the exact modular sharpness criterion;
- the exact integrality defect;
- the universal bound `floor((M-1)/2)`;
- explicit sharpness examples for every `M>=2`.

Tests exhaust all positive `A,B<16`, `N<40` for the bound and verify the sharpness family across both parities.

## 10. Next frontier

No hard block exists. Continue with:

1. exploit the actual relation `1+qr=p^m` to improve the generic coefficient bound;
2. study whether the prime-power congruence forces unusually small or large modular access defects;
3. seek exact asymptotics for the constructive-versus-optimal witness ratio on structured families;
4. test the same continuous-bound-plus-integrality-defect decomposition in higher-dimensional witness slices;
5. keep generic Diophantine optimization separate from any eventual claim specific to abc arithmetic.
