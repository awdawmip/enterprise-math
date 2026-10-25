# D25/LIFT — exact terminal Jacobi jet factorization and third-digit forcing

Date: 2026-10-25. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Research lane TASK_RESEARCH (portable author derivation). Frozen scientific source pin: c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CHECKPOINT. Mother D25/LIFT/JT2 OPEN.

## Minimal unrepeated question

The previously saved endpoint-jet result (research_notes/portable_direct/20261025_hourly_d25_terminal_jacobi_jet_universal_forcing.md) proved the terminating second-Jacobi-jet forcing coefficient is -4 modulo p and is -2 after evaluation at z=1/2. Determine the source-preserving *next two p-adic digits* of this nonhomogeneous forcing, without replacing the polynomial z^p by its finite-field point readout z before further differential operations.

For every prime p=6m+1>=7, let N=p-1 and

\[
b_n(x)=\frac{(-x)_n(-2x)_n}{(n!)^2},\quad
F_i(z)=\left.\partial_x^i\sum_{n=0}^{N}b_n(x)z^n\right|_{x=m},
\quad
w_N=\tfrac12b_N''(m).
\]
Set \(\theta=z\,d/dz\) and \(\mathcal L_m=\theta^2-z(\theta-m)(\theta-2m)\). The *exact rational* differential equation from the predecessor is
\[
\mathcal L_m F_2+2z(3\theta-4m)F_1-4zF_0=K_pz^p,\qquad
K_p=-40m^2w_N.
\]

## Theorem: all-source exact product and mod p^3 expansion

Let \(a=m+1\), \(b=2m+1\), and define the p-integral rational harmonic quantities
\[
H_n=\sum_{j=1}^n j^{-1},\qquad H_n^{(2)}=\sum_{j=1}^n j^{-2},
\]
\[
A_p=H_a+H_b-\frac{27}{10},\qquad
B_p=\frac{A_p^2+H_a^{(2)}+H_b^{(2)}}2-\frac{171}{200}.
\]
All denominators are p-units (a,b<p and p>=7). Then the endpoint coefficient has the **exact rational factorization**
\[
\boxed{\quad
K_p=-4\frac{(1-p)^2}{(1+p/5)(1+p/2)}
\prod_{j=1}^{a}(1-p/j)^{-1}
\prod_{j=1}^{b}(1-p/j)^{-1}.\quad}
\tag{1}
\]
Consequently, in the p-local ring,
\[
\boxed{\quad K_p\equiv-4\,[1+pA_p+p^2B_p]\pmod{p^3}.\quad}
\tag{2}
\]
Define the **integer** Fermat quotient \(q_p(2)=(2^{p-1}-1)/p\). At the actual D25 observer \(z=1/2\), the exact forcing value \(J_p=K_p2^{-p}\) obeys
\[
\boxed{\quad
J_p\equiv-2\left[
1+p(A_p-q_p(2))
+p^2(B_p+q_p(2)^2-A_pq_p(2))
\right]\pmod{p^3}.\quad}
\tag{3}
\]
In particular the second-digit terms differ before and after readout by the necessary \(-q_p(2)\) correction; the previous \(-4\) polynomial / \(-2\) observer statements are precisely the reductions modulo p of (2)/(3).

**No commutation shortcut.** Over \(\mathbb F_p\), point evaluation yields \(z_0^p=z_0\), but \(\theta(z^p)=pz^p\equiv0\pmod p\) whereas \(\theta z=z\). Therefore the replacement \(z^p\rightsquigarrow z\) is not safe if later differential operators are permitted, even though it preserves every \(\mathbb F_p\)-valued point observer. The exact polynomial forcing \(K_pz^p\) and the number \(J_p\) are distinct, explicitly typed output ports.

## Proof

The predecessor proved
\[
w_N=\frac{2(-1)^m m!(2m)!(5m-1)!(4m-1)!}{((6m)!)^2}.
\]
For \(0\le k<p\), the following is an exact rational factorial-complement identity (not merely a congruence):
\[
(p-1-k)!=\frac{(-1)^k(p-1)!}{k!}\prod_{j=1}^{k}(1-p/j)^{-1}.
\]
Apply it with \(k=m+1\) and \(k=2m+1\). The combined sign is
\((-1)^{m+(m+1)+(2m+1)}=(-1)^{4m+2}=1\), and both occurrences of \((p-1)!\) cancel. Hence
\[
w_N=\frac{2}{(m+1)(2m+1)}
\prod_{j=1}^{m+1}(1-p/j)^{-1}
\prod_{j=1}^{2m+1}(1-p/j)^{-1}.
\]
Substitution into \(-40m^2w_N\), with \(m=(p-1)/6\), gives exactly
\(-40(p-1)^2/[(p+5)(p+2)]\) times the product, equivalent to (1).

Each factor \(1-p/j\) is a unit in the p-local ring, and a finite product of such factors can be expanded through order p^2. For a formal variable t to second order, the logarithm of the product in (1), omitting the constant -4, is
\[
2\log(1-t)-\log(1+t/5)-\log(1+t/2)
-\sum_{j\le a}\log(1-t/j)-\sum_{j\le b}\log(1-t/j)
\]
\[
=t\left(H_a+H_b-\frac{27}{10}\right)+t^2\left[\frac12(H_a^{(2)}+H_b^{(2)})-\frac{171}{200}\right]\pmod{t^3}.
\]
Exponentiating (valid in this truncated p-local expansion since p>=7) supplies the additional \(A_p^2/2\) term and proves (2). Since \(2^{p-1}=1+pq_p(2)\) **exactly** and \(2^{-p}=\frac12(1+pq_p(2))^{-1}\), multiplying (2) by the inverse \(1-pq_p(2)+p^2q_p(2)^2\) proves (3). No unproved infinite-p expansion or denominator divisible by p is used.

## Exact author checks, reproducibility and limitations

Adjacent reproducible Python standard-library checker verifies (i) the factorial-source value of w_N and K_p against (2), (ii) the independent finite-field D25 observer K_p/2^p against (3), and (iii) the mod-p reductions. It passed all 35 primes \(p\equiv1\bmod6\) with \(7\le p\le373\), plus 1327 and 19963 (37 prime cases); a separate exact Fraction path confirmed the rational product equality for p=7,13,19. Selected residues, written as (p, K_p mod p^3, J_p mod p^3):

- (7, 122, 285)
- (13, 1218, 1701)
- (19, 224, 3836)
- (373, 11695038, 16851765)
- (1327, 2255537725, 280891396)
- (19963, 3899095883223, 2519162671242)

Author-exact checks do not establish independent review; the general statement follows from the displayed algebra. This is a p-local **auxiliary hypergeometric** result, not an authenticated original-class CM/divided-power computation or proof of the hard LIFT congruence. Its use of z and algebraic parameters is an external formal auxiliary representation, not a declaration of an Enterprise native plane, native 2D/3D reduction, or a transfer theorem for the P000 X6 world.

BRC resolution: COMPOSE_APPLIED. The carrier retains terminal rank N, its double-zero second parameter jet, factorial provenance, signed inhomogeneous differential operator, precision p^3, and two noninterchangeable ports (polynomial \(z^p\); evaluated \(2^{-p}\)). Compressing to the mod-p observation alone would delete the harmonic and Fermat-quotient residuals needed for later high-precision differentiation/Clausen combination.

## Durable continuation (minimal, not a native checkpoint)

Mother question: D25/LIFT/JT2 all-target-prime signed congruence, still OPEN. Previous first/second-jet, Clausen-reflection and moment-closure notes remain separate durable inputs, not prior native completed_units. Do-not-repeat: previous \(-4\bmod p\), \(-2\bmod p\), the all-order ordinary moment closure, and finite-prime sampling alone. The newly proved full second/third-digit terminal coefficient enables the next exact unit: insert its \(K_pz^p\) source port into the finite Jacobi-jet/reflected-corner signed operator, then attempt a uniform, source-preserving telescoping identity for \(B_{01,p}+A_2H_0/72-T_{\rm jet,p}\); if a point observer is used, carry (3), not just -2. Still required: authentic CM \(H_0/B_0\), \([X]U\bmod p^2\), Frobenius normalization/direction and native \(\kappa\), independent review, current Source-authorized claim/run and durable checkpoint. No maintenance session or other owner can be substituted for the Research lane. Research logical ID: chatgpt-research-hourly-enterprise-math-20260923; native session/claim ownership must be rechecked against Source before any formal write.
