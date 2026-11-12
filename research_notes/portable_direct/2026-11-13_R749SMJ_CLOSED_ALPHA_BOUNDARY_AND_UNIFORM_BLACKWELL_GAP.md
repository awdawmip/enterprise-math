# R749SMJ — Closed A-noise Blackwell classification

**2026-11-13 (Asia/Shanghai).** Continuing R749SMG/H/I, with unchanged scientific input pin awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This is a conditional eight-source observer theorem; no native V29/V39 event, physical BRC residual, independent review, or shared-task CLAIM is asserted.

## Definitions and result

Let z=(x,y,t), o=(u,v,w) belong to {±1}³, with z₊=y, z₋=t. Set alpha=1−2ε_A, beta=1−2ε_B, gamma=1−2ε_C in [-1,1]. The previous R749SMI kernels, output rows by source columns, are
\[
F_{uvw,xyz}=\frac{(2+\alpha ux)(2+\beta v z_u)(2+\gamma wyt)}{64},\quad
P_{uvw,xyz}=\frac{2+\gamma wyt}{128}\sum_{i=\pm1}(2+ix)(1+\alpha ui)(2+\beta vz_i).
\]
For source-independent stochastic G, a garbling K→L means L=GK; let \(\delta(K\to L)=\inf_G\max_z\mathrm{TV}(L_{\cdot z},(GK)_{\cdot z})\).

**Theorem.** On the entire cube \((\alpha,\beta,\gamma)\in[-1,1]^3\), F=P exactly if alpha=1 or beta=0. Otherwise (alpha<1, beta≠0), F and P are strictly Blackwell-incomparable. Write
\[
M_+=\max\{2(1+\alpha),(1-\alpha)|\gamma|\},\qquad
M_-=\max\{2(1-\alpha),(1+\alpha)|\gamma|\}.
\]
For alpha<1, beta≠0, the following explicit positive lower bounds hold:
\[
\boxed{\delta(F\to P)\ge|\beta|(4-M_+)/64>0,}
\]
\[
\boxed{\delta(P\to F)\ge|\beta|\max\{4(1-|\alpha|),[M_--2|\gamma|]_+\}/64>0.}
\]
At the previously unresolved deterministic A-complement boundary alpha=-1, both deficiencies are bounded below by \(|\beta|(2-|\gamma|)/32\ge|\beta|/32\).

## Proof with strictly positive priors

Introduce the signed Walsh source functions
\[
\phi(x,y,t)=y+t+2x(y-t),\quad\psi(x,y,t)=y+t-2x(y-t)=\phi(x,t,y).
\]
Both have zero uniform mean and absolute value at most 4. Thus \(q^\phi_\pm(z)=(1\pm\phi(z)/8)/8\) and \(q^\psi_\pm(z)=(1\pm\psi(z)/8)/8\) are normalized, with minimum source atom 1/16. Their respective signed differences are \(\phi/32,\psi/32\). The further priors \(\mu_Y=(1+y/2)/8,\mu_T=(1+t/2)/8\) are also strictly positive.

Substitute \(z_i=(y+t+i(y-t))/2\) into F and P, expand their finite Walsh characters and apply \(\sum_{z\in\{\pm1\}^3}\chi_S(z)\chi_T(z)=8\,\mathbf1_{S=T}\). The resulting eight-output vector identities, valid individually at every o=(u,v,w), are:
\[
(F\phi)_{uvw}=\frac{\beta v}{4}[2(1+\alpha)+(1-\alpha)\gamma w],\quad(P\phi)_{uvw}=\beta v;
\]
\[
(F\psi)_{uvw}=\frac{\beta v}{4}[2(1-\alpha)+(1+\alpha)\gamma w],\quad(P\psi)_{uvw}=\frac{\beta\gamma}{2}vw,
\]
where (Fφ)_o means \(\sum_zF_{o,z}\phi(z)\). The identity \(|A+B|+|A-B|=2\max(|A|,|B|)\) gives
\[
\begin{array}{ll}
\mathrm{TV}(Fq^\phi_+,Fq^\phi_-)=|\beta|M_+/32,&\mathrm{TV}(Pq^\phi_+,Pq^\phi_-)=|\beta|/8,\\
\mathrm{TV}(Fq^\psi_+,Fq^\psi_-)=|\beta|M_-/32,&\mathrm{TV}(Pq^\psi_+,Pq^\psi_-)=|\beta\gamma|/16.
\end{array}
\]
The same Walsh expansion for \(\mu_Y,\mu_T\) gives \(\mathrm{TV}(F\mu_Y,F\mu_T)=|\beta|/8\) and \(\mathrm{TV}(P\mu_Y,P\mu_T)=|\alpha\beta|/8\).

For alpha<1, \(M_+<4\): \(2(1+\alpha)<4\) and \((1-\alpha)|\gamma|\le2\). Hence P strictly distinguishes the φ pair more than F, excluding any F→P garbling. For −1<alpha<1, the μ pair is strictly more distinguishable under F, excluding P→F. At alpha=−1, the ψ pair replaces μ: \(M_-=4>2|\gamma|\), again excluding P→F.

For any approximate stochastic garbling with worst-source TV error η, data processing and the triangle inequality imply \(\mathrm{TV}(L\rho,L\sigma)\le\mathrm{TV}(K\rho,K\sigma)+2\eta\) for all priors ρ,σ. Applying this to each displayed gap yields the deficiency bounds. At alpha=−1, \(M_+=2|\gamma|\), \(M_-=4\), giving the symmetric bound. If alpha=1, the internal summand of P vanishes for i=−u and equals twice the intended i=u selector; if beta=0, \(\sum_i(2+ix)(1+\alpha ui)=4+2\alpha ux\). Both substitutions yield P=F. QED.

## Verification, interpretation and next problem

The previous R749SMI factor \(1-|\alpha|\) vanishes at alpha=−1 only because its μ witness becomes neutral. A strictly positive ψ contrast establishes a **nonvanishing two-way information gap** there. The new φ witness also strengthens the F→P bound over the entire closed A-noise interval.

Executed standard-library Python Fraction checker: PASS on all 125 triples from {-1,-1/2,0,1/2,1}³, 2000 stochastic source columns, 4000 signed-output Walsh equalities, strictly positive source priors and all exact TV formulas, including 80 informative non-equivalent parameter triples. The all-real claim rests on the algebra above; the finite grid is regression evidence. Program and JSON are companion files.

Preserve P000 and the native six-axis/signed-source type boundary. No physical BRC trajectory or V29/V39 triadic event was computed here.

**Next:** calculate sharp stochastic deficiencies for the rank-four alpha=−1, gamma=0 family and then finite-memory predictive-Walsh closure; separately resolve native V29/V39 permission and source-to-Port correspondence. Author proof and exact checks complete; independent review pending.
