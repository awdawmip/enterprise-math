# D25 onhour — mirrored p≡7(mod8) Jacobi/Frobenius carry, new exact odd-sector diagnostic

2026-11-01 10:00 Asia/Hong_Kong. **TASK_RESEARCH / AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN.**

Mother RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3**, unchanged. Logical Research lane **chatgpt-research-onhour-enterprise-math-20260923**, separate from maintenance. Original objective: A_p ≡ p (mod p³) for p≡13,19 (mod24), or frozen Δ_p−R_p=0 (mod p). The p13 identity in 20261101_onhour_d25_p13_exact_frobenius_carry_coefficient.md is a consumed input, not a new claim.

## New mirrored theorem and complete arithmetic proof

For every prime p≡7(mod8), p≥7, define

\[
a=(7p-1)/8,\qquad b=(5p-3)/8,\qquad 0<b<a<p,\qquad \lambda=1/9.
\]

Let the **original** finite Gauss factor be
\[
G_{\beta,p}=\sum_{k=0}^{p-1}\frac{(1/8)_k(3/8)_k}{(k!)^2}\lambda^k.
\]
Use the terminating binomial polynomial
\[
K_n(x)=\sum_{k=0}^{n}\binom nk\binom xk\lambda^k,\quad
J=K_b(a)=K_a(b).
\]
Then the **all-prime p≡7(mod8) congruence** is
\[
\boxed{8G_{\beta,p}\equiv20J-7K_b(a+p)-5K_a(b+p)\pmod{p^2}.}\tag{1}
\]

Proof: work in the p-local ring, with p-unit denominators k! for k<p. The finite bivariate polynomial
\[
S(X,Y)=\sum_{k=0}^{p-1}\frac{(X)_k(Y)_k}{(k!)^2}\lambda^k
\]
has the exact terminating values
\[
S(-a,-b)=J,\quad S(-a-p,-b)=K_b(a+p),\quad S(-a,-b-p)=K_a(b+p).
\]
Because 1/8=−a+7p/8 and 3/8=−b+5p/8, first-order Taylor expansion modulo p² gives
\[
G_{\beta,p}\equiv J+\frac{7p}{8}S_X(-a,-b)+\frac{5p}{8}S_Y(-a,-b).
\]
The other two evaluations respectively equal J−pS_X and J−pS_Y modulo p². Eliminating both derivatives gives (1). This proof covers parameter zeros because it differentiates polynomial Pochhammer factors, never divides by a vanishing (−a+j) or (−b+j).

Define one common source polynomial and **separate indexed sources**:
\[
P(t)=(1+t)^a(t+\lambda)^b,\quad J=[t^b]P(t),
\]
\[
E_1(t)=\frac{(1+t)^p-1-t^p}{p},\quad
E_\lambda(t)=\frac{(t+\lambda)^p-t^p-\lambda^p}{p},
\]
\[
C_1=[t^b]PE_1,\qquad C_\lambda=[t^{b+p}]PE_\lambda.
\]
Here E_1 and E_λ have coefficients in Z_(p); divide binomial coefficients by p **before** reduction. Binomial coefficient extraction gives the exact, not just modular, identities
\[
K_b(a+p)=J+pC_1,\qquad K_a(b+p)=J+pC_\lambda.
\]
Indeed [t^b]P(t)t^p=0 because b<p; [t^{b+p}]P(t)\lambda^p=0 because deg P=a+b<b+p. Hence (1) becomes
\[
\boxed{8G_{\beta,p}\equiv8J-p(7C_1+5C_\lambda)\pmod{p^2}.}\tag{2}
\]

**Comparison with the previously proved p≡5(mod8) port:** there the exact corresponding weights are 5C_1+7C_λ, with a=(5p−1)/8<b=(7p−3)/8. The odd-Legendre p≡5,7 sector therefore has two different, sourced first-carry weightings; the terminal value alone is not a safe port identification for derivatives, signed cutoffs or original native observers.

For the p≡23(mod24) branch, the previously author-proved CM(-24) mod-p selector gives J≡G≡0 (mod p). Conditional only on that already established mod-p result, (2) yields a **proved equivalence**:
\[
G_{\beta,p}\equiv0\pmod{p^2}
\iff
8(J/p)\equiv7C_1+5C_\lambda\pmod p.\tag{3}
\]
The infinite-prime right-side cancellation is **UNPROVED**. The matching p13 condition, 8(J/p)≡5C_1+7C_λ, is also still unproved. The p23 companion is a new discriminating test for a CM/character argument intended to establish p13; it does not substitute for the p13 proof.

## Executed exact independent certificate

Program: research_notes/portable_direct/d25_p7_mirror_frobenius_20261101.py. Executed using Python standard-library integer/binomial operations. All **109 primes p≤3000, p≡7(mod8)** passed (1) and (2). At fixed **7,23,31,47,71,167,191,239**, an independent binomial convolution and exact integer divided-Frobenius extraction reproduced both ports (8 passes). Among the 109, **55 p≡23(mod24)** all gave G≡0(modp²), while **54 p≡7(mod24)** yielded p-units; these are finite observations, not a proof of their infinite-prime classification.

Exact independent rows in Z/p²Z (C_1,C_λ mod p):
- p=23: J=368=16p; C_1=6, C_λ=8, G=0. 8·16−7·6−5·8=46≡0(mod23).
- p=47: J=1269=27p; C_1=22, C_λ=3, G=0. 8·27−7·22−5·3=47≡0(mod47).
- p=71: J=4118=58p; C_1=43, C_λ=61, G=0. 8·58−7·43−5·61=−142≡0(mod71).
- Negative control p=7: J=32, G=39 (mod49), both nonzero mod7; J/p is not defined p-locally in this control.

BRC **COMPOSE_APPLIED**: two distinguishable signed p-adic coefficient/shift ports, integer p-adic valuation, original β recurrence, terminal observation modulo p². Ordinary polynomial Frobenius is *not* the H0/B0 native semilinear Frobenius or the six-axis X6 operation. No theorem/working-truth/P000 promotion.

## Honest recovery frontier

Preserve mother objective and frozen Source pin. Consume completed D24 UR, prior p13 Jacobi two-shift, p19 CM-Hensel and earlier signed boundary work without replay. Next **target-critical** unit: prove/refute the p13 8(J/p)=5C_1+7C_λ relation by a CM-compatible two-port symmetry, using p23 7C_1+5C_λ as an independent falsification/control before combining original 216 R_p. Neither parity branch establishes original A216 LIFT.

Native benchmark https://github.com/awdawmip/enterprise-math/issues/1559 remains original fixed p=373 H0/B0 divided-power [X]U mod139129, rank, real semilinear Frobenius direction/eta, odd signed Hesse/Green, κ, independent reproduction: **NOT_RUN / PENDING_OWNER**; acceptance demands actual original-class versioned code, raw outputs, signed observer and independent check. The current gateway v0.6.11's Sites subject reports research_authority_granted=false and executor_binding_configured=false; source Control CODE_REVIEW_REQUIRED and quota 5/5. Research lane has **no verified active Source session/claim/run** in this read; old request research-onhour-20261031-0205-dispatch-r15 remains subject to exact-scope reconciliation, not mutation replay. No Source checkpoint/Result/acceptance is claimed; prior three staging sources remain independent. P000/ACTIVE worldview and existing scheduled task settings unchanged.
