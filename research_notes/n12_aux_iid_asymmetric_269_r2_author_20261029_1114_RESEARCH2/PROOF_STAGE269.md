# Stage269 — exact adjacent Bellman face across Stage268 W–Z

Date: 2026-10-29. Evidence classification: PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. Scope: external ternary IID sequential binary decision model; not a native P000 X6 theorem, Source CLAIM, formal Result or independent Driver review. Local author label: EM-R2-RESEARCH2-20261029-1114-LOCAL (not a service-issued identity).

## Verified inputs and mathematical problem

Fixed GLOBAL_KNOWLEDGE_V1 main@19cf4b3db73394b6a2f43af5a282e802caeb5524 and Enterprise Math main@2f9fd05d81744d01fa8cbd84921b57e70bb98bef. Consulted global entry/manual, project TASK_RESEARCH router, P000 startup and original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview, portable research and activity protocols, plus Stage268 source/proof from immutable research commit 9b627ea1baa8477d630429e5c7008c06780a5654. Native research authority was false; owner inventory returned CONTROL_QUOTA. Existing Stage268 scientific result reused without duplicate re-verification.

Alphabet {0,1,2}, IID probabilities P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon N=12. Arbitrary complete ordered-prefix randomized stopping and terminal decisions are permitted. eP=P(declare Q), eQ=Q(declare P), tP=E_P(T), tQ=E_Q(T). V12(a,b) denotes minimum max(tP,tQ) among such policies with eP<=a and eQ<=b for real caps in [0,1]^2, or +infinity if infeasible.

## Exact theorem

For the Stage269 caps

    a=107398477982417/1408964021452800
    b=28788331614361/37150418534400

the exact GLOBAL optimum is

    V12(a,b)=8204685878260270197067129/1427152351549896190328832
            ≈ 5.7489908973978361.

The exact dual multipliers and root constant are

    lambdaP=132796528772096/960387801707
    lambdaQ=71829966906324/960387801707
    thetaP=0, thetaQ=1
    H=3311293384195030691817557/44598510985934255947776.

Define the rational, nondegenerate strictly convex parallelogram R269=conv(W,Z,D,C), using the first two coordinates of the four-observer tuples below. Its EXACT area is

    15006059401671875/17251919966013638049792.

For EVERY REAL pair (a,b) in [0,1]^2,

    V12(a,b)=H-lambdaP*a-lambdaQ*b  IF AND ONLY IF  (a,b) is in R269.

This is a full-real two-dimensional equality-face statement, not an interpolation of finite test points. R269 shares the whole W–Z edge with Stage268 R268, but the two interiors do not overlap.

## Four exact deterministic corner policies

The tuple order is (eP,eQ,tP,tQ), and (r,u) denotes continuation at the two tied count states T1=(0,0,5) and T3=(1,2,1), respectively.

    W, (r,u)=(0,0):
    (378877764437/5283615080448,146176760405/185752092672,
     27566635857287/5944066965504,254184389485/46438023168)

    Z, (r,u)=(1,0):
    (47509440493/587068342272,424845981215/557256278016,
     10156839152429/1981355655168,280281089485/46438023168)

    C, (r,u)=(0,1):
    (1135528662191/15850845241344,146193716605/185752092672,
     27574125092087/5944066965504,254314824805/46438023168)

    D, (r,u)=(1,1):
    (1281650262191/15850845241344,424896849815/557256278016,
     10159335564029/1981355655168,280411524805/46438023168)

In all four observer coordinates D-Z=C-W holds exactly. Every corner satisfies tQ>tP and lambdaP*eP+lambdaQ*eQ+tQ=H. Thus the affine map of independent coin probabilities is

    Obs(r,u)=W+r(Z-W)+u(C-W), 0<=r,u<=1.

The unique rational interior target coordinates are

    r=75294403653622137309/153662048273120000000,
    u=479208909/61464819309248000.

Both are STRICTLY in (0,1). This independent rational two-coin policy exactly saturates both error caps, with

    tP=22272958815958270485484430687/4566887524959667809052262400,
    tQ=8204685878260270197067129/1427152351549896190328832,
    tQ-tP=442448443830510460570042457/507431947217740867672473600 > 0.

It therefore attains max(tP,tQ)=tQ equal to the dual lower bound. Stage268's exterior-point feasible witness had tQ=53394354497531/9287604633600; it was not Stage269-optimal, with exact positive excess

    428502556554481/11892936262915801586073600.

This strict improvement is a new rational statement, not a relabelled prior upper bound.

## Full-history Bellman proof of the lower bound

For any ordered prefix with counts s=(i,j,k), let p_s=(1/8)^i*(1/24)^j*(5/6)^k and q_s=(1/12)^(i+j)*(5/6)^k. Define the UNNORMALIZED backward Bellman recursion

    B_s=min(lambdaQ*q_s,lambdaP*p_s,q_s+sum_{x=0}^2 B_(s+e_x))

when depth(s)<12; omit continuation at depth 12. These costs correspond respectively to stop declaring P, stop declaring Q, and continue. At every individual ordered history, its two likelihoods and the available continuation suffix costs depend only on counts; backward induction therefore proves the Bellman lower bound against every FULL ORDERED-HISTORY policy, including randomized history-dependent policies, rather than restricting competitors to count-only rules.

The exact root is B_(0,0,0)=H, hence for ALL such policies

    lambdaP*eP+lambdaQ*eQ+tQ >= H.

Since lambdaP and lambdaQ are strictly positive, every feasible policy obeys V12(a,b)>=H-lambdaP*a-lambdaQ*b.

The Python standard-library Fraction verifier completely covers 455 count states and 1274 legal action costs. There are exactly 817 strictly positive competing gaps, whose minimum is 411190974797/3805739604133056507543552. The ONLY action ties are T1=(0,0,5): stop-P versus continue, and T3=(1,2,1): stop-Q versus continue. All other actions have a unique minimizer.

## Exhaustiveness of the full-real equality face

T1 has exactly one reached ordered prefix (five consecutive symbol-2 events); T3 has four reached ordered prefixes with symbol counts (1,2,1), all with the same separate positive P and Q likelihoods and identical optimal suffix kernels. The two tie cones are disjoint: T1 is at depth 5 with five occurrences of symbol 2, while T3 is at depth 4 with only one such occurrence. No history can pass through both. All four T3 coin decisions enter the four observers ONLY through their average continuation probability u, because their likelihoods and suffix effects are identical. The independent T1 coin is r. Thus every globally Bellman-equal FULL-HISTORY randomized policy has exactly the four-observer form Obs(r,u) above; there are no omitted hidden path-dependent contributions or extra equality points.

The four corners have tQ>tP, and hence this is true throughout the convex hull. Equality in the error-cap dual with strictly positive lambdaP and lambdaQ forces eP=a AND eQ=b. Therefore equality outside R269 is impossible, since every Bellman-equal strategy has its error pair in exactly that parallelogram. Conversely, every point of R269 is realized by some pair of coins r,u and satisfies tQ>tP, attaining the lower bound. The finite ordered-prefix tree yields a finite product of compact decision simplices with continuous observable maps, so every feasible minimum is actually attained; exterior equality cannot arise merely as a nonattained limiting infimum. This proves the iff over ALL REAL caps in the stated square.

For adjacency, exact orientation orient(W,Z,C)=-15006059401671875/17251919966013638049792, whereas orient(W,Z,L5)=+11415537109375/7667519984894950244352 for the old Stage268 region's interior vertex L5. Both faces are convex nondegenerate parallelograms with shared endpoints W and Z and opposite half-plane interiors. Their intersection is exactly their complete shared edge.

## Actually executed verification, BRC and next discriminating question

REPRO_STAGE269.py is the actual locally executed exact certificate saved as executable UTF-8; REPRO_STAGE269_EXECUTED_STDOUT.txt is its corresponding raw output. Four deterministic policies were independently measured (a) with multiplicity-preserving integer count-state source flow and (b) by unmerged complete ordered-word DFS propagating exact P and Q rational probability masses separately along each concrete branch. All four eP,eQ,tP,tQ vectors agree exactly by both methods. The ordered DFS visited 7288 nodes and 4860 terminal leaves across four corner policies; each P/Q terminal mass separately equals 1. Program outcome: STAGE269_EXACT_ALL_REAL_FACE_PASS. No floating-point numerical fit supports the proof.

The BRC-compatible carrier is nonnegative rational source mass with ordered path identity and exact multiplicity. The count quotient is mathematically justified only for the stated IID four observers and their future operations. This does NOT assert signed/phase cancellation, native X6 Cell geometry, native rotations or a P000 physical theorem. A native bridge would require a six-axis path/Cell embedding, specified three-dimensional slice and third-coordinate semantics, preserved relations and updates, and an explicit compatible readout.

The next exact frontier is Stage270 across the new C–D edge. A dual-only first-switch scan identifies the state (1,2,2): Q/continue while preserving T1's tie. A feasible exterior rational cap and a precise successor proof obligation are stated in NEXT_TASK_PACKET_270.md. These are candidates, not a promoted Stage270 optimality result.
