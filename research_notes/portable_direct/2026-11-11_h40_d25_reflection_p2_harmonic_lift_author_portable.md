# D25/LIFT — harmonic p-adic reflection lift to mod p²

**2026-11-11 · TASK_RESEARCH author-side evidence · AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.**

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains open. Frozen scientific input: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3. The p-modulus reciprocity at commit 4f13bd606e89c465060780e49ab4c02f19f621fe is reused, not claimed anew.

## Theorem: two-digit normalized reflected product

For any prime p>3, integer 1≤k<p, set
\[
a_k=\frac{(2k)!(3k)!}{216^k(k!)^5},\quad
q_2=\lfloor2k/p\rfloor,\quad q_3=\lfloor3k/p\rfloor,\quad
r_2=2k-pq_2,\quad r_3=3k-pq_3.
\]
For 0≤n<p let \(H_n=\sum_{i=1}^n i^{-1}\in\mathbb F_p\), and let \(Q_p(216)=(216^{p-1}-1)/p\bmod p\). Then:
\[
\boxed{
\frac{a_k a_{p-k}}{p^3}\equiv
-\frac{(-1)^{q_2+q_3}\,q_3!(2-q_3)!}{36k^3}
\left[1+p\left(2H_{r_2-1}+3H_{r_3-1}-5H_{k-1}-Q_p(216)\right)\right]\pmod{p^2}.
}
\tag{R2}
\]
The left side is p-adically integral since \(v_p(a_k)+v_p(a_{p-k})=3\). All base fractions are read modulo \(p^2\), with unit denominators; the bracket correction is read modulo p.

## Proof

Put \(w_p=((p-1)!+1)/p\). For 0≤q≤2, 0≤r<p, the factorial block decomposition, using \(H_{p-1}=0\bmod p\), gives
\[
\frac{(qp+r)!}{p^q}\equiv (-1)^q q!r!\,[1+pq(H_r-w_p)]\pmod{p^2}. \tag{1}
\]
Wilson and the final reverse block give, for 1≤r<p,
\[
r!(p-r)!\equiv(-1)^r r\,[1+p(H_{r-1}-w_p)]\pmod{p^2}. \tag{2}
\]
Apply (1) to 2k,3k,2(p-k),3(p-k). The quotient parts are \(q_2,q_3,1-q_2,2-q_3\), and the partner remainders are \(p-r_2,p-r_3\). Use (2) on each remainder pair and on \(k!(p-k)!\). The Wilson quotient contributions cancel between numerator and the fifth power in the denominator. In \(\mathbb F_p\), \(H_{p-r}=H_{r-1}\) and \(H_r=H_{r-1}+1/r\); the provisional first-order correction is
\[
2H_{r_2-1}+3H_{r_3-1}-5H_{k-1}
+\frac{q_2}{r_2}+\frac{q_3}{r_3}-Q_p(216).
\]
Meanwhile
\[
\frac{r_2r_3}{6k^2}\equiv1-p\frac{3q_2+2q_3}{6k}\pmod{p^2}.
\]
Its correction cancels \(q_2/r_2+q_3/r_3\), because \(r_2\equiv2k\), \(r_3\equiv3k\pmod p\). The remaining sign is \(-(-1)^{q_2+q_3}\), the surviving floor factorial is \(q_3!(2-q_3)!\), and \(216^p\equiv216(1+pQ_p(216))\pmod{p^2}\). This is (R2).

## Corollary: fourth-band reconstruction to p⁵

For the D25 primes p=6m+1, let
\[
F_p^{[2]}=p^{-3}\sum_{k=4m+1}^{6m}(6k+1)a_k\bmod p^2.
\]
Reflecting k=p-j in (R2), with 1≤j≤2m and \(a_j\) a p-unit, yields the exact finite-field precision lift
\[
\boxed{
F_p^{[2]}\equiv \sum_{j=1}^{2m}
\frac{6j-1-6p}{18j^3a_j}
\left[1+pD_p(j)\right]\pmod{p^2},
}
\tag{F2}
\]
where \(D_p(j)=2H_{2j-1}+3H_{3j-1}-5H_{j-1}-Q_p(216)\bmod p\). It uses \(a_j\bmod p^2\); it reconstructs the original fourth band's contribution to \(W_p=\sum_{k=0}^{p-1}(6k+1)a_k\) modulo \(p^5\), one p-adic digit further than the earlier result.

| p | F mod p | second digit | F mod p² |
|---:|---:|---:|---:|
|13|5|5|70|
|19|4|8|156|
|157|96|143|22547|
|373|278|293|109567|

## Exact regression and provenance

Original coefficients are computed by their source recurrence modulo p⁵. For all 312 eligible primes p≤10000 and p≡13,19 (mod 24), all 1,475,586 reflected index pairs satisfy (R2), and all 312 normalized upper-band sums equal (F2). Eleven extra primes outside the eligible classes add 312 pairs; total 1,475,898 checks. Independently computed factorial coefficients for p=5,11,13,19,157,373 agree exactly. No floating-point operations. The local portable package also contains the full 312-prime two-digit certificate and runnable verification code.

This new work is the harmonic correction, the all-prime mod-p² proof, and the p⁵ weighted-band reconstruction. It does not recredit previous base reciprocity, Green/WZ, or UR work. Native Source execution currently lacks the original valid session capability and winning CLAIM; this note is NOT an admitted Result nor a native H0/B0 experiment. Original UR V2 four-file bundle (94,687 bytes, SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76) remains unlocated.

Next: use \(D_p(j)\) in a paired/WZ identity addressing the still-open uniform \(W_p\equiv p\bmod p^3\), or obtain authentic original-class H0/B0 for native Frobenius comparison under separate valid Source authority.
