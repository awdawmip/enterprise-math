# R749SK — Exact minimal affine source coordinates for adaptive signed-Port posterior ratios

Date: 2026-11-13 (Asia/Shanghai). Research continuation of R749SJ in PR #2183; typed abstract R749SF kernel, not a native Cell/Link/Port permission. Frozen scientific source remains \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Predecessor R749SJ: \`@a1b658b031824e1e784949dd77f8c921c45536cc:research_notes/portable_direct/2026-11-12_R749SJ_SIGNED_ADAPTIVE_WALSH_LIKELIHOOD.md\`; R749SI all-time Walsh pullback at same commit. This note is independent author-side exact algebra, not an accepted task Result/review. Continue the lane's existing Researcher \`EM-DIRECT-F5DC4E\`, Activity \`RA-C90B76621B9191DE224257C3\`, without shared CLAIM.

## Question and scope

R749SJ proved that every specified signed-state-dependent gate and joint-Walsh query gives a fractional-linear function of the seven initial nonconstant Walsh moments. It supplied a sufficient union-of-nonzero-Walsh-index carrier but left its sharp minimal rank unresolved. Here "coordinate" means a real affine-linear expectation statistic of the *arbitrary initial eight-state prior*, and sufficiency means exact evaluation of the declared finite posterior ratio family for all strictly interior priors with positive observation likelihood. No lower bound for arbitrary unrestricted nonlinear encodings is asserted.

Let \(\mu\) be an arbitrary probability distribution on the eight signed lifts of a fixed directed unsigned support \((A,B)\). Choose any basis \(\{\chi_W:\emptyset\ne W\subseteq A\cup B\}\) of the seven nonconstant initial Walsh characters. Set \(v=(\hat\mu(W))_{W\ne\emptyset}\in\mathbb R^7\). The set of strictly positive \(\mu\)'s is an open full-dimensional convex subset \(\Omega\) in these coordinates.

For fixed parameter \(p\), a positive-probability observed support word, specified nonnegative sign-adaptive gate likelihoods, and a declared finite family of conditioned signed-time queries, R749SJ yields
\[
F_i(v)=\frac{N_i(v)}{D_i(v)}
=\frac{a_{i0}+a_i\cdot v}{b_{i0}+b_i\cdot v},\quad D_i(v)>0\ \hbox{on }\Omega.
\]
The numerator and denominator are the exact backwards-Walsh arrays, including the empty-mask coefficients. Remove those \(i\) for which \(N_i\) and \(D_i\) are proportional as affine functions (constant posterior ratios).

## Theorem 1: exact minimal ratio-equivalence coordinate rank

For the remaining nonconstant ratios define the linear subspace
\[
L=\operatorname{span}_{\mathbb R}\{a_i,b_i:i\text{ is nonconstant}\}\subseteq\mathbb R^7.
\]
Then the smallest number of independent affine-linear source expectation coordinates from which **every** \(F_i\) can be recovered, by an arbitrary deterministic readout function, is exactly
\[
\boxed{r_{\min}=\dim L
=\operatorname{rank}\begin{bmatrix}a_1\\b_1\\ \vdots\\a_k\\b_k\end{bmatrix}},
\]
where the rows are the seven *nonconstant* Walsh coefficients. Consequently one may use **any row-space basis of this matrix**, not necessarily individual Walsh moments, and the proposed carrier is exact on every admissible prior with positive observation likelihood.

**Proof (necessity, including nonlinear readout).** An affine-linear carrier with \(d\) coordinates is \(C v+c\). For any \(h\in\ker C\), \(v\) and \(v+th\) have identical carrier values for all sufficiently small real \(t\) when \(v\in\Omega\). Exactness forces \(F_i(v+th)=F_i(v)\); clearing the strictly positive denominators and differentiating in \(t\) gives
\[
(a_i\cdot h)D_i(v)-(b_i\cdot h)N_i(v)=0\quad(\forall v\in\Omega).
\]
Since this affine polynomial vanishes on a full-dimensional open set, it vanishes identically. The augmented coefficient vectors \((a_{i0},a_i)\) and \((b_{i0},b_i)\) are linearly independent for a nonconstant ratio, so their scalar combination can vanish only if \(a_i\cdot h=b_i\cdot h=0\). Thus \(\ker C\subseteq L^\perp\) and \(d\ge\dim L\). This argument allows any nonlinear function of the retained affine coordinates, not just linear ratio reconstruction.

**Sufficiency.** A basis of \(L\) permits exact reconstruction of all \(a_i\cdot v\) and \(b_i\cdot v\), hence all \(N_i,D_i,F_i\). Its dimension is \(\dim L\). End of proof.

A constant ratio imposes no coordinate obligation: proportionality of the *augmented* coefficient arrays, not vanishing or overlap of their Walsh supports, is the correct removal test. The exact algorithm is: calculate R749SJ's rational arrays, remove constant ratios by full augmented proportionality, strip the empty coefficient, and row-reduce the remaining arrays over \(\mathbb Q\) when \(p\) and gates are rational. The row rank is the sharp affine-statistical residual for that declared query family. For nonrational parameters the same theorem holds over \(\mathbb R\); symbolic exceptional parameter values may change rank.

## Theorem 2: strict compression and parameter-boundary rank drop on the native six-axis support set

Choose any of the 120 directed unsigned supports \((A,B)\), with old-only axis \(a\in A\setminus B\), and a named shared axis \(b\in B\). Take the forced completion \(C=A\triangle B\), and R749SF's conditional signed transfer: the new sign at axis \(a\) undergoes an independent binary symmetric channel with correlation \(\theta=8p/(1+7p)\); the shared sign at \(b\) is copied.

Add an observable binary gate outcome \(G=1\) **before** the signed transfer with valid likelihood
\[
\ell(x)=\Pr(G=1\mid X=x)=\frac{2+x_a+x_b}{4}\in\{0,\tfrac12,1\}.
\]
An outcome \(G=0\) takes the complementary likelihood. This is the R749SJ explicitly augmented observer/controller model; only \(G=1\) with positive marginal probability is used. Ask the single signed-output parity query \(F_p(\mu)=\mathbb E[Y_aY_b\mid G=1,C,\mu]\). Define initial Walsh moments \(m_a=\mathbb E X_a\), \(m_b=\mathbb E X_b\), \(m_{ab}=\mathbb E X_aX_b\), and combined source coordinates
\[
u=m_a+m_b,\qquad v=m_{ab}.
\]
The exact gate normalizer and query numerator are
\[
D=\tfrac14(2+u),\qquad N=\tfrac{\theta}{4}(2v+u),
\]
and therefore
\[
\boxed{F_p(\mu)=\theta\frac{2v+u}{2+u}}.
\]
For \(p>0\) this is a nonconstant ratio whose two nonconstant coefficient rows span exactly \(\operatorname{span}\{m_a+m_b,m_{ab}\}\); hence its minimal affine-carrier rank is **two**, whereas the naive union-of-nonzero individual Walsh masks has **three** coordinates \(\{m_a,m_b,m_{ab}\}\). At \(p=0\), \(\theta=0\) and \(F_p\equiv0\), so the minimum drops sharply to **zero**; \(p=1\) retains rank two. The formula requires \(D>0\), automatically true for any strictly interior initial eight-state prior, and for all other priors on which \(G=1\) has positive probability.

This establishes a concrete model-internal observer-safe **3-to-2 source-statistic compression** (and rank-0 boundary) across all 120 named unsigned supports without erasing typed Port identities in the actual transition. It is a query-scoped sufficiency theorem, not a claim about all future queries.

## Exact finite validation

\`R749SK_RATIO_RANK_EXACT_CHECK.py\` uses Python standard-library exact \`Fraction\` arithmetic; it reconstructs all 120 initial directed supports, their eight signed lifts and three rational parameter values \(p=0,1/2,1\). It checks 2,880 direct conditional forced-transition/gate parity rows; 360 independent three-sign Walsh coefficient pairs and exact rational row ranks; and 2,880 strictly positive-evidence rational-mixture identities. Expected / actual output: \`status=PASS\`, \`minimal_affine_coordinate_ranks={p=0:0,p=1/2:2,p=1:2}\`. The all-prior and all-family minimality in Theorem 1 rests on the preceding open-set algebraic proof; the finite checks independently exercise the instantiated R749SF model. No float approximations and no native event-permission inference.

## Durable continuation

An adaptive **multi-query** family can share coordinate rows and reduce residual rank further; compute the exact row-space over explicitly declared gates and signed-time queries rather than retaining the support union. Separately compare a real V29/V39 source-authorized triadic Cell/Link/Port event with the R749SF signed controller likelihood; native event validity remains governed by its own guard. This paper is a bounded, constructive response to R749SJ's outstanding minimality question, not a redefinition of P000 or a full-world dynamics claim.
