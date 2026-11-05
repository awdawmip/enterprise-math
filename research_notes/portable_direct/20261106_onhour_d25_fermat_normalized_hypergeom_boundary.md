# D25 SECOND-DIGIT-LIFT — single Fermat quotient and inhomogeneous finite hypergeometric boundary

**2026-11-06; TASK_RESEARCH; AUTHOR-SIDE EXACT PROOF + 166 PRIME BIG-INTEGER CHECK; UNREVIEWED / NOT_ADMITTED.**

Source task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; unchanged scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Logical research lane: chatgpt-research-onhour-enterprise-math-20260923 (independent of maintenance lane).

Consumes the already verified author-side shortened signed certificate and reflected two-digit tail:
- research_notes/portable_direct/20261106_onhour_d25_shortened_signed_certificate.md
- research_notes/portable_direct/20261106_onhour_d25_reflected_tail_second_digit_certificate.md

## Theorem 1. Wilson/half-factorial contributions cancel into one Fermat quotient

For every prime p>3, set h=(p-1)/2, define q_p(a)=(a^(p-1)-1)/p mod p. The reflected-tail parameter from the previous proof was

\[
\beta_p=2\mathcal W_p-2+\mathcal H_{4,p}+q_p(48)\pmod p,
\quad
\mathcal W_p=((p-1)!+1)/p,\quad
\mathcal H_{4,p}=((h!)^4-1)/p.
\]

Then

\[
\boxed{\beta_p\equiv q_p(3)-2\pmod p},
\qquad
\boxed{\frac{b_h}{p}\equiv-(1+2p)3^{1-p}\pmod {p^2}},
\quad b_k=\frac{(4k)!}{2304^k(k!)^4}.
\]

**Proof.** Put H_h=sum_{i=1}^h 1/i mod p. The exact identity (h!)^4=((p-1)!)^2/binom(p-1,h)^2 and binom(p-1,h)=(-1)^h product_{i=1}^h(1-p/i) give \(\mathcal H_{4,p}\equiv2(H_h-\mathcal W_p)\pmod p\). In 2^p-2=sum_{i=1}^{p-1} binom(p,i), use binom(p,i)=p(-1)^(i-1)/i mod p²; the alternating harmonic sum is -H_h mod p, hence H_h=-2q_p(2) mod p. Multiplicativity of Fermat quotients yields q_p(48)=q_p(3)+4q_p(2) mod p. Substitution proves the first box. The previous proved top-shell identity b_h/p=-1+p beta_p mod p² and 3^(p-1)=1+p q_p(3) mod p² prove the second. Both statements are unconditional for primes p>3.

## Theorem 2. Exact terminating p-deformed hypergeometric carrier

Let L=floor((2p-1)/3), K0=floor(2L/3), K=K0-1 if 2L-3K0=1, otherwise K=K0; J=h-K-1. The original signed compensator is

\[
V_{\mathrm{tail}}=\sum_{k=K+1}^{h}(8k+1)b_k.
\]

For 0<=j<=J, put

\[
Q_{p,j}=
9^j\frac{(-h)_j^3}{(3/4-p/2)_j(1-p/2)_j(5/4-p/2)_j},
\quad Q_{p,0}=1.
\]

All denominators are p-units on this range. The exact backward coefficient ratio gives

\[
\frac{b_{h-j}}p=\frac{b_h}p\,Q_{p,j},
\quad
\frac{Q_{p,j+1}}{Q_{p,j}}=
9\frac{(j-h)^3}{(j+3/4-p/2)(j+1-p/2)(j+5/4-p/2)}.
\]

With \(H_{p,J}(z)=\sum_{j=0}^J Q_{p,j}z^j\) and \(\theta=z\,d/dz\), use 8(h-j)+1=4p-(8j+3) and Theorem 1:

\[
\boxed{
\frac{V_{\mathrm{tail}}}{p}\equiv
-(1+2p)3^{1-p}\{(4p-3)H_{p,J}(1)-8\theta H_{p,J}(1)\}
\pmod {p^2}.
}
\]

If J=-1 the polynomial and compensator are zero. This combines both p-adic digits of the boundary, including the signed derivative, without explicit Wilson or factorial quotients.

## Theorem 3. Exact inhomogeneous differential endpoint

Define the fourth-order operator

\[
\mathcal L_p =
\theta(\theta-\tfrac14-\tfrac p2)(\theta-\tfrac p2)
(\theta+\tfrac14-\tfrac p2)
-9z(\theta-h)^3(\theta+1).
\]

For 0<=J<h, the following is an exact rational identity:

\[
\boxed{
\mathcal L_p H_{p,J}(z)
=-9(J+1)(J-h)^3Q_{p,J} z^{J+1}.
}
\]

Proof: the coefficient of z^n cancels for 1<=n<=J by the exact displayed ratio; the constant vanishes by theta. Since H has no z^(J+1) term, its last coefficient comes solely from -9z(theta-h)^3(theta+1) acting on Q_J z^J. The inhomogeneous term retains the true finite endpoint and sign.

The frozen LIFT mother proof, after the previously established signed shortened identity, now has an explicit adjoint-matching obligation on its **own** C_p carrier:

\[
\frac{C_p}{p}\equiv
-(1+2p)3^{1-p}\{(4p-3)H_{p,J}(1)-8\theta H_{p,J}(1)\}
\pmod{p^2},\qquad p\equiv13,19\pmod{24}.
\]

This matching is OPEN; the mathematical theorem proved here is the exact tail boundary and differential equation, not the full all-prime equality. The inhomogeneous endpoint supplies a testable obstruction/boundary for a future telescoper.

## Executed checks and BRC provenance

Executed exact arbitrary-precision Python modular arithmetic on all 166 primes 5<=p<=997 with zero failed assertions. Direct original factorial shells were compared independently to (i) the old and new beta, (ii) top-unit normalization, (iii) every p-deformed hypergeometric term, (iv) the old S0+p S1 and the new signed whole-tail formula, and (v) the coefficients of the inhomogeneous operator modulo p². Representative tuple (p, q_p(3), beta, V_tail/p mod p², operator endpoint mod p²):
- (13,8,6,89,48)
- (19,18,16,98,63)
- (67,15,13,835,392)
- (139,45,43,5411,14119)
- (373,301,299,120175,59367)
- (997,296,294,229520,33426).

Code: research_notes/portable_direct/d25_fermat_normalized_hypergeom_tail_check_20261106.py.

**BRC reuse:** COMPOSE_APPLIED from original 2304 signed reflection and two-digit deformation; retained observer is (original model, p, k=h-j, j, valuation=1, Fermat quotient, signed 8k+1, theta port, endpoint J), precision p² after original tail division by p. The resulting hypergeometric polynomial is a compact **computational carrier**, not a source-native H0/B0 model.

**Frontier:** The original-class p=373 H0/B0 divided-power [X]U mod 139129, module rank, native Frobenius/eta/kappa and independent replication are still NOT_RUN/PENDING_OWNER (support Issue #1559). This author-side proof requires independent review/admission. No CLAIM, run, Source checkpoint or frozen Result is asserted. Next: construct and test the dual/adjoint of the existing signed shortened C_p carrier against the inhomogeneous endpoint; separately execute the original native benchmark through its authorized Source owner.
