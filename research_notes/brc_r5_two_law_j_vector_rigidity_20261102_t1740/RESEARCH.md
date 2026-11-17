# R5 — Two-law J-source vector rigidity under arbitrary K answer compensation

Date: 2026-11-02 Asia/Shanghai. Evidence status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Source and mother problem

Scientific predecessor: awdawmip/enterprise-math@82ee201bc5998f740517db81b9dc05eb5bf9ab92, research_notes/brc_r5_source_conditioned_j_bridge_20261102_t1640/RESEARCH.md and its exact verifier. Frozen science pins are unchanged: awdawmip/chatgpt-global-knowledge@a01383f825ef9d43b4b754254303298c64041568 and awdawmip/enterprise-math@86149263e38c22292c9def1e0f69092efa1be77e. Applicable rules from canonical main were read separately. P000 and ACTIVE worldview remain unchanged. This is a model-internal four-observer result; native X6 realization is a separate open bridge.

Mother objective: a strictly positive finite two-law stopping model where FULL and seedless likelihood-ratio (LR) have equal four-observer convex hulls but distinct actual real-behavior observer images. This unit tests whether fully independent P/Q K terminal answer kernels can compensate source differences at J.

## Exact source-labelled BRC carrier

Keep the preceding I→J→K stopping and time graph, including its positive P/Q K time kernels. For real FULL policies x,jB,jI,kC,kI,kBJ,kIJ in [0,1], use sources C,I,BJ,IJ and the exact positive masses

    DB=(1-jB)/8; DI=(1-x)(1-jI)/8; D=DB+DI;
    w=(1/4,(1-x)/4,DB,DI); Cs=ws(1-ks); C=sum_s Cs.

At J direct termination, answer Q has probability aB,aI under P and bB,bI under Q. At K continuation, answer Q has arbitrary *independent* source-specific probabilities uP_s and uQ_s. All 12 answer-kernel entries lie in (0,1). Four observations:

    eP=1-aB*DB-aI*DI-sum_s(uP_s*Cs)
    eQ=bB*DB+bI*DI+sum_s(uQ_s*Cs)
    TP=5/2-3*x/4+2*D+3*C/2
    TQ=5/2-3*x/4+2*D+4*C/3.

LR uses jB=jI=y and kC=kI=kBJ=kIJ=z, with x,y,z in [0,1]. Source identity is retained in the carrier, rather than erased by aggregating branches before the four-observer readout.

## Theorem — exact continuous-domain two-law J rigidity

For EVERY choice of strictly positive aB,aI,bB,bI,uP_s,uQ_s and EVERY real FULL/LR behavioral policy, define the signed support normals

    sP=aB+aI; nP=(1,0,-2*sP,9*sP/4);
    sQ=bB+bI; nQ=(0,-1,-2*sQ,9*sQ/4).

Then, for the support function h_A(n)=max{n·O(p):p in A},

    h_FULL(nP)-h_LR(nP)=|aB-aI|/16
    h_FULL(nQ)-h_LR(nQ)=|bB-bI|/16.

Thus four-observer convex-hull equality NECESSARILY implies the full source-conditioned two-law J vectors coincide:

    (aB,bB)=(aI,bI).

The conclusion holds with completely unrestricted K source-specific P/Q answer probabilities in (0,1): the K answer layer cannot cancel a J-vector defect while this time/action architecture is fixed. A quantitative lower bound for one-sided L∞ Hausdorff distance is

    d∞(conv FULL,conv LR) >= max(
      |aB-aI| / (16+68*(aB+aI)),
      |bB-bI| / (16+68*(bB+bI)) ).

**Proof (entire real parameter domain).** Fix L=P or Q. Let (rB,rI) be (aB,aI) or (bB,bI), let s=rB+rI>0, δ=rB-rI, η=s/4, and u_s the chosen law's K answer probabilities. Let n=nP or nQ, and c=n[0]+(5/2)*η. The time coefficients of n are (-8η,9η); they obey n3+n4=η and (3/2)n3+(4/3)n4=0. Substituting the four exact observer coordinates, the K time contribution cancels and gives

    n·O=c-3η*x/4 - (δ/2)*DB + (δ/2)*DI - sum_s(u_s*Cs).

All u_s Cs are nonnegative; DB<=1/8, DI<=(1-x)/8, x>=0. Consequently h_FULL(n)<=c+|δ|/16. Equality occurs at x=0 with all K stopping and with ONLY the J source having smaller r continuing; its D source mass is 1/8, the other is 0. Thus h_FULL(n)=c+|δ|/16.

For LR, DB=(1-y)/8 and DI=(1-x)(1-y)/8. Their sum in the displayed signed expression is -δ*x*(1-y)/16. Therefore

    n·O-c= -3*s*x/16-δ*x*(1-y)/16-sum_s(u_s*Cs)
          <= x*(|δ|-3s)/16 <=0,

because |δ|<=s with nonnegative rB,rI. Equality holds for x=0 and z=1. Hence h_LR(n)=c, proving both exact support gaps. Norm duality gives the stated distances because ||n||_1=1+17s/4. This proof covers the entire continuous cube of actual behavioral policies; vertex enumeration is an independent exact implementation check. QED.

## Temporal observer equivalence (an additional positive result)

For ANY FULL real strategy, define

    y=(jB+(1-x)*jI)/(2-x);
    z=(sum_s ws*ks)/(sum_s ws).

These lie in [0,1] and denominators are strictly positive. The LR strategy (x,y,z) has exactly the same D and C, hence the same actual (TP,TQ), regardless of the J and K P/Q answer kernels. Therefore the ACTUAL time-only observer images of FULL and LR are equal. Their joint four-observer hulls may still be separated by the preceding exact J normals. This is an observer-scoped factorization certificate and does not collapse the saved source flows.

## Strictly positive rational rank-four witness

Choose (aB,aI,bB,bI)=(3/5,7/20,2/5,3/4), uP=(1/4,2/3,5/8,3/7), uQ=(1/3,4/5,2/7,9/20).

P: nP=(1,0,-19/10,171/80). FULL witness WP=(153/160,3/32,11/4,11/4), hFULL=103/64, hLR=51/32, gap 1/64, distance >=5/1612.

Q: nQ=(0,-1,-23/10,207/80). FULL witness WQ=(37/40,1/20,11/4,11/4), hFULL=237/320, hLR=23/32, gap 7/320, distance >=7/1884.

An independently computed LR four-vertex affine determinant is -221119/541900800 and a FULL midpoint Jacobian minor for (x,jB,kC,kI) is -3857/29491200, both nonzero. This instance has full affine dimension four for LR and a four-dimensional open subset for FULL real behavior.

## Evidence, scope and next action

A standalone standard-library Fraction verifier (VERIFY.py) was actually executed for six rational source/kernel cases, all 128 FULL and 8 LR deterministic policies per case, 108 nonbinary exact temporal Markovization tests. Captured output EXACT_OUTPUT.txt ends PASS_EXACT_R5_TWO_LAW_J_VECTOR_PORTABLE 264 exact assertions. A separate expanded local verifier also passed 2041 exact assertions, checking independent terminal-path flow and four-dimensional determinants; the analytic proof above is the universal result.

Next: impose aB=aI and bB=bI, then classify the remaining eight source-specific K answer probabilities using exposed faces or exact 128-to-8 rational hull certificates/Farkas normals; if full signed hull equality arises, address actual-image nonmembership. An alternative genuinely changed time/action graph might support cancellation that this exact model rules out.

Authenticated GitHub user: awdawmip with repository push permission. Native service reports research_authority_granted=false and executor_binding_configured=false; live owner inventory returned CONTROL_QUOTA. This author-side PR artifact is not a CLAIM, Result, independent Driver review or mathematical admission. No credentials or changes to protected axioms/worldview.
