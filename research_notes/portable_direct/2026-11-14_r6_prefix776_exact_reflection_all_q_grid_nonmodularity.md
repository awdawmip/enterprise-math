# PREFIX-776 / R6 — Reflection involution gives opposite 1/768 Gamma mixed signs for every positive q

Date: 2026-11-14 (Asia/Shanghai)
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
Status: AUTHOR_EXACT_INTEGER_THEOREM / UNREVIEWED / NOT_ADMITTED.

## 1. Exact domain and objective

In the *external*, 189-layer killed-Pascal first-stop / independent two-Gamma-clock auxiliary model, let
\[
Y(p,z)=\max(C_p,C_z),\quad
\mu(p,z)=\mathbb E Y(p,z),\quad
W(p,z)=\operatorname{Var}(Y(p,z)),\quad
V_q(p,z)=q^2W(p,z)-q\mu(p,z).
\]
Each first-stop layer \(T_x\le189\) independently determines a unit-scale \(\operatorname{Gamma}(T_x,1)\) clock. The source's frozen width predicate, terminal row and the 189-layer survivor \(S_n(x)=\Pr(T_x>n)\) are the same as in PREFIX-774 and PREFIX-775. The parameter grid is \(G=\{k/768:0\le k\le768\}\), with two-variable lattice \(G^2\).

PREFIX-775 exhibited two individual cells of opposite mixed sign only for \(q\ge0.033662\). We now prove the stronger exact statement:
\[
\boxed{\forall q\in(0,\infty),\quad V_q|_{G^2}
\text{ is neither supermodular nor submodular}.}
\]
The statement concerns the auxiliary Gamma model on the entire finite grid, and is proved with four explicitly specified cells, not an approximate enumeration.

## 2. Structural lemma: the survivor distribution is reflection invariant

The killed-Pascal survivor rows are integers \(c_{n,k}\), indexed by \(0\le k\le n\). At the initial row \(c_{0,0}=1\). The transition is
\[
c_{n+1,k}=(c_{n,k-1}+c_{n,k})\,
\boldsymbol 1_{\{\mathrm{wide}(n+1,k)\}},
\]
where missing endpoints have count zero. The frozen width predicate compares the exact binomial likelihood
\[
40(n+1)\binom{n}{k}x^k(2^{18}-x)^{n-k}>(2^{18})^n
\]
and uses the same quartile-width rule at its reflected index \(n-k\). Consequently
\(\mathrm{wide}(n,k)=\mathrm{wide}(n,n-k)\), which, by induction, gives
\[
c_{n,k}=c_{n,n-k}\quad(0\le n\le188).
\]

Writing \(\bar x=1-x\), the finite survival polynomials
\[
S_n(x)=\sum_{k=0}^nc_{n,k}x^k(1-x)^{n-k}
\]
satisfy the **exact identity**
\[
\boxed{S_n(\bar x)=S_n(x).}
\]
All finite Gamma moment kernels depend only on the two survivor vectors. Therefore
\[
\mu(p,1-z)=\mu(p,z),\quad
W(p,1-z)=W(p,z),\quad
V_q(p,1-z)=V_q(p,z)
\]
for all admissible \(p,z,q\). This is an equality in the external auxiliary model, not an identification of native spatial axes.

## 3. Reflection flips a rectangular mixed difference

For \(F\colon[0,1]^2\to\mathbb R\) set
\[
\Delta_{[a,b]\times[c,d]}F
=F(b,d)-F(b,c)-F(a,d)+F(a,c).
\]
If \(F(p,z)=F(p,1-z)\), its reflected cell
\[
R^\#=[a,b]\times[1-d,1-c]
\]
has
\[
\boxed{\Delta_{R^\#}F=-\Delta_RF.}
\]
This follows by substituting \(1-c,1-d\) into the four terms and reversing the order of the second coordinate. It applies to \(\mu,W,V_q\) for **every real \(q\)**, and preserves unit cells of \(G^2\).

Thus any nonzero mixed difference of \(V_q\) on a grid cell produces both signs on the same grid. The remaining exact question is whether \(V_q\) can have *all* mixed differences zero at some positive \(q\).

## 4. Two distinct exact switching ratios rule out that exception

For \(k=38,39\), define
\[
R_k=[k/768,(k+1)/768]^2,\qquad
R_k^\#=[k/768,(k+1)/768]\times[(767-k)/768,(768-k)/768].
\]
These are respectively \(R_{38}^\#=[38,39]\times[729,730]\) and \(R_{39}^\#=[39,40]\times[728,729]\), with every endpoint divided by 768.

The complete exact-integer checker reconstructs all 189 survivor rows, confirms 9,529 nonzero survivor entries and an empty terminal row, validates each row's \(k\mapsto n-k\) coefficient symmetry, and directly checks the reflected survivor vectors at the required grid endpoints.

The moment formulae, inherited without changing the frozen model, are
\[
\begin{split}
\mu(p,z)&=\sum_iS_i(p)+\sum_iS_i(z)-s(p)^TKs(z),\\
M_2(p,z)&=2\sum_i(i+1)(S_i(p)+S_i(z))-s(p)^TLs(z),\\
W&=M_2-\mu^2,
\end{split}
\]
with \(K_{ij}=\binom{i+j}i/2^{i+j+1}\), \(L_{ij}=(i+j+1)K_{ij}\).

For both \(R_k\), integer computations establish
\[
\Delta_{R_k}\mu<0,\qquad \Delta_{R_k}W<0.
\]
Consequently their switch values
\[
r_k=\frac{\Delta_{R_k}\mu}{\Delta_{R_k}W}>0
\]
are well-defined, and exact integer cross-products give **disjoint** strict rational enclosures:
\[
\boxed{
\frac{2852034258349}{10^{14}}<r_{38}<
\frac{2852034258350}{10^{14}},}
\]
\[
\boxed{
\frac{28523464}{10^{9}}<r_{39}<
\frac{28523465}{10^{9}}.}
\]
Display-only decimals are \(r_{38}\approx0.02852034258349057517836\) and \(r_{39}\approx0.02852346402359032573360\). The computation additionally directly verifies \(r_{38}\ne r_{39}\) through nonzero signed integer cross-products; this does not rely on rounded decimal displays.

For every real \(q>0\),
\[
\Delta_{R_k}V_q
=q\,\Delta_{R_k}W\,(q-r_k).
\]
Because \(r_{38}\ne r_{39}\), at least one of \(q-r_{38}\) or \(q-r_{39}\) is nonzero. For that \(k\), \(\Delta_{R_k}V_q\ne0\), whereas
\(\Delta_{R_k^\#}V_q=-\Delta_{R_k}V_q\). Thus the finite grid contains both strict signs for **every** \(q>0\), proving the theorem.

Notice the quantifiers: two **fixed** base cells and their fixed reflected cells suffice simultaneously for *all* \(q>0\). No parameter-dependent search is needed at deployment.

## 5. Exact verification and remaining frontier

The attached standard-library Python checker uses only arbitrary-precision integer arithmetic for survivor coefficients, kernel moment numerators, reflection equalities, switch separation and test cases \(q=1/1000,2,r_{38},r_{39}\).

Define \(E=768^{188}\), \(H=E^2 2^{377}>0\), and integer corner numerators \(U=H\mu\), \(Z=H^2W\). For any cell \(R\), \(r_R=H\,\Delta_RU/\Delta_RZ\) exactly. The script checks the two rational enclosures with the correct reversal for the negative denominator and tests both exceptional switch values exactly. Its return label is ALL_CHECKS_PASS PREFIX776 REFLECTION_ALL_Q. The universal-in-\(q\) conclusion is an algebraic consequence of these finite certificates and the reflection lemma, not an exhaustive uncountable search.

Reproduction:
    python3 research_notes/portable_direct/PREFIX776_R6_REFLECTION_EXACT_CHECK.py

Output: research_notes/portable_direct/PREFIX776_R6_REFLECTION_EXACT_RESULTS.json

Scientifically, this refines PREFIX-775 from a conditional high-\(q\) grid statement to a **uniform all-\(q>0\)** theorem using the BRC binomial survivor involution. It does not assert any original comparator grid exclusion, native X6 dynamical result, or formal reviewed Result. This new reflection method also motivates identifying higher-dimensional signed observer involutions (with full port/provenance typing), and the exact separability criterion for finite lattice moment functionals.

Next concrete mathematical question: classify the \(q=0\) limiting degenerate case \(V_0\equiv0\) and test whether a native comparator under its own frozen predicates retains the exact survivor-reflection symmetry; if a typed observer mapping is absent, retain this exact external auxiliary result and examine a separate native bridge construction.
