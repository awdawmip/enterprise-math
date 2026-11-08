# D25 — Semilinear CM exchange: conjugate second port and quartic-norm parity

Date: 2026-11-08 (Asia/Hong_Kong).
Status: AUTHOR_SIDE_CONDITIONAL_ALGEBRA_PROVED / EXACT_8_E3_PRIMES_AND_77_QUARTIC_PRIMES_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7. Immutable scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
Logical research lane: chatgpt-research-onhour-enterprise-math-20260923. Excluded maintenance lane: chatgpt-hourly-enterprise-math-20260921.

## Dependency and precise question

Consume the already persisted author-side original-E3 coefficient identity in
research_notes/portable_direct/20261108_onhour_d25_prop16_quartic_twist_cm_companion_bridge.md.
That prior unit supplies, for every prime p >= 13 with p mod 24 = 13 or 19, the *author-side* identity
A_p B_p = 1 in k = F_p[s]/(s^2-2), where A_p = a_(p-1)/p mod p and
B_p = beta^(-1) b_(p-1) mod p, beta=(4-s)/72. It has not been independently admitted as a Source Result.
The present algebraic theorems are conditional only on this explicit coefficient input, not on
an unexecuted native H0/B0 experiment. On these prime classes, (2/p)=-1 and sigma(s)=-s.

Discriminating question: does the ordinary coefficient product A_p B_p=1 determine the
two entries of a *sigma-semilinear* exchange whose square is [-p]? What does the quartic
coordinate factor do under sigma-semilinear composition, compared with ordinary products?

## Theorem 1 — an explicit coefficient-compatible semilinear lift

Let R_2=(Z/p²Z)[s]/(s²-2), sigma(s)=-s, sigma²=1.
Take arbitrary lifts a,b in R_2 of A_p,B_p with ab=1 mod p.
In the declared two-line module V=R_2 e_+ + R_2 e_-, define a sigma-semilinear map by

    Phi(e_+) = b e_-
    Phi(e_-) = -p sigma(a) e_+.

Its matrix, with columns in the ordered basis (e_+,e_-), is

    M_Phi = [ [0, -p sigma(a)],
              [b,  0         ] ] .

Then M_Phi sigma(M_Phi) = -p I (mod p²). Indeed, its two diagonal entries are
-p sigma(a) sigma(b) and -p b a, and both equal -p because ab=1 mod p.
The individual ports have valuations 0 and 1, respectively; the p-scaled port
is NOT -p a in general, but -p sigma(a). This conjugation is forced by
sigma-semilinear composition.

The construction supplies a reproducible coefficient-*compatible candidate*;
it is not an identification with the actual crystalline Frobenius, whose native
module rank, generator calibration and divided-power [X]U are independent data.

## Theorem 2 — gauge classification and minimum missing observer

For an arbitrary unit u in k, the semilinear matrix

    M(u) = [ [0, -p sigma(u)^(-1)],
             [u, 0] ]

satisfies M(u) sigma(M(u))=-pI mod p², interpreting u through any lifts.
Every possible nonzero choice of the mod-p unit exchange port gives such a
candidate. Replacing e_+ by lambda_+ e_+, e_- by lambda_- e_- acts by

    M -> diag(lambda_+,lambda_-)^(-1) M sigma(diag(lambda_+,lambda_-)).

Hence the lower port changes as u -> lambda_-^(-1) u sigma(lambda_+).
In particular, changing lambda_- can prescribe any unit lower coefficient.
Thus the square relation and the CM eigenline decomposition alone determine a
gauge class, not the entries in a fixed geometrically normalized eigenbasis.
One independently calibrated image of an original differential/eigenvector
(and the basis transformation including the eta principal part) fixes the missing
unit port; then the other is forced. This identifies the exact native-data
dependency rather than silently substituting the product A_p B_p.

## Theorem 3 — quartic twist: ordinary sign versus semilinear norm

Fix alpha^4=1/2 and, for p=19 mod 24, the convention alpha²=s/2.
Let delta=alpha^(p-1). Since (s/2)^p=-(s/2), in both classes delta²=-1.
But its semilinear norm splits:

  p=13 mod 24: delta=2^(-(p-1)/4) in F_p, so delta sigma(delta)=-1.
  p=19 mod 24: delta=2^(-(p+1)/4) s in s F_p, so delta sigma(delta)=+1.

Consequently, scaling both ordinary coefficient ports by delta changes their
ordinary product by delta²=-1 in BOTH classes, but scaling the semilinear map
changes its square by delta sigma(delta):

    (delta Phi)² = (delta sigma(delta)) Phi²
                 = +p I  (p=13 mod 24),
                   -p I  (p=19 mod 24)                 mod p².

This precise parity split shows why the quartic product-sign transport from
Proposition 16 cannot simply be reused as a sigma-semilinear Frobenius-square
sign without an operator/basis calibration. The p=19 sign of alpha² changes
delta but not this norm.

## Exact original-E3 numerical discriminants

The companion checker independently recomputes the E3 original-coordinate
coefficient streams from their integer binomial formulas modulo p³. Then it
divides a_(p-1) by p, normalizes b_(p-1) by beta, and tests the semilinear
matrix modulo p².

| field | p=19 | p=373 |
|---|---|---|
| A_p | 11+16s | 349+48s |
| B_p=beta^-1 b_(p-1) | 18+17s | 131+262s |
| Phi(e_+) coefficient u=B_p | 18+17s | 131+262s |
| Phi(e_-)/p coefficient -sigma(A_p) | 8+16s | 24+48s |
| Upper matrix entry -p sigma(A_p), mod p² | 152+304s (mod 361) | 8952+17904s (mod 139129) |
| Phi² diagonal | -19=342 (mod 361) | -373=138756 (mod 139129) |
| Incorrect -p A_p substitution, Phi² diagonal | 76+247s | 119733+39538s |
| quartic delta | 3s | 269 |
| delta sigma(delta) | +1 | -1 |

The incorrect -p A_p substitution fails BOTH discriminating examples with a
nonzero s-component. In addition to p=19 and 373, exact E3 checks pass at
p=13,37,43,61,67,211. The quartic sign/norm formulas pass at ALL 77 target
primes p<=2000, with exact modular arithmetic. No floating approximation is
used. Executable evidence: d25_semilinear_cm_gauge_check_20261108.py.

## BRC observer and frozen benchmark

Carrier: two distinct CM eigenspaces, valuation-0/valuation-1 semilinear
ports, sigma conjugation, quartic scalar and its ordinary square/norm. The
ordinary product A_p B_p is a derived scalar observation and loses the
semilinear orientation. COMPOSE_APPLIED: previous original-E3 coefficient
pair and the existing BRC typed-port/valuation observer are used to derive
the square condition and gauge calibration requirement. Do not coalesce the
two ports into a scalar before the sigma operation.

The native same-original-class H0/B0 benchmark in issue #1559 remains
NOT_EXECUTED / PENDING_OWNER. Required independent data include the native
module rank, basis normalization and eta principal-part treatment, [X]U
mod p² for p=373 (then p=19), Frobenius direction, signed odd Hesse/Green
kappa and original Delta_p-R_p. If the native object is not rank-one, keep
the actual matrix/operator and retype the comparison; no rank-one
candidate is imposed on native H0/B0.

The mother targets remain Delta_p-R_p=0 mod p and W_p=p mod p³ at
p=13,19 mod 24. The new theorem addresses a precise operator-translation
dependency; it does not close either target.

## Source/identity continuation

Original target_request_id: onhour11-20261106-1400-exact-research-lane-continuation.
In this run em_status and the original receipt read both returned
BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR /
STATUS_DATABASE_UNAVAILABLE, operation_sent=false.
The Site reports CONFIGURED_NOT_LIVE_VERIFIED, backend_connected=false,
research_authority_granted=false. No Source-native session, claim, run,
checkpoint, review or Result is asserted. These artifacts are author-side
GitHub evidence only. Next step: native authorized executor takes #1559,
runs the frozen p373 original benchmark and calibrates its semilinear CM
operator against the separately displayed pair of coefficient ports.
