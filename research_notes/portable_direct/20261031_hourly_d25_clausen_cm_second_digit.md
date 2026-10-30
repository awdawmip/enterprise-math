# D25/LIFT — exact CM second-digit scalar of terminating Clausen denominator jet

Date: 2026-10-31 Asia/Hong_Kong. Research conversation: chatgpt-research-hourly-enterprise-math-20260923, not maintenance. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3 and P000 ACTIVE_LOCKED unchanged. External p-adic scalar model, not a native Enterprise X6 theorem.

## Theorem (conditional only on the established frozen-class CM root)

For prime p=6l+1 with p mod24 in {13,19}, let

T_l(z) = sum_{n=0}^{2l} (-1)^n binom(3l,n)binom(2l,n)binom(4l,n) z^n,

G(z) = sum_{j=0}^l binom(l,j)binom(2l,j) z^j,

theta=z d/dz, W=1+6theta, z0=1/2.

For polynomial P=sum c_n z^n define Hcal(P)=sum H_n c_n z^n, Hcal11(P)=sum H_n^2 c_n z^n and Hcal2(P)=sum H_n^(2)c_n z^n. All harmonic denominators are p-units. Write G1=Hcal(G), G2=Hcal11(G)+Hcal2(G), and

E = (G1^2+G G2)/4 - (3/2)Hcal(G G1) + [9Hcal11(G^2)-5Hcal2(G^2)]/8.

Consume the previously sourced CM condition G(z0)=0 mod p, and set alpha=G(z0)/p in Z_(p). Then the exact normalized SECOND-digit weighted scalar identity is

[W T_l](z0)/p =
    6 alpha G'(z0) + 3 G'(z0) G1(z0) - (3/2) [W Hcal(G^2)](z0)
  + p*[ alpha^2 + alpha G1(z0) + 3 alpha G1'(z0) + [W E](z0) ]
                                            (mod p^2).       (1)

**Proof.** The preceding full-polynomial result at EM commit 4b81d5cf864574c5f2108137cae6fbc599dc653b gives, coefficientwise modulo p^3,

T_l = G^2 + p[ G G1 - (3/2)Hcal(G^2)] + p^2 E.

At z0=1/2 the exact differential products satisfy
W(G^2)=G^2+6G G' and W(G G1)=G G1+3G' G1+3G G1'.
Put G(z0)=p alpha and divide by p. The displayed polynomial identity proves divisibility, hence division is legal. Keep every term through order p, including p alpha^2, p alpha G1 and 3p alpha G1'. This proves (1) for every prime in the declared CM-root family; finite computation is not used in the general proof.

The first-digit part of (1) agrees with the previous low-polynomial scalar observer. The new contribution is the complete p-correction with distinct quadratic carry, carry×harmonic coupling, first-harmonic derivative and second-harmonic jet. BRC: COMPOSE_APPLIED on a signed valuation/source-labeled observer. This does not prove a six-dimensional native-space result or a positive-mass statement.

## Executed independent direct source checks

The accompanying standard-library Python verifier independently sums the original *terminating* binomial coefficients modulo p^3, computes the full Gauss/harmonic port and checks (1) modulo p^2 for all 92 frozen-class primes p<=2400. No floats; actual marker PASS_D25_CLAUSEN_CM_SECOND_DIGIT_OBSERVER_EXACT.

Tuples (p, [WT_l](z0)/p modulo p^2, first-cluster mod p^2, p-correction cluster mod p, [WE](z0) mod p):
13:  (13,34,8,2,4)
19:  (19,289,213,4,17)
37:  (37,726,911,32,9)
157: (157,17661,24255,115,115)
373: (373,41612,11399,81,168).

At p=373, 11399+373*81=41612 exactly. This is the low-band weighted scalar, not full A_p. The earlier full-polynomial checker has separate 175-prime/65,973-coefficient coverage and is not relabeled an independent second-digit native experiment.

## Remaining original source obligations

This formula alone does NOT prove the open original 216 target sum A_p=p mod p^3. The actual four-port first-digit source bridge still requires S_t/p+H_A+U = 1 (mod p) uniformly on p mod24 in {13,19}. Then the original second digit requires (D0+D1)/p^2+I_p = 0 (mod p) after proved divisibility. Transferring (1) into the full A_p MUST retain the original source-labeled low-band harmonic deformations, once-crossed middle band, high signed strip and carry; none is replaced by the terminating scalar.

This is a new p^2 CM scalar consequence of the *denominator* Clausen jet, and does not recredit classical Clausen, the already known CM root, the previously proved full polynomial or Van Hamme E.2. Native H0/B0, [X]U mod p^2, semilinear Frobenius, normalization eta/kappa, native 373 experiment, independent review and Source admission remain separate.

Native service 0.6.11 status during this run: research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED. Actual Research-lane historical recovery/continuation (#6424/#6425) authorized=false. No new native session, CLAIM, OPEN, Source checkpoint, Result or review; protected staging and maintenance identity unchanged. Control repair issue Enterprise Math #1558, native experiment #1559. Scheduler unchanged.