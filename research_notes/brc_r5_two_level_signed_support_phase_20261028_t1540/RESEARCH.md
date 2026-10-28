# R5 — 两层异质似然比碰撞的精确有符号支撑相变

2026-10-28 Asia/Shanghai. Local author-side identity LOCAL_EM_R5_20261028_1540_PHASEGATE / TASK_RESEARCH. AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. This is portable author evidence, not service-issued research identity, formal CLAIM, Result, or Driver review.

Frozen global source: GLOBAL_KNOWLEDGE_V1 main@c4a44293d89f7f12bfbdb89d261ec77abf8f2595. Frozen project baseline: enterprise-math main@f75dae1d65ef842089950d0a440c61cab20e42e2. P000 canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches the P000 startup projection. ACTIVE worldview, TASK_RESEARCH routing and portable research constraints applied. Source owner is not confirmed: current em_control_tasks returned CONTROL_QUOTA, source context granted no research execution authority. Predecessor: research_notes/brc_r5_occupation_weighted_tv_20261028_t1440 at immutable project commit e8bfe95b2fe90203681df9e59cccfd8a3b3d6c6b. The model below is the same strictly positive rational external statistical tree, not a native X6 physics demonstration.

## Exact model and observer

A passive two-law P,Q observation tree has 22 raw histories, 14 terminal leaves, three decision stages, 11 distinct time–likelihood-ratio signatures. Initial hidden-source tags A and B each have Q and P mass 1/2, hence each has ratio r=P(h)/Q(h)=1. At the next stage the child ratios are s=(1/2,1,3/2). Under Q, conditional rows are A=(1/4,1/2,1/4) and B=(1/8,3/4,1/8). Under P the conditional probabilities are s_i times these Q probabilities; each row sums to 1 because its Q-weighted ratio mean is 1. At stage 2, ratio s=1 again uses the respective A/B row to produce stage-3 ratios (1/2,1,3/2). For stage-2 ratio r=1/2 or 3/2, stage-3 ratios are r·(3/4,5/4) with Q probabilities (1/2,1/2) and P conditional probabilities (3/8,5/8). Every leaf has positive P,Q mass; both measures sum to 1.

A full-history policy chooses stop/declare-P, stop/declare-Q, or continue from the raw history. A seedless LR behavioral policy chooses solely from the current (time, ratio) and fresh local randomness. At stage 3 continuation is forbidden. Each action probability may be any real in [0,1]. O=(e_P,e_Q,T_P,T_Q): e_P=P(declare Q), e_Q=Q(declare P), T_mu=E_mu[stopping stage]. For signed lambda, V_full and V_LR mean minimum lambda·O within the respective complete real-policy classes.

## Exact signed-support theorem and quantitative witness

For lambda(w)=(4,4,-8,w) over the complete interval 17/2 <= w <= 12, put Delta(w)=V_LR(w)-V_full(w). The exact piecewise result is

Delta(w) = 0 for 17/2 <= w <= 26/3;
Delta(w) = (9w-78)/16 for 26/3 <= w <= 170/19;
Delta(w) = (46-5w)/8 for 170/19 <= w <= 46/5;
Delta(w) = 0 for 46/5 <= w <= 12.

All expressions agree at their shared endpoints. Delta>0 exactly on (26/3,46/5) and attains its maximum 3/19 at w=170/19.

For the integer lambda=(4,4,-8,9): V_full=39/8 < V_LR=5, gap=1/8. A full-history optimal action policy is: stage-1 A continues, B declares P; on the reached stage-2 A children, r=1/2 declares Q, r=1 declares P, r=3/2 continues; on the reached stage-3 r>1 children declare P. All other unreachable actions can be chosen arbitrarily. This achieves the exact four-vector O*=(1/16,7/8,27/16,13/8).

Therefore every seedless real LR strategy has 4e_P+4e_Q-8T_P+9T_Q >= 5 while the full witness has value 39/8. By the dual norm inequality, ||O_LR-O*||_infty >= (1/8)/(4+4+8+9)=1/200 for every LR policy.

At the peak, multiply lambda(170/19) by 19/2 to obtain integer normal lambda_peak=(38,38,-76,85). The same O* remains full-optimal and gives min_full=91/2, whereas min_LR=47. The global separation is 3/2, so ||O_LR-O*||_infty >= (3/2)/(38+38+76+85)=1/158. This is a GLOBAL REAL-POLICY nonmembership certificate. It also refutes convex-hull equality for this 22-history model, which is thus excluded from the original mother-question candidates.

## Algebraic proof (not extrapolated from a grid)

The first-stage time cost is a policy-independent -8+w, as E_mu[stopping time]=1+sum_{t<3}Pr_mu(continue beyond t). For a stage-3 history with Q mass q and ratio s, stopping and declaring P costs 4q; stopping and declaring Q costs 4sq. Their minimum for any real randomized declaration is q f(s), f(s)=4 min(s,1).

At stage 2, stopping has per-unit-Q minimum f(r); continuing has per-unit-Q cost -8r+w+E_Q f(s_next). For r=1/2, E f=2 (terminal ratios 3/8,5/8), giving continuation w-2 > 2=f(1/2) throughout the interval. For r=3/2, E f=4 (terminal ratios 9/8,15/8), giving w-8 <= 4=f(3/2). For r=1, Q expected terminal costs are 7/2 under source A and 15/4 under source B. Continuation costs w-9/2 and w-17/4, both >=4=f(1) for w>=17/2. Thus one common stage-2 LR policy simultaneously realizes every hidden source's Bellman minimum: declare Q at r=1/2; stop (either declaration) at r=1; continue at r=3/2. Its stage-3 Bayes declaration is likewise determined by the current ratio. No stage-2 compression defect is being omitted.

At stage 1, immediately stopping has cost 4 per unit Q. Continuing from A and B under those sourcewise-optimal common downstream actions has the respective costs
C_A(w) = (w-8)+(1/4)*2+(1/2)*4+(1/4)*(w-8) = 5w/4-15/2;
C_B(w) = (w-8)+(1/8)*2+(3/4)*4+(1/8)*(w-8) = 9w/8-23/4.

Both root masses under Q are 1/2, and C_A(w)<C_B(w) on the entire specified interval. Full-history policies can choose A and B independently:
V_full(w)=(w-8)+[min(4,C_A(w))+min(4,C_B(w))]/2.
An LR policy must use the SAME action on the two initial histories with signature (1,1):
V_LR(w)=(w-8)+min(4,[C_A(w)+C_B(w)]/2).
These are exact minima over all real behavior policies. Conditional on reaching each stage-2 fiber, all raw sourcewise minima are already achieved by a common LR rule, so no future adjustment can improve these minima; each local probability mixture simply interpolates its action costs. Equivalently, a path visits each (stage,ratio) at most once, so the global linear functional is multi-affine in independent fiber-action vectors and attains a minimum at a deterministic vertex.

The crossings C_B=4, (C_A+C_B)/2=4, and C_A=4 occur respectively at 26/3, 170/19, 46/5. Substitution gives the complete four-interval formula above. At w=9, C_A=15/4, C_B=35/8, full=1+(15/4+4)/2=39/8, LR=1+4=5. At w=170/19, C_A=70/19, C_B=82/19, their mean is 4, and the values are 91/19 and 94/19 respectively before the 19/2 normal scaling. The stated L-infinity bounds follow from Holder's inequality. QED.

## Verification scope, BRC reuse and next issue

VERIFY.py independently reconstructs the 22-node exact P/Q tree and checks positive leaf masses, exact normalization and P/Q conditional ratio means. It computes full minima by backward Bellman recursion and compressed minima by all 3^4=81 deterministic nonterminal time-ratio action combinations, with Bayes-optimal terminal declarations. It checks seven rational values including breakpoints and interior points, plus the explicit full four-vector and two integer normals. Exact program output is in EXACT_OUTPUT.txt. Interval-wide validity comes from the algebra above, not sample coverage.

BRC_REUSE_APPLIED: preserve A/B branch provenance and positive rational Q mass; transport the typed P mass using P(h)=r_h Q(h); retain ratio conditional moment constraints, continuation flux and signed Bellman-source residual. Collapsing sources A,B to the same initial ratio discards the observable future cost contrast C_A!=C_B. This is a finite external statistical experiment; native Heartbeat World X6 embedding/readout/future-relation preservation remains a separate obligation. No formal acceptance, independent review, active-owner verification or scientific priority claim is made.

Next: seek a multi-collision family whose EVERY four-dimensional signed support direction has exact convex-hull equality. Only after establishing that stronger precondition seek a global semialgebraic real-LR-image nonmembership witness. See NEXT_TASK.md.