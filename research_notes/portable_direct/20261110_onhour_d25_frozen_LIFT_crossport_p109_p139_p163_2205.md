# D25/LIFT — three exact new frozen signed scalar cross-port certificates (p=109,139,163)

Date: 2026-11-10 22:05 Asia/Hong_Kong.
Research lane: `chatgpt-research-onhour-enterprise-math-20260923` (not the maintenance lane).
Status: **AUTHOR_SIDE / EXACT FINITE ORIGINAL-OBSERVER CERTIFICATE / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN**.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. Immutable publication: `TP2-B6F4FC938FF94941C1B7`.
**Frozen scientific Source** `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).

## New unit: compute the frozen Delta and reflected signed R on previously unverified scalar ports

Consume the proven original-source port identity from
`research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md` without claiming to re-prove it.
For `p=6m+1`, `p mod24 in {13,19}`, set

```
B_k=(1/6)_k(1/3)_k / [2^k(k!)^2],  A_k=binom(2k,k)^2 binom(3k,k) / 216^k
M=sum_(k<p) B_k,  N=sum_(k<p) k B_k,  h=M+12N,
W=sum_(k<p)(6k+1) A_k,
Q=sum_(0<=i,j<p; i+j>=p) [6(i+j)+1] B_i B_j.
G=M/p, Delta=((G*h-1)/p) mod p.
C_a=2^(a-1) ((a-1)!)^2/[18(5/6)_a(2/3)_a].
R_p=2 sum_(i=1)^m B_i sum_(a=1)^i [1+6(i-a)] C_a (mod p).
```

Use all these as p-local rationals before quotienting. The previously proved exact Clausen identity is `M*h-W=Q`; the prior frozen port equality is `Q/p²=R_p mod p`. The exact observer identity then is
```
Delta-R_p = (W-p)/p²  (mod p).
```
The new work independently computes all three observer values on the **original frozen definitions**, not merely on a surrogate power-scale W sum.

### Newly computed exact integer witnesses

All `M,N,W,Q` are canonical residues modulo `p³`; `Gh` is modulo `p²`. The final columns are modulo p.

| p | class | p³ | M | N | W | Q | Gh | Delta | original R | (W-p)/p² |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|109|13|1295029|139193|1025954|109|594050|5451|**50**|**50**|0|
|139|19|2685619|1054732|1572406|139|1758211|12650|**91**|**91**|0|
|163|19|4330747|2336605|3074100|163|1487864|9129|**56**|**56**|0|

Each row has the independently checkable integer witnesses
```
p=109: Q=50*109²,  Gh=1+50*109, W=109 (mod 109³)
p=139: Q=91*139²,  Gh=1+91*139, W=139 (mod 139³)
p=163: Q=56*163²,  Gh=1+56*163, W=163 (mod 163³).
```
Consequently the **original signed LIFT residue** equals zero at each named prime, while its two constituents are nonzero. These are *three finite certified cases*, not a universal LIFT proof.

### Prior-work controls, explicitly not new

For `p=13,19,373` the checker reproduces earlier original-source values `R=Delta=0,12,196`.
For `p=157` it reproduces `R=Delta=82`, already recorded in
`research_notes/portable_direct/2026-11-10_h40_d25_tail_reflected_two_way_zero_observer_author_portable.md`, where the distinct third-band scalar tail vanished. That existing counterexample is consumed without re-credit. The prior p109/p139 W prime-power scale measurements remain prior evidence; only their **newly computed original Delta/R cross-port** is credited here.

## Reproducible exact arithmetic, observer/BRC audit

Checker: `research_notes/portable_direct/d25_frozen_lift_crossport_three_new_primes_20261110.py`.
Executed with Python standard-library integers, on the seven primes `13,19,109,139,157,163,373`. It checks the complete `B_k` and `A_k` vectors in two separate constructions (p-local recurrence versus factorial/Pochhammer numerator with integer binomial coefficients); computes Q by the complete ordered `(i,j)` triangular cutoff and independently by `M(M+12N)-W`; computes the original reflected C via both its factorial definition and its recurrence; checks `R=Q/p²`, `p|M`, `Gh=1 mod p` and `Delta-R=(W-p)/p²` with exact quotient-before-reduction. All checks passed.

BRC: **COMPOSE_APPLIED** at the original signed observer: retain ordered branch labels `(i,j)`, reflected `(i,a)`, p-adic valuation/denominator units, `M,N,Q,W,Delta,R`; projection to `(Delta-R)` is certified only for the declared `mod p` final scalar and is **not** sound for later signed-cutoff, higher-digit, odd-Green or native Frobenius operations. Zero residual does not mean the separate nonzero Delta/R directions can be discarded.

## Open mother target and capability debt

All-prime `Delta_p-R_p=0 mod p` remains OPEN for both classes; the finite cases neither close it nor independently review prior Source authors. The distinct same-original-class native fixed p373 H0/B0 divided-power experiment `[X]U mod 139129`, actual module rank, semilinear Frobenius direction, normalization eta, signed odd Green/Hesse kappa, comparison with original Delta/R and independent replication is **NOT_RUN/PENDING_OWNER** under existing support issue #1559. There is no verified native owner. The ordinary quadratic Hesse candidate is not used as a substitute.

Research lane's historical Source session `MCP-5378d3819d8947bda9049c9428493e2d` was previously registered, but this client lacks its private session capability; no current authenticated CLAIM, open run, native Source checkpoint, Result or HANDOFF is asserted. The exact read-only request `onhour11-20261110-2205-exact-cont` is separately reconciled and does not confer execution authorization. The maintenance lane identity and IDs are not used for any role-bound action.

**Next action:** first route an authorized *native* evaluator to the original fixed p373 H0/B0 [X]U and its full acceptance conditions (#1559). If still unowned, preserve the pending support path, and for mathematics attack the signed original LIFT all-prime cancellation `Delta-R=0` with the existing sourced CM first-jet and WZ/Clausen carriers; do not extend these seven finite scalar checks as a proxy for the missing experiment.

Scientific pin and Source-author claims stay distinct. No scheduler or hosted cron created; no claim/dispatch inferred from this Git author note.
