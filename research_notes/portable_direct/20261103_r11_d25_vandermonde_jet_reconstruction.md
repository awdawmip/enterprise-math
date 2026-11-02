# D25 V1/V2 | Terminating Vandermonde jet and second endpoint derivative

2026-11-03 +08:00. AUTHOR-DERIVED / HAND-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. TASK_RESEARCH logical lane chatgpt-research-hourly-enterprise-math-20260923, not maintenance. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Native H0/B0=NOT_EXECUTED.

## Source and exact definitions

For each prime p=6r+1>=7 put u=3r=(p-1)/2 and work in F_p. Define ell(z)=sum_{j=0}^r binom(r,j) binom(2r,j) z^j, B=binom(3r,r), A(z)=ell(z)^2. Define original hypergeometric source a_n=(1/2)_n(1/3)_n(2/3)_n/(n!)^3 and S(z)=sum_{n=0}^{2r} (9n+4)a_n z^n/36. Reuse the previously proved finite Clausen A(z)=sum a_n z^n (mod p), so 36S=4A+9zA'. The preceding new author-side reflected-Wronskian theorem is at Enterprise Math commit 6c70c75bc9c846c3f4d81917acdbd420e9c5a570: put d_k=[x^k]S(1-x)=(-1)^k S^(k)(1)/k!, then Omega(z)=(1-z)^u/6+sum_{k=0}^{2r}d_k(1-z)^k/(u-k). This is used as an inherited exact source interface.

## V1: explicit finite Vandermonde factorial-moment convolution (PROVED)

For 0<=m<=r set rho_m=r_falling(m)*(2r)_falling(m)/(3r)_falling(m), and rho_m=0 for m>r. For 0<=k<=2r+1 let M_k=sum_{i=max(0,k-r)}^{min(k,r)} binom(k,i)*rho_i*rho_{k-i}. Then for every 0<=k<=2r,

d_k = (-1)^k * B^2 * [(4+9k) M_k + 9 M_{k+1}] / (36 k!)  (mod p).   (V1)

All denominators are p-units, since 3r<p and k<=2r<p. M_{2r+1}=0.

PROOF: Since j_falling(m)*binom(r,j)=r_falling(m)*binom(r-m,j-m), Vandermonde gives
ell^(m)(1)=r_falling(m)*sum_{j=m}^r binom(r-m,j-m)*binom(2r,j)
=r_falling(m)*binom(3r-m,r)=B*rho_m.
For m>r the derivative vanishes. Leibniz yields A^(k)(1)=B^2 M_k. Differentiating 36S(z)=4A(z)+9zA'(z) k times gives 36S^(k)(1)=(4+9k)A^(k)(1)+9A^(k+1)(1). Multiply by (-1)^k/k! to obtain V1. QED.

A complete explicit finite reciprocal-moment interface follows:

J_p = (B^2/36) * sum_{k=0}^{2r} (-1)^k 2^(-k) [(4+9k)M_k+9M_{k+1}] / [k!(3r-k)]  (mod p).   (V1a)

This is the same J_p defined in the preceding reflected-Wronskian note, not a new fitted observable. On target p mod24 in {13,19}, the earlier open second-carry condition is exactly J_p-g*j ?= 1/12 mod p. Here g=ell(1/2)/p mod p computed at integer/mod-p^2 precision, and j=(z ell'(z))|_(1/2) mod p.

## V2: closed endpoint first derivative (PROVED)

For every prime p=6r+1>=7,

Omega'(1) = (8/729) * binom(3r,r)^2  (mod p).   (V2)

PROOF: Set rho_1=2r/3=-1/9 mod p and rho_2=28/243 mod p from p=6r+1. Thus A'(1)/B^2=M_1=2rho_1=-2/9; A''(1)/B^2=M_2=2rho_2+2rho_1^2=62/243. Differentiating the source expression gives 36S'(1)=13 A'(1)+9A''(1), whence S'(1)/B^2=-4/243. Differentiating the inherited finite Wronskian equation (1-z)Omega'(z)+u Omega(z)=S(z), and evaluating z=1, gives (u-1)Omega'(1)=S'(1). Since u-1=-3/2 mod p, the asserted value follows. QED.

Together with the prior Omega(1)=-B^2/9, the full endpoint first jet is B^2*(-1/9,8/729). B is a nonzero p-unit; the derivative never vanishes on this prime domain.

## Exact verification, provenance and next action

The attached independent pure-integer script d25_vandermonde_jet_20261103.py computes original a_n and s_n, builds the binomial-reversed d_k via Horner substitution, reconstructs the full d_k sequence using rho/M and checks *every* coefficient and V2 on all 148 primes 7<=p<=2000 with p mod6=1. PASS 148/148 on V1 and V2. For p=373: r=62, B=38, J=338, Omega'(1)=242. This is bounded exact verification in addition to the general proofs, not a native p373 H0/B0 experiment or the universal OPEN second-carry proof.

BRC: COMPOSE_APPLIED to original signed source indices n/j, reversible binomial carrier d, finite joint factorial-moment convolution rho/M, independent endpoint and midpoint observers, plus a separately typed integer-lift g. Every quotient is scoped to the displayed finite-field observation; preserve the nonzero Frobenius top port from the prior source.

NEXT: construct a terminating WZ/contiguous certificate or genuine counterexample to J_p-g*j=1/12 for p mod24 in {13,19}; compare the factorial-moment double sum with the CM integer root lift. Carry the result through the existing p-adic precision tower toward the frozen mother Delta_p-R_p=0 mod p. The native Source execution remains gated at Gateway 0.6.11 (UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active quota 5/5); existing #1558 and original p373 H0/B0 #1559 handle their own owner scopes. No new native CLAIM, OPEN, Source checkpoint, Result or independent review is represented by these author files.
