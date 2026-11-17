# R5 — Exact compensation of the whole maximal-time source face, but a new mixed obstruction

Date: 2026-11-02 (Asia/Shanghai). Scope: strictly positive finite auxiliary two-law I→J→K stopping experiment. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Scientific lineage and frozen inputs

The mother target seeks equal four-observer FULL/seedless-LR convex hulls but different actual real-behavior images, preferably full-dimensional. This result does not solve it. Exact predecessor: enterprise-math@209f8b8502adc1900a55c65ee03b0e0f10ea4ef5:research_notes/brc_r5_k_source_vector_rigidity_20261102_t1840/RESEARCH.md (the fixed-time answer-only 12-parameter classification). Keep the scientific freeze global@a01383f825ef9d43b4b754254303298c64041568 and enterprise-math@86149263e38c22292c9def1e0f69092efa1be77e. Current behavioral rules were read separately from canonical main. P000/ACTIVE worldview remain unchanged. Source-labelled positive P/Q probability mass and provenance are the BRC carrier; no native X6 physics or physical probability calibration is claimed.

## Exact dual-law source-flow model

Behavioral parameters x,jB,jI,kC,kI,kBJ,kIJ independently range over [0,1] in FULL. Source order s=(C,I,BJ,IJ). Define

    DB=(1-jB)/8; DI=(1-x)(1-jI)/8; D=DB+DI;
    w=(1/4,(1-x)/4,DB,DI); Cs=ws*(1-ks).

At J the source-conditional P-answer probabilities are aB,aI and Q-answer probabilities bB,bI. At K, the answer probabilities under P,Q are U_s,V_s. A K-continued path also receives a binary terminal delay of either one additional unit (probability 1-p_s under P, 1-q_s under Q) or two units (p_s under P, q_s under Q), with no further behavior decision. All nature rates aB,aI,bB,bI,U_s,V_s,p_s,q_s are strictly in (0,1), and the K answer is independent of the last duration given source and law. This is a strictly positive realization of conditional time increments 1+p_s,1+q_s on the fixed original colliding-LR prefix.

    eP=1-aB*DB-aI*DI-sum_s U_s*Cs;
    eQ=bB*DB+bI*DI+sum_s V_s*Cs;
    base=5/2-3*x/4+2*(DB+DI);
    TP=base+sum_s(1+p_s)*Cs;
    TQ=base+sum_s(1+q_s)*Cs;
    O=(eP,eQ,TP,TQ).

LR imposes jB=jI=y and all ks=z, with real x,y,z∈[0,1]. Each path visits a given behavioral key at most once, so O is separately affine in each behavior parameter; a support maximum in any signed normal is attained on the 128 FULL or 8 LR deterministic corners. This finite endpoint reduction covers all real behavioral strategies.

## Theorem A — necessary and sufficient exact equality of the complete B=3 faces

Assume for every source the *time compensation* identity

    9(1+q_s)=8(1+p_s), equivalently q_s=(8*p_s-1)/9,

and require the resulting p_s,q_s strictly in (0,1). Then with B=-8TP+9TQ,

    B=base=5/2-3*x/4+2*(DB+DI) <= 3-x <=3.

Equality B=3 forces x=jB=jI=0. Here the four source masses m=(1/4,1/4,1/8,1/8) are strictly positive. Put v_s=(-U_s,V_s,1+p_s,1+q_s) and O0=(1-(aB+aI)/8,(bB+bI)/8,3,3). The **actual real-behavior** face images are exactly

    FULL_face=O0+sum_s [0,m_s]*v_s,
    LR_face=O0+[0,1]*(sum_s m_s*v_s).

Their complete four-coordinate images coincide **if and only if**

    U_s=κ(1+p_s), V_s=λ(1+p_s) for all s,

for two source-independent real constants κ,λ (with all rates remaining strictly positive).

Proof: If the zonotope equals the LR segment, each isolated generator m_s v_s (select only that source at K) must lie on this segment, hence each v_s is a positive scalar multiple of its total direction: all its TP entries are positive. Conversely collinear positive generators fill exactly the total segment. The assumed time identity already makes (1+q_s)/(1+p_s)=8/9, leaving precisely the two displayed ratios as necessary and sufficient. The exposed B bound and its equality case follow by DB≤1/8 and DI≤(1-x)/8, which give B≤3-x. This is an all-real continuous-parameter theorem, not a finite-sample inference.

Thus a whole source-labelled K zonotope can become an exactly matched LR segment even with nonconstant positive answer AND time kernels. The prior fixed-time maximal-face obstruction disappears **on this complete exposed face**. Whether the whole convex hull coincides remains a separate test.

## Strictly positive compensated full-rank witness family

Choose source order C,I,BJ,IJ:

    p=(1/4,1/3,1/2,2/3);
    q=(1/9,5/27,1/3,13/27);
    κ=2/5, λ=1/3;
    U=(1/2,8/15,3/5,2/3);
    V=(5/12,4/9,1/2,5/9);
    (aB,aI,bB,bI)=(3/5,1/2,2/5,1/2).

Every conditional nature rate is strictly between zero and one. Let R=Σ_s(1+p_s) Cs. Its maximal-face range is the complete interval [0,25/24], and

    O_face=O0+R*(-2/5,1/3,1,8/9).

A real LR policy matches every FULL face observer exactly by x=y=0 and z=1-R/(25/24).

For **all** strategies of this example,

    eP=1-(3/5)DB-(1/2)DI-(2/5)R;
    eQ=(2/5)DB+(1/2)DI+(1/3)R;
    TP=5/2-3*x/4+2*(DB+DI)+R;
    TQ=5/2-3*x/4+2*(DB+DI)+(8/9)R.

Its reduced linear Jacobian in (x,DB,DI,R) is -1/120. More generally on this compensated family that determinant is -(aB*bI-aI*bB)/12. The FULL real-image Jacobian minor in behavioral coordinates (x,jB,jI,kC) is

    (1-x)*(1+p_C)*(aB*bI-aI*bB)/3072,

which equals (1-x)/24576 in the concrete example. At strictly interior x=jB=jI=kC=kI=kBJ=kIJ=1/2 this minor equals **1/49152**, so FULL's actual real image contains a four-dimensional open set. The LR convex hull also has full four-rank: the 4x4 determinant of the LR vertex-difference rows at indices (1,2,4,6) relative to LR vertex 0 is **-5/36864**, where LR vertices are ordered lexicographically by bits (x,y,z).

## Theorem B — an exact all-real off-face separation

Despite entire B=3-face compensation and full four-dimensional rank, take the mixed normal

    n=(125,0,1806,-1854).

Then

    h_FULL(n)=1239/16, h_LR(n)=1221/16;
    h_FULL(n)-h_LR(n)=9/8>0.

A FULL deterministic witness (x,jB,jI,kC,kI,kBJ,kIJ)=(0,1,0,0,0,0,0) gives

    W=(143/240,25/72,173/48,379/108), n·W=1239/16.

**Complete all-real proof:** Substitution gives

    n·O = 5+36*x-171*DB-(317/2)*DI+108*R.

For fixed upstream actions, 108>0 and every coefficient of (1-ks) in R is nonnegative; thus both FULL and LR maximize K by setting all ks=0 (LR z=0). On that K choice,

    R=5/16+(1-x)/3+(3/2)DB+(5/3)DI,

and exactly

    n·O_maxK=299/4-9*DB+(43/2)*DI.

FULL can independently set DB=0, DI=1/8 by x=0,jB=1,jI=0, giving 1239/16. LR has DB=(1-y)/8, DI=(1-x)(1-y)/8, so

    n·O_maxK,LR=299/4+(1-y)*(25-43*x)/16 <=299/4+25/16=1221/16,

with equality at x=y=0. These maximizations hold for all real hazards; no numerical optimizer or unproved rounding assumption is used. Since ||n||_1=3785, the one-sided L-infinity distance from conv FULL to conv LR is at least

    (9/8)/3785 = 9/30280.

This is a **rejected mother candidate**. Crucially, its strict separation comes from a different mixed face, not from the fully cancelled old B=3 zonotope. The finite model supports genuine source-time compensation without convex equality.

## Verification and limits

The attached Python standard-library Fraction verifier was actually run and produced the recorded EXACT_OUTPUT.txt. It passed 349 exact assertions: positive kernels and ratio identities, all 128 FULL and 8 LR deterministic vertices, all 16 maximal FULL face vertices mapped to real LR strategies, support maxima, witness and distance, LR determinant, interior FULL Jacobian determinant and nine noncorner time-cancellation checks. Analytic proofs establish the all-real theorems; finite checks test arithmetic and coverage for this exact example. No Lean/formal proof, independent Driver review, official native Result/admission, native X6 realization or empirical calibration is claimed.

**Next:** keep source-labelled BRC mass and dual-law timing, classify other exposed faces in the full compensated family allowing independent J vectors. Seek exact rational all-128 FULL-to-8 LR convex mixtures (at most five terms by Carathéodory in R4), or an exact rational Farkas separator. If hull equality is actually proved, test actual real-policy image strictness with a polynomial nonmembership certificate. Else adjust a further interacting decision key. See NEXT_TASK.md.

**Authority:** author-side portable PR material only. Connected GitHub identity awdawmip has repo push permission; native service this turn reported research_authority_granted=false, executor_binding_configured=false and returned CONTROL_QUOTA for the active owner/task query. No CLAIM, Result, independent review, or admission is inferred. No credentials or private global knowledge source bodies are included.
