# P025 Supplement 45 — Modular Corner Obstruction to Projective Alignment

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplements 43–44  
Hard block: `NONE`

## 1. The remaining alignment gap is arithmetic

For a `(1,2,1)` support triple, write the additive derivative equation as

\[
A x+B_1y+B_2z=Cw.
\]

Assume the `(a,c)` pair realizes the minimum projective capacity from Supplement 43.

Choose the positive-W orientation and radius `R`. Exact projective equality requires

\[
x=-R,
\qquad
w=R.
\]

For an arbitrary radius-R witness write its two outer deficits as

\[
\boxed{
x=-R+e,
\qquad
w=R-d,}
\]

where

\[
0\le e,d\le2R.
\]

## 2. P025-T111 — exact capacity loss is a weighted corner distance

For a `(1,2,1)` triple, the Wronskian can be written using only the outer derivative values:

\[
W
=aCw-cAx.
\]

The exact projective capacity is

\[
L=cA+aC.
\]

Substituting the deficit coordinates gives

\[
W
=L R
-cAe
-aCd.
\]

Therefore the raw projective capacity slack is exactly

\[
\boxed{
\chi_{\rm corner}(e,d)
=cAe+aCd.
}
\]

No middle-block witness coordinate appears in this loss formula.

## 3. P025-T112 — middle-block integrality imposes a finite modular obstruction

Let

\[
g=\gcd(B_1,B_2).
\]

The middle derivative contribution must satisfy

\[
B_1y+B_2z
=(A+C)R-Ae-Cd.
\]

The left side is divisible by `g`, so every integer witness must satisfy

\[
\boxed{
Ae+Cd
\equiv
(A+C)R
\pmod g.
}
\]

Thus, before checking any finer bounded representability by `(y,z)`, the outer deficits lie in an affine congruence lattice in `Z^2`.

Define the radius-R **modular corner defect**

\[
\boxed{
\delta_R^{\rm mod}
=
\min
\{cAe+aCd:
0\le e,d\le2R,
Ae+Cd\equiv(A+C)R\pmod g\}.
}
\]

Every positive-W radius-R witness satisfies

\[
\boxed{
|W|
\le
LR-\delta_R^{\rm mod}.
}
\]

Whenever the right side is positive, its projective alignment factor is bounded below by

\[
\boxed{
G_{\rm align}(R)
\ge
\frac{LR}{LR-\delta_R^{\rm mod}}.
}
\]

This is a finite modular obstruction, not a high-dimensional lattice-volume estimate.

## 4. Exact classical calibration at radius 601

For

\[
2+3^{10}\cdot109=23^5
\]

one has

\[
g=19683.
\]

At

\[
R=601,
\]

the exact weighted congruence minimization gives

\[
\boxed{(e,d)=(0,15)}
\]

and

\[
\boxed{
\delta_{601}^{\rm mod}
=41{,}976{,}150.
}
\]

The actual first witness from Supplement 44, after orienting W positively, is

\[
(-601,38,79,586).
\]

It has exactly the same outer deficits `(0,15)`. Therefore

\[
\boxed{
\text{the first witness attains the congruence-only modular defect floor.}
}
\]

Consequently

\[
G_{\rm align}
=
\frac{LR}{LR-\delta_{601}^{\rm mod}}
=
\boxed{
\frac{6611}{6561}
}.
\]

So the entire first-witness alignment gap is already forced by the finite congruence modulo `19683`; no additional middle-block representability penalty remains at radius 601.

## 5. Exact projective radius kills the modular obstruction

At

\[
R=6561,
\]

Supplement 44 shows

\[
g\mid(A+C)R.
\]

Hence

\[
(e,d)=(0,0)
\]

is congruence-admissible and

\[
\boxed{
\delta_{6561}^{\rm mod}=0.
}
\]

This is exactly the first radius at which continuous projective equality can be realized integrally.

## 6. New attack surface for the `eta_min=1` hard subfamily

When

\[
\eta_{\min}=1,
\]

intrinsic Wronskian normalization does not help. If also

\[
G_{\rm abs}=1,
\]

then the remaining effective-derivative gap is entirely projective alignment.

For `(1,2,1)` supports, Supplement 45 converts that alignment problem into two nested finite questions:

1. **modular corner approximation** in the congruence
   \[
   Ae+Cd\equiv(A+C)R\pmod g;
   \]
2. **bounded middle-block representability** of the resulting multiple of `g`.

The classical high-quality sample shows the first layer can already be exact.

This is substantially narrower than searching the original prime-coordinate witness box.

## 7. Prior-art boundary

Linear congruences, closest lattice points, and weighted modular approximation are standard mathematics. P025 claims no priority for them.

The project-specific pressure-test result is the exact identification of the projective alignment overhead with a weighted outer-corner congruence defect in the arithmetic-derivative witness system.

## 8. Executable assets

Added:

- `src/enterprise_math/abc_one_two_one_corner_defect.py`;
- `tests/test_abc_one_two_one_corner_defect.py`.

## 9. Next frontier

No hard block exists. Continue with:

1. upper bounds on `delta_R^mod` from Euclidean/continued-fraction structure;
2. comparison of modular and actual alignment loss across high-quality `(1,2,1)` triples;
3. prime-local decomposition of the modulus `g=A(b)`;
4. subpower control of alignment in intrinsically saturated families;
5. do not infer a global abc result from the one calibration family.
