# D25 / LIFT auxiliary modular-curve first-jet no-go at p = 43

Date: 2026-10-27 Asia/Hong_Kong. Author-side portable proof, exact-check PASS; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. Same shared D25 author context as PR #1566, not an independent review. Original task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; scientific Source frozen at c47e13e4aba0e006366f989d6334d443f6333ae3.

## Exact theorem

Let s²=2 and h_±=(3±2s)/27. On the *auxiliary* X_0(3) parameter define
t=h/(1+27h)², J=(1+27h)(1+243h)³/h,
theta_t=[h(1+27h)/(1-27h)] d/dh.

For fixed A,B in Z_(43) (they may vary with the prime but not with h), observe
O_(A,B)=A J+B theta_t J. Its Laurent pole coefficient at h=0 is A−B; its signed
CM difference is exactly

    O_(A,B)(h_+)−O_(A,B)(h_−)
      = (3414528 A−13519872 B)s.

Since 3414528 ≡ 27 (mod 43) and −13519872 ≡ 16 ≡ −27 (mod 43),

    [O_(A,B)(h_+)−O_(A,B)(h_−)] mod 43 = 27s(A−B).

The polynomial X²−2 is irreducible over F_43, hence 27s is a unit.
Consequently, cusp-pole cancellation modulo 43 and CM-sheet separation
modulo 43 are mutually exclusive for this *constant-coefficient linear
first-jet family*: A=B (mod 43) iff the sheet difference vanishes.

For actual cusp holomorphy over Q_43, A=B exactly. Then the fixed-sheet
difference is

    (A J+A theta_t J)(h_+)−(A J+A theta_t J)(h_−)
      = −10105344 A s
      = −2^9 * 3^3 * 17 * 43 * A s,

which is also zero modulo 43 for all 43-integral A.

## Proof and checks

Set N=(1+27h)(1+243h)^3. Then
J=N/h and theta_t J=[(1+27h)/(1−27h)](N'−J).
At h=0, N=1+756h+196830h²+…, yielding Laurent expansions

    J = h^(-1)+756+196830h+…,
    theta_t J = −h^(-1)−54+…

and the claimed pole coefficient. Direct exact reduction in Q[s]/(s²−2)
at h_± gives

    J(h_+)−J(h_−) = 3414528 s,
    (theta_t J)(h_+)−(theta_t J)(h_−) = −13519872 s.

Reduction modulo 43 gives the boxed proportionality. The naturally
weighted previous observer H=(1+6 theta_t)J retains Laurent pole −5 and
distinguishes sheets by −77704704 s ≡ 37s (mod 43). The earlier modified
M=(9+6 theta_t)J also retains a pole, of coefficient 3. This clarifies the
information cost of the previous successful auxiliary sheet separation.

The adjacent executable standard-library Python checker evaluates the
two CM points exactly with Fraction arithmetic in Q(s); verifies all
integer identities and cross-checks H, M; then exhaustively checks all
43²=1849 pairs (A,B) modulo 43. Result: PASS, 1849/1849.
Mathematical universality over the coefficient pair domain follows from
the symbolic identity; finite enumeration is regression evidence only.

## Scope, BRC and remaining original obligation

BRC COMPOSE_APPLIED: keep sheet label, signed quadratic residue,
cusp Laurent principal part and future observer; the displayed rank-one
relation proves that this attempted quotient removes the same bit of
information at p=43. This external auxiliary quadratic field is not a
P000 native plane or the full Enterprise X6 state.

The theorem excludes neither nonlinear/higher-jet or variable-coefficient
auxiliary observables nor a meromorphic observer that keeps the pole, and
does not establish an original H0/B0/Frobenius transfer. It is not a
proof/counterexample of original W_p≡p (mod p³) or Delta_p−R_p=0.
For a proposed globally cusp-regular *constant-coefficient J/first-jet*
transfer, p43 is an exact failure test. The next genuine research action
is a native same-original-class transfer/provenance certificate with
correct signed ports and the original p373 H0/B0 rank, [X]U mod 139129,
Frobenius eta/kappa (support Issue #1559), not further auxiliary
sheet-only precision scans.

Evidence is author-derived, author-exact-checked, GitHub Draft PR
storage only. Native current winning CLAIM/OPEN/Result and independent
review are not established. Exact continuation read in this run returned
CONTROL_QUOTA; own checkpoint list ACCESS_DENIED; original read request
r40_20261027_1140_cont_read returned CONTROL_REQUEST_NOT_FOUND.
Site static_machine_readonly / write_relay_enabled=false grants no
research write authority. Any current-input-only continuation seed must
have predecessor completed_units=[] and requires full input readback
before lawful prepare.

Original UR V2 four-file source provenance remains separately pending:
94687 bytes, SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76.
This author-only lemma neither reconstructs UR nor counts as its formal
Source checkpoint. Parent objective and frozen scientific source unchanged.

## Target-prime corollary: one exceptional target prime

The h=0 cusp-regular normalized auxiliary first jet J+theta_t J has exact signed sheet difference −2^9*3^3*17*43 sqrt(2). Consequently it separates the original fixed CM sheets modulo every target prime p≡13,19 (mod24) **except p=43**, for which its sheet contrast vanishes. The only prime factors of the exact integer are 2,3,17,43; among target primes only 43 occurs. The difference modulo 13,19,43 has scalar coefficients 11,15,0. All source-point rational denominators are p-units for target p>3. This corollary is local holomorphy at h=0 only, not a claim about every cusp of X_0(3). Classification for all target primes follows from the factorization; the checker additionally verifies 166 target primes below 5000 as finite regression. The restricted constant-linear-firstjet family still has the genuine p43 obstruction; no claim about original native LIFT follows.


## Exact rational form and the retained ramification pole

The h=0-cusp-regular combination has the exact rational simplification

    J+theta_t J = 54(1+27h)(1+243h)^2(13+243h)/(1−27h).

Indeed writing N=(1+27h)(1+243h)^3, the expression is
((1+27h)N'−54N)/(1−27h), and factoring the numerator yields the displayed result.
The cusp h=0 pole cancels, but a pole may remain at the theta_t ramification
locus h=1/27. At the two original CM sheets 1−27h_±=−2(1±sqrt(2)),
whose norm is −4, a unit for every target prime. Thus the target-class
mod-p contrast proved above is well defined. The claimed regularity is
strictly local at h=0; the meromorphic/ramification divisor and its
source-provenance cannot be silently discarded by a native transfer.
