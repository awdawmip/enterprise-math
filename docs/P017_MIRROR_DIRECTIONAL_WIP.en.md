# P017 Mirror Certificate — Directional Refinement WIP

Status: `ACTIVE PROGRAM RESEARCH / NOT CANONICAL`  
Owner: P017 program layer  
Depends on: canonical mirror MC01–MC06  
Novelty: `NOVELTY_UNVERIFIED`

## MC07 candidate — retain the two directions of the first moment

For each surviving radius `r`, let

\[
a_r=|\mathcal P_-(r)|,
\qquad
b_r=|\mathcal P_+(r)|.
\]

Instead of immediately collapsing them into the old first moment

\[
J=\sum_r(a_r+b_r),
\]

retain

\[
J_-:=\sum_r a_r,
\qquad
J_+:=\sum_r b_r.
\]

Let `S=|S_k|` and define directional excess slacks

\[
U_-:=J_--S,
\qquad
U_+:=J_+-S.
\]

The existing cross-side slack is

\[
V=E-J_- -J_+ +S
 =\sum_r(a_r-1)(b_r-1).
\]

Under hypothetical prime-free behavior every surviving mirror side is composite, so

\[
a_r\ge1,
\qquad
b_r\ge1.
\]

Putting

\[
x_r=a_r-1,
\qquad
y_r=b_r-1,
\]

gives

\[
U_- =\sum_r x_r\ge0,
\qquad
U_+ =\sum_r y_r\ge0,
\qquad
V=\sum_r x_ry_r\ge0.
\]

Because all terms are nonnegative,

\[
\boxed{
V=\sum_r x_ry_r
\le
\left(\sum_r x_r\right)
\left(\sum_r y_r\right)
=U_-U_+.
}
\]

Therefore a prime-free basin must satisfy

\[
\boxed{
U_-\ge0,
\quad
U_+\ge0,
\quad
V\ge0,
\quad
V\le U_-U_+.
}
\]

Any violation is a sufficient prime certificate.

## MC07 strictly subsumes MC06

The old slack is

\[
U=U_-+U_+.
\]

If `U<0`, at least one directional slack is negative.

If `V<0`, MC07 detects the same contradiction.

If the old quadratic certificate fires,

\[
4V>U^2,
\]

then, when both directional slacks are nonnegative,

\[
U_-U_+\le\frac{(U_-+U_+)^2}{4}=\frac{U^2}{4}<V.
\]

Hence every MC06 certificate is an MC07 certificate.

## Finite pressure test

A direct bounded check for `3<=k<=1000` gives:

- MC06 certificates: `733`;
- MC07 directional certificates: `740`;
- new MC07-only roots:

`137, 171, 233, 293, 336, 470, 570`.

The six roots other than `233` already fail one directional first-moment inequality. At `k=233`,

\[
U_-=0,
\qquad
U_+=4,
\qquad
V=1,
\]

so the old total certificate is silent but the directional product envelope gives

\[
1>0\cdot4.
\]

This computation is pressure-test evidence, not a proof for all `k`.

## Negative test: do not reopen unstructured moment expansion

We also tested the obvious next extension using same-side second moments and a Cauchy bound on `V`. It produced **no additional certificates** beyond MC07 for `k<=1000`.

Therefore the program should stop that moment-expansion route here. The next useful information must come from a structurally different source, such as a bounded least-factor gate, exact support closure, or a non-tautological coupling with quotient/root windows.

## Implementation

Program branch assets:

- `src/enterprise_math/p017_mirror_directional.py`;
- `tests/test_p017_mirror_directional.py`.

The directional counts use the same anchor Möbius / CRT machinery as MC01; no new external theorem is introduced.
