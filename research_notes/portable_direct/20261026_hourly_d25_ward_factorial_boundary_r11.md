# D25/LIFT — Factorial-normalized oriented Ward quotient and unavoidable Hasse-(1,2) boundary

Date: 2026-10-26. Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** External corrected-Clausen finite-rank theorem; not native original-class CM/divided-power evidence, a Source checkpoint, an all-prime D25/LIFT/JT2 proof or independent review.

## Exact inherited input and new question

Consume without re-crediting research_notes/portable_direct/20261026_hourly_d25_diagonal_one_digit_resonance_r11.md: its actual corrected-Hasse sources S_n^{ab}=J_n^{ab}+E_n^{ab}, labels (j,ell), orientation n=ell-j, and channels (a,b)=(0,2),(1,2),(0,3). For a prime p=6m+1>=7, set L=1-2m, U=2m and

\[
Y_n^{ab}=M_n^{ab,1}-\frac{p-n}{2}M_n^{ab,0},\qquad
(p-2n)Y_n^{ab}-(p-2n-1)Y_{n+1}^{ab}=S_n^{ab}\quad (L\le n<U). \tag{1}
\]

The signed labelled moments are formed from the corrected Clausen jets u_{a,j}u_{b,p-\ell}. The prior theorem proved the exact endpoint Ward law

\[
\sum_{h=0}^{U-1}D_hS_h^{ab}=P Y_L^{ab}-\sum_{h=L}^{-1}D_hS_h^{ab},\quad
D_h=\frac1{p-2h-1}\prod_{k=h+1}^{U-1}\frac{p-2k}{p-2k-1},\quad
P=\prod_{k=L}^{U-1}\frac{p-2k}{p-2k-1}. \tag{2}
\]

The LHS is divisible by p in Z_(p). New problem: explicitly normalize the Green products after factoring p, preserve negative-orientation source terms, and decide whether the actual finite left boundary may be discarded in each Hasse channel.

## Theorem A — factorial-normalized one-digit Ward law

Define the p-units

\[
F_m=\prod_{k=1}^{2m-1}\frac{2k}{2k+1}
=\frac{2^{4m-1}(2m-1)!(2m)!}{(4m)!},\qquad
C_a=\prod_{t=1}^{a}\frac{2t}{2t-1}
=\frac{4^a(a!)^2}{(2a)!},\qquad C_0=1. \tag{3}
\]

For 0<=a<=2m-2 all terms are p-integral and

\[
\boxed{\frac{D_{-a-1}}p\equiv-\frac{F_m C_a}{2a+1}\pmod p},\qquad
\boxed{\frac Pp\equiv-F_m C_{2m-1}\pmod p}. \tag{4}
\]

Consequently the complete p-local normalized flux is

\[
\boxed{\frac1{pF_m}\sum_{h=0}^{2m-1}D_h S_h^{ab}
\equiv\sum_{a=0}^{2m-2}\frac{C_a}{2a+1}S_{-a-1}^{ab}
-C_{2m-1}Y_{1-2m}^{ab}\pmod p.} \tag{5}
\]

The quotient on the LHS is p-integral BEFORE reducing modulo p, by (2) and the single exceptional factor k=0. This is not division by an arbitrary zero class.

**Proof.** Every denominator p-2k-1 for 1-2m<=k<2m is a p-unit: |2k+1|<p. The numerator p-2k is a unit except at k=0, where it is exactly p. At h=-a-1, separate the product into k=-a,...,-1, k=0, and k=1,...,2m-1. After extracting p and reducing modulo p, the negative factors equal 2t/(2t-1) for t=1,...,a, the positive factors 2k/(2k+1), the exceptional denominator (p-1)^{-1}=-1, and the prefactor (p+2a+1)^{-1}=(2a+1)^{-1}. This gives the first (4). Starting at L=1-2m instead includes all negative t up to 2m-1 and proves the second (4). Substitution into (2), retaining all channel and source labels, proves (5). All factorial arguments in (3) are below p, so F_m and C_a are p-units. QED.

## Theorem B — a uniform non-removable (1,2) boundary

At n=L there is exactly one labelled pair: j=2m, ell=1. Therefore

\[
Y_L^{ab}=\left(2m-\frac{p-L}{2}\right)u_{a,2m}u_{b,p-1}
=-2m u_{a,2m}u_{b,p-1}. \tag{6}
\]

For the corrected Clausen family

\[
\widetilde b_r(x)=\frac{(-x)_r(-2x)_r}{(\frac12-3x)_r r!},
\qquad u_{a,r}=[t^a]\widetilde b_r(m+t), \tag{7}
\]

we have u_{0,2m}=0 EXACTLY, so Y_L^{02}=Y_L^{03}=0 over Q. But at r=2m the first Pochhammer zero is simple, and at r=p-1=6m the two Pochhammer zeros make the reflected second jet nonzero. Direct product expansion gives

\[
u_{1,2m}=\frac{(-1)^{m+1}m!(m-1)!}{(\frac12-3m)_{2m}},\quad
u_{2,p-1}=\frac{2(-1)^m m!(2m)!(4m-1)!(5m-1)!}
{(\frac12-3m)_{p-1}(p-1)!}. \tag{8}
\]

Since 1/2-3m=1-p/2, each denominator (1-p/2)_r is r! modulo p. Wilson's theorem and factorial reflection r!(p-1-r)!\equiv(-1)^{r+1} imply

\[
u_{1,2m}\equiv\frac{(-1)^{m+1}}{m\binom{2m}{m}},\qquad
u_{2,p-1}\equiv\frac{2}{(2m+1)(m+1)}\pmod p. \tag{9}
\]

Thus

\[
\boxed{Y_L^{12}\equiv
\frac{4(-1)^m}{\binom{2m}{m}(2m+1)(m+1)}\not\equiv0\pmod p.} \tag{10}
\]

All denominators and C_{2m-1} are p-units, so the correction C_{2m-1}Y_L^{12} in (5) is nonzero for EVERY target prime. It cannot be dropped in the (1,2) oriented transfer; corresponding (0,2) and (0,3) boundary terms vanish exactly. A separately proved correction from another source/infinity port could still cancel it in a different observer. QED.

## Reproducible author evidence

Companion stdlib checker reconstructs exact Fraction corrected jets, labelled moments and BOTH finite J+E source faces. It checks rational recurrences and Ward law, then the factorial Green limits (4), full quotient (5), nonzero seed (10), and a p=13 three-channel witness. Actual local run over m=1,...,12: **1,374 counted exact assertions PASS**. Prime targets p=7,13,19,31,37,43,61,67,73 receive modular checks; composites 25,49,55 are rational-only checks. No independent review or native CM test.

For p=13, m=2, F_m=9 mod13, the tagged values are:

| Channel | Positive flux / p | Negative factorial sum | Boundary C_3 Y_L | Normalized positive flux / (p F_m) |
|---|---:|---:|---:|---:|
| (0,2) | 8 | 11 | 0 | 11 |
| (1,2) | 11 | 2 | 8 | 7 |
| (0,3) | 2 | 6 | 0 | 6 |

The middle row is a concrete error certificate: 2-8=7 mod13; deleting the genuine boundary produces 2 instead of 7.

## BRC and continuation

BRC **COMPOSE_APPLIED**: exact rational/p-valuation carrier; preserve ordered pair (j,ell), signed orientation, three Hasse channels, both cutoff sources, and the separately tagged infinity observer. This normalized quotient is sufficient only for the first-digit Green operator; it is not a reconstruction of the full second-rank operation or the separately weighted original reflection 2^n(1-6n). Reuse the accepted-source full unimodular binomial-fibre formulas only at their proved scope. Auxiliary Laurent/Hasse variables are external mathematics, not native X6 primitive P000 axes. P000 and science Source pin unchanged.

**Next exact unit:** couple (5) and (10) to the complete corrected-Clausen (k-1,k-2) Hasse recurrence, carry both finite boundaries and the infinity port, then compare separately tagged T02,U02,T12,T03; obtain a real adjoint/WZ cancellation or source-tagged nonzero remainder. Original-class H0/B0, [X]U mod p^2, Frobenius direction/eta, kappa, Delta_p-R_p and independent review remain outstanding. Native CM NOT_RUN; D25/LIFT/JT2 remains OPEN. GitHub portable storage is not a winning Source CLAIM, authorized run, native checkpoint or mathematical admission. Research logical ID: chatgpt-research-hourly-enterprise-math-20260923 (not the maintenance lane).