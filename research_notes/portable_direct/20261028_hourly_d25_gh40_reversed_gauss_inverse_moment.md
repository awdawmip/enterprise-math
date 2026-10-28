# D25/LIFT GH-40: exact reverse-Gauss high tail at inverse argument

2026-10-28, TASK_RESEARCH author derivation, exact locally tested; UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION OPEN, task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. This reuses GH-39, not its unproved congruence. Scientific frozen Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 and ACTIVE P000 unchanged.

For prime p=4d+3>=7, over F_p retain GH-39 a_0=1 and
\[
a_{r+1}/a_r=(8r+1)^2/[16(4r+3)(r+1)],\quad
B_d(z)=\sum_{r=0}^da_rz^r.
\]
Its genuine high-degree source tail is
\[
E_d(z)=\sum_{n=d+1}^{2d}(8n+1)[x^n]B_d(x)^2z^n.
\]
Define an independent REVERSED sequence, with all denominators invertible,
\[
\beta_0=1,\qquad\beta_{r+1}/\beta_r=
16(r+1)(4r+3)/(8r+13)^2,\quad 0\le r<d.
\]
A zero denominator would require p=5 mod8, impossible for p=3 mod4. Let
\[
V_d(u)=\sum_{r=0}^d\beta_ru^r,\quad
v_r=[u^r]V_d(u)^2,\quad
W_{d-1}(u)=\sum_{r=0}^{d-1}(8r+11)v_ru^r.
\]

**THEOREM GH-40 (proved, all specified primes).**
\[
\boxed{a_{d-r}=a_d\beta_r \ (0\le r\le d),\qquad
E_d(z)=-a_d^2z^{2d}W_{d-1}(z^{-1})\ (z\ne0).}
\]
At z=9, since 2d=(p-3)/2 and 9 is a nonzero square,
\[
\boxed{E_d(9)=-a_d^2 W_{d-1}(1/9)/9.}
\]
Consequently the original OPEN GH-3 target is equivalently
\[
T_d(9)=B_d(9)(B_d(9)+16\theta B_d(9))
+a_d^2W_{d-1}(1/9)/9\stackrel{?}=0.
\]
The equality to T is proved, NOT its desired vanishing.

PROOF. Reverse the Gauss recurrence:
\[
\frac{a_{d-r-1}}{a_{d-r}}
=\frac{16(4(d-r-1)+3)(d-r)}{(8(d-r-1)+1)^2}
=\frac{16(r+1)(4r+3)}{(8r+13)^2}\pmod p.
\]
The first equality is a literal reciprocal of the forward recurrence; the second uses 4d+3=0 in F_p. Hence beta_r=a_{d-r}/a_d. Ordered pairs (i,j) with i+j=2d-r are in bijection with pairs (d-i,d-j) whose sum is r. Therefore
\[
[x^{2d-r}]B_d(x)^2=a_d^2v_r
\]
for 0<=r<d; no signed term or multiplicity is lost. Also 8(2d-r)+1=-(8r+11) mod p. Reindex E_d by n=2d-r to obtain the displayed inverse-polynomial identity. Finally, 9^{2d}=9^{-1} by Euler's criterion. QED.

The companion reverse series has the exact truncated hypergeometric representation
\[
V_d(u)=\left[{}_3F_2(1,1,3/4;13/8,13/8;u)\right]_{\le d}.
\]
This moves the distinct high tail to a **low-degree inverse-point** moment u=1/9, but does not evaluate that moment independently or solve T_d(9)=0.

EXACT EVIDENCE: The companion pure-Python standard-library code has been run for every one of the 154 primes 7<=p<2000, p=3 mod4. Checks include coefficientwise reversed Gauss recurrence, ordered-pair convolution, high-tail inversion and 9^{2d}=9^{-1}. (p; a_d,W(1/9),E(9)) samples: (19;9,5,12), (43;14,11,28), (67;54,6,66). Finite checks support the algebra but are not theorem admission, native X6 execution or independent replication.

BRC COMPOSE_APPLIED: the source map (i,j)->(d-i,d-j) is a provenance-preserving bijection on exact signed F_p terms. All rank, source, multiplicity, forward/reverse direction, modulus, weighted observer and index cutoff are kept. It grants no transfer into P000's native X6 geometry or the original W/S six Hasse ports.

NEXT: derive a genuinely independent finite-field/CM/Frobenius or nonlocal WZ special-value certificate for the inverse moment W_{d-1}(1/9) (first for p=19 mod24), preserving the cutoff and sign; do not count this algebraic reversal as vanishing. Continue GH-20/21 next-digit, GH-5 S, R23/R36 Green, six original Hasse ports, [X]U mod p^2, eta/kappa, native p=373 and independent Driver review when authorized. No service session, CLAIM, OPEN, Source checkpoint, freeze or admission was created by this evidence.