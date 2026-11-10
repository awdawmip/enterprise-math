# D25/JT2 — original W216 polynomial-observer reflection at precision p^3

Date: 2026-11-11, Asia/Hong_Kong. Classification: AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN. This is a theorem about the *original* W216 coefficients and original index observer, not a native H0/B0 computation or authorized Source execution. Declared research lane: chatgpt-research-onhour-enterprise-math-20260923; no service-issued active CLAIM/open run has been authenticated here. Never use maintenance conversation chatgpt-hourly-enterprise-math-20260921 as a Researcher.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; original scientific freeze: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3. The accepted first digit and old auxiliary results are consumed, not reopened. Previous source-index half-range scalar theorem: research_notes/portable_direct/20261111_onhour_d25_W216_half_range_signed_LIFT_certificate.md (blob af9351dd2108dd66ee40b244fc58e13cb224ed70).

## I. New exact statement: preservation for *every* polynomial observation

Let p>3 be prime, H=(p-1)/2, T=floor((p-1)/3), and in the p-local integers put

    a_k = (2k)!(3k)! / (216^k(k!)^5),    0<=k<p.

For every polynomial P(X) in Z_(p)[X] define the original labeled source observation

    M_p(P) = sum_{k=0}^{p-1} P(k) a_k.

For T<k<=H define the valuation-one unit

    u_k = a_k/p mod p = -(2k)!(3k-p)!/[216^k(k!)^5] mod p.

Then, for every prime p>3 and every such P, *without a degree bound*,

    M_p(P)
      = sum_{k=0}^{H} P(k) a_k
        + p^2 sum_{k=T+1}^{H} P(-k)/(36 k^3 u_k)
        (mod p^3).                                          (POLY)

Every denominator in the correction is a p-unit. The polynomial values on the first half retain their original p^3 precision; only P(-k) mod p is needed in the reflected band. In particular, for j>=0,

    M_p(X^j) = sum_{k=0}^H k^j a_k
                  + (-1)^j p^2/36 * sum_{k=T+1}^H k^(j-3)/u_k
                  (mod p^3),

where negative exponents mean inverses in F_p. The original signed observer is P(X)=1+6X and its exact repair is J_ref,p = C_0+6C_1, where C_j is the j-th finite-field moment correction.

This strengthens the preceding scalar half-range formula in two precise ways: (a) its same-original-class p-adic argument applies to **all p>3**, including p=6m+5, and (b) it preserves the full module of p-local **polynomial index observations**, not only the one signed linear weight. It is a strict exact source-observer factorization at precision p^3, not a new native Frobenius or independent validation of LIFT.

## II. Complete finite arithmetic proof

For 0<k<p, v_p(a_k)=floor(2k/p)+floor(3k/p), because 216 and k! are p-units. Pair k with p-k, with 1<=k<=H; k=0 stays in the low half. For 1<=k<=T, the low coefficient has valuation 0 and the high partner valuation 3, hence P(p-k)a_(p-k)=0 (mod p^3). For T<k<=H the respective valuations are 1 and 2.

Write s=3k-p. In that second band 1<=s<p. Wilson's theorem gives the exact first-unit congruences

    (2k)!(2p-2k)! / p   = -2k       (mod p),
    (3k)!(3p-3k)! / p^2 = (-1)^s s (mod p),
    k!(p-k)!              = (-1)^k k (mod p).

With 216^p=216 (mod p) and s-k=2k-p odd, these imply

    a_k a_(p-k) / p^3 = 1/(36 k^3) (mod p).

Because a_k/p=u_k is a unit, one obtains

    a_(p-k) = p^2/(36 k^3 u_k) (mod p^3).

Since P(p-k)=P(-k) (mod p) for P in Z_(p)[X], the high partner contribution is exactly p^2 P(-k)/(36k^3u_k) modulo p^3. All pairs are disjoint, which proves (POLY). For T<k<=H, (3k)!/p = -(3k-p)! (mod p), yielding the displayed source-unit formula. This completes the proof for every prime p>3 and every P in the declared domain.

BRC/observer semantics: population is original 0<=k<p and exact index labels; operation is involution k<->p-k. Retain valuation 0/1 low coefficients mod p^3 and valuation-one units u_k plus signed reflected P(-k) mod p. Kill only high valuation-3 partners at this precision. The preserved family of future operations is all linear polynomial-index observations (not arbitrary nonlinear state access). This supplies a typed, observer-faithful compact source representation, not just a scalar total.

## III. Exact author-side verification and discriminating example

Reproducible Python standard-library checker:
research_notes/portable_direct/d25_w216_allprime_polynomial_observer_reflection_20261111.py .

Executed locally using recurrence for the original complete coefficient array; an independent integer-binomial constructor checked every coefficient for p=5,11,13,19,37,109,139,157,373,997. A separate factorial-stripping constructor checked each middle-band unit against the recurrence coefficient. Across all 166 primes 5<=p<=997 (80 p=1 mod6, 86 p=5 mod6), there were **830 exact independent polynomial moment congruence checks** at degrees 0..4 and 166 separate signed P=6X+1 checks. All passed; arithmetic was integer modular, no floating point. This is supporting finite evidence for the algebraic theorem, not a claim that the 166 tests prove the all-prime case.

Precision-sensitive witness at p=373, with every C_j reduced mod 373:

    (C_0,C_1,C_2,C_3,C_4) = (28,164,131,59,252).
    C_0+6 C_1 = 28+6*164 = 1012 = 266 (mod373).

The original signed low-half sum is S_373=14,887,176 (mod373^3), while the full signed sum is W_373=373 (mod373^3). The exact reflected repair is 373^2*266, and these values reconstruct the full signed observer. Distinct low-degree moment ports 28 and 164 are both nonzero: an unweighted scalar alone would discard the particular signed correction needed by LIFT. The original target second-digit certificate remains L_373=107 and J_ref,373=266, cancelling only after retaining both ports.

For p=5 and 11 (outside the frozen p=13/19 mod24 target), the signed corrections are 1 and 1 respectively, furnishing explicit boundary tests of the new all-prime quantifier. In this 166-prime sample, W_p equals (Legendre(-3,p))*p modulo p^3; this last statement is **finite observation only** and is not used in the proof of (POLY).

## IV. Exact continuation and native outstanding gate

Mathematical parent target remains: for each prime p=13 or 19 mod24, prove or refute original Delta_p-R_p=0 mod p, equivalently L_p+J_ref,p=0 mod p under the prior accepted source-port identity. (POLY) is reusable as an independently auditable, signed polynomial observer transport; it alone does not establish the cancellation. Next mathematical proof unit: derive a finite terminating identity that forces the signed low-half p^2 digit plus its p^2 reflection repair to vanish *for both target residue classes*, retaining the original two ports and without assuming the target congruence.

Highest native evidence gate unchanged: existing GitHub Issue #1559, PENDING_OWNER / NOT_EXECUTED. Exact required object is original, same-CM-class H0/B0 divided-power [X]U mod 139129 at p=373; retain module rank, true semilinear Frobenius direction/eta, odd signed Green/Hesse observer kappa, original Delta_p-R_p and independently reproduced raw data. The externally derived ordinary Hesse norm 122102 mod139129 is a *conditional comparison*, not a native coefficient.

Control: exact canonical read request onhour11-20261111-0204-exact-cont -> SUCCEEDED, Source 2c91711f60aa74d93880780929f532da24140ec0, router PREPARE_TYPED_CONTINUATION_WITH_EXACT_PREDECESSOR_AND_FRONTIER, execution_authorized=false. Own recovery_status returned SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED. No authenticated winning CLAIM/open run/Source-native checkpoint; all evidence here remains AUTHOR_SIDE/UNREVIEWED/NOT_ADMITTED. Keep the earlier Source frontier and native #1559 distinct, do not adopt the predecessor's session/claim. Next control action upon lawful capability: recover exact own native session/claim/run from Source, or perform permitted continuation_prepare/claim only under current matching authority; otherwise retain original requests and the support path.

The local checker, this proof, and any JSON continuation are author-side Git objects; Git publication is not Result, freeze, Driver review or official Source checkpoint.
