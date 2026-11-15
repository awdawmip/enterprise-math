# R749SPY — An infinite family of Walsh source-fiber sign re-entry and eventual boundary stabilization

Date: 2026-11-15. Status: **AUTHOR_EXACT_NOT_REVIEWED**. Scientific pin: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Independent continuation of R749SPR–SPX, restricted to the auxiliary 16-atom Walsh center model at \((t,s)=(1/10,1/2)\). Source branch/PR: \`research/r749spx-conditional-tail-flux-20261115\`, Draft PR #2477.

## 1. Exact theorem

Let \(F\) denote the forced 25-point first-grid alphabet of R749SPU, \(A_0=F\cup\{(0,0,0)\}\) and \(A_1=F\cup\{(-1,0,0)\}\). Let \(M_j(n,H,U,V)\) be the exact multiplicity of source multisets of size \(n\) with summed coordinates \((H,U,V)\). Put \(D_n=M_0-M_1\).

**Theorem A (stable signed boundary profile).** For **every integer \(n\ge9\)**, on the moving lattice slice \((U,V)=(2n-6,0)\), the entire nonzero pointwise fiber difference is independent of \(n\) and equals

| H | -5 | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(D_n(H,2n-6,0)\) | -15 | -9 | -13 | +3 | -6 | +18 | +9 | +9 | +1 | +3 |

For every other integer \(H\), the difference is zero. Thus, at **every precision \(n\ge9\)**, the same source slice has the three alternating signs
\[
D_n(-2,2n-6,0)=3>0,\quad
D_n(-1,2n-6,0)=-6<0,\quad
D_n(0,2n-6,0)=18>0.
\]
The pointwise source-fiber ordering therefore has infinitely many exact re-entry witnesses. This extends R749SPX's finite \(n=3\) counterexample to an all-\(n\ge9\) family.

**Theorem B (saturated slice mass and conditional transport).** For every \(n\ge12\), each of the two alphabets has exactly **1468** size-\(n\) source multisets on the moving slice \((U,V)=(2n-6,0)\); among them the optional-slot count has sum **192**. Consequently,
\[
\mathbb E[K_n\mid U=2n-6,V=0]=\frac{48}{367},
\]
and the conditional normalized Walsh-center transport metric from R749SPX is exactly
\[
\boxed{W_1^{TV}(\mu_{0,n}\mid U=2n-6,V=0,\,
\mu_{1,n}\mid U=2n-6,V=0)=\frac{12}{1835n}.}
\]

## 2. Finite-deficit proof for every n

Write \(d(f)=2-u(f)\) for a forced source letter \(f=(h,u,v)\). The 25 types have precisely two zero-deficit letters
\[
a=(-1,2,-1),\qquad b=(0,2,0).
\]
The other 23 forced types have \(d(f)\ge1\) and satisfy the **checked finite inequality** \(v(f)\le d(f)\). The last optional slot, whether \((0,0,0)\) or \((-1,0,0)\), contributes deficit 2 and \(v=0\).

On the moving slice \(U=2n-6\), the total deficiency is exactly 6. Condition on \(k\) occurrences of the optional slot. Then \(0\le k\le3\), and the remaining 23 positive-deficit forced types form a multiset \(c\) with
\[
D(c)=\sum_{f\in c}d(f)=6-2k,\quad
m=|c|,\quad h=\sum_{f\in c}h(f),\quad v=\sum_{f\in c}v(f).
\]
The \(V=0\) condition forces exactly \(v\ge0\) copies of \(a\), as it is the only zero-deficit letter contributing \(V=-1\). The remaining \(n-k-m-v\) sources must all be copies of \(b\); this completion is unique.

Because \(m\le D(c)\) and \(v\le D(c)\), every such \(c\) with \(k\ge1\) can be completed for all
\[
n\ge k+m+v\le k+2(6-2k)=12-3k\le9.
\]
Thus for **all \(n\ge9\)**, each possible positive-deficit multiset with \(k\ge1\) occurs exactly once (per multiset of letters) in both alphabets. In \(A_0\) it contributes \(H=h-v\); in \(A_1\) it contributes \(H=h-v-k\). The \(k=0\) terms cancel in the difference, leaving the finite exact formula
\[
\boxed{D_n(H,2n-6,0)=
\sum_{k=1}^{3}
\sum_{\substack{c\text{ multiset of 23 types}\\D(c)=6-2k,\ v(c)\ge0}}
\left(\mathbf1_{\{H=h(c)-v(c)\}}
-\mathbf1_{\{H=h(c)-v(c)-k\}}\right),\quad n\ge9.}
\]

For the complete slice mass, include \(k=0\): here \(D(c)=6\), so \(k+m+v\le12\). All alphabets therefore saturate at \(n\ge12\).

## 3. Exact finite coefficient evaluation

The finite expression above is exhaustively evaluated by a direct integer dynamic program with deficit \(D\le6\). Each of the 23 distinct positive-deficit types can occur with any nonnegative multiplicity; unbounded-coin recurrence over increasing deficit includes all and only unordered source multisets. The accepted counts after requiring \(v\ge0\) are:

| optional count k | remaining deficit 6-2k | valid positive-deficit multisets | maximal minimum n |
|---:|---:|---:|---:|
| 0 | 6 | 1292 | 12 |
| 1 | 4 | 161 | 9 |
| 2 | 2 | 14 | 6 |
| 3 | 0 | 1 | 3 |

Summing the k=1,2,3 indicator differences gives precisely Theorem A's ten-term signed vector, whose sum is zero. Summing all four counts gives \(1292+161+14+1=1468\), and the optional-count total is \(161+2\cdot14+3=192\). Theorem B then follows from the conditional Wasserstein identity proved in R749SPX. This proof is valid for arbitrary \(n\) above the stated thresholds, since the remaining parameter \(n\) only determines the unique number of \(b\) fillers.

**Reproduction.** Execute the dependency-free \`R749SPY_WALSH_BOUNDARY_SIGN_STABILIZATION_CERT.js\`. It regenerates \(F\) from the eight exact facets, checks the zero-deficit alphabet and positive-deficit inequality, exhausts every deficiency class \(D=0,\ldots,6\), checks 1292/161/14/1, all stabilization thresholds and the signed profile, and emits \`R749SPY_WALSH_BOUNDARY_SIGN_STABILIZATION_RESULTS.json\`. The actual integer computation returned PASS, independently consistent with complete multiset enumeration at \(n=9,\ldots,14\).

**Scope and continuation.** This is an exact model-internal provenance theorem. It inherits R749SPR/SPU's author-level classification of the minimizing Walsh center and forced alphabet. Next, derive the largest/sign-chamber structure at other fixed-deficiency boundary slices, and test whether a finite family of saturation profiles controls maximal-fiber ordering. The native signed Port/Cell observer bridge remains independently open.
