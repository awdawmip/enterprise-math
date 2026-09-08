# Enterprise BRC Half-Coupling Inert-Plus Terminating Jacobi-Jet Certificate — Research Return

Status: `FINAL_FROZEN / SUCCESS_BY_STRICT_REDUCTION / CM0+SIMPLE_PROVED / JT2_REDUCED_TO_UR+LIFT`

Date: `2026-09-08`

Researcher-ID: `EM-EBP6JT-4D1A01`  
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE`  
Publication: `TP2-A19C97A703AF47D1CBEC`  
Claim: `chatgpt-ebp6jt-20260907-2359-solc4a91e`  
Execution: `ER-A84CDD1F0678E7BEE767`  
Recovered durable frontier: `research/enterprise-brc-half-coupling-inert-plus-terminating-jacobi-jet-certificate-em-ebp6jt-25c94a@a722292873eba2449f0959fad7b766a12741ff47`

## 1. Terminal disposition

`HARD_TARGET_DISPOSITION = ACHIEVED_BY_STRICT_REDUCTION`.

The taskbook permits three closing outcomes for `(JT2)`: proof, exact refutation, or a strictly smaller exact certificate. This execution adopts and independently checks the strongest durable predecessor frontier instead of replaying already verified mathematics.

For every prime
\[
p=6m+1,\qquad p\equiv 13,19\pmod{24},
\]
the following theorem-level facts are retained and revalidated:

1. `CM0`: \(Q_m(1/2)\equiv0\pmod p\);
2. `SIMPLE`: \(Q'_m(1/2)\not\equiv0\pmod p\);
3. `JT0` is exactly equivalent to one nonzero unit-reciprocity certificate `UR`;
4. `JT2` is exactly equivalent to `UR + LIFT`, with the cutoff-sensitive \(\Phi_{xx}\) contribution retained inside \(G_p=g/p\bmod p^2\).

Therefore the current task is complete at its explicitly authorized strict-reduction scope. `UR` and `LIFT` are successor-frontier mathematics, not an unperformed part of this task.

No Working Truth, Foundation authority, canonical promotion, historical novelty, or factoring/supercongruence priority claim is asserted.

## 2. Frozen parent interface

Let
\[
\Phi_m(x,z)=\sum_{k=0}^{6m}\frac{(-x)_k(-2x)_k}{(k!)^2}z^k,\qquad
\Psi_m=(1+12z\partial_z)\Phi_m,
\]
evaluated at \((x,z)=(m,1/2)\), and
\[
a=\frac{\Phi}{p}-\frac{\Phi_x}{6}.
\]

The hard target is
\[
\left(a+\frac{p\Phi_{xx}}{72}\right)
\left(\Psi-\frac{p\Psi_x}{6}\right)
\equiv 1+pR_p\pmod{p^2}. \tag{JT2}
\]

The accepted parent reduction supplies exact rational quantities
\[
B_0=1,\qquad
\frac{B_{k+1}}{B_k}=\frac{(6k+1)(3k+1)}{36(k+1)^2},
\]
\[
g=\sum_{k=0}^{p-1}B_k,\qquad
h=\sum_{k=0}^{p-1}(12k+1)B_k,\qquad p\mid g,
\]
and
\[
G_p:=\frac gp\equiv a+\frac{p\Phi_{xx}}{72}\pmod{p^2},
\qquad
h\equiv\Psi-\frac{p\Psi_x}{6}\pmod{p^2}.
\]

Hence
\[
(JT2)\iff G_ph\equiv 1+pR_p\pmod{p^2}. \tag{SCALAR-JT2}
\]

This formulation is intentionally retained at exact rational / mod-\(p^2\) precision: reducing \(G_p\) modulo \(p\) too early destroys precisely the second digit needed for `LIFT`.

## 3. Terminating quadratic / Legendre transport

At the integer parameter,
\[
H_m(z):=\Phi_m(m,z)
={}_2F_1(-m,-2m;1;z)
=\sum_{k=0}^{m}\binom mk\binom{2m}kz^k.
\]

Modulo \(p\), because \(-m\equiv1/6\) and \(-2m\equiv1/3\), the terminating quadratic transformation gives
\[
H_m(1-t^2)=P_{2m}(t)\qquad\text{in }\mathbf F_p[t].
\]

Since \(P_{2m}\) is even, write
\[
P_{2m}(T)=Q_m(T^2).
\]
Then
\[
H_m(z)=Q_m(1-z), \tag{QL}
\]
and at \(z=1/2\),
\[
\Phi=Q_m(1/2),\qquad
\Psi=Q_m(1/2)-6Q'_m(1/2)\pmod p. \tag{QPsi}
\]

All identities in this step are finite terminating polynomial identities; no infinite-series truncation exchange is used.

## 4. Hesse Hasse invariant and CM discriminant -24

Take \(t^2=1/2\) and \(u=(1-t)/2\). Since \(2m=(p-1)/3\),
\[
P_{2m}(1-2u)=
A_p(u):=\sum_{k=0}^{(p-1)/3}
\frac{(3k)!}{27^k(k!)^3}u^k\pmod p.
\]

For the Hesse cubic
\[
E_\lambda:\ X^3+Y^3+Z^3-3\lambda XYZ=0,\qquad \lambda^{-3}=u,
\]
the coefficient of \((XYZ)^{p-1}\) in its \((p-1)\)-st power is a nonzero scalar multiple of \(A_p(u)\). Thus \(A_p(u)=0\) is the supersingular Hasse-invariant condition.

The Hesse \(j\)-invariant specializes to
\[
j=2417472\pm1707264\sqrt2,
\]
whose two values are the roots of
\[
X^2-4834944X+14670139392,
\]
the Hilbert class polynomial of discriminant \(-24\). The corresponding CM field is \(\mathbf Q(\sqrt{-6})\).

For \(p\equiv13,19\pmod{24}\),
\[
\left(\frac{-6}{p}\right)=-1.
\]
Thus the target primes are inert in the CM field. The classical Deuring CM reduction theorem makes the good reduction supersingular, so the Hasse invariant vanishes. Transporting through `(QL)` gives
\[
Q_m(1/2)\equiv0\pmod p. \tag{CM0}
\]

Both required residue classes are covered uniformly.

## 5. The CM zero is simple

For \(n=2m<p\), \(P_n\) satisfies
\[
(1-T^2)P_n''-2TP_n'+n(n+1)P_n=0.
\]

At \(t^2=1/2\), the leading coefficient is nonzero. If both \(P_n(t)\) and \(P'_n(t)\) vanished, the differential equation and its repeated derivatives would force every derivative through degree \(n\) to vanish at \(t\). Since \(n<p\), the factorials in the Taylor coefficients are units, which would imply \(P_n=0\), contradicting \(P_n(1)=1\).

Therefore
\[
P'_{2m}(t)\ne0.
\]
Since \(P'_{2m}(t)=2tQ'_m(t^2)\) and \(t\ne0\),
\[
Q'_m(1/2)\not\equiv0\pmod p. \tag{SIMPLE}
\]

## 6. Exact reduction of JT0 and JT2

By `(CM0)`, `(QPsi)`, and `(SIMPLE)`,
\[
\Psi\equiv-6Q'_m(1/2)\pmod p
\]
is a unit. The parent identity gives \(G_p\equiv a\pmod p\). Hence
\[
(JT0)\iff
G_p\bigl(-6Q'_m(1/2)\bigr)\equiv1\pmod p. \tag{UR}
\]

Equivalently,
\[
G_p\equiv-\frac1{6Q'_m(1/2)}\pmod p.
\]

For the second digit, `(SCALAR-JT2)` is exact. Once `UR` holds, define
\[
\Delta_p=\frac{G_ph-1}{p}\pmod p.
\]
Then
\[
(JT2)\iff (UR)\ \text{and}\ 
\Delta_p\equiv R_p\pmod p. \tag{LIFT}
\]

Thus:
\[
JT2\iff UR+LIFT.
\]

This is a strict reduction, not a rename:
- `CM0` removes the Hasse value entirely;
- `SIMPLE` proves the surviving derivative is a unit, so `UR` is a genuine reciprocal-scalar condition;
- the first and second digits are separated;
- the parent \(\Phi_{xx}\) contribution is preserved in \(G_p\bmod p^2\);
- the five earlier harmonic-block objects and Clausen-tail bookkeeping do not re-enter.

## 7. BRC first-line gate and information audit

BRC is applied as an information-preservation discipline rather than as a name-only analogy.

**Population.** Target primes \(p\equiv13,19\pmod{24}\).

**Branch identity.** The two residue classes remain labeled through the CM/inert step; they are not averaged together.

**Exact carrier.** The adequate carrier is
\[
(B_k;\ g,h,G_p\bmod p^2,R_p;\ Q_m(1/2),Q'_m(1/2)),
\]
with exact rational arithmetic before modular observation.

**Observer.** The terminal observers are mod-\(p\) for `CM0/SIMPLE/UR` and mod-\(p^2\) followed by divided first-order extraction for `LIFT`.

**Allowed future operation.** Division of \(g\) by \(p\), multiplication with \(h\), and extraction of the second \(p\)-adic digit.

**Information-loss guard.** Replacing \(G_p\bmod p^2\) by only \(G_p\bmod p\) is forbidden before `LIFT`, because that quotient erases the only coordinate capable of carrying the second digit. Likewise, Boolean truth of `UR` cannot substitute for its exact unit value if a successor attempts a lift.

**Provenance audit.** The theorem-level CM transport, the finite regression, and the parent reduction remain separately labeled. Finite success is not promoted into all-prime proof of `UR` or `LIFT`.

`BRC_REUSE_RESOLUTION = REUSE_APPLIED`.

## 8. Independent deterministic regression

A structurally independent task-local checker was run on all target primes below `2000`.

It does not reuse the predecessor's polynomial-array construction for the Legendre object. Instead it evaluates \(P_{2m}(t)\) and its derivative directly by the differentiated three-term Legendre recurrence inside
\[
\mathbf F_p[t]/(t^2-1/2).
\]

Results:

- target primes: `77`;
- `p mod 24 = 13`: `40`;
- `p mod 24 = 19`: `37`;
- `CM0` failures: `0`;
- `SIMPLE` failures: `0`;
- `UR` regression failures: `0`;
- `JT2/LIFT` regression failures: `0`.

This is falsification/regression evidence only for `UR` and `LIFT`. The theorem status of `CM0` and `SIMPLE` comes from the exact arguments above.

## 9. Failed shortcuts and scope boundaries

1. Sun A14(ii) remains an inherited conjectural target and is not used as a theorem.
2. Ordinary split-CM ASD/unit-root machinery requires the opposite splitting regime; direct instantiation is not licensed on this inert lane.
3. Reopening the parent finite-tail or harmonic-block bookkeeping would enlarge, not reduce, the current interface.
4. Collapsing \(G_p\) to mod \(p\) before the lift destroys the required second digit.
5. Enlarging the finite prime scan cannot close `UR` or `LIFT`.

## 10. Final freeze

`CM_HASSE_ZERO = PROVED`.

`CM_HASSE_ZERO_SCOPE = p mod 24 in {13,19}`.

`SIMPLE_ROOT_TRANSVERSALITY = PROVED`.

`JT0 = EQUIVALENT_TO_UR / SUCCESSOR_FRONTIER_OPEN`.

`JT2 = EQUIVALENT_TO_UR_PLUS_LIFT / SUCCESSOR_FRONTIER_OPEN`.

`CUTOFF_SENSITIVE_PHI_XX = RETAINED_INSIDE_G_OVER_P_MOD_P2`.

`TASK_HARD_TARGET = ACHIEVED_BY_STRICT_REDUCTION`.

`FINITE_REGRESSION = 77 TARGET PRIMES BELOW 2000 / ZERO FAILURES / NOT AN ALL-PRIME PROOF OF UR OR LIFT`.

`WORKING_TRUTH = NOT_GRANTED`.

`FOUNDATION_AUTHORITY = NOT_GRANTED`.

`CANONICAL_PROMOTION = NOT_GRANTED`.

Smallest successor frontier: first prove the discriminant \(-24\) supersingular unit reciprocity `UR`; only after `UR` closes, prove the single `LIFT` congruence. That successor should be separately published if the Driver elects to continue; the present task should not be redispatched merely to redo `CM0`, `SIMPLE`, or the parent reduction.

## 11. Provenance boundary

This execution is a recovery/verification closure. It consumes the mathematically complete durable predecessor frontier at commit `a722292873eba2449f0959fad7b766a12741ff47`, rechecks the taskbook success criterion, independently re-runs the finite falsifier through a structurally different Legendre evaluator, and freezes the result under the current claim/execution identity.

The recovered predecessor's mathematical content is preserved as provenance; the current Result record is the durable control-plane handoff for Driver review.
