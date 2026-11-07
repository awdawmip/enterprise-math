# D25 — Quartic-twisted CM exchange: individual entries at p=19 and p=373

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT  
Publication: TP2-B6F4FC938FF94941C1B7  
Frozen scientific pin: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3  
Continuation source: current D25 Prop-16 bridge at 4efef1592c0e576b11478352e8ca97c835ebd3ee, blob ebf3a0d1efef5c472ef45eff469ecae3d9caf22c2  
Researcher-ID: EM-DIRECT-912549 (local direct allocation; global identity registration verified; native Source binding unconfirmed)  
Research-Activity-ID: RA-0CA61A48E6C904E1952278E8  
Status: AUTHOR_SIDE_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED

## 1. Individual-entry formula

The pinned D25 bridge establishes, for target primes p>=13 with p=13 or 19 (mod 24),
A_p B_p^CM = 1 in k=F_p[T]/(T^2-2), where sigma(T)=-T,
A_p=a_(p-1)/p, B_p^CM=beta^(-1)b_(p-1), beta=(4-T)/72.

For the d=3 quartic coordinate twist xi_tilde=alpha xi, alpha^4=1/2, put gamma=alpha^(p-1). The pinned twist calculation gives gamma^2=-1. Hence
A_tilde=gamma A_p, B_tilde=gamma B_p^CM, and A_tilde B_tilde=-1.

In the ordered original-E3 CM eigenbasis (omega, nu), nu=eta+beta omega, the Hodge-ordered coefficient-side semilinear exchange has
F_gamma(omega)=p sigma(A_tilde) nu,
F_gamma(nu)=B_tilde omega.
For F_gamma(v)=M_gamma sigma(v),
M_gamma = [[0, B_tilde], [p sigma(A_tilde), 0]].

The first column is p-divisible (invariant/Hodge line); the complementary eigenline port is a unit. Semilinearity forces sigma on the divided coefficient. Directly,
M_gamma sigma(M_gamma)
= diag(p B_tilde A_tilde, p sigma(A_tilde B_tilde))
= -p I (mod p^2).

This refines the earlier product-only result. The unit entry is specified modulo p; the lower-left entry is specified modulo p^2. No p^2 lift of the unit entry is asserted.

## 2. Exact specializations

Choose gamma=3T at p=19 and gamma=104 at p=373; both square to -1. Choose u=4 and u=177 respectively, so u^2=-3. Pairs denote a+bT.

| Quantity | p=19 | p=373 |
|---|---:|---:|
| A_p | 11+16T | 349+48T |
| b_(p-1) | 16T | 49T |
| beta | 18+5T | 228+316T |
| B_p^CM | 18+17T | 131+262T |
| gamma | 3T | 104 |
| A_tilde | 1+14T | 115+143T |
| B_tilde | 7+16T | 196+19T |
| sigma(A_tilde) | 1+5T | 115+230T |
| lower-left p sigma(A_tilde) mod p^2 | 19+95T mod 361 | 42895+85790T mod 139129 |
| semilinear square | -19 I mod 361 | -373 I mod 139129 |

Thus
M_19 = [[0, 7+16T], [19+95T, 0]],
M_373 = [[0, 196+19T], [42895+85790T, 0]],
with semilinear action T -> -T. Upper-right entries are modulo p; lower-left entries modulo p^2.

The inverse-pullback convention replaces gamma by gamma^(-1)=-gamma, negating both entries but preserving [-p]. The quartic sign gauge must remain explicit.

## 3. Sign and conjugation controls

Before twisting,
M_0 = [[0, B_p^CM], [p sigma(A_p), 0]]
and M_0 sigma(M_0)=+p I (mod p^2). Its lower-left entries are 209+57T mod 361 at p=19 and 130177+121225T mod 139129 at p=373. This agrees in sign with the separately recorded unmodified geometric q-Frobenius point-count result at these primes. Multiplying both ports by gamma, gamma^2=-1, changes +p to -p.

A negative control replacing p sigma(A_tilde) by p A_tilde fails at both primes. Exact diagonal outputs are in EXACT_OUTPUT.txt. Therefore T -> -T cannot be dropped.

## 4. Divided-power port and native H0/B0 observer

The coefficient-side divided port is D_p = sigma(A_tilde) mod p:
D_19=1+5T mod 19; D_373=115+230T mod 373.
The corresponding E3 lower-left coefficient at the native benchmark precision is
C_373=42895+85790T mod 139129 (and C_19=19+95T mod 361).

These are comparison targets, not a claimed equality with native H0/B0 [X]U. Issue #1559 remains open and unassigned; no native [X]U execution/value was available. A valid comparison requires an authenticated map from (omega,nu) to native H0/B0 carrying quartic gauge, source/target Frobenius direction, identity branch, exact Laurent principal part, CM normalizer, eta and kappa. Until both map and native value exist, status is COMPARATOR_VALUES_DERIVED / NATIVE_VALUE_NOT_EXECUTED, not MATCH or MISMATCH. Do not substitute S_mid, K-H scalar, coefficient product, norm or trace for [X]U.

## 5. Exact verification and scope

VERIFY_CM_EXCHANGE.py uses Python standard library only. It recomputes a_(p-1), b_(p-1) modulo p^3 in (Z/p^3)[T]/(T^2-2), then checks at p=19,373: divisibility by p; A_p b_(p-1)=beta; A_p B_p^CM=1; gamma^2=-1; A_tilde B_tilde=-1; both entries of the twisted semilinear square equal -p mod p^2; both entries of the untwisted square equal +p; omitting sigma fails; and the opposite quartic gauge preserves the square. Actual stdout is EXACT_OUTPUT.txt.

This is an exact two-prime specialization check. The all-target-prime coefficient identity remains conditional on the cited published Proposition-16 d=3 lift and the pinned D25 CM/branch identities; the two-prime run is not an all-prime computation.

## 6. BRC / P000 / ACTIVE-world audit

Carrier retained: original E3 identity branch, both CM eigenlines, unramified quadratic coefficient field, quartic gauge, invariant and second-kind streams, full semilinear exchange. Observers retained separately: A_p, B_p^CM, gamma, A_tilde, B_tilde, unit entry, divided entry, semilinear square, native [X]U. BRC resolution: COMPOSE_APPLIED; no new primitive or destructive quotient. Preserve T -> -T, eigenline labels, twist sign, source/target direction, Hodge valuation, principal part and coefficient/native observer distinction.

P000 / ACTIVE worldview unchanged: this is external elliptic-curve/formal-cohomology arithmetic over a finite quadratic coefficient field, not a native X6 spatial plane or lower-dimensional Enterprise space; no time coordinate is required.

## 7. Sources, authority, next question

Frozen input: task publication record TP2-B6F4FC938FF94941C1B7 and pin c47e13e4aba0e006366f989d6334d443f6333ae3. Continuation sources: pinned D25 Prop-16 bridge; original-E3 three-isogeny/CM exchange; signed de Rham transport; p=373 twist-sign gauge; second-kind coefficient note; q-Frobenius trace note; frozen D24 UR/JT0 return. External source in the pinned bridge: Chisholm–Deines–Long–Nebe–Swisher (2013), “p-Adic Analogues of Ramanujan Type Formulas for 1/pi,” Proposition 16 and §4.3.

Next: obtain authorized native H0/B0 [X]U at p=373 mod 139129 and the typed E3-to-native basis map. Compare with C_373 if native returns the undivided lower-left port, or D_373 if it explicitly returns the quotient; retain the companion unit port 196+19T mod 373. Cross-check the same map at p=19. Any mismatch is a scoped observer/basis residual, not a refutation of the coefficient identity. The mother LIFT Delta_p-R_p=0 mod p and W_p=p mod p^3 for all target primes remains OPEN. No review or Result admission is claimed.

Authority: taskbook owner is taskbook/unassigned; issue #1559 has no assignee. Site phase CONFIGURED_NOT_LIVE_VERIFIED, backend_connected=false, research_authority_granted=false; native status/task/source calls return BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE, operation_sent=false. No CLAIM or Source session was created.