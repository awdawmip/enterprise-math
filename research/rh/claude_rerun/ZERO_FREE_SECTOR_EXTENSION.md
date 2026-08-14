# ZERO_FREE_SECTOR_EXTENSION — corrected explicit PF-order gain using the 2026 zero-free region

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`

Status:

`NEW_WEAKER_RESULT_SURVIVES / EXPLICIT_PF_ORDER_EXTENSION_V2 / DERIVED_FROM_PUBLISHED_THEOREMS / NOVELTY_UNCHECKED / RH_NOT_CLOSED`

This file supersedes the previous numerical constants in the same path. The theorem-grade
published verification input is `H=3*10^12`; the zero-free constant is updated to the stronger
2026 value `R=4.896`.

## 1. Inputs

Let

`G(z)=sum_(k>=0) a_k z^k = (1/8) xi(1/2+sqrt(z)/2)`.

A nontrivial zeta zero

`rho=beta+i gamma = 1/2+delta+i gamma`

corresponds to the zero

`w=4(delta+i gamma)^2`

of `G`. Its angular defect from the negative real axis is

`theta(gamma,delta)=2 atan(|delta|/|gamma|)`.

Use two published rigorous inputs.

1. Platt–Trudgian prove RH for all zeros with `0<gamma<=H`,
   `H=3,000,000,000,000`.

2. Bellotti–Trudgian–Yang (arXiv:2603.21490, 2026) prove

   `zeta(sigma+it) != 0`
   for `t>=3` and
   `sigma >= 1-1/(R log t)`,
   `R=4.896`.

By functional-equation symmetry, every zero above `H` satisfies

`|delta| < 1/2 - 1/(R log|gamma|)`.

Schoenberg's genus-zero sector criterion therefore gives PF order `r` whenever

`theta < pi/(r+1)`

for every zero of `G`.

## 2. Monotone angular envelope

For `t>=H` define

`x(t)=(1/2-1/(R log t))/t`,
`Theta(t)=2 atan(x(t))`.

Then

`x'(t)=
 [1/(R(log t)^2) - (1/2-1/(R log t))]/t^2`.

At these heights the bracket is negative, so `x` and `Theta` are strictly decreasing.
The worst unverified angle is therefore at the verification boundary.

Hence the exact symbolic safe-order statement is

`boxed:
 r <= floor(pi/Theta(H))-1
   = floor(pi/(2 atan((1/2-1/(R log H))/H)))-1.`

No assumption is made that zeros above `H` lie on the critical line.

## 3. Conservative rational certificate

Avoid floating evaluation of `log`, `atan`, or `pi`.

Use

`atan y<y`,
`log H<29`,
`pi>3.1415`.

The logarithm bound follows from the exact rational inequality
`(2.718)^29>H` together with `e>2.718`.

Thus

`1/(R log H)>1/(29R)`

and

`Theta(H)<(1-2/(29R))/H`.

It is sufficient that

`r+1 <= 3.1415 H/(1-2/(29R))`.

With

`H=3,000,000,000,000`,
`R=4.896=612/125`,

the right side is exactly

`83,633,013,000,000,000 / 8,749`

and is greater than

`9,559,151,102,983`.

Therefore:

`boxed:
 D_(r,k)>=0 for every k>=0 and every
 1<=r<=9,559,151,102,982.`

Equivalently, the Xi coefficient sequence is unconditionally PF of order at least

`9,559,151,102,982`.

## 4. Conservative comparison with verification height alone

Using only the verified height plus the crude critical-strip bound, the same
`pi>3.1415` certificate gives

`r<=9,424,499,999,999`.

The zero-free refinement therefore adds at least

`134,651,102,983`

certified PF orders over that conservative verification-only certificate.

This comparison deliberately uses the same rational lower bound for `pi` on both sides.

## 5. BRC interpretation

The gain comes from refusing the premature collapse

`unverified zero -> |delta|<1/2 only`.

The pair carrier retains the future-relevant angular defect. The zero-free theorem refines that
branch to

`|delta|<1/2-1/(R log gamma)`

without deciding whether the zero lies on the critical line. The enlarged collection of
sector-safe branches then recoalesces to a stronger finite-order `PF_SAFE` token.

## 6. Boundary and novelty

This is not RH: the zero-free margin tends to zero as the height grows, whereas PF-infinity
requires unbounded order.

The ingredients are published/classical. This task does not claim that the exact numerical
corollary `PF_(9,559,151,102,982)` is new in the literature; novelty remains unchecked.

The result is a reusable theorem-grade input for the weighted boundary-layer BRC rerun.
