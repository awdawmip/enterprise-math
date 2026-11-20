# EC49FUS — A certified re-entrant least-favorable-prior window for 30 clipped-price observations

Date: 2026-11-20 (Asia/Shanghai). Scientific mode: independent portable TASK_RESEARCH continuation. Evidence: **AUTHOR_PROVED / EXACT_FRACTION_INTERVAL_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED**.

## Frozen scope and dependencies

- Frozen scientific input: BRC16943 at \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\` (retained; not rebased to current control code).
- Immediate predecessor: [EC49FUR](https://github.com/awdawmip/enterprise-math/blob/0ac1ef58d84517835260e4aefbe6d2c2b3a293c9/research_notes/portable_direct/EC49FUR_DUAL_TV_SUPPORT_PHASE_AND_N30_ONSET.md), with the exact n=30 onset and the two-endpoint total-variation dual. The further dependencies are EC49FUQ (endpoint-only worst nuisance for every upper-tail rule) and EC49FUO (uniform threshold complete class). These dependencies are assumed as published author proofs, not independently reviewed here.
- This is a **lossy binary clipped-price observer**, not native X6 state, an exact three-dimensional slice, or a lossless quotient of branch/port/provenance information. P000 and the residual-faithful worldview are unchanged.

## Model

Fix \(n=30\), \(a=749/5000=0.1498\), \(c=79/500=0.158\), and \(x\in I=[a,c]\). Write \(Z=0\) for the compactified nuisance limit and \(E=31597745/1653649\) for its upper endpoint. Define

\[
\beta=3/637,\qquad
u_\theta=\frac{21829245984}{45529434409-456083905\theta},\qquad
T_\theta(x)=(1-x)(1-\beta x+\beta x\theta).
\]

Under the two hypotheses the one-bit success probabilities are \(p_\theta=1-T_\theta\) and \(q_\theta=1-u_\theta T_\theta\). For a count \(K=k\),

\[
\Delta_\theta(k;x)=\binom{30}{k}
\{q_\theta^k(1-q_\theta)^{30-k}-p_\theta^k(1-p_\theta)^{30-k}\}.
\]

Let \(D_\theta^{\ge j}(x)=\sum_{k=j}^{30}\Delta_\theta(k;x)\),
\(d_k=\Delta_E(k)-\Delta_0(k)\),
\(G=D_E^{\ge9}-D_0^{\ge9}\), \(H=D_E^{\ge10}-D_0^{\ge10}\).
For \(\lambda\in[0,1]\) set \(\Delta_\lambda=\Delta_0+\lambda d\) and
\(f_x(\lambda)=\sum_{k=0}^{30}[\Delta_\lambda(k;x)]_+\).
By EC49FUR's exact dual, the composite minimax risk is
\[
V_{30}(x)=\tfrac12[1-\min_{\lambda\in[0,1]}f_x(\lambda)].
\]

## New theorem: one complete entry-and-exit mixing window

There exist two **distinct unique algebraic widths**
\[
\boxed{x_{\rm in}\in(0.149800823443,\ 0.149800823445)}
\]
and
\[
\boxed{x_{\rm out}\in(0.157052266639,\ 0.157052266641)}
\]
inside \(I\), respectively defined by
\[
G(x_{\rm in})=0,\qquad \Delta_E(9;x_{\rm out})=0.
\]
For \(x\in[x_{\rm in},x_{\rm out}]\) put
\[
\lambda_9(x)=
-\frac{\Delta_0(9;x)}{\Delta_E(9;x)-\Delta_0(9;x)},\qquad
\gamma_9(x)=
-\frac{H(x)}{\Delta_E(9;x)-\Delta_0(9;x)}.
\]
The following statements completely classify the minimax priors and tests throughout \(I\).

| Width | All least-favorable endpoint-mixture weights \(\lambda\) | Optimal decision \(\phi(K)\) |
|---|---|---|
| \(a\le x<x_{\rm in}\) | unique \(\lambda=1\) | right iff \(K\ge9\) |
| \(x=x_{\rm in}\) | interval \([\lambda_9(x_{\rm in}),1]\) | right iff \(K\ge9\) |
| \(x_{\rm in}<x<x_{\rm out}\) | unique \(\lambda=\lambda_9(x)\in(3/4,1)\) | right for \(K\ge10\), left for \(K\le8\); right at \(K=9\) with probability \(\gamma_9(x)\in(0,1)\) |
| \(x=x_{\rm out}\) | unique \(\lambda=1\) | right for \(K\ge10\), left for \(K\le8\); at \(K=9\), right with any probability \(0\le\gamma\le\gamma_9(x_{\rm out})\) |
| \(x_{\rm out}<x\le c\) | unique \(\lambda=1\) | right iff \(K\ge10\) |

The corresponding exact minimax advantage \(A=1-2V\) is
\[
\boxed{
A_{30}(x)=
\begin{cases}
D_E^{\ge9}(x),&a\le x\le x_{\rm in},\\[2pt]
(1-\lambda_9(x))D_0^{\ge10}(x)+\lambda_9(x)D_E^{\ge10}(x),
&x_{\rm in}<x<x_{\rm out},\\[2pt]
D_E^{\ge10}(x),&x_{\rm out}\le x\le c.
\end{cases}}
\]
At \(x_{\rm in}\), the entire nontrivial interval of priors is least favorable; immediately to its right the unique prior weight is near \(0.773938\). At \(x_{\rm out}\), the unique mixed weight tends continuously to \(1\). This is a **re-entrant pure-upper-endpoint phase**: pure \(E\) \(\to\) compulsory two-endpoint mixture \(\to\) pure \(E\) as width increases. In the middle phase the primal randomization probability changes continuously from \(1\) to approximately \(0.818465\). At the exit it becomes set-valued, and above the exit the deterministic \(K\ge10\) rule is optimal.

## Proof

**1. Certified continuous signs.** The companion verifier performs outward rational interval arithmetic over 128 closed, overlapping-at-boundaries equal slabs of \(I\); every endpoint and operation is a \`fractions.Fraction\`. On all of \(I\) it certifies the strict inequalities
\[
\Delta_E(8)<0,\quad \Delta_0(9)<0,\quad \Delta_0(10)<0,
\quad \Delta_E(10)>0,
\]
\[
\Delta_{\lambda=3/4}(9)<0,\quad
\Delta_{\lambda=1/3}(10)>0,\quad
H<-1/100,\quad G'>1/4.
\]
Reported *lower margins beyond these claimed bounds* are respectively
\(0.022905428202,\ 0.017516201352,\ 0.004279078988,\ 0.025639732583,\ 0.000507117662,\ 0.003640364269,\ 0.005881801324,\ 0.29058160131\) (decimal displays are truncated; signs are checked exactly). The derivative is computed from the exact binomial-tail identity
\[
\frac{d}{dx}D_\theta^{\ge j}
=30\binom{29}{j-1}
\{q_\theta^{j-1}(1-q_\theta)^{30-j}q'_\theta
-p_\theta^{j-1}(1-p_\theta)^{30-j}p'_\theta\},
\]
with \(p'=-T'\), \(q'=-uT'\).
This is a genuine continuous interval certificate, not a point grid or floating sample.

**2. Two unique algebraic roots.** The verifier evaluates
\(G(149800823443/10^{12})<0<G(149800823445/10^{12})\).
With \(G'>1/4\) everywhere in \(I\), \(G\) has precisely one root there. Likewise
\(\Delta_E(9;157052266639/10^{12})>0\) and
\(\Delta_E(9;157052266641/10^{12})<0\).
For \(u=u_E\in(0,1)\), the sign of \(\Delta_E(9;x)\) equals the sign of
\[
u^{7/3}(1-uT_E(x))-(1-T_E(x))
=(u^{7/3}-1)+(1-u^{10/3})T_E(x).
\]
The latter is strictly increasing in \(T_E\), while \(T_E(x)\) is strictly decreasing in \(x\in I\); hence \(\Delta_E(9;x)\) changes sign exactly once in \(I\). Both equations are rational-coefficient polynomial equations before isolating the roots, so the widths are algebraic.

**3. Exact minimizer of the TV dual.** On \(x<x_{\rm out}\) the signed mass \(\Delta_E(9)>0>\Delta_0(9)\). Hence \(\lambda_9\in(3/4,1)\), using the verified \(\Delta_{3/4}(9)<0\). At \(\lambda_9\), the count-9 mixed signed mass vanishes. The count-10 mass is positive because \(\Delta_{1/3}(10)>0\), \(\Delta_0(10)<0<\Delta_E(10)\) and \(\lambda_9>3/4>1/3\). Count 8 is negative, since both endpoint likelihood-ratio sequences have a single crossing and both endpoint count-8 masses are negative. The predecessor's strict mixed-binomial monotone likelihood ratio shows that all counts \(0,\dots,8\) are negative and \(10,\dots,30\) positive at this kink. Immediately to the left of \(\lambda_9\), \(f_x' = H(x)<0\); immediately to the right, \(f_x'=G(x)\).

If \(x<x_{\rm in}\), \(G(x)<0\), and the convex function \(f_x\) has a strictly negative left derivative at \(1\); its unique minimizer is \(1\). If \(x=x_{\rm in}\), \(G=0\), \(H<0\), and the exact minimizer set is \([\lambda_9,1]\). If \(x_{\rm in}<x<x_{\rm out}\), \(H<0<G\); the unique minimizer is \(\lambda_9\). At \(x=x_{\rm out}\), the count-9 \(E\)-mass is zero and \(f_x'(1-)=H<0\), again giving unique \(\lambda=1\). For \(x>x_{\rm out}\), the signs \(\Delta_E(9)<0<\Delta_E(10)\) give the strict endpoint Bayes rule \(K\ge10\), and \(f_x'(1-)=H<0\), so the unique minimizer stays at \(1\).

**4. Primal strategies and exact risks.** Before entry, the pure-\(E\) Bayes rule is \(K\ge9\); its worst value is at \(E\). In the compulsory-mixing window the prior's Bayes signed mass is zero only at \(K=9\), so the primal saddle test can randomize there. Matching the two endpoint advantages yields
\[
D_0^{\ge10}+\gamma\Delta_0(9)
=D_E^{\ge10}+\gamma\Delta_E(9)
\iff \gamma=-H/d_9.
\]
The strict \(H<0<G=H+d_9\) implies \(0<\gamma<1\). At the entry it tends to \(\gamma=1\). At the exit, \(\Delta_E(9)=0\); any \(0\le\gamma\le H/\Delta_0(9)=\gamma_9(x_{\rm out})\) keeps the zero-endpoint advantage at least as large as the pure-\(E\) optimum. Above the exit the unique \(E\) Bayes test is \(K\ge10\). Inserting the dual minimizer into the positive-part sum gives the stated piecewise exact \(A_{30}\) and hence the minimax risk.

## Reproduction and evidence boundary

Execute \`python3 research_notes/portable_direct/EC49FUS_N30_MIXED_WINDOW_VERIFY.py\` with Python 3 standard library. It checks every claim from step 1, both isolating rational intervals, and three rational representative widths. Observed local result on 2026-11-20: \`PASS 128 exact interval slabs\`; displayed parameters at \(x=3/20\): \(\lambda_9\approx0.779814723978\), \(\gamma_9\approx0.995202093564\). Exact \`Fraction\` comparisons, not displayed decimals, decide PASS.

The proof depends on the exact-source parent theorems (threshold complete class and endpoint reduction), whose independent mathematical review remains pending. No physical effect, native X6 transport, P000 modification, formal CLAIM, Result or independent Review is asserted.

## Next unresolved science

Determine the next re-entrant two-endpoint window for \(n=30\) after \(x_{\rm out}\) (numerical exploration suggests one near the next endpoint threshold), isolate its two algebraic boundaries by exact certificates, and classify the ordering/number of these windows as \(n\) varies. Preserve the complete finite-width observer and price-source provenance as separate carriers when comparing against native BRC/X6 residual models.

Provenance: prior author \`EM-DIRECT-8454C6\`, SID \`MCP-44cfc4e6f2094f96861854ebefc77e84\`, exact activity \`RA-ED136F89271FD89288F3E58D\` are recorded lineage; current control read establishes no active formal execution authorization. Portable scientific publication and activity bookkeeping are distinct.
