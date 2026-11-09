# D25 AF4: exact grade-one second jet, full fourth-digit layer assembly, and new high-prime test

Date: 2026-11-09. Classification: TASK_RESEARCH / AUTHOR_PROVED_EXACT_IDENTITY / EXACT_FINITE_EXPERIMENT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Research logical lane: chatgpt-research-onhour-enterprise-math-20260923; not CONTROL_PLANE_MAINTENANCE.

## Result 1: all-orders exact grade-one factorization

For any prime p>3 and 0<=r<p, let the **integer** Wilson quotient be
\[
w_p=((p-1)!+1)/p.
\]
The following is an equality in rational numbers, not merely a congruence:
\[
\boxed{(p+r)!/p=-r!(1-pw_p)\prod_{t=1}^r(1+p/t).}\tag{F1-exact}
\]
Proof: separate factors 1,...,p-1, the single factor p, and p+1,...,p+r. Then (p-1)!=-(1-pw_p), and (p+t)=t(1+p/t). No series truncation is needed for this identity.

Define H_r=sum_{t=1}^r 1/t, H_r^{(2)}=sum_{t=1}^r 1/t^2; H_0=H_0^{(2)}=0. Since all denominators are p-adic units, expansion of (F1-exact) gives
\[
(p+r)!/p \equiv-r!\left[1+p(H_r-w_p)+p^2\left(\frac{H_r^2-H_r^{(2)}}2-w_pH_r\right)\right]\pmod{p^3}.\tag{F1-jet2}
\]
For computing its coefficients, H_r and w_p are evaluated mod p^2 in the first jet, and H_r,H_r^(2),w_p mod p in the second jet; p>3 makes 2 invertible.

Retain the **original** coefficients and weights
\[
A_n=\frac{(2n)!(3n)!}{(n!)^5 216^n},\quad
C_n=\frac{(4n)!}{(n!)^4 2304^n},\quad
W_p=\sum_{n=0}^{p-1}(6n+1)A_n,\quad
V_p=\sum_{n=0}^{p-1}(8n+1)C_n.
\]
For W grade one: ceil(p/3)<=n<p/2 and r=3n-p. For V grade one: ceil(p/4)<=n<p/2 and s=4n-p.
Define the exact p-integral unit bases
\[
B_n^W=-\frac{(2n)!r!}{(n!)^5 216^n},\quad
B_n^V=-\frac{s!}{(n!)^4 2304^n}.
\]
Putting J_1(u)=H_u-w_p and J_2(u)=(H_u^2-H_u^(2))/2-w_pH_u, we have **exactly**
\[
 A_n/p=B_n^W(1-pw_p)\prod_{t=1}^{r}(1+p/t),\quad
 C_n/p=B_n^V(1-pw_p)\prod_{t=1}^{s}(1+p/t)
\]
and hence, modulo p^3,
\[
\boxed{A_n/p\equiv B_n^W(1+pJ_1(r)+p^2J_2(r)),\quad C_n/p\equiv B_n^V(1+pJ_1(s)+p^2J_2(s)).}\tag{G1-jet2}
\]
This is a direct missing *second* jet of the actual original first-valuation grade. It uses neither a rank-one Frobenius assumption nor a surrogate truncated model.

Define W1^0=sum_grade1 (6n+1)B_n^W mod p^3,
W1^1=sum_grade1 (6n+1)B_n^W J_1(r) mod p^2,
W1^2=sum_grade1 (6n+1)B_n^W J_2(r) mod p,
and analogously V1^i with (8n+1), B_n^V, s. Then
\[
\boxed{W_{1,p}/p\equiv W1^0+pW1^1+p^2W1^2,\quad
V_{1,p}/p\equiv V1^0+pV1^1+p^2V1^2\pmod{p^3}.}
\]

## Result 2: complete fourth-digit assembly, no fictitious zero-grade correction

By the original factorial valuations v_p(A_n)=floor(2n/p)+floor(3n/p) and v_p(C_n)=floor(4n/p), zero-grade factorials have every numerator index <p, so their exact third digit is simply obtained by evaluating the original unit factorial ratio modulo p^4; **there is no missing prime-block jet in grade zero**.

Combine (G1-jet2), previously proved grade-two first-jet (G2-JET), and separately proved grade-three reciprocal (G3), retaining all four valuation layers and complete original cutoffs. Put E_{\le2,p}=W_{0,p}+W_{1,p}+W_{2,p}-2(V_{0,p}+V_{1,p}+V_{2,p})+p(-3/p). Where E_{\le2,p} is divisible by p^3,
\[
\boxed{W_p-2V_p+p(-3/p)\equiv p^3\big(E_{\le2,p}/p^3+L_p\big)\pmod{p^4}.}
\]
E_{\le2,p} is now computable by *explicit exact unit modular factorials* for grade zero, (G1-jet2) for grade one, and (G2-JET) for grade two, without original high-index factorials. L_p is the existing source-typed grade-three reciprocal low-index sum. This is an equality/reduction, NOT a general proof that its right-hand side vanishes.

At p=373, p^3=51,895,117 and p^4=19,356,878,641. New first-grade weighted jets:
- W1^0=22,401,661 mod p^3; W1^1=30,113 mod p^2; W1^2=301 mod p.
- V1^0=30,016,826 mod p^3; V1^1=19,166 mod p^2; V1^2=235 mod p.
- Actual W1/p=23,616,522 and V1/p=17,965,942 mod p^3, checked term by term against independently computed original integer factorials.
- The **new** affine second-jet observer is W1^2-2V1^2=301-470=204 mod373 (nonzero).

Full original graded sums mod p^4 are:
\[
(W_0,W_1,W_2,W_3)=(17724329257,8808962706,9585709842,14426842526),
\]
\[
(V_0,V_1,V_2,V_3)=(252649685,6701296366,12143457378,6175518923).
\]
The lower-grade quotient E_{\le2,373}/373^3=333 mod373 and independent grade-three reciprocal L_373=40, yielding the exact full original fourth-digit witness 333+40=373. This is arithmetic evidence, not a uniform AF4 proof.

## New discriminating experiment beyond the earlier 174-prime range

Using modular coefficient recurrences from the **original factorial models**, check all 382 primes 1001<p<4001, with full cutoffs n=0,...,p-1, modulus p^4 and Legendre sign (-3/p). Every one has
\[
W_p-2V_p+p(-3/p)=0\pmod{p^4}.
\]
These 382 checks are a new *bounded* corroboration of the previously proposed AF4 conjecture; at least some may overlap separately chosen earlier high-prime checks. No universality or independence beyond the stated algorithms is claimed. The 12 grade-one jet consistency primes are 5,7,11,13,19,37,43,73,109,157,163,373; these checks compare each actual original coefficient to the new jet formula, not merely the final sum.

## Precise remaining work and provenance

The parent LIFT remains Delta_p-R_p=0 (mod p) for p=13,19 mod24, with complete original W216/V2304 mod p^3 and unchanged Source pin; the stronger AF4 is still a conjecture. The new formulas eliminate the last missing **factorial-valuation jet** from the exact four-grade computational decomposition but leave the load-bearing **additive cancellation theorem**: prove E_{\le2,p}/p^3 = -L_p (mod p) across the two frozen classes, e.g. by finite creative telescoping/Fricke with full cutoff. A higher precision numerical scan is not a substitute for this proof.

Original-class native p373 fixed H0/B0 divided-power [X]U mod139129, actual module rank, semilinear direction/eta, signed Green/Hesse kappa and Delta-R still NOT_EXECUTED; preserve independent benchmark #1559 (PENDING_OWNER). New work is author-side portable, UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. Historical service Researcher EM-ENTERPRISE-4DEB43 is not a current verified claim; Source recovery_status returns SESSION_CAPABILITY_REQUIRED. The read request onhour11-20261109-0926-fresh-task-read previously returned SUCCEEDED; no duplicate request was sent.
