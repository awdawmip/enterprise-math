# D25 — Prime-square digit palindrome and infinite-progression transport

Date: 2026-11-06. Status: AUTHOR-PROVED / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / ORDINARY INTEGER MODEL ONLY.

This follows the just-published D25 two-digit signed Lucas/carry theorem at \`research_notes/portable_direct/20261106_hourly20_d25_lucas_q2_two_moments.md\`. Same D25 Task/publication \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\` / \`TP2-B6F4FC938FF94941C1B7\`, frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. The native H0/B0 and LIFT second digit remain unexecuted/unsettled.

## Theorem: an exact q-adic propagation law

Let q>=5 be a prime, \(n_0=(q^2-1)/6\), \(n_t=n_0+tq^2\) for any integer t>=0, and
\[
 C_n=\sum_{k=0}^{2n}(6k+1)(-1)^k2^{2n-k}
 \binom{2n}k\binom{3n}k\binom{4n}k.
\]
Let \(a=-1/2\bmod q\) and let the *unweighted* high-digit observer be
\[
 U_t=\sum_{h=0}^{2t}a^h\binom{2t}h\binom{3t}h\binom{4t}h\bmod q.
\]
For n0=qN0+r, define the three lower digits \(s_i=ir\bmod q\) (i=2,3,4). Define
\[
L=\sum_{j=0}^{\min_i s_i}(6j+1)a^j\prod_i\binom{s_i}j\bmod q^2.
\]
Assume the **explicit first-digit premise** \(L\equiv0\bmod q\). Then \(q\mid C_{n_t}\) for every t, and the exact transport congruence holds:
\[
\boxed{\frac{C_{n_t}}q\equiv 2^{2t}U_t\,\frac{C_{n_0}}q\pmod q.}\tag{PST}
\]
Consequently, \(q^2\mid C_{n_0}\implies q^2\mid C_{n_0+tq^2}\) for **all** t>=0. The converse is immediate when the statement is quantified for all t since t=0 is included. No asymptotic hypothesis or numerical extrapolation enters this propagation theorem.

### Structural proof: the top digits are a palindrome

When q=6b+1, \(N_0=r=b\) and
\[
(M_2,M_3,M_4)=(s_2,s_3,s_4)=(2b,3b,4b).
\]
When q=6b+5, \(N_0=b,\ r=5b+4\), so
\[
(M_2,M_3,M_4)=(2b+1,3b+2,4b+3),\quad
(s_2,s_3,s_4)=(4b+3,3b+2,2b+1).
\]
Thus in either residue class the multisets of high and low binomial top digits are **identical**, either in order or in reverse order. For \(n_t=n_0+tq^2\), the low digits s_i remain fixed and the high top digits become \(M_i(t)=M_i(0)+iqt\). Lucas's theorem applied to the high sum in the preceding q² theorem yields
\[
T(n_t)\equiv U_t\,T(n_0)\pmod q,\qquad
T_1(n_t)\equiv U_t\,T_1(n_0)\pmod q.
\]
Indeed the high summation index \(\ell=qh+j\) has \(q h+j\equiv j\bmod q\), and the three binomial products split into the top \(it\) and palindromic bottom \(s_i\) factors.

In the preceding two-digit formula, the low \(L\), its quotient \(\lambda=L/q\bmod q\), and coefficients A and B modulo q are unchanged as N increases by qt (since each M_i increases by iqt). The formula therefore gives
\[
C_{n_t}/q\equiv2^{2(N_0+r+qt)}U_t[(\lambda+A)T(n_0)+B T_1(n_0)]\pmod q.
\]
Since \(2^{2qt}=2^{2t}\bmod q\), comparison with t=0 proves (PST).

## Exact checks and certified infinite families

A standalone standard-library follow-up checker is \`research_notes/portable_direct/d25_prime_square_transfer_20261106.py\`, importing the exact q² verifier. It checks the T/T1 Lucas scaling and A/B invariance for **32** cases q=5,7,11,13,19,23,31,37; t=0,1,2,3. It additionally evaluates the original integer-binomial sum at six large n for q=5,7,11 and t=1,2, obtaining 6/6 PASS.

The previous exact two-digit formula was checked for each of the **166 primes** 5<=q<=1000 at n0=(q²-1)/6, and in this follow-up the checker separately confirmed \(L\bmod q=0\) and \(C_{n_0}\bmod q^2=0\) for all 166. Combining these finite exact base computations with the **proved** (PST) implication yields a rigorously determined infinite arithmetic progression for every one of those 166 primes:
\[
\boxed{q^2\mid C_{(q^2-1)/6+tq^2}\quad\text{for every integer }t\ge0.}
\]
The infinite quantification is justified by (PST); the prime list q<=1000 is the finite certified base domain. This is a local integer-shadow theorem; no uniform all-prime base divisibility claim is promoted.

## Observer value and next step

PST retains the sign and multiplicity of original k, the q-digit order/carry, unique original-class low carry channel and the high factor U_t. It is a source-preserving two-scale propagation certificate, not an original native crystalline/Frobenius/heartbeat experiment. Next scientific question: prove the **base** q² divisibility \(q^2\mid C_{(q^2-1)/6}\) for all primes q using finite-sum telescoping or the first-digit Clausen parameters; alternatively use these oriented carry terms to seek a genuine cancellation of the frozen D25 signed F/H second-digit ports. Source checkpoint, previous native completed units and contributed identities are untouched.

Classification: AUTHOR-PROVED algebra with finite exact checks; independent Driver review and native Result/Source publication remain pending.
