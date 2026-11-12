# R749SMH — Feedback and postprocessing experiments are Blackwell-incomparable

Date: 2026-11-13 (Asia/Shanghai). Author-side mathematical continuation of R749SMF/R749SMG.
Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Scope: the exact finite three-sign conditional provenance observer, not a native V29/V39 event.

## 1. Two experiments with the same hidden source

Let the unknown historical state be \(z=(x,y,t)\in\{-1,1\}^3\), with eight strictly positive prior probabilities. The public outputs are \((a,b,c)\in\{-1,1\}^3\). Put \(\alpha_i=1-2\varepsilon_i\).

* \(N^{\mathrm{post}}\) is R749SMF: first use internal \(a_0\) to select the B port (\(y\) if \(a_0=+\), \(t\) if \(a_0=-\)), then independently corrupt the public A, B and C outputs.
* \(N^{\mathrm{fb}}\) is R749SMG: corrupt A first and use that *public* A to select the B port, with B and C subsequently corrupted.

Both use the identical source labels, the same internal \(x,y,t\) queries and equal bit-flip parameters. A Blackwell garbling of experiment \(K\) into experiment \(L\) means a single source-independent, column-stochastic kernel \(G\) on public outputs satisfies \(L=GK\). Such a garbling contracts total variation for every pair of source priors.

## 2. Theorem — neither experiment garbles the other

For every \(\varepsilon_A=1/2\), \(\varepsilon_B\in[0,1]\setminus\{1/2\}\), and every \(\varepsilon_C\in[0,1]\), there is no stochastic kernel \(G\) with

\[
N^{\mathrm{post}}=GN^{\mathrm{fb}},
\]

and no stochastic kernel \(H\) with

\[
N^{\mathrm{fb}}=HN^{\mathrm{post}}.
\]

Both failures have witnesses consisting entirely of strictly positive source priors, with every atom at least \(1/16\).

**Witness 1 (information revealed only by feedback).** Define

\[
\mu_Y(x,y,t)=\frac{1+y/2}{8},\qquad
\mu_T(x,y,t)=\frac{1+t/2}{8}.
\]

Under postprocessing, A's public bit is fair and independent of the internal selector. Because both priors have the same \(E[Y]+E[T]=1/2\), and their \(E[YT]=0\), the entire observed output distribution agrees for any \(\varepsilon_C\). Under feedback, public A specifies which named port (Y or T) is read. Therefore

\[
\operatorname{TV}(N^{\mathrm{post}}\mu_Y,N^{\mathrm{post}}\mu_T)=0,\qquad
\operatorname{TV}(N^{\mathrm{fb}}\mu_Y,N^{\mathrm{fb}}\mu_T)
=\frac{|\alpha_B|}{8}>0.
\]

In particular feedback cannot be obtained from the postprocessed observation by source-independent garbling.

**Witness 2 (information revealed only by internal selection).** Define

\[
\pi_\pm(x,y,t)=\frac{1\pm x(y-t)/4}{8}.
\]

Both are strictly positive with minimum atom \(1/16\), and have identical \((Y,T)\) marginals. When \(\alpha_A=0\), every row of the feedback likelihood \(N^{\mathrm{fb}}\) depends only on \((Y,T)\); hence its entire observed distribution agrees under \(\pi_+\) and \(\pi_-\). The postprocessing system retains the internal selector based on X. Its B-bit has means

\[
\mathbb{E}_{\pi_\pm}[B]
=\pm\frac{\alpha_B}{8}.
\]

Moreover the joint B,C law under \(\pi_\pm\) has difference proportional to \(b\alpha_B(2-c\alpha_C)\); since \(|\alpha_C|\le1\), the exact total variation is

\[
\operatorname{TV}(N^{\mathrm{fb}}\pi_+,N^{\mathrm{fb}}\pi_-)=0,\qquad
\operatorname{TV}(N^{\mathrm{post}}\pi_+,N^{\mathrm{post}}\pi_-)
=\frac{|\alpha_B|}{8}>0.
\]

Therefore postprocessing cannot be obtained by source-independent garbling of feedback either.

**Derivation of the second TV law.** The joint law after marginalizing the public fair A can be written \(P_\pm(b,c)=\frac14[1+bc\,\mathbb E_{\pi_\pm}(B_0C_0)]\) after including the marginal terms. More directly, one can calculate the posterior sign contrast by a Walsh expansion: \(E_{\pi_\pm}[X(Y-T)]=\pm1\), the internal B conditional mean is \(\alpha_B[(Y+T)/4+X(Y-T)/8]\), so its prior mean is \(\pm\alpha_B/8\). The mixed BC Walsh moment is \(\mp\alpha_B\alpha_C/8\) times an additional factor depending on the conditional scaling; the exact rational verifier below evaluates all eight observed word masses and their \(L^1\) difference without any approximate arithmetic. In the range \(|\alpha_C|\le1\), its TV evaluates to the formula above.

## 3. Consequence for provenance compression

At \(\alpha_A=0,\alpha_B\ne0,\alpha_C=0\), the feedback rank equals three whereas the postprocessed rank equals two (R749SMG). For \(\alpha_C\ne0\), the rank can coincide, yet the two experiments remain Blackwell-incomparable: equal rank does not imply one observer's source distinctions can be recovered from the other's outputs. The identity of the selector and whether noise enters before/after it are part of the provenance interface.

## 4. Evidence and exact verification

The companion Python verifier imports R749SMG's standard-library Fraction kernel and checks every \(\varepsilon_B\in\{0,\frac14,\frac34,1\}\), \(\varepsilon_C\in\{0,\frac14,\frac12,\frac34,1\}\), with \(\varepsilon_A=1/2\). It verifies normalization, strictly positive priors, both zero-TV and nonzero-TV equalities using exact rational arithmetic. Result: PASS on 20 independent parameter pairs. The proof applies for all real parameters in the displayed domain by algebraic identities and elementary total-variation contraction.

Remaining question: classify the full stochastic simulation preorder when \(\alpha_A\ne0\), and derive finite-memory observer closure for all admissible future feedback controls; native V29/V39 triadic permission requires an independent source-backed witness.
