# EC49FTS — Prior-score identity and nonlinear correlated ridge-prior stochastic order

**Date:** 2026-11-19. **Scientific status:** AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED.

**Scientific origin:** The native BRC16943 228-observer/141-profile optimum is inherited from frozen scientific input awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab and author-proved EC49FTH PR #2774@999bf1069403306b3813e0e390dae4435d7b4b8c. The external price-prior fiber and mixed TP2/top-atom criterion are inherited from EC49FTR PR #2795@6e6da57541f965b0c02c27ceed97daddff2e1417. **This unit studies external price-prior postprocessing; it does not rerun or promote the native BRC proof, replace P000, or establish native heartbeat dynamics.**

## 1. Exact high-gap model and coordinates

Consider prices \(a\in[3/4,49/64]\), \(b\in[7/16,57/128]\), with a strictly positive joint density \(h(a,b)\), normalized by any common positive factor. In the inherited high-gap sector
\[
I=(1469/64,187/8),\qquad m=M=\max_z(D-S),
\]
the nonclipped optimizer \(Z\) has lower endpoint \(L(m)=(8m+173)/480\), upper endpoint \(U=3/4\), and (unnormalized) continuous density
\[
K_h(m,z)=\frac{16}{945}h\left(\frac{47-m}{945}+\frac{44z}{45},
  \frac1{27}-\frac m{54}+\frac{10z}{9}\right),\quad L(m)<z<U.
\]
The clipped contribution (a conditional atom at \(Z=U\)) is
\[
B_h(m)=\frac1{54}\int_{x(m)}^{49/64} h(a,b_m)\,da,\quad
 x(m)=\frac{740-m}{945},\quad b_m=\frac{47-m}{54}.
\]
Write \(A_h(m)=\int_{L(m)}^U K_h(m,z)\,dz\), and \(r_h(m)=B_h(m)/A_h(m)\). The inherited EC49FTR theorem states that for positive TP2 \(K_h\), with nondecreasing \(L\), \(Z|M=m\) increases in first-order stochastic order iff \(r_h\) is nondecreasing.

The following reduction expresses \(r_h\) **directly in the joint price prior**, without integrating an optimizer kernel. Define
\[
\phi_m(b)=\frac3{175}+\frac{8m}{525}+\frac{22b}{25},\quad
C(m)=\int_{7/16}^{b_m}h(\phi_m(b),b)\,db,\quad
D(m)=\int_{x(m)}^{49/64}h(a,b_m)\,da.
\]
The change of variables \(b=1/27-m/54+10z/9\) sends \(z=L(m)\) to \(b=7/16\), \(z=U\) to \(b=b_m\), and \(a\) to \(\phi_m(b)\). Consequently,
\[
A_h(m)=\frac8{525}C(m),\qquad B_h(m)=\frac1{54}D(m),\qquad
\boxed{r_h(m)=\frac{175}{144}\frac{D(m)}{C(m)}.}
\]
All integrals are strictly positive on \(I\), and \(\phi_m(b_m)=x(m)\).

## 2. Exact prior-score identity

Assume \(h\) is positive \(C^1\). Let \(H(m)=h(x(m),b_m)\). Leibniz' rule gives
\[
C'(m)=-\frac{H(m)}{54}+\frac8{525}
 \int_{7/16}^{b_m}h_a(\phi_m(b),b)\,db,
\]
\[
D'(m)=\frac{H(m)}{945}-\frac1{54}
 \int_{x(m)}^{49/64}h_b(a,b_m)\,da.
\]
Thus the following is a **necessary and sufficient local criterion** for \(r_h\) to be nondecreasing wherever its derivative exists:
\[
\boxed{
\frac{d}{dm}\log r_h
=\frac{H}{945D}+\frac{H}{54C}
-\frac1{54}\frac{\int_{x(m)}^{49/64}h_b(a,b_m)\,da}{D}
-\frac8{525}\frac{\int_{7/16}^{b_m}h_a(\phi_m(b),b)\,db}{C}
\ \ge 0.
}
\]
The two integrals divided by \(D,C\) are precisely conditional averages of the prior's coordinate scores \(\partial_b\log h\) and \(\partial_a\log h\), respectively. This is an exact prior-level, one-dimensional criterion. It is not an additional hypothesis or restatement of TP2.

**Corollary (coordinatewise decreasing priors).** If \(h_a\le0\), \(h_b\le0\) throughout the price box, then \(D'>0\), \(C'<0\), and \(r_h'>0\) throughout \(I\); the strictly positive edge terms force strictness. If in addition the pullback continuous kernel \(K_h\) is TP2, the full mixed distribution \(Z|M=m\) is strictly increasing in first-order stochastic order on \(I\). This condition is stated on the *prior* itself and includes nonproduct joint priors.

## 3. An infinite correlated nonlinear ridge family

Let \(h(a,b)=\rho(a+b)\), where \(\rho\) is strictly positive, \(C^2\), nonincreasing and log-concave on
\[
a+b\in [19/16,155/128].
\]
Then \(h_a=h_b=\rho'(a+b)\le0\), so the prior-score criterion gives \(r_h'>0\). Moreover, set
\[
u(m,z)=a(m,z)+b(m,z)=\frac{82}{945}-\frac{37m}{1890}+\frac{94z}{45}.
\]
The continuous-kernel log cross derivative is
\[
\frac{\partial^2}{\partial m\,\partial z}\log K_h(m,z)
=-\frac{37}{1890}\frac{94}{45}(\log\rho)''(u(m,z))\ge0,
\]
because \((\log\rho)''\le0\). Hence \(K_h\) is TP2 and **for every such ridge prior, the full mixed conditional law \(Z|M=m\) is strictly stochastically increasing on the high-gap sector \(I\)**. If \((\log\rho)''<0\), the continuous kernel is strictly TP2. A nonexponential ridge is generally a genuine nonproduct correlated prior.

Examples: \(\rho(s)=\exp(-\lambda s^2)\) for \(\lambda>0\), and the exact polynomial \(\rho(s)=(3-s)^2\). These involve no independence assumption on \(a,b\).

## 4. Fully rational nonlinear nonproduct witness

Take \(h(a,b)=(3-a-b)^2\) on the price box, then normalize as a probability density. Since \(a+b\le155/128<3\), this density is strictly positive, coordinatewise decreasing and strictly log-concave along the sum. It is nonproduct because \(h h_{ab}-h_a h_b=-2(3-a-b)^2<0\).

Under the inherited entire-box optimizer \(Z=\min\{3/4,(105a-6b-5)/96\}\), the clipped event is exactly
\[
Z=3/4\iff a\ge a_c(b),\qquad a_c(b)=\frac{77+6b}{105}.
\]
Direct exact integration of the *joint prior* yields
\[
\int_{7/16}^{57/128}\int_{3/4}^{49/64}h\,da\,db
=\frac{4981}{12582912},
\]
\[
\int_{7/16}^{57/128}\int_{a_c(b)}^{49/64}h\,da\,db
=\frac{66463162673}{372897113702400}.
\]
Therefore the **global optimizer saturation probability** is
\[
\boxed{\Pr_h(Z=3/4)=\frac{66463162673}{147612931200}\approx0.45025298348.}
\]
This is an all-box probability; the stochastic-order theorem itself is stated on \(I\).

For an exact high-gap CDF witness, at \(p=23<q=93/4\) and \(t=719/960\), full polynomial-fiber integration gives
\[
F_p(t)=\frac{142919525557120}{375702410965173},\qquad
F_q(t)=\frac{257409057608064}{2434591469005301},
\]
and
\[
\boxed{F_p(t)-F_q(t)=
\frac{251241454128026688021270338048}
{914681884620533840389663382073}>0.}
\]
The rational checker also verifies strictly positive 2-by-2 TP2 minors at five independent rational interior rectangles. The **all-real** conclusion follows from Sections 2–3, not from those finite checks.

## 5. Evidence, provenance, and open frontier

A standard-library Fraction verifier re-integrates all displayed polynomial-fiber and joint-probability integrals, verifies exact rational identities and the strict CDF ordering. The new derivation uses the inherited high-gap native Bellman author theorem as an explicit parent; that theorem is NOT_REVIEWED. This EC49FTS result is independently reasoned and author-verified, also NOT_REVIEWED.

Further research: (i) classify wider nonlinear joint priors where the score identity remains nonnegative without coordinatewise decrease; (ii) identify the sharp prior-parameter boundary where this balance changes sign; (iii) independently extend original-index native BRC Bellman strategy cells below \(z=11/16\), using the frozen native input and actual 228-observer verification when available.

No formal task CLAIM, native Activity association, Source Result/Review, or canonical-main merge is inferred from this publication.
