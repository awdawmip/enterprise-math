# Enterprise BRC inert-plus D=-24 UR successor handoff — 2026-09-09

Status: `PARENT_ACCEPTED / UR SUCCESSOR PUBLISHED-PACKET / LIFT DEFERRED`

Driver: `EM-DVR-CJ7F3A`

Successor task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`  
Successor publication: `TP2-C0E85430A37213F301EB`  
Successor taskbook: `research_tasks/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_D24_SUPERSINGULAR_UNIT_RECIPROCITY_20260909.md`

## Canonical predecessor chain

Start here before doing mathematics:

- Parent publication: `research_task_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/TP2-A19C97A703AF47D1CBEC.json`
- Accepted parent Result: `research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/RR-82F6383FB6634F72B457.json` (`RR-82F6383FB6634F72B457`)
- Accepted Driver Review: `research_result_reviews/RR-82F6383FB6634F72B457/DR-2EA60F5817976E662FA6.json` (`DR-2EA60F5817976E662FA6`)
- Review narrative: `driver_reviews/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_DRIVER_REVIEW_20260908.md`
- Frozen parent return: `research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md`
- Structurally independent regression checker: `scripts/check_enterprise_brc_half_coupling_inert_plus_terminating_jacobi_jet_certificate_independent.py`

The accepted predecessor is terminal at strict-reduction scope. Do not reclaim or replay the old Jacobi-jet task.

## What is already theorem-level at the accepted predecessor

For every prime
\[
p\equiv13,19\pmod{24},\qquad m=(p-1)/6,
\]
write \(P_{2m}(T)=Q_m(T^2)\). The accepted predecessor proves

\[
Q_m(1/2)\equiv0\pmod p,
\qquad
Q_m'(1/2)\not\equiv0\pmod p.
\]

The first statement is obtained from the Hesse Hasse invariant at the discriminant \(-24\) CM specialization and inert supersingular reduction in \(\mathbf Q(\sqrt{-6})\); the second from the Legendre differential equation and the degree bound \(2m<p\).

The accepted scalar reconstruction is

\[
G_p=\frac{g}p,\qquad
g=\sum_{k=0}^{p-1}B_k,\qquad
\frac{B_{k+1}}{B_k}
=\frac{(6k+1)(3k+1)}{36(k+1)^2},
\]

and it proves

\[
JT0\iff
\boxed{G_p(-6Q_m'(1/2))\equiv1\pmod p}.
\]

Call the boxed identity `UR`. The full second digit is already separated as

\[
JT2\iff UR+LIFT,
\]

where, once `UR` holds,
\[
\Delta_p=\frac{G_ph-1}p\pmod p,
\qquad
LIFT:\;\Delta_p\equiv R_p\pmod p.
\]

`UR`, `LIFT`, `JT0`, `JT2` and Sun A14(ii) remain open at theorem level.

## New UR frontier from the 2026-09-09 continuation

These items were derived in the continuation that generated this handoff but have **not** received an independent Result/Driver acceptance. The new researcher must rederive the exact equivalence before promoting them from task-local frontier to proof input.

Work in the unramified quadratic residue extension with
\[
t^2=1/2,\qquad u=(1-t)/2,
\]
and define
\[
L_p(u)=\sum_{k=0}^{p-1}
\frac{(1/3)_k(2/3)_k}{(k!)^2}u^k.
\]

The Mao--Pan terminating quadratic-transform route suggests the exact bridge
\[
\boxed{\frac{L_p(u)}pL_p'(u)\equiv\frac{2t}3\pmod p}.
\tag{UR-L}
\]

Because the target primes have \((2/p)=-1\), Frobenius interchanges \(t\leftrightarrow-t\) and \(u\leftrightarrow1-u\). The coefficientwise quadratic transform plus the generalized-Legendre reflection indicates
\[
L_p(u)\equiv L_p(1-u)\pmod{p^2},
\]
so the divided value \(L_p(u)/p\) should descend to the base field modulo \(p\). Recheck this carefully as part of the `UR-L` derivation.

Let
\[
n=(p-1)/3=2m.
\]
A further ordinary-Legendre candidate isolated in this continuation is
\[
\boxed{(P_{2n}(t)+2P_n(t))P_n'(t)\equiv-pt\pmod{p^2}}.
\tag{UR-LEG}
\]

The intended first attack is to derive the divided-value identity behind `UR-LEG` from Zhi-Hong Sun's generalized Legendre polynomial at \(a=-1/3\), use the \(p\)-adic three-term parameter recurrence at the Frobenius pair \(t,-t\), eliminate the neighboring parameters by parity/reflection, and differentiate. If that derivation fails, record the exact failed coefficient or precision step rather than treating `UR-LEG` as established.

## Deferred second-digit packet — not yet claimable

The accepted Driver review requires `LIFT` to wait until `UR` closes. Preserve the following as a deferred route, not a theorem and not an independently executable task.

Let \(F_p\) denote the truncated \((1/6,1/3)\) side of the quadratic transform and consider its \(p^3\) defect against \(L_p\). The continuation found the candidate structure
\[
L_p(u)-F_p(4u(1-u))
\equiv p^2u^p r_p(u)\pmod{p^3},
\]
with residual hypergeometric operator
\[
\mathcal D
=u(1-u)\frac{d^2}{du^2}
+(1-2u)\frac d{du}-\frac29
\]
and the task-local symbolic relation
\[
\mathcal D r_p(u)
=\frac29(1+u+\cdots+u^{p-2}).
\tag{QTF3-ODE}
\]

The right side is odd under \(u\leftrightarrow1-u\). The remaining obstruction to a clean anti-symmetry statement is one homogeneous Hasse normalization constant. Finite exact experiments from the continuation indicated
\[
\delta_p\in(1+\sqrt2)\mathbf F_p,
\]
for the tested target primes, but this is **diagnostic finite evidence only**.

A natural deferred fixed-point candidate is
\[
\sum_{k=0}^{p-1}
\frac{(1/3)_k(2/3)_k}{(k!)^2 2^k}
\equiv
\sum_{k=0}^{p-1}
\frac{(1/6)_k(1/3)_k}{(k!)^2}
\pmod{p^3}.
\tag{QTF3}
\]

Do not publish the `LIFT/QTF3` successor until the `UR` task has a terminal accepted result or a new authorized route explicitly changes that gate.

## Mechanism ledger

Already exhausted or bounded:

- terminating quadratic/Legendre transport: useful and retained;
- Hesse Hasse invariant + discriminant \(-24\) CM + Deuring: closes `CM0`, do not reopen;
- Legendre differential equation: closes simple-root transversality, do not reopen;
- finite WZ/creative-microscoping search: no matching all-prime `UR`/`LIFT` close found;
- ordinary split-CM ASD/unit-root instantiation: structural mismatch on the inert target lane;
- finite prime scans: regression/falsification only.

Live mechanisms for `UR`:

- generalized-Legendre \(p\)-adic recurrence at \(a=-1/3\) with \(t,-t\) parity/Frobenius elimination;
- supersingular Frobenius/Wronskian or Jacobi-sum computation of the divided-period/derivative unit;
- Mao--Pan \(p^2\) quadratic-transform bridge as an exact transport interface, after rechecking its hypotheses and differentiation precision.

## BRC information boundary

Population: the finite truncation terms \(k=0,\ldots,p-1\).  
Required carrier: labeled term provenance + exact rational/\(p\)-adic valuations + derivative/jet data + Frobenius-conjugate ports.  
Unsafe compression: positive total mass or magnitude-only summaries; they erase the cancellation and conjugate information needed by `UR` and `LIFT`.

## Immediate next action for the new researcher

1. Read the accepted Result/Review and this handoff.
2. Reprove the quadratic-transform bridge to `UR-L`, including the base-field descent of \(L_p(u)/p\).
3. Derive or falsify `UR-LEG` exactly.
4. If `UR-LEG` survives, attack it through the generalized-Legendre recurrence and a distinct Frobenius/Wronskian route.
5. Return a uniform proof, exact counterexample, or a strictly smaller exact residue. Do not reopen `CM0`, `SIMPLE`, or the old harmonic/tail interface.
