# R5: one quadratic scalar gate for the nonlumpable four-observer image

Date: 2026-11-06 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Source and mother question
R5 seeks a strictly positive finite P/Q stopping tree with equal four-observer FULL_HIST and seedless LR convex hulls but different real-behavior images. Freeze GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. This is an auxiliary P/Q likelihood-ratio/BRC observer, not native X6 dynamics. Reuse the particular δ=1/4 tree and earlier six-variable quadratic-zonotope criterion (EM f00bca43d2c668e4bf05ff7974db140c9e0d2adf) and author-side hull equality certificate (EM fed51a882c12831a889cd5437da5d1dc564fd673). The hull certificate is inherited, not rerun this turn.

At time 2: q2=(1/2,1/2), r2=(3/4,5/4). At time 3: q3[0]=(13/20,1/5,3/20), q3[1]=(1/40,9/20,21/40), r3=(1/2,1,3/2). At time 4: r4=(1/10,1,19/10); q4[i,0]=(509,382,9)/900 and q4[i,2]=(9,382,509)/900 regardless of i; q4[0,1]=(47/180,43/90,47/180), q4[1,1]=(67/162,14/81,67/162). All rows are strictly positive, stochastic, and have their child's LR mean equal to the parent's LR. Every stop key has unrestricted P/Q declarations.

## Theorem A: FULL is a rational polytope projection
Let g be root continuation and u_i=g*a_i be products for time-2 continuation. Set b_ij=q2[i]*q3[i,j]*u_i, V_j=b_0j+b_1j; for FULL choose independent history-conditioned time-3 continuations z_ij and set x_ij=b_ij*z_ij, X_j=x_0j+x_1j. The linear bounds are 0<=u_i<=g<=1, 0<=X_j<=V_j.

Only the history split at j=1 changes terminal ratio aggregates because q4[i,0] and q4[i,2] are independent of i. Define A=b_01=u_0/10; B=b_11=9u_1/40; alpha=47/180; beta=67/162; d=beta-alpha=247/1620>0; J=alpha*x_01+beta*x_11. The exact *four linear* central-split restrictions are

    max(alpha*X_1, beta*X_1-d*A) <= J <= min(beta*X_1, alpha*X_1+d*B).

Sufficiency: recover x_01=(beta*X_1-J)/d, x_11=X_1-x_01, yielding 0<=x_01<=A and 0<=x_11<=B. For j=0,2 take x_ij=b_ij*X_j/V_j if V_j>0, otherwise zero. Thus any linear-feasible (g,u,X,J) is a genuine FULL continuation, including zero-mass boundaries.

Let R={1/10,1/2,3/4,1,5/4,3/2,19/10}; aggregated Q stop-ratio masses M_r are *affine* in seven variables v=(g,u_0,u_1,X_0,X_1,X_2,J). Initialize M_r=0; add 1-g at r=1, add (g-u_i)/2 at r=r2[i], add V_j-X_j at r=r3[j], and finally add

    M_{1/10} += (509 X_0+9 X_2)/900 + J
    M_1 += 382(X_0+X_2)/900 + X_1-2 J
    M_{19/10} += (9 X_0+509 X_2)/900 + J.

Flow construction gives M_r>=0, sum M_r=1, sum r*M_r=1. Stopping time coordinates are affine:

    T_Q=1+g+(u_0+u_1)/2+X_0+X_1+X_2;
    T_P=1+g+(3u_0+5u_1)/8+X_0/2+X_1+3X_2/2.

For every r introduce ell_r = Q stopped mass declaring P, with 0<=ell_r<=M_r. Then e_Q=sum ell_r and e_P=1-sum r*ell_r. Every FULL declaration aggregate is captured, and every aggregate is realized by declaring P with common conditional probability ell_r/M_r on stopped histories of ratio r (arbitrary if M_r=0). Hence O4(FULL_HIST) is exactly a linear projection of a bounded rational polytope with seven v and seven ell variables.

## Theorem B: LR adds precisely ONE quadratic equality
Common seedless time/ratio continuation z_j requires x_ij=b_ij*z_j. For j=0,2 use common z_j=X_j/V_j whenever V_j>0; they preserve the terminal aggregate because their q4 rows are i-independent. At j=1, common z_1=X_1/(A+B) (if positive) is compatible with J iff

    F(v) := (A+B)*J - X_1*(alpha*A+beta*B) = 0.

This is *one* rational quadratic equality. It is necessary from any LR policy, sufficient for reconstructing a legal LR policy with identical aggregate stop masses and labels, and remains valid at A+B=0 because X_1=J=0 there. The full LR image is thus exactly the same 14-variable rational linear lift with only F=0 added. This is an alternative to the older six-variable/14-quadratic-inequality formulation; no complexity speedup is asserted without an algorithmic comparison.

## Theorem C: every fixed target reduces to two extrema on a rational polytope
Fix W=(e_P,e_Q,T_P,T_Q). Eliminate ell using the exact planar seven-ratio zonotope inequalities (previously proved for all real declarations, including degenerate masses):

    L_rho(v) <= e_P+rho*e_Q <= U_rho(v)  for every rho in R,
    L_rho(v)=1+sum_{r>rho}(rho-r)*M_r(v),
    U_rho(v)=1+sum_{r<rho}(rho-r)*M_r(v).

Because the M_r are affine, these 14 inequalities are linear in v. Let K(W) be the bounded rational polytope defined by these inequalities, the two time equalities, the bounds on g,u,X, and the four central J inequalities. Then exactly

    W in O4(FULL_HIST) <=> K(W) is nonempty,
    W in O4(seedless LR) <=> there exists v in K(W) with F(v)=0.

For nonempty K(W), convexity and compactness imply F(K(W)) is a closed interval, hence

    W in O4(seedless LR) <=> min_{K(W)} F <= 0 <= max_{K(W)} F.

Two feasible opposite-sign v give a constructive LR witness by interpolation along their segment: F is quadratic along it and must have a real root. A strict one-sided global certificate for F over K(W) is a complete all-real LR-unattainability certificate. An appropriate rational W in inherited hull H with such certificate would solve the missing actual-image-difference half conditional on earlier hull equality; no such certificate is claimed here.

## Theorem D: one-dimensional information defect and sharp pooling bound
For arbitrary FULL central history-continuations z_01,z_11, pooling them to z_1=X_1/(A+B), when A+B>0, changes the central coefficient by the exact factorization

    epsilon = J-J_LR = d*A*B/(A+B)*(z_11-z_01).

The aggregated stop-ratio masses differ only by (epsilon,-2epsilon,epsilon) at ratios (1/10,1,19/10); both time coordinates are identical. Since A<=1/10 and B<=9/40, the increasing harmonic expression AB/(A+B) is <=9/130. Thus

    |epsilon| <= d*9/130 = 247/23400 = 19/1800.

Reuse the same ratio-dependent declaration probabilities under FULL and the pooled LR profile. Each error coordinate changes in magnitude by at most 2|epsilon|, so every FULL observation has a genuine LR observation with identical stopping time coordinates and four-dimensional L-infinity distance <=19/900. The scalar and this *pooling comparison* error bound are attained for g=u_0=u_1=1, z_01=0,z_11=1 and declarations that choose P at ratios 1/10 and 19/10 and Q at ratio 1. This does **not** prove different actual image sets or a lower bound on the distance to the entire LR image. If alpha=beta, this history defect vanishes and actual image equality follows in this topology.

## Evidence and open dependency
A Python standard-library Fraction checker executed: positivity/normalization/LR martingale moments; direct six-history terminal masses vs affine lift; 600 seeded rational FULL profiles including boundaries; 360 reverse reconstructions of all four J bounds; exact factorization, seven-ratio zonotope halfspaces; sharp pooling error example. PASS_EXACT_R5_SCALAR_NONLUMPABILITY_LIFT. The universal claims above have independent analytic proofs; finite checks are model-specific safeguards. No independent Driver review, formal Result, Source task CLAIM or admission is asserted.

Next: for rational W in the inherited 80-halfspace hull H, assemble K(W) via exact linear constraints and certify min/max of the **single quadratic** F over K(W), with all boundary cases. Either strict sign on all K(W) proves a real-image gap for this model or a proof of sign crossing for all W in H proves its actual image equality.