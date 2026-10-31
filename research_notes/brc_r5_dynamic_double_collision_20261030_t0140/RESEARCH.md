# R5 — Nonfrozen two-stage likelihood-ratio collisions and an exact support obstruction

Date: 2026-10-30 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

Fixed input: GLOBAL_KNOWLEDGE_V1 main@239935e95a8ed3cc0176fe9be619482c6753f354 (bootstrap, manual, P000, ACTIVE worldview, research and BRC policies); Enterprise Math main@e65565e5b32cf22455de0a488d41a0cd8d57fb31 (portable protocol and current control authority). Exact predecessor: research_notes/brc_r5_frozen_lr_dynamic_branch_20261030_t0035/RESEARCH.md at 85f244caefa0ae2fcf32457575699ba8465f547d. This is a finite auxiliary two-law stop experiment, not an X6/native Heartbeat physics claim. BRC reuse: COMPOSE_APPLIED to positive labeled P/Q path mass and provenance; signed differences occur only in the observer.

## Question

For original O=(e_P,e_Q,T_P,T_Q) of a finite strictly positive absorbing stopping experiment, compare FULL behavioral policies (all history) with seedless LR policies (only current time and exact prefix L=P(h)/Q(h)). The mother target seeks equal four-dimensional convex hulls and unequal actual real observer images. Prior R5 proved frozen LR keys cannot yield that target. Here LR keys update nontrivially, collide twice, and all three optional stopping times are consequential. This exact positive candidate still fails hull equality, and we locate its two separate information penalties.

## Lemma — complete binary LR-collision parameterization

At a positive parent with ratio r>0, let a binary continuation event E have probabilities p=P(E=1|h) and q=Q(E=1|h). For a selected child ratio c>0,

L(h,1)=c iff p=(c/r)q with 0<q<min(1,r/c).

The complementary sibling has the necessarily positive ratio

d=L(h,0)=(r-cq)/(1-q), and r=qc+(1-q)d.

Conversely, these formulas generate every strictly positive rational binary transition realizing the selected rational ratio c. For r_A<c<r_B, simultaneous first-child collision at c implies d_A<r_A<c<r_B<d_B, since d-r=q(r-c)/(1-q). If two parents already have ratio c, a new common selected-child ratio c'!=c can be obtained with different legal q_A!=q_B and p_s=(c'/c)q_s; their complementary ratios differ since d(q)=(c-c'q)/(1-q) is strictly monotone for c'!=c (cross multiplication, or derivative (c-c')/(1-q)^2). This constructs source-sensitive later kernels with a preserved exact LR collision and nonzero complementary branches. All claims follow from L(child)=r P(event|h)/Q(event|h), with strict positivity as stated.

## Strictly positive 4-time model

Initial nature source S is A or B, observed by FULL at t=1. P(A)=1/3, Q(A)=2/3, so L(A)=1/2; P(B)=2/3, Q(B)=1/3, so L(B)=2. Optional stop at t=1; after continuation first positive binary nature signal Y leads to optional stop t=2. After continuation second positive binary signal Z leads to optional stop t=3, else forced stop t=4. Stopping absorbs; potential future nature paths below are only a counterfactual expectation coupling.

First nature kernel P(Y=1|S), Q(Y=1|S):
A: (1/2,1/4); B: (1/4,1/2).
At t=2: A1 and B1 share exact LR=1; A0 has LR=1/3 and B0 has LR=3. In particular neither selected parent has frozen LR.

Second nature kernel P(Z=1|S,Y), Q(Z=1|S,Y), and its exact child ratios:

| S,Y | P(Z1) | Q(Z1) | LR at Z1 | LR at Z0 |
|---|---:|---:|---:|---:|
| A1 | 1/2 | 1/4 | 2 | 2/3 |
| B1 | 2/3 | 1/3 | 2 | 1/2 |
| A0 | 1/2 | 2/5 | 5/12 | 5/18 |
| B0 | 1/2 | 3/5 | 5/2 | 15/4 |

A11 and B11 collide *again* at t=3 with LR=2 even though both P and Q second-stage conditional kernels are source-sensitive. The other Z child ratios are distinct. All 8 full potential leaves have strictly positive P/Q mass; their masses sum to one under each law.

P-law error Bernoulli rates are: p1=3/4; p2(A1,B1,A0,B0)=(1/10,9/10,1/2,1/2); p3(A1z,B1z,A0z,B0z)=(9/10,1/10,1/2,1/2) for each z; p4=1/2.
Q-law Bernoulli rates are: q1=2/3; q2(A1,B1,A0,B0)=(3/10,7/10,2/5,3/5); q3(A11,A10,B11,B10,A01,A00,B01,B00)=(1/5,3/5,4/5,2/5,2/5,3/5,1/3,2/3); q4=1/2. All are strictly between 0 and 1. These q-rates complete the exact original four-coordinate observer, and every optional time can change an observable.

## Theorem — exact all-real separation, two-stage attribution

For this fixed model, across **every real** seedless LR strategy and every real FULL strategy,

min_FULL e_P=11/30, min_LR e_P=7/15, gap=1/10.

Hence the global LR halfspace **30e_P>=14** contains the entire real LR observer set and its convex hull. Yet a legal deterministic FULL strategy that continues at t=1, stops on A1 at t=2, stops on B1 at t=3, and otherwise stops at t=4, has the exact four-observer vector

O_*=(11/30, 17/36, 7/2, 7/2).

At O_* the left side 30e_P is 11, violating the LR threshold 14 by 3. Consequently conv(O_FULL) != conv(O_LR), and L-infinity distance of O_* from the whole LR convex hull is at least 1/10. This is a **rejected mother candidate**, not a hull-equal solution.

**All-real proof.** Every real behavioral policy is specified by one stop hazard in [0,1] for each permitted key (t,history) or (t,L). A potential nature path visits a given time-key at most once; its contribution to e_P is a product of stop/continue hazards times a fixed positive path mass and terminal-error rate. Thus e_P is affine in each hazard separately when others are fixed. Each coordinate can be rounded to an endpoint without improving beyond the global minimum. Therefore both minima over all real behavior policies are attained among their deterministic hazard corners, even with shared LR keys and unreachable branches. There are 2+4+8=14 FULL keys (16,384 corners), and 2+3+7=12 LR keys (4,096 corners), exactly enumerated using Fraction in VERIFY.py. The following direct reduction establishes the minima independently of enumeration.

At t=1 immediate P-error is 3/4. Any continuation from source A has error at most (1/2)(9/10)+(1/2)(1/2)=7/10; from source B at most (1/4)(9/10)+(3/4)(1/2)=3/5. So optimal policies under either information class never stop at t=1. For Y=0 histories all t>=2 P-errors equal 1/2; their combined P mass is 2/3, contributing 1/3 to both minima.

On the A1 and B1 histories at t=2, their P masses are each 1/6. FULL stops A1 immediately for error 1/10, but continues B1 to t=3 for error 1/10, making a combined cost 1/30.

LR sees the same time-2 key LR=1 on A1 and B1, so it must stop both or continue both. Stopping both yields P-error cost (1/6)(1/10+9/10)=1/6. On continuing, the t=3 LR=2 key combines A11 of P mass 1/12 and B11 of P mass 1/9. Its cost(stop3)-cost(continue4) equals (1/12)(9/10-1/2)+(1/9)(1/10-1/2)=-1/90, so LR optimally stops both. At the t=3 distinct keys A10 (LR=2/3) and B10 (LR=1/2) it chooses continue A10 to t=4 (P-error 1/2) and stop B10 at t=3 (P-error 1/10). Thus continuing both A1 and B1 at t=2 has cost (1/6)(7/10)+(1/6)(1/10)=2/15, smaller than stopping both (1/6). Add common Y=0 cost 1/3: min_LR e_P=7/15, min_FULL e_P=11/30. The multiaffine endpoint argument extends this exact support conclusion to all real hazards. QED.

**Two-stage residual localization.** Define a precise *diagnostic relaxation* TAG3 that has the same LR information at t=1 and t=2, but additionally sees the source tag only at (t=3,LR=2). This is *not* the original LR class. It can continue A11 to t=4 (error 1/2) and stop B11 at t=3 (error 1/10), giving min_TAG3 e_P=13/30. Therefore

min_LR e_P-min_FULL e_P = (min_TAG3 e_P-min_FULL e_P)+(min_LR e_P-min_TAG3 e_P)
= 1/15 + 1/30 = 1/10.

These two positive losses are an **exact conditional observer decomposition for this model**, not a universal information measure, signed BRC mass, or physical energy. Positive labeled path mass and the source tag must be preserved before quotient; the signed residual is an observer comparison.

## Actual verification and source boundary

VERIFY.py executes standard-library fractions.Fraction exhaustive enumeration of all **4,096 LR**, **8,192 TAG3**, and **16,384 FULL** deterministic strategies, plus checks all P/Q kernels and terminal Bernoulli rates strictly positive and <1, positive nature-leaf mass conservation, all time-2 and time-3 collision identities, the explicit full observer witness, minima and both loss components. EXACT_OUTPUT.txt is the actual executed stdout; marker PASS_EXACT_R5_DYNAMIC_DOUBLE_COLLISION_TWO_STAGE_OBSTRUCTION. Re-execution of the same program locally agreed with the output. Universal real-strategy scope follows from the multiaffine proof, not extrapolation of numerical samples.

Limitations: The general collision chart is mathematically proved in the declared finite auxiliary model. Numerical minima and observer decomposition hold only for this explicit rational experiment. This candidate has a **nonzero signed support gap**, so it cannot solve the mother question. No all-signed hull equality, actual-image counterexample, native X6 correspondence, independent reviewer, formal Source CLAIM/Result, or P000 revision is asserted. Native current-owner query returned CONTROL_QUOTA at this turn and service research_authority_granted=false; this is portable author evidence only.

## Next mathematical unit

Hold the exact nonfrozen two-stage nature chart fixed while varying terminal P/Q error kernels over positive rationals, maintaining three genuinely consequential stop times. Seek elimination of **all** signed FULL-vs-LR support gaps before any real-image nonmembership work. For every deterministic FULL four-observer vector, produce an exact nonnegative convex representation by <=5 LR deterministic vertices (Carathéodory in R4), or an explicit rational Farkas separator, then test the actual seedless LR semialgebraic image only when all such certificates pass. Keep BRC positive path/provenance typed; stage-specific residuals and zero-reach/boundary cases remain explicit. See NEXT_TASK.md.
