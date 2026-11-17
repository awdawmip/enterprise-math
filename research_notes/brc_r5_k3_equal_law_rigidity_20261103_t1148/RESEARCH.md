# R5: complete K3 equal-law source rigidity by a signed threshold family

Date: 2026-11-03 Asia/Shanghai.
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Provenance and exact model
Mother objective: find a genuine finite two-law P/Q stopping experiment whose FULL-history and seedless LR four-observer convex hulls agree but whose actual real-behavior four-observer images differ. Previous all-signed K3 oracle and positive BRC flow: enterprise-math commit 2c47ed2096e2cbdc1b5bbd88291dc8583d9f72de, research_notes/brc_r5_k3_all_signed_fiber_20261103_t1040/RESEARCH.md. Original K3 topology: commit 9bcdb1337dbe9d7b05e99010e0a2a55edce59524.
Frozen science input pins unchanged: global a01383f825ef9d43b4b754254303298c64041568, Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current separate normative reads: global main 06a22a838421cf6958fac956ae676b30b0bba59c, EM main 6e566d86091cd675165e316e850574feb6720dd6. This is a typed four-observer auxiliary, not a native X6 physical-calibration claim.

Sources s=(C,I,BJ,IJ), alpha=(1/2,2/3,1/2,3/4).
FULL upstream: real 0<=x,y,i<=1 and x+i<=1. Seedless LR upstream: i=(1-x)y.
Positive source masses w=(1/4,(1-x)/4,y/8,i/8); d=y/16+3i/32.
M_s=w_s alpha_s z_s, S_s=(2/3)M_s t_s, U_s=S_s u_s.
FULL has independent sourcewise z_s,t_s,u_s in [0,1]; LR has a common z,t,u.
K3 at time 5 has likelihood ratio 4. Its P and Q delay Bernoulli probabilities both equal r_s with 0<r_s<1, including strictly positive complements.
The exact four observers are:

    eP=107/128-21x/128+d/4-(sum S_s)/2
    eQ=13/64+3x/64-d/2+(sum S_s)/8
    TP=3+sum M_s+(3/2)sum S_s+sum r_s U_s
    TQ=3+(1/2)sum M_s+(3/8)sum S_s+(1/4)sum r_s U_s.

All source weights and pre-observer BRC carrier flows remain nonnegative and source-labelled.

## Theorem (all real r in (0,1)^4 and all real behavior controls)
Write c=(1/8,1/6,1/16,3/32), t any real in (0,1), and n(t)=(0,-12-8t,2,-4). The exact signed support gap is

    h_FULL(n(t))-h_LR(n(t))
      =(2/3) min{sum_s c_s max(r_s-t,0), sum_s c_s max(t-r_s,0)}.       (1)

Hence the FULL and LR four-observer convex hulls coincide if and only if r_C=r_I=r_BJ=r_IJ. For uniform r_s=r0, even the actual real behavioral four-observer sets coincide: O(FULL)=O(LR). Thus this whole continuous four-parameter equal-P/Q K3 delay family is classified.

## Proof of exact threshold gap
For the previous all-signed K3 formula set A=0, B=-L, C=2, D=-4, L=12+8t. The Bellman coefficients K=C+D/2=0, H=-A/2+B/8+3C/2+3D/8=-t, and J_s=Cr_s+D r_s/4=r_s.
Thus each FULL source envelope is

    F_s=max(0,K,K+(2/3)H,K+(2/3)(H+J_s))
       =(2/3)max(r_s-t,0).

Its upstream baseline B(x,y,i)=-6-L(13/64+3x/64-d/2) increases in y and i and decreases in x. All F_s are nonnegative; the four source weights w_s alpha_s increase or remain fixed when moving toward (x,y,i)=(0,1,1). This feasible prism corner therefore maximizes the FULL support. At it c_s=w_s alpha_s and B_*=B(0,1,1). Hence h_FULL=B_*+(2/3)sum c_s (r_s-t)_+.

For LR, only two relevant Bellman alternatives remain: the baseline B(x,y,(1-x)y), and B plus

    R(x,y)=(2/3)sum c_s(x,y)(r_s-t),
    c(x,y)=(1/8,(1-x)/6,y/16,3(1-x)y/32).

The other two alternatives give 0 and a negative value -(2/3)t sum c_s(x,y). Both B and B+R attain their global maxima at (x,y)=(0,1). Indeed d=y(5-3x)/32 implies

    partial_x B=-3L(1+y)/64 <= -9/16,
    partial_y B=L(5-3x)/64 >= 3/8,
    partial_x R <= (2/3)(1/6+3/32)=25/144,
    partial_y R >= -(2/3)(1/16+3/32)=-5/48,

using 0<r_s,t<1. Hence B and B+R are strictly decreasing in x and strictly increasing in y. Consequently

    h_LR=B_*+(2/3)max(0,sum_s c_s(r_s-t)).

Set P=sum c_s(r_s-t)_+, N=sum c_s(t-r_s)_+. Since sum c_s(r_s-t)=P-N, subtracting yields (2/3)[P-max(0,P-N)]=(2/3)min(P,N). This completes the optimization for every real behavior strategy and proves (1).

## Proof of the classification and actual-image equality
Every c_s is strictly positive. If r is not constant, choose real t strictly between min_s r_s and max_s r_s. Then P>0 and N>0; (1) gives strict four-dimensional support separation.

For the uniform case r_s=r0, consider arbitrary FULL controls and retain x, d=y/16+3i/32. Define a legal LR upstream

    y'=32d/(5-3x),   i'=(1-x)y'.

The prism constraints imply 0<=d<=(5-3x)/32, so 0<=y'<=1. Both upstream descriptions have the same x and d, and therefore the same total available M-carrier

    T=sum_s w_s alpha_s=1/8+(1-x)/6+d > 0.

Let M=sum M_s, S=sum S_s, U=sum U_s, and choose common LR

    z=M/T,
    t_gate=3S/(2M) when M>0, else 0,
    u=U/S when S>0, else 0.

The bounds 0<=U<=S<=(2/3)M<=(2/3)T make these valid [0,1] controls. They exactly reproduce M,S,U. For uniform r0 the four observers depend on source gates only through these three sums, and on upstream only through x,d. Thus every FULL real observation is realized by LR. Conversely every LR policy is a FULL policy, so the actual images coincide.

## Exact rational witness and distance
Take r=v=(1/4,1/2,3/4,1/2), threshold t=1/2, n=(0,-16,2,-4).
P=1/64, N=1/32; h_FULL=-767/96, h_LR=-8 and gap=1/96.
The FULL policy x=0,y=i=1, BJ only (z=t_gate=u=1), all other source gates off, realizes

    W=(41/48,25/192,101/32,391/128).

Then n.W=h_FULL; ||n||_1=22, so for all LR observers and all points of their convex hull,

    ||W-V||_infinity >= (h_FULL-h_LR)/||n||_1 = 1/2112.

This provides a genuine positive-probability four-dimensional separation inside a family with identical P/Q K3 delay probabilities at each source.

## Verification and exact scope
The accompanying Python standard-library Fraction verifier enumerates all observer-distinct deterministic triples per source: OFF, z-only, z=t_gate, z=t_gate=u. Each of the eight Boolean triples is observer-equivalent to one of these four. Thus the complete distinct deterministic sets have 6*4^4=1536 FULL and 4*4=16 LR observation vectors per rational kernel. Three positive rational kernels and seven threshold values yield 21 independently enumerated support-pair checks, plus exact witness and distance assertions. Execution result: PASS_EXACT_R5_K3_PROPORTIONAL_EQUAL_LAW_RIGIDITY. The continuous parameter theorem is established by the analytic proof above; the finite enumeration independently cross-checks rational instances.

## Next research question
Classify proportional two-law K3 kernels v_s=lambda*r_s, lambda>0, all r_s and lambda*r_s in (0,1). For lambda !=2 search a threshold signed family with K=0 and J_s proportional to r_s, proving its upstream maximizer conditions. For lambda=2 this family becomes degenerate and a different signed direction may distinguish sources. Apply the exact full-hull/Farkas method to surviving candidates, then test actual-image nonmembership only after a complete hull equality certificate. All P000, ACTIVE worldview, frozen science pins, and native review requirements remain in force.
