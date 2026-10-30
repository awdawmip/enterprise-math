# BRC N=4 — exact joint-deficiency factorization and marginal inversion

2026-10-30. AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED. This is a theorem in the frozen external finite P/Q positive-weight BRC observer model, not a native X6 or physical-heartbeat statement. It extends the noisy fixed-G4 theorem in PR #1738, commit c2ac4b7d0a3bd2a70620d1fa793c21dd51ce191e.

## Frozen source and lawful operations

For s=AU,AV,BU,BV, j,k in {0,1}, set Q(s,j,k)=q_s/4 and P(s,j,k)=q_s r_sj/4. In source order q=(1/6,1/3,1/4,1/4), r_AU=(9/10,11/10), r_AV=(1/4,1/4), r_BU=(1/5,9/5), r_BV=(2,2). All 16 masses are strictly positive under both normalized laws. BU mass is 1/4 under both; conditional BU branch prior P(j=0)=p=1/10 and Q(j=0)=1/2, while k|BU,j is fair under both.

AV/BV stop at T2 with Q and AU stops at T3 with P. In BU, the third-stage j=0 daughter continues to T4 at rate u; j=1 at rate v. Otherwise it stops T3,Q. Upon T4 the already-sampled k is read and a terminal P decision is selected with rate d_jk (Q otherwise). Parameters u,v,d00,d01,d10,d11 lie in [0,1]. This is lawful behavioral S2 and writes no physical k; S23 additionally enforces d_j0=d_j1 on reachable daughters. The BU terminal alphabet Y is B3,B4P0,B4Q0,B4P1,B4Q1. Let F_j be the law of Y given BU,j:

F_j(B3)=1-u_j, F_j(B4Pk)=u_j*d_jk/2, F_j(B4Qk)=u_j*(1-d_jk)/2, u_0=u, u_1=v.

The old compressed C is E,A,B with P_C=Q_C=(7/12,1/6,1/4). On BU, an auxiliary shared source sensor Z=j XOR N uses independent Bernoulli(eps), 0<=eps<=1/2; outside BU Z=NA. A decoder observes (C,Z), uses the same output kernel under P and Q, and must preserve (C,Z) for JOINT fidelity. MARGINAL fidelity checks only (C,Y), discarding Z in the resulting output.

Put D=TV(F_0,F_1). Direct aggregation yields

$$ D={2|u-v|+\sum_{k=0}^1(|v d_{1k}-u d_{0k}|+|v(1-d_{1k})-u(1-d_{0k})|)\over4}, $$

and TV(P_(C,Y),Q_(C,Y))=D/10. The actual j is a sufficient generated-distribution state because F_j is shared across laws, but cannot reconstruct authentic k without the recorded path.

## New theorem 1 — universal finite-outcome factorization for FULL JOINT fidelity

Suppose binary latent J has two possibly different priors, a common finite sensor W(z|j), and common finite future output kernels F_0,F_1. The two-law minimax total variation radius for reconstructing (Z,Y) from Z under a shared decoder equals D=TV(F_0,F_1) times the radius obtained by replacing F_0,F_1 with disjoint point masses delta_0,delta_1. This holds with overlapping F_j, and with zero-mass sensor atoms ignored.

Proof: For D>0 choose the finite Hahn event A satisfying F_0(A)-F_1(A)=D. For any common decoder K_z put theta_z=clip((K_z(A)-F_1(A))/D,0,1). Every target conditional distribution given z has the form F_t=tF_0+(1-t)F_1 with t in [0,1]. Event A gives

$$TV(F_t,K_z)\ge |F_t(A)-K_z(A)|\ge D|t-\theta_z|.$$

Replacing K_z by F_(theta_z) makes the loss exactly D|t-theta_z| for every t, since TV is homogeneous on this line segment. The replacement weakly improves both laws simultaneously, separately for every z. Thus the entire joint minimax problem reduces exactly to scalar theta_z in [0,1], with objective multiplied by D. When D=0 the decoder F_0 is exact. QED.

This argument does NOT establish the analogous factorization for a marginal-only loss: conditional outputs K_z may be valid probabilities outside the convex segment [F_0,F_1], and after Z is discarded their contributions can cancel.

## New theorem 2 — exact attained all-real JOINT minimax radius for every S2/S23 policy

For the symmetric binary sensor write a=p+(1-2p)eps, b=1-a, p=1/10. A scalar decoder sets alpha=theta_0,beta=theta_1. The BU-conditional joint losses under P and Q satisfy

$$e_P\ge |a\alpha-p(1-\epsilon)|+|b\beta-p\epsilon|,$$
$$e_Q\ge (|\alpha-(1-\epsilon)|+|\beta-\epsilon|)/2.$$

Putting E=max(e_P,e_Q), combine the inequalities with positive multipliers 1 and 2a:

$$E\ge {e_P+2ae_Q\over1+2a}
\ge {a-p(1-\epsilon)-a\beta+|b\beta-p\epsilon|\over1+2a}.$$

For 0<=eps<=1/2 we have a<=b. The numerator is minimized over all beta in [0,1] at beta*=p eps/b; the bound becomes

$$E\ge e_*={(1-2p)\epsilon(1-\epsilon)\over b(1+2a)}.$$

Take beta*=p eps/b and alpha*=1-beta*-2e*. Both are in [0,1] throughout; the exact identities alpha*-p(1-eps)/a=e*/a and 1-eps-alpha*=(1-2p)^2 eps(1-eps)(1-2eps)/[b(1+2a)] provide sign certificates, and beta*<=eps. These choices make e_P=e_Q=e*. On BU, output the mixture theta_z F_0+(1-theta_z)F_1; on E/A recover exactly. Multiplying by P(BU)=Q(BU)=1/4 and using theorem 1 proves the **attained, all-real** formula:

$$\boxed{R_{\rm joint}(\epsilon;u,v,d)=D\,{5\epsilon(1-\epsilon)\over(9-8\epsilon)(3+4\epsilon)}.}$$

The old G4 case was D=1. For 0<eps<=1/2 the coefficient is positive. Thus joint zero deficiency is equivalent to F_0=F_1, namely u=v and [u=0 or (d00=d10 and d01=d11)]. Within S23 at nonzero u this is simply u=v and d0=d1. At eps=0 the sensor reveals j and all policies have zero deficiency.

## New theorem 3 — exact ZERO criterion for MARGINAL-ONLY fidelity

The same decoder can see Z but only (C,Y) is checked. Write K_0,K_1 for its full BU output distributions. They must satisfy simultaneously

$$a K_0+(1-a)K_1=pF_0+(1-p)F_1,\qquad (K_0+K_1)/2=(F_0+F_1)/2.$$

For 0<=eps<1/2 and p!=1/2 these linear equations have the unique solution

$$\boxed{K_0={(1-\epsilon)F_0-\epsilon F_1\over1-2\epsilon},
\quad K_1={(1-\epsilon)F_1-\epsilon F_0\over1-2\epsilon}.}$$

Mass normalization is automatic. They are probability distributions if and only if **for every y**

$$(1-\epsilon)F_0(y)\ge\epsilon F_1(y),\qquad
(1-\epsilon)F_1(y)\ge\epsilon F_0(y).$$

These coordinate inequalities are therefore necessary and sufficient for exact P/Q-common marginal reconstruction. At eps=1/2, Z has the same law under both sources, so zero marginal error is equivalent to F_0=F_1. In particular the fixed-G4 marginal radius eps/(6+8eps) applies only to its disjoint-support F_j and must NOT be multiplied by D for a general future kernel.

## New exact S23 witness — marginal radius ZERO but joint radius strictly positive

Take eps=1/4, u=1/4, v=3/4, and d00=d01=d10=d11=0 (all terminal Q). This meets S23's equal-likelihood daughter rule. On (B3,B4Q0,B4Q1) we have F_0=(3/4,1/8,1/8), F_1=(1/4,3/8,3/8), D=1/2. The uniquely inverted K_0=(1,0,0), K_1=(0,1/2,1/2) are both valid probability distributions, hence exact marginal minimax error is zero. However the universally sharp full-joint radius is

$$\boxed{R_{\rm joint}=(1/2)(15/448)=15/896>0.}$$

Strikingly this witness also has TV(P_(C,Z,Y),Q_(C,Z,Y))=TV(P_(C,Z),Q_(C,Z))=1/20. Equality of ONE binary discrimination TV statistic after compression does not imply stochastic reconstructibility of the full joint experiment.

The full between-law joint TV depends on more than D. In general it equals

$$ {1\over20}\sum_y\bigl(|\epsilon F_1(y)-(1-\epsilon)F_0(y)|
+|(1-\epsilon)F_1(y)-\epsilon F_0(y)|\bigr).$$

The other lawful S23 profile u=0,v=1/2, all d_jk=0, has the SAME D=1/2 but full between-law joint TV=1/16 at eps=1/4. Both profiles have the same sharp joint reconstruction radius 15/896, despite different total variation between the P/Q joint experiments.

## Verification, typing, and provenance

The actual attached Python Fraction verifier constructs the 16 strictly positive normalized P/Q leaves, pushes forward 750 rational profile/sensor combinations, and checks the joint optimal decoder, signed-law formulas, S23 marginal-zero witness, and same-D contrast. RUN_EVIDENCE.txt is captured program stdout. The all-real statements are supplied by the Hahn projection, dual inequalities and exact linear inversion, not extrapolated from those finite tests. The external positive-weight observer results do not establish signed/phase cancellation or P000 native physical residuals.

Locked P000 remains six native spatial axes and separately typed time, with a three-dimensional layer (not a native two-dimensional plane). A native Cell/slice/time observer-and-future-operation bridge remains unproved. Authored by this ChatGPT research turn using GitHub principal awdawmip; independent Driver review, native CLAIM and Result are not asserted. A bounded native owner query returned CONTROL_QUOTA; Site research_authority_granted=false.

Read pins: GLOBAL_KNOWLEDGE_V1 main@bf1a9f60d357fc3f87da751eeb170fc58c651d79; enterprise-math main@f05844fa7a1ed5fa3e75fc98eecd757949bcb3f2; preceding PR #1738 head@c2ac4b7d0a3bd2a70620d1fa793c21dd51ce191e.