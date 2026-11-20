# R5 — Exact all-cost nonadaptive mixed-fault spectrum by a finite rational generating function

**Date 2026-11-20. Author-side symbolic proof and finite coefficient validation; NOT_REVIEWED.** Independent portable R5 continuation, using unchanged frozen 256-hypothesis scalar query evidence \`awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551\`, \`EXACT_R5_ALL_101_BUDGETS.json\` SHA-256 \`50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b\` and the same five complete minimal separating sets as the predecessor.

## Statement

Fix any nonnegative integers \(f,e\) and put \(m=2f+e+1\). Queries are **nonadaptive**, chosen as an unordered multiset of integer-priced labels \(214,\ldots,314\), repetitions allowed. A query multiset is uniquely decodable against at most \(f\) unflagged arbitrary errors and \(e\) flagged erasures exactly when all five minimal separating-set cardinalities are at least \(m\).

Let \(U_A(q)=\prod_{k\in A}(1-q^k)^{-1}\). For any interval \(I=[p,p+r]\) of consecutive query prices and \(n\ge0\), define the **size-at-least-\(n\)** tail
\[
T_{I,n}(q)=U_I(q)-\sum_{j=0}^{n-1}q^{pj}G_{j,r}(q),
\qquad G_{j,r}(q)=\left[\begin{smallmatrix}j+r\\r\end{smallmatrix}\right]_q.
\]
The finite subtraction is empty when \(n=0\), so \(T_{I,0}=U_I\). Let \(D_s=T_{[219,221],s}\) and \(H_0=U_{\{214,215\}}D_0\). For \(s\ge1\), define
\[
\begin{aligned}
H_s={}&\frac{q^{429s}}{(1-q^{214})(1-q^{215})}D_0\\
&+\frac{q^{214s}}{1-q^{214}}\sum_{b=0}^{s-1}q^{215b}D_{s-b}\\
&+\frac{q^{215s}}{1-q^{215}}\sum_{a=0}^{s-1}q^{214a}D_{s-a}\\
&+\sum_{\substack{0\le a,b<s\\a+b\ge s}}
q^{214a+215b}D_{\max(s-a,s-b)}.
\end{aligned}
\]
All these are explicitly rational power series, built from finite sums and products. Set
\[
E_m=T_{[216,218],m}H_0+
\sum_{c=0}^{m-1}q^{216c}G_{c,2}H_{m-c},
\quad
M_m=T_{[223,290],m},
\quad L_m=T_{[296,312],m},
\]
and define the eight support-null prices
\(O=\{222,291,292,293,294,295,313,314\}\).

**Exact all-excess theorem:** for **every integer \(D\ge0\)**, the number \(a_m(D)\) of feasible unordered query multisets of total price \(735m+D\) is
\[
\boxed{
a_m(D)=[q^{735m+D}]
\ E_m(q)M_m(q)L_m(q)U_O(q).
}
\]
This is a finite rational-function expression for the **entire cost spectrum**, with no upper cut-off on \(D\) or \(m\). Its construction uses only \(O(m^2)\) finite summand terms (up to the polynomial sizes of \(G\)) and the five frozen separating constraints; it does not enumerate all 256 hypotheses again for each cost or require an adaptive Bellman tree.

**Structural consequences (for each fixed \(m\ge1\)):**

1. The cost series has zero coefficients below \(735m\), consistent with the unique optimum from the predecessor. The prior sharp low-excess formula through \(D=425\) is the reduction of this rational expression modulo \(q^{735m+426}\).
2. Since every denominator is a product of factors \(1-q^k\) with \(k\in\{214,\ldots,314\}\), the sequence \(D\mapsto a_m(D)\) is eventually quasipolynomial, with a period dividing \(\operatorname{lcm}(214,\ldots,314)\).
3. As \(D\to\infty\) at fixed \(m\),
\[
\boxed{a_m(D)\sim\frac{D^{100}}{100!\prod_{k=214}^{314}k}.}
\]
Equivalently, among all unordered priced query multisets at a very large exact cost, the proportion satisfying the fixed five robust-separation requirements tends to one. This asymptotic is in the **number of fixed nonadaptive query designs**, not a performance or native-world dynamics claim.

## Full proof

The early query group \(\{214,\ldots,221\}\) has three separating constraints. Write \(a,b\) for the counts of 214 and 215, \(c\) for the total count in \(\{216,217,218\}\), and \(d\) for the total count in \(\{219,220,221\}\). The constraints are
\(a+b+c\ge m,\ a+c+d\ge m,\ b+c+d\ge m\).

When \(c\ge m\), the partial prices 214,215,219..221 are wholly unconstrained. The generating function of these partial prices is \(H_0\), and the generating function of central prices with at least \(m\) occurrences is \(T_{[216,218],m}\). This gives the first term of \(E_m\).

When \(0\le c<m\), put \(s=m-c\). We need \(a+b\ge s,\ a+d\ge s,\ b+d\ge s\). Partition \((a,b)\) into the four disjoint regions:
- \(a\ge s,b\ge s\): arbitrary \(d\ge0\);
- \(a\ge s,0\le b<s\): \(d\ge s-b\);
- \(b\ge s,0\le a<s\): \(d\ge s-a\);
- \(0\le a,b<s,a+b\ge s\): \(d\ge\max(s-a,s-b)\).
For fixed \(a,b\), the generating series of admissible \(d\) repetitions of 219..221 is precisely \(D_{\text{threshold}}\). The four region sums equal the four terms of \(H_s\). Independently, the exact-\(c\) central query multisets have series \(q^{216c}G_{c,2}\). Summing \(c=0,\ldots,m-1\) establishes the formula for \(E_m\).

The remaining two minimal witness constraints require at least \(m\) occurrences in the disjoint groups 223..290 and 296..312, giving \(M_m,L_m\). The eight prices in \(O\) occur in none of the five minimal sets, so they are unconstrained; their multiplicities have generating series \(U_O\). There are no further restrictions because the five sets are inclusion-minimal among the complete 53 separation patterns. Multiplying the four independent factors counts each unordered query multiset exactly once, with exponent equal to its paid total cost. Extracting the coefficient proves the exact formula for all \(D\ge0\).

For the quasipolynomial statement, the derived expression is rational with all poles at roots of unity, so its coefficient sequence is eventually a sum of polynomial-times-root-of-unity terms. For the asymptotic, the unrestricted 101-price generating function \(U_{\{214,\ldots,314\}}\) has a pole of order 101 at \(q=1\), whose leading coefficient is \(1/\prod_{k=214}^{314}k\). Every other root-of-unity pole has smaller order because the 101 prices are consecutive (gcd one). With fixed \(m\), failure of any one minimal separating constraint bounds the multiplicity of at least five distinct price types by \(m-1\); each excluded family contributes at most \(O(D^{95})\) designs. The unrestricted count at cost \(735m+D\) is therefore \(D^{100}/(100!\prod k)+O(D^{99})\), and the failures are asymptotically negligible. QED.

## Finite validation and remaining questions

The exact symbolic proof is supported by a new independent integer-program check in \`VERIFY_R5_GLOBAL_RATIONAL.py\`: for \(m=1,2,3\) and **all 501 excess values \(D=0,\ldots,500\)**, the early rational partition \(\{H_s\}\) agrees with an independent direct count over the five early multiplicities and all three incidence inequalities. The resulting all-cost product agrees with the separately proved one-excursion formula for all \(D=0,\ldots,425\). The input SHA-256 and five witness sets were rechecked. A stored \`RESULT_R5_GLOBAL_RATIONAL.json\` has \(D=425,\ldots,430\) coefficients and verification status. Independent mathematical Review remains NOT_REVIEWED.

Next mathematical question: extract sharper closed-form quasipolynomial pieces, leading subdominant terms and fast coefficient algorithms for general \(m\). The original *adaptive* full-256 eight-error bound remains \(8335\le C_8^*\le8343\) and requires a separate adaptive strategy/lower-bound certificate. The rational generating function is an exact scalar fixed-query observer quotient; it neither identifies native X6 branch/path histories nor asserts BRC dynamics.
