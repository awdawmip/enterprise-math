# R749SPZ — Uniform finite-deficit stabilization of Walsh provenance fibers

Date: 2026-11-15. Status: **AUTHOR_EXACT_NOT_REVIEWED**. Research mode: independent portable TASK_RESEARCH. Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`; predecessors R749SPR, R749SPU, R749SPX and R749SPY, especially PR #2477 @ \`61d61f6b8a58306cfcb9788ec549508cc2f84118\`. Scope: **auxiliary signed 16-atom Walsh optimal-center source model** at \((t,s)=(1/10,1/2)\); no native X6 operator/port identification is asserted.

## 1. Statement: every fixed deficit stabilizes

Let \(K\subset\mathbb R^3\) be the previously classified full optimal-center polytope in first-grid coordinates \((H,U,V)\). Let \(F\subset K\cap\mathbb Z^3\) be the 25 forced first-grid source types recovered from unique unordered pair targets (the exact generation algorithm is in the attached checker). Set
\[
A_0=F\cup\{(0,0,0)\},\quad A_1=F\cup\{(-1,0,0)\}.
\]
For \(j\in\{0,1\}\), let \(M_j(n,H,U,V)\) count *unordered multisets of exactly \(n\) types* from \(A_j\) whose coordinate sum equals \((H,U,V)\). For an arbitrary integer deficit \(D\ge2\), define the boundary signed fiber profile
\[
D_{n,D}(H)=M_0(n,H,2n-D,0)-M_1(n,H,2n-D,0).
\]

**Theorem 1 (uniform arbitrary-deficit stabilization).** For each integer \(D\ge2\), the entire finite signed sequence \(H\mapsto D_{n,D}(H)\) is exactly independent of \(n\) whenever
\[
\boxed{n\ge 2D-3.}
\]
Both unsigned boundary-fiber masses are identical for every \(n\), and each becomes exactly constant in \(n\) for
\[
\boxed{n\ge 2D.}
\]
The mass threshold \(2D\) is sharp as a cutoff guaranteeing that *all* admissible finite-deficit source patterns have appeared: the full mass is strictly smaller at \(n=2D-1\). The signed threshold \(2D-3\) is a universal sufficient bound (not claimed sharp for every \(D\)).

More explicitly, let \(B=\{f=(h,u,v)\in F:u<2\}\) (23 distinct letters), with positive deficit \(d(f)=2-u\). The zero-deficit types in \(F\) are exactly \(a=(-1,2,-1)\) and \(b=(0,2,0)\); all \(f\in B\) satisfy \(1\le d(f)\le4\) and \(v(f)\le d(f)\).

For any unordered multiset \(c\) of \(B\), write \(\delta(c)=\sum d(f)\), \(m(c)=|c|\), \(h(c)=\sum h(f)\), \(v(c)=\sum v(f)\). Define the finite polynomial
\[
\boxed{
P_D(z)=\sum_{k=1}^{\lfloor D/2\rfloor}
\sum_{\substack{c\in \operatorname{Multiset}(B)\\
\delta(c)=D-2k,\;v(c)\ge0}}
\left(z^{h(c)-v(c)}-z^{h(c)-v(c)-k}\right).
}
\]
Then for every \(n\ge2D-3\), \(D_{n,D}(H)=[z^H]P_D(z)\) (Laurent coefficients; no limiting approximation).

Define the finite nonnegative integers
\[
N_D=\sum_{k=0}^{\lfloor D/2\rfloor}\sum_{\delta(c)=D-2k,\ v(c)\ge0}1,\qquad
W_D=\sum_{k=0}^{\lfloor D/2\rfloor}\sum_{\delta(c)=D-2k,\ v(c)\ge0}k.
\]
For all \(n\ge2D\), each source alphabet has exactly \(N_D\) boundary multisets. The paired optional-slot count has total \(W_D\). Hence the conditional Walsh-TV metric Wasserstein-1 distance between *uniform* source-multiset-induced center distributions on \(U=2n-D,V=0\) is exactly
\[
\boxed{W_1^{TV}=\frac{W_D}{20nN_D},\qquad n\ge2D.}
\]
Here the distance of center reads differing only in first-grid \(H\) by \(\Delta H\) is \(|\Delta H|/(20n)\). The coordinatewise pairing shifts \(H\) by \(k\ge0\), giving an optimal one-dimensional monotone transport. These two measures have equal total mass because the alphabets differ only in the \(h\)-coordinate of the optional letter.

## 2. Proof

Every source letter \(f\in F\) has \(u\le2\); the optional letter has \(u=0\), so its deficit is 2. For fixed \(n,D\), let \(k\ge0\) be the optional-letter count and \(c\) the multiset of positive-deficit forced types. The equation \(U=2n-D\) forces \(\delta(c)=D-2k\), so only finitely many \(c\) and \(0\le k\le\lfloor D/2\rfloor\) are possible.

Let \(\alpha\) and \(\beta\) count zero-deficit letters \(a,b\). As \(V=0\), the exact source balance gives \(\alpha=v(c)\), requiring \(v(c)\ge0\). The length equation then uniquely forces \(\beta=n-k-m(c)-v(c)\). This source pattern exists exactly when
\[
n\ge n_{\min}(k,c):=k+m(c)+v(c).
\]
Because every positive-deficit letter satisfies \(d\ge1\) and \(v\le d\), we have \(m(c)\le D-2k\) and \(v(c)\le D-2k\); hence
\[
n_{\min}(k,c)\le k+2(D-2k)=2D-3k.
\]
For \(k\ge1\), all patterns have therefore appeared by \(n=2D-3\). Each contributes one source multiset to each alphabet: its \(H\)-value is \(h(c)-v(c)\) in \(A_0\), respectively \(h(c)-v(c)-k\) in \(A_1\). The \(k=0\) patterns contribute identically and cancel for *every* \(n\). This proves the stable signed polynomial formula.

Including \(k=0\) gives the uniform bound \(n_{\min}\le2D\), proving saturation of the unsigned masses. The letter \((0,1,1)\in B\) has \(d=v=1\); taking \(D\) copies and \(k=0\) gives \(m=v=D\), hence \(n_{\min}=2D\). Therefore the full mass at \(n=2D-1\) lacks at least this source pattern, proving sharpness of the *pattern and mass* cutoff.

At \(n\ge2D\), the uniform pairing of source multisets preserves \(U,V\) and changes \(H\) by exactly \(k\ge0\). The Walsh-TV cost for the fixed \(U,V\) fiber is \(|\Delta H|/(20n)\), and Kantorovich duality on the line gives equality of the pairing cost and the mean-coordinate gap, namely \(W_D/(20nN_D)\). This proves the transport formula.

## 3. New exact D=8 boundary census

The integer DP described below establishes for the previously unclassified slice \(U=2n-8,\ V=0\):
- The full signed profile is constant for every \(n\ge13\), with nonzero coefficients
  \[
  \begin{array}{c|rrrrrrrrrrrrrr}
  H&-7&-6&-5&-4&-3&-2&-1&0&1&2&3&4&5&6\\\hline
  D_{n,8}(H)&-40&-42&-78&-56&-78&17&32&86&50&63&24&16&2&4
  \end{array}
  \]
  and zero elsewhere. The sum of signed coefficients is 0 and \(\sum_H H D_{n,8}(H)=1660\).
- Accepted positive-deficit multiset counts by optional count \(k=0,1,2,3,4\): \(8116,1292,161,14,1\). Therefore \(N_8=9584\) and \(W_8=1660\).
- For every \(n\ge16\), conditional \(W_1^{TV}=\boxed{83/(9584n)}\).
- An independent full length-and-deficit coefficient DP gives unsigned masses 9542 at \(n=12\), 9570 at \(n=13\), and 9584 at \(n=16\), equal for both alphabets; the signed profile differs at \(n=12\) and stabilizes at \(n=13\).

For comparison, the same checker reproduces \(D=2\) (signed profile \(-z^{-1}+1\), mass 15), \(D=4\) (\(-4z^{-3}+2+2z^2\), mass 176), and R749SPY's \(D=6\) ten-term signed vector and mass 1468. Thus the special \(D=6\) triple sign re-entry is one member of a general eventually stable coefficient family; \(D=8\) exhibits a different sign pattern.

## 4. Reproduction and evidence scope

Run \`node R749SPZ_ALL_DEFICIT_WALSH_STABILIZATION_CERT.js > R749SPZ_ALL_DEFICIT_WALSH_STABILIZATION_RESULTS.json\` on Node.js. The dependency-free program regenerates all 33 first-grid lattice points from eight exact facets, independently regenerates the 25 forced types through unique unordered pair targets, performs finite unbounded-multiset integer DP by deficit, and separately performs complete fixed-length coefficient extraction over all 26 types. It checks \(D=2,4,6,8\), the exact signed threshold behavior and unsigned masses at the given lengths, and the existing \(D=6\) certificate before returning PASS. Arithmetic is exact nonnegative integers within JavaScript's safe-integer range for these displayed values; no floating numerical tolerance or stochastic sampling is used. The all-\(D\) theorem is the preceding symbolic argument, *not* an inference from the finite DP range.

The original frozen model and predecessor's classification of \(K\) and \(F\) are inherited author-level scientific premises, not independently reviewed native X6 claims. No shared claim or formal Result/Review is asserted. This note provides a self-contained continuation of the finite-deficit argument at their declared scope.

## 5. Open frontier

Determine the coefficient sign-chamber diagram in \(D\) for \(P_D(z)\) (the \(D=6\) local re-entry disappears at \(D=8\)); identify a generating-function or quasipolynomial description of \(N_D,W_D\) and sharp transitions. Separately, seek an explicit provenance- and operation-preserving bridge from this auxiliary source model to the native X6 signed-Port/Cell observer, with no assumed quotient equivalence.
