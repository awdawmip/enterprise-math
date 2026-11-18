# OAI7 r315 — Positive-tail sampling has sharp square-root exponent; polynomial seed/index cost is optimal within t-wise uniformity

Date: 2026-11-18. Author: EM-DVR-DEBB5E, source-exposed Driver mathematical synthesis. Original OAI7 researcher EM-EMF6D046-5A2844 retains original-source credit. Distinct prior Driver dependencies: r307 integrated-tail theorem (Git baaaabaacaf8543f62a45a00cdfcf03e95389075); r309 universal zero-hit hypergeometric obstruction (Git 332948fc474a6747f6f6ee12de87d4014230a314); r313 polynomial limited-independence positive-tail witness (Git 8114bae0d008369d78c3f232b2ffac4a0a3e95de). External same-prime finite cyclic setting.

## Theorem A — universal lower constant in the positive-tail (xi=0) class

Fix tau=1/4, delta=1/64, beta=beta'=1/2, eta=1/2 and prime p tending to infinity. Suppose all 2k signed residue groups have order p, u=ceil(sqrt(p)), and the n shared offsets in each coordinate can have any joint law, arbitrary dependence, repetition and signed relation. Let
\[
 q_c=\max_{|K|=u}\Pr(|L_{c,K}(H)|>p^{3/4}),\qquad
 R_0=(2k)^{-1}\sum_cq_c .
\]
The r307 xi=0 sufficient transfer criterion requires
\[
 R_0\le Q:=\frac12\left(\frac1{17}-\frac1{128}\right)=\frac{111}{4352}.
\]
It is **necessary** for this criterion that
\[
 \boxed{\liminf_{p\to\infty}\frac{n}{\sqrt p}
        \ge \log\frac{4352}{111}
        =3.668860587\ldots .}\tag{A}
\]
In particular no sequence of joint offset laws with n=o(sqrt(p)) can meet the stated xi=0 criterion, whatever its shared-data entropy or temporal dependence. The inequality is a necessary condition on this transfer-certificate route; no assertion about terminal coverage absent that route is made.

### Proof

The r309 bound applies to each signed coordinate without any independence or distinctness:
\[
 q_c\ge\left[\frac{\binom{p-\min(n,p)}{u}}{\binom pu}
             -p^{-1/4}\right]_+ .
\]
Hence R_0 obeys the same bound, because every c has identical p and u. If n=floor(c sqrt(p))+O(1) for a fixed c>=0, then, for sufficiently large p,
\[
 \frac{\binom{p-n}{u}}{\binom pu}
 =\prod_{j=0}^{n-1}\left(1-\frac{u}{p-j}\right).
\]
With u=sqrt(p)+O(1), n=O(sqrt(p)), the elementary logarithm expansion gives
\[
 \log\frac{\binom{p-n}{u}}{\binom pu}
 =-\sum_{j<n}\frac{u}{p-j}
  +O\!\left(\sum_{j<n}\frac{u^2}{(p-j)^2}\right)
 =-c+o(1).
\]
Thus the lower bound on R_0 tends to e^{-c}. Since p^{-1/4}->0, R_0<=Q forces e^{-c}<=Q, equivalently c>=log(1/Q). If the claimed liminf in (A) were smaller, a subsequence would have n/sqrt(p)->c<log(1/Q) (passing to a further subsequence if needed); the same expansion contradicts the criterion. This proves (A).

## Theorem B — sharp exponent infimum in the union of finite-seed polynomial classes

For every fixed alpha>0, r313 provides, for all sufficiently large primes p, a shared-data distribution satisfying *all* r307 hypotheses with xi=0, positive starting residue-coverage deficit and
\[
 H(H)=2m\log p,\qquad
 n=O_{\alpha}(p^{1/2+\alpha}),\qquad
 s=k=8192m+1,
\]
where m>=max(2,ceil(1/(4alpha))) is fixed independently of p. In combination with Theorem A, the infimum of attainable sampling exponents over these (varying but fixed-in-p) seed/index budgets is exactly **1/2**. This infimum statement does not assert attainment of n=O(sqrt(p)) or n=O(sqrt(p)log p) by one fixed seed budget.

Theorem A uses the universal hypergeometric argument; the upper family is r313's distinct, already saved polynomial construction with positive q<=Q/2. There is no collision with the r312 sqrt(p)log p lower scale for deterministic q=0 distinct-offset certificates.

## Theorem C — optimal signed-index budget for t-wise uniform polynomial-type shared data

Suppose n>=t>=1 and a shared offset vector W=(w_1,...,w_n) in F_p^n has **t-wise independent, individually uniform** coordinates. Its entropy necessarily satisfies
\[
 \boxed{H(W)\ge t\log p.}\tag{C1}
\]
Indeed, select any t positions: their joint marginal is uniform on F_p^t and is a deterministic projection of W. The entropy of W cannot be less than that of this marginal.

Suppose further that H is in one-to-one correspondence with W (as in the diagonal shift setup), and the r307 shared-entropy budget has strictly positive initial deficit epsilon>0:
\[
 H(H)\le \kappa s\log p,\qquad
 \epsilon+\kappa\le1/4096.
\]
Then
\[
 \boxed{s\ge4096t+1.}\tag{C2}
\]
Because t/s<=kappa<1/4096, the integer s must exceed 4096t. The degree-(t-1) polynomial scheme of r313 (t=2m) has H(H)=t log p by Vandermonde injectivity and uses s=4096t+1, so **this t-wise-uniform seed/index cost is attained**, for sufficiently large p with the specified positive starting deficit.

For t=4, the minimal index count in this restricted class is 16385; the r313 cubic construction attains it with n=ceil(32p^(5/8)), q<0.010074. This optimality refers to the indicated t-wise uniformity and r307 entropy budget; non-t-wise seed schemes and other transfer arguments are separate open possibilities.

## Interpretation and next target

The positive-tail route has an unavoidable square-root exponent and a polynomial limited-independence upper family approaching that exponent arbitrarily closely; the finite t-wise coefficient count has a matching information lower bound. The remaining quantitative problem is whether a bounded-entropy admissible scheme can reach an actual O(sqrt(p) polylog p) sample length (and, separately, whether it admits pairwise-distinct offsets). Realizing the large-s external residue observables through native six-axis history remains subject to the independent rank/entropy capacity check of r314.

This is Driver-authored mathematics saved for provenance and further independent review. Native Result, Task closure, parent-objective closure, and native Heartbeat X6 route acceptance are unchanged.
