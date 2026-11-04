# D25 author-side result: exact Frobenius–Euler degree descent for the 2304 Gauss port

Date: 2026-11-04. Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific input pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Logical lane claimed by scheduled prompt: chatgpt-research-hourly-enterprise-math-20260923; maintenance lane is distinct. This report is **AUTHOR-DERIVED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**, not a native result, independent review or execution CLAIM.

## Exact theorem over F_p

For every prime p = 8q+5 >= 5, put

\[
L=5q+3,\quad t=2q+1=(p-1)/4,\quad N=(p+1)/2,\quad g(z)=1-z/9.
\]
Define, in the prime field (all displayed coefficients have p-unit denominators),
\[
v_k=\frac{(1/8)_k(3/8)_k}{(k!)^2\,9^k},\quad
c_j=\frac{(5/8)_j(7/8)_j}{(j!)^2\,9^j},\quad
b_k=\frac{(4k)!}{(k!)^4\,2304^k},
\]
and the finite polynomials
\[
P(z)=\sum_{k=0}^{L}v_kz^k,\quad C(z)=\sum_{j=0}^{q}c_jz^j,\quad
B(z)=\sum_{k=0}^{t}b_kz^k.
\]

**Theorem (Frobenius–Euler/Clausen descent).** The following are polynomial identities in F_p[z]:
\[
\boxed{P(z)=g(z)^N C(z)},\qquad
\boxed{B(z)=g(z)C(z)^2},\qquad
\boxed{P(z)^2=B(z)(1-z^p/9).}
\]
In particular, the scalar \(\lambda_p=v_L^2/b_t\) from the previous two-block Frobenius carry **is explicitly \(-9^{-1}\pmod p\)** for every prime in this class. The new lower kernel has degree q, rather than L for P or t for B, and its coefficients are the reflected hypergeometric pair 5/8,7/8.

### Proof

The original Gauss hypergeometric power series has parameters a=1/8, b=3/8 and argument x=z/9. Classical Euler's transformation (an existing identity, not claimed as a new theorem) reads
\[
{}_2F_1(1/8,3/8;1;x)=(1-x)^{1/2}{}_2F_1(7/8,5/8;1;x).
\]
Since p=8q+5, the coefficient v_{L+1} has the factor 8L+1=5p and subsequent coefficients through index p-1 vanish modulo p. Likewise c_{q+1} has the factor 8q+5=p, and all later coefficients through index p-1 vanish modulo p. As N=(p+1)/2 is congruent to 1/2 modulo p, the first L+1 binomial coefficients of \((1-x)^{1/2}\) equal those of \((1-x)^N\) modulo p: all factorial denominators are p-units because L<p. The right side therefore has polynomial representative \(g^N C\) of degree N+q=L; its coefficient sequence through degree L agrees with the left side. This proves the first identity, including q=0 (p=5).

The classical Clausen identity gives, over Q, the full formal power-series coefficient identity
\[
\big({}_2F_1(1/8,3/8;1;z/9)\big)^2
=\sum_{k\ge0}b_kz^k.
\]
For every k<=t<p, truncation at L leaves this coefficient unchanged. The first identity gives
\[
P^2=g^{p+1}C^2=(1-z^p/9)\,gC^2\quad\text{in F_p[z]}
\]
by Frobenius. The polynomial \(gC^2\) has degree \(2q+1=t\). Comparing coefficients of degrees 0 through t with the preceding Clausen identity proves \(B=gC^2\), hence the third identity. Since \(2L=p+t\), its leading coefficient comparison is \(v_L^2=(-1/9)b_t\), and \(v_L,b_t\neq0\) modulo p. Thus \(\lambda_p=-1/9\) as stated.

This is a new *task-specific finite-field specialization and degree-reduction interface* obtained by combining existing Euler and Clausen transformations with the exact p-dependent truncation. It makes no novelty claim for the classical identities themselves.

## Signed/derivative observers and a shorter zero-selection problem

Let \(F_p(z)=\sum_{k=0}^{p-1}v_kz^k\). Modulo p it equals P. Write \(S=F_p(1)\), \(D=(z\,d/dz)F_p(1)\), \(Y=S+16D\). Because \(g(1)=8/9\) and \(2N=p+1\),
\[
\boxed{S=g(1)^N C(1)},\qquad
\boxed{Y=16g(1)^N C'(1)}\quad (\bmod p).
\]
The derivative observer therefore **loses its C(1) term exactly at z=1**; it isolates the derivative of a degree-q polynomial.

Likewise the original 2304 weighted sum satisfies
\[
V_p=\sum_{k=0}^{p-1}(8k+1)b_k
\equiv B(1)+8B'(1)=16(8/9) C(1)C'(1)\pmod p.
\]
The known Guo–Zudilin 2304 supercongruence gives \(V_p\equiv0\pmod p\), so \(C(1)C'(1)=0\) in F_p. The factors cannot vanish simultaneously: \(P=g^NC\) would then have a double zero at z=1, an ordinary point of its Gauss differential equation \(576\theta^2P-z(8\theta+1)(8\theta+3)P=0\). Coefficient uniqueness at an ordinary point for a degree < p polynomial (all Taylor n! denominators invertible) would force P identically zero, contrary to P(0)=1. Exactly one of C(1), C'(1) vanishes modulo p.

Finite tests identify C(1)=0 for p mod24=13, and C'(1)=0 for p mod24=5 within the tested interval. That **class selector**, and its second-digit lift, remain separate open proof obligations.

## Exact integer certificate and BRC use

The accompanying standard-library Python checker constructs v, c, b from three distinct modular recurrences; tests the full polynomial identities, \(\lambda=-1/9\), both observer identities, and exclusive zero over every prime p=5 mod8 up to 2000. For p in {5,13,29,37,373} it additionally reconstructs b_k from the original binomial coefficient product.

Executed result: **PASS 79 primes; 45,651 P coefficients; 18,292 B coefficients; 79 observer checks.** Witnesses:
- p=5: (q,lambda,C(1),C'(1))=(0,1,1,0).
- p=13: (1,10,0,12).
- p=29: (3,16,7,0).
- p=37: (4,4,0,30).
- p=53: (6,47,27,0).
- p=61: (7,27,0,3).
- p=373: (46,290,0,41).

BRC composition applied: carrier retains the original k-indexed 2304/Gauss coefficients, truncation bounds, signed derivative observation, prime residue, Frobenius multiplication and the reduced C polynomial. The map from (C,C') to (S,Y) is explicit and invertible modulo p at z=1. This reduction is certified only at the first p-adic digit; it does not discard the p-adic correction required at modulus p^2.

## Next exact action and preserved Source frontier

Lift the polynomial identity \(P=g^NC\) from mod p to mod p^2 by deriving the explicit discrepancy \(E_p(z)=(F_p(z)-g^NC(z))/p\bmod p\), retaining the middle Gauss carry separately. Establish how E_p(1) and E'_p(1) govern the selected C(1) or C'(1) second digit for the two mod24 classes. Compare this short-kernel route with the previously recorded Jacobi harmonic and boundary-injection terms; do not re-prove the older Gauss/Green/Clausen results.

The actual current native Source continuation receipt rhourly20-20261104-1923-cont-read is SUCCEEDED (observed 2026-11-04), Source pin 3645861db6452777b473a94c7938cc903a962a89, persisted native checkpoint SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED, route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION, execution_authorized=false. Its old session MCP-d6dd85529e9e45a9b5f808c1025f5918 and its protected data were not touched. Durable native unfinished question remains authenticated original-class H0/B0 divided-power module, [X]U mod p^2, rank/semilinear direction/normalization eta, native p373 test and D24 Delta_p-R_p bridge. This portable author-side paper does not modify or replace that Source frontier. No native CLAIM/open, native result, formal review or task admission is claimed.
