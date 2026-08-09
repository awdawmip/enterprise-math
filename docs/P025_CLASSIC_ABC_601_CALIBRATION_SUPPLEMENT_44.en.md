# P025 Supplement 44 — Exact 601-Radius Calibration of a Classical High-Quality ABC Triple

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplements 42–43  
Hard block: `NONE`

## 1. The triple

Consider

\[
\boxed{
2+3^{10}\cdot109=23^5.
}
\]

Numerically,

\[
2+6{,}436{,}341=6{,}436{,}343.
\]

Its radical is

\[
\operatorname{rad}(abc)
=2\cdot3\cdot109\cdot23
=15042.
\]

It is a standard high-quality calibration type; P025 uses it only as a finite exact pressure test, not as asymptotic evidence.

## 2. The prime-coordinate relation has support pattern `(1,2,1)`

The raw arithmetic-derivative coefficients are

\[
A=1
\]

for the `a=2` block,

\[
B_1
=3^{10}\cdot109\cdot\frac{10}{3}
=21{,}454{,}470,
\]

\[
B_2
=3^{10}\cdot109\cdot\frac1{109}
=59{,}049,
\]

and

\[
C
=23^5\cdot\frac5{23}
=1{,}399{,}205.
\]

Hence relation-adapted derivations satisfy

\[
\boxed{
 x+21{,}454{,}470y+59{,}049z
 =1{,}399{,}205w.
}
\]

## 3. P025-T108 — exact O(R) feasibility reduction

Let

\[
g=\gcd(B_1,B_2)=19{,}683=3^9.
\]

For fixed `w`, reduce the relation modulo `g`:

\[
\boxed{x\equiv Cw\pmod{19683}.}
\]

For any radius below `g/2`, at most one representative of this congruence can lie in `[-R,R]`.

Once that representative `x` is fixed, divide the remaining relation by `g`:

\[
\boxed{
1090y+3z
=
\frac{Cw-x}{19683}.
}
\]

The coefficients `1090` and `3` are coprime. Their full integer solution set is one affine line, and exact `L_infinity` box feasibility is an intersection of two integer parameter intervals.

Therefore radius feasibility for this four-coordinate witness problem is decided by scanning only `w in [-R,R]` and performing constant-time integer congruence/interval arithmetic per `w`.

This replaces a four-dimensional witness-cube search by a linear-size exact certificate.

## 4. P025-T109 — the exact minimum derivative radius is 601

The exact feasibility oracle gives:

\[
\boxed{
\text{no nondegenerate relation witness exists with }\|x\|_\infty\le600,
}
\]

while radius `601` contains

\[
\boxed{
(x,y,z,w)
=(601,-38,-79,-586).
}
\]

Its additive relation is exact and its Wronskian is nonzero. Thus

\[
\boxed{\mu=601.}
\]

For this witness the Wronskian equals one unit of the compulsory normalized image:

\[
\eta=1.
\]

The global absorption floor is also

\[
\boxed{\eta_{\min}=1,}
\]

so this is a hard intrinsically saturated example: Stage-42 normalization provides no gain.

## 5. Exact projective optimum

Supplement 43 gives

\[
\boxed{
\sigma_{\rm proj}
=
\frac{6561}{11}
\approx596.45.
}
\]

Hence the first-witness projective alignment factor is exactly

\[
\boxed{
G_{\rm align}
=
\frac{601}{6561/11}
=
\frac{6611}{6561}
<1.01.
}
\]

Since `eta_mu=eta_min=1`,

\[
G_{\rm abs}=1.
\]

Thus this high-quality triple is already within one percent of the continuous projective optimum at its very first nondegenerate witness.

The difficult resource is not a large integer-search overhead; it is the projective factor/radical pressure itself.

## 6. P025-T110 — exact projective attainment occurs only at radius 6561

For this triple the `(a,c)` pair is the projective-capacity minimizer. Equality in the dual `L_1/L_infinity` bound forces, in positive-W orientation,

\[
x=-R,
\qquad
w=R.
\]

The middle block must therefore solve

\[
B_1y+B_2z=(A+C)R.
\]

Because the left side is divisible by `g=19683`, exact projective attainment requires

\[
19683\mid(A+C)R.
\]

Here

\[
\frac{19683}{\gcd(19683,A+C)}
=6561.
\]

Therefore every exact projective-attainment radius is a multiple of `6561`.

At radius `6561`, the witness

\[
\boxed{
(-6561,412,5774,6561)
}
\]

is relation-adapted and satisfies exact projective capacity equality. Its absorption redundancy is

\[
\boxed{\eta=11,}
\]

so

\[
\frac{\|x\|_\infty}{\eta}
=
\frac{6561}{11}
=
\sigma_{\rm proj}.
\]

Hence

\[
\boxed{
\rho_{\rm proj}=6561
}
\]

is the first radius at which an integer witness attains the continuous projective optimum exactly.

## 7. Earliest useful witness versus exactly optimal direction

This produces a strong separation:

\[
\boxed{
\mu=601
\ll
\rho_{\rm proj}=6561.
}
\]

The first witness sacrifices only about `0.76%` in projective efficiency but becomes available more than ten times earlier.

Thus task-relative precision should not insist on exact projective optimality when a very near-optimal certificate is available at much lower access radius.

## 8. Executable assets

Added:

- `src/enterprise_math/abc_one_two_one_mu.py`;
- `tests/test_abc_one_two_one_mu.py`;
- `src/enterprise_math/abc_one_two_one_projective.py`;
- `tests/test_abc_one_two_one_projective.py`.

The exact `R=600` infeasibility and `R=601` witness are repository-backed integer certificates rather than floating-point/heuristic searches.

## 9. Next frontier

The remaining `6611/6561` gap is analyzed in Supplement 45 as a finite modular corner obstruction. This is the next attack surface for intrinsically saturated high-quality examples.
