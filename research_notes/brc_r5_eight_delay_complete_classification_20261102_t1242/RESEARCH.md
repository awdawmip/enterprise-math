# R5 — Complete eight-delay classification from the upper answer exposed edge

Date: 2026-11-02, Asia/Shanghai. Scientific status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

Frozen scientific pins: GLOBAL_KNOWLEDGE_V1 main@a01383f825ef9d43b4b754254303298c64041568; Enterprise Math main@86149263e38c22292c9def1e0f69092efa1be77e. Behavioral rules use separately read current canonical main. Predecessor: Enterprise Math commit 39f37de5bfa005a6ad36ab9a649079b75eb837c1, research_notes/brc_r5_independent_pq_answer_edge_20261102_t1142/RESEARCH.md.

## Precisely defined two-law stopping model

Under each of the probability laws P and Q, initial mass 1/2 reaches decision I, mass 1/4 reaches J via B, and mass 1/4 reaches K via C. Stops at I,J,K answer P at times 1,2,3 respectively. Continuing I branches equally into J via I and K via I. Continuing J branches equally into a terminal time-3 answer, with probabilities P(answer P)=3/5 under P and Q(answer P)=2/5 under Q, and into K via BJ or IJ. Continuing K answers P with probability 1/2 and terminates at time 5 with source-conditioned probability p_s (under P) or q_s (under Q), otherwise at time 4. Sources s belong to S={C,I,BJ,IJ}. The eight parameters (p_s,q_s) range over all [0,1]^8; strictly positive time-4/5 branches hold for (0,1)^8. All source-labelled P/Q masses remain nonnegative.

The four-observer is O=(eP,eQ,TP,TQ), with eP=P(answer P), eQ=Q(answer Q), and expected terminal times TP,TQ. FULL allows real independent stop parameters (x,jB,jI,kC,kI,kBJ,kIJ) in [0,1]^7. LR restricts to (x,y,z) in [0,1]^3, setting jB=jI=y and all four k_s=z. The nonterminal shared decision keys are genuine (time,likelihood ratio)=(1,1),(2,1),(3,1). Each node is visited at most once per trajectory, so the observer maps are multi-affine; deterministic corners generate their observation convex hulls.

## Exact all-real classification theorem

For every real octuple (p_s,q_s) in [0,1]^8,

    conv O(FULL) = conv O(LR)
       if and only if
    p_C=p_I=p_BJ=p_IJ and q_C=q_I=q_BJ=q_IJ.

When those within-law equalities hold, the stronger *actual real-behaviour* identity is valid:

    O(FULL [0,1]^7) = O(LR [0,1]^3).

This completely classifies this eight-delay model class with respect to the proposed mother phenomenon.

### Necessity via the previously unused upper answer edge

For the eight deterministic LR vertices indexed xyz=000,001,010,011,100,101,110,111, the answer-coordinate sums eP+eQ are exactly

    (21/20,21/20,1,1,41/40,41/40,1,1).

The exposed face maximizing eP+eQ is therefore precisely the segment joining U0=O_LR(000) and U1=O_LR(001). An answer point strictly between its endpoints has a unique representation in conv O(LR) once the answer projection is fixed, namely the corresponding mixture of U0 and U1.

Now fix x=jB=jI=0. The source masses reaching K are the same under P and Q:

    m_C=1/4, m_I=1/4, m_BJ=1/8, m_IJ=1/8, M=sum m_s=3/4.

Define weighted means pbar=(sum_s m_s p_s)/M and qbar=(sum_s m_s q_s)/M. Direct nonnegative branch accounting gives

    U0=(21/40,21/40,15/4+M*pbar,15/4+M*qbar);
    U1=(9/10,3/20,3,3).

For each s, choose the FULL deterministic W_s with only k_s=1 and the other three K stop decisions zero. Stopping this single source moves (eP,eQ,TP,TQ) by

    (+m_s/2,-m_s/2,-m_s(1+p_s),-m_s(1+q_s))

relative to U0. Its answer projection is exactly that of the unique LR mixture

    V_s=U0+(m_s/M)(U1-U0).

Subtracting all four coordinates gives the *exact identity for every real parameter octuple*:

    W_s - V_s = (0,0,m_s(pbar-p_s),m_s(qbar-q_s)).      (1)

If conv FULL equalled conv LR, each W_s would have to lie in conv LR. Its exposed answer projection permits only V_s, so (1) must vanish. All m_s are strictly positive; hence p_s=pbar and q_s=qbar for all four sources. These are precisely the two sets of source-independence equations. This necessity argument covers [0,1]^8 directly, without sample extrapolation.

### Sufficiency via explicit simultaneous P/Q probability-flow aggregation

Suppose all p_s=p and all q_s=q, allowing p and q to differ. For any real FULL policy retain x. The total J arrival mass under both P and Q is aJ=(2-x)/4>0. Set

    y=(jB/4+(1-x)*jI/4)/aJ.

This matches the total J stop and continue mass simultaneously in both laws. FULL source masses at K under both laws are

    wC=1/4, wI=(1-x)/4, wBJ=(1-jB)/8, wIJ=(1-x)(1-jI)/8.

Set aK=wC+wI+wBJ+wIJ>0 and

    z=(wC*kC+wI*kI+wBJ*kBJ+wIJ*kIJ)/aK.

Then LR (x,y,z) matches aggregated stop/continue flows at I,J,K under both laws. The answer/time kernel at J is key-dependent but source-independent; the time law at K is also source-independent within P and within Q. Therefore the four observer components agree exactly. Both y and z belong to [0,1]. The reverse image inclusion is automatic because LR is a FULL policy subclass; this proves equality of actual real-behaviour images and of their convex hulls.

### Quantitative global separation certificate

Let

    R = max( max_s p_s - min_s p_s, max_s q_s - min_s q_s ).

If R>0 choose a law d in {p,q} attaining range R and a source s such that |d_s-dbar| >= R/2. Such a source exists because dbar is a weighted mean. Define sigma=sign(dbar-d_s), u=2(1+dbar) in [2,4], and A=400. Set the rational-or-real signed normal

    N=(A+sigma*u,A,sigma,0)  if d=p,
    N=(A+sigma*u,A,0,sigma)  if d=q.

This normal ties U0 and U1. Every other deterministic LR vertex has answer sum <=41/40, hence loses >=A/40=10 in the A(eP+eQ) component relative to the exposed face. Since 0<=eP<=1, 1<=T_P,T_Q<=5 and u<=4, the remaining term sigma*(u*eP+T_law) varies by no more than 8. Therefore U0,U1 alone maximize N on LR, for every parameter octuple. Formula (1) gives

    N.W_s - h_LR(N) = m_s*|dbar-d_s| >= R/16

because m_s>=1/8. The dual norm satisfies ||N||_1<=805. Consequently

    sup_{w in conv FULL} dist_infinity(w,conv LR) >= R/12880.     (2)

This is an explicit all-real one-sided Hausdorff distance lower bound. No optimality assertion is made.

## Strictly positive rational witness

Take P source time-5 probabilities (p_C,p_I,p_BJ,p_IJ)=(1/4,1/2,2/3,1/3), and Q source probabilities all 1/3. Then pbar=5/12, qbar=1/3 and

    U0=(21/40,21/40,65/16,4)
    U1=(9/10,3/20,3,3)
    W_C=(13/20,2/5,15/4,11/3).

The exact signed support normal N=(2417/6,400,1,0) has h_LR(N)=8511/20 and N.W_C-h_LR(N)=1/24. Thus W_C is outside the entire LR four-observer convex hull and

    dist_infinity(W_C,conv LR) >= (1/24)/(4823/6) = 1/19292.

Every natural terminal time split has strictly positive P and Q branch probability in this witness.

## Evidence, limits, authority and continuation

The saved standalone Python standard-library Fraction VERIFY.py was actually executed; its captured EXACT_OUTPUT.txt terminates with PASS_EXACT_R5_EIGHT_SOURCE_FIBER_GLOBAL_CLASSIFICATION and records 1812 exact assertions. Tests include all eight LR answer sums, the exact witness and its normal support over all eight LR vertices, four exact source-fiber lift identities for the witness, 50 independently generated rational parameter octuples with 400 source/law lift-and-support checks, and 100 noncorner rational FULL->LR Markovization regressions. The all-real theorem is proved above algebraically; finite tests are independent regressions.

This theorem is about the specified auxiliary dual-law stopping graph. Its observational geometry has not been promoted to native X6/P000 realization. P000 and the protected ACTIVE worldview were consulted and are unchanged. The current authenticated GitHub connector identity is awdawmip with repository push permission. The native gateway reported research_authority_granted=false, and current owner inventory returned CONTROL_QUOTA. Hence the author-side result has no authenticated native Owner/CLAIM/Result/independent Driver-review or mathematical admission receipt.

Next: alter the conditional K answer kernel or add a coupled decision to break the isolated LR 000<->001 answer exposed edge, preserving genuine shared time-likelihood-ratio keys and nonnegative labelled P/Q path probabilities. For each genuinely new class test every FULL deterministic four-vector against the LR convex hull with exact rational <=5-vertex combinations, or give an exact Farkas separator. On all-signed convex-hull equality, use a full-rank Jacobian plus a real-image nonmembership certificate. The eight-delay class is complete as an auxiliary model, and the original mother problem remains open.