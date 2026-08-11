# ZERO_FREE_SECTOR_EXTENSION — explicit PF-order gain from the zeta zero-free region

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`

Status:

`NEW_WEAKER_RESULT_SURVIVES / EXPLICIT_PF_ORDER_EXTENSION / DERIVED_FROM_PUBLISHED_THEOREMS / NOVELTY_UNCHECKED / RH_NOT_CLOSED`

## 1. Inputs

Let

`G(z)=sum_{k>=0} a_k z^k = (1/8) xi(1/2+sqrt(z)/2)`.

A nontrivial zeta zero

`rho=beta+i gamma = 1/2+delta+i gamma`

corresponds to a zero

`w=4(delta+i gamma)^2`

of `G`. Its angular defect from the negative real axis is

`theta(gamma,delta)=pi-|arg w|=2 atan(|delta|/|gamma|)`.

Two published rigorous inputs are used.

1. Platt–Trudgian verify RH through

`H=3,000,175,332,800`.

2. Mossinghoff–Trudgian–Yang prove the classical explicit zero-free region

`beta < 1 - 1/(R log|gamma|)`, `R=5.558691`, for `|gamma|>=2`.

By the functional equation symmetry, every zero above `H` therefore satisfies

`|delta| < 1/2 - 1/(R log|gamma|)`.

Schoenberg's sector criterion, equivalently the conjugate-pair RCC derived in this rerun, implies PF order `r` whenever every zero of `G` satisfies

`theta < pi/(r+1)`.

## 2. Monotone angular envelope

Define for `t>=H`

`x(t)=(1/2 - 1/(R log t))/t`.

Then

`x'(t)=[1/(R(log t)^2) - (1/2 - 1/(R log t))]/t^2`.

For `log t>=2` and `R>5`,

`1/(R(log t)^2)+1/(R log t) <= 3/20 < 1/2`,

so `x'(t)<0`. Hence the largest possible angular defect among all unverified zeros occurs at the verification boundary:

`theta < theta_H := 2 atan(x(H))`.

Therefore every integer rank satisfying

`r+1 <= pi/theta_H`

is unconditionally PF-safe.

This already yields the exact symbolic extension

`r <= floor(pi/(2 atan((1/2-1/(R log H))/H))) - 1`.

No assumption about zeros above `H` lying on the critical line is used.

## 3. Fully conservative rational lower certificate

To avoid relying on a floating evaluation of `log H` or `atan`, use

`atan y < y` for `y>0`.

Also `log H < 29`: indeed the finite exponential-series bound gives

`e > sum_{n=0}^6 1/n! = 1957/720 > 2.718`,

and exact rational arithmetic verifies

`(2.718)^29 > H`.

Thus

`1/(R log H) > 1/(29 R)`

and

`theta_H < (1 - 2/(29R))/H`.

Using the elementary lower bound `pi>3.1415`, it is sufficient that

`r+1 <= 3.1415 H / (1 - 2/(29R))`.

With

`H=3000175332800`, `R=5558691/1000000`,

exact rational arithmetic gives

`3.1415 H / (1 - 2/(29R)) = 7596687039633894670284 / 796010195`

which is greater than

`9,543,454,452,406`.

Hence the completely conservative explicit theorem is:

`boxed: D_{r,k} >= 0 for every k>=0 and every 1<=r<=9,543,454,452,405.`

Equivalently, the Xi coefficient sequence is PF of order at least

`9,543,454,452,405`.

## 4. Comparison with the verification-only sector strip

Using only `|delta|<1/2` above `H` gives the familiar verified-height condition

`r+1 <= pi H`,

i.e. `r<=floor(pi H)-1`.

The new zero-free-region correction replaces the angular bound `1/H` by approximately

`(1 - 2/(R log H))/H`.

At the Platt–Trudgian height this improves the certified PF order by about `1.25%`; a high-precision evaluation of the exact symbolic formula suggests an available extension of about `1.195e11` orders, while the rational certificate above already guarantees an extension of about `1.181e11` orders beyond the verification-only threshold.

The exact integer comparison with `floor(pi H)-1` is a presentation issue only; the theorem-grade new lower bound is the rationally certified rank `9,543,454,452,405` above.

## 5. BRC interpretation

This result was exposed by the conjugate-pair BRC carrier:

- the original verified-zero strip treated every unverified zero as if `|delta|` could approach `1/2` freely;
- the pair RCC retains the angular defect as future-relevant metadata;
- importing the zero-free-region constraint refines that metadata without resolving whether the zero is on the critical line;
- all branches satisfying the sharpened sector signature recoalesce into a larger `NONNEGATIVE/PF_r_SAFE` state.

Thus BRC did not prove RH by branching; it prevented premature collapse of the off-line-zero geometry and exposed an existing analytic constraint that enlarges the safe quotient.

## 6. Boundary of the result

This is not RH. The zero-free margin shrinks slowly as height increases, while PF-infinity requires unbounded rank. The result nevertheless strictly improves the finite-order region obtained from verified zeros alone and is a reusable input for the critical-band rerun.

Prior-art/novelty status: the ingredients are classical/published; whether this exact numerical PF-order corollary has appeared before is not established in this task.
