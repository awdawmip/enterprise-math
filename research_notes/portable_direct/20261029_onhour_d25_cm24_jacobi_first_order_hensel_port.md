# D25 / SECOND-DIGIT-LIFT: Jacobi first-order transport and source-preserving Hensel obstruction

**Date:** 2026-10-29. **Evidence status:** AUTHOR-SIDE / EXACT ALGEBRA / EXECUTED INTEGER CHECK / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_EXECUTED.

Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Unchanged frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research ordinary-control logical conversation chatgpt-research-onhour-enterprise-math-20260923; never the maintenance conversation.

This consumes the exact 616-prime CM(-24) Hasse rank-line frontier at commit 6aed9ded2a54f765249cddaa6cc4c4e71527e9f8; it adds a polynomial theorem, a first-order symmetry defect, a proved derivative orientation and a fixed-argument p² transport obstruction. It does not repeat the finite survey or claim a universal Root2 proof.

## 1. Exact Jacobi identity and full first-order correction

For every prime p>3 put k=(p-1)/2, e=floor((p-1)/4), and define the EXTERNAL Hasse polynomial

\[
H_p(t)=\sum_{j=0}^{e}\binom{k}{2j}\binom{2j}{j}\left(\frac{1-t}{4}\right)^j.
\]

**Theorem.** The following is an exact rational-polynomial identity, followed by a coefficientwise p² congruence:

\[
\boxed{H_p(t)=P_e^{(0,-p/2)}(2t-1)
=\sum_{j=0}^{e}\frac{(-e)_j(e+1-p/2)_j}{(j!)^2}(1-t)^j.}
\]

Let

\[
a_j=\frac{(-e)_j(e+1)_j}{(j!)^2},\quad
h_{e,j}=\sum_{r=0}^{j-1}(e+1+r)^{-1},\quad
M_e(X)=\sum_{j=1}^{e}a_j h_{e,j}X^j.
\]

All denominators e+1+r are p-units because e+j< p. Then

\[
\boxed{H_p(t)\equiv P_e(2t-1)-\frac p2M_e(1-t)\pmod{p^2}.}
\]

**Proof.** In the coefficient of (1-t)^j, use
\[
\binom{k}{2j}\binom{2j}{j}4^{-j}
=\frac{(-k)_{2j}}{4^j(j!)^2}
=\frac{((1-p)/4)_j((3-p)/4)_j}{(j!)^2}.
\]
For p=4e+1 or 4e+3, the unordered numerator parameter pair is precisely {-e,e+1-p/2}; the terminating hypergeometric normalization is the classical Jacobi polynomial. Expanding the second rising factorial once around e+1 gives the displayed p² formula, coefficient by coefficient. No limiting or infinite-series argument is used.

Writing \(\epsilon=(-1)^e=(\frac{-2}{p})\), classical Legendre parity gives both

\[
\boxed{H_p(1-t)\equiv\epsilon H_p(t)\pmod p}
\]

and the explicitly signed first-order parity defect

\[
\boxed{H_p(1-t)-\epsilon H_p(t)
\equiv-\frac p2\bigl(M_e(t)-\epsilon M_e(1-t)\bigr)\pmod{p^2}.}
\]

In particular the mod-p parity may NOT be lifted to p² without the harmonic correction.

## 2. Proved derivative eigenline split at the CM quadratic point

Work in the full two-component algebra
\[
R_p=\mathbf F_p[t]/(36t^2-36t+1),\quad x=2t-1,\quad x^2=8/9.
\]

Differentiating the polynomial congruence yields
\[
\boxed{H'_p(t)\equiv2P'_e(x)\pmod p.}
\]
For odd e, P'_e is even in x, so its evaluation is scalar in R_p. For even e, P'_e is odd in x, so it is proportional to x=2t-1. Consequently, writing \(H'_p(t)=D_0+D_1t\), **for all p>3**:

\[
\boxed{p\equiv5,7\pmod8\Longrightarrow D_1=0,}
\]
\[
\boxed{p\equiv1,3\pmod8\Longrightarrow 2D_0+D_1=0.}
\]

In the four CM-inert classes this exactly separates p=13,23 mod24 (scalar derivative port) from p=17,19 mod24 (trace-zero derivative port). The latter structural distinction is proved, not an extrapolation from the previous 616-prime root2 survey.

At a Hasse-zero CM point the derivative is a unit. Indeed Legendre's ODE
\((1-x^2)P''_e-2xP'_e+e(e+1)P_e=0\)
has \(1-x^2=1/9\) a unit; a simultaneous root of P_e and P'_e would force every derivative to vanish, contradicting \(0<\deg P_e=e<p\). This proves simple-root regularity in every CM branch for which the previously established first-digit Hasse zero applies.

## 3. Exact Hensel port and failure of a coordinate-only p² repair

In
\[
R_{p^2}=(\mathbf Z/p^2\mathbf Z)[t]/(36t^2-36t+1)
\]
we retain the original algebraic CM lift and its fixed argument \(z(t)=4t(1-t)=1/9\).

When \(H_p(t)=p h\) and \(d=H'_p(t)\bmod p\) is a unit, the unique first-order zero shift is
\[
\boxed{\delta_H=-h\,d^{-1},\quad H_p(t+p\delta_H)=0\pmod{p^2}.}
\]
Its exact argument change is
\[
\boxed{\delta_z=\frac{z(t+p\delta_H)-1/9}{p}
\equiv4(1-2t)\delta_H\pmod p.}
\]

For the ORIGINAL companion \(K_b(z)=\sum_{n=0}^{b}(1/8)_n(3/8)_n z^n/(n!)^2\), retain \(D=(z\partial_z K_b)(1/9)\) and its actual truncation index b. Taylor expansion, retaining the source and derivative operation, gives
\[
\boxed{K_b(1/9+p\delta_z)-K_b(1/9)
\equiv p(9D)\delta_z\pmod{p^2}.}
\]

If \(h\ne0\), \(D\ne0\pmod p\), and \(K_b(1/9)=0\pmod{p^2}\), then the right-hand side is nonzero: d and \(1-2t\) are units, with \((1-2t)^2=8/9\). Therefore moving only the Hasse parameter to its Hensel root DESTROYS the companion p² zero at the moved argument. A valid finite quadratic transport at the ORIGINAL z=1/9 requires a compensating derivative/source-port term. This is an exact obstruction to a naive proof shortcut, not a Root2 counterexample.

The following are exact (A,B) coefficients in the unreduced basis A+Bt, modulo p after the indicated division by p:

| p | H_p/p | H'_p mod p | delta_H | delta_z | shifted K_b / p |
|---:|---|---|---|---|---|
| 13 | (2,4) | (6,0) | (4,8) | (12,1) | (5,8) |
| 23 | (21,9) | (11,0) | (19,18) | (11,6) | (10,18) |
| 373 | (14,28) | (180,0) | (203,33) | (322,109) | (316,56) |

At p=373 the ORIGINAL \(K_b(1/9)=0\pmod{139129}\), \(D=5\pmod{373}\), and \(K'_b(1/9)=9D=45\pmod{373}\). Thus \(45(322+109t)=316+56t\pmod{373}\), nonzero. At p=23 the original companion also has a p² zero, but its Hasse vector is NOT on the 13-class rank-line, so the two branches must remain distinct.

## 4. Executed evidence, method reuse, and continuation

The self-contained exact integer checker is in the same submission as this note:
research_notes/portable_direct/d25_cm_jacobi_hensel_guard_20261029.py.

It verifies the Jacobi/harmonic formula coefficientwise and Legendre derivative eigenlines for **all 76 primes 5<=p<400**, and directly evaluates the shifted Hasse polynomial at eleven Root2-class primes (including 13,23,373). The original companion uses its true numerator-hit truncation and modular arithmetic rather than floating-point or a native H0/B0 surrogate. Its actual stdout:

    PASS_JACOBI_FIRST_ORDER_AND_DERIVATIVE_EIGENLINE 76 primes <400
    PASS_SOURCE_PRESERVING_HENSEL_PORT_OBSTRUCTION p=13,23,373

**BRC COMPOSE_APPLIED:** the carrier is the full pair (A,B), first-order Jacobi defect, derivative jet, original fixed CM quadratic relation, actual K_b(z) and D, valuations, branch/Galois labels and ordered operations. The B-2A rank-line readout alone is not a safe quotient for later differentiation/Frobenius or parameter movement.

**Unfinished scientific unit:** construct the true finite p² quadratic transformation at UNCHANGED z=1/9 and explicitly compute the correction coupling the M_e harmonic defect and companion jet, separately for 13 and 23 mod24. The universal 13-class rank-line and Root2 proof remain unproved. Reuse the existing Clausen, three-port, CM first-digit and 616-prime results without repeating them.

**Native priority and authority:** Existing Issue #1559 retains the p=373 same-original-class H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius/eta, signed odd Green/Hesse, kappa and Delta_p-R_p, requiring a real authorized evaluator and independent checks. This external author-side algebra does not fulfill it. 2026-10-29 read-only Site status: research_authority_granted=false, write_relay_enabled=false; no authenticated own session/claim/run or original target_request_id was confirmed. Formal Source checkpoint, Result and independent review await a lawful writer. Do not register, prepare, claim, open, or dispatch as the separate maintenance conversation. No source pin, taskbook, scheduler, or notification change.
