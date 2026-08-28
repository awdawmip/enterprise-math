# Enterprise BRC Half-Coupling Inert-Plus Terminating Jacobi-Jet Certificate — Research Return

Status: `FINAL_FROZEN / PARTIAL_STRICT_REDUCTION / CM_HASSE_ZERO_PROVED / FULL_JT2_OPEN`

Date: `2026-08-28`

Researcher-ID: `EM-EBP6JT-7A4C21`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE`

Publication: `TP2-A19C97A703AF47D1CBEC`

Claim: `chatgpt-ebp6jt-20260828-1426-7a4c21`

Execution branch: `research/enterprise-brc-half-inert-plus-terminating-jacobi-jet-certificate-em-ebp6jt-7a4c21`

Execution base: `0844f2d167e1665c52731125727e6423cd856dae`

## 1. Frozen disposition

`PRIMARY_VERDICT = PARTIAL_STRICT_REDUCTION_WITH_NEW_THEOREM`.

`CM_HASSE_ZERO = PROVED_FOR_BOTH_TARGET_CLASSES`.

`JT0 = STRICTLY_REDUCED_TO_ONE_NONZERO_UNIT_RECIPROCITY_CERTIFICATE`.

`JT2 = STRICTLY_REDUCED_TO_JT0_UNIT_RECIPROCITY_PLUS_ONE_SECOND_DIGIT_LIFT`.

`FULL_JT2 = UNPROVED_UNREFUTED`.

No finite prime scan is promoted to proof. No statement from Zhi-Hong Sun or Zhi-Wei Sun that is labelled conjectural is imported as a theorem.

The main advance is that the formerly conjectural-looking zero at the Jacobi/Legendre fixed point is no longer part of the open target. For every prime

\[
p=6m+1,\qquad p\equiv13,19\pmod{24},
\]

the task-local Jacobi polynomial satisfies

\[
\boxed{Q_m(1/2)=0\pmod p}
\]

for a structural reason: it is the Hasse invariant of a Hesse cubic whose \(j\)-invariant is a discriminant \(-24\) CM singular modulus, and the target primes are inert in \(\mathbf Q(\sqrt{-6})\). Deuring supersingular reduction therefore forces the Hasse invariant to vanish.

Moreover the zero is simple:

\[
\boxed{Q'_m(1/2)\ne0\pmod p}.
\]

Consequently the first digit `(JT0)` is exactly one unit reciprocity identity, and the second digit of `(JT2)` is exactly one cutoff-safe scalar lift defect.

## 2. Frozen parent interface

Keep the accepted parent definitions

\[
\Phi_m(x,z)=
\sum_{k=0}^{6m}
\frac{(-x)_k(-2x)_k}{(k!)^2}z^k,
\qquad
\Psi_m=(1+12z\partial_z)\Phi_m,
\]

evaluated at \((x,z)=(m,1/2)\), and

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

The parent also proved the exact \(p\)-adic reconstructions

\[
g\equiv \Phi-\frac{p\Phi_x}{6}
+\frac{p^2\Phi_{xx}}{72}\pmod{p^3},
\]

\[
h\equiv \Psi-\frac{p\Psi_x}{6}\pmod{p^2},
\]

where

\[
B_0=1,\qquad
\frac{B_{k+1}}{B_k}
=
\frac{(6k+1)(3k+1)}
{36(k+1)^2},
\]

\[
g=\sum_{k=0}^{p-1}B_k,
\qquad
h=\sum_{k=0}^{p-1}(12k+1)B_k.
\]

On the target lane \(p\mid g\), so put

\[
G_p:=\frac gp\in\mathbf Z_p.
\]

Then the frozen parent interface gives

\[
G_p\equiv a+\frac{p\Phi_{xx}}{72}\pmod{p^2}.
\]

This normalization is useful because it retains the cutoff-sensitive second derivative automatically; no tail or second-jet term is discarded below.

## 3. Exact quadratic / Legendre transport

At the integer point \(x=m\),

\[
H_m(z):=\Phi_m(m,z)
=
{}_2F_1(-m,-2m;1;z)
=
\sum_{k=0}^{m}
\binom mk\binom{2m}k z^k.
\]

Because \(p=6m+1\),

\[
-m\equiv\frac16,\qquad
-2m\equiv\frac13\pmod p.
\]

Use the classical quadratic transformation

\[
{}_2F_1\!\left(\frac16,\frac13;1;4u(1-u)\right)
=
{}_2F_1\!\left(\frac13,\frac23;1;u\right).
\]

Modulo \(p\), the right side terminates as

\[
{}_2F_1(-2m,2m+1;1;u)
=
P_{2m}(1-2u).
\]

Set \(t=1-2u\). Since \(4u(1-u)=1-t^2\),

\[
H_m(1-t^2)=P_{2m}(t)\qquad\text{in }\mathbf F_p[t].
\tag{QL1}
\]

Because \(P_{2m}\) is even, define \(Q_m\) by

\[
P_{2m}(T)=Q_m(T^2).
\]

Equation `(QL1)` is equivalent to the exact polynomial identity

\[
\boxed{H_m(z)=Q_m(1-z)\quad\text{in }\mathbf F_p[z].}
\tag{QL}
\]

Thus at \(z=1/2\),

\[
\Phi\equiv Q_m(1/2)\pmod p,
\]

and, because \(\Psi=H_m+6H_m'\) at \(z=1/2\),

\[
\Psi\equiv
Q_m(1/2)-6Q'_m(1/2)
\pmod p.
\tag{QPsi}
\]

## 4. The Hesse Hasse invariant at the same point

Let \(t^2=1/2\) and put

\[
u=\frac{1-t}{2}.
\]

Then \(2m=(p-1)/3\), and the polynomial

\[
P_{2m}(1-2u)
=
{}_2F_1(-2m,2m+1;1;u)
\]

is congruent modulo \(p\) to

\[
A_p(u):=
\sum_{k=0}^{(p-1)/3}
\frac{(3k)!}{27^k(k!)^3}u^k.
\tag{H}
\]

Now consider the Hesse cubic

\[
E_\lambda:\quad
X^3+Y^3+Z^3-3\lambda XYZ=0,
\qquad
\lambda^{-3}=u.
\]

The Hasse invariant of a smooth plane cubic is the coefficient of
\((XYZ)^{p-1}\) in its \((p-1)\)-st power. For this Hesse model that coefficient is

\[
\sum_{k=0}^{(p-1)/3}
\frac{(p-1)!}
{k!^3(p-1-3k)!}
(-3\lambda)^{p-1-3k}.
\]

Factor \((-3\lambda)^{p-1}\). Modulo \(p\),

\[
\frac{(p-1)!}{(p-1-3k)!}
\equiv
(-1)^{3k}(3k)!
=
(-1)^k(3k)!,
\]

whereas

\[
(-3\lambda)^{-3k}
=
(-1)^k\,27^{-k}\lambda^{-3k}.
\]

The signs cancel, and the Hasse coefficient becomes the nonzero scalar
\((-3\lambda)^{p-1}\) times `(H)`. Therefore

\[
A_p(u)=0
\quad\Longleftrightarrow\quad
E_\lambda\text{ is supersingular}.
\tag{Hasse}
\]

By the Legendre identification above,

\[
A_p(u)=P_{2m}(t)=Q_m(1/2).
\tag{HQ}
\]

## 5. Discriminant \(-24\) CM and inert supersingular reduction

For the Hesse cubic,

\[
j(E_\lambda)
=
\frac{27\lambda^3(\lambda^3+8)^3}
{(\lambda^3-1)^3}
=
\frac{27(1+8u)^3}{u(1-u)^3}.
\tag{jH}
\]

Substituting \(u=(1-t)/2\), \(t^2=1/2\), gives

\[
j
=
2417472-3414528\,t.
\]

Thus the two choices of \(t\) give

\[
\boxed{
j=2417472\pm1707264\sqrt2.
}
\]

They are precisely the two roots of the Hilbert class polynomial of discriminant \(-24\),

\[
X^2-4834944X+14670139392.
\]

Hence, over characteristic zero, the corresponding elliptic curve has CM by the order of discriminant \(-24\) in

\[
K=\mathbf Q(\sqrt{-6}).
\]

For \(p\equiv13,19\pmod{24}\),

\[
\left(\frac{-6}{p}\right)=-1.
\]

Indeed:

- if \(p\equiv13\pmod{24}\), then
  \(({-1}/p)=1\), \((2/p)=-1\), \((3/p)=1\);
- if \(p\equiv19\pmod{24}\), then
  \(({-1}/p)=-1\), \((2/p)=-1\), \((3/p)=-1\).

So every target prime is inert in \(K\). Since \(p>3\) and the specialized Hesse model has good reduction, Deuring's CM reduction theorem implies that its reduction is supersingular. By `(Hasse)` and `(HQ)`,

\[
\boxed{
Q_m(1/2)=P_{2m}(t)=0\pmod p
}
\tag{CM0}
\]

for every target prime.

This proves, for the two residue classes needed here, the zero branch that appears conjecturally in Zhi-Hong Sun's 2011 Legendre-polynomial formulation. No claim is made about the other branches of that conjecture.

## 6. The CM zero is simple

The Legendre polynomial \(P_n\), \(n=2m<p\), satisfies

\[
(1-T^2)P_n''-2TP_n'+n(n+1)P_n=0.
\]

At \(t^2=1/2\), \(1-t^2\ne0\). If both \(P_n(t)\) and \(P_n'(t)\) vanished, the differential equation would give \(P_n''(t)=0\). Differentiating the equation repeatedly then forces every derivative of \(P_n\) at \(t\) to vanish. Since \(\deg P_n=n<p\), all factorials up to degree \(n\) are units modulo \(p\); its Taylor expansion would therefore make \(P_n\) the zero polynomial, contradicting \(P_n(1)=1\).

Thus

\[
P'_{2m}(t)\ne0.
\]

Because

\[
P'_{2m}(t)=2tQ'_m(t^2)
\]

and \(t\ne0\),

\[
\boxed{Q'_m(1/2)\ne0\pmod p.}
\tag{SIMPLE}
\]

So the Hasse zero is genuinely transverse.

## 7. Exact disposition of JT0

Combine `(CM0)` with `(QPsi)`:

\[
\boxed{
\Psi\equiv-6Q'_m(1/2)\pmod p,
}
\]

and `(SIMPLE)` shows that this is a unit.

The frozen parent reconstruction gives

\[
G_p=\frac gp\equiv a\pmod p.
\]

Therefore `(JT0)` is equivalent to

\[
\boxed{
G_p\,(-6Q'_m(1/2))\equiv1\pmod p.
}
\tag{UR}
\]

Equivalently,

\[
\boxed{
G_p\equiv
-\frac1{6Q'_m(1/2)}
\pmod p.
}
\]

This is the smallest first-digit obstruction after the new CM theorem. The unknown statement is no longer a zero/nonzero question and no longer contains a Jacobi value: it is a reciprocity between

1. the divided \(p\)-adic period \(G_p=g/p\), and
2. the inverse derivative of the supersingular Hasse polynomial.

`UR` remains open in this execution.

## 8. Exact second-digit disposition of JT2

Using the frozen parent reconstructions,

\[
G_p
\equiv
a+\frac{p\Phi_{xx}}{72}
\pmod{p^2},
\]

\[
h
\equiv
\Psi-\frac{p\Psi_x}{6}
\pmod{p^2}.
\]

Hence `(JT2)` is exactly

\[
\boxed{
G_p h\equiv1+pR_p\pmod{p^2}.
}
\tag{SCALAR-JT2}
\]

Once `UR` holds, define the integral second-digit defect

\[
\Delta_p:=
\frac{G_ph-1}{p}\pmod p.
\]

Then the remaining lift is precisely

\[
\boxed{
\Delta_p\equiv R_p\pmod p.
}
\tag{LIFT}
\]

Thus the full target has been decomposed into two typed scalar units:

- `UR`: the supersingular Hasse-normal unit reciprocity;
- `LIFT`: one second-order Frobenius/reflected-tail lift defect.

The cutoff-sensitive \(\Phi_{xx}\) contribution remains present inside
\(G_p\bmod p^2\). This reduction does **not** drop or replace it.

## 9. Two proof mechanisms and the exact ordinary-ASD no-go

Two structurally different mechanisms were seriously tested.

### Mechanism A — terminating transform / polynomial route

The quadratic hypergeometric transformation gives the exact finite identity `(QL)`. It exposes the point \(z=1/2\) as the square \(t^2=1/2\) on a Legendre polynomial and makes the derivative \(Q'_m(1/2)\) the correct transverse datum.

A finite WZ/creative-microscoping scan was also made around this reduced interface. Nearby terminating identities were found, but no exact identity was located that gives `UR` or `LIFT` at the required \(1/2\) specialization and parameter set. No nonmatching WZ identity is imported.

### Mechanism B — CM / Frobenius route

The Hesse Hasse invariant and discriminant \(-24\) CM argument proves `(CM0)` uniformly in both residue classes.

The natural next literature candidate is Coster–van Hamme's 1991 Atkin–Swinnerton-Dyer supercongruence for Legendre polynomials with CM. However its main theorem assumes

\[
\left(\frac{-d}{p}\right)=+1,
\]

i.e. a split/ordinary prime admitting a \(p\)-adic unit-root factor. Our target has \(d=6\) and

\[
\left(\frac{-6}{p}\right)=-1.
\]

Therefore that theorem does **not** directly instantiate on this lane. This is an exact route mismatch, not merely a missing citation: `UR` is a supersingular divided-period/derivative problem, whereas the cited ordinary ASD theorem is built around a split unit root.

A successor should therefore seek either a supersingular analogue of this CM congruence or a terminating identity that computes the same Hasse-normal divided period.

## 10. Deterministic regression

Checker:

`python scripts/check_enterprise_brc_half_coupling_inert_plus_terminating_jacobi_jet_certificate.py --limit 2000`

Exact finite run:

- target primes checked: `77`;
- \(p\equiv13\pmod{24}\): `40`;
- \(p\equiv19\pmod{24}\): `37`;
- quadratic/Legendre transport failures: `0`;
- CM-Hasse zero failures: `0`;
- simple-root failures: `0`;
- `UR` failures: `0`;
- `(JT2)` / `LIFT` failures: `0`.

The checker independently constructs \(P_{2m}\) and \(Q_m\) over \(\mathbf F_p\), checks the polynomial transport, and computes \(g,h,R_p\) from the direct parent recurrences.

The finite checks are regression/falsification evidence only for `UR` and `LIFT`. The theorem-level status of `(CM0)` and `(SIMPLE)` comes from the proofs above, not from the scan.

## 11. Prior-art boundary

Relevant references inspected in this execution:

1. M. J. Coster and L. van Hamme, *Supercongruences of Atkin and Swinnerton-Dyer Type for Legendre Polynomials*, Journal of Number Theory 38 (1991), 265–286.
2. Zhi-Hong Sun, *Congruences involving \(\binom{2k}{k}^2\binom{3k}{k}m^{-k}\)*, arXiv:1104.2789.
3. The standard Hesse-pencil \(j\)-invariant formula and the discriminant \(-24\) singular modulus table/class polynomial.

The full weighted \(216\)-series modulo \(p^3\) remains beyond what is imported here. In particular, a conjectural formulation of the desired full supercongruence is not treated as proof.

No novelty or priority claim is made.

## 12. Exact open frontier

The strongest current exact frontier is now:

\[
\boxed{
\text{prove `UR`, then prove `LIFT`.}
}
\]

More explicitly,

\[
\boxed{
\frac gp
\equiv
-\frac1{6Q'_m(1/2)}
\pmod p
}
\]

for all \(p\equiv13,19\pmod{24}\), followed by

\[
\boxed{
\frac{(g/p)h-1}{p}
\equiv R_p\pmod p.
}
\]

Preferred successor routes:

1. derive a supersingular CM/ASD or crystalline Cartier formula that identifies the divided period \(g/p\) with the inverse Hasse derivative at the discriminant \(-24\) point;
2. derive an equivalent finite WZ/creative-microscoping certificate for `UR`;
3. only after `UR`, attack `LIFT` as the single second-order Frobenius/reflected-tail defect.

Do **not** reopen the already-proved CM zero, the simple-root lemma, or the parent three-block/tail bookkeeping.

## 13. Final freeze

`CM_HASSE_ZERO = PROVED`.

`CM_HASSE_ZERO_SCOPE = p mod 24 in {13,19}`.

`HESSIAN_ZERO_SIMPLE = PROVED`.

`JT0 = EQUIVALENT_TO_UR / OPEN`.

`JT2 = EQUIVALENT_TO_UR_PLUS_LIFT / OPEN`.

`ORDINARY_COSTER_VAN_HAMME_ASD_DIRECT_INSTANTIATION = NO_GO_BECAUSE_TARGET_PRIMES_ARE_INERT`.

`FINITE_REGRESSION = 77_TARGET_PRIMES_BELOW_2000 / ZERO_FAILURES / NOT_PROOF_OF_UR_OR_LIFT`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH = NOT_GRANTED`.

`NOVELTY_OR_PRIORITY_CLAIM = NONE`.

Recommended Driver action: accept this result as a strict exact reduction with a new theorem-level CM-Hasse zero and simple-root lemma. If execution continues, publish only the narrowed discriminant-\(-24\) supersingular unit-reciprocity successor (`UR`), with `LIFT` retained as the next second-digit gate.
