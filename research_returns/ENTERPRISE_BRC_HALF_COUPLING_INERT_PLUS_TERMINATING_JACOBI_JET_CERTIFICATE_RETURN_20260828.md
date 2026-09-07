# Enterprise BRC Half-Coupling Inert-Plus Terminating Jacobi-Jet Certificate — Research Return

Status: `FINAL_FROZEN / EXACT_STRICT_REDUCTION / CM0+SIMPLE_PROVED / JT2_OPEN_AS_UR+LIFT`

Date: `2026-09-07`

Researcher-ID: `EM-EBP6JT-25C94A`
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE`
Publication: `TP2-A19C97A703AF47D1CBEC`
Claim: `chatgpt-ebp6jt-20260907-1010-sol7f3a`
Execution: `ER-0E7A6ED487BA644FCD10`

## 1. Verdict

`HARD_TARGET_DISPOSITION = ACHIEVED_BY_STRICT_REDUCTION`.

For every prime `p=6m+1` with `p mod 24 in {13,19}` (equivalently `m mod 4 in {2,3}`), this execution proves two new theorem-level facts at the terminating Jacobi interface:

1. the relevant Hasse/Jacobi value vanishes, `Q_m(1/2)=0 mod p`;
2. the zero is simple, `Q'_m(1/2) != 0 mod p`.

Consequently `JT0` is exactly reduced to one nonzero unit-reciprocity certificate `UR`, and the full `JT2` is exactly reduced to `UR` plus one second-digit lift `LIFT`. No finite scan is promoted to theorem and no conjectural Sun statement is used as proof.

This result recovers a mathematically substantive non-main prior execution of the same task and independently revalidates it against the current frozen parent interface.

## 2. Frozen parent interface

Let

`Phi_m(x,z) = sum_{k=0}^{6m} (-x)_k(-2x)_k z^k/(k!)^2`,

`Psi_m = (1+12 z d/dz) Phi_m`,

all derivatives evaluated at `(x,z)=(m,1/2)`, and

`a = Phi/p - Phi_x/6`.

The target is

`(a + p Phi_xx/72)(Psi - p Psi_x/6) = 1 + p R_p (mod p^2)`  (`JT2`),

with first digit `a Psi = 1 (mod p)` (`JT0`).

The frozen parent also gives, with

`B_0=1`, `B_{k+1}/B_k=((6k+1)(3k+1))/(36(k+1)^2)`,

`g=sum_{k=0}^{p-1} B_k`, `h=sum_{k=0}^{p-1}(12k+1)B_k`, and `p | g`,

`g/p = a + p Phi_xx/72 (mod p^2)`,

`h = Psi - p Psi_x/6 (mod p^2)`.

Thus the cutoff-sensitive `Phi_xx` contribution is retained exactly inside `g/p mod p^2` throughout the reduction.

## 3. Terminating quadratic/Legendre transport

At integer parameter,

`H_m(z):=Phi_m(m,z)=_2F_1(-m,-2m;1;z)=sum_{k=0}^m C(m,k)C(2m,k)z^k`.

Modulo `p`, `-m=1/6` and `-2m=1/3`. The classical quadratic transformation

`_2F_1(1/6,1/3;1;4u(1-u)) = _2F_1(1/3,2/3;1;u)`

terminates on the right as `_2F_1(-2m,2m+1;1;u)=P_{2m}(1-2u)`.
Writing `t=1-2u`, hence `4u(1-u)=1-t^2`, yields

`H_m(1-t^2)=P_{2m}(t)` in `F_p[t]`.

Because `P_{2m}` is even, define `Q_m` by `P_{2m}(T)=Q_m(T^2)`. Then

`H_m(z)=Q_m(1-z)` in `F_p[z]`.                                                   (`QL`)

At `z=1/2`,

`Phi = Q_m(1/2)` and `Psi = Q_m(1/2)-6 Q'_m(1/2) (mod p)`.                 (`QPsi`)

This is a finite terminating polynomial identity.

## 4. Hesse Hasse invariant and CM discriminant -24

Choose `t^2=1/2` and put `u=(1-t)/2`. Since `2m=(p-1)/3`,

`P_{2m}(1-2u) = A_p(u) := sum_{k=0}^{(p-1)/3} (3k)!/(27^k(k!)^3) u^k (mod p)`.

For the Hesse cubic

`E_lambda: X^3+Y^3+Z^3-3 lambda XYZ=0`, `lambda^(-3)=u`,

the Hasse invariant is the coefficient of `(XYZ)^(p-1)` in the `(p-1)`-st power. Direct multinomial extraction and Wilson reduction show that coefficient is a nonzero scalar times `A_p(u)`. Hence

`A_p(u)=0  <=>  E_lambda is supersingular`.                                    (`HASSE`)

The Hesse `j`-invariant is

`j=27 lambda^3(lambda^3+8)^3/(lambda^3-1)^3 = 27(1+8u)^3/[u(1-u)^3]`.

At `u=(1-t)/2`, `t^2=1/2`, this gives

`j = 2417472 +/- 1707264 sqrt(2)`,

the roots of `X^2-4834944 X+14670139392`, the Hilbert class polynomial of discriminant `-24`. Thus the characteristic-zero curve has CM in `Q(sqrt(-6))`.

For both `p mod 24 = 13` and `19`, `(-6/p)=-1`; the target primes are inert in `Q(sqrt(-6))`. For `p>3` the specialization has good reduction, so Deuring CM reduction makes it supersingular. By `HASSE`,

`Q_m(1/2)=0 (mod p)`.                                                           (`CM0`)

This covers both requested residue classes uniformly.

## 5. Simplicity of the zero

`P_n`, `n=2m<p`, satisfies

`(1-T^2)P_n'' - 2T P_n' + n(n+1)P_n = 0`.

At `t^2=1/2` the leading coefficient is nonzero. If both `P_n(t)` and `P_n'(t)` vanished, the differential equation gives `P_n''(t)=0`; repeated differentiation forces every derivative through degree `n` to vanish. Since `n<p`, the factorials are units, so the Taylor expansion would force `P_n=0`, contradicting `P_n(1)=1`.

Thus `P'_{2m}(t) != 0`. Since `P'_{2m}(t)=2t Q'_m(t^2)` and `t!=0`,

`Q'_m(1/2) != 0 (mod p)`.                                                       (`SIMPLE`)

## 6. Exact disposition of JT0

By `CM0`, `QPsi`, and `SIMPLE`,

`Psi = -6 Q'_m(1/2) (mod p)`, a unit.

Put `G_p=g/p`. The frozen parent gives `G_p=a (mod p)`. Therefore

`JT0  <=>  G_p (-6 Q'_m(1/2)) = 1 (mod p)`.                                   (`UR`)

Equivalently,

`G_p = -1/[6 Q'_m(1/2)] (mod p)`.

So the first digit is strictly reduced from a parameter-jet congruence to one supersingular Hasse-normal divided-period unit reciprocity. `UR` remains open.

## 7. Exact second-digit disposition

The frozen parent reconstruction gives

`JT2  <=>  G_p h = 1 + p R_p (mod p^2)`.                                      (`SCALAR-JT2`)

Once `UR` holds, define

`Delta_p=((G_p h)-1)/p (mod p)`.

Then the entire remaining second digit is exactly

`Delta_p = R_p (mod p)`.                                                        (`LIFT`)

Hence `JT2 <=> UR + LIFT`, with `CM0` and `SIMPLE` already proved. The cutoff-sensitive `Phi_xx` term has not been discarded; it remains encoded in `G_p mod p^2`.

## 8. Two structurally distinct mechanisms

Mechanism A: terminating quadratic hypergeometric/Legendre transport proves `QL` and identifies the transverse derivative datum. A finite WZ/creative-microscoping search around the reduced interface did not yield a matching all-prime certificate for `UR` or `LIFT`; no nonmatching identity is imported.

Mechanism B: Hesse Hasse-invariant extraction plus discriminant `-24` CM and Deuring inert reduction proves `CM0`. The natural Coster–van Hamme ordinary CM ASD route is a split/unit-root theorem requiring `(-d/p)=+1`; here `(-6/p)=-1`, so direct instantiation is an exact route mismatch. The surviving reciprocity is genuinely supersingular.

## 9. Deterministic regression

The task-local exact checker was independently rerun for all target primes `p<2000`:

- target primes: `77`;
- class `13 mod 24`: `40`;
- class `19 mod 24`: `37`;
- quadratic/Legendre transport failures: `0`;
- CM-Hasse-zero failures: `0`;
- simple-root failures: `0`;
- `UR` regression failures: `0`;
- `JT2/LIFT` regression failures: `0`.

This scan is regression/falsification support only for `UR` and `LIFT`. The theorem status of `CM0` and `SIMPLE` comes from Sections 4–5.

## 10. Final freeze

`CM_HASSE_ZERO = PROVED`.
`CM_HASSE_ZERO_SCOPE = p mod 24 in {13,19}`.
`SIMPLE_ROOT_TRANSVERSALITY = PROVED`.
`JT0 = EQUIVALENT_TO_UR / OPEN`.
`JT2 = EQUIVALENT_TO_UR_PLUS_LIFT / OPEN`.
`CUTOFF_SENSITIVE_PHI_XX = RETAINED_INSIDE_G_OVER_P_MOD_P2`.
`ORDINARY_SPLIT_CM_ASD_DIRECT_INSTANTIATION = NO_GO_ON_INERT_LANE`.
`FINITE_REGRESSION = 77 TARGET PRIMES BELOW 2000 / ZERO FAILURES / NOT PROOF OF UR OR LIFT`.
`FOUNDATION_MUTATION = NONE`.
`WORKING_TRUTH = NOT_GRANTED`.
`NOVELTY_OR_PRIORITY_CLAIM = NONE`.

Smallest live residue: prove discriminant `-24` supersingular unit reciprocity `UR`; after that prove the single lift `LIFT`. Do not reopen the CM zero, simple-root lemma, or the parent finite-tail/harmonic-block bookkeeping.
