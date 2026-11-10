# PREFIX-666-R6 — A 16-fold BRC boundary-strip enlargement by signed Taylor–Bernstein jets

Date: 2026-11-10 (Asia/Shanghai). Researcher-ID: EM-DIRECT-4D0FD7 / TASK_RESEARCH. Activity: RA-FF547EFAD41019F3529D02C5.
Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Model: unchanged PREFIX-665 frozen 189-layer, two-direction BRC first-stop observer.
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Theorem (new local domain)

Write \(\mu=E[Y]\), \(H=E[Y^2]/2\), \(W=2H-\mu^2\), \(V_q=q^2W-q\mu\). For all real
\[
0\le p\le 1/256,\quad 607/4096\le z\le609/4096,\quad 12\le q\le24,
\]
the following strict signed bounds hold:
\[
\mu(p,z)>879/10,\quad \mu_{pp}(p,z)>193,\quad
H_{pp}(p,z)<12855,\quad W_{pp}(p,z)<-8000.
\]
Consequently \((V_q)_{pp}<-8000q^2\).

Using the verified edge hypotheses of PREFIX-660 (unique \(z_*(q)\) and \(V_q(0,z_*)-V_q(0,z)\ge6400000(z-z_*)^2\) on the stated z-band) and PREFIX-661 (\((V_q)_p(0,z)<-76650\) for all \(q\in[12,24]\) and all z in the band), the **unique strip maximum** is
\[
(p_*,z_*)=(0,z_*(q)),\qquad
M_q-V_q(p,z)\ge76650p+4000q^2p^2+6400000(z-z_*)^2.
\]
This is **16 times the area of PREFIX-665**, with the same z-band; the certified gain is local to this strip.

## Exact finite proof

Let \(f_n(k)=A_n(k)/\binom nk\in[0,1]\), where \(A_n(k)\) is the survivor multiplicity in the fixed 189-layer recurrence. With \(s_n(u)=\sum_k A_n(k)u^k(1-u)^{n-k}\), \(t_m(z)=s_m(z)\),
\(w_{nm}=2^{-(n+m+1)}\binom{n+m}{n}\), define
\[
a_n(z)=1-\sum_{m=0}^{188}w_{nm}t_m(z),\quad
b_n(z)=n+1-\sum_{m=0}^{188}\frac{n+m+1}{2}w_{nm}t_m(z).
\]
The previously established maximum-of-two-Gamma-clocks identity gives
\[
\mu=\sum_{n=0}^{188}a_n(z)s_n(p)+\sum_{m=0}^{188}t_m(z),\quad
H=\sum_{n=0}^{188}b_n(z)s_n(p)+\sum_{m=0}^{188}(m+1)t_m(z).
\]
Thus \(0\le a_n\le1\) and \(0\le b_n\le n+1\). Put \(Q=19/128\), \(\delta=1/4096\), \(\varepsilon=1/256\), \(K=12\), \(R=14\). Exact binomial differentiation yields
\[
s_n^{(r)}(0)=n^{\underline r}\Delta^r f_n(0),\qquad
\big|s_n^{(r)}(u)\big|\le2^{r-1}n^{\underline r}\quad(r\ge1,\;0\le u\le1).
\]
For each \(n\) the computable bound
\[
L_n=\sum_{j=0}^{K-1}\frac{\varepsilon^j}{j!}|s_n^{(j+2)}(0)|
+\frac{\varepsilon^K}{K!}2^{K+1}n^{\underline{K+2}}
\]
therefore encloses \(|s_n''(p)|\) for every \(p\in[0,\varepsilon]\). It is crucial to retain the **signed, exact low-order jets** before applying the absolute-value bound to the remainder.

The binomial score estimate \(|t_m'(z)|\le\frac12\sqrt{m/(z(1-z))}<21\) holds throughout the z-band for \(m\le188\). Negative-binomial moment identities give
\[
|a_n'|\le21,\quad |b_n'|\le21(n+1),\quad
|a_n''|\le2(n+1)(n+2),\quad
|b_n''|\le2(n+1)(n+2)(n+3).
\]
In particular, the exact rational sums \(Z_\mu=\sum_n2(n+1)(n+2)L_n\) and \(Z_H=\sum_n2(n+1)(n+2)(n+3)L_n\) bound \(|\mu_{ppzz}|\), \(|H_{ppzz}|\).

Calculate the signed center jets of \(\mu,H,\mu_z,H_z\) through order \(R-1\), and bound their order-\(R\) Taylor remainders in \(p\) using \(2^{R-1}\sum_n n^{\underline R}\) (respectively with \(n+1\) for \(H\)); for \(\mu_z,H_z\) multiply by the score factor 21. Two-stage Taylor expansion, first from \(p=0\) to \([0,\varepsilon]\), then from \(z=Q\) to \([Q-\delta,Q+\delta]\), gives *exact rational* enclosures
\[
\mu_{pp}>193,\qquad H_{pp}<12855.
\]
The certificate prints the complete rational envelope values.

Because \(\mu_{pp}>0\), \(\mu_p(p,z)\ge\mu_p(0,z)\). At \(p=0\), only \(n<25\) survive in the first direction, so
\[
|\mu_z(0,z)|\le21(189+25),\quad
|\mu_p(0,z)-\mu_p(0,Q)|\le21\delta\sum_{n=0}^{188}n.
\]
These estimates and the exact center mean give \(\mu>879/10\). Finally,
\[
W_{pp}=2H_{pp}-2\mu_p^2-2\mu\mu_{pp}
<2(12855)-2(879/10)(193)<-8000.
\]
Integrate \(V_{q,pp}<-8000q^2\) and the PREFIX-661 boundary slope; add the PREFIX-660 edge gap to prove the maximum/stability statement.

## Computation and reproducibility

Companion \`PREFIX666_R6_JET_STRIP_CERTIFICATE.py\` reruns the frozen 189-layer survivor recurrence via the exact PREFIX-665 predicate, constructs the negative-binomial kernels and their z-derivatives, computes the 12th-order p-jet envelopes and all displayed inequalities entirely with Python integers and \`fractions.Fraction\`. Original local run returned \`ALL_CHECKS_PASS 12\`. No floating-point decision is used. The compact JSON companion states the certified rational brackets; the program prints the full exact rational values.

Dependency scope: frozen statistical BRC observer and PREFIX-660/661 edge certificates. The full \([0,1]^2\) variance maximum is the mother objective and remains open. No formal Result, independent review or admission has been asserted.

## Next discriminating unit

Subdivide \(p\in[1/256,1/128]\) into dyadic subintervals, re-center the exact signed derivatives, and build interval-specific \(Z_\mu,Z_H\) bounds rather than reusing a single origin-based absolute envelope. Independently start triangle-wise Bernstein upper-bound pruning against the latest boundary candidate. Preserve the unchanged frozen science pin and current Source ownership on any formal return.
