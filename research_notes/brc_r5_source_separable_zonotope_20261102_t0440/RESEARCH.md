# R5 — exact ray criterion for source-separable LR decisions

**Date:** 2026-11-02 Asia/Shanghai. **Result class:** mathematical author-side proof, exact rational regression, UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

**Scientific pins, unchanged:** GLOBAL_KNOWLEDGE_V1 main@a01383f825ef9d43b4b754254303298c64041568; Enterprise Math main@86149263e38c22292c9def1e0f69092efa1be77e. **Current normative snapshot:** Global Knowledge main@114aee9d25a2a939412f5ee4aa78dcd7b711d29f; Enterprise Math main@28f85eb6ab2d327918209fa2ec8dc91cdbbad505. P000 original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches the P000_STARTUP projection; ACTIVE worldview remains unmodified.

**Predecessor:** Enterprise Math commit 046ec682f1d0f38ef4b4a9b34201fdc7208ac54b, research_notes/brc_r5_balanced_two_route_kernel_20261102_t0340/RESEARCH.md and NEXT_TASK.md. The predecessor obtains signed FULL/LR support gap (31/40)t for a different, interacting source-sensitive two-route model. This note is a new general classification of the restricted source-separable subcase.

## Model and question

The mother question: construct a finite two-law P/Q stopping model whose FULL and seedless LR four-observer **convex hulls agree** but whose actual real four-observer images differ. O=(e_P,e_Q,T_P,T_Q), where e_P is P(final answer P), e_Q is Q(final answer Q), and T_P,T_Q are expectations of terminal integer time.

Fix k>=1 positive source-tagged P/Q arrivals at a single shared (time,likelihood-ratio) decision key. All origins share the same positive P/Q likelihood ratio. Arrivals are *exogenous*, unaffected by behavioural decisions here; origin i has precisely two actions stop/continue with fixed additive observer contributions v_i^1 and v_i^0. After this key there are no behavioural choices or decision-dependent downstream arrivals. A fixed observer contribution B may come from other noninteracting paths. FULL chooses independently x_i in [0,1] for each origin; seedless LR chooses one common real x in [0,1] for the shared key. Put d_i=v_i^1-v_i^0 and V=B+sum_i v_i^0. Natural probabilities and source masses stay nonnegative; the explicit example uses strictly positive P/Q natural transitions.

## Theorem 1 — exact all-signed support and complete image classification

For all real x_i,x and every signed normal n in R^4,

FULL_image = V + {sum_i x_i d_i : 0<=x_i<=1} (a zonotope);

LR_image = V + {x sum_i d_i : 0<=x<=1} (a segment);

gap(n) = h_FULL(n)-h_LR(n)
= sum_i max(0,n·d_i)-max(0,sum_i n·d_i)
= min(sum_i max(0,n·d_i),sum_i max(0,-n·d_i)) >= 0.

The following are equivalent:
(1) conv(FULL_image)=conv(LR_image);
(2) FULL_image=LR_image;
(3) all nonzero d_i belong to one common nonnegative ray, or every d_i is zero.

**Proof.** Independent Bernoulli choices and linear expectation give the two images. A signed linear functional on the FULL product [0,1]^k attains its maximum by choosing x_i=1 exactly when n·d_i>0; LR has one x and chooses according to the sign of their sum. Let A=sum max(0,n·d_i), Bneg=sum max(0,-n·d_i); then A-max(0,A-Bneg)=min(A,Bneg), giving the gap formula.

If d_i=c_i d with all c_i>=0, the scalar sum sum c_i x_i ranges over the complete interval [0,sum c_i]. One LR choice x=(sum c_i x_i)/(sum c_i) reproduces it (or both images are a point). Thus (3) implies (2) implies (1).

If the nonzero d_i do not lie on a common nonnegative ray, two nonzero vectors a,b are either independent or opposite-collinear. For an independent pair choose n with n·a=1, n·b=-1; for opposite-collinear b=-c a, c>0 choose n·a=1, n·b=-c. Both signs then occur and gap(n)>0, separating the convex hulls, proving the converse. Both images are already convex (zonotope and segment), so the equivalences are exact.

### Rational constructive signed separation

For rational independent a,b choose indices r<s with D=a_r b_s-a_s b_r !=0. Set n_r=(b_s+a_s)/D and n_s=(-b_r-a_r)/D, all other coordinates zero. Then n·a=1 and n·b=-1. For opposite-collinear b=-c a, c>0, choose coordinate r with a_r!=0 and put n_r=1/a_r, others zero, yielding n·a=1,n·b=-c. Multiplying by a positive common denominator gives an integer normal. With k sources, the gap is at least 1 in the independent-pair case and min(1,c) in the opposite-collinear case. A FULL maximizer W obtained by selecting x_i=1 for positive n·d_i satisfies dist_infinity(W,LR_image)>=gap(n)/||n||_1.

For rational data, compare every nonzero d_i against one fixed nonzero reference to test nonnegative collinearity in O(k*4^2) field operations. A violating pair returns the rational normal above, without a linear program. This is an early exact rejection filter for separable provenance gadgets, not a substitute for the full coupled-key convex-hull test.

## Theorem 2 — independent parallel keys cannot solve the mother target

Take finitely many independent, exogenously visited keys, each as above, with additive observer contributions and **no shared behavioural parameters across keys**. The FULL and LR images are Minkowski sums of per-key images; their signed support gap is the sum of the nonnegative per-key gaps. If the global hulls agree in all directions, each per-key gap vanishes in every direction. By Theorem 1 each local FULL real image equals its LR image, hence their Minkowski sums (the actual global real images) are equal.

**Proof.** Support functions obey h_(A+B)(n)=h_A(n)+h_B(n). Each local gap is >=0. A zero sum for all n forces every summand zero for all n. Apply Theorem 1 at each independent key, then sum the actual images. Decision-dependent reachability (such as I controlling arrivals at J) is outside this theorem.

## Strictly positive two-law exact example with cancelling aggregate kernels

At a single (time=1, LR=1) key, two hidden origins each carry incoming P=Q=1/2. Stop answers P at time 1. Continue naturally answers at time 2. Under origin 1 the conditional answer-P probabilities under P,Q are (3/4,1/4); under origin 2 they are (1/4,3/4). Each answer and each complementary branch is strictly positive in both measures. Across origins the aggregate answer-P chance under both P,Q is exactly 1/2: the source-dependent kernel deviations cancel in the aggregated dual-law flow.

The per-origin continue, stop and advantage vectors are:
v1^0=(3/8,3/8,1,1), v1^1=(1/2,0,1/2,1/2), d1=(1/8,-3/8,-1/2,-1/2);
v2^0=(1/8,1/8,1,1), v2^1=(1/2,0,1/2,1/2), d2=(3/8,-1/8,-1/2,-1/2).

With signed n=(1,1,0,0), n·d1=-1/4 and n·d2=1/4. Therefore max_FULL n·O=5/4; every real LR policy has n·O=1; exact gap=1/4. The FULL action 'continue origin 1, stop origin 2' produces W=(7/8,3/8,3/2,3/2). LR endpoints are (1/2,1/2,2,2) and (1,0,1,1), with midpoint (3/4,1/4,3/2,3/2). The normal gives dist_infinity(W,LR_image)>=1/8; the midpoint attains 1/8, so the **exact distance is 1/8**.

The BRC P/Q carriers are all positive, and origin tags are preserved through terminal readout. Signed normals are observer-level dual functionals, never signed physical probability mass.

## Executed computation and boundaries

The accompanying VERIFY.py was executed using only Python standard-library fractions.Fraction and itertools.product, with actual stdout captured in EXACT_OUTPUT.txt. It checks the 4 deterministic FULL and 2 LR endpoint policies, strict conditional natural positivity, P/Q aggregate cancellation, signed support, explicit witness, exact infinity distance, constructive rational separation for independent, positive-collinear and opposite-collinear pairs, and a three-origin gap regression. The all-real k-source and parallel-key classifications above follow from the analytical proof, not finite sampling.

Scientific scope: author-side proved and exact checked; no native X6/3D-slice transfer, independent Driver review, Source Result, or Foundation promotion claimed. This runtime's native gateway reported research_authority_granted=false and executor_binding_configured=false; em_session_start returned STATIC_READONLY_SCOPE_DENIED without backend submission; bounded active-owner read returned CONTROL_QUOTA. Formal owner/CLAIM remains unconfirmed.

## Next question

Build a genuinely causally coupled I→J two-law stopping model: an upstream behaviour parameter should change the source-weighted arrivals at a later shared key, while exact P/Q ratios and positive transitions are retained. Use this theorem to simplify separable tails, not the coupled whole. First test complete four-observer hull equality using exact rational FULL-vertex vs LR convex-combination certificates (or rational Farkas separators); if hull equality holds, investigate actual real LR image nonmembership using an exact algebraic or semialgebraic argument.