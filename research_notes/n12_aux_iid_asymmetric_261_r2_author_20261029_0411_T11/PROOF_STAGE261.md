# Stage261 — exact adjacent all-real Bellman face

2026-10-29. **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.** External finite ternary-IID auxiliary mathematics only. No native P000 X6 / Heartbeat physical correspondence, native CLAIM, Source Result, or independent Driver admission is claimed.

## Frozen inputs and provenance

GLOBAL_KNOWLEDGE_V1 current canonical read: main@d2d6fc3f8643da399ba72c0c2f0b39e4c55daa3e (00_BOOTSTRAP, OPERATING_MANUAL, Enterprise Math role router, P000 startup/original, ACTIVE worldview). P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc agrees with startup projection. Enterprise Math current control read: main@81e2b59eafd850eea03f7050b73a8526b67d5700 (AGENTS.md and current portable research protocol). Exact scientific predecessor: Stage260 immutable commit 0937cf8d239123d67da1d9d4c1ec495f263b2fd4, with inherited complete four-observer vectors C5, C12 and Stage261 task. Author scope: local researcher, NOT service-issued identity. Native owner inventory returned CONTROL_QUOTA; own native session creation was rejected STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Source capability reports research_authority_granted=false. GitHub author science storage does not grant Source control or amend P000.

## Exact model and theorem

P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon N=12. On arbitrary complete ordered observation histories, including randomized stopping and terminal decisions, let eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP=E_P(number of observations), tQ=E_Q(number of observations). Define V12(a,b) as min max(tP,tQ) subject to errors eP<=a, eQ<=b for any real a,b in [0,1], and +infinity if infeasible.

The exact Bellman dual parameters are

    lambdaP = 2985984/35755
    lambdaQ = 1922052/35755
    thetaP=0, thetaQ=1
    H = 1106067577/20594880.

Let R261 be the convex hull of the following five rational four-observer vectors, in counterclockwise error-plane order (each row lists eP,eQ,tP,tQ):

    D5:
    (1166286571/11609505792,3274031045/4353564672,
     2092263019/483729408,1774015963/362797056)
    D6:
    (1786693553/15479341056,4182329935/5804752896,
     3064528817/644972544,2580799409/483729408)
    E12:
    (23837991977/139314069504,10607552305/17414258688,
     35338509353/5804752896,9681835727/1451188224)
    C12:
    (25325973227/139314069504,10403158555/17414258688,
     34493690603/5804752896,9303029477/1451188224)
    C5:
    (1692824803/15479341056,4308598685/5804752896,
     2711460067/644972544,2260130659/483729408).

**All-real theorem.** For EVERY real (a,b) in [0,1]^2,

    V12(a,b) = H - lambdaP*a - lambdaQ*b
    if and only if (a,b) belongs to R261.

R261 is a strictly convex rational pentagon, with exact Euclidean parameter-plane area

    69108758447265625 / 101085468550861160448.

All Bellman-optimal deterministic policies and their randomized mixtures have tQ>tP on this face. Thus the time support remains entirely Q-side. This is a mathematical claim about the defined IID model, not a general statement about six-dimensional dynamics.

**Exact target and optimum.** Put

    a261 = 12662375697859/87071293440000
    b261 = 11664477305/17414258688.

Then

    V12(a261,b261)
      = 180113344229101789/32429521843200000
      ≈ 5.55399321334332.

An explicit optimal randomized policy samples, independently at the root, the deterministic policies C5, D5 and C12 with respective strictly positive weights

    wC5  = 64838811099718633/140932662207031250
    wD5  = 13060694016/349169921875
    wC12 = 14164453533437333/28186532441406250.

The three weights sum exactly to one, both errors saturate their caps, and the complete expected values are

    eP=a261,
    eQ=b261,
    tP=659238036620443201/129718087372800000,
    tQ=180113344229101789/32429521843200000,
    tQ-tP=570692586547/1209323520000 >0.

The target crosses Stage260's opposing edge by the exact amount

    2*a261+b261 =
      22312869149/23219011584 - 3/10000.

## Exact dual proof and all-history scope

For an ordered history h with counts s=(i,j,k), its two strictly positive source masses satisfy Q(h)/P(h)=L(s)=(2/3)^i * 2^j. With the value H(s) normalized by P(h), at each state the three Bellman action costs (third one legal only before depth 12) are

    decide P: lambdaQ*L(s)
    decide Q: lambdaP
    continue: L(s)+sum over z in {1,2,3} P[z]*H(s+unit_z).

The minimum is H(s). Exact backward induction gives H(0,0,0)=1106067577/20594880. For all complete-history stopping policies, including stochastic ones, backward induction yields

    tQ + lambdaP*eP + lambdaQ*eQ >= H,
    hence V12(a,b) >= H-lambdaP*a-lambdaQ*b.

The standalone Fraction checker computes the entire 455-state horizon-12 count DAG and all 1274 action costs; precisely 811 non-minimizing costs have strictly positive gap. There are exactly eight two-way ties, ordered by increasing total depth and count enumeration:

    (0,0,5),(0,0,6),(0,1,5),(0,0,7),
    (0,0,8),(0,0,9),(0,0,10),(0,0,11).

Every remaining state has exactly one minimizer. The ties are stop P/continue for the seven all-neutral states and stop Q/continue for (0,1,5).

The count quotient is sufficient for EXACTLY the four declared observers in this model. For each count s, aggregate all positive P-weighted incoming masses and action masses over histories of that count. For every such history the Q mass equals L(s) times P mass. Dividing the aggregated P mass choosing an action by aggregated visiting P mass gives legal count-state action probabilities (assign arbitrary actions at never-visited states). The resulting forward DAG preserves eP,eQ,tP,tQ under BOTH P and Q. Conversely every count-state policy is a full ordered-history policy. This is a proved limited quotient, not lossless compression of arbitrary future paths, joint relations or P000-native states.

A randomized count-state policy is a convex mixture of deterministic count-state policies by sampling one independent action per count state in advance. No count state can recur along a strictly increasing-depth history; expanding the finite product of action probabilities preserves the four observer totals. If the universal dual bound is attained, all visited actions must minimize the Bellman expression. Enumerating the 2^8=256 deterministic tie masks produces exactly 16 distinct (eP,eQ,tP,tQ) vectors, all satisfying

    tQ+lambdaP*eP+lambdaQ*eQ=H
    and tQ>tP.

An independent unmerged ordered-history DFS propagates separate positive rational P and Q masses for all 16 distinct policies. Across those runs, 7270 ordered nodes and 4852 terminal branches were visited. Every individual policy has total terminal P mass=1 and Q mass=1, and its four observations exactly match the suffix Bellman policy recurrence. The evidence is in the executed program and log attached to this same research directory.

An all-rational monotone-chain convex hull of the 16 vectors has exactly the five vertices above. Each of its five consecutive turn determinants is strictly positive; all 16 distinct points lie in/on that pentagon, and the exact shoelace area is the fraction above. All five vertices are achieved by actual Bellman-minimizing deterministic policies (the source prints their eight-bit masks). Every point in the hull therefore has a finite root mixture with exactly that error pair, tQ>tP, and equality to the dual bound. This proves sufficiency for all real error pairs, including irrational ones and edge points.

Conversely, the space of full ordered-history randomized action kernels is a finite product of compact simplexes. Errors and expected stopping times depend continuously on its finite coordinates. Every feasible infimum is thus attained. If a policy attains equality to the supporting affine bound with lambdaP>0 and lambdaQ>0, both error caps must be saturated and every positive-mass visited action must have zero Bellman slack. Its error pair is therefore in the 16-policy convex hull R261. This proves the necessity, without assuming rational caps or an a priori count-state policy. Infeasible pairs have value +infinity and cannot attain the finite affine value.

## Exact adjacency and representation-fidelity limit

Stage260's pentagon R260 has C5 and C12 as adjacent vertices with exactly the same full four-vectors. Stage260 lies on the >= side of

    2a+b = 22312869149/23219011584,

whereas the other THREE R261 vertices satisfy the strict < inequality, and its C5,C12 share equality. Thus R260 and R261 share their entire C5--C12 edge, their interiors are disjoint, and their source-labelled four-observer values agree at both endpoints and all convex mixtures along the common edge. No plotting, rounded equality or unordered-path count was used to infer adjacency.

Positive P and Q masses, ordered-branch multiplicity and exact four-observer quotient are compatible with the BRC provenance-preservation methodology, but this result neither executes native BRC-Shor dynamics nor supplies a P000 X6/three-dimensional-slice/heartbeat embedding. Physical and mathematical admission claims remain unchanged.

## Reproduction, evidence strength and next problem

The exact certificate is the actually executed standard-library Python source STAGE261_EXACT_FACE.py; executed SHA256 was 1801252463b0f0d38db4572131468769c45fc2900fa3e5756d56aedaa88b75b9. Run python3 STAGE261_EXACT_FACE.py. The run output ends STAGE261_EXACT_ALL_REAL_FACE_PASS. All 455 Bellman states, all 256 masks, the 16 independent full-history path propagations, rational hull, rational mixture and terminal conservation were asserted during execution. Exploratory floating-point HiGHS LP was used to discover candidate multipliers; it is NOT part of the mathematical certificate or final proof. External scientific novelty against literature has not been audited and no independent Driver review has occurred.

Stage262 should cross the new D5--D6 edge with exact caps

    a262=6259962086479/58047528960000,
    b262=25643113985/34828517376.

This is the error midpoint of D5,D6, shifted by -1/10000 in a; its exact D5→D6 oriented-area determinant is -878615/278628139008. Floating-point discovery indicates a feasible LP and V≈5.12101204416, but exact feasibility, matching dual, and all-real support are OPEN. See NEXT_TASK_PACKET_262.md for immutable inputs and acceptance conditions.
