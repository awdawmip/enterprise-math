# D25/LIFT GH-36/GH-37: cyclic return band and source-complete Laurent finite parts

2026-10-28, author-side TASK_RESEARCH, logical lane chatgpt-research-hourly-enterprise-math-20260923 (not maintenance chatgpt-hourly-enterprise-math-20260921). Status AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains OPEN. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

## Exact context

Let p=4d+3>=7 be prime, k=F_p, z a nonzero element different from 1. Reuse GH-13/GH-15:
\[
a_z(x)=z(4x+1)^3/[(4x+2)(4x+3)(4x+4)],\quad
f(x)=8x+1,\quad t_j(x)=\prod_{i<j}a_z(x+i),
\]
\[
R_z(x)=(z-1)^{-1}\sum_{j=0}^{p-1}f(x+j)t_j(x),\quad
C_r=t_r(0)\ (0\le r\le d),\quad
T=\sum_{r=0}^d f(r)C_r.
\]
All C_r are units. Define
\[
\ell_i=12/(4i+1)-4\sum_{b=2}^4(4i+b)^{-1},\quad
\ell_i'=-48/(4i+1)^2+16\sum_{b=2}^4(4i+b)^{-2},
\quad L_r=\sum_{i<r}\ell_i,\ L=L_d,\ J=\sum_{i<d}\ell_i'.
\]
The Laurent coefficient H_r^{fin}=[epsilon^0]R_z(r+epsilon), and A_0,B_0 are its order -2 and -1 coefficients at rank zero. These are NOT the original Hasse H0/B0.

## GH-36: the missing regular cyclic return

Because a_z and f are p-periodic in k(x), and the GH-13 complete product t_p(x)=z, for every 0<=r<=d and 0<=j<p:
\[
t_j(r+\epsilon)=
\begin{cases}
t_{r+j}(\epsilon)/t_r(\epsilon),&r+j<p,\\
z\,t_{r+j-p}(\epsilon)/t_r(\epsilon),&r+j\ge p.
\end{cases}\tag{36.1}
\]
Therefore the originally indexed late return terms, including their full rational jets, satisfy
\[
\mathcal W_r(\epsilon):=\sum_{j=p-r}^{p-1}f(r+j+\epsilon)t_j(r+\epsilon)
=\frac{z}{t_r(\epsilon)}\sum_{i=0}^{r-1}f(i+\epsilon)t_i(\epsilon).
\tag{36.2}
\]
All right-side products are regular units at epsilon=0; the r=0 sum is empty. Set P_r=\sum_{i<r}f(i)C_i. Expanding t_i(\epsilon)=C_i(1+L_i\epsilon+O(\epsilon^2)) proves
\[
\boxed{\mathcal W_r(0)=zP_r/C_r,\quad
\mathcal W_r'(0)=\frac z{C_r}
\left[\sum_{i<r}C_i(8+f(i)L_i)-L_rP_r\right].}\tag{36.3}
\]
At the genuine upper endpoint, f(d)=8d+1=-5 (mod p):
\[
\boxed{\mathcal W_d(0)=z(T/C_d+5).}\tag{36.4}
\]
In particular, IF T=0, then the return band is exactly 5z, a NONZERO unit. At z=9 it equals 45 (mod p), nonzero for every p>=7 of the stated class. Thus a supposed proof that every late source band vanishes separately is invalid. Proving T_{p,9}=0 is equivalently proving the independent arithmetic assertion W_d(0)=45. This equivalence alone is not its proof.

Source-index detail: at rank d, original j=3d+3,...,4d+2 follow the cubic numerator zero AND the third denominator zero in the shifted product. They are regular and cannot be erased. Equations (36.1) and (36.2) are exact identities of rational functions, not a finite-sample fit.

## GH-37: complete finite parts and exact source-band nonclosure

Use GH-35 sequences k_0=h_0=1 and
\[
k_{s+1}/k_s=(4s+2)^3/[(4s+3)(4s+4)(4s+5)],\quad
h_{s+1}/h_s=(4s+3)^3/[(4s+4)(4s+5)(4s+6)],\quad 0\le s<d.
\]
Let j_0=2d+2=(p+1)/2. Define the two distinct first-log tails and the new second-log tail
\[
\rho_s=\sum_{u<s}\left(12/(4u+2)-\sum_{b=3}^5 4/(4u+b)\right),
\quad
\lambda_s=\sum_{u<s}\left(12/(4u+3)-\sum_{b=4}^6 4/(4u+b)\right),
\]
\[
\eta_s=\sum_{u<s}\left(-48/(4u+3)^2+\sum_{b=4}^6 16/(4u+b)^2\right).
\]
Use GH-35 alpha_p (nonzero leading Laurent coefficient of t_{j0}(epsilon)/z^{j0}) and lambda_* (regularized first-log slope). The second-log slope of that same regularized leading product is
\[
\eta_*=-48\sum_{i<j_0}(4i+1)^{-2}
+16\sum_{\substack{i<j_0,\ b=2,3,4\\4i+b\not\equiv0\ (p)}}(4i+b)^{-2}.
\]
Exactly two zero denominator factors are first divided out as 4epsilon and contribute zero logarithmic derivatives. Every displayed inverse is a unit. Write M_s=lambda_*+lambda_s, N_s=eta_*+eta_s. Define UNNORMALIZED source-band finite coefficients
\[
\begin{aligned}
U_0^{(1)}&=2zC_d\sum_{s=0}^d k_sz^s[8+(8s+3)(L-6+\rho_s)],\\
U_d^{(1)}&=2z\sum_{s=0}^d k_sz^s[8+(8s+3)(-6+\rho_s)],\\
U_0^{(2)}&=\alpha_pz^{j_0}\sum_{s=0}^d h_sz^s
[8M_s+(8s+5)(M_s^2+N_s)/2],\\
U_d^{(2)}&=\alpha_pz^{j_0}C_d^{-1}\sum_{s=0}^d h_sz^s
[8(M_s-L)+(8s+5)((M_s-L)^2+N_s-J)/2].
\end{aligned}\tag{37.1}
\]
Then the **two authentic Laurent finite endpoints** have explicit independent source sums:
\[
\boxed{H_0^{fin}=\frac{T+U_0^{(1)}+U_0^{(2)}}{z-1},\quad
H_d^{fin}=\frac{f(d)+\mathcal W_d(0)+U_d^{(1)}+U_d^{(2)}}{z-1}.}\tag{37.2}
\]
Proof: at rank zero, j=0,...,d are regular (sum T), j=d+1,...,2d+1 have one denominator pole, j=2d+2,...,3d+2 have two denominator poles, and the rest have positive valuation. Their regularized product first/second logarithmic derivatives yield the first and third formulas in (37.1), since a term with leading u/epsilon^2 and jets (M,N) contributes finite part u[8M+f_j(M^2+N)/2]. At rank d, the same initial two bands occur at j=1,...,d+1 and j=d+2,...,2d+2. Dividing by t_d(epsilon)=C_d exp(L epsilon+J epsilon^2/2+...) subtracts L,J. The initial shifted pole a_z(d+epsilon)=2z/epsilon (1-6epsilon+28epsilon^2+...) adds -6. The middle j=2d+3,...,3d+2 terms have positive valuation; the late j=3d+3,...,4d+2 are the regular GH-36 return. This proves (37.2).

For an exact band-wise check, retain GH-35 polynomial labels
\[
Q=\sum_{s=0}^d(8s+3)k_sz^s,\quad K=\sum_{s=0}^dh_sz^s,\quad
\mathcal H=\sum_{s=0}^d(8s+5)h_sz^s,\quad
D=\sum_{s=0}^d(8s+5)h_s\lambda_sz^s.
\]
Put b_1=2zC_dQ, b_2=alpha_p z^{j_0}(lambda_*\mathcal H+8K+D), a=alpha_p z^{j_0}\mathcal H. The known GH-35/GH-16 residues are B_0=(b_1+b_2)/(z-1), A_0=a/(z-1). **Each original provenance band separately** satisfies
\[
\begin{aligned}
C_dU_d^{(1)}-U_0^{(1)}&=-Lb_1,\\
C_dU_d^{(2)}-U_0^{(2)}&=-Lb_2+(L^2-J)a/2,\\
C_d(f(d)+\mathcal W_d(0))-T&=(z-1)(T-f(d)C_d).
\end{aligned}\tag{37.3}
\]
Hence
\[
C_dH_d^{fin}-H_0^{fin}
=T-f(d)C_d-B_0L+A_0(L^2-J)/2.
\tag{37.4}
\]
This rederives the **already known** GH-15 Laurent telescope from separate source bands. Substituting (37.2) back into GH-15 returns T=T, **not** a new vanishing theorem. This is a precise no-closure finding for this combination of GH-15/GH-35; it does NOT rule out other Laurent, CM or WZ proofs. The remaining arithmetic content is exactly the regular return-band trace.

## Verification and limits

The actual locally executed exact Python checker (full author artifact) covered 242 (p,z) cases, all primes 7<=p<1500, p=3 mod4, z in {2,9}; in 29 target cases p=19 mod24 it verified the already sourced A_0=0. It independently enumerated the complete p-term rational cyclic sum at ranks 0,d by finite-field valuations, first/second log jets, compared (37.2), the separate differences (37.3), GH-15, and for small primes all source-index wrap terms and their first derivatives (36.3). No floating-point arithmetic. For p=19,z=9: T=0, W_d=7=45 mod19, W_d'=10, H_0^{fin}=17, H_d^{fin}=5, A_0=0, B_0=8. p=43,67 yield W_d=2,45 respectively (both equal 45 modp). Finite checks support the author algebra; they do not prove a universal T_{p,9} congruence or constitute independent review.

BRC COMPOSE_APPLIED: carrier keeps exact (p,z,r,j), source-band identity, signed coefficients, epsilon valuation and two log jets, both finite endpoints and returned regular terms. Observer (A_0,B_0,H_0^{fin},H_d^{fin},W_r(0),W_r'(0)); future operation true finite telescope or independently derived characteristic-p character/CM/WZ certificate. No positive-weight-only projection or native X6 claim.

Next unproved obligation: obtain an *independent* arithmetic certificate for W_d(0)=45, equivalently T_{p,9}=0, first at p=19 mod24 (potentially the wider p=3 mod4 conjectural class). Do NOT recombine (37.1)-(37.4) and claim a proof: it is circular. Preserve original GH-20/21 next-digit sources, GH-5 S, R23/R36 Green, Hasse six ports, [X]U mod p^2, Frobenius eta/kappa, native p=373, and independent Driver review. No protected previous session/claim/staging or frozen source pin was modified. Existing native control support remains enterprise-math#1558.

Existing inputs: GH-13 cyclic rational resolvent, GH-15 Laurent endpoint identity, GH-16 obstruction, GH-35 two-pole-band residue. The new units are the return-band identity and the complete finite-part decomposition/no-closure diagnosis, not re-publication of these inputs.