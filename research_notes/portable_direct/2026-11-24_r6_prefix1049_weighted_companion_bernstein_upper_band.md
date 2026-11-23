# PREFIX-1049 — Weighted companion contraction and Bernstein certificate for the upper spectral band

Date: 2026-11-24 Asia/Shanghai. Parent: PREFIX-1048. Status: AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED.

## Input and result

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; inherited Stage46 W=J12−6I12, incoming −e1, both directions excluded on Link {0,e1}, exactly one outgoing negative step. Retain full X6 Cell–terminal-port–grade observer, signs, multiplicities, provenance, branch order and residual. This is an analytic certificate for the existing auxiliary scalar observer only, NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION. No new native state propagation, classical reference-model run, phase evaluation or pi calculation. The rational arithmetic below checks algebraic inequalities in the inherited ODE proof, not a new physical input or trajectory.

Primary source: 189df0a35de84cf478c7b06181db602a064ad425:research_notes/portable_direct/2026-11-24_r6_prefix1048_frobenius_majorant_upper_band_positivity.md, equations (1), (5) and branch matching §3. Retain its pinned PREFIX-1035 ODE and PREFIX-1044 edge coefficient c>0. The new theorem is
\[
\boxed{20\le y<36 \quad\Longrightarrow\quad g(y)>1396c(36-y)^{5/2}>0.}
\]
At y=36, g(36)=0. This extends the previously certified length 39/10 to 16, i.e. by factor 160/39. It covers the entire interval, not just sampled points.

## 1. Preserve the cancellation in the Frobenius coefficient transport

Put x=36−y, rho(36−x)=c x^(3/2) A(x), A(x)=sum b_n x^n and b_0=1. The preceding paper determines its formal coefficients by
\[
 b_n=-\frac{\sum_{k=1}^{\min(5,n)}P_k(3/2+n-k)b_{n-k}}{P_0(3/2+n)}.
\]
The six P_k are copied verbatim into the companion checker below. Use c_n=16^n b_n (not the edge coefficient c) and D(n)=−P_0(3/2+n)=1866240 n(2n−3)(2n−1)(2n+1)(2n+3). Define R_k(n)=16^k P_k(3/2+n-k). For n>=5 the state v_n=(c_n,c_{n-1},...,c_{n-4})^T obeys v_n=E(n)v_{n-1}/D(n), where E has first row (R_1,...,R_5) and subdiagonal D, all other entries zero. No sign is erased before taking the transformed norm.

The limiting matrix M=lim E(n)/D(n) has characteristic polynomial
\[
(\lambda-4/5)(\lambda-1/2)(\lambda-4/9)^3.
\]
The repeated root is dealt with by a scaled Jordan chain, not treated as diagonalizable. Let
\[
 V=\begin{pmatrix}
256/6561&256/729&32/27&1/16&256/625\\
64/729&16/27&4/3&1/8&64/125\\
16/81&8/9&1&1/4&16/25\\
4/9&1&0&1/2&4/5\\
1&0&0&1&1
\end{pmatrix},\quad S=V\operatorname{diag}(1,1/8,1/64,1,1).
\]
Exact multiplication gives S^-1 M S with diagonal (4/9,4/9,4/9,1/2,4/5) and superdiagonal 1/8 in the first 3-by-3 block only. Also ||S||_infty ||S^-1||_infty=316368.

Let d_5 be the leading coefficient of D and B(n)=S^-1 E(n) S=sum_{k=0}^5 B_k n^k. Set C_k=||B_k||_infty/d_5 and d_k=[n^k]D. For every real n>=N=5000, triangle inequality and the positive denominator give
\[
 \|S^{-1}E(n)S/D(n)\|_\infty
 \le \frac{\sum_{k=0}^5 C_k/N^{5-k}}{1-\sum_{k=0}^4 |d_k/d_5|/N^{5-k}} <91/100<19/20.
\]
The final comparison and positivity of the denominator are exact polynomial-coefficient rational checks, not an asymptotic fit. They establish a uniform contraction for every later integer n, including arbitrarily large ones.

## 2. Certified infinite tail

The checker evaluates the first 5000 rational c_n, n=0,...,4999, from the frozen recurrence with absent negative indices omitted. It verifies ||v_4999||_infty<10^-40. For every j>=1, by iterating the uniform contraction,
\[
 |c_{4999+j}|\le316368\cdot10^{-40}(19/20)^j.
\]
Write Q=19/20, H=316368*10^-40. Thus
\[
 \sum_{n\ge5000}|c_n|\le H Q/(1-Q)=T_0,\qquad
 \sum_{n\ge5000}n|c_n|\le H(4999Q/(1-Q)+Q/(1-Q)^2)=T_1.
\]
This also gives convergence of the series for |x|<16/Q, a radius strictly exceeding 16. The series solves the same ODE by coefficient recurrence. It agrees near zero with the actual density by the branch matching proved in PREFIX-1048 §3; ordinary ODE uniqueness propagates equality to 0<x<=16, since the nearest other singular point is x=20. Thus the bounds apply to the actual inherited auxiliary density and not an unrelated formal solution.

## 3. Whole-interval sign certificate

Use the exact contrast identity of PREFIX-1048 (5). Termwise differentiation and integration on the compact x range are justified by §2. Write G(x)=5g(36−x)/(c x^(5/2)), for x>0. Substituting A yields
\[
G(x)=\sum_{n\ge0} c_n (x/16)^n F_n(x),
\quad
F_n(x)=(36-x)(538-12x)-4(36-x)^2 n
-12(47-x)\left(\frac{30}{n+5/2}-\frac{x}{n+7/2}\right).
\]
For 0<=x<=16, |F_n(x)| <=30000+5200n, using 36*538, 4*36^2 and 12*47*(30*2/5+16*2/7) as respective term bounds. Consequently
\[
 |G(x)-G_{20}(x)|\le 30000\left(\sum_{n=21}^{4999}|c_n|+T_0\right)
 +5200\left(\sum_{n=21}^{4999}n|c_n|+T_1\right)<16.
\]
Here G_20 is the polynomial through n=20. The final comparison is checked in exact Fraction arithmetic.

With t=x/16, expand G_20(16t)=sum_{j=0}^{22} a_j t^j. Its degree-22 Bernstein coefficients are
\[
 \beta_k=\sum_{j=0}^k a_j \frac{\binom{k}{j}}{\binom{22}{j}},\quad k=0,\ldots,22.
\]
The checker verifies each beta_k>7000. The Bernstein basis is nonnegative and sums to one on [0,1], giving G_20(16t)>7000 throughout. With the tail bound, G(x)>6984 and g(36−x)>(6984/5)c x^(5/2)>1396c x^(5/2). This proves the theorem, including x=16. The separate endpoint x=0 has g(36)=0 by the inherited asymptotic.

## 4. Reproduction and provenance

Companion code (complete, remotely read back and identical to executed local blob):
1c1a850fe661981f2ea9ff7a79ea532c820ae217:research_notes/portable_direct/PREFIX1049_R6_WEIGHTED_COMPANION_CHECK.py
git blob 56756b8879d0e4c14fe2f160c2dddc7fe451d249
SHA256 1c17cf4dafc8697acf8e7426b7d7a911dee1337f8a40977babbc2cdf5e7d5fd1.
Run python PREFIX1049_R6_WEIGHTED_COMPANION_CHECK.py with SymPy. Actual output:
PREFIX1049_EXACT_COMPANION_BERNSTEIN_CERTIFICATE_PASSED
norm < 91/100; tail < 16; 23 Bernstein coefficients > 7000

Finite arithmetic checks: exact matrix similarity and norm coefficient bound, 5000 rational recurrence terms, terminal vector bound, exact absolute-tail comparison, and all 23 rational Bernstein coefficients. The all-index contraction, geometric summation, ODE uniqueness and Bernstein basis identity are the mathematical extensions from those finite checks to the entire interval. No new native BRC trajectory, comparison-model experiment or independent scientific review. No P000 or observer equivalence claim is changed.

Current normative entry snapshots: global main@59e855b5cf4fccbfb0c9f21322ff09844dd7fefe; project main@bdc3cf2a82e18426c91ff71c40f0b1c4ed8c31ba. Frozen science pin unchanged. Current LEASED read r6-20261124-0752-leased-observe-v1 SUCCEEDED/error=null, empty filtered list as of 2026-11-23T23:52:22.226037Z, execution_authorized=false. Original own registration EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322, activity checkpoints empty at pinned current read. Own recovery metadata r6-20261124-0755-own-recovery-read-v1 confirms open underlying SID, no runs, no execution authority; no fresh logical-session binding attested. Independent portable note; no CLAIM, PROGRESS, Result or Activity mutation.

Next scientific question: approach x=20 (y=16) with stronger scaled companion bounds or regular ODE propagation, then connect to the existing certified critical neighborhood. Full scalar sign question elsewhere, native signed BRC joint observer correspondence, and mother B_fix,odd(32) in {19,20} remain open. Do not repeat the established x<=16 certificate.
