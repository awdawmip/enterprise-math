# Stage352-B: conditional full-model first endpoint switch at the exact Bernoulli/BRC cusp

Status: PORTABLE_AUTHOR_CONDITIONAL_THEOREM / EXACT_FRACTION_BERNSTEIN_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Date 2026-11-01 Asia/Shanghai.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@69e1f32ec41c700e11f8da6f46b2c3b58e4bcf25; Enterprise Math main@37ab859d390bd72771541d24567b16bf07a5ba7e; original P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Research continuation Stage351-B PR #1736 @cef9ad60c0c4a81d8cc86b1235917aba2ad45e06.

## Precise external auxiliary model

For k=0,1,2,3, put B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9). Define r_k(x,y)=(4 B_k(x)+B_k(y))/5-m_k/160, b=5/32 sum_k w_k |r_k| and D_3(a,z)=1/2 sum_k w_k|B_k(a)-B_k(z)|. Let
c=[63 D_3(1/4,x)+D_3(3/4,x)+9 D_3(1/4,y)+7 D_3(3/4,y)]/256. All sixteen source-word comparisons are retained. The two-source target T=33/1024+c(q1)+c(q2), constrained by b(q1)+b(q2)≤2 beta_*+E. Here q_* is the r0=r1=0 double root, beta_*=b(q_*), q_s lies on the right r1=0 arc with b(q_s)=beta_*+s, and phi(s)=c(q_s).

## EXACT conditional mathematical claim

Assumption A: Stage346-B author's global uniqueness of q_* as minimizer of b holds. Assumption B: Stage336/342-B author's strict Pareto domination of the entire r3≥0 stratum, including r3=0, holds. Both are author proofs awaiting independent review.

The Stage351 restricted-right-arc exact interval certificate isolates tag cusp E† by
0.0021814072266 < E† < 0.0021814072275.
Under A and B, for every *real* E in [0,E†] the full auxiliary problem has exact optimum
min T = 33/1024+phi(0)+phi(E),
with unique optimal configuration (q*,q*) for E=0, and the two endpoint permutations (q*,q_E),(q_E,q*) for E>0. For every E†<E≤11/5000, the incumbent endpoint pair is strictly beaten by the feasible cusp split, with
phi(0)+phi(E)-phi(E†)-phi(E-E†) > (E-E†)/50.
Thus E† is the infimum of budgets where the endpoint pair ceases to be globally optimal, **conditional on A and B**. No post-cusp global optimizer is identified.

## New exact certificates

Let Q=5961/1000000 and R=[219/1000,6/25]×[101/200,16/25]. The 391-leaf rational Bernstein quadtree (max depth 11) proves b(x,y)≤Q implies (x,y)∈R for *all real* x,y∈[0,1]. The strict minimum outside-box rational margin is 127343549/16777216000000, with total exact leaf area 1. The inherited root/cusp isolators verify beta_*+E†<Q.

On the low strip L=[.219,.240]×[.505,.531] and high strip H=[.219,.240]×[.625,.640], 22 and 1 exact Bernstein leaves (max depths 4 and 0) establish the label-preserving fused inequality
c+(121/100)b > 3776281/100000000 = 611/20000+(121/100)Q.
Exact strict minima are respectively 202389891/131072000000000 and 158772379/51200000000, so b≤Q forces c>611/20000 in both strips. This replaces the old invalid-at-the-cusp uniform 0.031 audit floor. At E0=1/500, right-arc root bracketing and all sixteen cost labels imply c(q_E0)<7818466377393/256000000000000=0.0305408842866914<611/20000, and monotonicity extends that upper bound to E†. These strict inequalities exclude outer strips from optimality.

In the middle strip [.219,.240]×[.531,.625], exact bounds show r2>0, c_x<-0.43, c_y>0 and check all changed rational sign-chamber derivative inequalities for the expanded x_min=.219. Invoking A/B plus Stage347 analytic region topology reduces each scalar sourcewise Pareto optimum to q_s. The prior Stage349 conditional frontier covers s≤.0020; the new certificates extend it to s≤E†. Stage351 strict phi'<0, phi''<0 implies the two-source budget optimum exhausts the budget and lies at endpoints until the cusp.

## Reproducibility and obligations

Executed twice with Fraction rational arithmetic, reusing Stage348 and Stage351 exact checkers unchanged. Recorded result: STAGE352B_EXACT_GLOBAL_CUSP_ENCLOSURE_AND_FUSED_BARRIER_PASS. Certificate SHA256:
global 5cab8d02d9bcc92c078fedc9e299850a61b9f9e8987244f8e6daff72ab4fe1ba (391 leaves);
low 615050cf103d3e39193eb23d583b23e1bddf3f82cf85125ecd84169c098c200f (22 leaves);
high 11250fe1e742748bc06f112819c49827ca759e2dbda7f5125bc528700ffcb815 (1 leaf).

Formal review next: independent full proof/verification of inherited A and B and sign-boundary topology, then post-cusp global split optimization. A future-safe P000-native X6 bridge is a separate scientific obligation. No service-issued Researcher authority, owner confirmation, CLAIM, Source Result or Driver acceptance was obtained: native owner query returned CONTROL_QUOTA; service research_authority_granted=false.

This summary contains the complete exact statement, local evidence inventory and execution scope; the seven original full-length files remain in the originating research run for now, until GitHub can store and verify their original bytes.
