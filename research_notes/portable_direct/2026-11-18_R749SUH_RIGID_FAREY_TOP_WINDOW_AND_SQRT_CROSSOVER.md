# R749SUH — Top-threshold rigidity and sharp square-root crossover for labeled two-Port BRC feedback

Date: 2026-11-18 (Asia/Shanghai). Status: **AUTHOR_EXACT_NOT_REVIEWED**. Source lineage: R749SUF/R749SUG, GitHub Draft PR #2689 (commit 72937afbab96237df00a33cfe2eb6c5689762564). Frozen scientific inputs: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, WBRC-T30–T32. The present model is the positive-rational, labeled Port *observation* signature; no native X6 triadic event admission is asserted.

## 1. Exact domain and preserved observations

Let integer M>=6. A labeled unimodular Port-bin matrix is the ordered tuple (a,u,v,d) with 1<=a,u,v,d<=M and ad-uv=1; both Port orientations are retained. Its feedback threshold is

\[
\tau(a,u,v,d)=\max(u,v)\,ad.
\]

For 1<=j<=M-2, the two adjacent-diagonal canonical configurations are

\[
C_j^\pm=(M-j,\ M-j\pm1,\ M-j\mp1,\ M-j),
\quad F_j=\tau(C_j^\pm)=(M-j+1)(M-j)^2 .
\]

Here the displayed tuple order is (a,u,v,d), with the plus sign applying to u. These two are distinct labeled configurations. The F_j decrease strictly in j. All other configurations are *noncanonical*. Denote their largest threshold by T_*(M), taking 0 if there are none.

R749SUE/SUF proved that for integers K>M with 2K>M^3, the late-grid deficiency is the number of these configurations whose thresholds are at least K. We first study the **entire integer threshold spectrum**, and afterward restrict it to that late interval.

## 2. Theorem A — Congruence defect and diagonal rigidity

Orient the off-diagonal entries so that u=max(u,v). Introduce nonnegative deficiencies

\[
x=M-a,\quad y=M-d,\quad z=M-u,\quad w=M-v\quad (z\le w),
\qquad S=x+y+z .
\]

The determinant-one condition is equivalent to the existence of an integer q with

\[
\boxed{(x-z)(y-z)=1+(M-z)q,\qquad w=x+y-z-q.}
\]

Furthermore q=0 holds **exactly** for the adjacent-diagonal canonical family. Every noncanonical configuration satisfies

\[
\boxed{S\ge 2\sqrt{M+1}\qquad(M\ge6).}
\]

**Proof.** Expanding (M-x)(M-y)-(M-z)(M-w)=1 yields the boxed identity with q=x+y-z-w. When q=0, the integer product (x-z)(y-z)=1 forces either x-z=y-z=1 or x-z=y-z=-1. The second case gives w=z-2<z, contradicting u>=v. The first gives x=y=z+1 and w=z+2, exactly C_j^+ up to the two Port orientations. Conversely C_j^\pm gives q=0.

Now let q be nonzero and U=M-z=max(u,v). If U=1, then u=v=1 and ad=2. In this case S=3M-4, satisfying the asserted bound for M>=6. Assume U>=2.

If q>=1, then (x-z)(y-z)>=U+1>0. Both factors cannot be negative: that would make a,d>=U+1, whereas ad=Uv+1<=U^2+1<(U+1)^2. Hence p=x-z>=1 and r=y-z>=1, with pr>=M-z+1. By AM–GM,

\[
S=3z+p+r\ge3z+2\sqrt{M-z+1}\ge2\sqrt{M+1}.
\]

The last lower bound follows from monotonicity in z on 0<=z<=M-1.

If q<=-1, then the two factors have opposite signs. Up to exchanging a and d, let p=x-z>=1 and r=z-y>=1; then r<=z and pr>=U-1=M-z-1. Again by AM–GM,

\[
\begin{aligned}
S&=3z+p-r\\
&\ge3z-r+(M-z-1)/r\\
&\ge2r-1+(M-1)/r\\
&\ge2\sqrt{2(M-1)}-1\\
&\ge2\sqrt{M+1}\qquad(M\ge6).
\end{aligned}
\]

For the third inequality we used z>=r and 3-1/r>0. The last inequality holds at M=6 and its left-minus-right side increases for M>=6. QED.

## 3. Theorem B — An explicit initial spectrum of exact multiplicity two

Define

\[
j_0(M)=\max\big(\{0\}\cup
\{\,j\in\mathbb Z:1\le j\le M-2,\ (3j-1)^2<4(M+1)\,\}\big).
\]

**For every integer M>=6, the j_0(M) highest distinct thresholds of all labeled bounded unimodular matrices are exactly**

\[
\boxed{F_1>F_2>\cdots>F_{j_0(M)}},
\]

**each with precisely two configurations C_j^+,C_j^-.**

**Proof.** If \(\tau\ge F_j\) yet \(S=x+y+z\ge3j\), arithmetic–geometric mean gives

\[
\tau=(M-x)(M-y)(M-z)
\le (M-S/3)^3\le(M-j)^3<F_j,
\]

a contradiction. Thus S<=3j-1. For j<=j_0, we have S<2sqrt(M+1), forcing the canonical family by Theorem A. Since F_j strictly decreases, the only configurations at or above F_j are C_k^\pm for k<=j, as claimed. QED.

This supplies a uniform *square-root-scale* protected prefix: \(j_0(M)=\frac23\sqrt M+O(1)\). This is an exact all-M lower bound on the first noncanonical intrusion rank, not an empirical extrapolation.

## 4. Theorem C — Optimal leading crossover along a concrete infinite sequence

For every M>=6, Theorem A and AM–GM give the universal envelope

\[
\boxed{T_*(M)\le\left(M-\tfrac23\sqrt{M+1}\right)^3.}
\]

For t>=4 and M=t^2-1, reuse the exact noncanonical R749SUG divisor-layer witness

\[
a=d=M-t,\quad u=M,\quad v=t(t-2),
\qquad ad-uv=1.
\]

Its threshold is W_t=M(M-t)^2, giving the explicit sandwich

\[
\boxed{M(M-t)^2\le T_*(t^2-1)\le(M-2t/3)^3.}
\]

The right-minus-left width is exactly \(\frac13t^2M-\frac8{27}t^3\). Consequently, **along M=t^2-1**,

\[
\boxed{T_*(M)=M^3-2M^{5/2}+O(M^2).}
\]

Let J(M) count the initial canonical threshold levels strictly greater than T_*(M). Then

\[
\boxed{J(t^2-1)=\frac23t+O(1).}
\]

**Proof of the rank claim.** Theorem B gives J>=j_0=(2/3)t+O(1). The witness implies J is no greater than the number of j for which F_j>W_t. Take j=ceil(2t/3)+2. For t>=6, j<=t and the exact expansion gives

\[
W_t-F_j=(3j-1-2t)M^2+(t^2-3j^2+2j)M+j^2(j-1)
\ge5M^2-2t^2M>0 .
\]

For t=4,5, direct substitution also gives F_j<W_t. Hence J<ceil(2t/3)+2, and combining with the lower bound proves the statement. The leading threshold asymptotic follows by expanding the two sides of the sandwich: both have leading terms M^3-2sqrt(M+1)M^2 and differ by O(M^2). QED.

## 5. Exact finite certificate

The accompanying dependency-free JavaScript code independently enumerates all a,d,u, solving v=(ad-1)/u in exact integers. It verifies every labeled tuple in all M=6,...,96; all noncanonical defect inequalities; all initial canonical rank and multiplicity assertions; and the reusable square-minus-one construction for t=4,...,40.

Executed result: **PASS**, 360,304 matrices enumerated, 351,386 classified noncanonical, and 403 checked initial-rank assertions. JavaScript Number arithmetic is exact on this bounded integer domain. The infinite-domain results are proved above; the finite certificate is regression evidence.

Selected examples:

| M | Certified initial ranks j_0 | Actual canonical ranks before first intrusion | Largest noncanonical threshold |
|---:|---:|---:|---:|
| 15 | 2 | 3 | 1815 |
| 20 | 3 | 3 | 4420 |
| 32 | 4 | 5 | 19488 |
| 64 | 5 | 6 | 192576 |
| 80 | 6 | 6 | 403280 |
| 96 | 6 | 8 | 685995 |

## 6. Status, provenance, and next questions

Prior exact inputs: R749SUE's late unimodular reduction, R749SUF's Farey-tree threshold spectrum, and R749SUG's maximal-Port divisor-layer family. Their original proofs and authorship are retained. New work here is the defect congruence rigidity argument, uniform protected top-prefix theorem, and asymptotically sharp crossover ranking along the square-minus-one family.

Scientific status: **AUTHOR_EXACT_NOT_REVIEWED**. A labeled WBRC Port feedback threshold is an auxiliary observable. Native P000/Heartbeat X6 Cell/Link/Port events still require separately admitted triadic closure, source/target resource guards, time-order semantics and a certified observer bridge.

Next: classify the exact finite-M winner among q=1 divisor-layer and interior Farey branches, identify the first intrusion threshold and multiplicity, and test native resource/time admission on a concrete typed event rather than by relabeling the feedback observer.
