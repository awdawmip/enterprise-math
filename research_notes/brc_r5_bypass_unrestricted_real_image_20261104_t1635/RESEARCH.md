# R5 bypass BRC: unrestricted declarations restore actual four-observer image equality

Date: 2026-11-04. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Parent problem, scope and pins

The parent R5 objective seeks a strictly positive, source/route-sensitive P/Q BRC experiment with equal complete four-observer FULL and seedless-likelihood-ratio (LR) convex hulls but different **actual real-policy** images. This is the unrestricted-declaration continuation of the controlled-label two-merger bypass model at immutable predecessor commit ce5f5d87e57c725be56e8109c772cc2b26a5a3cc, RESEARCH.md in research_notes/brc_r5_two_merger_bypass_graph_polytope_20261104_t1540/. Scientific input pins retained: Global Knowledge a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current operating rules were read separately. The model is an auxiliary finite positive BRC, without a claimed native X6 realization.

## Exact model and complete actions

Under P and Q, A1, A2, B have equal initial P/Q masses respectively 1/4, 1/4, 1/2. At time 1 the first merged (time,likelihood-ratio) key r=1 contains A1,A2, with options STOP/declare P, STOP/declare Q or CONTINUE; B bypasses to time 2. At time 2 the continuing A histories and B share a second r=1 key with the same three options. At time 3, after continued time-2 action, each A history has Q-law terminal probabilities (1/2,1/2), likelihood ratios (1/2,3/2); B has (1/2,1/2), likelihood ratios (1/4,7/4). Each terminal independently permits both P and Q declarations (including randomization). Under P each terminal probability is r times the Q probability. All transition and initial probabilities are strictly positive and normalize under each law. Terminal ratios are four distinct observed LR keys. FULL observes full history, seedless LR uses one behavior probability per common (time,r) key, and there is no common random seed. The observation is O4=(P[declare Q],Q[declare P],E_P[t_stop],E_Q[t_stop]).

## Theorem

For all real behavioral probabilities in [0,1] in this exact unrestricted-declaration BRC,

    O4(FULL) = O4(seedless LR).

Both actual sets are compact and convex in the three-dimensional affine plane T_P=T_Q. In particular the complete four-observer convex hulls are equal.

### 1. Exact occupancy and error fibers

For FULL let x_i be time-1 continuation probability at A_i, a_i its conditional time-2 continuation probability, and y the B time-2 continuation probability. Write

    x=(x1+x2)/2, z=(x1*a1+x2*a2)/2, y=b.

All and only triples 0<=z<=x<=1, 0<=y<=1 are FULL-feasible: the converse takes x1=x2=x, a1=a2=z/x if x>0, otherwise 0. LR requires z=xy. The P/Q timing distributions coincide because all source entry likelihood ratios are 1 and the terminal laws separately normalize. Therefore

    T_P=T_Q=3/2+(x+z+y)/2,    f=2(T_P-3/2)=x+z+y in [0,3]. (1)

For a Q-law probability mass m with likelihood ratio r, declare-Q probability d contributes (m*r*d, m*(1-d)) to (eP,eQ). Let K(r)=conv{(r,0),(0,1)} and use Minkowski sum of subsets of R². Define

    K0=K(1),
    KA=[K(1/2)+K(3/2)]/2,
    KB=[K(1/4)+K(7/4)]/2.

The Q-law mass stopping at r=1 is 1-(z+y)/2, while A/B terminal masses are z/2 and y/2. Because each terminal ratio is an observable key and declarations are unconstrained, **the complete error fiber** at a feasible (x,z,y) is

    E(x,z,y)=[1-(z+y)/2]K0 + (z/2)KA + (y/2)KB.          (2)

Different declarations across A1/A2 yield the same mass-weighted per-terminal probabilities. Different stopped r=1 keys similarly aggregate to K0. Conversely any vector in (2) can be realized through the corresponding legal individual declaration probabilities. Formula (2) also governs LR when z=xy.

### 2. All-signed convex-order inequality

Fix any signed direction n=(alpha,beta) on the two error coordinates and define the convex function v(r)=max(alpha*r,beta), and

    h0=v(1), hA=[v(1/2)+v(3/2)]/2,
    hB=[v(1/4)+v(7/4)]/2.

The A terminal ratio lottery is a mean-preserving spread of r=1. The B lottery is in turn a mean-preserving spread of A: 1/2=(5/6)(1/4)+(1/6)(7/4) and 3/2=(1/6)(1/4)+(5/6)(7/4). By Jensen, for **every signed n**,

    0<=DA:=hA-h0<=DB:=hB-h0.                              (3)

By (2), support of the error fiber is exactly

    h(E(x,z,y);n)=h0+[z*DA+y*DB]/2.                        (4)

### 3. One LR timing policy covers the full FULL fiber

Fix the time f=x+z+y. As z<=x, z<=(f-y)/2; also 0<=y<=min(f,1). By (3),

    z*DA+y*DB <= f*DA/2+y*(DB-DA/2).

The right side is maximized at y*=min(f,1), independently of the signed direction n. Its bound is attained by the feasible triples

    (x*,z*,y*)=(0,0,f),                   0<=f<=1;
                ((f-1)/2,(f-1)/2,1),      1<=f<=3.          (5)

They are **actual seedless LR policies**, with common continue parameters (x*,y*) and z*=x*y*. For all n, the FULL fixed-f support thus equals that of the single canonical LR error polygon E*, and is

    H_f(n)=h0+(f/2)*DB,                         0<=f<=1;
           h0+(1/2)*DB+((f-1)/4)*DA,           1<=f<=3.    (6)

The complete FULL fixed-f error set is compact convex: its source occupancy parameters and f constraint form a polytope; scaled fixed declaration segments K0,KA,KB can be represented by finitely many linear occupancy and declaration-mass inequalities. Hence it is a linear projection of a finite polytope. Since that FULL fiber and the canonical polygon E* have the same support function for **every signed n** by (3)-(6), equality follows by compact convex separation. Thus each FULL error vector, at its exact original time f, is attained by the canonical LR timing policy (5) with suitable free declaration probabilities. This establishes O4(FULL) subset O4(LR); reverse inclusion is immediate.

### 4. Explicit behavioral reconstruction and rational certificates

The canonical LR error polygon E* has at most 32 candidate vertices: for its effective early r=1 stop group and four distinct terminal r keys choose binary P/Q declaration labels. Any FULL error vector in E* is a convex combination of at most three polygon vertices by the planar Carathéodory theorem. Mix each key's binary declaration probabilities by those same nonnegative coefficients; the error observation is affine in each declaration probability for fixed timing. This gives one **seedless randomized behavioral LR policy without a shared seed**, with exact original O4. For rational FULL probabilities, all polygon vertices and triangle barycentric weights are rational.

The previous controlled-label LR midpoint witness (eP,eQ,f)=(29/32,1/4,3/2) is now in the unrestricted-declaration canonical LR fiber. The fixed-label nonconvexity relied on the previous action restriction; unrestricted declarations enlarge fibers and restore full real-image equality in this topology.

## Executed exact validation

The Python stdlib Fraction VERIFY.py independently computes P/Q contributions history-by-history, including individual A1/A2 stop/terminal declarations. It checks all 48 effective deterministic A/B action pairs (A1/A2 have identical kernels), all 441 signed rational error directions across selected rational occupancy states, 240 heterogeneous nonvertex FULL policies against exact canonical convex-polygon half-planes, and 240 further nonvertex FULL policies by exact at-most-three-vertex rational barycentric certificates. It checks the former fixed-label midpoint and exact f boundaries. All assertions passed; EXACT_OUTPUT.txt ends with PASS_EXACT_R5_BYPASS_UNRESTRICTED_DECLARATION_IMAGE_EQUALITY. These finite checks corroborate the direct analytic all-real theorem.

## Information preserved and next mathematical unit

The source and route identities remain in the FULL occupancy carrier. Their projection to (eP,eQ,T_P,T_Q) is proven safe for the stated observation and free declaration actions; no claim is made about later provenance-sensitive observations. The result supplies a reusable convex-order canonical-fiber compression principle: when B's terminal ratio experiment dominates A in convex order and the bypass permits B to use terminal capacity first, one LR timing policy can reproduce every full-history fixed-time error fiber. The R5 mother objective remains open; a useful next trial is **crossing terminal experiments** for which neither terminal kernel dominates the other for all signed error directions, retaining positive kernels and distinct terminal observability. Test all-signed convex-hull equality with rational primal/Farkas certificates, then actual-image membership. The present proof has no independent Driver review or native RESULT admission; P000 and ACTIVE worldview remain unchanged.
