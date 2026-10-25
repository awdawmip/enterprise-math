# D25/LIFT — a source-corrected Clausen parameter port and denominator drift

Date 2026-10-25. Distinct TASK_RESEARCH author derivation, UNREVIEWED / NOT_ADMITTED / NO_NEW_NATIVE_CHECKPOINT. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Logical Research conversation chatgpt-research-hourly-enterprise-math-20260923. Scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains frozen. External auxiliary hypergeometric algebra only; no original-class CM or native X6 assertion.

## Question

Previous Jacobi jets were formed from b_n(x)=(-x)_n(-2x)_n/(n!)², keeping its lower denominator fixed. Yet the *parameterized* classical Clausen square identity requires a+b+1/2 as its lower 2F1 parameter. The two agree at original x=-1/6 but NOT at terminating x=m=(p-1)/6. Quantify the omitted source coordinate and construct a genuinely cross-source finite identity.

For p=6m+1>=7 prime, 0<=n<p, set c(x)=1/2-3x and

\[
\widetilde b_n(x)=\frac{(-x)_n(-2x)_n}{(c(x))_n\,n!},
\qquad \widetilde\Phi_x(z)=\sum_{n\ge0}\widetilde b_n(x)z^n.
\]

At x_0=-1/6=m-p/6, c(x_0)=1 and \widetilde b_n(x_0)=b_n(x_0) **exactly**, before truncation.

## Result A: a terminating cross-source identity

At x=m, the classical Clausen symmetric-square identity with a=-m, b=-2m and c=a+b+1/2=1-p/2 specializes to the exact finite rational polynomial equality

\[
\boxed{
\left(\sum_{n=0}^{m}\frac{(-m)_n(-2m)_n}{(1-p/2)_n n!}z^n\right)^2
=\sum_{n=0}^{2m}\frac{(-2m)_n(-3m)_n(-4m)_n}{(1-p/2)_n(1-p)_n n!}z^n.
}\tag{1}
\]

The general Clausen formula is a **known classical identity**, not claimed as newly discovered. Its familiar proof is the symmetric-square ODE of 2F1, whose third-order coefficient recurrence equals that of 3F2 under c=a+b+1/2, with constant coefficient 1. The negative-integer numerator terminates both sides before a denominator pole. This is a cross-source equality between *distinct terminating* 2F1 and 3F2 polynomials, not the earlier self-Green identity.

At the original x=-1/6, the same family gives the original hypergeometric equality

\[
{}_2F_1(1/6,1/3;1;z)^2
={}_3F_2(1/3,1/2,2/3;1,1;z).
\]

Finite D25 truncation still has an **ordered signed convolution tail**; a whole-series identity must not erase it.

## Result B: exact denominator corrections and mod p³ expansion

For 0<=n<p, all the following denominators are p-units. Put H_n=\sum_{j=1}^n j^{-1} and H_n^{(2)}=\sum_{j=1}^n j^{-2}. Define the two different source correction factors

\[
A_n=\frac{n!}{(1-p/2)_n}=\prod_{j=1}^n(1-p/(2j))^{-1},
\quad
C_n=\frac{(n!)^2}{(1-p/2)_n(1-p)_n}
=\prod_{j=1}^n (1-p/(2j))^{-1}(1-p/j)^{-1}.
\]

Their first two p-adic digits satisfy, in Z_(p),

\[
\boxed{A_n\equiv 1+\frac p2H_n+
\frac{p^2}{8}(H_n^2+H_n^{(2)})\pmod{p^3}.}\tag{2}
\]
\[
\boxed{C_n\equiv 1+\frac{3p}{2}H_n+
\frac{p^2}{8}(9H_n^2+5H_n^{(2)})\pmod{p^3}.}\tag{3}
\]

Thus the terminating 2F1 coefficient is A_n times the earlier fixed-denominator b_n(m), whereas the terminating 3F2 coefficient is C_n times (-2m)_n(-3m)_n(-4m)/(n!)³. These correction ports are distinct.

**Proof.** Expand each exact finite unit product in the p-local ring. Its formal logarithm has first-order coefficients (1/2)H_n and (3/2)H_n respectively, and second-order coefficients (1/8)H_n^(2) and (5/8)H_n^(2). Exponentiating to order p² adds the squares (1/8)H_n² and (9/8)H_n², proving (2)-(3).

## Result C: parameter derivative contamination, valid even at source zeros

Set A_n(x)=n!/(c(x))_n and S_n(x)=\sum_{j=0}^{n-1}1/(c(x)+j), S_{2,n}(x)=\sum_{j=0}^{n-1}1/(c(x)+j)^2. The following **exact rational** identities hold wherever the denominators are nonzero:

\[
\boxed{\widetilde b_n'(x)=A_n(x)\bigl(b_n'(x)+3S_n(x)b_n(x)\bigr).}\tag{4}
\]
\[
\boxed{\widetilde b_n''(x)=A_n(x)\bigl(b_n''(x)+6S_n(x)b_n'(x)+9(S_n(x)^2+S_{2,n}(x))b_n(x)\bigr).}\tag{5}
\]

They follow by differentiating A_n'/A_n=3S_n and (3S_n)'=9S_{2,n}. They divide by NO numerator and remain valid at zeros b_n(m)=0 on higher-rank layers.

**Nonzero loss witness at rank n=1**:
\[
b_1(m)=2m^2,\quad \widetilde b_1(m)=\frac{2m^2}{1-p/2},\quad
\boxed{\widetilde b_1(m)-b_1(m)\equiv p m^2\ne0\pmod{p^2}.}
\]
Hence treating raw F_i jets as if they were jets of a Clausen-compatible parameter family loses a real first-order p-adic source correction. This *repairs an interface*, without proving the hard D25/LIFT target.

## Evidence and next unit

The adjacent Python-standard-library checker verified exact rational polynomial identity (1) coefficientwise and p³ expansions (2)-(3) for every n<p for 8 primes p=7,13,19,31,37,43,73,103, plus the rank-one loss witness. General formulas derive from the stated finite products; the Clausen step remains identified as a known classical identity. AUTHOR-CHECKED, independent review PENDING.

BRC resolution COMPOSE_APPLIED: retain original versus terminating parameter, denominator source, Taylor-jet order, rank-zero layers, signed tail and permitted future differentiation. No positive-weight or native-X6 claim.

**Next minimum action:** form the finite signed Jacobi/Clausen relation using the corrected jets (4)-(5) and *the distinct Hasse boundary ports* from the preceding new unit, preserving the original ordered reflected tail; test that it is not a self-pairing tautology. The all-target-prime B_01,p+A_2H_0/72-T_jet,p=0 remains UNPROVED; authentic same-original-class CM H_0/B_0, [X]U mod p², Frobenius normalization and kappa bridge missing. D25/LIFT/JT2 parent OPEN.

Native Source read this run: INVALID_ARGUMENT / CONTROL_QUOTA. No new winning CLAIM, authorized OPEN or durable native Source checkpoint. The cross-epoch predecessor mismatch remains a historical unresolved support item under Enterprise Math Issue #1558; original receipts, staging, contributors and frozen scientific source stay unchanged. No maintenance ID or scheduler change.
