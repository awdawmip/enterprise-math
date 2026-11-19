# EC49FUH-S — Exact n=15 composite minimax saddlepoint at x=7/25000

2026-11-20. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED. Continuation of EC49FUH in the same PR, retaining original BRC16943 frozen price-science pin \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Auxiliary clipped-price binomial observer, not a new native X6 or Bellman-optimality theorem.

## Sharp theorem

For the original two-hypothesis clipped-price model, fix \(n=15\) conditionally independent trials, a common nuisance \(e\le E=1048576/18958647\), normalized detector width \(x=7/25000\), and equal hypothesis priors.

Write \(\theta=(1-ae)^{-1}\), with \(a=2807259/163840\), \(\theta\in(0,\theta_E]\), and use the exact coordinate established in EC49FUH:
\[
 T(\theta)=1-p_e(x)=(1-x)(1-\beta x+\beta x\theta),\qquad
 u(\theta)=1-q_e=\frac{C}{H+B\theta},
\]
where
\[
 \beta=\frac3{637},\quad C=21829245984,\quad
 H=45529434409,\quad B=-456083905.
\]
For \(j\ge1\), put \(F_j(\theta)=T(\theta)^j[1-u(\theta)^j]\). The binary-count discrimination gaps for the rules \(K\ge1\) and \(K\ge2\) are exactly
\[
 D_1(\theta)=F_{15}(\theta),\qquad
 D_2(\theta)=15F_{14}(\theta)-14F_{15}(\theta).
\]
Let \(\theta_0=0\) denote only the \(e\to-\infty\) limit. Let \(\Delta_1(\theta)=P_+(K=1\mid\theta)-P_-(K=1\mid\theta)\). Define the following **exact rational numbers**:
\[
 A=D_1(\theta_E),\quad I=D_1(0),\quad
 d_E=\Delta_1(\theta_E),\quad d_I=\Delta_1(0),
\]
\[
 \boxed{\alpha=1-\frac{A-I}{d_E-d_I}},\qquad
 \boxed{\lambda_E=\frac{-d_I}{d_E-d_I}}.
\]
The attached Fraction certificate establishes \(A>I\), \(d_E>0>d_I\), and \(14/15<\alpha<1,\ 0<\lambda_E<1\). Numerically only for orientation,
\[
 \alpha\approx0.9999182197507327,\qquad
 \lambda_E\approx0.9485077982871909.
\]

**Theorem.** The sharp composite minimax decision rule is
\[
 \boxed{\begin{cases}
 K=0 &: \text{choose }H_-,\\
 K=1 &: \text{choose }H_+\text{ with probability }\alpha,\\
 K\ge2 &: \text{choose }H_+.
 \end{cases}}
\]
Its **exact** minimax error probability is the rational number
\[
 \boxed{R^*=\frac{1-\bigl[(15\alpha-14)F_{15}(0)
                 +15(1-\alpha)F_{14}(0)\bigr]}2},
\]
approximately \(0.0021136736626381075\), versus \(0.0021136649180596634\) for the endpoint-only Bayes risk. An exact least-favorable **limiting** nuisance distribution is the two-point measure with weight \(\lambda_E\) at \(e=E\) and \(1-\lambda_E\) at \(e=-\infty\) in the parameter compactification. Since the original nuisance set contains only finite \(e\), this measure denotes an attainable minimax lower-bound limit, not a newly admitted finite nuisance.

## Full analytic proof: global upper bound

The randomized rule has gap
\[
 D_\alpha(\theta)=\alpha D_1+(1-\alpha)D_2
   =(15\alpha-14)F_{15}(\theta)+15(1-\alpha)F_{14}(\theta).
\]
Both coefficients are nonnegative by \(14/15<\alpha<1\). We prove that **both** \(F_{14}\) and \(F_{15}\) are strictly concave on the entire interval \([0,\theta_E]\), rather than extrapolating from a nuisance grid.

Write \(S(\theta)=T(\theta)u(\theta)\). Then \(F_j=T^j-S^j\), \(T''=0,\ T'>0\), and \(S''=2T'u'+Tu''>0\). Consequently
\[
 F_j''=j(j-1)(T^{j-2}T'^2-S^{j-2}S'^2)-jS^{j-1}S''.
\]
An exact sufficient condition for \(S^{j-2}S'^2>T^{j-2}T'^2\) is
\[
 u^{j/2}\frac{u'}u>\frac{T'}T.
\]
For this **fixed rational width** and all \(0\le\theta\le\theta_E\), the following elementary rational bounds hold:
\[
 \frac{T'}T\le \frac{\beta x}{1-\beta x}<\frac1{500000},\qquad
 u(\theta)\ge\frac{C}{H}>\frac25,\qquad
 \frac{u'}u=\frac{-B}{H+B\theta}\ge\frac{-B}{H}>\frac1{100}.
\]
For \(j=14\) and \(j=15\), since \(0<u<1\) and \(j/2<8\),
\[
 u^{j/2}\frac{u'}u>
  \frac{(2/5)^8}{100}>\frac1{500000}>\frac{T'}T.
\]
Thus \(F_j''<0\) on the **complete** interval. Hence \(D_\alpha\), a nonnegative combination, is concave, and its minimum occurs at \(\theta=0\) or \(\theta=\theta_E\). By the exact definition of \(\alpha\),
\[
 D_\alpha(0)=D_\alpha(\theta_E).
\]
For all finite nuisance \(e\le E\) the rule therefore has risk no larger than \(R^*\). This is a full-nuisance upper bound.

## Full analytic proof: matching lower bound

At each of the two endpoints \(\theta=0,\theta_E\), the binomial signed mass at \(K=0\) is negative and every signed mass at \(K\ge2\) is positive. The binomial likelihood ratio increases strictly with \(k\); in fact checking the \(k=2\) sign suffices for the latter claim. At \(K=1\), the signed masses have opposite signs \(d_I<0<d_E\), as established by exact rational comparisons. A nuisance prior placing mass \(\lambda_E\) at \(\theta_E\) and \(1-\lambda_E\) at \(\theta=0\) makes the **mixture signed mass at K=1 identically zero**:
\[
 \lambda_E d_E+(1-\lambda_E)d_I=0.
\]
For that mixture, the Bayes rule chooses \(H_-\) at zero counts and \(H_+\) at every count at least two; any randomization at exactly one count is equally Bayes-optimal. Therefore the candidate rule is Bayes for the two-point mixture.

By the construction of \(\alpha\), its endpoint risks coincide. Thus the mixture Bayes risk equals the common endpoint risk \(R^*\). Every test's supremum over finite nuisance parameters dominates its risk at \(E\) and its limit at \(-\infty\), and consequently dominates this mixture Bayes risk. This lower bound matches the upper bound, proving the claimed exact composite minimax value and rule. QED.

The key quantifiers preserve a **single shared nuisance for both hypotheses and across all 15 trials**: the mixing of binomial laws is performed after forming each 15-trial distribution, not by redrawing the nuisance independently per trial.

## Verification and boundaries

The accompanying Python standard-library Fraction verifier evaluates every exact rational endpoint comparison, signs of count masses, the mixture cancellation, equalization of the two endpoint gaps, and the rational global concavity bounds. It reports PASS. The analytic concavity plus two-point Bayes lower bound is the universal real-parameter proof; finite check cases alone are not used as a proof. No independent mathematical review or formal theorem admission has occurred.

This solves the sharp composite minimax game for the **single exact width** \(x=7/25000\). The exact optimal randomized rule as a function of every \(x\in(x_{15},x_B)\), including possible changes of least-favorable support, remains open. The Bellman and BRC16943 source assumptions and the original observer/clipping provenance are preserved.
