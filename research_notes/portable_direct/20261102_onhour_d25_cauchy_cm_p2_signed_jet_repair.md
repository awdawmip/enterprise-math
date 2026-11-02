# D25 — Exact second-digit repair for the 2026 Cauchy / original W216 signed CM first-jet bridge
**2026-11-02; AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF / FINITE INTEGER REPLAY / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** This continues the immutable author-side theorem at commit 84d5205d874d4cab4000585146a4770ccd96d882, retaining accepted D24 CM0 and original frozen input c47e13e4aba0e006366f989d6334d443f6333ae3. Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7.

## Objects and all-target theorem
Let p=6m+1, p≡13 or 19 (mod24), z0=1/2, theta=z*d/dz, and let F_p(z), C_p(z), E_p(z), ell_m(z) be **exactly the original finite polynomials defined in the preceding note**: original 216 hypergeometric F_p, Roman Le Lan's differently sourced outer Cauchy product C_p, the truncated binomial factor E_p, and the accepted terminating Gauss ell_m. In the p-local rational polynomial ring, define coefficientwise quotient polynomials modulo p:
\[
R_A(z)=\frac{F_p(z)-\ell_m(z)^2}{p}\bmod p,\quad
R_E(z)=\frac{E_p(z)-(1-z)^{3m}}p\bmod p.
\]
They exist because the differences vanish coefficientwise modulo p. Set
\[
\boxed{R_C(z)=[(1-z)^{3m}R_A(z)+R_E(z)\ell_m(z)^2]_{<p}\pmod p.}\tag{1}
\]
The cutoff <p is on the **total source index**, preserving both ordered Cauchy indices. The exact rational convolution and multiplication to second order imply
\[
C_p(z)\equiv (1-z)^{3m}\ell_m(z)^2+pR_C(z)\pmod {p^2}
\]
coefficientwise as polynomials. An untruncated product on the right generally has degrees >=p and is **not** interchangeable under later evaluation at z0, a p-adic unit.

Consume accepted CM0 ell_m(z0)≡0 (modp). Define three **typed p-adic repair coordinates**
\[
g=\frac{\ell_m(z_0)}p\bmod p,\qquad
j=(\theta\ell_m)(z_0)\bmod p,\qquad
\delta=\frac{1+2^{-3m}}p\bmod p.
\]
The latter is p-integral because Euler's criterion gives 2^{-3m}≡(2/p)=-1 (modp) in both target classes. Define the weighted original and Cauchy readouts
\[
W_p(z)=(1+6\theta)F_p(z),\qquad L_p(z)=(3\theta-1)C_p(z).
\]
The first-jet theorem gives D_p=2(\theta L_p)(z0)+(\theta W_p)(z0)≡0 (modp). **The new all-target second-digit theorem is**
\[
\boxed{
\frac{D_p}{p}\equiv
-6gj+12\delta j^2+
\left[2\theta(3\theta-1)R_C+\theta(1+6\theta)R_A\right]_{z=z_0}
\pmod p.}\tag{2}
\]
This proves a complete repair **for the declared first-jet observer modulo p²**. It does not assert p³ equality of the two original weighted values or completion of the D25 LIFT.

## Exact proof, including the p-adic boundary
Let P(z)=ell_m(z)^2 and e(z)=(1-z)^{3m}. Substitution of the exact coefficientwise decompositions yields
\[
D_p =
[6\theta^2(eP)-2\theta(eP)+\theta P+6\theta^2P]_{z_0}
+p[2\theta(3\theta-1)R_C+\theta(1+6\theta)R_A]_{z_0}
\pmod {p^2}.
\]
By the Leibniz rule, the first square bracket equals
\[
[ (6\theta^2e-2\theta e)P+
(12\theta e-2e+1)\theta P+
6(e+1)\theta^2P]_{z_0}.
\]
Since ell_m(z0)=p g (mod p²), P(z0) is divisible by p² and
theta P(z0)=2p g j (mod p²), theta² P(z0)=2j² (modp).
At z0, e≡-1 and \theta e/e=-3m z/(1-z)=-3m≡1/2 (modp);
therefore \theta e≡-1/2 (modp) and
12\theta e-2e+1≡-3 (modp). Also e+1=p delta (mod p²).
Thus, after dividing the first square bracket by p, its residue is
-3*(2gj)+6*delta*(2j²)=-6gj+12delta j².
The exact <p convolution expansion supplies the R_C term, proving (2).
All rational denominators in source coefficients have p-unit denominators for k<p and p>3. The proof is polynomial algebra, not finite numerical interpolation.

## Exact computed certificate and diagnostic
The accompanying independently executed Python standard-library checker reconstructs the original W216 recurrence, Le Lan A*B outer Cauchy product, a distinct E*F convolution, the full coefficientwise mod-p polynomial identity and the complete mod-p² R_A,R_E,R_C. It checked 53 primes (45 target primes <=1000, plus another target 1171 and 7 non-CM controls), 22,507 source positions and all signed-jet identities, all PASS. The script checks (2) against the **direct original signed weighted sums** modulo p² without using (2) to construct that direct sum.

| p | g | j | delta | -6gj+12delta j² | source/truncation correction | D_p/p mod p |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 7 | 7 | 8 | 3 | 6 | 9 |
| 19 | 6 | 1 | 11 | 1 | 11 | 12 |
| 373 | 340 | 294 | 102 | 341 | 221 | **189** |
| 1171 | 1082 | 544 | 149 | 912 | 847 | 588 |

At p=373, original theta W=292 and Cauchy theta L=227 (mod373) give the first-jet zero 2*227+292=746. The next digit is **189**, and its complete provenance is 341+221=562≡189 (mod373). Consequently, replacing (2) by the uncorrected stronger assertion D_p=0 mod p² fails already at p=13,19,373. This is a precisely scoped method counterexample, not a negative result for the original D25 target.

## Source, BRC observer, remaining mother objective
The external Cauchy identity belongs to Roman Le Lan, *Series for 1/pi arising from Cauchy product*, arXiv:2604.03327v2, Lemma 1 / Eq. (3.2), https://arxiv.org/pdf/2604.03327. This note's new result is the exact finite CM p² repair (1)-(2) under accepted D24 CM0, with independent original integer replay; novelty versus all external literature remains unreviewed. The 2026 paper's Sun congruence is called **Conjecture 1** and is not promoted to theorem.

Original mother goal remains Delta_p-R_p=0 (modp) for all p≡13,19 (mod24), equivalently W_p(1/2)=p (modp³) under accepted D24 sources. This result supplies a finite, source-preserving Cauchy auxiliary coordinate and explicit next-digit repair. Next scientific priority is a genuinely matched original weighted W216 WZ / finite 216-to-2304 transport at modulus p³, consuming (2) only if its operator actually preserves the signed original value, rather than extending auxiliary jet towers for their own sake.

Original native fixed-p373 H0/B0 divided-power [X]U mod139129, module rank, actual semilinear Frobenius/eta, signed odd Green/Hesse/kappa and independent replay remain NOT_EXECUTED, PENDING_OWNER under existing #1559. No Cauchy scalar proxy substitutes for native evidence. Source Site gateway 0.6.11 read-only status at 2026-11-02T13:22Z: research_authority_granted=false, write_relay_enabled=false. No current own native session/CLAIM/run/checkpoint/Result is attested; no blocked mutation replay or maintenance-lane identity used. Original scheduler/notifications unchanged.
