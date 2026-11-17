# R5 — K-source answer-vector rigidity on a maximal time-base face

Date: 2026-11-02 Asia/Shanghai.
Evidence status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Mother problem, source and scope

Mother target: a strictly positive finite two-law stopping model whose FULL and seedless LR four-observer convex hulls are equal but whose actual real-behavior observer images differ. This turn classifies the **answer-kernel-only** continuation in one fixed I→J→K time/action graph. It does not classify changed graphs.

Frozen SCIENTIFIC pins, unchanged: global knowledge a01383f825ef9d43b4b754254303298c64041568 and enterprise-math 86149263e38c22292c9def1e0f69092efa1be77e. Current normative rules were independently read on main. Predecessor theorem: enterprise-math@7988c1512cff94aefd25adbccd4886b58e56a0b4, research_notes/brc_r5_two_law_j_vector_rigidity_20261102_t1740/RESEARCH.md. P000 and ACTIVE worldview are unchanged. This is a source-labelled positive BRC probability-flow carrier; a native X6 physical realization is not asserted.

Connected GitHub user was awdawmip with push permission. Native active-owner query returned CONTROL_QUOTA; service stated research_authority_granted=false, executor_binding_configured=false and CODE_REVIEW_REQUIRED. This PR-branch research note is not a Source CLAIM, Result, independent review, or mathematical admission.

## Exact model and observer

The seven independent FULL real behavior parameters are x,jB,jI,kC,kI,kBJ,kIJ in [0,1]. Retain four labelled sources C,I,BJ,IJ:

    DB=(1-jB)/8; DI=(1-x)(1-jI)/8; D=DB+DI;
    w=(1/4,(1-x)/4,DB,DI);
    Cs=ws(1-ks); C=sum_s Cs.

At J suppose terminal answer probabilities are source-equal within each law: aB=aI=a under P, bB=bI=b under Q. At K the eight probabilities U_s and V_s are independent under P and Q. All a,b,U_s,V_s are in (0,1). Read out

    eP=1-aD-sum_s U_s Cs,
    eQ=bD+sum_s V_s Cs,
    TP=5/2-3x/4+2D+3C/2,
    TQ=5/2-3x/4+2D+4C/3.

LR requires jB=jI=y, kC=kI=kBJ=kIJ=z, with x,y,z real in [0,1]. Thus LR is a subset of FULL. Observer O=(eP,eQ,TP,TQ). Since each coordinate is multiaffine separately in the behavior variables, each entire real-behavior image is contained in the convex hull of its 128 or 8 deterministic vertex images. Hence support maxima over real behavior equal deterministic-vertex maxima.

## Exact all-real-parameter K rigidity theorem

Define positive weights m=(1/4,1/4,1/8,1/8), M=sum m=3/4, and means

    Ubar=(sum_s ms U_s)/M, Vbar=(sum_s ms V_s)/M.

Choose the two exact four-observer normals

    nP=(1,0,-32+6Ubar,36-6Ubar),
    nQ=(0,-1,-32+6Vbar,36-6Vbar).

For every strictly positive real parameter choice, the exact support identities are

    hLR(nP)=13-a/4,
    hFULL(nP)=13-a/4 + DeltaP,
    DeltaP=sum_s ms max(0,Ubar-U_s)
           =(1/2)sum_s ms abs(U_s-Ubar);

    hLR(nQ)=12-b/4,
    hFULL(nQ)=12-b/4 + DeltaQ,
    DeltaQ=sum_s ms max(0,Vbar-V_s)
           =(1/2)sum_s ms abs(V_s-Vbar).

Therefore, in this fixed graph with source-equal J vectors,

    conv O(FULL)=conv O(LR)
      iff U_C=U_I=U_BJ=U_IJ and V_C=V_I=V_BJ=V_IJ.

On the equality locus, the actual (not merely convexified) real-behavior observer images are equal.

Writing RU=max U_s-min U_s and RV=max V_s-min V_s, the one-sided Hausdorff distance in L-infinity obeys

    sup_{w in conv FULL} inf_{v in conv LR} ||w-v||_infinity
      >= max(DeltaP/(69-12Ubar), DeltaQ/(69-12Vbar))
      >= max(RU,RV)/1104.

All assertions are exact over the entire continuous parameter domain; rational examples below are checks and witnesses, not the basis of the universal result.

### Proof

Construct the observer-derived time statistics

    B=-8TP+9TQ=5/2-3x/4+2D,
    C=6(TP-TQ)=sum_s Cs.

Since D <= (2-x)/8, B <= 3-x <=3. Equality B=3 forces x=jB=jI=0. At this maximal exposed time-base face, the four source masses are precisely m_s and FULL can independently vary C_s through [0,m_s]. On the same LR face, C_s=t m_s for a single real t in [0,1].

For nP, its linear functional is LP=eP+Ubar*C+4B. On B=3,

    LP=13-a/4+sum_s(Ubar-U_s) C_s.

For LR the sum is zero for every common t because sum_s m_s(Ubar-U_s)=0. For FULL its maximum is 13-a/4+sum_s m_s max(0,Ubar-U_s), attained by selecting precisely those K sources with U_s<Ubar. Similarly nQ corresponds to LQ=-eQ+Vbar*C+4B, yielding on the face

    LQ=12-b/4+sum_s(Vbar-V_s) C_s.

Its LR and FULL face maxima differ by DeltaQ.

These are GLOBAL support maxima. At every deterministic FULL vertex outside B=3, one has B<=11/4. For every strategy, 0<=eP<=1, eQ>=0 and 0<=C<=3/4. Therefore at any such vertex,

    LP <= 1+3/4+4*(11/4)=51/4 < 13-a/4;
    LQ <=   3/4+4*(11/4)=47/4 < 12-b/4,

where the inequalities are strict because a,b<1. The same bounds hold for nonmaximal LR vertices. Multiaffinity upgrades vertex optimization to ALL real policies, proving the exact support formulas.

Because all m_s>0, the P gap vanishes exactly when all U_s equal their weighted mean, and likewise for V. This proves necessity of the two K vector equalities.

For sufficiency, suppose all U_s=U and V_s=V. For arbitrary FULL strategy define

    y=(jB+(1-x)jI)/(2-x),
    z=(sum_s ws ks)/(sum_s ws).

Both denominators are strictly positive, y,z lie in [0,1], and the corresponding LR (x,y,z) has exactly the same D and C as FULL. The four observations depend only on (x,D,C) on this locus; hence the actual real-behavior images are equal. Their convex hulls coincide.

For quantitative distances, the dual L1 norms of nP and nQ equal 69-12Ubar and 69-12Vbar. Dual norm separation yields the first inequality. For any positive m_s>=1/8, the two extreme kernel entries imply

    Delta=(1/2)sum_s ms abs(r_s-rbar) >= (max r_s-min r_s)/16.

Both normal norms are <=69, giving the uniform range lower bound. QED.

## Combined theorem: 12 answer parameters of the fixed graph

In the wider family with independent J answer probabilities (aB,aI,bB,bI) and independent K answer probabilities (U_s,V_s), the already saved predecessor theorem gives two exact support gaps |aB-aI|/16 and |bB-bI|/16 for explicit normals, irrespective of all K kernels. Thus convex equality FIRST forces aB=aI and bB=bI. The new theorem above THEN forces all K P entries equal and all K Q entries equal. Conversely these equalities give the explicit full real-policy aggregation. Therefore in this fixed I→J→K timing/action graph, with all 12 probabilities strictly inside (0,1), convex-hull equality holds iff every source has the same J vector (at its J node) and every source has the same K vector (at K); actual images then coincide. The predecessor is cited as an author-checked mathematical input; there is still no independent Driver admission.

## Geometric / BRC interpretation

The B=3 face retains the four source-labelled positive masses m_s. Its FULL image is a zonotope generated by the four vectors m_s(-U_s,V_s,3/2,4/3), while LR has only the diagonal segment generated by their sum. The P/Q weighted absolute deviations are exact transverse observer-residual certificates. Positive branch mass, source provenance, joint observers and their scope remain explicit. This is a restricted observer factorization result and makes no claim to native X6 physical dynamics.

## Exact verifier, witness and remaining target

Standalone VERIFY.py was ACTUALLY executed with standard-library Fraction. EXACT_OUTPUT.txt records PASS_EXACT_R5_K_SOURCE_VECTOR_RIGIDITY: 273 assertions; 8 strictly positive rational parameter cases; 1024 enumerated FULL vertices and 64 LR vertices; 72 nonbinary actual-behavior-to-LR aggregation tests on uniform-source cases. The universal parameter theorem is proved algebraically above. Case 0 has LR affine four-rank, with an exact 4x4 vertex-difference determinant -59821/135475200 for indices (1,2,3,4) relative to vertex 0.

For a=3/5, b=2/5, U=(1/4,2/3,5/8,3/7), V=(1/3,4/5,2/7,9/20):

    Ubar=485/1008; Vbar=1261/2520;
    DeltaP=173/2688; DeltaQ=151/2016;
    FULL P witness (411/560,23/96,57/16,7/2);
    FULL Q witness (1469/2240,185/672,15/4,11/3);
    dist_inf(P witness, conv LR)>=173/169952;
    dist_inf(Q witness, conv LR)>=755/634992.

No formal Lean proof, independent mathematical review, native X6 realization or empirical physical calibration was performed.

NEXT: change the graph rather than rerun the exact answer-only family. Jointly vary source-conditioned K TIME and answer kernels, or add an interacting decision key. Inspect the altered exposed-time face, and if a strictly positive rational candidate avoids the present obstruction, test all FULL vertices against exact LR mixtures or give rational Farkas separating normals; test actual real-behavior images only after hull equality. See NEXT_TASK.md.