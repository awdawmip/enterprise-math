# R749SQO — Fourth-order Walsh source signature and cyclotomic residue

Date: 2026-11-15. **Status: AUTHOR_EXACT_NOT_REVIEWED.** Independent auxiliary source-count line, not a new native-X6 task or CLAIM. Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Immediate predecessor: R749SQN at \`0c007e1f4d8a2b78f2e35c324dc57454a172ff0a\` (\`research_notes/portable_direct/2026-11-15_R749SQN_THIRD_ORDER_SOURCE_PHASE.md\`). The actual observer retains the entire labeled positive-integer source multiplicity vector and marked index, with no unproved equivalence to full Heartbeat-X6 state.

## Definitions

For a labeled alphabet of positive weights \(s=(s_1,\ldots,s_d)\), choose a marked source \(j\) with weight \(h=s_j\). Let \(\Omega_r=\{k\in\mathbb Z_{\ge0}^d:\sum_i s_i k_i\le r-1\}\), \(r\ge1\), equipped with uniform counting measure. Define \(X_r=h k_j/r\), \(D=\sum_i(s_i-1)\), \(Q=\sum_i(s_i^2-1)\), \(S_4=\sum_i(s_i^4-1)\), \(W=\prod_i s_i\), and \(m_\zeta=\#\{i:\zeta^{s_i}=1\}\) for nontrivial roots of unity.

## Theorem 1 — first new smooth source statistic at order four

Suppose alphabets \(s,t\) have identical \(d\ge4,D,Q,h\) and that each nontrivial root of unity has \(m_\zeta\le d-4\) for both alphabets. Then uniformly as integer \(r\to\infty\),

\[
\boxed{\mathbb E_sX_r-\mathbb E_tX_r=
\frac{d(d-1)(d-2)}{720(d+1)}
\frac{S_4(s)-S_4(t)}{r^4}+O_{s,t}(r^{-5}).}
\]

The first three smooth coefficients depend only on \((d,D,Q,h)\), as in R749SQN; the fourth introduces a new datum \(S_4\). Without the root-order condition, this formula identifies the difference of the *z=1 smooth components*, which may coexist with lower-order periodic effects.

**Proof.** Set \(w=1-z\), \(f_s(w)=s w/[1-(1-w)^s]\). Direct formal-series division and logarithm give

\[
[w^4]\log f_s(w)=\frac{s^4-110s^2+360s-251}{2880}.
\]

The exact generating function for source counts is \(F_s(z)=(1-z)^{-1}\prod_i(1-z^{s_i})^{-1}\). Thus

\[
F_s(1-w)=\frac{1}{Ww^{d+1}}\exp(\lambda_1 w+\lambda_2w^2+\lambda_3w^3+\lambda_4w^4+O(w^5)),
\]
\[
\lambda_4=\frac{S_4-110Q+360D}{2880}.
\]

The preceding three logarithmic coefficients depend only on \(D,Q\). At fixed \(d,D,Q,h\), the normalized \(w^4\) coefficient therefore differs by \(\delta a_4=\delta S_4/2880\). The marked moment generating function is \(F_s(z)z^h/(1-z^h)\). The normalized marked multiplier \(h w z^h/(1-z^h)=1+O(w)\) is the same for the two alphabets. Relative to \(c_0r^d\), \(c_0=1/(d!W)\), the effect of \(\delta a_4\) on the count \(C_r\) at relative order \(r^{-4}\) is \((d)_4\delta a_4\); the corresponding effect on \(C_r\mathbb E X_r\) is \((d)_3\delta a_4\). The leading mean is \(1/(d+1)\), hence the new fourth coefficient difference is
\[
\left((d)_3-\frac{(d)_4}{d+1}\right)\frac{\delta S_4}{2880}
=\frac{d(d-1)(d-2)}{720(d+1)}\delta S_4.
\]
At \(\zeta\ne1\), the pole of \(F_s\) has order \(m_\zeta\), and marking adds at most one. After coefficient extraction and the extra division by \(r\), each root contributes \(O(r^{-(d-m_\zeta+1)})=O(r^{-5})\) to the normalized mean. Finite rational root-of-unity pole decomposition gives a uniform remainder over all residue classes. QED.

## Theorem 2 — concrete infinite fourth-order separation

Take distinct labeled weights
\[
A=(1,1,2,3,7),\qquad B=(1,1,1,5,6),
\]
and mark the first weight-1 source in each. Both have \((d,D,Q,h)=(5,9,59,1)\), while \(S_4(A)=2495\), \(S_4(B)=1919\), difference 576. Within each alphabet, all nonunit weights are pairwise coprime. Hence \(m_\zeta\le1=d-4\) at every nontrivial root. Theorem 1 gives
\[
\boxed{\lim_{r\to\infty}r^4(\mathbb E_A X_r-\mathbb E_B X_r)=8.}
\]
An independent rational polynomial expansion at the \(z=1\) pole yields
\[
\begin{aligned}
\mathbb E_AX_r={}&1/6+7/(12r)-295/(72r^2)+3835/(144r^3)-196325/(864r^4)+O(r^{-5}),\\
\mathbb E_BX_r={}&1/6+7/(12r)-295/(72r^2)+3835/(144r^3)-203237/(864r^4)+O(r^{-5}).
\end{aligned}
\]
The difference equals \(6912/864=8\). Their unnormalized \(W\) values (42 and 30) differ; the normalized mean preserves a different source statistic.

## Theorem 3 — complete fourth-order root sector for exactly three unit weights

Suppose exactly three of the \(d\ge4\) weights equal 1. Let \(g=\gcd\{s_i:s_i>1\}\). Let \(A_0+\cdots+A_4/r^4\) be the unique expansion from the \(z=1\) pole. If \(g=1\), the full mean equals that expansion plus \(O_s(r^{-5})\). If \(g>1\), the complete first periodic term is

\[
\boxed{\frac{\beta}{r^4}S_g^{(4)}(r)+O_s(r^{-5}),\qquad
S_g^{(4)}(r)=\sum_{\substack{\zeta^g=1\\\zeta\ne1}}
\frac{\zeta^{-(r-1)}}{(1-\zeta)^4},}
\]
\[
\beta=
\begin{cases}
4d(d-1)(d-2)/(d+1),&h>1,\\
-d(d-1)(d-2)(d-3)/(d+1),&h=1.
\end{cases}
\]

The phase is rational, real, nonconstant and periodic of period \(g\). **Proof.** A nontrivial root has at most \(d-3\) singular factors, reaching this order exactly at nontrivial \(g\)-th roots. The leading local coefficient of \(F_s\), in powers of \(1-z/\zeta\), is \(1/[W(1-\zeta)^4]\). Normalized count corrections therefore give \(d(d-1)(d-2)(d-3)S_g^{(4)}(r)/r^4\). If the marked weight \(h>1\), it is divisible by the order of every such root; its marked generating factor adds one pole, giving \(d(d-1)(d-2)S_g^{(4)}(r)/r^4\) to the normalized numerator. If \(h=1\), the numerator has no contribution at this order. Subtract the leading mean \(1/(d+1)\) times the count correction to obtain the stated \(\beta\). All other roots are \(O(r^{-5})\). QED.

For weights \((1,1,1,2)\), \(g=2\) and \(S_2^{(4)}(r)=(-1)^{r-1}/16\). Thus marking weight 2 gives phase \(+(6/5)(-1)^{r-1}/r^4\); marking a unit gives \(-(3/10)(-1)^{r-1}/r^4\). An exact rational certificate checks both signs and amplitudes.

## Reproduction and evidence scope

The companion Python certificate uses exact integer source-multiplicity DP, independent recursive enumeration, formal Taylor division and polynomial extraction with \`fractions.Fraction\`. Verified: 2,048 deletion identities, 60 independent enumerations, all first-four coefficients of the pair, eight full-mean scaled samples through \(r=4000\), and 12 rational phase samples for the \(u=3\) witness, all PASS. These finite checks verify the calculations, whereas the infinite claims use the pole arguments above. No independent review or Lean check is asserted. Status: **AUTHOR_EXACT_NOT_REVIEWED**.

Next: classify one-unit (\(u=1\)) root sectors through order three, fifth-order smooth invariants and observer-specific safe quotient maps preserving marked deletions. Scientific materials here are separate from native Task/CLAIM authority and Source Activity bookkeeping.
