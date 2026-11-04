# D25 — Sun quadratic square: full-source p² lift and first-moment derivative bridge

2026-11-04 (Asia/Hong_Kong). TASK_RESEARCH author-side portable result. **EXACT PUBLISHED-THEOREM COROLLARY / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** This mathematical artifact is not a native Source checkpoint or formal Result.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Research logical conversation: chatgpt-research-onhour-enterprise-math-20260923. Independent from maintenance chatgpt-hourly-enterprise-math-20260921.

## Entire original source

For all primes p>3, work in Z_(p) and retain full k=0,...,p-1 sums:
a_k=C(2k,k)^2 C(3k,k)/216^k; b_k=C(2k,k)^2 C(4k,2k)/2304^k.
A=Σa_k, B=Σb_k, M_A=Σka_k, M_B=Σkb_k, W=A+6M_A, V=B+8M_B.

Define F_a(X)=Σ_{k=0}^{p-1} binom(-1/3,k)binom(-2/3,k)X^k and
F_b(X)=Σ_{k=0}^{p-1} binom(-1/4,k)binom(-3/4,k)X^k.

In the quadratic étale algebra R_p=(Z/p²)[s]/(s²−2), let
x_a=(2+s)/4, x_b=(3+2s)/6.
Then x_a(1−x_a)=1/8 and x_b(1−x_b)=1/36; the factors 1−2x_a=−s/2 and 1−2x_b=−2s/3 are units.

## Result 1: quadratic-square lift

Zhi-Hong Sun's published 2015 Theorem 2.2 is the *polynomial congruence* (valid for every p-adic integer α and every odd prime p):

(Σ_{k=0}^{p-1} binom(α,k)binom(−1−α,k)X^k)^2
  ≡ Σ_{k=0}^{p-1} binom(2k,k)binom(α,k)binom(−1−α,k)[X(1−X)]^k (mod p²).

Apply α=−1/3,−1/4 and the exact factorial relations
binom(−1/3,k)binom(−2/3,k)=C(2k,k)C(3k,k)/27^k and
binom(−1/4,k)binom(−3/4,k)=C(2k,k)C(4k,2k)/64^k.
Consequently, for all p>3:

**A≡F_a(x_a)^2 (mod p²), B≡F_b(x_b)^2 (mod p²).**

Sun Theorem 2.3/Corollary 2.2 also implies *individually* for these two full original sources:
A≡0(mod p) => A≡0(mod p²);
B≡0(mod p) => B≡0(mod p²).

The previous D25 Hesse/CM author proof (unreviewed, not admitted) gives A≡0 modp for p≡13,19 mod24, thereby implying A≡0 modp² in those classes if that upstream proof is valid. For the B-family, p≡13,19 mod24 first-digit vanishing requires separate proof; it has been exactly checked in 23 target primes p≤500, but no universal B statement is claimed here.

## Result 2: *weighted* first moments from differentiated polynomial identity

Because Sun's identity is polynomial in X, differentiate formally, multiply by X(1−X)/(1−2X) and specialize at x_a,x_b. This yields for every prime p>3 (no zero premise):

**M_A ≡ −(s/4)F_a(x_a)F'_a(x_a) (mod p²).**

**M_B ≡ −(s/24)F_b(x_b)F'_b(x_b) (mod p²).**

Indeed 2 t_a/(1−2x_a)=−s/4 and 2 t_b/(1−2x_b)=−s/24. The formula is in R_p; M_A,M_B map to its scalar subalgebra. No truncation above p/2, no change to original coefficients, and no native X6/H0/B0 conclusion is inferred.

If both F_a(x_a) and F_b(x_b) vanish modp, their coefficientwise quotients U_a=F_a(x_a)/p modp and U_b=F_b(x_b)/p modp are well defined in F_p[s]/(s²−2). Then
M_A/p≡−(s/4)U_a F'_a(x_a);
M_B/p≡−(s/24)U_b F'_b(x_b) (mod p).

The full weighted difference W−V=A−B+6M_A−8M_B is therefore equivalent modulo p², under both period-zero hypotheses, to the explicit *signed* first-period derivative equation

**W−V≡0(mod p²) iff 2U_b F'_b(x_b)−9U_a F'_a(x_a)≡0(modp).**

This equivalence is a proved algebraic reduction. Universality of the derivative-pairing zero is still an open target-class question.

## Exact check / source observers

Executed locally with standard-library integer arithmetic and complete original C(2k,k)^2... terms, modulo p³, plus independently constructed period polynomials and formal derivatives in (Z/p²)[s]/(s²−2). All 23 target primes p≤500, p mod24 in {13,19}, passed 253 checks (0 failures): quadratic-square, both derivative moments, source p² vanishings, period modp zeros, signed 2:9 pairing, finite W−V modp³, and first-moment unit digits. This is finite evidence, not a general W−V modp³ proof.

p | A/p² modp | B/p² modp | D=(A−B)/p² modp | (M_A/p,M_B/p) modp | 9U_aF'_a=2U_bF'_b modp
---|---:|---:|---:|---|---
13 | 11 | 4 | 7 | (11,5) | 10s
19 | 8 | 7 | 1 | (16,12) | 16s
373 | 71 | 203 | 241 | (311,140) | 370s

In these 23 samples, 6M_A/p≡8M_B/p≡1 modp; this stronger pattern is an *observed candidate*, not a theorem. Retain full-source integer/valuation, observer/period/Frobenius context, and signed interaction information. BRC/native reinterpretation has not been established; these are classical auxiliary algebraic observers, not native experiment replacements.

## Next exact unit and recovery

Construct modulo p³ the exact p² correction to Sun's **truncated** square identity and its differentiated derivative, preserving contributions of all high valuation bands. At p=13,19,373 compare A/p², B/p², D=(A−B)/p² and first-moment units before searching WZ/Green finite certificates; separately derive B first-digit zero and the 2:9 period pairing via an independent elliptic/isogeny transformation. Mother goal remains Δ_p−R_p≡0(modp) in target classes, via original W−V≡0(modp³), pending proof.

Native p=373 [X]U mod139129, module rank, actual semilinear Frobenius and independent replay remain due under awdawmip/enterprise-math#1559; not executed here.

Native service read at 2026-11-04 18h Asia/Hong_Kong: em_status 0.6.11, research_authority_granted=false, source control CODE_UPGRADE_AVAILABLE, reviewed_code_gate_passed=true, full_snapshot_verified=false. Exact old request onhour-d25-20261104-1702-continuation-read returned FAILED / SOURCE_TREE_SIZE_LIMIT 20001/20000; do not resubmit. Old research-onhour-20261031-0205-dispatch-r15 returned FAILED / UPSTREAM_CODE_REVIEW_REQUIRED; do not replay. No authenticated new research session/claim/open/run/native checkpoint/Result, no use of maintenance identity, three old staging sources separate. Author-side durable GitHub work only, UNREVIEWED / NOT_ADMITTED.

Published primary theorem: Zhi-Hong Sun, *Note on super congruences modulo p²* (2015-03-11), Theorems 2.2–2.3 and Corollary 2.2, https://arxiv.org/html/1503.03418v1. Prior author-side CM bridge: research_notes/portable_direct/20261104_onhour_d25_hesse_cm_inert_first_digit_proof.md.
