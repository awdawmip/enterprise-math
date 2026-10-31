# Stage266 — exact adjacent Bellman equality face, N=12 ternary IID

Date: 2026-10-29. Author: EM-R2-266-20261029-0911-PORTABLE, a local author identity (not a Source-issued researcher/session/CLAIM). Scientific status: AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.

## Frozen sources and scope

The explicit continuation source is NEXT_TASK_PACKET_266.md from Enterprise Math commit 61394b936454da0422b047e1b0590ad7d47ffc9e. GLOBAL_KNOWLEDGE_V1 read snapshot: awdawmip/chatgpt-global-knowledge main@6a64ee417cd514498acdd18523442c72f4083d41. Enterprise Math control read snapshot: main@5787ce4de734307c4cce793fe2179be67fc6fbc0. P000, the ACTIVE Heartbeat World, observer preservation, current portable research protocol and the BRC provenance discipline were checked. This theorem is for an EXTERNAL IID auxiliary model, not a physical or native X6 Cell/Heartbeat theorem.

Alphabet {0,1,2}. Source probabilities P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), independently sampled up to N=12 observations. Policies may use the complete ordered history and independent randomization. eP is probability under P of incorrectly stopping with Q; eQ is probability under Q of incorrectly stopping with P. tP,tQ are the corresponding expected numbers of observations. Define V12(a,b)=inf max(tP,tQ), over policies with eP<=a,eQ<=b, and V12=+infinity when the constraints are infeasible.

Target:
a266 = 4693965992729/58047528960000
b266 = 26764770235/34828517376

## Theorem — one exact point and an if-and-only-if face over all real caps

Dual multipliers: lambdaP=12729920/136697, lambdaQ=7907076/136697, thetaP=0, thetaQ=1, Bellman root H=11494057433/199304226.

The exact global optimal value at the target is

V12(a266,b266) = 282137639660138177/49593269164032000
              approximately 5.689030878907278.

For every real (a,b) in [0,1]^2,

V12(a,b) = H - lambdaP*a - lambdaQ*b
IF AND ONLY IF
(a,b) belongs to the strictly convex quadrilateral
R266=conv(I5,J5,J6,I6).

Its exact Euclidean parameter-area (in a,b coordinates) is
45888275146484375/808683748406889283584.

The new region and the Stage265 region R265=conv(H5,I5,I6,H6) share the entire side I5–I6, and their interiors are disjoint.

## Exact full-observer vertices

All four entries in each tuple are (eP,eQ,tP,tQ). Tie bits refer respectively to actions at count states (0,0,5) and (0,1,10). Bit 0 uses the stop action (P at the former, Q at the latter), and bit 1 continues.

I5 (0,0) =
(1763120017/23219011584, 6802983965/8707129344,
 4453822913/967458816, 3922172551/725594112).

J5 (0,1) =
(555154589/7739670528, 3425906045/4353564672,
 13459124989/2902376448, 330916723/60466176).

J6 (1,1) =
(1253006053/15479341056, 4425329935/5804752896,
 9918023951/1934917632, 2919174409/483729408).

I6 (1,0) =
(443710351/5159780352, 1462089145/1934917632,
 3279966317/644972544, 960037303/161243136).

The independently recorded Stage265 I5 and I6 vectors agree in all four source-aware observables. Every vertex has tQ>tP, hence every convex mixture does too. The four cap projections are in strictly convex position with counter-clockwise order I5,J5,J6,I6.

## Exact dual proof for every ordered-history policy

For each count state s=(i,j,k), i+j+k<=12, define the likelihood of ONE ordered history by

p_s=(1/8)^i*(1/24)^j*(5/6)^k,
q_s=(1/12)^(i+j)*(5/6)^k.

The non-normalized Bellman value for remaining costs is, at depth n<12,

B_s = min(lambdaQ*q_s, lambdaP*p_s,
          q_s + B_{s+e0}+B_{s+e1}+B_{s+e2}).

At n=12 the continuation term is omitted. Stop P incurs lambdaQ*q_s, stop Q incurs lambdaP*p_s, while continuing incurs one Q-weighted observation and all three subsequent non-normalized branches. Backward induction applies to every ordered-history policy, regardless of its dependence on the ordered prefix, because the conditional future distributions depend only on the count state and every history with these counts has these same exact likelihoods. Thus

lambdaP*eP + lambdaQ*eQ + tQ >= B_(0,0,0) = H,

and since max(tP,tQ)>=tQ and lambdaP,lambdaQ>0,

V12(a,b) >= H - lambdaP*a - lambdaQ*b.

The executable standard-library Fraction certificate checks all 455 count states and 1,274 legal action costs EXACTLY, locating exactly two tie states: at (0,0,5), stop-P = continue; at (0,1,10), stop-Q = continue. There are exactly 817 strictly positive action gaps. The minimum such positive gap is 11311889/26001155903472009216. The root value is the rational H above. No floating-point result is used to certify these identities.

## Complete equivalence of full-history Bellman-optimal observations and four vertices

An equality policy must use only Bellman-minimizing actions on all reached ordered histories. It therefore has only two possible decision locations. At T1=(0,0,5), there is just ONE all-neutral ordered history. Let r in [0,1] be its probability of choosing continue.

At T2=(0,1,10), there are EXACTLY five ordered histories reaching T2 whose single symbol 1 appeared among positions 1–5; each was unaffected by the T1 action. If the all-neutral five-symbol prefix continues, the path whose symbol 1 appears in position SIX also reaches T2. Other later first appearances are blocked by the unique stop-P action at the all-neutral state (0,0,6). Thus the total weighted number of active ordered histories reaching T2 is 5+r, NOT the unrestricted multinomial count 11.

All T2 histories have identical source likelihoods p_T2,q_T2 and identical minimizing suffix behavior as count-state functions. Let u be the expected number of these T2 histories selecting continue. Exactly 0<=u<=5+r is attainable, including by randomization at individual histories. The complete four-observer vector is an affine function of (r,u), since the difference between the T2 stopping and continuation actions has an identical source-aware observable increment for each active T2 history.

The trapezoid of parameters has exact vertices (0,0),(0,5),(1,0),(1,6). Their observer vectors are respectively I5,J5,I6,J6. Hence ALL full-history Bellman-minimizing randomized policies yield precisely conv(I5,J5,J6,I6), including boundary points. In particular the exact componentwise relation

J6-I6 = (6/5)*(J5-I5)

is not a numerical coincidence: the factor 6/5 counts surviving provenance-carrying ordered histories. This is the scope-typed BRC observer-preservation insight; no signed-mass cancellation or arbitrary path-identification occurs.

Because both lambdas are strictly positive, equality in the dual bound with feasible error caps requires BOTH errors to equal the caps. All four minimizing policies satisfy tQ>tP, therefore all their mixtures have max(tP,tQ)=tQ. Consequently:
(a) every point of R266 is achieved by a mixture saturating both caps and attaining the dual bound;
(b) any point outside R266 cannot achieve the affine bound, since equality would force a Bellman-minimizing full-history policy with its cap pair outside the exact observer hull.
The feasible finite-horizon randomized-policy space is compact, and the infimum is attained whenever feasible. This establishes the stated IF AND ONLY IF for all real caps, not merely a sampled grid.

## Matching exact target primal certificate

Mix I5, J5, I6 with strictly positive rational weights, respectively,

3665652359879461/8343322753906250,
207654876536832/4171661376953125,
272791081021/533972656250.

These sum to one exactly. Exact arithmetic yields
eP=a266, eQ=b266,
tQ-tP=6077469874313/7255941120000 > 0,
tQ=282137639660138177/49593269164032000
   =H-lambdaP*a266-lambdaQ*b266.

Thus primal and dual coincide, proving GLOBAL optimality, not only a feasible bound.

## Stage265 adjacency certificate

Stage265 old-side cap coordinates are
H5=(3750849409/46438023168, 13498546055/17414258688),
H6=(1420974803/15479341056, 4343298685/5804752896).

Let orient(A,B,C)=(B-A) cross (C-A). Relative to the directed I5→I6 edge, both H5 and H6 have strictly positive orientations,
2093963623046875/33695156183620386816,
418792724609375/5615859363936731136;
both J5 and J6 have strictly negative orientations,
-20858306884765625/404341874203444641792,
-4171661376953125/67390312367240773632.
Since the two polygons are convex, each is contained in its own opposite closed half-plane and their only intersection is the full shared I5–I6 segment. Edge matching holds in all four observer coordinates.

## Reproduction and scientific boundaries

The actually executed unmodified file STAGE266_EXACT_FACE.py uses only standard-library fractions and checks dual recurrence, ties and positive gaps; computes four deterministic policies via count-state path multiplicity; independently enumerates every ordered history via a separate DFS under each policy; normalizes P and Q mass separately to exactly one; derives exact cap hull and area and a positive rational target mixture; and checks prior I5/I6 observer vectors. Execution returned STAGE266_EXACT_ALL_REAL_FACE_PASS. Totals across the four ordered-history verifications: 2,923 nodes, 1,950 terminal leaves. The full executed stdout is saved as STAGE266_EXECUTED_STDOUT.txt. Exploratory floating-point LP was only a discovery aid and is excluded from the proof.

The native service read for this work reported research_authority_granted=false and active job count 5/5; its control task-owner inventory request returned CONTROL_QUOTA. No native CLAIM, formal Source Result, independent Driver admission, Lean proof or native P000 X6 correspondence is asserted. The next unresolved unit is Stage267, across the new J5–J6 side; NEXT_TASK_PACKET_267.md contains an EXACT constructive feasible outside point.
