# R749SQA — Sharp Walsh stabilization and universal boundary-layer correction

Date: 2026-11-15. Status: **AUTHOR_EXACT_NOT_REVIEWED**. Research mode: independent portable TASK_RESEARCH. Own Researcher-ID **EM-DIRECT-5AD5C5**, SID **MCP-b7e4fc4f9908457da9fb6a112db109b0**, Activity **RA-23D649E29465155706DB0336**. Frozen scientific source: **awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389**. Predecessor: R749SPZ, Git commit **b4507430ced229f67db20fe0424e3988ca747c7a**; inherited author-level R749SPR/R749SPU classification. Scope: auxiliary signed 16-atom Walsh optimal-center source model at $(t,s)=(1/10,1/2)$, not an assertion about native X6 signed Cell/Port dynamics.

## Definitions

Let $K\cap\mathbb Z^3$ be the 33 first-grid lattice points satisfying R749SPR's eight facets, and $F$ the 25 forced source types determined by unique unordered two-source target sums. The competing 26-letter alphabets are $A_0=F\cup\{(0,0,0)\}$ and $A_1=F\cup\{(-1,0,0)\}$. A source is $(h,u,v)$ and its deficit is $d=2-u$. In $F$, the zero-deficit letters are exactly $a=(-1,2,-1)$ and $b=(0,2,0)$; the remaining 23 types $B$ satisfy $d\ge1$ and $v\le d$. Exactly one $B$ letter has $(d,v)=(1,1)$: $e=(0,1,1)$.

Write $M_j(n,H,U,V)$ for the count of unordered multisets of $n$ source letters from $A_j$ with coordinate sum $(H,U,V)$. Fix arbitrary integers $D\ge2$, $n\ge0$ and the slice $(U,V)=(2n-D,0)$. Write $\Delta_{n,D}(H)=M_0(n,H,2n-D,0)-M_1(n,H,2n-D,0)$. Let $N_{n,D}=\sum_H M_j(n,H,2n-D,0)$ (independent of $j$); $N_D$ is its saturated value. Let $W_{n,D}$ be the total number of uses of the optional alphabet letter across all these multisets.

## Theorem A — exact earliest signed stabilization

For **every** integer $D\ge2$, $\Delta_{n,D}$ becomes identically equal to its stable profile **if and only if** $n\ge 2D-3$. In particular, R749SPZ's universal sufficient bound is sharp at every deficit, not merely the previously calculated deficits $2,4,6,8$. At $n=2D-4$ the first moment of the signed profile is exactly one less than its stabilized first moment:
\[
\sum_H H\Delta_{2D-3,D}(H)-\sum_H H\Delta_{2D-4,D}(H)=1.
\]

## Theorem B — universal unsigned boundary layer

For every integer $r\ge1$, define
\[
G(z)=\frac{1}{(1-z)^3(1-z^2)^4(1-z^3)^6(1-z^4)^4(1-z^5)^3(1-z^6)^2(1-z^7)},
\quad C_r=\sum_{q=0}^{r-1}[z^q]G(z).
\]
Equivalently, $\sum_{r\ge0}C_rz^r=zG(z)/(1-z)$.

For all $D\ge\max(2,2r-2)$, the **exact** mass missing at $n=2D-r$ is $N_D-N_{2D-r,D}=C_r$. For $r\ge3$, the bound $D\ge2r-2$ is sharp: at $D=2r-3$ the missing count is strictly below $C_r$. For $r=2$, $D=2$ is the earliest $D$ in the present domain. The initial constants are:

| $r$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $C_r$ | 1 | 4 | 14 | 42 | 113 | 279 | 651 | 1437 |

Thus $N_{2D-1,D}=N_D-1$ and $N_{2D-2,D}=N_D-4$ for all $D\ge2$. At the signed cutoff $n=2D-3$, for $D\ge4$, **14 common multisets are still absent** although the signed difference is stable.

The $C_r$ are a rational-generating-function quasipolynomial of degree 23 with period dividing 420; their leading growth is
\[
C_r\sim\frac{r^{23}}{23!\cdot 94{,}058{,}496{,}000}.
\]
This is an asymptotic as the boundary depth $r\to\infty$ after applying the stated $D\ge2r-2$ applicability condition.

## Theorem C — all-length exact conditional transport

For every $n\ge1$ with $N_{n,D}>0$, use the Walsh total-variation ground metric on the first-grid predictions ($|H-H'|/(20n)$ when $U,V$ agree). For distributions induced by **uniform unordered source multisets** in $A_0$ and $A_1$ at the fixed slice,
\[
W_1^{TV}(n,D)=\frac{W_{n,D}}{20nN_{n,D}}.
\]
The numerator $W_{n,D}$ first saturates exactly at $n=2D-3$, whereas $N_{n,D}$ first saturates at $n=2D$. For $2D-3\le n\le 2D$, the numerator has its full saturated value $W_D$ even though the mass denominator can still increase.

## Proof

For a multiset $c$ of positive-deficit forced letters, write $m=|c|$, $\delta=\sum d(f)$, $v=\sum v(f)$, $h=\sum h(f)$ and let $k\ge0$ be the optional-letter multiplicity. The slice forces $\delta+2k=D$. The multiplicity of $a=(-1,2,-1)$ must be $\alpha=v\ge0$, and the multiplicity of $b=(0,2,0)$ is $\beta=n-k-m-v$. The pattern is admissible exactly when $n\ge n_{\min}=k+m+v$. Its readings in the two alphabets are $H_0=h-v$ and $H_1=h-v-k$.

Consequently, at each integer threshold $T$, the integrated signed tail is
\[
\sum_{H\ge T}\Delta_{n,D}(H)
=\sum_{\substack{k\ge1,\ c:\ \delta(c)+2k=D\\ n\ge n_{\min}(k,c)}}
\mathbf1_{\{H_0-k<T\le H_0\}}.
\]
All terms are nonnegative, so the tails only increase with $n$. For $k\ge1$, $m,v\le D-2k$, hence $n_{\min}\le 2D-3k\le 2D-3$. Conversely the pattern $k=1$, $c=e^{D-2}$ has $n_{\min}=2D-3$, and gives a strictly positive additional tail at $T=-(D-2)$. No cancellation is possible. To see uniqueness at the final step, put $s(f)=2d(f)-1-v(f)\ge0$ for $f\in B$. Only $e$ has $s=0$; an optional letter has $s=3$. The exact identity
\[
2D-n_{\min}=\sum_{f\in c}s(f)+3k
\]
shows that the **only** pattern with $k>0$ and $n_{\min}=2D-3$ is $k=1,c=e^{D-2}$. Its first-moment increment is one, proving Theorem A.

For Theorem B, put $n=2D-r$. A pattern is missing iff its slack $S=2D-n_{\min}$ is $<r$. Remove all copies of the unique zero-slack letter $e$ and call the remaining positive-deficit and optional multiset $L$. Every nonzero-slack type has strictly positive integer $s=2d-1-v$ (the optional type has $(d,v,s)=(2,0,3)$). Enumerating the original 33 first-grid lattice points and the 25 forced types gives **exactly** the 23 nonzero-slack types with multiplicities
\[
(s:\#)=(1:3,\ 2:4,\ 3:6,\ 4:4,\ 5:3,\ 6:2,\ 7:1).
\]
The number $q$ of removed $e$ letters is uniquely $q=D-\delta(L)$, and the required zero-deficit $a$ multiplicity is $q+v(L)=D-(\delta(L)-v(L))$. For each nonzero-slack type, $d\le2s$ and $d-v\le2s$; hence $\delta(L),\delta(L)-v(L)\le2S$. If $D\ge2(r-1)$, every $L$ with $S<r$ automatically gives valid nonnegative $q$ and $a$ multiplicities. All missing patterns are therefore counted by the finite product generating function $G$, giving the exact coefficient law.

Sharpness for $r\ge3$ follows from the type $(h,d,v)=(0,2,2)$ with $s=1$. The multiset of $r-1$ such letters has deficit $2r-2$ and hence cannot exist at $D=2r-3$; it is a distinct positive contribution to $C_r$. Finally $G(z)/(1-z)$ has a pole of order 24 at $z=1$ and no equally high pole elsewhere; the denominator periods divide $\mathrm{lcm}(1,\ldots,7)=420$, and the product of the 23 slack weights is $94,058,496,000$, establishing the quasi-polynomial and leading term.

For Theorem C, pair a multiset in $A_0$ with its identical source multiplicities in $A_1$, substituting only the optional letter. This bijection preserves $(n,U,V)$ and shifts $H$ by $k\ge0$. Its transportation cost averages to $W_{n,D}/(20nN_{n,D})$. The mean-$H$ gap yields the same value as a Kantorovich dual lower bound for the one-dimensional ground metric. Equality follows. Theorem A's unique late pattern proves sharp numerator saturation.

## Exact reproduction and evidence

The attached dependency-free Python 3 checker reconstructs the first-grid alphabet from the eight facets and unique two-source sums; applies integer multiset DP for all $D=2,\ldots,12$; checks the exact signed cutoff and noncancellation, penultimate mass and numerator claims, and independently enumerates slack weights and $C_1,\ldots,C_8$ at and just below the sharp deficit thresholds. All operations use exact integers and rational fractions. The universal quantifiers rest on the symbolic proof above, not on a finite run.

Fresh values: $D=10$ gives $N_{10}=51968,W_{10}=11244$ and for $n\ge20$, $W_1^{TV}=2811/(259840n)$. $D=12$ gives $N_{12}=243454,W_{12}=63212$ and for $n\ge24$, $W_1^{TV}=15803/(1217270n)$. The preexisting $D=2,4,6,8$ exact values are reproduced.

## Status and open frontier

Author-level exact mathematical result; underlying R749SPR/SPU source classification is still author-level, not independently reviewed. No Result, Review, native X6 equivalence, Working Truth or Foundation promotion is asserted. Continue by computing the **H-resolved** boundary-layer correction at fixed $r$ and high $D$, then seek the minimal BRC provenance residual required to reconstruct it; native signed X6 event/Port bridge remains independently open.