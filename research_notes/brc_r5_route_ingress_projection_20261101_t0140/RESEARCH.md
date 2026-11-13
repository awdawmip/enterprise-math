# R5: route-ingress refinement — exact 3-observer hull equality and 4-observer obstruction

Date: 2026-11-01 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is an auxiliary finite two-measure stopping-model theorem, NOT native BRC, X6, 3D-slice or empirical physics. The result remains subject to independent review.

## Frozen input and provenance

GLOBAL_KNOWLEDGE_V1 main@d61acce5599c5e6ceb33f5bd48f6b29e947bca06 and Enterprise Math main@993a408982a302265cb3c31f93e69e4751299500 were read and pinned. Global bootstrap, manual, P000 startup projection and ACTIVE worldview were read; P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched startup canonical_blob_sha1. Project current portable/autonomous research protocols and AGENTS were read. Neither P000 nor worldview was changed. Previous immutable author frontier: d728bd847995063174e89633c38f629fbb1be4bd, research_notes/brc_r5_all_sourceblind_complete_nogo_20261101_t0037/{RESEARCH.md,VERIFY.py,NEXT_TASK.md} (source-/route-blind response cube exclusion).

The current native gateway em_status reported research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED and active job quota 5/5. A bounded em_control_tasks active-owner query returned CONTROL_QUOTA. This does not establish an inactive owner. The author work here is portable, not an authorized native CLAIM, Result, or independent Driver review.

## Model and information keys

Retain the previous fixed P/Q compensated two-source stopping model: origin weights P=Q=1/2; (alpha0,kappa0)=(1/4,3/4); (alpha1,kappa1)=(1/5,1/6); theta_i=(1+kappa_i*(1-2alpha_i))/alpha_i=11/2. Source i continuing A reaches D,C,Y at time 2 with Q fractions alpha_i,1-2alpha_i,alpha_i and likelihood ratios 1/2,1,3/2. At D, CONTINUE reaches DH with Q fraction 2/3 (time 3, ratio 1/4) and L with fraction 1/3; at Y, CONTINUE reaches YH with fraction 1/2 (time 3, ratio 2) and L with fraction 1/2; C naturally stops with fraction 1-kappa_i or enters L with fraction kappa_i. L STOP occurs at time 3; L CONTINUE reaches L4 at time 4; all L/L4 leaves have likelihood ratio 1. A STOP time is 1. D/Y/C STOP time is 2. All natural probabilities are strictly positive.

NEW: retain the ingress provenance of the shared node L, splitting STOP leaves LD,LY,LC and CONTINUE leaves L4D,L4Y,L4C. LR still chooses ONE common L action and does NOT observe ingress. The 12 leaf Q-mass vector has order (A,D,Y,C,DH,YH,LD,LY,LC,L4D,L4Y,L4C); P mass equals each leaf Q mass times its stated likelihood ratio. FULL has 6 binary actions (A,D,Y,LD,LY,LC) per origin: 2^12=4096 corners. LR has shared binary (A,D,Y,L): 2^4=16 corners.

On every path each behavioral information key occurs at most once. Expected observations are multi-affine in action probabilities, thus each behavioral policy's observation is a convex combination of deterministic corners. Consequently every linear support maximum is attained at one deterministic corner, and the convex hull of real behavioral observations equals the finite deterministic polytope hull. This does not assert equality of the actual nonconvex behavioral images.

Let x=Q(DH), u=Q(YH), t=T_Q, y=Q(L4D)+Q(L4Y)+Q(L4C), c=Q(LC). These are positive route-flow readouts. Signed support coefficients below do not turn into negative transition mass.

## Theorem A: complete exact 3D hull equality

The convex hulls of the three-coordinate observer V3=(x,u,t) are EXACTLY EQUAL for FULL and LR.

Proof (finite exact certificate). The LR 3D affine rank is three, with vertex minor -2673/128000 for lexicographic binary LR indices (0,8,10,12). Enumerate all 16-choose-3 LR triples, form nondegenerate supporting hyperplanes by exact rational cross products, orient each against the LR vertices and primitive-integral-normalize. This yields exactly the following SEVEN facets n_x*x+n_u*u+n_t*t <= b:

    (-80,-120,40,99)
    (-1,0,0,0)
    (0,-1,0,0)
    (0,80,0,9)
    (3,26,-2,-2)
    (20,0,0,3)
    (39,8,-4,-4)

Every facet of a full-dimensional 3D polytope has three independent defining vertices, so the triple enumeration is complete; these seven halfspaces are its entire H-representation. Direct exact Fraction evaluation shows the maximum FULL slack is zero against EACH of these seven inequalities, over all 4096 FULL vertices. Therefore conv V3(FULL) is contained in conv V3(LR). The reverse inclusion is trivial because LR actions are a subset of FULL actions (choose the same actions for both sources and every ingress). By the multi-affinity lemma, this establishes convex-hull equality for ALL real behavioral policies. It does not establish equality of their actual nonconvex real images.

Additional exact rank computation on 12 route-labelled terminal mass coordinates gives affine rank FULL=7 and LR=6. This is an auxiliary flow-carrier rank; it is NOT a claim about native P000 spatial dimensions.

## Theorem B: legal rank-4 route-sensitive response still strictly separates

Set all terminal Bernoulli error probabilities r_j=1/2 except r_DH=5/8; r_L4D=r_L4Y=r_L4C=3/4; and r_LC=5/8. In particular, LC is distinguished by the OBSERVATION law but not by the LR ACTION key. These are all legal source-independent response probabilities in [0,1], while the error law now depends on the L ingress route.

With O=(e_P,e_Q,T_P,T_Q), the exact identities are

    e_Q-1/2=x/8+y/4+c/8
    e_P-1/2=x/32+y/4+c/8
    T_P-T_Q=u-3x/4.

Let s=y+c/2. The four observed coordinates are affinely invertible to (x,u,t,s):

    x=(32/3)*(e_Q-e_P)
    u=T_P-T_Q+(3/4)*x
    t=T_Q
    s=4*(e_Q-1/2)-x/2.

The LR affine 4D minor for vertex indices (0,8,9,10,12) is -513/256000 != 0. Thus the LR four-observation convex hull is genuinely full-dimensional.

For the signed reduced functional F=-21x-61u-19t+118s, exact enumeration of all 16 LR and 4096 FULL corners gives max_LR F=-19, max_FULL F=-27/2 and support gap exactly 11/2. A maximizing FULL action pair, represented in source0/source1 order (A,D,Y,LD,LY,LC), is 100001000000, giving (x,u,t,s)=(0,0,15/8,3/16), and

    O_FULL=(35/64,35/64,15/8,15/8).

Substituting the inverse map into F and clearing denominators yields an INTEGER OBSERVER SEPARATOR

    J=4024*e_P - 2608*e_Q - 183*T_P + 126*T_Q.

All real LR policies satisfy J<=651; the displayed FULL policy attains J=1335/2. The exact support gap is 33/2. In particular, the witness's L-infinity distance to the entire LR 4D convex hull is >= (33/2)/(4024+2608+183+126)=33/13882. Negative signed score coefficients never describe negative Q/P route flow.

This model has full LR 4D rank but FAILS hull equality. Theorem A shows the three-coordinate observer entirely loses the convex-hull discrepancy, yet the fourth ingress-sensitive observation reveals it. This is new information, not a resolution of the original four-dimensional mother question.

## Verification and remaining scope

VERIFY.py is a self-contained Python 3 stdlib Fraction program. It checks exact P=Q normalization for 4096 FULL and 16 LR corners; full/limited labelled-flow affine ranks; LR 3D rank and COMPLETE seven-facet enumeration; all 4096 FULL inclusions; rank-four LR minor; all 4112 affine observer identities and the integer separator; exact LR/FULL support maxima; and a displayed FULL witness. EXACT_OUTPUT.txt records the actual local run. The universal real-behavioral implications use multi-affinity; no floating point, finite-q extrapolation or ordinary sampling is used.

The theorem applies only to the declared fixed auxiliary topology, two source parameters, particular ingress-sensitive response and observation maps. It does not classify all route-sensitive response families, assert behavioral-image equality in 3D, show the desired rank-four hull equality plus real-image inequality, or establish physical X6 correspondence or typed BRC arithmetic. Adversarial independent verification and formal project admission are outstanding.

Next: classify the full real parameter q of projected observers (x,u,t,s_q=y+q*c), using exact piecewise-linear support envelopes and Farkas certificates. Determine whether ANY q allows rank-four equal FULL/LR hulls, or prove none do. For prospective equality require exact <=5 LR vertex combinations for every FULL vertex (or complete facet inclusion) and a nonzero rank-four minor. Only thereafter investigate strict real LR-behavioral image nonmembership.
