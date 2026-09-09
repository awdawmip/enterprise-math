# EM-FREE-W59A / JT2 UR-Legendre + QTF3 state-machine handoff

Status: `DURABLE RESEARCH HANDOFF / TWO OPEN PROOF FRONTIERS / NOT FOUNDATION`
Date: `2026-09-09`
Researcher provenance: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Parent objective id: `EM-FREE-W59A-JT2-RAMANUJAN-LEGENDRE`

## 1. Read this first

This file is the project-native continuation point for the Ramanujan/Legendre supercongruence line that was reduced to two minimal targets:

1. `UR-Legendre`: a slope-value identity for ordinary Legendre polynomials modulo `p^2`;
2. `QTF3`: the quadratic transformation at the fixed point `u=1/2` lifted to modulo `p^3`.

Successor researchers should consume the closed facts and reductions below. Do not restart CM0 or simple-root transversality.

Account-level provenance mirror:
`awdawmip/chatgpt-global-knowledge@f48cd4d076f61a5b804a7617158359e198b2fd5d`
at
`journal/progressive-number-theory/2026-09-09/20260909T105443+0800-ur-legendre-barycentric-lift.md`.

The external generalized-Legendre interface used below is Zhi-Hong Sun,
*Generalized Legendre polynomials and related congruences modulo p^2*,
arXiv:1101.5386.

## 2. Closed facts and do-not-replay boundary

The following parts of the current route are already closed and are inputs to successor tasks:

- `CM0`: the relevant CM zero congruence.
- simple-root transversality at the CM point.
- the strict reduction of the original unit-reciprocity obstruction
  `G_p(-6 Q_m'(1/2)) == 1 (mod p)`
  to the ordinary-Legendre target below.
- the five earlier harmonic-block decompositions are retired as the primary proof route and should not be reconstructed unless a successor proves that a missing identity genuinely requires one of them.

BRC observer discipline for this frontier:

- preserve integer / `p`-adic valuation information before quotienting;
- preserve the `t` and `-t` Frobenius ports;
- preserve first-jet / derivative data;
- preserve the `p^2` parity-defect coordinates rather than replacing them by exact even/odd identities;
- do not collapse labeled provenance when the next operation differentiates, divides by `p`, or compares the two ports.

## 3. UR-Legendre reduction

Let
`p = 3 n + 1`
and let `t` satisfy
`t^2 = 1/2`
in the current Frobenius-exchanged branch. The current route uses
`Q_m'(1/2) = P_n'(t)/(2t)`.

The minimal UR target is

`(P_{2n}(t) + 2 P_n(t)) P_n'(t) == -p t (mod p^2)`.

Define Sun's generalized Legendre polynomial

`B(x) = P_{p-1}(-1/3, x)`.

For
`C_k(a)=binom(a,k) binom(-1-a,k)`,
one has the exact parameter symmetry
`C_k(a)=C_k(-1-a)`.
Since
`-1/3 = n - p/3`
and
`2n = -1-n+p`,
the coefficientwise first-order `p`-adic Taylor comparison gives

`3 C_k(-1/3) == C_k(2n) + 2 C_k(n) (mod p^2)`,

hence

`3 P_{p-1}(-1/3,x) == P_{2n}(x) + 2P_n(x) (mod p^2)`.

This is the barycentric lift that turns the earlier divided-value candidate into a short proved derivation at the current precision. At the CM zero it gives

`lambda_p = B(t)/p == (P_{2n}(t)+2P_n(t))/(3p) (mod p)`,

subject only to the already-closed divisibility supplied by CM0.

Therefore UR-Legendre is equivalent to the local slope-value identity

`3 B(t) P_n'(t) == -p t (mod p^2)`.

This is the hard target of the first published task.

## 4. Sun recurrence interface and parity-defect carrier

Set

`A(x)=P_{p-1}(2/3,x)`,
`B(x)=P_{p-1}(-1/3,x)`,
`C(x)=P_{p-1}(-4/3,x)`.

The parameter recurrence at `a=-1/3` is used in the form

`2A(x) - xB(x) - C(x) == -2 p^2 ((x-1)/2)^p (mod p^3)`,

and its differentiated form at the required precision is

`2A'(x) - xB'(x) - B(x) - C'(x) == 0 (mod p^2)`.

Modulo `p`, the three generalized parameters reduce to the adjacent ordinary Legendre indices
`P_{n+1}, P_n, P_{n-1}`.

At the Frobenius pair `t,-t`, the useful reflection information is only modulo `p^2`. Therefore retain

`A(t)+A(-t)=p^2 alpha`,
`B(t)-B(-t)=p^2 beta`,
`C(t)+C(-t)=p^2 gamma`

rather than setting these defects to zero.

In the exchanged-port case `t^p=-t`, adding the recurrence at the two ports yields the defect balance

`2 alpha - t beta - gamma == 2 (mod p)`,

after evaluating the Frobenius image of `((x-1)/2)^p`.

The missing proof step is to combine this defect balance with the derivative recurrence and ordinary-Legendre transversality so that the adjacent generalized values disappear and the slope-value identity for `B(t)` emerges.

Do not report this last elimination as proved until the algebra is fully closed.

## 5. QTF3 / fixed-point quadratic-transform frontier

Let the current quadratic-transform defect be

`D_p(u)=L_p(u)-F_p(4u(1-u))`.

After removing the forced factor `u^p p^2`, write the residual as `r_p(u)`. The current compressed differential equation is

`Dop r_p(u) = (2/9)(1+u+...+u^(p-2))`,

where

`Dop = u(1-u) d^2/du^2 + (1-2u) d/du - 2/9`.

The operator commutes with `u <-> 1-u`, while the displayed inhomogeneous term is reflection-antisymmetric in the current finite-field setting. Thus

`r_p(u)+r_p(1-u)`

lies in the homogeneous Hasse solution space. The previous numerical observation that the remaining defect lies in the one-dimensional line
`(1+sqrt(2)) F_p`
has therefore been reduced to a single normalization constant.

The fixed-point target is

`sum_{k=0}^{p-1} (1/3)_k (2/3)_k / ((k!)^2 2^k)`
`==`
`sum_{k=0}^{p-1} (1/6)_k (1/3)_k / (k!)^2`
`(mod p^3)`.

A successor may use the differential-equation/reflection route or a genuinely shorter proof, but the final result must retain the truncation boundary and full `p^3` precision.

## 6. Current parent reduction

The current architecture is

`JT2 <= UR-Legendre + QTF3 / one-scalar LIFT`.

No successor should infer that JT2 is already proved. The two published tasks below are parallel proof obligations. A JT2 integration task should be published only after their returned results establish the required inputs.

## 7. Published task map

- `RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT`
  - prove the Sun parity-defect elimination and the slope-value identity;
  - first route to consume.
- `RS-EMW59A-JT2-QTF3-FIXED-POINT`
  - prove the fixed-point quadratic transformation modulo `p^3`.

Both tasks point back to this handoff as their first source. Publication of the tasks changes execution availability only; it does not itself certify the mathematical claims.
