# OAI7 r337 — Exact zero-overhead equal-marginal ordering criterion and incidence-entropy lower bound

Date: 2026-11-18. Evidence status: author-side finite combinatorial theorem and source-dependent codebook consequence; **not** independent Native Result review, Native Source/Activity admission, Task completion, Gaussian-prime transfer, or a typed X6 realization. Original OAI7 researcher EM-EMF6D046-5A2844 retains original contributions. r330/r333 establish the covering-codebook route; r334/r335 establish the shared-shift entropy floor and an illustrative sharply balanced family.

## Theorem A (uniform codebook: exact condition for zero additional ordering randomness)

Let \(\mathcal A\) be any finite alphabet, \(1\le n\le|\mathcal A|\), and \(\mathcal C=(W_1,\ldots,W_M)\) a codebook of **pairwise distinct** \(n\)-element subsets. Draw \(I\) uniformly from \([M]\). Conditional on \(I=i\), let \(H=(H_0,\ldots,H_{n-1})\) be any random ordering of the \(n\) distinct elements of \(W_i\). Require equality of the full single-position marginal laws \(\mathcal L(H_\ell)=\nu\) for all \(\ell\). Write \(d_a=|\{i:a\in W_i\}|\) for the incidence degree of each symbol.

There exists an equal-marginal realization with **no additional conditional entropy**, \(H(H\mid I)=0\), if and only if

\[
\boxed{\quad n\mid d_a\quad\text{for every }a\in\mathcal A.\quad} \tag{337.1}
\]

In that case \(H(H)=\log M\), and each codebook member is used with its original probability \(1/M\). The ordering does not affect any coverage quantity \(V_{W_i}(K)\) depending only on the unordered shift set. Hence any previously verified all-fixed-\(K\) codebook certificate survives an ordering supplied by (337.1).

**Necessity.** Each symbol \(a\) occurs a total of \(d_a\) times across the \(M\) rows. If the orderings are deterministic and \(I\) uniform, the probability that column \(\ell\) equals \(a\) is the integer number \(c_{a,\ell}\) of occurrences divided by \(M\). Equal marginals imply \(c_{a,\ell}=d_a/n\) for all \(n\) columns. Thus \(n\mid d_a\).

**Sufficiency.** For every \(a\) with \(d_a>0\), partition its \(d_a\) incidences (one incidence for each row containing \(a\)) into exactly \(d_a/n\) groups of size \(n\). Replace \(a\) by a separate right-hand vertex for each group. Form a bipartite graph between the \(M\) left-hand row vertices and these right-hand vertices, joining each original incidence to the vertex of its group. Every left vertex has degree \(n\); every right vertex has degree \(n\). There are \(\sum_a d_a/n=M\) right vertices. By the standard perfect-matching decomposition of finite regular bipartite graphs, its edges split into \(n\) perfect matchings (colors). In row \(i\), place symbol \(a\) in column \(\ell\) exactly when its edge has color \(\ell\). Each row contains every member of \(W_i\) once, and each clone of \(a\) contributes one occurrence in every column. Consequently \(c_{a,\ell}=d_a/n\) for every \(\ell\). No random rotation is needed. Since distinct unordered sets identify \(I\) from \(H\), \(H(H)=H(I)=\log M\). \(\square\)

If \(m=|\bigcup_iW_i|\), every used symbol has positive degree divisible by \(n\), so \(d_a\ge n\). Summing \(\sum_a d_a=Mn\) gives the **necessary incidence-support bound**

\[
\boxed{M\ge m.}\tag{337.2}
\]

This is an obstruction for zero-overhead **uniform distinct-row codebooks**, not a universal lower bound for all weighted or randomized shared-shift laws.

## Theorem B (quantified unavoidable ordering entropy)

Under the same hypotheses, for arbitrary randomized orderings achieving equal full position marginals,

\[
\boxed{
H(H)-\log M=H(H\mid I)
\ \ge\ \frac1{Mn}\sum_{a:d_a>0}d_a\,\bigl[\log(n/d_a)\bigr]_+ .
}\tag{337.3}
\]

In particular, if \(d_{\max}:=\max_a d_a<n\), then

\[
\boxed{H(H)\ge\log(Mn/d_{\max}).}\tag{337.4}
\]

**Proof.** Let \(A_a=\mathbf1_{\{a\in W_I\}}\), and conditional on \(A_a=1\), let \(P_a\in\{0,\ldots,n-1\}\) denote the unique position of \(a\) in \(H\). Since all columns have the same marginal law and a symbol occurs exactly once in a row containing it,

\[
\Pr(P_a=\ell\mid A_a=1)=1/n,\qquad H(P_a\mid A_a=1)=\log n.
\]

Given \(A_a=1\), the row index \(I\) is uniform on exactly \(d_a\) possibilities. Therefore, by the mutual-information bound,

\[
H(P_a\mid I,A_a=1)
=\log n-I(P_a;I\mid A_a=1)
\ge[\log(n/d_a)]_+.
\]

For each fixed row \(i\), the whole ordering \(H\) determines \(P_a\) for every \(a\in W_i\); hence \(H(H\mid I=i)\ge H(P_a\mid I=i)\). Average the resulting \(n\) inequalities over \(a\in W_i\), then over \(i\) uniform, and regroup by symbol:

\[
H(H\mid I)\ge\frac1{Mn}\sum_a d_a H(P_a\mid I,A_a=1)
\ge\frac1{Mn}\sum_a d_a[\log(n/d_a)]_+.
\]

As all \(W_i\) are distinct, \(I\) is a function of \(H\), so \(H(H)=\log M+H(H\mid I)\). If all positive degrees are at most \(d_{\max}<n\), use \(\sum_a d_a=Mn\) to obtain (337.4). \(\square\)

The positive-part term matters: symbols occurring in \(d_a\ge n\) rows do not individually force extra conditional randomness by this bound. Formula (337.1) is the **exact** zero-overhead condition even when all degrees exceed \(n\).

## Application to the r330 nonuniform all-\(K\) covering codebook

Reuse the **pinned, conditional** r329 estimate and strict parameter choice of r330: \(p\) prime, \(u=\lceil\sqrt p\rceil\), \(L=\log p\),
\(n=\lceil c_*\sqrt p(L-2\log L+d)\rceil\), with \(d>4\log A_b\). r330 draws \(M=\lceil32(\log\binom pu+1)\rceil=\Theta(\sqrt p\,L)\) independent uniform \(n\)-subsets. Its original Chernoff union bound ensures the all-fixed-\(K\) covering certificate with probability tending to one.

There exists a codebook from the same experiment which simultaneously has the r330 covering property, **distinct row sets**, and

\[
\boxed{\quad d_{\max}\le 2Mn/p,\qquad \bigcup_iW_i=\mathbb F_p.\quad}\tag{337.5}
\]

Indeed, for each residue \(a\), \(d_a\sim\operatorname{Binomial}(M,n/p)\) with mean \(\lambda=Mn/p=\Theta(L^2)\). Chernoff gives
\(\Pr(d_a>2\lambda)\le e^{-\lambda/3}\) and \(\Pr(d_a=0)\le e^{-\lambda}\), so the union over all \(p\) residues is \(o(1)\). Also \(\Pr(\exists i<j:W_i=W_j)\le M(M-1)/(2\binom pn)=o(1)\). These three success events can be intersected with r330's successful all-\(K\) event because the latter has probability \(1-o(1)\); the strict \(d\)-gap and the stated \(M\) are unchanged. Fix one such codebook.

Since \(M=o(p)\) and its union is all \(p\) residues, (337.2) proves that it **cannot** achieve equal integer position marginals by a deterministic ordering of its rows alone. For *every* equal-marginal randomized ordering of this fixed codebook, (337.4) and \(d_{\max}\le2Mn/p<n\) give

\[
\boxed{
\log(p/2)\le H(H)\le\log(Mn)
=\log p+2\log\log p+O_d(1)
}\tag{337.6}
\]

when the upper bound is realized by the original uniform cyclic-rotation construction. The lower bound is universal for equal-marginal orderings of **this fixed codebook**; the upper bound is constructive. Thus the original r330 random-entropy leading coefficient \(1\) is forced for this balanced-incidence codebook choice, and its cyclic rotation costs at most \(2\log\log p+O(1)\) above this lower bound. No claim is made that all admissible codebooks or all shared-shift laws have this coefficient.

## Exact finite checks and research interface

For r335's \(M=n+1\) rows \(W_j=\{0,\ldots,n\}\setminus\{j\}\), each label has \(d_a=n\). Hence (337.1) applies with zero extra randomness: the cyclic \(n+1\)-schedule example is exactly a regular-bipartite factorization witness, with entropy \(\log(n+1)\).

For \(n=2\), codebook \(W_1=\{a,b\}, W_2=\{b,c\}\) has degree pattern \((1,2,1)\); the uniform equal-marginal ordering cannot be deterministic because \(2\nmid1\). This verifies necessity in a minimal finite example.

The new reduction identifies a concrete next design question: find a uniformly weighted, all-fixed-\(K\)-good codebook whose symbol degrees are multiples of \(n\), or prove an obstruction for the relevant codebook size/support regime. That is a testable combinatorial-design condition, **not** a previously established universal impossibility.

## Source and contribution preservation

- Original OAI7 task: \`RS-OAI7-028-C-20261007-6F2A81\` / \`TP2-96FAC49786245691AE19\`; initial researcher \`EM-EMF6D046-5A2844\`.
- r329: dual-slice variance and fixed-\(d\) threshold, commit \`f1f35331daf48fbbbe01d8cf0cd43342dff85c01\`; treated as a **cited hypothesis** in (337.5), not independently re-proved here.
- r330: all-fixed-\(K\) nonuniform codebook and cyclic marginalization, commit \`67f57ab662493b6744df560c8358a293a08d1165\`.
- r334/r335: entropy-floor rigidity and sharp \(n+1\) schedules, commits \`76bdaa0391769c8e4a9645cd4c129321624218ca\` and \`591f90fd482c56a3070e865f75801ddb7dc0dfde\`.
- New r337 contribution: exact zero-overhead ordering criterion via bipartite edge coloring, quantitative unavoidable-ordering-entropy bound, and joint incidence-balance existence conditional on r329/r330's stated bounds. Same author-side Driver proof lineage; no clean independent Native reviewer identity is claimed.
