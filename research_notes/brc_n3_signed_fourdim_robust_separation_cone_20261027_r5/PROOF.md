# R5 — Four-dimensional signed Bellman separation cone (N=3)

2026-10-27. Author-level portable finite BRC research, **UNREVIEWED / NOT_ADMITTED**. No native CLAIM, Result, independent Driver review or native X6/Heartbeat physical inference. Current native task owner query failed with CONTROL_QUOTA.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@f9f5620c6fa2b9cfff8b49551878080e158a98d9; Enterprise Math main@f8fcea6dd1783b578aaf434aac68b7a1388e49d6. Read project router, P000 V4, ACTIVE worldview, BRC priority, joint-observer preservation, native six-axis/time typing and docs/PORTABLE_RESEARCH_PROTOCOL.md. This work extends the verified optional-early-stop model in research_notes/brc_n3_optional_early_stop_activation_masking_20261027_r5; its price-axis diagram is not repeated as a new result. P000 and protected worldview are unchanged.

## Model and exact observables

Finite strictly positive two-measure tree P,Q, with optional stop and decision P/Q at t=1,2 and compulsory decision at t=3. For policy pi,

    O(pi) = (P(decide Q), Q(decide P), E_P tau, E_Q tau).

Full-history behavioral policies may depend on labels. Seedless LR behavioral policies depend only on (t,L), L=P(h)/Q(h), with real local randomness but no persistent seed. Minimize lambda dot O for any signed real lambda=(a,b,u,v).

At t=1, two labels A,B each have Q=P=1/2, L=1. At t=2, from either parent, Q conditional probabilities of C,L,H are (1/2,1/4,1/4), and their likelihood ratios are (1,1/4,7/4). At C, terminal LR is Y=(1/4,1,7/4) with Q conditional distributions K_A=(2/5,1/5,2/5) and K_B=(1/20,9/10,1/20). At L/H the sole terminal child preserves its LR. Terminal P mass is terminal LR times terminal Q mass. All ten leaves are strictly positive and both measures total one. The hidden predecessor at the common C likelihood ratio has different future kernels: this is a typed structural residual, not a numerical-roundoff effect.

## Theorem: explicit OPEN FOUR-DIMENSIONAL signed cone

Set D=4b-a, c=u+v, c_L=u/4+v, c_H=7u/4+v. Consider the strict rational polyhedral cone C in R^4:

    a>0; a/4<b<a; c_L>0; c_H>0; D/80<c<9D/160.       (C)

For EVERY real lambda in C, including arbitrary real local behavioral randomization:

1. At t=1, A and B both continue in the full-history model; their pooled LR state also continues. All L and H histories stop at t=2. Full-history A-C continues, B-C stops, while the pooled seedless LR C state continues. At stop/terminal nodes, decide Q if LR=1/4 and P if LR=1 or 7/4. Every listed decision comparison is strict.
2. The exact global minimizing observer vectors are

    O_full = (7/80,13/20,9/4,9/4),
    O_LR   = (29/320,51/80,5/2,5/2).

3. Their global Bellman support-value gap is

    V_LR(lambda)-V_full(lambda) = c/4-D/320 = (c-D/80)/4 > 0.       (G)

Thus the earlier one-dimensional nonnegative sample-price gap extends to a nonempty *open full-dimensional signed objective cone*. It contains lambda*=(1,63/64,0,1/16), lambda-=(1,63/64,-1/128,9/128) with negative u, and lambda-Q=(1,63/64,1/10,-1/50) with negative v. Both sampling-time coefficients are genuinely allowed to have either sign on different parts of C.

## Proof, including optional early stopping

Under a/4<b<a and a>0, the terminal/stop decision minimizing a*P(error Q)+b*Q(error P) costs S(1/4)=a/4 and S(1)=S(7/4)=b per unit Q mass, strictly. An extra sample at current LR r costs c(r)=u*r+v. At L/H, further sampling gives no information, so c_L,c_H>0 imply strict stop.

At C, conditional optimal terminal decision losses are

    H_A = a/10+3b/5,     H_B=a/80+19b/20.

Their sampling benefits excluding the extra time cost are

    d_A=b-H_A=D/10,     d_B=b-H_B=D/80,
    d_bar=(d_A+d_B)/2=9D/160.

Condition (C) gives d_B<c<d_bar<d_A. Hence full-history continues at A-C but stops at B-C, whereas the compressed LR state continues at both. Since all decisions at t=3 are pointwise optimal, there is no other terminal optimization degree of freedom.

The crucial early-stop check is as follows. Exclude the unavoidable first sampling cost c and calculate subsequent conditional costs T_A,T_B when continuing from the respective first-stage histories:

    T_A=c+(1/2)(c+H_A)+(1/4)(a/4)+(1/4)b
       =(3/2)c+(9/80)a+(11/20)b.

    T_B=c+(1/2)b+(1/4)(a/4)+(1/4)b
       =c+a/16+(3/4)b.

Stopping at the first-stage LR=1 would instead cost b. However,

    b-T_A=9D/80-(3/2)c > 9D/320 >0,
    b-T_B=D/16-c > D/160 >0.

Thus both full-history first-stage histories continue strictly. For the seedless strategy, pooled C continuation and the same L/H stops yield

    T_LR=(3/2)c+(29/320)a+(51/80)b,
    b-T_LR=29D/320-(3/2)c>D/160>0.

Hence its pooled first-stage LR state continues strictly too; early-stop masking is ruled out throughout C.

Positive Q branch accounting now gives the observer vectors. For full-history, the only Q classifications occur at t=2 L, with total Q mass 1/4 and P mass 1/16, and at t=3 low-LR after A-C, whose Q mass is 1/10 and P mass 1/40. Hence eP_full=7/80 and eQ_full=1-1/4-1/10=13/20. The compressed strategy also samples B-C: this adds low-LR Q mass 1/80 and P error mass 1/320. Thus eP_LR=29/320 and eQ_LR=51/80. All paths reach t=2. At t=2, full-history continues Q and P mass 1/4 after A-C; LR continues mass 1/2 after both C nodes; consequently time expectations are 9/4 and 5/2 respectively for both measures.

Subtracting yields

    O_LR-O_full=(1/320,-1/80,1/4,1/4),

so the signed dot product is a/320-b/80+(u+v)/4=c/4-D/320>0. These are *global* minima: all backward induction action comparisons are strict and the finite-tree randomized objective is multiaffine in local independent action probabilities, hence achieves its minimum at a deterministic behavioral vertex. This proves the theorem for ALL real local probabilities and signed weights in C. QED.

## Exact verification and scope

Locally executed VERIFY.py uses only Python Fraction, constructs all ten positive leaves, checks probability and LR-martingale conservation, independently performs Bellman minimization over stop-versus-continue actions and classifications, checks the exact optimal four-vectors and gap at three signed witnesses and 48 additional rational chamber points. EXACT_OUTPUT.txt captures the actual run. A second local execution gave a byte-identical output. These finite tests are corroboration, NOT the universal proof; the displayed strict linear inequalities prove the all-real cone statement.

At lambda*, V_full=1111/1280, V_LR=4477/5120, gap=33/5120. With lambda-Q, gap=277/25600. The lower boundary c=D/80 is a tie at B-C and is not claimed to belong to the strict cone.

This result **rejects this ten-leaf tree** as a solution to the stronger still-open problem conv(O_seedless)=O_full but O_seedless != O_full, because it already has strict support gap on a whole cone. We have not certified all of R^4, all other N=3 models, real semialgebraic nonmembership, or an X6/Heartbeat embedding. No P000, research-admission, Working Truth or Foundation status is changed. See NEXT_TASK.md.
