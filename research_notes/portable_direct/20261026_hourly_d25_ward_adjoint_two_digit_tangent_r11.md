# D25/LIFT — Second-digit tangent of the negative Ward adjoint

Date: 2026-10-26. TASK_RESEARCH logical conversation: chatgpt-research-hourly-enterprise-math-20260923. Maintenance conversation chatgpt-hourly-enterprise-math-20260921 is separate.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 **unchanged**.

Status: **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** Extends the already-proved first-digit central-binomial adjoint at p=733. It is not native CM, an accepted LIFT theorem, a native Source checkpoint, a claim or independent review. The known p=733 first-digit zero is not recredited as a new discovery.

## Input and theorem

For prime p=6m+1>=7 put N=2m-1. The inherited exact rational, p-unit-safe negative-orientation Ward adjoint is

\[
b_0=0,\quad b_t=\lambda_{-t}=
\frac{(p+2t-2)b_{t-1}-2^{1-t}}{p+2t-1}
\quad(1\le t\le N),\quad
\delta=2^{-N}-(p+2N)b_N.
\]

Define the already-used first-digit coefficients, and new weighted sums, over the p-local rationals:

\[
A_t=\frac{2^{2t-1}}{t\binom{2t}{t}},\quad
v_s=\frac{\binom{2s-2}{s-1}}{8^{s-1}},\quad
S_t=\sum_{s=1}^t v_s,
\]
\[
h_t=\sum_{u=2}^t\left(\frac1{2u-2}-\frac1{2u-1}\right),\quad h_1=0,\quad
T_t=\sum_{s=1}^t v_s\left(h_s+\frac1{2s-1}\right),\quad
W_t=h_tS_t-T_t.
\]

**New uniform two-digit formula (all target primes):**

\[
\boxed{b_t\equiv-A_t(S_t+pW_t)\pmod{p^2}}
\]
\[
\boxed{\delta\equiv d_0+p\,d_1\pmod{p^2},\quad
d_0=2^{-N}+2NA_NS_N,\quad
d_1=A_NS_N+2NA_NW_N.}
\]

The new harmonic-weighted carrier T is necessary to compute the genuine second-digit correction by this exact source decomposition. No assumption that the original signed Clausen tail or its infinity port vanishes is made.

## Complete proof

At fixed m introduce a formal algebraic variable X and set
\[
a_1(X)=1,\quad a_t(X)=\prod_{u=2}^{t}\frac{X+2u-2}{X+2u-1}.
\]
Variation of constants solves the original backward recurrence at X:
\[
b_t(X)=-a_t(X)\sum_{s=1}^{t}
\frac{2^{1-s}}{(X+2s-1)a_s(X)}.
\]
Direct substitution checks the base t=0 and the recurrence. The constant terms are a_t(0)=A_t and 2^{1-s}/((2s-1)A_s)=v_s. Differentiating the finite product at X=0 yields
\[
a_t(X)=A_t(1+Xh_t)+O(X^2),
\]
\[
\frac{2^{1-s}}{(X+2s-1)a_s(X)}
=v_s\left(1-X\left(h_s+\frac1{2s-1}\right)\right)+O(X^2).
\]
Multiplication gives b_t(X)=-A_t[S_t+X(h_tS_t-T_t)]+O(X^2).
For every target p, all constant denominators in these finite products and expansions are p-units (their positive factors are <p), so the coefficients belong to Z_(p). Evaluate at X=p and reduce mod p^2, proving the first boxed formula. Substitute into the exact definition of delta to obtain the second. There is no division by p in either derivation. QED.

## Secondary-port recovery and the explicit p=733 correction

Let Y be any p-integral *labelled* left-face source. If d_0 is divisible by p in Z_(p), define c=d_0/p+d_1 mod p. The boxed theorem gives
\[
\delta Y\equiv p\,c\,Y\pmod{p^2},\qquad
(\delta Y)/p\equiv c(Y\bmod p)\pmod p.
\]
When c is a p-unit the normalized secondary readout recovers Y mod p even though delta Y mod p=0. This recovers one raw-face digit, NOT Y mod p^2, other channels, or the original reflection.

For p=733, m=122,N=243, exact modular evaluation gives
\[
d_0\equiv142202=733\cdot194\pmod{733^2},\quad
d_1\equiv47\pmod{733},
\]
\[
\delta/733\equiv194+47=241\pmod{733},\quad
\delta\equiv176653=733\cdot241\pmod{733^2}.
\]
The previously independently established genuine unweighted corrected-Hasse (1,2) left face is Y_L^{12}=610 mod 733. Consequently
\[
\boxed{(\delta Y_L^{12})/733\equiv241\cdot610=410\pmod{733}.}
\]
The already-known direct recurrence checked delta=733*241; the **new** result is the universal closed tangent formula and its independently computable decomposition 194+47.

## Actual verification, scope, and next action

The accompanying Python standard-library checker evaluates the new A,v,h,S,T route independently of the original backward b recurrence, comparing all b_t and delta modulo p^2 across all 80 primes p=6m+1, 7<=p<=997: **12,196 coefficient/terminal identities PASS**. Exact Fraction checks cover six small prime cases; 733 secondary-face data separately PASS. These are author computations, not independent review or native H0/B0.

BRC **COMPOSE_APPLIED**: retained signed orientation n=ell-j, source channel (0,2)/(1,2)/(0,3), p-adic valuation, raw finite left face and its separate weighted observer. The scalar S alone omits the harmonic-weighted tangent T when subsequent operations require the next p-adic digit. Algebraic X is not a P000 native spatial axis; no transfer to the six-dimensional native geometry or three-dimensional slice is claimed.

Latest *read-only* own-lane canonical continuation evidence before this note: 2026-10-26 ~11:28 +08, kimi-query-bridge #6514–#6517. Persisted original Source checkpoint remains verified but historical claim pointer conflict persists, execution_authorized=false; no fresh CLAIM/OPEN/Source checkpoint is asserted by these author notes.

The next mathematical unit is to combine the actual (0,2),(1,2),(0,3) Hasse source and signed original T/U/K reflection at p=733 with the second-digit left-face repair, both finite cutoff faces, third-digit Green propagation, and the independent infinity port, obtaining an exact source-labelled remainder or a proved coupled telescoper. The original same-class H0/B0, [X]U mod p^2, semilinear Frobenius eta/kappa, Delta_p-R_p, native CM experiment and independent Driver review remain outstanding. Parent D25/LIFT/JT2 OPEN.