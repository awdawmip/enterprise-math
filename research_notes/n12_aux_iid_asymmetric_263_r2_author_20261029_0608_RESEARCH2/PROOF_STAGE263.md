# Stage263: an exact four-vertex all-real optimality face beyond R262

**Research scope / provenance (2026-10-29).** Author-side external ternary IID sequential testing; status **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. Predecessor: immutable Stage262 author proof, executed script, stdout and task packet at Enterprise Math PR #1571 commit f1741edbe9ca2fa3c646603dc9c52bbf61061018. Reuse the existing Stage262 F5,F6 vectors. The analysis is conditional on this finite probabilistic model, not a P000-native theorem or a physical-law claim.

## 1. Exact statement and original target

Observations in the alphabet {0,1,2} are IID with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). At each complete **ordered** history a randomized rule decides P, decides Q, or (when fewer than twelve symbols have been observed) continues. Every rule stops by depth 12. Its four observables are eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP=E_P(length), tQ=E_Q(length). Write V12(a,b) for the minimum of max(tP,tQ) under eP≤a and eQ≤b, taking +∞ when infeasible.

The Stage263 exact caps are

    a=1443791791151/14511882240000,
    b=6493321465/8707129344.

**Theorem 263A.** Among all such full-ordered-history randomized rules,

    V12(a,b)=1313484313680967/247155494400000
            ≈5.314404670102981.

The dual coefficients and root value are

    lambdaP=47156/545, lambdaQ=60111/1090,
    (thetaP,thetaQ)=(0,1), H=89584701487/1627361280.

Thus for every feasible pair of real error caps (a,b),

    V12(a,b) >= H-lambdaP*a-lambdaQ*b.

## 2. The four exact equality vectors and primal witness

In each row below, entries are precisely (eP,eQ,tP,tQ), not rounded estimates.

    F5 / mask 00:
    (4312568159/46438023168,13246202305/17414258688,
     8556473951/1934917632,7350985727/1451188224)

    F6 / mask 01:
    (182851367/1719926784,471373465/644972544,
     348833063/71663616,298085351/53747712)

    G5 / mask 10:
    (668435839/7739670528,2229900905/2902376448,
     1450753471/322486272,1259213767/241864704)

    G6 / mask 11:
    (1524881053/15479341056,4295642435/5804752896,
     3198716317/644972544,2764486909/483729408)

To interpret mask bits, use the **ordered** tied count states (0,1,7) with actions [decide Q,continue] and (0,0,5) with actions [decide P,continue]; bits 0/1 select the first/second action. At all other count states use the unique minimum-cost Bellman action. The vectors F5,F6 agree in all four entries with the existing Stage262 F5,F6, not merely their error coordinates. They and the two new vectors are pairwise distinct.

At the initial state, independently sample the deterministic strategies F5,F6,G5 with the following strictly positive rational probabilities, respectively:

    wF5=122100138041/266113281250
    wF6=1082351533/2128906250
    wG5=4359600792/133056640625.

The exact sum is one. Expanding the mixture gives

    eP=a; eQ=b;
    tP=1532741199372751/329540659200000;
    tQ=1313484313680967/247155494400000;
    tQ-tP=1203144324047/1813985280000>0.

Each of the four deterministic policies satisfies tQ+lambdaP*eP+lambdaQ*eQ=H. In particular the displayed mixture makes tQ equal to the global dual lower bound, and tQ=max(tP,tQ). This proves Theorem 263A, including exact feasibility.

## 3. Entire all-real face and precise Stage262 adjacency

Define R263 as the convex hull of the first two coordinates of **F5,G5,G6,F6**, taken in that counterclockwise order. This is a strictly convex rational quadrilateral, of exact area

    area(R263)=1463623046875/14624633760251904.

The four consecutive oriented corner determinants, again in that order, are

    665283203125/7312316880125952,
    133056640625/1218719480020992,
    133056640625/1218719480020992,
    665283203125/7312316880125952,

all positive.

**Theorem 263B (all real parameters).** For every real (a,b) in [0,1]^2, including irrational caps and infeasible boundary pairs,

    V12(a,b)=H-lambdaP*a-lambdaQ*b
    if and only if (a,b) lies in R263.

Moreover, the intersection between R262=conv(D5,F5,F6,D6) from Stage262 and R263 is exactly their entire closed F5--F6 segment; they have no overlapping interiors. Writing orient(U,V,W) for the signed 2x2 determinant of V-U,W-U, the two new vertices G5,G6 lie strictly on the negative side of F5→F6, whereas the old D5,D6 lie strictly on its positive side. Both convex polygons contain that full segment as a boundary edge. The signs prove the exact intersection without a numerical tolerance. The Stage263 cap pair is outside R262 by the exact witness

    orient(F5,F6,(a,b))=-415295/139314069504<0,

and inside R263 by the positive mixture in §2.

## 4. Global Bellman argument on complete ordered histories

For *each* ordered history h of counts (i,j,k), strict positivity gives the likelihood ratio L(s)=Q(h)/P(h)=(2/3)^i*2^j. Under cost tQ+lambdaP*eP+lambdaQ*eQ, normalize the future value at h by P(h). Stopping with decision P costs lambdaQ*L(s); stopping with decision Q costs lambdaP; continuing, when |s|<12, costs

    L(s) + sum_{z=0}^2 P(z) H(s+unit_z).

The Bellman value H(s) is the exact minimum of all legal costs with terminal boundary at |s|=12. Because all three expressions depend only on the counts, the recursion applies to every individual ordered word, including paths that share counts without sharing order.

The attached executed standard-library Fraction certificate verifies *all* 455 count states and 1,274 legal action values. Their backward recursion has H(0,0,0)=89584701487/1627361280; exactly two two-way ties, at the states listed in §2; and 817 strictly positive nonminimizer action gaps, minimum 125/20928. Summing Bellman inequalities over the complete history tree, for **every full ordered-history randomized rule**,

    tQ+lambdaP*eP+lambdaQ*eQ >= H.

Both lambdas are positive, so eP≤a, eQ≤b imply the stated affine lower bound on max(tP,tQ).

**Sufficiency of count compression for the stated four observables only.** For an arbitrary full-history strategy, at each count s sum the visiting P masses over *all* ordered histories and the masses choosing each action; take their ratios to define a count-conditional action distribution, arbitrary at unvisited states. Since every individual history at s has the same strictly positive Q/P likelihood ratio, the same proportions also preserve the aggregated Q action masses. IID propagation of P(z),Q(z) preserves both visiting masses at each successor count by induction on depth. The new count strategy therefore has exactly the same (eP,eQ,tP,tQ). Conversely each count strategy is a valid full-history strategy. This reduction makes **no** claim about other path observers, native six-dimensional Cell dynamics, or arbitrary future non-IID processes.

**Characterization of all Bellman equality policies.** A count-state random kernel is a convex mixture of deterministic count-state policies: pre-sample the action at each state independently before observing. No count state is revisited since depth strictly increases, so the expansion preserves the distribution of all action paths and all four observables. At Bellman equality all positive-mass visited actions must have zero gap. Only the two listed tied states then permit a nontrivial choice. Unreachable state decisions do not alter observables, so the equality fiber is exactly the four-vector convex hull from §2.

**Proof of the all-real iff.** For any real point in R263, a real convex root mixture of the four policies attains exactly its caps; all vertex policies satisfy tQ>tP, so the mixture also has tQ>tP and the affine bound is attained. Conversely the space of finite full-history randomized decision kernels is a finite product of compact action simplexes, with the four observables continuous; feasible closed cap constraints have an attaining optimizer. If the optimizer meets the affine bound, strict positivity of both multipliers forces eP=a and eQ=b; zero Bellman gap forces its observer vector into the stated convex hull. Hence the cap pair is in R263. Infeasible caps have value +∞ and cannot equal the finite affine expression. Thus the theorem covers *all* real pairs in the unit square.

## 5. Reproducibility, observer fidelity, and unclosed bridge

The attached STAGE263_EXACT_FACE.py is **the byte-identical Python Fraction source actually executed**. It independently evaluates each of the four equality strategies using a forward count DAG and an unmerged full ordered-word DFS that separately propagates **positive, source-labelled** P and Q rational branch masses. The latter visits 2,428 ordered nodes and 1,620 terminal action branches in total. For every strategy the terminal P and Q masses each equal exactly one; all four observers exactly match the count DAG. Script also asserts the four vertices, dual equality, exact root mixture, quadrilateral geometry and adjacency, and the outside determinant; actual output ends STAGE263_EXACT_ALL_REAL_FACE_PASS.

BRC reuse is the finite positive rational carrier: sequential multiplication for each labelled source/letter, alternate addition of histories, and explicit observer-quotient preservation. Original source labels, ordered-path multiplicity and distinct P/Q masses are retained for the DFS. This is scoped structural reuse, **not** native BRC–Shor execution or a typed P000 X6 transfer. P000, the ACTIVE Heartbeat World, six-axis ontology, three-dimensional slice constraints, and joint-observer preservation were held fixed; a native transfer and physical calibration require a separate proven interface.

**Control/authority as observed on 2026-10-29:** Global Knowledge main at 37c9c9e84c716149c9d9a949ce2dba8ce81a5734, Enterprise Math canonical control main at 58463dc801532163a8ebd5f3730408cfd15ca768, Stage262 author source at f1741edbe9ca2fa3c646603dc9c52bbf61061018. Own research identity is local EM-RESEARCH2-STAGE263-20261029-0608, not a Source-issued session/CLAIM or independent review. Native service reported research_authority_granted=false and CODE_REVIEW_REQUIRED; live owner query returned CONTROL_QUOTA. Thus the author proof is unreviewed/not admitted, and a real registered activity, formal checkpoint/Source Result and independent Driver review remain separate authorized next control steps. No service credential or shared permission was changed.

**Next mathematical frontier Stage264:** Cross the other R263 edge G5--G6 at a264=595553513081/6449725440000, b264=2918481415/3869835264, with orient(G5,G6,(a264,b264))=-262655/92876046336<0. A non-certifying float HiGHS LP returned feasible with V≈5.469449923962442 and Q-side support; recover *exact* rational primal/dual and characterize the new all-real face before making an optimality claim. Full requirements in NEXT_TASK_PACKET_264.md.
