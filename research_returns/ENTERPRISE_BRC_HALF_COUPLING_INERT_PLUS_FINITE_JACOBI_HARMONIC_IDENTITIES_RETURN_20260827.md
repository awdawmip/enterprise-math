# Enterprise BRC Half-Coupling Inert Plus Finite Jacobi-Harmonic Identities — Research Return

Status: `FINAL_FROZEN / EXACT_OBSTRUCTION / SINGLE_JACOBI_JET_CERTIFICATE`

Date: `2026-08-27`

Researcher-ID: `EM-EBP5JH-1097F5`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-FINITE-JACOBI-HARMONIC-IDENTITIES`

Publication: `TP2-AFF3DA9E8BBF2F6C886B`

Claim: `chatgpt-ebp5jh-20260827-2137`

Execution: `ER-20F444E74939EB5B2839`

## 1. Frozen verdict

`PRIMARY_VERDICT = PROOF_NOT_CLOSED_WITH_STRICTER_SINGLE_JACOBI_JET_CERTIFICATE`.

`HARD_TARGET_DISPOSITION = ACHIEVED_BY_EXACT_OBSTRUCTION_AND_STRICT_REDUCTION`.

No counterexample was found in either requested plus class. No all-prime proof of the parent identities `(R0)` and `(R1)` is claimed.

The exact advance is that the parent five finite objects

\[
F_0,F_1,F_2,J_0,J_1
\]

are not five independent harmonic sums. They are exactly the value, first derivative, and second derivative of one terminating hypergeometric polynomial along one parameter direction. Consequently the pair `(R0)+(R1)` collapses to one modulo-\(p^2\) Jacobi-jet certificate. The zero-order part is an explicit Jacobi-polynomial transversality condition at the fixed point \(x=3\).

A separate prior-art audit also identifies the inherited full weighted target with the plus-class specialization of Zhi-Wei Sun's Conjecture A14(ii). That source is a conjecture, not an admissible theorem dependency. No proof of the exact weighted \(216\)-supercongruence was located in the audited search set through `2026-08-27`.

## 2. Frozen parent interface

Write

\[
p=6m+1,\qquad p\equiv13,19\pmod{24},
\]

so \(m\equiv2,3\pmod4\).

The accepted parent reduction defines

\[
A_m=\frac{F_0}{p}+F_1
\]

and leaves exactly

\[
\boxed{A_mJ_0\equiv1\pmod p}
\tag{R0}
\]

and

\[
\boxed{
\frac{A_mJ_0-1}{p}+A_mJ_1+F_2J_0\equiv R_p\pmod p.
}
\tag{R1}
\]

The reflected scalar \(R_p\) and the finite-tail reduction are frozen parent inputs and are not reopened here.

## 3. One terminating jet object

Define

\[
\Phi_m(x,z)
=
\sum_{k=0}^{6m}
\frac{(-x)_k(-2x)_k}{(k!)^2}z^k
\]

and

\[
\Psi_m(x,z)
=
(1+12z\partial_z)\Phi_m(x,z).
\]

The key observation is exact, not asymptotic:

\[
\frac{(-m+\varepsilon/6)_k(-2m+\varepsilon/3)_k}
{(k!)^2 2^k}
\]

is precisely the \(k\)-th summand of

\[
\Phi_m\!\left(m-\frac{\varepsilon}{6},\frac12\right).
\]

Therefore the entire parent deformation is one directional Taylor jet.

By the ordinary chain rule,

\[
\boxed{
F_0=\Phi_m(m,1/2),
\qquad
F_1=-\frac16\Phi_x(m,1/2),
\qquad
F_2=\frac1{72}\Phi_{xx}(m,1/2)
}
\tag{J-F}
\]

and

\[
\boxed{
J_0=\Psi_m(m,1/2),
\qquad
J_1=-\frac16\Psi_x(m,1/2).
}
\tag{J-H}
\]

These identities exactly reproduce every low/middle/high block coefficient in the parent return.

### Why the old `0/1/2` blocks disappear

Let

\[
f_k(x)=\frac{(-x)_k(-2x)_k}{(k!)^2 2^k}.
\]

Then

\[
f_{k+1}(x)
=f_k(x)\frac{(k-x)(k-2x)}{2(k+1)^2}.
\]

At \(x=m\):

- \(k\le m\): zero vanishing factors;
- \(m<k\le2m\): one vanishing factor;
- \(k>2m\): two vanishing factors.

Thus the parent valuation/Taylor stratification is exactly the multiplicity structure of one polynomial recurrence. First derivatives beyond \(2m\) vanish automatically; second derivatives survive and therefore correctly retain the frozen cutoff \(k\le6m=p-1\).

The task-local checker propagates \(f_k,f'_k,f''_k\) by this recurrence and verifies `(J-F)` and `(J-H)` against an independent replay of the parent's harmonic formulas.

## 4. The zero-order Jacobi form

At the integer point \(x=m\), the sum terminates already at \(k=2m\):

\[
\Phi_m(m,z)={}_2F_1(-m,-2m;1;z).
\]

Pfaff's transformation gives

\[
{}_2F_1(-m,-2m;1;z)
=(1-z)^m
P_m^{(0,m)}\!\left(\frac{1+z}{1-z}\right).
\]

Setting \(z=1/2\),

\[
\boxed{
F_0=2^{-m}P_m^{(0,m)}(3).
}
\tag{P0}
\]

Differentiating in \(z\), and using

\[
\frac{d}{dx}P_m^{(0,m)}(x)
=\frac{2m+1}{2}P_{m-1}^{(1,m+1)}(x),
\]

gives

\[
\boxed{
J_0
=2^{-m}
\Bigl[
(1-12m)P_m^{(0,m)}(3)
+24(2m+1)P_{m-1}^{(1,m+1)}(3)
\Bigr].
}
\tag{P1}
\]

So `(R0)` is a Jacobi transversality statement, not an opaque harmonic identity.

## 5. Exact reduced certificates

For compactness, evaluate all derivatives below at \((x,z)=(m,1/2)\), and put

\[
a:=\frac{\Phi}{p}-\frac{\Phi_x}{6}.
\]

Then `(R0)` becomes

\[
\boxed{a\Psi\equiv1\pmod p.}
\tag{JT0}
\]

The correction `(R1)` becomes

\[
\boxed{
\frac{a\Psi-1}{p}
-\frac{a\Psi_x}{6}
+\frac{\Phi_{xx}\Psi}{72}
\equiv R_p\pmod p.
}
\tag{JT1}
\]

Equivalently, the two scalar congruences are exactly one certificate:

\[
\boxed{
\left(a+\frac{p\Phi_{xx}}{72}\right)
\left(\Psi-\frac{p\Psi_x}{6}\right)
\equiv1+pR_p\pmod{p^2}.
}
\tag{JT2}
\]

Thus

\[
(R0)+(R1)
\quad\Longleftrightarrow\quad
(JT2).
\]

This is the smallest exact object obtained in this execution: one terminating hypergeometric/Jacobi second-order jet certificate, with no separate harmonic arrays and no three-block bookkeeping.

## 6. Prior-art boundary: exact identification with Sun A14(ii)

Let

\[
\mathcal F(z)={}_2F_1\left(\frac16,\frac13;1;z\right).
\]

Clausen's identity gives

\[
\mathcal F(z)^2
={}_3F_2\left(\frac13,\frac23,\frac12;1,1;z\right).
\]

Therefore

\[
\mathcal F(z)
\bigl(\mathcal F(z)+12z\mathcal F'(z)\bigr)
=
(1+6z\partial_z)\mathcal F(z)^2.
\]

At \(z=1/2\), the coefficient of degree \(n\) on the right is

\[
(6n+1)
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}.
\]

This is exactly the weighted Ramanujan truncation appearing in Zhi-Wei Sun, *Open Conjectures on Congruences*, arXiv:0911.5665, Conjecture A14(ii):

\[
\frac1{p^a}
\sum_{k=0}^{p^a-1}
(6k+1)
\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k}
\equiv
\left(\frac{p^a}{3}\right)
\pmod{p^2}.
\]

For the present plus classes \(p\equiv13,19\pmod{24}\), one has \((p/3)=1\). For \(a=1\), the conjecture predicts

\[
\sum_{k=0}^{p-1}
(6k+1)
\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k}
\equiv p\pmod{p^3}.
\]

Under the already-frozen Clausen-tail bridge:

- `(R0)` is its first \(p\)-adic digit, i.e. the corresponding mod-\(p^2\) statement;
- `(R0)+(R1)` recovers the full mod-\(p^3\) plus-class statement after the reflected \(p^2R_p\) tail is restored.

This prior-art identification is important negatively: A14(ii) is explicitly presented as a conjecture in the source. It cannot be imported as proof of `(R0)` or `(R1)`.

### Audited proof search

A targeted search through current material up to `2026-08-27` did not locate a proof of this exact weighted \(216\) congruence. In particular:

1. Guo-Shuai Mao, arXiv:1910.00779 proves a different weighted \(256\) central-binomial-cube supercongruence;
2. Zhi-Hong Sun and Dongxi Ye, arXiv:2408.09776 prove other Beukers-method families; the audited material did not contain this exact weighted \(216\) theorem;
3. Qing-Hu Hou and Zhi-Wei Sun, arXiv:2604.15172 develops WZ derivative evaluations for other series, but the audited material did not provide the required all-prime p-adic statement.

This is an audit statement, not a global claim that no proof can exist anywhere.

## 7. Deterministic checker

Task-local checker:

`scripts/check_enterprise_brc_half_coupling_inert_plus_finite_jacobi_harmonic_identities.py`

It uses exact `Fraction` arithmetic and two structurally different descriptions of the same coefficients:

1. direct jet propagation of \(f_k,f'_k,f''_k\) using the single rational recurrence;
2. an independent replay of the parent's low/middle/high harmonic formulas.

For every tested prime it checks:

- exact equality `F0=Phi`, `F1=-Phi_x/6`, `F2=Phi_xx/72`;
- exact equality `J0=Psi`, `J1=-Psi_x/6`;
- reconstruction of \(G_p\pmod{p^3}\) and \(H_p\pmod{p^2}\);
- `(JT0)` and `(JT1)`;
- the corresponding weighted Ramanujan residue as a regression-only prior-art interface check.

Exact run performed in this execution:

`python scripts/check_enterprise_brc_half_coupling_inert_plus_finite_jacobi_harmonic_identities.py --limit 2000`

Result:

- plus-class primes checked: `77`;
- class `13 mod24`: `40`;
- class `19 mod24`: `37`;
- exact jet-identification failures: `0`;
- `(R0)` failures: `0`;
- `(R1)` failures: `0`.

This is `FINITE_REGRESSION_ONLY_NOT_A_PROOF`.

## 8. What is closed and what remains open

Closed exactly here:

1. the five parent finite harmonic coefficients are one terminating \({}_2F_1\) parameter jet;
2. the three parent Taylor blocks are multiplicity strata of one recurrence;
3. `(R0)+(R1)` is one mod-\(p^2\) terminating Jacobi-jet certificate `(JT2)`;
4. \(F_0\) and \(J_0\) have explicit Jacobi-polynomial formulas at the single point \(3\);
5. the inherited full weighted target is exactly identified with the plus-class \(a=1\) specialization of Sun A14(ii), so the project has a precise prior-art boundary and cannot accidentally treat that conjecture as proved.

Not closed:

1. an all-prime proof of `(JT0)` / `(R0)`;
2. an all-prime proof of `(JT1)` / `(R1)`;
3. therefore an all-prime proof of `(JT2)` and of the full plus target.

No exact counterexample was found.

## 9. Smallest successor-worthy unit

The next task should not return to the old harmonic block formulas. The smallest remaining target is:

> Prove the single terminating Jacobi-jet certificate `(JT2)` for \(m\equiv2,3\pmod4\), \(p=6m+1\) prime, preferably by either (i) a finite WZ/creative-microscoping certificate for the jet recurrence, or (ii) a Frobenius/Jacobi-sum transversality theorem at the supersingular point \(z=1/2\).

For a staged attack, `(JT0)` is the correct first subtarget because it needs only the untruncated first Jacobi parameter derivative; `(JT1)` is the first place where the cutoff-sensitive second derivative \(\Phi_{xx}^{[6m]}\) genuinely enters.

Broadening the prime scan is not a successor-worthy action.

## 10. Final freeze

`PRIMARY_VERDICT = PROOF_NOT_CLOSED_WITH_STRICTER_SINGLE_JACOBI_JET_CERTIFICATE`.

`HARD_TARGET = ACHIEVED_AT_EXACT_OBSTRUCTION_STRENGTH`.

`R0 = UNPROVED_UNREFUTED / REDUCED_TO_JACOBI_TRANSVERSALITY`.

`R1 = UNPROVED_UNREFUTED / REDUCED_TO_SECOND_JACOBI_JET_CORRECTION`.

`R0_PLUS_R1 = ONE_MOD_P2_TERMINATING_JACOBI_JET_CERTIFICATE`.

`SUN_A14_II = IDENTIFIED_PRIOR_ART_CONJECTURE / NOT_IMPORTED_AS_THEOREM`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH = NOT_GRANTED`.

`NOVELTY_OR_PRIORITY_CLAIM = NONE`.

Recommended Driver action: accept as a strict exact reduction and prior-art boundary. If continuing, publish one narrow successor for `(JT2)` (or `(JT0)` first), without reopening finite-tail bookkeeping.
