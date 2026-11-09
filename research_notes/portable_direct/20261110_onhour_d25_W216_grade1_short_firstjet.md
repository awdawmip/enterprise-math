# D25 — Original W216 grade-1 terminating first p-adic jet

Date: 2026-11-10. Status: **AUTHOR_SIDE / EXACT ALGEBRAIC PROOF / 13 EXACT PRIME CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical conversation chatgpt-research-onhour-enterprise-math-20260923, separate from maintenance.

## Theorem — all primes p=6m+1>3

Retain the original, signed 216 coefficient:

$$
A_k=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k}
=\frac{(2k)!(3k)!}{(k!)^5\,216^k},
\qquad W_p=\sum_{k=0}^{p-1}(6k+1)A_k.
$$

The valuation-one band is $2m<k\le3m$. Set $n_1=2m+1=(p+2)/3$. The Wilson quotient is $w_p=((p-1)!+1)/p$ reduced mod $p$. Put $u_0=A_{n_1}/p$ mod $p^2$.

**Seed formula:**

$$
\boxed{u_0\equiv
-\frac{2(2n_1)!}{(n_1!)^5\,216^{n_1}}
\left[1+p\left(\frac32-w_p\right)\right]\pmod{p^2}.}\tag{1}
$$

Set $g_0=1$, $S_0=0$ and, for $0\le j<m-1$, define

$$
r_j=\frac{3(6j+7)(j+1)(3j+4)}{4(3j+5)^3},
\qquad
E_j=\frac{2}{6j+7}+\frac{1}{3(j+1)}
+\frac{1}{3j+4}-\frac{3}{3j+5},
$$

$$
g_{j+1}=g_jr_j\pmod{p^2},\qquad S_{j+1}=S_j+E_j\pmod p.
$$

All fractions involve $p$-units on their displayed index ranges. For every $0\le j\le m-1$,

$$
\boxed{\frac{A_{n_1+j}}p\equiv u_0g_j(1+pS_j)\pmod{p^2}.}\tag{2}
$$

Consequently the **original signed** valuation-one contribution is a length-$m$ terminating first jet:

$$
\boxed{\frac{W_{1,p}}p\equiv
u_0\sum_{j=0}^{m-1}(2p+5+6j)\,g_j(1+pS_j)
\pmod{p^2}.}\tag{3}
$$

At the transition step $j=m-1\to m$, the factor $6j+7$ equals $p$; the first-jet recurrence is used only for $j<m-1$. The next coefficient belongs to valuation grade two, whose previously proved jet is separately retained.

## Proof

The exact original coefficient recurrence is

$$
\frac{A_{k+1}}{A_k}=
\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}.
$$

After substituting $k=n_1+j$, it becomes *exactly*

$$
\frac{(j+\frac76+\frac p3)(j+1+\frac p3)(j+\frac43+\frac p3)}
{2(j+\frac53+\frac p3)^3}.
$$

Expanding to first order in $p$ gives $r_j(1+pE_j)\pmod{p^2}$ for $j<m-1$. Multiplying produces the harmonic prefix $S_j$ and proves (2) from (1). For (1), use $3n_1=p+2$ and

$$
\frac{(p+2)!}{p}=(p-1)!(p+1)(p+2),\qquad
(p-1)!=-1+pw_p.
$$

The exact weight $6(n_1+j)+1=2p+5+6j$ proves (3). All termwise divisions are performed only after the valuation-one factor has been established.

## BRC provenance and earlier results

The carrier is $(k,v_p(A_k),A_k,6k+1)$, and the typed port is $(j,u_0,g_j,S_j,2p+5+6j)$. Equations (2)–(3) prove preservation of the signed original grade-1 observer at the declared $p^2$ precision.

This consumes the already completed grade-2 first-jet result, research_notes/portable_direct/20261109_onhour_d25_W_grade2_firstjet_signed_AF4.md, and the preceding new grade-0 second-jet reconstruction, research_notes/portable_direct/20261110_onhour_d25_W216_lower_grade_twojet_completion.md. No prior result is recredited. The new first-jet format supplies a second length-$m$ terminating port for a future *signed cross-band* finite WZ/Jacobi telescope; the grade-0 second jet and original 2304 signed cross-band carry remain independent inputs.

## Executed independent exact checks

Source code: research_notes/portable_direct/d25_w216_grade1_short_firstjet_20261110.py. The checker compares every predicted coefficient $A_{n_1+j}/p\bmod p^2$ and the weighted sum with independently computed original integer binomial sums modulo $p^3$.

For $p=7,13,19,31,37,43,61,67,73,109,157,181,373$, all **13/13** primes pass, in exact integer modular arithmetic without floats. Representatives:

- $p=13$: $u_0=28$, $W_{1,p}/p=149\bmod169$;
- $p=19$: $u_0=337$, $W_{1,p}/p=254\bmod361$;
- $p=373$: $u_0=93197$, $W_{1,p}/p=103721\bmod139129$; leading digit $27\bmod373$.

## Live obligations

The parent $\Delta_p-R_p\pmod p$ for $p\equiv13,19\pmod{24}$ remains OPEN. The next portable research operation is to couple the grade-0 second jet, the present grade-1 first jet, and the previously proved grade-2 first jet into a signed original $W_p-p$ telescoper preserving p-adic carry and both $m$ parities.

The **highest original native benchmark** remains fixed p=373 same-original-class H0/B0 divided-power $[X]U\bmod139129$, native rank, semilinear Frobenius direction, normalization $\eta$, signed odd Green/Hesse, native $\kappa$, $\Delta_p-R_p$, and independent reproduction. Existing support Issue #1559 is PENDING_OWNER; this proof is not native execution.

Native Source: the fresh continuation request onhour11-20261110-0556-current-continuation later reconciled to SUCCEEDED, but the Research lane has no authenticated current issued session key, winning CLAIM or run. All outputs here are AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED.
