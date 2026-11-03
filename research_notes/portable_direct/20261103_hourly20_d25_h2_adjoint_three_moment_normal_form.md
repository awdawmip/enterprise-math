# D25 — High-band adjoint, three-moment normal form, signed endpoint certificates

Date: 2026-11-03. Status: AUTHOR-DERIVED / ALGEBRAICALLY-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. TASK_RESEARCH logical conversation: chatgpt-research-hourly-enterprise-math-20260923. This is portable evidence, not a canonical Source checkpoint/Result.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3; parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.

## Input and question

Consume the existing D25 original-source result in research_notes/portable_direct/20261103_hourly20_d25_character_hypergeometric_h2_ode.md and the full low/middle/high reduction in 20261103_hourly20_d25_fermquotient_middle_second_digit.md.

For prime p=6r+1 >=7, let
b_k=(2k)!(3k)!/((k!)^5 216^k), H2=sum_{k=3r+1}^{4r}(6k+1)b_k.
Let chi=(6/p), T_s=(1)_s(5/6)_s(7/6)_s / [(3/2)_s^3 2^s] in F_p for 0<=s<=r.
Previously established original-source map: b_{3r+1+s}/p^2 = chi*T_s/9 mod p for 0<=s<r. Set M_j=sum_{s=0}^{r-1}s^j T_s. H2/p^2=chi*(6M1+4M0)/9 mod p.

Selected new question: determine a discrete adjoint for this high-band hypergeometric source, the exact terminal contribution, and the minimum polynomial normal-form dimension for its signed observer.

## Theorem 1: discrete Green adjoint with genuine terminal boundary

For any polynomial P(s) define
 L(P)(s)=[(s+1)(6s+5)(6s+7)/9]P(s+1)-(2s+1)^3 P(s).
Since q(s)=T_{s+1}/T_s=(s+1)(6s+5)(6s+7)/[9(2s+3)^3], exact telescoping yields

  sum_{s=0}^{N-1} L(P)(s)T_s=(2N+1)^3 P(N)T_N-P(0).

When N=r, the numerator 6(r-1)+7=6r+1=p forces T_r=0 mod p, while all denominators remain units. Therefore for every p=6r+1 >=7,

  sum_{s=0}^{r-1} L(P)(s)T_s = -P(0) (mod p).                     (A)

Proof is the termwise difference of (2s+1)^3P(s)T_s, followed by the justified exact terminal zero.

## Theorem 2: unique three-moment normal form

Over Q[s], and also over F_p[s] for p>=7, for every polynomial W(s) there are UNIQUE P(s) and d0,d1,d2 such that

  W(s)=L(P)(s)+d0+d1*s+d2*s^2.                                   (B)

For nonzero P of degree m with leading coefficient a, L(P) has degree m+3 with leading coefficient -4a: the forward cubic contributes +4a, the backward cubic contributes -8a. Repeated leading-degree cancellation proves existence; the same degree shift proves uniqueness and that the polynomial quotient by L(Q[s]) has dimension 3.

Consequently the source-preserving mod-p finite observer formula is

  sum_{s=0}^{r-1}W(s)T_s=d0*M0+d1*M1+d2*M2-P(0) (mod p).        (C)

In particular, L(1)=(-36s^3+53s+26)/9 and
L(s)=(-36s^4+36s^3+161s^2+133s+35)/9, yielding the universal exact certificates

  36*M3-53*M1-26*M0=9 (mod p),                                   (D)
  36*M4-36*M3-161*M2-133*M1-35*M0=0 (mod p).                  (E)

The three-dimensional quotient is relative to this FIRST-ORDER polynomial telescoping operator; it is not a blanket minimality claim for every possible output or future operation.

## Theorem 3: exact scope of p-independent single-index rational obstruction

In characteristic zero, no rational R(s) in Q(s) satisfies

  q(s)*R(s+1)-R(s)=6s+4.                                         (F)

Indeed, more generally no nonzero right-hand polynomial of degree <3 is possible. To prove this, suppose rational R has poles. Within any orbit modulo integer translation, its largest pole alpha_max must be a pole of q, which has only pole -3/2. The smallest pole alpha_min forces q to vanish at alpha_min-1; the q zeros are -1,-5/6,-7/6, forcing alpha_min in residue class 0,+1/6 or -1/6 modulo Z. No such class equals the half-integer pole class -3/2, contradiction. Hence R is polynomial. Cancelling the triple pole of q at -3/2 forces R(s)=(2s+1)^3 P(s). Then the left side is L(P), of degree >=3 unless P=0. Formula (F) is impossible. The result leaves p-dependent terminating certificates, multi-index WZ and low/middle/high couplings open.

## Verification, source and information fidelity

The attached standalone standard-library exact checker evaluates the recurrence, 9 polynomial normal forms, (A),(D),(E) for all 148 primes 7<=p<=2000 with p=1 mod6: PASS, 22,952 high-band field coefficients. For p=7,13,19,37,373,1999 it independently constructs the original factorial p-free units for b_{3r+1+s}/p^2, verifies every index and recovers the signed original H2: PASS.

Examples (p,r,M0,M1,M2,M3,H2/p²):
(13,2,2,1,1,1,10);
(19,3,15,13,11,7,9);
(373,62,121,142,234,162,266).
All examples satisfy (D). General statements above have algebraic proofs; the finite tests provide arithmetic regression evidence.

BRC carrier: retain original factorial b_k and signed index k=3r+1+s, valuation 2, chi, T_s with the witness P and terminal -P(0). This normal form preserves the declared polynomial F_p observer; the source remains necessary for higher precision, Frobenius and other strips. x in the generating function is an auxiliary scalar, not native X6 space.

Next exact action: use (A)-(C) as the high-band adjoint normalizer in the already established low+middle+H2 mod p^3 formula, seek a *p-dependent* signed two-index WZ/Green certificate, and test all 2r/3r/4r endpoints with original arithmetic for p=13,19,373. The frozen mother target W_{p-1}=p mod p^3 for p mod24 in {13,19} remains open.

Control: em_status 0.6.11 on 2026-11-03 reported UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false and quota 5/5. Existing recovery #6637 has no own pending claim/run and reports two neutral preserved staging manifests; continuation #6638 definitively FAILED. No new native CLAIM, open, checkpoint, Result, review or admission. Keep historical session, staging, immutable pins and the Research-vs-maintenance identity boundary intact.