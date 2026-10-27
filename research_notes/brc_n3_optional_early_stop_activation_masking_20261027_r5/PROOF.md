# R5 — N=3 optional-early-stop exact Bellman activation/masking theorem

2026-10-27. Author-level finite BRC positive-mass probability-tree result; **UNREVIEWED / NOT_ADMITTED**. This is not a native Task CLAIM, Source Result, independent Driver review, native X6 transfer or P000 promotion.

Frozen research inputs: GLOBAL_KNOWLEDGE_V1 main@ad4f63878ca0534cdd52af1c5590bff3a777ab08 and Enterprise Math main@e802688c4c520633a7880b817e46778903d0f967, including P000, the ACTIVE worldview, joint-observer preservation, BRC typed positive mass and portable research protocol. Predecessor: research_notes/brc_n3_penultimate_hinge_completeness_20261027_r5, which required compulsory arrival at the penultimate decision. This theorem removes compulsory arrival. Native owner lookup returned CONTROL_QUOTA, so this portable work has no verified CLAIM/Driver approval.

## Model and typed observables

For a finite strictly positive P,Q observation tree with optional stop-and-classify at t=1 or t=2 and compulsory stop at t=3, define L(h)=P(h)/Q(h), and
O(pi)=(P(decide Q),Q(decide P),E_P tau,E_Q tau).
Full-history behavioral decisions may condition on the observed history. Seedless LR behavioral decisions depend only on (time,L), with local real randomization but no persistent random seed. For arbitrary signed lambda=(l1,l2,l3,l4), minimize lambda·O. Define S(r)=min(l1*r,l2), c(r)=l3*r+l4. For each t=2 history h, define its terminal Q-kernel K_h(y)=Q(L3=y|h), H_h=sum_y K_h(y)S(y), and a_h=c(L(h))+H_h-S(L(h)). These are exact positive-branch masses and conditional LR kernels; the hidden history label is the information potentially erased by LR compression.

## Theorem 1: general signed-objective decomposition with optional early stop

Let I be all distinct first-stage LR classes. Let alpha in {0,1}^I be a pure LR-compatible first-stage continuation schedule. Set b_h(alpha)=Q(h)alpha_{L(parent(h))} for each t=2 history. Define

F(alpha)=l3+l4 + sum_{g at t=1} Q(g)[(1-alpha_{L(g)})S(L(g))+alpha_{L(g)}c(L(g))]
         + sum_{h at t=2} b_h(alpha)[S(L(h))+min(0,a_h)].

F(alpha) is the minimum **full-history downstream** cost with that LR-compatible first-stage schedule frozen. In each second-stage LR fiber G_r, put
A_r(alpha)=sum_{h in G_r:a_h>0} b_h(alpha)*a_h,
B_r(alpha)=sum_{h in G_r:a_h<0} b_h(alpha)*(-a_h),
D(alpha)=sum_r min(A_r(alpha), B_r(alpha)) >= 0.

Then for all signed real lambda, including arbitrary real local behavioral randomization,

V_LR(lambda)=min_{alpha in {0,1}^I} [F(alpha)+D(alpha)]

and

V_LR(lambda)-V_full(lambda)
  =min_{alpha in {0,1}^I} [(F(alpha)-V_full(lambda))+D(alpha)].

Thus **equality for this lambda** holds precisely when there is an LR-compatible pure early schedule alpha with F(alpha)=V_full and, on every reached t=2 LR fiber, A_r(alpha)=0 or B_r(alpha)=0. An unrealized collision with opposite hidden action advantages can be masked by optional early stopping.

**Proof.** The first compulsory unit of expected sampling time contributes l3+l4. Stopping at LR r chooses the cheaper of Q (error cost l1*r per Q mass) and P (l2 per Q mass), hence S(r). Continuing to t+1 adds c(r), possibly signed. At t=3 the Bayes-optimal classification is pointwise by terminal LR, hence H_h. A full-history choice at each t=2 h has cost S(r_h)+min(0,a_h), yielding F(alpha). A seedless LR choice on a fiber G_r must use a common continuation action, producing aggregated increment min(0,sum_h b_h a_h). Full history produces sum_h b_h min(0,a_h)=-B_r; the difference is min(0,A_r-B_r)+B_r=min(A_r,B_r). Summing fibers proves the fixed-alpha cost identity. For any fixed values of all but one local behavioral probability, the finite-tree objective is affine in that probability; a global minimum exists at a deterministic vertex of the finite product of action simplices. Thus optimizing alpha over {0,1}^I is exhaustive even with real randomization. Full-history t=1 actions have at least as much freedom, so F(alpha)>=V_full. Subtraction gives the exact nonnegative decomposition and the zero-gap criterion. QED.

The compulsory-arrival formula from the predecessor is therefore only a **conditional** time-2 gap, not a global gap formula in the presence of optional t=1 stopping.

## Theorem 2: exact 10-leaf rational model and all-price phase diagram

At t=1, observable histories A and B each have Q mass 1/2, P mass 1/2, LR 1. Conditional on either, t=2 has child labels C,L,H, Q transition probabilities (1/2,1/4,1/4), and LR (1,1/4,7/4). Their weighted LR mean is 1. At the common C state, t=3 has LR support Y=(1/4,1,7/4), with Q kernels
K_A=(2/5,1/5,2/5), K_B=(1/20,9/10,1/20).
At L or H the one final child retains its LR. Set every terminal P mass equal to LR times terminal Q mass. Exactly ten positive-probability terminal leaves result and P,Q each sum to 1.

For J_s=e_P+e_Q+s E_Q tau, s>=0, stop loss S(r)=min(r,1). The t=1-to-t=2 information gain is
b=1-[S(1)/2+S(1/4)/4+S(7/4)/4]=3/16.
Continuation at the common C fiber has advantages d_A=3/10, d_B=3/80, dbar=(d_A+d_B)/2=27/160. Exact backward induction yields

V_full(s)=1+s +(1/2)*sum_{h=A,B} min(0, s-b+(1/2)*min(0,s-d_h)),
V_LR(s)=1+s +min(0, s-b+(1/2)*min(0,s-dbar)).

Consequently, for **every real s>=0**, the gap G(s)=V_LR(s)-V_full(s) is

G(s)=0                                  for 0<=s<=3/80,
G(s)=(s-3/80)/4                        for 3/80<=s<=27/160,
G(s)=(3/10-s)/4                        for 27/160<=s<=3/16,
G(s)=27/160-3*s/4                      for 3/16<=s<=9/40,
G(s)=0                                  for s>=9/40.

These affine pieces follow by checking the signs inside the nested min operators. Endpoints match exactly; the **maximum gap** is 21/640 at s=27/160.

* Activated collision at s=1/16: every globally optimal strategy continues at t=1; the full-history optimum continues at common t=2 C after A, but stops after B. Seedless LR must share the C action. Exact minima: V_full=281/320 and V_LR=283/320, gap 1/160. With tie decisions set to P, witnesses are O_full=(7/80,13/20,9/4,9/4), O_LR=(29/320,51/80,5/2,5/2).
* Masked collision at s=1/4: the hypothetical common-state continuation advantages remain opposite, s-d_A<0<s-d_B, but both optimal policies stop at t=1. Thus V_full=V_LR=5/4 and O=(0,1,1,1). A latent kernel collision does not automatically yield a global gap.

This establishes both a **genuinely reached** t=2 collision with opposite optimal actions under voluntary t=1 stopping and a rigorously masked collision on the same ten-leaf tree. One-direction gap equality at s=1/4 is **not** equality of all signed support functions or actual four-observer sets.

## Evidence and scope

VERIFY.py, executed locally with fractions.Fraction, verifies all 10 positive leaf masses, P/Q normalization, LR conditional means, exact time/error observers, 256 full-history pure stop/continue descriptions and 16 seedless LR pure descriptions per price (with optimal terminal classification labels), both stated rational price witnesses, and 11 rational phase samples. EXACT_OUTPUT.txt is the captured execution output. The universal all-real-price formula is derived symbolically from the displayed Bellman min formulas, **not** inferred from 11 samples. Vertex optimality covers real randomized strategies for the signed-objective theorem.

There is a strict gap for some lambda, hence this model is *excluded* from the still-open stronger question conv(O_LR)=O_full but O_LR!=O_full. This is a finite external probability tree; no native Heartbeat/X6 physical law or infinite-horizon claim is inferred. See NEXT_TASK.md for the smallest unresolved step.