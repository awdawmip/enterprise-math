# Enterprise BRC Half-Coupling Inert-Plus Terminating Jacobi-Jet Certificate — Research Return

Status: `FINAL_FROZEN / EXACT_STRICT_REDUCTION / CM_HASSE_ZERO_PROVED / SIMPLE_ROOT_PROVED / FULL_JT2_OPEN`

Date: `2026-09-07`

Researcher-ID: `EM-EBP6JT-25C94A`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE`

Publication: `TP2-A19C97A703AF47D1CBEC`

Claim: `chatgpt-ebp6jt-20260907-1010-sol7f3a`

Execution: `ER-0E7A6ED487BA644FCD10`

Execution branch: `research/enterprise-brc-half-coupling-inert-plus-terminating-jacobi-jet-certificate-em-ebp6jt-25c94a`

## 1. Frozen disposition

`PRIMARY_VERDICT = EXACT_STRICT_REDUCTION_WITH_NEW_THEOREM_LEVEL_CM_STEP`.

`HARD_TARGET_DISPOSITION = ACHIEVED_BY_STRICT_REDUCTION`.

`CM_HASSE_ZERO = PROVED_FOR_BOTH_TARGET_CLASSES`.

`SIMPLE_ROOT_TRANSVERSALITY = PROVED`.

`JT0 = EQUIVALENT_TO_ONE_UNIT_RECIPROCITY_CERTIFICATE_UR / OPEN`.

`JT2 = EQUIVALENT_TO_UR_PLUS_ONE_SECOND_DIGIT_LIFT / OPEN`.

No finite scan is promoted to proof. No conjectural statement of Zhi-Wei Sun or Zhi-Hong Sun is imported as a theorem.

This execution recovers a mathematically substantive but non-main prior execution of the same task, rechecks the reduction against the current frozen parent interface, and independently reruns the exact finite regression. The accepted mathematical content below is the proof itself, not the existence of the old branch.

## 2. Frozen parent interface

Let

\[
p=6m+1,\qquad p\equiv13,19\pmod{24},
\]

so `m mod 4` is respectively `2` or `3`. Keep the accepted parent definitions

\[
\Phi_m(x,z)=\sum_{k=0}^{6m}\frac{(-x)_k(-2x)_k}{(k!)^2}z^k,
\qquad
\Psi_m=(1+12z\partial_z)\Phi_m,
\]

all evaluated at `(x,z)=(m,1/2)`, and

\[
a=\frac{\Phi}{p}-\frac{\Phi_x}{6}.
\]

The task target is

\[
\left(a+\frac{p\Phi_{xx}}{72}\right)
\left(\Psi-\frac{p\Psi_x}{6}\right)
\equiv1+pR_p\pmod{p^2}.
\tag{JT2}
\]

Its first digit is

\[
a\Psi\equiv1\pmod p.
\tag{JT0}
\]

The frozen parent reconstruction also gives, for

\[
B_0=1,\qquad
\frac{B_{k+1}}{B_k}=\frac{(6k+1)(3k+1)}{36(k+1)^2},
\]

\[
g=\sum_{k=0}^{p-1}B_k,\qquad
h=\sum_{k=0}^{p-1}(12k+1)B_k,
\]

that `p | g` on the target lane and

\[
\frac gp\equiv a+\frac{p\Phi_{xx}}{72}\pmod{p^2},
\qquad
h\equiv\Psi-\frac{p\Psi_x}{6}\pmod{p^2}.
\tag{PARENT}
\]

Thus the cutoff-sensitive second parameter derivative is retained inside `g/p mod p^2`; no `Phi_xx` term is discarded in the reduction below.

## 3. Exact terminating quadratic transport

At the integer parameter,

\[
H_m(z):=\Phi_m(m,z)={}_2F_1(-m,-2m;1;z)
=\sum_{k=0}^{m}\binom mk\binom{2m}kz^k.
\]

Modulo `p`, `-m=1/6` and `-2m=1/3`. The classical quadratic transformation

\[
{}_2F_1\left(\frac16,\frac13;1;4u(1-u)\right)
={}_2F_1\left(\frac13,\frac23;1;u\right)
\]

terminates on the right as

\[
{}_2F_1(-2m,2m+1;1;u)=P_{2m}(1-2u).
\]

Writing `t=1-2u`, so `4u(1-u)=1-t^2`, gives the polynomial identity

\[
H_m(1-t^2)=P_{2m}(t)\quad\text{in }\mathbf F_p[t].
\]

Since `P_{2m}` is even, define `Q_m` by

\[
P_{2m}(T)=Q_m(T^2).
\]

Then

\[
\boxed{H_m(z)=Q_m(1-z)\quad\text{in }\mathbf F_p[z].}
\tag{QL}
\]

At `z=1/2`,

\[
\Phi\equiv Q_m(1/2),
\qquad
\Psi=H_m+6H_m'\equiv Q_m(1/2)-6Q_m'(1/2)\pmod p.
\tag{QPsi}
\]

This is a terminating finite identity, not an infinite-series substitution.

## 4. Hesse Hasse invariant and discriminant -24 CM

Choose `t` with `t^2=1/2` and put

\[
u=\frac{1-t}{2}.
\]

Because `2m=(p-1)/3`,

\[
P_{2m}(1-2u)
\equiv
A_p(u):=\sum_{k=0}^{(p-1)/3}\frac{(3k)!}{27^k(k!)^3}u^k
\pmod p.
\tag{H}
\]

Consider the Hesse cubic

\[
E_\lambda:X^3+Y^3+Z^3-3\lambda XYZ=0,
\qquad \lambda^{-3}=u.
\]

The Hasse invariant of a smooth plane cubic is the coefficient of `(XYZ)^(p-1)` in its `(p-1)`-st power. Direct multinomial extraction gives this coefficient as a nonzero scalar times `A_p(u)`: after factoring `(-3lambda)^(p-1)`, Wilson reduction converts

\[
\frac{(p-1)!}{(p-1-3k)!}
\]

to `(-1)^(3k)(3k)!`, while `(-3lambda)^(-3k)` contributes the opposite sign and `27^{-k}u^k`. Hence

\[
A_p(u)=0\iff E_\lambda\text{ is supersingular}.
\tag{HASSE}
\]

For the Hesse pencil,

\[
j(E_\lambda)=\frac{27\lambda^3(\lambda^3+8)^3}{(\lambda^3-1)^3}
=\frac{27(1+8u)^3}{u(1-u)^3}.
\]

Substituting `u=(1-t)/2`, `t^2=1/2`, gives

\[
j=2417472\pm1707264\sqrt2,
\]

the two roots of

\[
X^2-4834944X+14670139392,
\]

the Hilbert class polynomial of discriminant `-24`. Thus the characteristic-zero curve has CM by the order of discriminant `-24` in `Q(sqrt(-6))`.

For both target classes,

\[
\left(\frac{-6}{p}\right)=-1.
\]

Therefore each target prime is inert in `Q(sqrt(-6))`; since `p>3` and reduction is good, Deuring CM reduction makes the specialized Hesse cubic supersingular. By `(HASSE)` and `(H)`,

\[
\boxed{Q_m(1/2)=P_{2m}(t)=0\pmod p}
\tag{CM0}
\]

uniformly for both `p mod 24 = 13` and `19`.

## 5. The CM zero is simple

`P_n`, with `n=2m<p`, satisfies

\[
(1-T^2)P_n''-2TP_n'+n(n+1)P_n=0.
\]

At `t^2=1/2`, the leading coefficient is nonzero. If both `P_n(t)` and `P_n'(t)` vanished, the differential equation gives `P_n''(t)=0`; differentiating repeatedly forces every derivative through degree `n` to vanish. Because `n<p`, the relevant factorials are units, so the Taylor expansion would force `P_n=0`, contradicting `P_n(1)=1`.

Hence `P'_{2m}(t) != 0`. Since

\[
P'_{2m}(t)=2tQ'_m(t^2)
\]

and `t != 0`,

\[
\boxed{Q'_m(1/2)\ne0\pmod p.}
\tag{SIMPLE}
\]

## 6. Exact disposition of JT0

From `(CM0)` and `(QPsi)`,

\[
\Psi\equiv-6Q'_m(1/2)\pmod p,
\]

and `(SIMPLE)` shows this is a unit. Put

\[
G_p:=g/p\in\mathbf Z_p.
\]

The frozen parent reconstruction gives `G_p=a mod p`, so `(JT0)` is exactly equivalent to

\[
\boxed{G_p(-6Q'_m(1/2))\equiv1\pmod p.}
\tag{UR}
\]

Equivalently,

\[
G_p\equiv-\frac1{6Q'_m(1/2)}\pmod p.
\]

Thus the first digit has been strictly reduced from the parameter-jet statement to one nonzero unit reciprocity between the divided p-adic period and the derivative of the supersingular Hasse polynomial.

`UR` remains unproved and unrefuted here.

## 7. Exact second-digit disposition

Using `(PARENT)`, `(JT2)` is exactly equivalent to

\[
\boxed{G_ph\equiv1+pR_p\pmod{p^2}.}
\tag{SCALAR-JT2}
\]

Once `UR` holds, define

\[
\Delta_p:=\frac{G_ph-1}{p}\pmod p.
\]

The entire remaining second digit is then

\[
\boxed{\Delta_p\equiv R_p\pmod p.}
\tag{LIFT}
\]

No cutoff term was removed: `Phi_xx` is still encoded in `G_p mod p^2` through `(PARENT)`.

Therefore

\[
JT2\iff UR+LIFT,
\]

with `CM0` and `SIMPLE` proved independently.

## 8. Two structurally distinct mechanisms

Mechanism A — terminating hypergeometric/Legendre route: the quadratic transformation proves `(QL)` and identifies the derivative datum at the fixed point. A finite creative-microscoping/WZ search around this reduced interface did not produce an exact closing certificate for `UR` or `LIFT`; no nearby but nonmatching identity is imported.

Mechanism B — Hesse/CM/Frobenius route: Hasse-invariant extraction plus the discriminant `-24` singular modulus and Deuring inert reduction proves `(CM0)` uniformly. The natural ordinary CM ASD theorem of Coster–van Hamme is a split/unit-root theorem requiring `(-d/p)=+1`; this lane has `(-6/p)=-1`, so direct instantiation is an exact route mismatch. The remaining object is genuinely supersingular.

This is a route-specific no-go plus a smaller live certificate, not a literature gap relabeled as proof.

## 9. Deterministic regression

Checker:

`scripts/check_enterprise_brc_half_coupling_inert_plus_terminating_jacobi_jet_certificate.py`

The current execution independently reran the exact Fraction/arithmetic checker for every target prime below 2000:

- total target primes: `77`;
- class `13 mod 24`: `40`;
- class `19 mod 24`: `37`;
- quadratic/Legendre transport failures: `0`;
- CM-Hasse-zero failures: `0`;
- simple-root failures: `0`;
- `UR` regression failures: `0`;
- `JT2/LIFT` regression failures: `0`.

This finite run is falsification/regression support only for `UR` and `LIFT`. The theorem status of `(CM0)` and `(SIMPLE)` comes from Sections 4–5.

## 10. Final freeze

`CM_HASSE_ZERO = PROVED`.

`CM_HASSE_ZERO_SCOPE = p mod 24 in {13,19}`.

`SIMPLE_ROOT_TRANSVERSALITY = PROVED`.

`JT0 = EQUIVALENT_TO_UR / OPEN`.

`JT2 = EQUIVALENT_TO_UR_PLUS_LIFT / OPEN`.

`CUTOFF_SENSITIVE_PHI_XX = RETAINED_INSIDE_G_OVER_P_MOD_P2`.

`ORDINARY_SPLIT_CM_ASD_DIRECT_INSTANTIATION = NO_GO_ON_INERT_LANE`.

`FINITE_REGRESSION = 77_TARGET_PRIMES_BELOW_2000 / ZERO_FAILURES / NOT_PROOF_OF_UR_OR_LIFT`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH = NOT_GRANTED`.

`NOVELTY_OR_PRIORITY_CLAIM = NONE`.

Smallest live residue: prove the discriminant `-24` supersingular unit reciprocity `(UR)`; after that, prove the single second-digit lift `(LIFT)`. Do not reopen the CM zero, simple-root lemma, or the parent finite-tail/harmonic-block bookkeeping.
