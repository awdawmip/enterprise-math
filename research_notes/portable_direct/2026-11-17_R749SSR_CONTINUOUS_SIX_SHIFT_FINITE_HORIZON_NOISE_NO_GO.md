# R749SSR — Continuous calibration, optimal six-shift asymptotics and finite-horizon noise obstruction

Date 2026-11-17. Evidence: **AUTHOR_EXACT_NOT_REVIEWED** (exact author certificate PASS; independent review pending).
Research mode: independent portable five-labeled-source scalar observer. Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessor: R749SSQ, PR #2581 @ a357d82b1a1a82a221f66ec4b8cf675f6d434bf4; relevant earlier integer-only sign theorem R749SSI, PR #2560.
P000 native X6/worldview, five source labels and joint-relation observer preservation are retained; no native BRC operation or X6 temporal law is asserted.

## Exact model

Five distinct labeled weights: \(w=(1,1,2,3,6)\), with the **first** unit-weight source marked.
For integer \(q\ge6\), define
\[
\Omega_q=\{k\in\mathbb{Z}_{\ge0}^{5}:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]
Let \(S(q)=18q^4+54q^3-345q^2+2070q-16315\), and
\[
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108},\quad
\mathcal O_q^{(m)}(e,d)=(Y_{q+6j}(e,d))_{j=0}^{m-1}.
\]
For each candidate cutoff, \((e,d)\in[-2,2]^2\) is *real*, fixed across the ordered reads of that candidate. Different candidate cutoffs may independently choose their own errors.

## Theorem 1: all six infinite-phase Laurent expansions

For \(q\equiv r\pmod6\), uniformly over the compact real error square,
\[
\boxed{Y_q(e,d)=L_r+\frac{A_r-720d}{q}
       +\frac{5(314928d+69984e-B_r)}{81q^2}+O(q^{-3})}.
\]

| r | L_r | A_r | B_r | d*_r=A_r/720 |
|---|---|---|---|---|
| 0 | 455/36 | 3335/3 | 151823 | 667/432 |
| 1 | -295/36 | 13780/9 | 252353 | 689/324 |
| 2 | -25/36 | 12845/9 | 241283 | 2569/1296 |
| 3 | 185/36 | 3740/3 | 192485 | 187/108 |
| 4 | -25/36 | 11485/9 | 182531 | 2297/1296 |
| 5 | -295/36 | 12980/9 | 217793 | 649/324 |

These constants are exact rational numbers, not numerical fits.

## Theorem 2: optimal fixed-calibration comparison orders

For any one fixed admissible pair \((e,d)\) in the same residue class,
\[
Y_{q+6}(e,d)-Y_q(e,d)=\frac{6(720d-A_r)}{q^2}+O(q^{-3}).
\]
For \(r=0,2,3,4\), the unique leading-term cancellation \(d=d_r^*\) is **inside** [-2,2], giving
\[
\boxed{Y_{q+6}(e,d_r^*)-Y_q(e,d_r^*)
=-\frac{60(314928d_r^*+69984e-B_r)}{81q^3}+O(q^{-4}).}
\]
The displayed coefficient is strictly negative for **every** \(e\in[-2,2]\). Indeed the \(q^{-2}\) Laurent coefficient at \(d_r^*\) is positive at both \(e=-2\) and \(e=2\), and is affine in \(e\); its zero would require \(e<-2\). Thus the best asymptotic order for a *fixed, q-independent, common calibration* is exactly \(q^{-3}\) for phases 0,2,3,4.

For \(r=1,5\), \(d_r^*>2\), so no admissible fixed calibration can eliminate the leading \(q^{-2}\) term: the best attainable order is \(q^{-2}\). These are asymptotic order statements, not explicit finite-q uniform inequalities; optimized independent/q-dependent competing calibration is a separate problem.

## Theorem 3: no universal finite-horizon absolute-noise radius

For every fixed integer \(m\ge1\),
\[
\boxed{\inf_{\substack{q,p\ge6\\q\ne p}}\;
\inf_{(e,d),(E,D)\in[-2,2]^2}
\|\mathcal O_q^{(m)}(e,d)-\mathcal O_p^{(m)}(E,D)\|_\infty=0.}
\]
In fact choose \(p=q+6\) and the **same** \((e,d)=(E,D)\) for both cutoffs. Coordinate \(j\) of the difference compares \(Y_{q+6j}(e,d)\) and \(Y_{q+6(j+1)}(e,d)\), hence is \(O_m(q^{-2})\) by Theorem 2. For phases 0,2,3,4 choose \(d=d_r^*\) to get \(O_m(q^{-3})\). Because \(m\) is fixed, taking the maximum over its coordinates preserves convergence to zero. The infimum is nonnegative and has an explicit sequence tending to zero, so it equals zero.

For any global proposed per-read error tolerance \(\varepsilon>0\), take two admissible noiseless vectors with distance less than \(2\varepsilon\); their midpoint is then consistent with both cutoffs. Therefore no **cutoff-independent positive absolute-noise tolerance** guarantees exact unbounded-cutoff identification from any fixed number of these readings. This is compatible with the earlier *pairwise* exact four-read separations: disjoint compact observation images for each fixed pair do not imply a positive lower bound uniform over infinitely many pairs.

## Proof: exact generating functions and infinite coefficient identity

Independent distinct labeled sources yield
\[
\sum_{q\ge0} C_qz^q=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\qquad
\sum_{q\ge0} T_qz^q=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]
Marking \(k_1\) replaces one of the two distinct unit-weight factors by \(z/(1-z)^2\). The cumulative cutoff contributes the extra \(z/(1-z)\). The equivalent recurrence \(T_q-T_{q-1}=C_{q-1}\) and direct small integer enumeration are independently checked in the companion program.

After multiplying the first series by \((1-z^6)^6\), its numerator is
\[
z(1+z+\cdots+z^5)^3(1+z^2+z^4)(1+z^3)
\]
of degree 23. For the second series multiply by \((1-z^6)^7\); the numerator is
\[
z^2(1+z+\cdots+z^5)^4(1+z^2+z^4)(1+z^3)
\]
of degree 29. Fixing a residue \(q=6n+r\), the coefficient formulas have terms \(\binom{n-j+5}{5}\) with \(j\le3\) and \(\binom{n-j+6}{6}\) with \(j\le4\), respectively. Their polynomial extensions vanish when \(0\le n<j\). Thus \(C_q\) and \(T_q\) are **exact** mod-six quasipolynomials of degrees 5 and 6 on the entire nonnegative-integer domain. Six/seven values per residue consequently determine exact infinite polynomial identities; this is not extrapolation from finite numerical sampling.

Let \(C_r(q)\), \(T_r(q)\) be these rational polynomials and put
\[
D_r(q)=C_r(q)+d,\qquad
N_r(q)=q^3(T_r(q)+e)-S(q)D_r(q)/108.
\]
The exact certificate constructs these polynomials, proves all degree 6–9 coefficients of \(N_r\) vanish identically, and checks both \(N_r\), \(D_r\) have degree five. If their coefficients at powers 5,4,3 are \(n_5,n_4,n_3\) and \(c_5,c_4,c_3\), respectively, rational division gives
\[
L_r=n_5/c_5,\quad a_r=(n_4-L_rc_4)/c_5,\quad
b_r=(n_3-L_rc_3-a_rc_4)/c_5.
\]
Exact coefficient comparison gives the six table rows and both symbolic expressions in Theorem 1. Since \(C_q+d>0\) for \(q\ge6\), the rational expansion has a remainder uniformly controlled on the compact calibration square. Substitution \(q\mapsto q+6\) and subtraction gives Theorem 2; the affine dependence of \(b_r\) on \(e\) gives its strict sign and optimal order. Theorem 3 follows as above.

## Exact diagnostic: do not transfer an integer-only sign theorem to real errors

For the **real-error** calibration \(e=0,d=667/432\) at \(q=5070\), the \(q^{-2}\) coefficient vanishes, but exact rational arithmetic gives
\[
\boxed{Y_{5076}(0,667/432)-Y_{5070}(0,667/432)
=-\frac{43072397158749918762229855318}
{22845986049467232904102240398950261}<0.}
\]
Thus using just \(\mathrm{sgn}(720d-A_0)\) to predict the exact continuous-error difference at the critical value would be invalid. R749SSI's earlier sign rule was stated for **integer** \(e,d\); it has no permitted critical \(d=667/432\) and is not contradicted by this example.

## Reproduction, scope, and next work

The accompanying Python 3/SymPy certificate reconstructs \(C_q,T_q\), double-checks 24 cutoffs by direct labeled enumeration, proves the rational mod-six coefficient identities and cancellation-domain assertions, and verifies the displayed full rational diagnostic. The local author run returned **PASS** with exact arithmetic; the JSON records the phase constants, cancellation tests and witness. Independent mathematical review remains pending.

The result is an **N2 scalar readout** over retained distinct labeled sources, not an X6 native physical-time event, Cell/Link/Port transition or BRC operation. A future typed transfer requires an explicit carrier and an exact observer-fibre preservation proof; no information-reducing projection is asserted here.

Next problems: sharpen minimax separation when the two candidate cutoffs use distinct and possibly q-dependent calibration; analyze whether any fixed pair needs more than four exact reads; derive cutoff-dependent positive noise certificates; treat integer-error-only recovery separately. Formal shared-task CLAIM/Result/review rights are neither implied nor requested by this publication.
