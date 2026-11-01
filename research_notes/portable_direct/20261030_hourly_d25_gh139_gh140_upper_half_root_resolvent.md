# D25/LIFT GH-139–GH-140 — upper-half root resolvent and original-mark universal certificates

**Date:** 2026-10-30 Asia/Hong_Kong. **Lane:** chatgpt-research-hourly-enterprise-math-20260923 (TASK_RESEARCH); not the maintenance conversation. **Mother task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; **publication:** TP2-B6F4FC938FF94941C1B7. **Frozen mathematical Source pin:** c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). **Class:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. No native research authorization, CLAIM, run or Source checkpoint is asserted.

## GH-139: general upper-half root-resolvent formula

Fix an odd prime p>=5, q=p^2, e=(q-1)/2, k=F_q, g_B(X)=X^2+X+B, f_B(X)=Xg_B(X) and the quadratic character chi of k with chi(0)=0. Consume the exact GH-124/GH-129 moment definition

\[
S_r(B)=\sum_{f_B(x)\ne0}\chi(f_B(x))(x/f_B(x))^r.
\]

Since the x=0 summand would vanish, sums may equivalently include x=0 while excluding g_B(x)=0. For each 0<=t<=e, the identity g^e=chi(g)=g^{-e} for nonzero g gives

\[
\boxed{S_{e+t}(B)=\sum_{g_B(x)\ne0}\chi(x)g_B(x)^{-t}.}\tag{1}
\]

This concerns the complementary upper-half index window, distinct from the lower-half GH-129 coefficient identity for 0<=r<e.

If B is smooth (B != 0,1/4) and g_B=(X-alpha)(X-beta) splits with alpha,beta in k, both roots are nonzero and distinct. Then

\[
\boxed{S_e(B)=-\chi(\alpha)-\chi(\beta).}\tag{2}
\]

For 1<=t<=e and each ordered pair (a,b)=(alpha,beta) or (beta,alpha) set

\[
c_{a,j}^{(t)}=(-1)^{t-j}\binom{2t-j-1}{t-j}(a-b)^{-(2t-j)},\quad
L_j(a;b)=-\binom ej a^{e-j}-\frac{\chi(b)}{(b-a)^j}
\quad(1\le j\le t).
\]

Then the **exact finite sum of pole coefficients** is

\[
\boxed{S_{e+t}(B)=\sum_{j=1}^{t}\left(
c_{\alpha,j}^{(t)}L_j(\alpha;\beta)
+c_{\beta,j}^{(t)}L_j(\beta;\alpha)
\right).}\tag{3}
\]

**Proof:** Expand 1/((X-alpha)^t(X-beta)^t) into its two principal parts; the coefficient at (X-a)^(-j) is c_(a,j) above. For 1<=j<=e, translate y=x-a and expand (y+a)^e. The k^times power sum is -1 exactly when the exponent is a multiple of q-1, otherwise zero. In the range -j<=i-j<=e-j only i=j contributes, proving
\(\sum_{x\ne a}\chi(x)/(x-a)^j=-\binom ej a^{e-j}\).
Remove the omitted other root x=b to obtain L_j(a;b), then sum the principal parts. This proves (2)–(3) in characteristic p, with all omitted-root support explicitly retained.

## GH-140: elementary norm obstruction, no CM trace input

Now assume **every prime p>=11 with p ≡3 (mod 8)**. In k=F_p(rho) let rho²=2, T=2rho/3, B0=(1+T)/8, D=1-4B0=(1-T)/2 and B0(1-4B0)=1/144. Choose eta²=6 in k and define

\[
s=(\rho-1)/\eta,\qquad
\alpha=(-1+s)/2,\quad\beta=(-1-s)/2.
\]

As s²=D, these are the distinct nonzero roots of g_(B0). Frobenius satisfies rho^p=-rho. Two exhaustive, elementary cases for the F_p norm of alpha hold:

\[
\operatorname{N}_{k/F_p}(\alpha)=
\begin{cases}
2(1/4+\eta/12)^2,&\eta^p=\eta,\\
2(1/4-\rho/(2\eta))^2,&\eta^p=-\eta.
\end{cases}\tag{4}
\]

Each square factor lies in F_p^times: vanishing would imply respectively 6=9 or 6=8 in F_p, impossible for p>=11. Replacing eta with -eta swaps alpha and beta and yields the same property for beta. Since (2/p)=-1 for p≡3 (mod 8), and chi_k(z)=chi_p(N(z)), **both root characters are -1**:

\[
\boxed{\chi_k(\alpha)=\chi_k(\beta)=-1.}\tag{5}
\]

This is a new direct proof of the original-mark root-square obstruction, independently of GH-116/GH-118's CM trace and group-order calculations.

Substitute (5) in the GH-139 resolvent; e=-1/2 in characteristic p. For a split smooth B whose two root characters are -1, the first three shifted values simplify to

\[
S_{e+1}=\frac{1-8B}{2B(1-4B)},\quad
S_{e+2}=\frac{3-26B+104B^2}{8B^2(1-4B)^2},
\]
\[
S_{e+3}=-\frac{(2D-1)(23D^2-23D+20)}{D^3(D-1)^3},\qquad D=1-4B.
\]

For B=B0, use D(D-1)=-1/36 and 2D-1=-T. This gives **four proved exact special values uniformly in the entire specified prime family**:

\[
\boxed{
S_e(B_0)=2,\quad
S_{e+1}(B_0)=-72T=-48\rho,\quad
S_{e+2}(B_0)=7308,\quad
S_{e+3}(B_0)=-903312T=-602208\rho.}\tag{6}
\]

All integer constants are reduced modulo p; the divisions above are p-units for p>=11. They are a direct evaluation of upper-half moments, **not** an independent evaluation of the lower-half S_1(B0) or R_3347(9).

## Executed exact arithmetic

Executed standard-library Python finite-field checker with k=F_p[rho]/(rho²-2): seven primes 11,19,43,59,67,83,107, direct full-field character enumeration for t=0..3 (28 comparisons), plus independently computed pole-resolvent values at the same 28 moments; all pass. Tested three additional split-root prime fields p=11,19,43 with alpha=2,beta=-3,B=-6 for t=0..5 (18 comparisons); all pass. Root norm and chi signs were checked at each original prime. Separate p=3347 exact field operations use the resolvent, without q=11,202,409-element enumeration:

\[
B_0=(2092,279),\ \alpha=(1066,1977),\ \beta=(2280,1370),
\quad N(\alpha)=3257,\ N(\beta)=2043\pmod{3347},
\]
\[
\boxed{(S_e,S_{e+1},S_{e+2},S_{e+3})
=((2,0),(0,3299),(614,0),(0,252)).}
\]

Pairs denote a+b*rho. The actual executed full script is delivered as d25_gh139_gh140_upper_half_moment_check.py in the portable bundle; terminal lines:
PASS_GH139_ORIGINAL_DIRECT_CHAR_SUM_AND_ROOT_RESOLVENT
PASS_GH139_GENERAL_SPLIT_RESOLVENT
PASS_GH139_P3347_ROOT_NORM_AND_FOUR_UPPER_MOMENTS_NO_Q_ENUMERATION
PASS_GH139_ALL_EXACT.
The all-prime claims follow from the proofs, not sample interpolation.

## BRC and next exact frontier

Carrier (p,k,rho,B0,ordered alpha/beta,root norm/character, omitted-root support, e,t,exact S-value); observer: signed character moment at its exact index; future queries: upper-half moments via (3), with full provenance and root support. This composes GH-128 boundary support and GH-129 notation, and independently proves the root-character signs; it does not automatically lift to native P000 six-dimensional space or an H0/B0 operator.

The smallest scientific uncompleted step is a sourced independent CM/Jacobi/p-adic evaluation of **lower-half** S_1(B0), or the central pair S_837(B0), S_838(B0) at p=3347, sufficient to predict R_3347(9)=0 without circular GH-124/129 reconstruction. The GH-3/GH-83 and native p=373 H0/B0 divided-power, [X]U mod p², semilinear Frobenius, eta and independent review obligations remain. The new upper-half formula is an elementary noncircular consistency anchor, not a replacement for those tests.

**Control observation on 2026-10-30 09:22+08:** Enterprise Math Gateway 0.6.11 returned research_authority_granted=false, executor_binding_configured=false, control_quota.active_jobs=5/5, Source CODE_REVIEW_REQUIRED. Native session/claim/run/recovery ownership and protected staging were not mutated. Support: Enterprise Math #1558 (session/control) and #1559 (native p=373). This GitHub portable record is not a canonical predecessor completed_units field, checkpoint, frozen Result or admitted theorem. Frozen pin and scheduled task settings unchanged.
