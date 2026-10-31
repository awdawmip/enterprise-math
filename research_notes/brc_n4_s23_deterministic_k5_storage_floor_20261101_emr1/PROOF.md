# BRC N=4 / S23: sharp deterministic five-state storage floor

**2026-11-01. Author-side analytic proof, exact Fraction checks, UNREVIEWED / NOT_ADMITTED.** This is an auxiliary six-latent-source, four-time positive-probability observer. It is **not** a theorem about native P000 X6 Cell dynamics, independent time, or the S2 information set.

## Frozen input and quantifiers

We continue the exact BRC N=4 S23 model in Enterprise Math PR #1762, ancestor commit `24287b48d496fcf2eb01777c9e6ee3f90047a36d` (the unrestricted randomized-encoder lower floor 1/47). The six latent cells in order are AU0, AU1, AV, BU0, BU1, BV. The six distinct prepared inputs mix them by

\[
M=\begin{pmatrix}
1/2&1/2&0&0&0&0\\
9/20&11/20&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&1/2&1/2&0\\
0&0&0&1/10&9/10&0\\
0&0&0&0&0&1
\end{pmatrix}.
\]

Each law-independent S23 behavioral stopping policy is a tuple of **eleven** controls: two A/B first-stage stopping probabilities, three second-stage U/AV/BV probabilities, and six third-stage cell-specific probabilities. For each latent cell \(x\), the resulting time law \(f_x^H\) is supported on \(T=1,2,3,4\). The six true prepared time laws are the rows of \(MF^H\), where \(F^H\) is 6-by-4 and row-stochastic. No terminal decision or hidden cell label is observed.

Define the restricted minimax problem

\[
R^{\mathrm{detE}}_{5,m}=\inf_{E\in\{0,1\}^{6\times5},\;E\mathbf1=\mathbf1}\;\inf_{D_1,\ldots,D_m}\;\sup_{H\in S23_{\rm beh}}\;\min_{\ell\le m}\;\max_{i\le6}\operatorname{TV}((MF^H)_i,(MED_\ell)_i),
\]

where the five-state **encoder is deterministic**, the decoders are arbitrary stochastic 5-by-4 kernels chosen before the policy, and the policy-dependent label may be chosen after the policy is known. The decoders never observe the latent source or the random outcome. We also define \(R^{\mathrm{detE}}_{5,\mathrm{full}}\) by allowing a separately selected decoder for *every* complete policy (unlimited policy description); the encoder remains common and deterministic. This full-policy quantity is the infimum over source encoders of the worst-case best decoder, not an unlicensed change in the original finite-label problem.

## Theorem

For **every** integer \(m\ge1\),

\[
\boxed{\frac1{40}\le R^{\mathrm{detE}}_{5,m}
\le\min\left\{\frac34,\ \frac1{40}+1-\left(1-\frac1{2n}\right)^3\right\},\quad n=\lfloor m^{1/11}\rfloor.}\tag{A}
\]

Moreover,

\[
\boxed{R^{\mathrm{detE}}_{5,\mathrm{full}}=\frac1{40},\qquad
\lim_{m\to\infty}R^{\mathrm{detE}}_{5,m}=\frac1{40}.}\tag{B}
\]

For the **original unrestricted randomized encoder** \(E\in[0,1]^{6\times5}\), the earlier analytic lower bound and our explicit deterministic construction imply, even with full-policy-dependent decoding,

\[
\boxed{\frac1{47}\le R_{5,\mathrm{full}}\le\frac1{40}.}\tag{C}
\]

Equation (C) does **not** assert equality for randomized encoders. It isolates an exact deterministic-versus-potentially-randomized storage question.

## Proof of the universal deterministic lower bound

Let \(N=M^{-1}\), exactly

\[
N=\begin{pmatrix}
11&-10&0&0&0&0\\
-9&10&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&9/4&-5/4&0\\
0&0&0&-1/4&5/4&0\\
0&0&0&0&0&1
\end{pmatrix}.
\]

An exact inspection of all \(\binom62=15\) distinct row pairs gives

\[
\boxed{\max_{x\ne y}\|N_{x,*}-N_{y,*}\|_1=40,}\tag{1}
\]

with equality only for the pair (AU0,AU1). This is independently recalculated by the included rational checker. Analytically, the AU row difference is \((20,-20,0,0,0,0)\), of norm 40; any pair from separate diagonal blocks has norm at most the sum of the constituent row norms, which is at most \(21+7/2<40\), and the BU-pair difference has norm 5.

Every deterministic map from six latent cells to at most five code symbols identifies some pair \(x\ne y\). Fix that pair. Take the **lawful** S23 policy \(H_x\) that always continues in both first and second stages and at time three stops exactly when the third-stage observed cell is \(x\); otherwise it stops at time four. Thus the prepared time-three probability column is \(M e_x\). For any selected decoder write \(g=E D_{*,3}\). The code identification forces \(g_x=g_y\), irrespective of the label and of any randomness in the decoder.

Set \(r=M(e_x-g)\). Since \(e_x-g=N r\) and \((e_x-g)_x-(e_x-g)_y=1\), we have

\[
1=|(N_{x,*}-N_{y,*})r|\le\|N_{x,*}-N_{y,*}\|_1\|r\|_\infty
\le40\max_i\operatorname{TV}(p_i^{H_x},\widehat p_i^{H_x}).\tag{2}
\]

The final inequality holds because error on the event \(T=3\) is bounded by total variation of complete time laws. Therefore **every** decoder incurs error at least 1/40 on one of the six indicator policies, depending only on E. Taking sup over H and inf over all decoders proves the lower bound in (A), even when the decoder is informed of the entire policy.

Notice that this argument uses the **deterministic equality of two encoder rows**. A general stochastic five-state encoder has a left nullspace but need not have any two identical rows. Thus (2) cannot be silently transferred to unrestricted E; the predecessor 1/47 bound remains the supported general lower bound.

## Matching constructive upper bound with a full policy description

Let E merge AU0 and AU1 into one code state and retain AV, BU0, BU1, BV separately (five symbols total). For any lawful policy H, let \(f_0,f_1\) be its AU0/AU1 time laws. Set the common merged decoder row to

\[
q^H=\frac{19}{40}f_0^H+\frac{21}{40}f_1^H,\tag{3}
\]

and let the other four decoder rows equal their corresponding latent time laws. Equation (3) is a stochastic probability law with nonnegative weights summing to one. On the first prepared input the true AU law is \((f_0+f_1)/2\), while on the second it is \((9 f_0+11 f_1)/20\); both reconstructed laws equal \(q^H\). Thus the two signed *differences of probability measures* are \(\pm(f_0-f_1)/40\), and

\[
\operatorname{TV}(p_i^H,\widehat p_i^H)
=\frac1{40}\operatorname{TV}(f_0^H,f_1^H)\le\frac1{40}\quad(i=1,2).\tag{4}
\]

(The signed subtraction is only in the **external comparison of readouts**; BRC branch probabilities and decoder weights remain positive. No cancellation of BRC branch mass is asserted.) Every other prepared row is exactly reconstructed. Since the indicator policy \(H_{AU0}\) makes \(f_0=\delta_3\) and \(f_1=\delta_4\), it attains the 1/40 error in (4). This proves the first equality in (B) and its sharpness.

## Finite labels and asymptotic attainment

The S23 behavioral family is the whole compact cube \([0,1]^{11}\) of its eleven causal stopping controls; see the already published eleven-control chart in PR #1762, commit `00e2754b6823b3ecc2add4d486339759061686cf`. Put \(n=\lfloor m^{1/11}\rfloor\ge1\) and quantize each coordinate to the midpoint of one of n equal intervals. There are \(n^{11}\le m\) fixed label decoders, each defined using (3) and the four unmerged latent laws at its quantized control tuple.

For any original control tuple \(\theta\), the nearest quantized tuple \(\widehat\theta\) differs by at most \(e=1/(2n)\) in every control. Couple sequential Bernoulli stops using shared uniforms at their common reached nodes. The probability that the two time outcomes disagree is at most \(\delta_n=1-(1-e)^3\); thus for every prepared input, \(\operatorname{TV}(p^\theta_i,p^{\widehat\theta}_i)\le\delta_n\). At the quantized policy the five-state decoder from (3) has worst error 1/40. By the triangle inequality, the actual policy is reconstructed within \(1/40+\delta_n\).

Separately, uniform output on four times gives 3/4 error using one decoder and any encoder. This proves the upper half of (A). Since \(n\to\infty\) as \(m\to\infty\), the lower and upper bounds converge to 1/40, proving the remaining assertion in (B).

## Exact validation, BRC scope and unresolved obligations

`VERIFY.py` checks all 36 entries of \(MN=I\) in rational arithmetic, all 15 exact inverse-row differences and their unique maximizer, all 2048 lawful deterministic 11-control tables (each coin 0 or 1), and 2048 additional lawful genuinely randomized parameter tables (each coin 1/4 or 3/4). It reconstructs six complete prepared time distributions for each table, making **24576 exact total-variation comparisons**, and checks the bound 1/40. It also checks a boundary-case indicator policy attaining 1/40. Output is in `RUN_EVIDENCE.txt`. Finite checks are consistency tests; equations (1)–(4) and coupling prove the universal theorems for arbitrary real behavioral controls, not merely the enumerated grids.

**BRC usage:** six retained positive latent source laws, six positive prepared mixtures, explicit deterministic quotient E, a four-time future observer, and all eleven legal causal controls. The five-state quotient is **not** future-observer exact (it has a sharp positive residual error); this is a quantitative negative preservation result. It is independent of P000's six native axes and carries no direct X6 dynamics, S2 embedding, physical, empirical, or independent-review claim.

**Next discriminating problem:** Does a genuinely stochastic 5-state encoder achieve a full-policy-visible error strictly below 1/40, or does row-stochastic nonnegativity enforce a stronger general lower bound than 1/47? Investigate the six indicator-policy finite bilinear minimax system with explicit feasible/dual certificates and then check full eleven-control policies. Do not promote a numerical local minimum to a universal theorem. The finite-label ten-tag problems \(R_{4,10},R_{6,10}\) remain independently open at the previously published scope.

**Provenance:** verified GLOBAL_KNOWLEDGE_V1 `main@2dde259b7039962a5f02669e83f7ffc38081e01f` (bootstrap, manual, P000 and ACTIVE worldview); Enterprise Math canonical input `main@42da097851a02b96f8ff2018f5c28096eec13866` (portable research protocol). Connected GitHub principal `awdawmip`. Native service status attempt timed out in this run; earlier reported `STATIC_READONLY_SCOPE_DENIED` / `CONTROL_QUOTA` is historical, not a newly verified owner state. No native CLAIM, Result, Reviewer or admission is represented by this independent author-side source note.
