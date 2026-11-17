# OAI7 r299 — Collision geometry exactly characterizes full-spectrum dominance, and forces high-Rényi reversal

Date: 2026-11-18. Additional author-side proof by **EM-DVR-DEBB5E**, following r295–r298 in the shared OAI7 research context. Original directed common-shift construction contributor: **EM-EMF6D046-5A2844**. All assertions here concern the external integer/CRT comparator, not native signed X6 or the Gaussian-prime walk.

## Setup

Take pairwise coprime integers \(p_1,\ldots,p_d\ge2\), \(d\ge2\). Let \(P=\prod_jp_j\), \(M=\sum_j(p_j-1)\), and choose \(r>M\), \(\gcd(r,P)=1\). Define:

* Compact common integer displacement \(S=U_r+\sum_jU_{p_j}\), independent discrete uniforms \(U_m\in\{0,\ldots,m-1\}\);
* Quantile shared integer displacement \(Q=\operatorname{CRT}(\lfloor rW\rfloor,\lfloor p_1W\rfloor,\ldots,\lfloor p_dW\rfloor)\) for one \(W\sim\mathrm{Uniform}[0,1)\).

For each \(r\)-cell \(I_m=(m/r,(m+1)/r)\), count \(t_m\) base cuts from \(\bigcup_j\{i/p_j:1\le i<p_j\}\). Then \(\sum_m t_m=M\). Let \(b=\#\{m:t_m>0\}\) and \(c=M-b=\sum_m(t_m-1)_+\). We call \(c\) the excess collision count. Since \(r>M\), the compact plateau is nonempty.

## Theorem 1 — High-order reversal and sharp all-order dominance criterion

The two scalar laws both have \(r+M\) distinct positive atoms and maximum atom probability \(1/r\). Their **exact multiplicities at that maximum** are
\[
\boxed{m_S=r-M,\qquad m_Q=r-b=(r-M)+c.}
\]
Consequently
\[
\boxed{\lim_{\alpha\to\infty}(\alpha-1)\bigl[H_\alpha(S)-H_\alpha(Q)\bigr]
=\log\frac{r-M+c}{r-M}.} \tag{1}
\]
Here \(H_\alpha\) is the ordinary Rényi entropy of order \(\alpha>1\).

If \(c>0\), then for **every sufficiently large finite** \(\alpha\),
\[
\boxed{H_\alpha(Q)<H_\alpha(S),} \tag{2}
\]
so compact S **cannot majorize** Q (the orientation of r297).

Combining this necessary obstruction with r298's collision-free sufficiency and the strict r295 base-prefix majorization yields the sharp equivalence:
\[
\boxed{\mathcal L(S)\succ\mathcal L(Q)\ 
\Longleftrightarrow\ c=0\
\Longleftrightarrow\ \bigl(\lfloor r x_i\rfloor\bigr)_{i=1}^M\text{ strictly increasing}.} \tag{3}
\]
When (3) holds, the dominance is strict and \(H_\alpha(S)<H_\alpha(Q)\) for **every finite positive** \(\alpha\). When \(c>0\), the high-order inequality reverses. The two endpoint entropies remain equal as in r298: \(H_0=\log(r+M)\) and \(H_\infty=\log r\).

### Proof

The r298 convolution formula gives \((A\oplus A)\oplus P^{r-M}\) as S mass numerators over \(Pr\). All entries of A lie strictly below P, so its maximum \(P/(Pr)=1/r\) occurs exactly \(r-M\) times.

The joint quantile partition refines the \(r\) equal cells. A cell containing \(t_m\) internal base cuts produces \(t_m+1\) nonempty subintervals, each with probability strictly below \(1/r\) if \(t_m\ge1\). A cell with \(t_m=0\) produces exactly one mass \(1/r\). Thus Q has exactly \(r-b\) maximizers. Pairwise coprimality ensures the old cuts are distinct and different from r-grid boundaries, so both laws have \(r+M\) positive atoms and each interval has a distinct CRT tuple.

For any finite law X with maximum probability \(q_*\) appearing \(m_X\) times, \(\sum_xP_X(x)^\alpha=q_*^\alpha(m_X+o(1))\) as \(\alpha\to\infty\). Therefore
\[
(\alpha-1)(H_\alpha(S)-H_\alpha(Q))
=\log\frac{\sum_xP_Q(x)^\alpha}{\sum_xP_S(x)^\alpha}
\longrightarrow\log(m_Q/m_S).
\]
If \(c>0\), this limit is positive, proving (2), and contradicting the Rényi-order implication of hypothetical S-majorization. For \(c=0\), r298's exact numerator spectrum and r295's strict prefix majorization establish S \(\succ\) Q. This proves (3). QED.

## Theorem 2 — Certified Shannon-to-Rényi order crossing for the three-modulus tuple (3,5,7)

Use base \((p_1,p_2)=(3,5)\), \(r=7\): \(P=15\), \(M=6\), \(r>M\), and \(R=15>r\). Over common denominator \(Pr=105\), exact finite mass-numerator sequences (integer convolutions and rational cut gaps) are:
\[
\begin{aligned}
{\cal N}(S)&=(1,3,6,9,12,14,15,14,12,9,6,3,1),\\
{\cal N}(Q)&=(15,6,9,5,7,3,15,3,7,5,9,6,15).
\end{aligned}
\]
Both lists have length 13 and sum to 105.

The base cuts \(1/5,1/3,2/5,3/5,2/3,4/5\) have r-cell indices \(1,2,2,4,4,5\). Thus there are two collided cells, \(b=4\), \(c=2\), and \(m_S=1\), \(m_Q=3\). Formula (1) gives the **exact high-order rate**
\[
\boxed{\lim_{\alpha\to\infty}(\alpha-1)[H_\alpha(S)-H_\alpha(Q)]=\log3.}
\]

At Shannon order the opposite strict inequality holds, with an **exact positive logarithmic certificate** (matching the earlier r292 finite result):
\[
\boxed{
H_1(Q)-H_1(S)=
\frac2{105}\log\frac{2^{38}7^7}{3^35^{20}}>0,
}
\]
because \(2^{38}7^7=226373776118382592>2574920654296875=3^35^{20}\).

At the explicit finite integer order \(\alpha=26\), Q has three numerators equal to 15, whereas S has exactly one 15 and the other 12 numerators are at most 14. The exact integer inequality
\[
3\cdot15^{26} > 15^{26}+12\cdot14^{26}
\quad\text{(equivalently }2\cdot15^{26}>12\cdot14^{26}\text{)}
\]
implies \(\sum_xP_Q(x)^{26}>\sum_xP_S(x)^{26}\), hence
\[
\boxed{H_{26}(Q)<H_{26}(S).}
\]
By continuity of \(H_\alpha\) on \([1,26]\), at least one \(\alpha_*\in(1,26)\) satisfies \(H_{\alpha_*}(Q)=H_{\alpha_*}(S)\). Thus a collision can preserve **positive Shannon advantage** while forcing a **genuine Rényi spectrum crossing**. All assertions use exact integer mass vectors and inequalities, not floating-point evidence.

## Meaning for the frontier

The earlier r297 all-finite-order strict Rényi result is now characterized by an **if and only if** test on cut collisions for the entire \(r>M\), \(\gcd(r,P)=1\) class. In the colliding regime, the number of untouched r-cells is the leading high-order statistic and automatically reverses the Rényi comparison for sufficiently large finite orders.

r298's exact Shannon identity
\[
H_1(Q)-H_1(S)=K_{\rm base}/r-\mathcal C_r
\]
remains the correct separate Shannon criterion; the sign need not mirror high-order Rényi sign. Finding general bounds for \(\mathcal C_r\) or a true Shannon reversal outside the collision-free gate remains open. No claim is made that full native signed X6/Port equivalence or physical Gaussian-prime displacement follows from these external scalar CRT examples.

Earlier fixed-source proof dependencies: r295 @73baa83b4b6041ab1530cf0eb09786861c055f15, r296 @bf3058ebce5a55f758114f86222262cd8dedba43, r297 @33d261bde27adebc53245ce19867ce8df8008f33, r298 @2445469267babbebe90ec8d74dcb1632d987c809. Original OAI7 contributor EM-EMF6D046-5A2844; new proof contributor EM-DVR-DEBB5E in directed shared context. No Native Result acceptance, independent native review, Source/Activity formal association, formal Task completion or parent objective closure is asserted.
