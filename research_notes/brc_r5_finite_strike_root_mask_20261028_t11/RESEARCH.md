# R5 | Finite-strike kernel tomography and an unrestricted signed-support certificate

2026-10-28 Asia/Shanghai. Local Researcher-ID: EM-R005-KS6E2B. Source snapshot: GLOBAL_KNOWLEDGE_V1 main@2d20804f76d412bcba30cde6485f866709504af3; Enterprise Math main@af31973123ca639af956eb4d59608c2a6b75e7e8. Direct predecessor: research_notes/brc_r5_predictive_lumpability_20261028_t11/RESEARCH.md. Claim: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. This is a finite EXTERNAL two-measure sequential decision tree, not a physical native heartbeat-X6 propagation law. P000 is unchanged: native six-dimensional discrete X6 plus separately typed time. BRC use here is typed positive rational path-mass multiplication, branch summation and preservation of AU/AV/BU/BV provenance; signed coefficients are confined to the four-observable evaluation.

## Theorem A — finite-strike tomography

At a common nonterminal time/likelihood-ratio signature (t,r), two hidden histories A,B have conditional Q predictive distributions K_h on the finite union support 0<y_1<...<y_m, with total mass one and Q expectation r. Let p_hj=K_h(y_j), and write

G_h(k)=min(r,k)-sum_j p_hj min(y_j,k),
C_h(k)=sum_j p_hj (y_j-k)_+,
G_h(k)=C_h(k)-(r-k)_+, for k>0.

Concavity of min(y,k) gives G_h(k)>=0. At the support endpoints C_h(y_1)=r-y_1 and C_h(y_m)=0. Each interval slope is

s_hj=[C_h(y_{j+1})-C_h(y_j)]/(y_{j+1}-y_j)=-sum_{i>j}p_hi.

Writing T_hj=-s_hj recovers every probability exactly: p_h1=1-T_h1, p_hj=T_h,j-1-T_hj for 2<=j<m, and p_hm=T_h,m-1. Therefore

K_A=K_B if and only if G_A(y_j)=G_B(y_j) for all 2<=j<=m-1.

For m<=2 the moment and normalization equations uniquely determine the kernel. Distinct finite rational kernels with the same mean always have a rational strike k with G_A(k)!=G_B(k); continuity permits choosing k unequal to r and to each support point, avoiding decision-price ties. Only m-2 interior exact rational strike checks are needed. This is a finite stop-loss/call-payoff distribution-recovery identity, not a claim of novelty for the general option-recovery principle.

## Theorem B — exact conditional regret witness

At a single collided signature assume two already-arrived hidden histories have positive absolute Q weights w_A,w_B and one more observation followed by terminal P/Q declaration. Fix the same output O=(e_P,e_Q,E_P tau,E_Q tau) and minimize the four-dimensional signed objective J=e_P+k e_Q+s E_Q tau. For either hidden history h, declaring P/Q immediately costs min(r,k)+t*s per unit Q, whereas continuing costs E_Q min(Y,k)+(t+1)*s. Its continue advantage is G_h(k)-s.

With W=w_A+w_B, the full-history benefit over immediate stopping is B_full(s)=w_A(G_A-s)_+ +w_B(G_B-s)_+. The seedless LR policy must choose one common action; its benefit is B_LR(s)=[w_A(G_A-s)+w_B(G_B-s)]_+. Thus

Delta_cond(s)=B_full(s)-B_LR(s)>=0.

At the exact rational price s*=[w_A G_A+w_B G_B]/W, one gets

Delta_cond(s*)=(w_A w_B/W)*abs(G_A-G_B).

This is the maximum over real s, by the three affine intervals separated by G_A,G_B,s*. Kernel inequality therefore implies a strictly positive CONDITIONAL value witness. This does NOT by itself imply a full-tree separation when earlier voluntary stopping is available.

## New eight-leaf strictly positive rational tree

At t=1, Q(A)=Q(B)=1/2, cumulative likelihood ratios R(A)=1/2, R(B)=3/2. At t=2, the absolute Q weights and R are AU:(1/6,1), AV:(1/3,1/4), BU:(1/4,1), BV:(1/4,2). The t=3 R support for AU and BU is Y=(1/2,1,3/2), with different Q conditional kernels:

K_A=(1/4,1/2,1/4), K_B=(1/8,3/4,1/8).

AV has one terminal at R=1/4 and BV one terminal at R=2. The eight full Q/P leaves, in order AU0,AU1,AU2,AV0,BU0,BU1,BU2,BV0, are:

Q=(1/24,1/12,1/24,1/3,1/32,3/16,1/32,1/4);
P=(1/48,1/12,1/16,1/12,1/64,3/16,3/64,1/2).

Every mass is strictly positive, and both P and Q sums are one. At the collision AU/BU both R=1 but K_A!=K_B. G_A(1)=1/8 versus G_B(1)=1/16. Choose a tie-free strike k=9/10: G_A=1/10 and G_B=1/20; w_A=1/6,w_B=1/4 give s*=7/100 and Delta_cond=1/200.

### Early-stop masking on the positive direction

For lambda_+=(1,9/10,0,7/100), the full and seedless LR GLOBAL minimum both equal 77/100. An optimal policy stops at t=1 in both roots, declaring Q at A and P at B, giving O=(1/4,1/2,1,1). Under the optimal continuations the Q-conditional costs at the roots would be A=179/300 > 57/100 and B=26/25 > 97/100. Hence the strictly positive local conditional deficit 1/200 is completely masked at this direction. A nonzero predictive residual and a local decision conflict alone are NOT global signed-support certificates.

### Removing the mask — exact all-real-policies separation

Take the signed direction lambda*=(406,489,35,-14); the time slope at LR value r is c(r)=35r-14. In each t=2 history, the per-unit-Q costs for (stop declaring P; stop declaring Q; continue then optimally declare at t=3) are:

AU: (531,448,439);
BU: (531,448,454);
AV: (957/2,91,343/4);
BV: (601,924,657).

The full-history optimal actions are AU=C, BU=Q, AV=C, BV=P. At t=1 the minimum direct stop costs in roots A/B are respectively 413/2 and 1055/2; their full-history continuation costs are 407/2 and 1049/2. Both roots optimally continue, each has Q mass 1/2, and

V_full(lambda*)=(407/2+1049/2)/2=364.

The LR policy must use the SAME action at t=2 on AU and BU. Exact Bellman optimization over their three common choices, with all root early stops and AV/BV independent choices permitted, gives:

common C: root A 407/2, root B 1055/2, aggregate 731/2;
common Q: root A 413/2, root B 1049/2, aggregate 731/2;
common P: root A 413/2, root B 1055/2, aggregate 367.

Therefore V_LR(lambda*)=731/2 and the gap is exactly 3/2>0.

A full-history pure-strategy witness reaches

O*=(7/16,7/24,9/4,5/2), lambda* dot O*=364.

An explicit witness: at t=1 both roots continue; AU continues and at its three leaves declares Q,Q,P; AV continues and declares Q; BU stops at t=2 declaring Q; BV stops at t=2 declaring P. Every seedless LR strategy must satisfy the global exact supporting inequality

406 e_P + 489 e_Q + 35 E_P tau -14 E_Q tau >= 731/2,

strictly violated by O*. Thus O* is not in conv(O_LR), the two strategy convex hulls differ, and THIS eight-leaf model is excluded from the desired equal-hull/non-equal-image counterexample class.

The result covers ALL REAL LOCAL BEHAVIOR RANDOMIZATIONS, not just the enumerated rational ones: each time-indexed LR signature is visited at most once per trajectory, so total expected loss is multi-affine in the local action-simplex variables. Minimizing successively over each simplex pushes a minimizer to a deterministic vertex without increasing loss. Complete finite deterministic Bellman minimization proves the all-real infimum. The same holds for full history. Since 0<=e_P,e_Q<=1 and 1<=T_P,T_Q<=3, the full-versus-LR support gap is 16-Lipschitz in the infinity norm of lambda. In particular ||lambda-lambda*||_infty<3/32 also separates strictly.

## Verification and limits

Executed local Python stdlib fractions.Fraction checks: eight strictly positive P/Q leaves, normalization and conditional LR martingale means; exact finite-strike kernel recovery; two objectives; and 1764 complete-history effective pure descriptions versus 7776 seedless LR descriptions (including all terminal declaration signatures). Exact results: 77/100=77/100 on lambda_+; 364 versus 731/2 and gap 3/2 on lambda*. The full witness was recomputed. Standalone Bellman verification provides an independent short checker. Discovery through a floating Qhull facet candidate was ONLY exploratory and is not used as mathematical evidence. No Lean checker, native Source CLAIM/Result or independent Driver review has been obtained.

External literature provenance only (metadata verified, full text not independently checked): Douglas T. Breeden and Robert H. Litzenberger, Prices of State-contingent Claims Implicit in Option Prices, Journal of Business 51(4), 621-651 (October 1978), DOI https://doi.org/10.1086/296025. The classic distribution recovery concept is acknowledged; our specialized double-measure, root-mask and rational signed Bellman certificates do not claim general-principle priority.

## Next independent question

For a finite N=3 tree with one collided t=2 signature, derive and certify exact rational polyhedral regions of lambda=(a,b,u,v) in which a local kernel-strike discrepancy survives all t=1 root stopping options. Reuse the existing masked-regret formula rather than inventing a second runtime or proving the same kernel sufficiency lemma. Separate individual-direction masking from all-direction hull equality. A genuine mother-target candidate must satisfy the ALL-SIGNED-DIRECTIONS hull-equality gate before an all-real LR-image nonconvexity claim. Maintain frozen P000/native-X6 semantic boundary and author/reviewer independence.

Activity pointer: research_activity_records/RA-EMR5-20261028-0238-KSTRIKE-6E2B.json (local session identity only). No claim of official task ownership, mathematical admission, or registered native execution.
