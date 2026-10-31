# BRC N=4 / S23: exact six-state storage threshold for vanishing policy-observer error

Date: 2026-11-01. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_CHECK_EXECUTED / UNREVIEWED / NOT_ADMITTED. Auxiliary finite positive-probability BRC model, not native Heartbeat X6/time dynamics or an S2 theorem.

## Frozen model and minimax quantity

This continues Enterprise Math PR #1762 at immutable commit 00e2754b6823b3ecc2add4d486339759061686cf, using its law-independent causal S23 behavioral stopping-time grammar. The six latent cells are AU0, AU1, AV, BU0, BU1, BV. The six distinct prepared-input rows have the stochastic mixing matrix

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

The sole observable is stopping time \(T\in\{1,2,3,4\}\). A common row-stochastic encoder \(E\in[0,1]^{6\times k}\) is fixed before the subsequent stopping policy. A policy may select one of at most \(m\) fixed row-stochastic decoders \(D_\ell\in[0,1]^{k\times4}\). The reconstructed laws are the six rows of \(MED_\ell\); the true laws for policy \(H\) are \(p_i^H(T)\). Define

\[
R_{k,m}=\inf_{E,D_1,\ldots,D_m}\ \sup_{H\in S23_{\rm beh}}\ \min_{\ell\le m}\ \max_{i=1,\ldots,6}\operatorname{TV}(p_i^H,(MED_\ell)_i).
\]

## NEW theorem: storage capacity cannot be replaced by policy knowledge

For every \(1\le k\le5\) and \(m\ge1\),

\[
\boxed{R_{k,m}\ge1/47.}\tag{A}
\]

In fact (A) remains valid even with a distinct policy-specific stochastic decoder for every possible policy (unlimited policy labels). The lower-bound witnesses are only six lawful *deterministic* S23 policies.

For \(k\ge6\), predecessor PR #1762 gives

\[
R_{k,m}\le \min\left\{\frac34,\ 1-\left(1-\frac{1}{2\lfloor m^{1/11}\rfloor}\right)^3\right\}
\ \longrightarrow 0\quad(m\to\infty).\tag{B}
\]

Thus **six is the exact minimal number of common source encoding states that permits arbitrarily small uniform stopping-time reconstruction error as strategy labels proliferate**. For \(k\ge6\) the previously established author-side information-rate exponent is \(1/11\); for \(k\le5\) a strict error floor remains. These facts do not determine \(R_{4,10}\) or \(R_{6,10}\).

## Proof: six legal time-three indicator policies

For each latent cell \(x=1,\ldots,6\), choose policy \(H_x\) as follows. The two first-stage stopping probabilities are 0. The three second-stage stopping probabilities (U, AV, BV) are 0. At the third stage stop with probability 1 in precisely the observed latent likelihood-ratio cell \(x\), and with probability 0 in the other five cells. The action does not depend on which source law generated the observation. It uses only the available third-stage information set, so it is a legal deterministic S23 policy. If \(e_x\) denotes the x-th standard basis vector, then

\[
\mathbf p^{H_x}(T=3) = M e_x,\qquad
\mathbf p^{H_x}(T=4)=\mathbf1-M e_x,\qquad
\mathbf p^{H_x}(T=1)=\mathbf p^{H_x}(T=2)=0. \tag{1}
\]

Fix an **arbitrary**, possibly randomized, common six-to-k encoder E, with \(k\le5\). Because \(ME\) is six-by-k and has rank at most five, there is a nonzero \(w\in\mathbb R^6\) with

\[
w^{\mathsf T}ME=0. \tag{2}
\]

The matrix M is invertible, hence \(z=M^{\mathsf T}w\ne0\). Select a cell x for which \(|z_x|=\|z\|_\infty\). Under \(H_x\), any selected decoder D predicts the time-three probability column \(MEv\), where \(v\) is the time-three column of D. Regardless of the number of labels or knowledge of the full policy, equation (2) forces

\[
|z_x|=|w^{\mathsf T}(M e_x-MEv)|
\le\|w\|_1\|M e_x-MEv\|_\infty. \tag{3}
\]

For every prepared-input row, the error on the singleton event \(T=3\) is bounded by the total variation between the complete distributions. Consequently every possible decoder on this policy has

\[
\max_i\operatorname{TV}(p_i^{H_x},(MED)_i)
\ge\frac{\|M^{\mathsf T}w\|_\infty}{\|w\|_1}. \tag{4}
\]

The exact inverse is

\[
M^{-1}=\begin{pmatrix}
11&-10&0&0&0&0\\
-9&10&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&9/4&-5/4&0\\
0&0&0&-1/4&5/4&0\\
0&0&0&0&0&1
\end{pmatrix}.
\]

The absolute entry sum of \(M^{-T}\) is \(40+5+1+1=47\), so \(\|M^{-T}z\|_1\le47\|z\|_\infty\) for every z. Equality is attained at \(z=(1,-1,1,1,-1,-1)^{\mathsf T}\), where \(M^{-T}z=(20,-20,1,5/2,-5/2,-1)^{\mathsf T}\). Thus the exact induced infinity-to-one norm is 47; all 64 sign vertices are also tested by VERIFY.py.

Using \(w=M^{-T}z\), inequality (4) gives \(1/47\) for the policy \(H_x\) selected after the encoder. Since the minimax order is \(\inf_E\sup_H\), that dependence on E is legitimate. The argument includes all real-valued randomized encoders and decoders, not just finite sampled kernels. This proves (A).

## BRC semantics, validation and limits

All branch masses remain positive probabilities; the signed w is an *auxiliary linear-algebra dual witness*, not a signed BRC branch mass or a license for positive-mass cancellation. The population is the six latent source cells, the observers are all six prepared-row time laws, and the future operation language is all legal S23 stopping policies. The six witnesses show exactly why compressing the source to fewer than six common encoding states loses an observable future direction. This is not a native X6 spatial embedding; numerical equality of the two sixes establishes no physical identification.

The executable VERIFY.py uses exact fractions, checks all 36 inverse entries, all 64 sign vertices, all six legal indicator stopping-time laws (with six prepared rows), and an illustrative k=5 stochastic encoder and dual annihilator. RUN_EVIDENCE.txt is actual output. Universal validity in the encoder continuum follows from equations (2)-(4), not finite testing. Bound (B) is reused at its unreviewed author-side scope from PR #1762, without rerunning prior tests.

Pending separate work: sharpen the numerical floor for k=4 and k=5, solve finite m=10, independently audit S23 information sets and decoder quantifiers, test any S2 embedding, and supply a real P000 X6/time and joint-relation/future-observer preservation bridge. No native CLAIM, Result, review, Foundation promotion or empirical physical claim is made.

Provenance: GLOBAL_KNOWLEDGE_V1 fixed main@21a6d767034f342fbb64d3788339333776d5b3bd; Enterprise Math pinned main@0e46715ac981a244ea0b799b29dc4efaf410acc8. Real connected GitHub principal awdawmip. Native status read-only and owner lookup CONTROL_QUOTA; no formal owner assertion.