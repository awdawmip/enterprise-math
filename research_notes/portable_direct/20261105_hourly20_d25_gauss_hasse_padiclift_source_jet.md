# D25 — Gauss–Hasse mod p² carry and the indispensable first-jet port

Date: 2026-11-05. Lane: TASK_RESEARCH, author-side portable; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. AUTHOR-DERIVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED. No native H0/B0 run or new Source checkpoint.

## Definitions and theorem (prior finite three-band lemma used)

Let p=8q+5 be prime >=5, m=(p-1)/2, ell=(5p-1)/8, d=4ell=(5p-1)/2. Work over the p-local rationals and reduce as stated. Put
\[
a=t^2-6t+1,\quad n=16t(1-t)^2,\quad h=(1+t)^4,\quad x=n/h,\quad Q=t^4-140t^3+294t^2-140t+1,
\]
\[
f_k={(1/8)_k(3/8)_k\over(k!)^2},\quad
F_p(x)=\sum_{k=0}^{\ell}f_kx^k,\quad
H_m(t)=\sum_{j=0}^{m}{m\choose j}^2t^j,\quad
B_p(t)=\sum_{k=0}^{\ell}f_kn^kh^{\ell-k}.
\]
All k <= ell < p have p-free denominators, so B_p is p-integral, of formal degree d. The prior author-side three-band theorem yields
\[
B_p\equiv a^pH_m\pmod p\quad\text{in }\mathbb F_p[t].
\]
The exact coefficientwise one-digit carry is therefore
\[
\boxed{S_p=(B_p-a^pH_m)/p\bmod p\in\mathbb F_p[t].}\tag{1}
\]
To compute it, generate f_0=1 and f_k=f_{k-1}(8k-7)(8k-5)/(64k^2) modulo p². The polynomials n,h are reciprocal of formal degree 4, a of degree 2, and H_m of degree m; as 2p+m=d, both summands in (1) are reciprocal of degree d. Therefore
\[
\boxed{t^d S_p(t^{-1})=S_p(t).}\tag{2}
\]
Directly expanding their linear terms gives
\[
[t](B_p-a^pH_m)/p=(4\ell+3/4-m^2+6p)/p=(36-p)/4,
\]
so S_p(0)=0, [t]S_p=9 mod p, and S_p is nonzero for every specified prime.

Define L(t)=16t(1-t²), c(t)=1+2t-7t² and \(\mathcal D=L\partial_t+c\). For any reciprocal V of formal degree r,
\[
t^{r+2}(\mathcal D V)(t^{-1})-(\mathcal D V)(t)
=8(2r+1)(t^2-1)V(t).
\]
For r=d, 2d+1=5p; hence the carry jet is reciprocal modulo p:
\[
\boxed{t^{d+2}(\mathcal D S_p)(t^{-1})=(\mathcal D S_p)(t)\pmod p.}\tag{3}
\]
Thus this carry derivative has reciprocal parity, unlike the known uncorrected Hasse second-digit inversion anomaly 8(t²−1)H_m.

## Exact denominator-free p² jet source

Set C_m=\mathcal D H_m. From B_p=a^pH_m+pS_p (mod p²) and the product rule:
\[
\boxed{a^{p+1}C_m=a\mathcal D B_p-p\{a\mathcal D S_p+L a'B_p\}\pmod{p^2}.}\tag{4}
\]
One must differentiate S_p *before* reducing modulo Q. The p-multiplied terms need any polynomial lift of S_p mod p. There are no p-denominators or infinite-series expansion in (4).

The exact fiber identity 9n-h=-Q gives x=1/9 mod Q. Also Lx'=16xa, so Lx'=16a/9 mod Q. Using B_p=(1+t)^d F_p(x), formula (4) at the fiber becomes in \(R_p=(\mathbb Z/p^2)[t]/(Q)\):
\[
\boxed{\begin{aligned}
a^{p+1}C_m
={}&(1+t)^{d-1}\left[
\frac{16a^2(1+t)}9F'_p(1/9)
+a\{c(1+t)+dL\}F_p(1/9)\right]\\
&-p\left[a\mathcal D S_p+La'(1+t)^d F_p(1/9)\right]
\pmod{(p^2,Q)}.
\end{aligned}}\tag{5}
\]
It explicitly retains the F value, derivative, finite Frobenius carry and prefactor derivative, with the inversion branch as an independent label. At split p≡5 mod24, the previous author CM-selection result implies Q|C_m mod p; the coefficientwise quotient of (5) by p gives the second digit a^{p+1}T_p, where T_p=(C_m mod Q)/p mod p. Formula (5) is an exact source interface, *not* an established cancellation with Jacobi W(1) or with frozen native \(\Delta_p-R_p\).

## Nonrecoverability of the carry derivative from values alone

The pair S and S+Q have the same reduction modulo Q, but (\mathcal D(S+Q)-\mathcal DS) mod Q=LQ' mod Q. This is nonzero and invertible modulo (p,Q): Q has discriminant supported only at 2 and 3, and Q(0)=1,Q(1)=16,Q(-1)=576, so Q' and L are units at its roots for p>=5. More strongly, even fixing reciprocity of formal degree d and both constant and linear coefficients, the alternative
\[
S^*=S+Q\,t^2(1+t)^{d-8}
\]
has the same value mod Q and those properties, but different derivative modulo Q by the unit LQ't²(1+t)^{d-8}. Thus the value-only quotient is not sufficient for (5). Preserve (S mod Q,S' mod Q) or an equivalent two-port observer. This is a concrete BRC information-retention result in an *auxiliary* classical ring, not a native six-axis proof.

## Exact verification and remaining work

The accompanying pure-stdlib Python checker constructs B_p and a^p H_m independently modulo p²; verifies divisibility by p, reciprocity of S_p and \(\mathcal DS_p\), coefficientwise polynomial formula (4), and fiber formula (5) in the quartic quotient ring. PASS on p=5,13,29,37,53,61,101,149,173,197 (seven split, three inert). At p=5: [t]S=4, C_2 mod (25,Q)=15+10t, T_5=(3,2,0,0), a^6 C_2 mod (25,Q)=5+20t, \(\mathcal D S_5\bmod(5,Q)=(4,2,4,0)\). At p=29 and 53 the second-digit vectors are (17,8,16,17) and (49,21,2,24). Finite exact checks corroborate the statements; the universal proof of (4) is direct algebra and (1)-(3) use the earlier author three-band lemma.

Next scientific unit: construct the *finite Euler/Jacobi second-digit difference* and compare the two labeled p² ports (F,F'; S,S') to the existing short Jacobi W(1), retaining inversion sign and exact truncation. Prove a same-prime equality or an explicit counterexample. Frozen original-class p373 H0/B0 module, [X]U mod p², eta/kappa, semilinear direction, Delta-R and independent review remain separately outstanding.

Author-side evidence only: no CLAIM, OPEN, canonical Source checkpoint, Result, reviewer admission or P000 promotion.