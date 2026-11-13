# R749SMZ — Exact zero-fiber Walsh minimax radius for sum-free omitted families

Date: 2026-11-13 (Asia/Shanghai). Lineage: R749SMQ–R749SMY. Frozen scientific input is still \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Author-side analytical proof and exact finite check; independent scientific review pending. This is an auxiliary signed-source observer, not a native X6/V29/V39 event.

## Statement (all finite dimensions)

Let \(G=\mathbb F_2^d\), \(d\ge1\), with characters \(\chi_a(x)=(-1)^{a\cdot x}\). Fix a nonempty omitted family \(C\subseteq G\setminus\{0\}\) satisfying the **sum-free condition**
\[
a,b\in C,\quad a\ne b\quad\Longrightarrow\quad a\oplus b\notin C.
\]
Retain all other nonconstant Walsh moments \(B=G\setminus(C\cup\{0\})\) at value zero. Define
\[
F_C=\{\mu\in\Delta(G):\ \mathbb E_\mu\chi_b=0\ \forall b\in B\},\qquad
R_C=\min_{q\in\Delta(G)}\max_{\mu\in F_C}\operatorname{TV}(q,\mu).
\]

**Theorem:** \(\boxed{R_C=1/2}\). The uniform distribution \(U\) is an optimal decoder. This holds for arbitrary real-valued compatible source laws and any \(d\ge1\), independent of the number of omitted characters and possible higher-order linear dependencies among them.

## Complete proof

Write \(N=2^d\). Walsh inversion yields the unique form
\[
\mu(x)=N^{-1}\bigl(1+\sum_{a\in C}m_a\chi_a(x)\bigr),\qquad
m_a=\mathbb E_\mu\chi_a.
\]
Let \(X=(\chi_a)_{a\in C}\). For \(a\ne b\), the sum-free condition places \(a\oplus b\) in \(B\), giving \(\mathbb E_\mu X_aX_b=0\); every diagonal is one. Therefore \(\mathbb E_\mu XX^\top=I\), and
\[
I-mm^\top=\operatorname{Cov}_\mu(X)\succeq0
\quad\Longrightarrow\quad \sum_{a\in C}m_a^2\le1.
\]
By Walsh orthogonality under \(U\) and Cauchy–Schwarz,
\[
\operatorname{TV}(\mu,U)
=\frac12\mathbb E_U\bigl|\sum_{a\in C}m_a\chi_a\bigr|
\le\frac12\sqrt{\sum_{a\in C}m_a^2}
\le\frac12.
\]
This gives the explicit upper bound. For any \(c\in C\), the two valid laws
\[
\mu_\pm(x)=N^{-1}(1\pm\chi_c(x))
\]
retain all required zero moments, and their supports are disjoint; hence \(\operatorname{TV}(\mu_+,\mu_-)=1\). The triangle inequality forces any decoder's worst-case error to be at least \(1/2\), proving equality.

## Future observer and exact deletion condition

For an arbitrary finite stochastic kernel \(K:Y\leftarrow G\), let
\[
\widehat K(y,c)=N^{-1}\sum_{x\in G}K(y\mid x)\chi_c(x),\qquad
R_C(K)=\min_{r\in\Delta(Y)}\max_{\mu\in F_C}\operatorname{TV}(r,K\mu).
\]
Since \(K\mu=KU+\sum_{c\in C}m_c\widehat K(\cdot,c)\), and the above \(\mu_\pm\) are in the fiber,
\[
\boxed{\frac12\max_{c\in C}\sum_y|\widehat K(y,c)|\le R_C(K)\le\frac12.}
\]
In particular, **exact future losslessness** of deleting all \(C\) moments is equivalent to
\[
\boxed{R_C(K)=0\iff\widehat K(y,c)=0\quad\forall y,c\in C.}
\]
If the future observer is \(K_\lambda(y\mid x)=(1+y\lambda\chi_c(x))/2\) with \(y=\pm1\) and \(|\lambda|\le1\), then \(\boxed{R_C(K_\lambda)=|\lambda|/2}\) exactly.

## Exact five-circuit corollary and sharp necessity example

In the existing R749SMX/R749SMY auxiliary model \(G=\mathbb F_2^4\), set
\[
C=\{1,2,4,8,15\},\quad B=\{3,5,6,7,9,10,11,12,13,14\}.
\]
Every pairwise XOR of distinct elements of \(C\) is in \(B\). At the zero retained-moment origin \(m_b=0\) for all ten \(b\in B\), including \((t,s)=(0,0)\), the exact previously unresolved anchor is
\[
\boxed{\rho_B(0,0)=1/2.}
\]
Here the sharp lower witness is \((1\pm\chi_{15})/16\), and the exact minimax decoder is uniform on all 16 states.

The sum-free condition has substantive force: for \(G=\mathbb F_2^2\), \(C=\{1,2,3\}\) violates \(1\oplus2\notin C\). With no nonzero retained moment, the fiber is the full four-state simplex, whose Chebyshev TV radius is \(3/4>1/2\).

## Reproduction, status and next question

\`R749SMZ_SUMFREE_WALSH_ORIGIN_EXACT_CHECK.py\` uses only integer Walsh characters and standard-library \`fractions.Fraction\`, with the real output in \`R749SMZ_SUMFREE_WALSH_ORIGIN_RESULTS.json\`. It returned **PASS**. The full origin five-dimensional polytope has 16 nonnegativity constraints: enumerating all \(\binom{16}5=4368\) active subsets gives 3,008 nonsingular systems, 336 feasible systems and **26 distinct rational vertices**. All vertices independently satisfy the ten retained moments and \(\|m\|_2^2\le1\); maximum TV from uniform is \(1/2\), attained by 10 vertices. Also checked the explicit extremal pair and noisy binary observer for rational biases in dimensions 2, 3 and 4. The general result follows from the analytic proof, not from this finite enumeration.

The next concrete target is an exact axis-wide or piecewise-parametric derivation of \(\rho_B(t,0)\) and \(\rho_B(0,s)\), then the complete interior phase diagram \(\rho_B(t,s)\), using previous exact points \((1/2,1/2)\) and \((1/3,1/3)\). A numerical axial pattern alone remains a conjecture. Native V29/V39 correspondence and independent review remain open. No shared Task CLAIM or Foundation admission is asserted by this auxiliary theorem.
