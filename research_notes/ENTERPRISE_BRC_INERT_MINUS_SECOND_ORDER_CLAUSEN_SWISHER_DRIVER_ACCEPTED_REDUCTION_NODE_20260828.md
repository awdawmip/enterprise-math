# Enterprise BRC Inert-Minus Second-Order Clausen–Swisher Bridge — Driver-Accepted Reduction Node

Status: `DRIVER_ACCEPTED_STRICT_EXACT_REDUCTION / RESULT_ONLY / FULL_TARGET_OPEN`

Date: `2026-08-28`

Node:

`ENTERPRISE_BRC_INERT_MINUS_SECOND_ORDER_CLAUSEN_SWISHER_REDUCTION`

Authority:

- result `RR-FFAA492DFF8FEBC025B5`;
- source-backed Driver review `DR-ED785B8184028DBB37C6`;
- human review `driver_reviews/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_SECOND_ORDER_CM_JACOBI_LIFT_AUTHORIZED_DRIVER_REVIEW_20260828.md`.

## 1. Accepted finite identity

For the inert-minus second-order problem, the frozen return proves the exact finite identity

`S_p = W_p`

by symmetrizing `G_p H_p`, subtracting the finite `i+j>=p` tail, and applying the coefficientwise finite Clausen identity.

This is a finite statement. The analytic infinite transformation is not substituted for the terminating boundary.

## 2. Two-scalar to one-scalar compression

For primes

`p == 17 or 23 (mod 24)`, 

the predecessor second-order conditions satisfy the exact equivalence

`(R0-) & (R1-) <=> W_p == -p (mod p^3)`.

Thus two second-order scalar congruences are compressed to one explicit finite scalar target.

## 3. Exact valuation truncation

The valuation law

`v_p(binomial(2n,n)^2 * binomial(3n,n)) = floor(2n/p)+floor(3n/p)`

implies the exact modulo-`p^3` truncation at

`M=(2p-1)/3`

for `p == 2 (mod 3)`.

The truncation boundary is load-bearing and must remain explicit.

## 4. Swisher bridge and smallest exact residue

Swisher's proved finite congruence gives

`E_p == -2p (mod p^3)`

at the exact used `p == 2 (mod 3)` scope.

Therefore the unresolved inert-minus target reduces exactly to the single terminating certificate

`C_p = 2*W_tilde_p - E_p == 0 (mod p^3)`.

This `C_p` certificate is the smallest accepted exact residue of the parent interface.

## 5. Prior-art boundary

Zhi-Wei Sun Conjecture A14(ii) is used only to identify the target family; it is not imported as a theorem.

Swisher's congruence is used only at its proved finite scope.

Finite scans and Domb diagnostics are regression/falsification evidence only.

## 6. Tool-harvest decision

`METHOD_HARVEST = RESULT_ONLY`.

No new toolbox family or domain operator is admitted. The proof composes existing BRC typing with finite hypergeometric/Jacobi/Clausen identities at a task-specific arithmetic interface.

The successor is theorem work on the single finite `C_p` certificate, not tool-building.

## 7. Scope boundary

Accepted:

- `S_p=W_p` finite identity;
- `(R0-)&(R1-) <=> W_p=-p mod p^3`;
- exact valuation truncation;
- reduction to `C_p=0 mod p^3`.

Not accepted:

- the full inert-minus supercongruence;
- Sun A14(ii) as proved;
- an infinite-to-finite transformation shortcut;
- a new reusable toolbox family;
- Working Truth or Foundation promotion.