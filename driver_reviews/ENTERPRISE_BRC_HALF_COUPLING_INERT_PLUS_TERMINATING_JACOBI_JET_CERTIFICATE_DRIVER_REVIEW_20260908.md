# Driver Review — Enterprise BRC inert-plus terminating Jacobi-jet strict reduction

Driver-ID: `EM-DVR-3E669D`
Review-ID: `DR-2EA60F5817976E662FA6`
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE`
Publication: `TP2-A19C97A703AF47D1CBEC`
Result: `RR-82F6383FB6634F72B457`
Execution: `ER-A84CDD1F0678E7BEE767`
Driver authority: `DA-CB4940DEE5917B8BC161` / Issue #240 comment `5586317225`

## Disposition

`ACCEPTED / TERMINAL_AT_TASKBOOK_AUTHORIZED_STRICT_REDUCTION_SCOPE`.

The Result is accepted as completion of the present task because the immutable taskbook explicitly permits exact strict reduction as a terminal hard-target disposition. This review does **not** promote `JT0`, `JT2`, Sun A14(ii), `UR`, or `LIFT` to theorem status.

## Digest and envelope audit

The reviewed Result record is the exact migrated Git blob `07caf4f8800bcbcdc581b0aa592f4900d1e6044b`, with SHA-256
`423ae2420b7b646be6620f8e88926be7b50b81db4f421396ce917144823575ee`.

Its frozen manifest resolves to the original exact blobs:

- Return: `cf36004694dc2c8c9134e2e1e989c076b88e4c03`;
- recovery verification: `1db1a02b815e30ef643b246677b533e11a637c4a`;
- structurally independent checker: `baaccc59041db27c8396d1b093832be65d7d23fc`;
- execution record: `89865d3405890f364dca4e01dbde8ce8dcf82757`.

The Result remains bound to taskbook blob `425c65757974783e4268f37b8ee903fd46642dd4`. The migration onto the current-main-derived Driver branch reused these Git blobs directly and therefore introduced no mathematical-byte rewrite.

## Mathematical audit

The accepted reduction has four load-bearing steps.

1. **Terminating Legendre transport.** At the integer parameter,
   `H_m(z)=Phi_m(m,z)={}_2F_1(-m,-2m;1;z)` is a finite polynomial and satisfies
   `H_m(1-t^2)=P_{2m}(t)` modulo `p`. Writing the even Legendre polynomial as
   `P_{2m}(T)=Q_m(T^2)` gives `Phi=Q_m(1/2)` and
   `Psi=Q_m(1/2)-6Q'_m(1/2)` modulo `p`.

2. **CM0.** At `t^2=1/2`, the corresponding Hesse Hasse invariant specializes to the CM discriminant `-24` locus. For `p mod 24 in {13,19}`, `(-6/p)=-1`, so the primes are inert in `Q(sqrt(-6))`; Deuring supersingular reduction gives
   `Q_m(1/2)=0 mod p`.

3. **SIMPLE.** The Legendre differential equation at `t^2=1/2` has nonzero leading coefficient. A simultaneous zero of `P_{2m}` and its derivative would force all derivatives to vanish while `2m<p`, contradicting `P_{2m}(1)=1`. Hence
   `Q'_m(1/2) != 0 mod p`.

4. **Exact scalar separation.** The frozen parent interface gives
   `G_p=g/p = a + p Phi_xx/72 (mod p^2)` and
   `h = Psi - p Psi_x/6 (mod p^2)`. Therefore
   `JT2` is exactly `G_p h = 1+pR_p (mod p^2)`.
   With CM0 and SIMPLE,
   `JT0` is equivalent to the single nonzero reciprocal-scalar condition
   `UR: G_p(-6Q'_m(1/2))=1 (mod p)`.
   Once `UR` holds, defining `Delta_p=(G_p h-1)/p (mod p)` reduces the second digit to
   `LIFT: Delta_p=R_p (mod p)`.
   Thus the current task has strictly reduced
   `JT2 <=> UR + LIFT`.

This is genuinely smaller than the parent finite-tail/harmonic-block interface: CM0 removes the Hasse value, SIMPLE proves the surviving derivative is a unit, and the first and second p-adic digits are separated. The cutoff-sensitive `Phi_xx` information is correctly retained in `G_p mod p^2`; collapsing it modulo `p` before `LIFT` would be invalid.

## Independent cross-check

PR #1379 / Result `RR-BDF69EEDA87C8D22F3BC` independently rederived the same strict-reduction chain and preserved the same scope guard. In this Driver session the structurally independent differentiated-Legendre recurrence checker from the primary Result was executed again: all 77 target primes below 2000 passed, comprising 40 primes in class 13 and 37 in class 19, with no CM0, SIMPLE, UR, or JT2/LIFT regression failures.

That finite scan is used only as falsification/regression evidence. The all-prime status accepted here applies only to CM0, SIMPLE, and the exact equivalences/reduction; it does not prove UR or LIFT.

## Scope guard and terminal boundary

Accepted:

- `CM0` proved for all target primes `p mod 24 in {13,19}`;
- `SIMPLE` proved for all target primes;
- `JT0 <=> UR`;
- `JT2 <=> UR + LIFT`;
- exact preservation of the second p-adic digit in `G_p mod p^2`;
- BRC information-loss guard.

Not accepted as theorem:

- `UR`;
- `LIFT`;
- `JT0`;
- `JT2`;
- Sun A14(ii);
- any Working Truth, Foundation, L4, canonical-promotion, historical-priority, or novelty claim.

The present task is therefore terminally closed at its declared strict-reduction scope. Mathematical continuation must begin with a **new immutable successor task for discriminant -24 supersingular unit reciprocity `UR`**. Only after UR is closed should a second successor attack `LIFT`; the current task must not be redispatched to replay CM0/SIMPLE or the frozen finite-tail bookkeeping.
