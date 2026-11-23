# PREFIX-1037 — Effective resonant Bessel bounds and certified signs at y=4,16

2026-11-23 (Asia/Shanghai). Parent: PREFIX-1036. Status: AUTHOR_COMPUTER_ASSISTED_PROOF / NOT_INDEPENDENTLY_REVIEWED.

## Scope and frozen sources

Frozen P000 V5: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Retain Stage46 signed BRC W=J12−6I12, incoming −e1, blocked bidirectional Link {0,e1}, exactly one negative outgoing step, and native X6 Cell–terminal-port–grade joint observer. This note studies **only** the *derived six-phase scalar spectral observer*, not a native BRC propagation or proof of full native-state equivalence.

Inputs: PREFIX-1033 continuous signed density, PREFIX-1034 critical cusps, PREFIX-1035 all-order recurrence, and PREFIX-1036 single-Bessel integral and resonant coefficients. The exact source for the latter is research_notes/portable_direct/2026-11-23_r6_prefix1036_bessel_resonant_tail_correction.md (read on current main, blob 3bb70e1b55743009491a2b5f7110fd6abde115b4). All assertions on g inherit the validity and domain of that original scalar representation.

For y∈(0,36), r=√y, H=y²(36−y)², P=y(y−36)(17y−91), A=2H'−P, set

\[
K(t;y)=\frac{J_0(t)^6}{5}\left[ A(y)tJ_0(rt)-\frac{H(y)}r t^2J_1(rt)+12(11+y)\left(r(y-6)J_1(rt)-\frac{2y}{t}J_2(rt)\right)\right].
\]

The inherited identity is \(g(y)=\int_0^\infty K(t;y)\,dt\). Write \(I_T(y)=\int_0^T K(t;y)\,dt\).

## Theorem A — effective tails (T≥20)

Define \(C_4=-1536\sqrt2/\pi^{7/2}\) and \(C_{16}=-1920/\pi^{7/2}\) (these are the *integrand's* nonoscillatory \(t^{-3/2}\) coefficients). Then

\[
\boxed{|g(4)-I_T(4)-2C_4/\sqrt T|\le 900/T^{3/2}},\qquad
\boxed{|g(16)-I_T(16)-2C_{16}/\sqrt T|\le2200/T^{3/2}}.
\]

Proof. For ν=0,1 set \(q_\nu=|\nu^2-1/4|\), \(a=\sqrt{2/\pi}\). The Bessel equation for \(w_\nu(x)=\sqrt{x}J_\nu(x)\) is \(w''+w=(\nu^2-1/4)w/x^2\). Variation of constants about the standard positive-infinity oscillatory asymptotic gives an integral of Volterra mass ≤\(q_\nu/x\). Its Neumann estimates give, for \(x>0\),

\[
|J_\nu(x)|\le a x^{-1/2}e^{q_\nu/x},\quad
|J_\nu(x)-a x^{-1/2}\cos(x-\nu\pi/2-\pi/4)|
\le a q_\nu x^{-3/2}e^{q_\nu/x}.
\]

Control \(J_2\) using \(J_2(x)=2J_1(x)/x-J_0(x)\). At r=2 or4, let \(L=H(r^2)a^7/(5r^{3/2})\), \(q_0=1/4,q_1=3/4\). The principal kernel equals
\(-L t^{-3/2}\cos^6(t-\pi/4)\cos(rt-3\pi/4)\).
The identity \(32\cos^6 x=10+15\cos2x+6\cos4x+\cos6x\) gives the above \(C_r\). After the constant mode is subtracted, every frequency has absolute value ≥2; the sum of absolute Fourier amplitudes is ≤1. Integration by parts bounds their tail by \(L/T^{3/2}\).

The other terms satisfy \(|R(t)|\le (M_1+M_2+M_3+M_4)t^{-5/2}\) on \(t\ge T\), with
\[
\begin{aligned}
M_1&=L(6q_0e^{(6q_0+q_1/r)/T}+(q_1/r)e^{q_1/(rT)}),\\
M_2&=|A|a^7e^{(6q_0+q_0/r)/T}/(5\sqrt r),\\
M_3&=12(11+y)r|y-6|a^7e^{(6q_0+q_1/r)/T}/(5\sqrt r\,T),\\
M_4&=24(11+y)y a^7e^{6q_0/T}(e^{q_0/(rT)}+2e^{q_1/(rT)}/(rT))/(5\sqrt r\,T^2).
\end{aligned}
\]
All terms decrease with T. The total effective constant is \(L+\frac23\sum M_i\). At T=20, use the rational inequalities
\(\pi>157/50,\ (2/\pi)^{7/2}<207/1000,\ 1/\sqrt2<3/4,\ e^z\le(1-z)^{-1}\) for 0≤z<1. The accompanying Fraction checker evaluates the resulting upper bounds as <858 at y=4 and <2130 at y=16. In particular they are below 900 and 2200. QED.

## Theorem B — certified finite integrals

An independent bounded-arithmetic finite calculation gives
\[
\boxed{I_{40}(4)>127,\qquad I_{40}(16)>168/5}.
\]

Details of the reproducible certificate are in PREFIX1037_R6_CRITICAL_SPECTRUM_CERT.py and its generated .json:

* On each of 40 unit intervals, apply 16-node Gauss–Legendre quadrature. Proposed nodes \(q_i\) are finite-decimal rationals. Verify with exact Fraction Legendre recurrence \(P_{16}(q_i-10^{-50})P_{16}(q_i+10^{-50})<0\), 16 disjoint brackets, \(|q_i|<.99\), and \(|P'_{16}(q_i)|>13/4\). This isolates all 16 true roots without trusting the root proposer.
* At these rational nodes, evaluate \(J_0,J_1,J_2\) by 310 terms of their standard alternating Bessel series at 130 Decimal significant digits. On \(|x|\le160\), exact integer checks \(80^{620+\nu}10^{90}<310!(310+\nu)!\) for ν=0,1,2, together with the next-term ratio <1/14, bound the series tail by \(2\cdot10^{-90}\). Absolute series sum ≤\(I_\nu(160)\le e^{160}<10^{70}\); elementary Decimal relative-roundoff accumulation across fewer than 2000 operations per Bessel value bounds error <\(10^{-50}\). After kernel and weight arithmetic, the total Decimal/series error in the finite quadrature is <\(10^{-30}\).
* The Fourier angular representation of integer Bessel functions gives \(|J_\nu^{(m)}|\le1\). Thus for λ=6+r the product \(J_0(t)^6J_\nu(rt)\) has m-th derivative bounded by λ^m. Remove the apparent division at zero using \(J_2(rt)/t=r\int_0^1 J_2'(rts)\,ds\). The following global bound for \(0\le t\le40\) follows by Leibniz:
\[
B_{y,m}=\frac15\left[|A|(40\lambda^m+m\lambda^{m-1})
+(H/r)(1600\lambda^m+80m\lambda^{m-1}+m(m-1)\lambda^{m-2})
+12(11+y)r(|y-6|+2y)\lambda^m\right].
\]
Terms with negative exponents at m=0 are omitted. The exact 16-point Gauss error per unit interval is ≤\((16!)^4 B_{y,32}/(33(32!)^3)\). The Fraction checker proves the sum over all 40 intervals is <\(10^{-12}\) for both y values.
* Bracket width \(10^{-50}\), bounds \(|P'_{16}|\ge3,\ |P''_{16}|\le16^4,\ 1-x^2>1/51\), give \(|w'(x)|<10^6\) for \(w=2/[(1-x^2)(P'_{16})^2]\) and \(|w|<12\). Here \(|K|<9\cdot10^6\), \(|K'|<9\cdot10^7\) on [0,40]. Therefore root/weight displacement contributes <\(10^{-30}\). Taken together these explicit bounds certify the two rational inequalities.

Computed complete finite sums (not precision claims on all displayed digits):
\(I_{40}(4)=127.2574809808838554\ldots\),
\(I_{40}(16)=33.6398737785673677\ldots\).
Checker status: all assertions passed; JSON SHA-256 9fa3c0eeda5853b31d6b29cc9626e6ca5feffd8064a5ca6a0f01e33fd3e21623.

## Corollary — strict positivity at both interior critical values

Apply Theorem A at T=40 and use only \(\pi>3\), \(\sqrt\pi>5/3\), \(\sqrt{40}>6\), \(\sqrt2<3/2\):
\[
g(4)>127-\frac{3072(3/2)}{45\cdot6}-\frac{900}{40\cdot6}
=\frac{6371}{60}>100;
\]
\[
g(16)>\frac{168}{5}-\frac{3840}{45\cdot6}-\frac{2200}{40\cdot6}
=\frac{919}{90}>10.
\]

These are rigorous conditional consequences of the inherited derived-scalar Bessel representation. **They are not a proof of full-interval \(g\ge0\), native signed-BRC positivity, or the open mother question \(B_{\rm fix,odd}(32)\in\{19,20\}\).**

## Next open problems

1. Independently audit the scalar reduction PREFIX-1033/1036 and the observer/type map from frozen native X6–BRC input. The current proof remains dependent on that exact premise.
2. Use effective local bounds and the Picard–Fuchs/Frobenius system to certify explicit positive open neighborhoods around y=4,16.
3. Enclose the sign of g across all remaining compact subintervals, using exact interval ODE propagation or directly bounded Bessel quadrature; seek an exact negative witness if one exists.

Attribution: previous work retained under historical EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056, not claimed as current-session authentication. This portable author proof does not establish a formal Task CLAIM, PROGRESS, independent review, Working Truth, or a P000 change.
