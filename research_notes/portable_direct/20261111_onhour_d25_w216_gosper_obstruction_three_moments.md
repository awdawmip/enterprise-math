# D25 original W216 — no rational one-term Gosper telescoper; exact three-unit-moment reduction

Date: 2026-11-11. Role: TASK_RESEARCH (logical lane chatgpt-research-onhour-enterprise-math-20260923). Status: AUTHOR_SIDE / PROOF_AND_13_EXACT_CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Immutable frozen science: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3.
Original highest-priority benchmark [X]U modulo 373^2=139129 is still NOT_RUN, supported by Issue #1559 and without confirmed native executor.

## 1. Exact scoped Gosper obstruction (characteristic zero)

Take the original hypergeometric summand

a_k=(2k)!(3k)!/[216^k(k!)^5], w_k=6k+1,
r(k)=a_(k+1)/a_k=(2k+1)(3k+1)(3k+2)/[36(k+1)^3].

There is NO rational function T(k) in Q(k) satisfying

    r(k) T(k+1) - T(k) = 6k+1.                           (G)

Thus this original signed hypergeometric term has no one-term rational Gosper antiderivative G_k=T(k)a_k. This is only a statement about one-term rational Gosper certificates, not general WZ/creative telescoping, algebraic antiderivatives, nor the solvability of LIFT.

Proof. Put A(k)=(2k+1)(3k+1)(3k+2), B(k)=36(k+1)^3. Equation (G) becomes

    A(k)T(k+1)-B(k)T(k)=(6k+1)B(k).                    (1)

Suppose rational T has a finite pole. In one integer-translation orbit of poles take the leftmost pole z_min and rightmost z_max (real parts, since the orbit differs by integers). At k=z_min-1, T(k) is regular and T(k+1) has a pole; hence A(z_min-1)=0, so z_min belongs to {1/2,2/3,1/3}. At k=z_max, T(k+1) is regular and T(k) has a pole; hence B(z_max)=0, so z_max=-1. This is impossible because Re(z_min)>Re(z_max). Therefore T is polynomial.

As k tends to infinity, r(k) tends to 1/2. A polynomial solution of degree d must have degree d=1 and leading coefficient -12, because the right side of (G) has leading term 6k. Write T(k)=-12k+b. Substituting k=-1 into (1) gives A(-1)T(0)=0 and A(-1)=-2, hence b=0. Substituting k=0 gives 2T(1)-36T(0)=36, hence T(1)=18, contrary to T(1)=-12. QED.

The proof uses exact polynomial/rational identities; the optional SymPy gosper_sum returning None was a search hint, not the proof.

## 2. Positive exact reduction using the canonical leading-term near-telescoper

Although T(k)=-12k is not a solution, its residual factors exactly:

    A(k)T(k+1)-B(k)T(k)-(6k+1)B(k)
      =12(k-1)(k+1)(6k+5).

Let G_k=-12k a_k and E_k=a_k (k-1)(6k+5)/[3(k+1)^2]. Then for ALL nonnegative integer k,

    (6k+1)a_k = G_(k+1)-G_k-E_k.                       (2)

For any prime p>3, summing (2) through k=p-1 and isolating the final term gives the exact rational identity

    W_p=(7-6p)a_(p-1)-sum_(k=0)^(p-2) E_k.            (3)

Indeed G_p-E_(p-1)=(7-6p)a_(p-1) follows directly from the original factorial recurrence. Since v_p(a_(p-1))=floor((2p-2)/p)+floor((3p-3)/p)=1+2=3, the first term in (3) vanishes modulo p^3. Every remaining denominator k+1, 0<=k<=p-2, is a p-unit.

Define the three original-index moment ports over Z_(p):

    M_j(p)=sum_(k=0)^(p-2) a_k/(k+1)^j  (mod p^3),   j=0,1,2.

The partial fraction identity

    (k-1)(6k+5)/[3(k+1)^2]
      =2-13/[3(k+1)]+2/[3(k+1)^2]

proves for every prime p>3 the exact congruence

    W_p = -2 M_0(p)+(13 M_1(p)-2 M_2(p))/3  (mod p^3). (4)

For both frozen classes p≡13,19 mod24, the already accepted first-digit UR plus separately established exact source alignment gives the original LIFT equivalence

    Delta_p-R_p=0 (mod p)
      iff -2 M_0+(13 M_1-2 M_2)/3=p (mod p^3).       (5)

This is a new exact source-preserving representation of the OPEN LIFT condition, not an all-prime proof of it. Its decisive difference from direct summation is the removal of the singular k=p-1 boundary and preservation of three labeled p-unit-denominator ports. No minimality or asymptotic improvement is claimed.

## 3. Exact p=373 certificate

All entries below are residues modulo 373^3=51895117 in the frozen original summand:

    M_0= 9878159
    M_1=48777891
    M_2=27945670

The right side of (4) is 373 (mod 51895117), matching the independent direct 373-term W216 sum. The unreduced boundary diagnostics are

    -12p a_p=19431435  (mod p^3),
    E_(p-1) =19431435  (mod p^3),

so their difference vanishes at the required precision; the omitted exact term (7-6p)a_(p-1) has v_p>=3. The integer checker further tests 13 primes p=5,7,11,13,17,19,23,31,37,43,109,157,373 against direct original coefficients, p-free factorial endpoint, and the three moments. All assertions passed with integer arithmetic.

## 4. BRC typing and next direct research action

Carrier: labeled original k, exact valuation of a_(p-1), signed residual E_k, three ordered moment ports M_0/M_1/M_2. Observer: W_p modulo p^3 and the frozen scalar Delta_p-R_p modulo p. Allowed future operation: p-adic moment comparison and original native H0/B0 source-to-scalar identification. The derivation is in the ordinary external p-adic coordinate model; it is not an X6-native spatial reduction.

The exact one-term rational Gosper route is now ruled out for the fixed original term. Next direct mathematical tests must either derive a genuinely different higher-order/parameter telescoping identity that evaluates the specific combination (4), or produce a valid original-target counterexample; a bare extra prime scan or another restatement of already known Clausen is not a closure. The strictly higher-priority native experiment remains same-original-class H0/B0 divided-power [X]U mod139129 with actual module rank, semilinear direction, eta, signed odd kappa, Delta-R and independent replay. Issue #1559 is an OPEN PENDING_OWNER support intake.

## 5. Provenance and Source isolation

The previous #6760 bridge continuation (original request onhour-d25-20261111-1810-source-continuation) was read back as SUCCEEDED with Source d8203792ff835058e2212a7654f85830a9b51aca, route PREPARE_TYPED_CONTINUATION_WITH_EXACT_PREDECESSOR_AND_FRONTIER and execution_authorized=false. The own ordinary bridge recovery #6759 returned REGISTRATION_FAILED for old session-start-20261007-1122-d25-01, which itself has FAILED / UPSTREAM_CODE_REVIEW_REQUIRED. No current own winning CLAIM/open run, Source-native checkpoint, Result/freeze or independent review is asserted. This GitHub note is AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED; prior owner/contribution and frozen scientific pins remain unchanged.

Reproducible companion: research_notes/portable_direct/d25_w216_gosper_moment_verify_20261111.py.
