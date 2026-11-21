# R5: Genuine-intersection primitive-19 lower bound, all thresholds in 14 residue classes

Scientific date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_PROOF / EXACT_INTEGER_FINITE_CHECKED / NOT_REVIEWED. Independent *scalar cost observer* within the frozen R5 model, not an X6/BRC transfer or a P000 modification. Do not reuse the erroneous collapsed-union-cap formula for overlapping failure events.

## Frozen problem and result

The original scalar cost counts multiplicities \(a_p\ge 0\) for prices \(p=214,\ldots,314\) with cost \(N=\sum_p p a_p\). The failure events are
- \(S_0=\{214,215,216,217,218\}\);
- \(S_1=\{214,216,217,218,219,220,221\}\);
- \(S_2=\{215,216,217,218,219,220,221\}\);
- \(S_3=\{223,\ldots,290\}\);
- \(S_4=\{296,\ldots,312\}\).

\(E_i=\{\sum_{p\in S_i}a_p<m\}\), \(f_m(N)\) counts the union, and \(F_m(q)=\sum_{N\ge0}f_m(N)q^N\). Let \(M_m(O_m(N^3))\) be the least positive coefficient period of a quasipolynomial approximation with remainder \(O_m(N^3)\), fixed \(m\ge1\).

**Theorem.** For every \(m\ge1\) with \(m\bmod19\in\{1,2,\ldots,14\}\),
\[
  19\mid M_m(O_m(N^3)).
\]
For the five previously untreated residue classes \(m\bmod19\in\{15,16,17,18,0\}\), the same necessary divisor is **exactly verified for the five representative thresholds \(m=15,16,17,18,19\)**. No all-threshold claim for those five classes is made.

A structural lemma applies without residue-class restriction: at any primitive nineteenth root \(\zeta\), the five-event numerator \(R_m(\zeta)\) equals the genuine three-event numerator \(R_{\{0,1,2\},m}(\zeta)\), so the other two events cannot change the leading \(N^4\) primitive-19 coefficient.

## Exact rational numerator and structural lemma

Put \(D(q)=\prod_{p=214}^{314}(1-q^p)\). For nonempty event mask \(I\), let \(U_I=\bigcup_{i\in I}S_i\) and
\[
 H_{I,m}(q)=
 \sum_{\substack{a_p\ge0\ (p\in U_I)\\
        \sum_{p\in S_i}a_p<m\ \forall i\in I}}
 q^{\sum_{p\in U_I}p a_p},\quad
 B_I(q)=\prod_{p\in U_I}(1-q^p).
\]
Each \(H_{I,m}\) is a finite integer polynomial because every variable in \(U_I\) is bounded by at least one constraint. By genuine inclusion-exclusion,
\[
 F_m(q)=\frac{R_m(q)}{D(q)},\quad
 R_m(q)=\sum_{\emptyset\ne I\subseteq\{0,\ldots,4\}}
  (-1)^{|I|+1}B_I(q)H_{I,m}(q).
\]
There are exactly five prices divisible by 19 in the full denominator: \(228,247,266,285,304\), so \(D\) has a fifth-order zero at each primitive nineteenth root.

Every term involving \(E_3\) contains \(1-q^{228}\), and every term involving \(E_4\) contains \(1-q^{304}\). Consequently these terms vanish at \(\zeta\); the remaining terms are precisely the seven masks involving only \(E_0,E_1,E_2\). In particular,
\[
 R_m(\zeta)=\sum_{\emptyset\ne I\subseteq\{0,1,2\}}
 (-1)^{|I|+1} B_I(\zeta)H_{I,m}(\zeta).
\]
No multi-event intersection is replaced by a single union-cardinality bound.

## Uniform proof for 14/19 threshold phases

In the cyclotomic integer ring \(\mathbf Z[\zeta]\), let \(\pi=1-\zeta\). Since 19 is prime, \(\mathbf Z[\zeta]/(\pi)\cong\mathbf F_{19}\). For \(19\nmid p\), \(1-\zeta^p=\pi u_p\), with \(u_p\bmod\pi=p\bmod19\ne0\). Thus this factor has exact \(\pi\)-adic valuation 1.

Among the seven surviving masks, the singleton \(I=\{0\}\) uses exactly five prices and its factor \(B_{\{0\}}(\zeta)\) has valuation 5. The singleton masks \(I=\{1\}\) and \(\{2\}\) use seven prices each, and the four masks with two or three events use all eight prices 214..221. Every other term therefore has valuation at least 7.

Moreover,
\[
 H_{\{0\},m}(\zeta)\bmod\pi
 =H_{\{0\},m}(1)\bmod19
 =\binom{m+4}{5}\bmod19.
\]
By Lucas's theorem, this binomial is nonzero modulo 19 exactly when \(m\bmod19\in\{1,\ldots,14\}\). On those fourteen classes the singleton contribution has exact valuation 5, while every other term is divisible by \(\pi^7\). Cancellation is impossible, hence \(R_m(\zeta)\ne0\).

The numerator is a polynomial over \(\mathbf Z\); a nonzero value at a primitive nineteenth root gives a genuine fifth-order pole of \(F_m\). By uniqueness of root-of-unity exponential-polynomial expansions, a nonzero degree-\(N^4\) character of exact order 19 cannot be represented to \(O_m(N^3)\) by a periodic-coefficient polynomial whose period is not divisible by 19. This proves the theorem.

## Independent small-threshold closed form

Let \(B_i=\prod_{p\in S_i}(1-q^p)\), \(B_U=\prod_{p=214}^{221}(1-q^p)\), \(T_X=\sum_{p\in X}q^p\), and \(U=\{214,\ldots,221\}\).

At \(m=2\), each single-event constraint allows zero or one unit among its own prices. A pair of events also allows exactly one unit in each of two disjoint incidence classes: \((215,\{219,220,221\})\) for \(\{0,1\}\), \((214,\{219,220,221\})\) for \(\{0,2\}\), and \((214,215)\) for \(\{1,2\}\). The triple intersection allows at most one unit across \(U\).

The exact primitive-19 numerator is therefore
\[
 R_2(\zeta)=
 \left[\sum_{i=0}^2 B_i(q)(1+T_{S_i})-
 B_U(q)\left\{2(1+T_U)+(q^{214}+q^{215})T_{\{219,220,221\}}+q^{429}\right\}\right]_{q=\zeta}.
\]
Independent cyclic-ring evaluation yields the 18-coordinate basis vector
\[
(-4,-10,-11,-16,-13,-11,-6,-1,5,10,18,26,27,27,25,23,14,11)\ne0.
\]
This is identical to the genuine seven-mask dynamic calculation. For \(m=1\), the checker reproduces the earlier immutable result at \`ba976ca1d5ea32392e409b5dec08c1607140a610\`.

## Finite reproducible evidence, scope and next question

The companion \`VERIFY_TRUE19.py\` performs *integer-only* convolution in \(\mathbf Z[z]/(z^{19}-1)\), reduces modulo \(\Phi_{19}(z)=1+\cdots+z^{18}\), and checks every threshold \(1\le m\le19\). The five exceptional representatives have nonzero coordinates:
\[
\begin{array}{c|rrrrr}
m&15&16&17&18&19\\\hline
[z^0]R_m &-210&210&-160&28&101\\
[z^1]R_m &-437&452&-365&165&86
\end{array}
\]
All other thirteen finite comparisons also report nonzero. These finite checks **do not** extend the theorem to every threshold in the five exceptional residue classes. The verifier independently checks the closed-form \(m=2\) identity and historic \(m=1\) vector.

Next discriminating question: derive the \(m\)-generating function for the genuine three-load intersection correction at \(q=\zeta_{19}\), especially \(m\equiv0,15,16,17,18\pmod {19}\); determine its eventual polynomial/quasipolynomial dependence, then prove or refute universal nonvanishing before recombining all orders \(d\le25\) for the strict minimal period.

Source provenance: frozen R5 model from \`ba976ca1d5ea32392e409b5dec08c1607140a610\`; genuine-intersection correction from \`75d986aa23b68a7ecf9b29dc1006f0e322b35a15\`. Scientific checks are author-side and not an independent review, native Activity checkpoint, formal Result, or P000/Working Truth update.
