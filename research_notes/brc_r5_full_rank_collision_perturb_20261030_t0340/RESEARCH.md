# Enterprise Math R5 — full-rank collision perturbations destroy convex-hull equality

2026-10-30, Asia/Shanghai. Author-side mathematical result: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is not a Source CLAIM, Result, Driver review, accepted theorem, native X6 transfer or external physics statement.

Frozen canonical inputs: GLOBAL_KNOWLEDGE_V1 main@97e477277dd758864016a00f047f282cb085572e; enterprise-math main@bb580b9159a1b170964b7c030c909c37a6f78106. Exact mathematical predecessor is research_notes/brc_r5_double_collision_winding_20261030_t0235/RESEARCH.md at commit 90ba9f691be661d8dea73d24cb2776ec6eda989b. P000 / ACTIVE residual-faithful worldview remain unchanged. This is a finite two-probability stopping model; BRC-like positive path masses retain source labels but do not instantiate native BRC-Shor arithmetic.

## Exact question and result

The predecessor proved equality of FULL and seedless exact-LR *actual real* four-observer images in a strictly positive, nonfrozen, doubly colliding nature tree, but the common image had only rank-two affine span. We now change only terminal Bernoulli error kernels by arbitrarily small rational source-opposed increments. **Both observer convex hulls become full affine rank four, yet the hulls differ strictly.** Thus a genuinely four-dimensional perturbed candidate is excluded by an exact signed support certificate, without attempting to infer real-image nonmembership from vertex counts.

## Full model and two exact collisions

At time 1, P(A)=1/3,P(B)=2/3 and Q(A)=2/3,Q(B)=1/3. At time 2, nature draws binary Y with (P(Y=1),Q(Y=1)) conditional on A = (1/2,1/4), conditional on B = (1/4,1/2). At time 3, nature draws binary Z with (P(Z=1),Q(Z=1)) at prefixes A1 = (1/2,1/4), B1 = (2/3,1/3), A0 = (1/2,2/5), B0 = (1/2,3/5). All complementary probabilities are strictly positive. Decisions to stop are made at t=1,2,3; t=4 is forced stop. There is no new observation at t=4.

For each full prefix h, L(h)=P(h)/Q(h)>0. Explicit source-labeled cylinder masses give P(A1)=Q(A1)=P(B1)=Q(B1)=1/6 and L(A1)=L(B1)=1 at time 2. At time 3, P(A11)=1/12,Q(A11)=1/24 and P(B11)=1/9,Q(B11)=1/18, so L(A11)=L(B11)=2. These two collisions survive every modification below, and the source-specific transition kernels are genuinely different.

FULL chooses separate real hazards for 14 full prefix decision keys. Seedless LR has 12 (time,L) decision keys and cannot distinguish A1 from B1 or A11 from B11. No persistent cross-time random seed is allowed. The four observer coordinates are O=(e_P,e_Q,T_P,T_Q), with two law-specific error probabilities and expected stop times.

At a stopped cylinder (t,h), the original exact-gauge Bernoulli rates are

p0(t,h) = 1/5 + t/20 + (t+1)/(100 L(h));
q0(t,h) = 2/5 - t/30 + (t+2)L(h)/200.

The stopped-cylinder change-of-measure identity P(h)=L(h)Q(h) gives, for **all real** FULL or seedless-LR policies,

e_P^0 = 21/100 + T_P/20 + T_Q/100,
e_Q^0 = 41/100 + T_P/200 - T_Q/30.

Define perturbed rates by changing ONLY

p(2,A1)=p0(2,A1)+eps,  p(2,B1)=p0(2,B1)-eps;
q(3,A11)=q0(3,A11)+eta, q(3,B11)=q0(3,B11)-eta;

and keep all other p/q equal to their baseline values. For 0<eps<33/100 and 0<|eta|<7/20 these are all valid strictly positive Bernoulli rates: p0 on A1/B1 at t2 is 33/100, q0 on A11/B11 at t3 is 7/20, and other baseline rates were already in (0,1). The executed exact instance sets eps=eta=1/1000.

## Sharp all-real theorem: exact residual and time-loss bounds

Write alpha,beta for the probability of continuing after root A,B, and a,b for conditional probabilities of stopping at A1,B1 at time 2. In FULL, a,b are independent variables in [0,1]; in LR, the exact L=1 collision forces a=b=y.

Define the P-error residual R = e_P - 21/100 - T_P/20 - T_Q/100 and the time deficit D = 8-T_P-T_Q. Keeping the original source-labelled positive P/Q cylinder masses until summation yields

(1) R = eps(alpha*a - beta*b)/6.

Every stop occurs by time 4. The disjoint early-stop cylinders at roots and at A1/B1 give the universal lower bound

(2) D >= 3[(1-alpha)+(1-beta)] + (2/3)(alpha*a+beta*b).

Here P(A)+Q(A)=P(B)+Q(B)=1, P(A1)+Q(A1)=P(B1)+Q(B1)=1/3, and all other stops contribute nonnegative extra time loss. No path is double counted.

Let Phi_eps(O) = R - (eps/10)*D. Under LR, a=b=y, so R=eps*y*(alpha-beta)/6 <= eps*(1-beta)/6, while D>=3(1-beta); hence Phi_eps <= eps*(1-beta)*(1/6-3/10)<=0. The never-stop policy attains zero. Consequently

(3) max over all real LR policies of Phi_eps = 0.

For FULL, (1)-(2) imply

Phi_eps <= eps[(1/10)alpha*a -(7/30)beta*b -(3/10)(2-alpha-beta)] <= eps/10.

Continue at both roots, stop at t2 only at A1 (alpha=beta=a=1,b=0) and otherwise at forced t4. Then D=2/3 and R=eps/6, attaining the bound. Therefore

(4) max over all real FULL policies of Phi_eps = eps/10.

This is an exact signed support difference for every eps in the stated interval, independent of eta. It proves distinct convex hulls for arbitrarily small nonzero rational perturbations. The proof includes all real hazards 0 and 1, unreachable nodes and time3 decisions; no finite direction grid or continuity guess is needed.

## Integer facet, witness, distance and dimension

At eps=eta=1/1000, multiply Phi_eps by 10000. Every real LR strategy and its convex hull satisfy

(5) 10000*e_P - 499*T_P - 99*T_Q <= 2108.

The lawful FULL policy stopping solely on A1 at time2 yields

(6) Ostar = (2581/6000,551/1800,11/3,11/3)

and makes the left side equal **2109**. Thus the exact integer support gap is 1. Hölder's inequality gives an L-infinity distance lower bound 1/(10000+499+99)=**1/10598** from Ostar to every LR observation, including convex mixtures. This is a lower bound, not an assertion of exact geometric distance.

Both observer polytopes have affine rank four. In the precise key order printed by VERIFY.py, difference vectors from the never-stop observation corresponding to LR binary masks [1,2,9,512] have determinant -1/144000000 = -eps*eta/144. The analogous FULL masks [1,2,8,32] have determinant 1/8640000000 = eps*eta/8640. Thus these determinant witnesses remain nonzero for all nonzero eps,eta in the domain. This is a full-dimensional **affine-span** statement and does not claim convex-hull equality.

## Actual computation, literature context and open boundary

VERIFY.py uses only Python standard-library fractions.Fraction, explicitly reconstructs source-labeled path P/Q masses, checks strictly positive transition and error kernels and the two collisions; enumerates **16,384 FULL and 4,096 LR** deterministic strategies; checks four-observer observations, exact signed maxima, and both full-rank rational determinants. Actual stdout is EXACT_OUTPUT.txt, ending PASS_EXACT_R5_DOUBLE_COLLISION_FULL_RANK_PERTURBATION. The deterministic support extrema cover all real behavioral policies since no natural path can revisit the same time-labelled LR decision key, so the objective is multi-affine in every hazard. The analytic proof above independently proves the all-real extrema.

This negative candidate does **not** solve the mother's hull-equal-but-real-image-different question. Neither an original-science-priority assertion nor a physics/native-X6 validation is implied. Classical background: Cho and Stockbridge, *Linear Programming Formulation for Optimal Stopping Problems*, SIAM J. Control Optim., DOI 10.1137/S0363012900377663 (stop/occupation measure perspective); Hobson and Zeng, *Randomised Rules for Stopping Problems*, J. Appl. Probab. 57 (2020), DOI 10.1017/jpr.2020.43. These references are contextual and are **not** claimed as independent proof of (1)-(6).

Native status observed this run: research_authority_granted=false, UPSTREAM_CODE_REVIEW_REQUIRED, active quota 5/5; an em_control_tasks owner-inventory request returned CONTROL_QUOTA. Consequently current task owner/CLAIM/Result/review cannot be authenticated. This author-side PR delivery does not adopt a Source task, forge reviewer independence, modify P000, or change task admission. Files: RESEARCH.md, actual VERIFY.py, actual EXACT_OUTPUT.txt, NEXT_TASK.md. All four are intended for immutable remote readback.

**Next exact unit:** Find compensated multi-history rational error perturbations preserving both collisions and full dimension while removing every signed convex-hull obstruction. For each FULL deterministic four-vector produce a rational LR convex combination of at most five points, or an exact Farkas separator; only after full hull equality passes, test actual real seedless-LR image membership with a certified semialgebraic or component-range certificate. Preserve the baseline 13-vertex winding proof and the present explicit full-rank counter-screen as separate scoped results.
