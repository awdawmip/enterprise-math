# R762HY — Exact second-order correction for rooted signed Port/BRC returns

Date: 2026-11-21. Scientific state: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / NOT_REVIEWED. Scope: frozen six-axis **composite Port candidate**, not native TRIADIC_CLOSURE_E dynamics. Frozen scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Mathematical antecedent: R762HX_SIGNED_PORT_LOCAL_LIMIT.md@13feed6f521a5d221700a918d86db4b903e1630c. This refinement reuses the predecessor's six-saddle classification, which has not been independently reviewed.

## Precise result

Let the 15 Ports be the two-element subsets of X={0,1,2,3,4,5}. A directed Port transition p→q is legal exactly when |p∩q|=1. Each ordered transition has three-axis support h_{p∪q}∈Z^6 and an independently labeled sign ±. K_m(p) counts all m-step rooted closed Port walks with total signed six-axis displacement zero, retaining order and multiplicity.

For odd m, K_m(p)=0. For even m→∞,

\[
\boxed{K_m(p)=\frac{10\sqrt5}{27\pi^3}\frac{16^m}{m^3}
\left(1+\frac{19}{6m}+O(m^{-2})\right).}
\]

The second-order relative coefficient **19/6** is exact and root-independent. This is a model-internal asymptotic of the labeled pair (Port walk, sign choices), not a histogram-by-histogram existence theorem, physical heartbeat law or primitive triadic law.

## Proof

Use the exact derived Fourier observer B(u), a real symmetric 15×15 matrix with entries cos(〈u,h_{p∪q}〉)/8 for adjacent p,q, zero otherwise. Every BRC source still has a separate positive integer multiplicity and signed displacement; the Fourier observer does not update native physical state. At u=0 the matrix A=B(0) has eigenvalues 1 (simple), 1/4 (multiplicity 5), and -1/4 (multiplicity 9). R762HX proves precisely six unit-modulus saddles u=(jπ/3)1, j=0,…,5, with spectral gap away from them.

**Constant eigenprojection amplitude.** The permutation group of six axes acts transitively on Port roots and preserves the count, so K_m(p) is independent of p. Thus the rooted integral equals 1/15 times the trace integral. Near each saddle, the simple leading eigenvalue enters the trace with **amplitude exactly 1**, not a varying diagonal eigenprojection. At even m the six contributions have identical sign and expansion.

Set f=15^{-1/2}1, Σ=(3/10)I_6+(1/5)11ᵀ. The exact inverse and determinant are
\[
\Sigma^{-1}=(10/3)I_6-(4/9)11^T,\qquad
\det\Sigma=729/200000.
\]
For a fixed six-vector u, the expansion B(tu)=A+t²B₂(u)+t⁴B₄(u)+O(t⁶) has entries on legal Port edges
\[
(B_2)_{pq}=-\langle u,h_{p\cup q}\rangle^2/16,\qquad
(B_4)_{pq}=\langle u,h_{p\cup q}\rangle^4/192.
\]
Let Π₅, Π₉ project onto A-eigenspaces of dimension 5 and 9, and R=(4/3)Π₅+(4/5)Π₉. Analytic symmetric-eigenvalue perturbation gives
\[
\lambda(tu)=1-\tfrac12 t^2 Q(u)+t^4 L_4(u)+O(t^6),\quad
Q(u)=u^T\Sigma u,\quad
L_4=f^TB_4f+f^TB_2RB_2f.
\]
The first contribution is fᵀB₄f=(1/24)E_S〈u,h_S〉⁴, averaging uniformly over all 20 triple supports, each occurring on six ordered Port edges.

**Port-resolvent term.** For p={a,b}, define the quadratic row sum
\[
\rho_p(u)=(B_2\,1)_p=-\tfrac18\sum_{c\notin p}(u_a+u_b+u_c)^2.
\]
Its mean over all 15 Ports is -Q(u)/2. Let U be centered Gaussian with covariance Σ^{-1}; the elementary Gaussian fourth-moment identity yields
\[
\operatorname{Cov}(\rho_p(U),\rho_q(U))
=\frac1{32}\sum_{c\notin p}\sum_{d\notin q}
(h_{p\cup\{c\}}^T\Sigma^{-1}h_{q\cup\{d\}})^2.
\]
Here h_SᵀΣ^{-1}h_T=(10/3)|S∩T|-4, so the entire 15×15 covariance is in the Johnson scheme J(6,2). Its entries by pair relationship are
\[
c_0=43/6\;(p=q),\quad c_1=77/24\;(|p\cap q|=1),
\quad c_2=73/36\;(p\cap q=\varnothing).
\]
On the standard five-dimensional and remaining nine-dimensional representations, the covariance eigenvalues are respectively
\[
\kappa_5=c_0+2c_1-3c_2=15/2,\qquad
\kappa_9=c_0-2c_1+c_2=25/9.
\]
Because B₂f=ρ/√15 and R annihilates constants,
\[
\mathbb E_U[f^TB_2(U)RB_2(U)f]
=\frac1{15}(5\cdot\frac43\kappa_5+9\cdot\frac45\kappa_9)=14/3.
\]

**Gaussian integral.** Every support h_S has h_SᵀΣ^{-1}h_S=6, giving E[(Uᵀh_S)^4]=108, hence E[fᵀB₄(U)f]=9/2. The quadratic form Q(U) follows chi-squared with six degrees of freedom, so E[Q(U)^2]=48. Taking the logarithm of the leading eigenvalue gives
\[
\log\lambda(tu)=-\tfrac12t^2Q(u)+t^4\big(L_4(u)-Q(u)^2/8\big)+O(t^6).
\]
With t=m^{-1/2}, the first relative Gaussian correction therefore equals
\[
\mathbb E[L_4(U)-Q(U)^2/8]=9/2+14/3-6=\boxed{19/6}.
\]
Analyticity and evenness of the leading eigenvalue around each saddle give uniform sixth-order Taylor control; the R762HX spectral gap controls the complement. Gaussian integration of the next Taylor term gives a relative O(m^{-2}) remainder. Combining the six equal saddle contributions with the R762HX leading constant proves the displayed result.

## Exact rational check

R762HY_CHECK.py uses rational Port incidence and all 225 ordered Port pairs to derive the covariance matrix, the Johnson eigenvalues and the exact 19/6 correction. It independently checks the symmetric spectral perturbation equation in the rational direction (1,2,-1,0,3,-2), obtaining λ₂=-15/4 and λ₄=6009/400, and verifies detΣ=729/200000. Actual invocation returned PASS R762HY. R762HY_EVIDENCE.json records the exact results and finite verification boundary.

The program validates the finite rational algebra, not R762HX's full continuous-saddle classification or the analytic error estimate independently. The refined asymptotic is conditional on those preserved predecessor lemmas, which remain NOT_REVIEWED. No new trigonometric physical input, native heartbeat update, classical-to-BRC residual attribution or signed primitive TRIADIC_CLOSURE_E permission is inferred.

## Meaning and next open questions

The next-order coefficient decomposes into a one-step Edgeworth contribution -3/2 and a positive Port-correlation resolvent contribution 14/3. The internal Port state therefore changes the first finite-size correction even when leading covariance is unchanged.

An independent next unit can compute the relative m^{-2} coefficient and an effective finite-m error bound. The original stronger question remains: does there exist a **connected rooted Port-Euler histogram n** with N_p(n)>0 and six-axis coordinate-even H(n), but no zero-displacement sign assignment C(n)=0? A total asymptotic is not a proof of signability of each individual histogram. Preserve primitive TRIADIC_CLOSURE_E as the mother objective.