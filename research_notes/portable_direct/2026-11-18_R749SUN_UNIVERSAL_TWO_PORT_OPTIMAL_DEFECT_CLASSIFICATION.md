# R749SUN — Complete universal classification of optimal labeled two-Port feedback defects

Date: 2026-11-18 (Asia/Shanghai).
Evidence: AUTHOR_EXACT_NOT_REVIEWED (new all-parameter proof plus previously completed exact finite certificate).
Scope: auxiliary positive-rational WBRC-T30–T32 *labeled* two-Port feedback observer; no native X6 Cell/Link/Port admission.

## Pinned scientific inputs

- Frozen WBRC-T30–T32 science: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
- R749SUK at @0b292a4181f3729b2bda282cf35e6df2166531e5: exhaustive exact C++17 optimizer certificate for 2 <= M <= 10000, including all tied maxima; independent brute check 2 <= M <= 120. Its saved result lists all optimal Q values {-1,1,2}, nonunit-optimal scales {58,93}.
- R749SUM at @29568bd754d2d6eb80c6c9f1730c1b02297c1204: prior global |Q| <= 16.
- R749SUL at @7d7a2957120a76467daafd359cef13b5f8fdbd0d: positive-unit optimum on specified positive-density square windows. The new near-product method covers every sufficiently large M.
- The P000 / ACTIVE worldview retains six native axes, its three-dimensional slice, provenance, triadic closure and resource/time conditions. This integer matrix is an auxiliary typed observer, not a native two-dimensional plane or a primitive two-force balance.

For each M >= 2, define

\[
\mathcal U_M=\{(a,u,v,d)\in\{1,\ldots,M\}^4:ad-uv=1\},\quad
\tau(a,u,v,d)=\max(u,v)ad,\quad Q=u+v-a-d.
\]

Canonical configurations have a=d and {u,v}={a-1,a+1}; by R749SUK they are precisely the Q=0 fiber. Let Opt(M) comprise **every labeled maximizer of tau among noncanonical configurations**, including all ties.

## Main theorem (all integer scales)

For every integer M >= 2 and every A in Opt(M),

\[
\boxed{Q(A)\in\{-1,+1\}\quad\text{for }M\notin\{58,93\};\qquad
       Q(A)=+2\quad\text{for }M\in\{58,93\}.}
\]

In particular, the only scales permitting optimal |Q| > 1 in the entire infinite domain are 58 and 93. The analytic argument below proves |Q|=1 for all M >= 9999; the finite region is already exhaustively covered by R749SUK. Exceptional witnesses are (a,u,v,d)=(45,58,38,49), tau=127890, and (76,93,67,82), tau=579576, both with ad-uv=1 and Q=2. Exact global optimality at these two scales is certified by the R749SUK enumeration.

### Lemma 1: a uniform positive-unit near-product competitor

For M >= 9999, put n=M+1, t=floor(sqrt(n)) >=100, and k=n-t² with 0 <= k <= 2t.
Choose j=1 when k <= t and j=2 otherwise, so 0 <= jt-k <= t.
Let z be the least nonnegative integer with z(z+j) >= jt-k; let c=ceil(sqrt(t)). Then z <= c.
Set

\[
r=t-z,\qquad s=t+z+j,\qquad p=rs-1,\qquad
\delta=M-p=z(z+j)-(jt-k).
\]

The choice of z gives 0 <= delta <= 2c+1, r+s=2t+j <=2t+2, and (for t>=100) r>1, s>1, p>r+s and 1<=p<=M. Define

\[
C_M=(a,u,v,d)=(p-r,\ p,\ p-r-s+1,\ p-s).
\]

All four entries lie in [1,M]. Direct expansion gives

\[
ad-uv=(p-r)(p-s)-p(p-r-s+1)=rs-p=1,\quad Q(C_M)=1.
\]

Thus this is an admissible noncanonical competitor, with W=p(p-r)(p-s).
The sum of deficits of its three threshold factors relative to M is

\[
S_C=3\delta+r+s\le 2t+6c+5\le 2t+6\sqrt t+11.
\]

The near-product rs differs from M+1 by O(sqrt(t)), bridging the gaps of the older single-square construction.

### Lemma 2: a two-unit transfer of the competitor deficit to every maximizer

Orient any maximizing tuple by exchanging u and v if necessary, so u=max(u,v). This changes neither tau nor Q. Put h=M-u, R=M-a, T=M-d, S=h+R+T. By optimality, uad >= W; by AM–GM,

\[
uad\le (M-S/3)^3.
\]

Set Z=(r+s+2)/3, so M-(S_C+2)/3=p-Z. The exact identity

\[
p(p-r)(p-s)-(p-Z)^3
=2p^2+p(rs-3Z^2)+Z^3
\]

shows W >= (p-Z)^3 whenever 6p >= (r+s+2)^2.
This holds for every t>=100: c<=t/5, p>=t²-2c-2 and r+s+2<=2t+4 imply

\[
6p-(r+s+2)^2\ge 2t^2-\frac{92}{5}t-28>0.
\]

The relevant bases are positive, hence

\[
M-S/3\ge M-(S_C+2)/3,\qquad
\boxed{S\le S_C+2\le B:=2t+6\sqrt t+13.}
\]

The two-unit transfer matters: bounding W only by its smallest factor cubed would lose an order-t term and would not establish the theorem.

### Lemma 3: a strict integer obstruction to |Q| >= 2

The determinant identity is

\[
\boxed{uQ=(u-a)(u-d)-1.}
\]

At t>=100, u>=M-B>1. Write x=u-a=R-h and y=u-d=T-h.
If x,y<0, then a,d>u>=v imply Q<0, while xy>=1 and the identity imply Q>=0, a contradiction.
If either x or y equals 0, then uQ=-1 is impossible for integer Q and u>1.
If x,y>0, xy<=RT<=S²/4.
If x,y have opposite signs, say x>0>y, then |xy|=(R-h)(h-T)<=Rh<=(R+h)²/4<=S²/4.
Therefore, in every permissible case,

\[
|uQ|\le S^2/4+1.
\]

Since u>=M-S>=M-B and M>=t²-1,

\[
|Q|\le\frac{B^2/4+1}{M-B}
\le\frac{(2t+6\sqrt t+13)^2+4}{4(t^2-1-(2t+6\sqrt t+13))}.
\]

For x=sqrt(t)>=10, the strict inequality that the right-hand side is less than 2 is equivalent to

\[
\begin{aligned}
F(x)&=8(x^4-1-(2x^2+6x+13))-(2x^2+6x+13)^2-4\\
&=4x^4-24x^3-104x^2-204x-285\\
&=4(x-10)^4+136(x-10)^3+1576(x-10)^2
+6516(x-10)+3275>0.
\end{aligned}
\]

This holds for all real x>=10 by its strictly positive shifted coefficients. Hence |Q|<2. Because Q is an integer and Q=0 is excluded, **|Q|=1 for every M>=9999**.

### Completing all M >= 2

The previously saved and executed R749SUK exact C++17 certificate enumerates every oriented solution ad-uv=1, 1<=a,u,v,d<=M, gcd(a,u)=1 and v<=u, via d ≡ a^{-1} (mod u) and v=(ad-1)/u. Each tuple is bucketed by its largest component, and prefix maxima yield all optima for every M=2,...,10000. The exchange u↔v preserves Q and tau, so the oriented enumeration is sufficient for this theorem. Its direct brute-force independent comparison covers 2,...,120; all intermediate arithmetic is integer exact. Its saved results give nonunit exceptions **exactly M=58,93**, with Q=+2 in each case; elsewhere Q∈{-1,+1}. This overlaps the analytic range (M=9999,10000) and proves the Main Theorem.

The original 60,779,744 candidate scan is reused by immutable source pin and prior execution result; it is **not** claimed to have been rerun this turn.

## Independent new exact validation

Companion R749SUN_NEAR_PRODUCT_RIGIDITY_CERT.py uses only Python standard-library exact integers/Fraction. It checks 12,801 complete (t,k) pairs for 100<=t<=150 and 0<=k<=2t; each explicit matrix's determinant, Q, factor comparison, AM–GM transfer bound, and the strict final integer obstruction. It independently exhausts small M=2,...,26 and verifies the shifted quartic coefficient identity in exact integer polynomial arithmetic. Results are preserved in R749SUN_NEAR_PRODUCT_RIGIDITY_RESULTS.json (PASS). Infinite validity comes from Lemmas 1–3, not the finite regression. Status remains AUTHOR_EXACT_NOT_REVIEWED; no independent Driver review or native X6 admission.

## Next research

Classify the sign Q=±1 and all tied maximizers for M>=9999; examine whether a stronger near-product selection yields a uniform *positive* sign. Separately construct a provenance-faithful X6 Cell/Link/Port event satisfying P000 triadic closure, resource permissions and causal time before transferring this auxiliary observer conclusion. Historical R2 research provenance: EM-DIRECT-44C346; RA-A16A5E663104EBDBA287C665. No new shared CLAIM or authenticated fresh session is asserted here.
