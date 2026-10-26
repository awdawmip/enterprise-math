# N=3 exact moment–covariance residual for BRC likelihood-ratio compression

**2026-10-27 · author-level algebraic proof and exact rational evidence.** External finite P/Q stopping-tree model with ordered positive BRC branch masses, not an admitted Source Result, P000/X6/Heartbeat dynamics theorem or external novelty claim.

## Frozen input and scope

GLOBAL_KNOWLEDGE_V1 canonical main \`54a9e0577333015088bff0f71d4ddc006b12e3e5\`; Enterprise Math research input main \`2cbcdaa4bede1c02e3fef657d9fc907a14a5b637\`. Project P000 startup canonical blob \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\` was matched to the original at the frozen global ref. The ACTIVE residual worldview, joint-relation observer preservation, X6/time companion, BRC priority and portable research protocol were read. Predecessors: \`research_notes/brc_n3_predecessor_kernel_rank_tv_20261027_r5/PROOF.md\` and \`research_notes/brc_n3_terminal_lr_moment_dimension_20261027_r5/PROOF.md\`. Their kernel-rank, moment-signature and TV formulae are reused, not redeclared new. Current activity is \`RA-EMR5-20261027-COVMOM-0638\`, with a local (not platform-attested) session identity. Native inventory returned CONTROL_QUOTA; native session creation returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No native owner/CLAIM/Result or independent review was obtained.

Horizon N=3. Each strictly positive finite P/Q edge carries its ordered branch identity. Full strategies observe the ordered history; seedless compressed strategies observe only (t,L=P/Q) and use local behavioral randomization without a persistent lottery seed. At t=0,1,2 stop/decide or continue; at t=3 decide. The four observers are O=(P(decide Q),Q(decide P),E_P tau,E_Q tau). Time is observation count, not native X6 physical time. A signed *difference* of positive laws below is a comparison residual, not signed branch mass.

## Exact theorem for a mixture of existing seedless strategies

Let pi_s be a finite family of seedless policies with mixture weights lambda_s>=0 summing to 1. At a time-2 exact-LR state r let b_s be its uncontrolled Q arrival mass, z_s the continue probability, and K_s(y) the Q distribution of final LR Y **conditional on continuing**, before applying z_s. By P/Q conservation, each K_s has mass 1 and mean r. If b=sum_s lambda_s b_s>0, set alpha_s=lambda_s b_s/b.

Construct the standard single seedless averaged-flow policy by averaging Q occupation/action masses at the root and time 1, normalizing each action mass by average incoming mass, and similarly at time 2. Because time-1 actions are constant within each predecessor LR fiber, the resulting time-2 kernel is Kbar=sum_s alpha_s K_s, and its continuation rate is zbar=sum_s alpha_s z_s. This exact procedure preserves the two time expectations, since P action mass at LR r is r times Q action mass.

The desired terminal Q arrival measure of the mixed policies and the actual measure of the single policy are respectively

    U_mix(y)=b sum_s alpha_s z_s K_s(y),
    U_bar(y)=b (sum_s alpha_s z_s)(sum_s alpha_s K_s(y)).

For the signed arrival-flow residual D=U_bar-U_mix, define Cov_alpha(X,Z)=E_alpha(XZ)-E_alpha X E_alpha Z. Then

    D(y)=-b Cov_alpha(z_s,K_s(y)).                               (1)

Let the distinct final LR support be y_1<...<y_m, with absent outcomes represented by zero kernel mass. Let M_k(s)=sum_j y_j^k K_s(y_j), and C_k=Cov_alpha(z_s,M_k(s)). Define Lagrange polynomials

    l_j(X)=prod_{i!=j}(X-y_i)/(y_j-y_i)
          =sum_{k=0}^{m-1} l_{j,k} X^k.

The following are exact for all real behavioral action probabilities:

    D(y_j)=-b sum_{k=2}^{m-1} l_{j,k} C_k.                       (2)
    D==0   iff   C_2=...=C_{m-1}=0.                             (3)

**Proof.** The moment of order k of (1) is -b Cov_alpha(z_s,M_k(s)). Every M_0(s)=1 and M_1(s)=r, so these two covariance coordinates are zero. By the Lagrange Kronecker property, D(y_j)=sum_i l_j(y_i)D(y_i). Expanding l_j in powers and inserting the moment identity yields (2). If the C_k vanish then D=0. Conversely D=0 makes all moments, hence every C_k, vanish. Distinct y_j ensure the Lagrange polynomials exist. No finite experiment or regularity beyond the stated finite model is used.

### Ternary support

For m=3, put gaps g1=y_2-y_1, g2=y_3-y_2. As the degree-two coefficients of l_j are the inverse Vandermonde denominators,

    TV(D):=(1/2)sum_j|D(y_j)|=b |C_2|/(g1*g2).                   (4)

Here M_2(s)=r^2+Var_{K_s}Y, so **one continuation/conditional-variance covariance** exactly determines whether this aggregation creates a terminal-law residual. Cauchy-Schwarz and Var(z)<=1/4, Var(M_2)<=range(M_2)^2/4 give |C_2|<=range(M_2)/4. Equation (4) recovers the predecessor's b*Delta_r/4 estimate. Two equally weighted extreme kernels and z=(1,0) attain the covariance bound. This is a construction-specific terminal-flow statement, not minimal distance to every compressed policy.

### Four terminal LR values

For m=4 let S=sum_j y_j and d_j=prod_{i!=j}(y_j-y_i). The degree-three Lagrange coefficients obey l_{j,3}=1/d_j and l_{j,2}=-(S-y_j)/d_j, giving

    D(y_j)=b ((S-y_j)C_2-C_3)/d_j,
    TV(D)=(b/2)sum_j |(S-y_j)C_2-C_3|/|d_j|.                   (5)

Thus C_2=0 does not imply D=0: the third-moment covariance is an independent, essential residual coordinate. In general the full exact residual has at most m-2 moment-covariance coordinates.

## Reachable 12-leaf strict-positive rational witness

Reuse the verified 12-leaf tree: Q(root->a,b)=(1/3,2/3), P=(2/3,1/3); conditional Q/P a->x,y=(1/2,1/2)/(1/4,3/4), b->x,y=(2/3,1/3)/(1/3,2/3). Thus L2(ax)=L2(by)=1; L2(ay)=3, L2(bx)=1/4. From ax,by take Y=(1/2,3/4,5/4,3/2), with Q kernels Ka=(3,6,2,5)/16, Kb=(5,2,6,3)/16 and P conditional probabilities Y*K. At ay/bx append two P=Q=(1/2,1/2) terminal outcomes. Every edge and all 12 leaves have strictly positive P/Q mass, and each P/Q conditional law normalizes.

The kernels have equal E(Y^2)=37/32 and third-moment difference E_Ka(Y^3)-E_Kb(Y^3)=3/128 (previously established inputs).

Seedless policy A: root continue, at a continue, at b stop/decide P, at time2 LR=1 continue, elsewhere stop/decide P. Policy B: root continue, at a stop/decide P, at b continue with probability 3/4, at time2 LR=1 stop, elsewhere stop/decide P. Terminal decision: decide Q exactly when LR=1/2 or 5/4, otherwise P. Mix A/B equally. Its averaged-flow seedless strategy C continues at a with 1/2, b with 3/8, LR2=1 with 1/2, with the same terminal decisions.

At r=1: b=1/6, alpha=(1/2,1/2), z=(1,0), C_2=0, C_3=3/512. Equation (5) yields

    D=(1/192,-1/96,1/96,-1/192); TV(D)=1/64.

Direct exact P/Q policy mass summation gives

    O(A)=(1/24,91/96,11/6,3/2)
    O(B)=(0,1,5/4,3/2)
    midpoint=(1/48,187/192,37/24,3/2)
    O(C)=(7/192,23/24,37/24,3/2)
    O(C)-midpoint=(1/64,-1/64,0,0).                           (6)

The two time observers match exactly. By selecting terminal decide-Q on the positive entries of D, the |Q-error change| attains TV(D)=1/64. Therefore even *zero variance covariance* need not make this exact averaging construction safe on four support points. **This does not establish** that the midpoint is absent from the entire seedless strategy image, its nonconvexity, or the still-open equal-convex-hulls/unequal-images conjecture.

## Validation and remaining question

The actually executed Python standard-library Fraction verifier checks ternary covariance/TV, four-point moments/covariances/Lagrange reconstruction, the complete rational 12-leaf probabilities and four observers, and a five-point independent moment inversion. The finite checks verify the explicit examples; general scope follows from the algebra above. No all-real QE/CAD or independent Driver proof review was performed.

Next: use C_2 as the exact ternary construction-residual coordinate, but do **not** confuse its vanishing with global image membership. For a candidate with distinct predecessor ternary kernels, first prove/refute full-deterministic policy vector containment in the convex hull of seedless deterministic policy vectors using exact rational LP; only if the hulls match test a rational full vector against the **all-real** seedless polynomial image by elimination. See NEXT_TASK.md.