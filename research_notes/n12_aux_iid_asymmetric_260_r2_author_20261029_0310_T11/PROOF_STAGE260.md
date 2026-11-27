# Stage260 exact sixth adjacent all-real contact region (portable author proof)

2026-10-29; author: local EM-R2-260-20261029T0310-AUTO11, not a native Source session. AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. External finite ternary IID only: no native P000 X6 embedding or heartbeat-physics claim. Predecessor Stage259: 4acb24b4090bb4c44c33fdc420491f9b4a56486e in Draft PR #1571.

Frozen science inputs: GLOBAL_KNOWLEDGE_V1 main@c5e31607f74ed3a396839bbb021c756fbc74c0c6; Enterprise Math main@058f67fb1a4aec53310819eb65d393e22538a7f0; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488; X6 time contract 94a02d067be2b039ca4c0f7ffedb5ebde8430e08; active user worldview blob 99238c3466eb0805748bae01fd1a20868a5a351e. BRC applied only to exact positive branch masses, path-labelled provenance and a proven four-observer quotient; no P000 transfer.

## Theorem: exact all-real region and target value

P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=12. For full ordered-history randomized stopping-and-binary-decision rules (including arbitrary real coins), eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP and tQ are their two expected observation counts. Define V12(a,b)=min max(tP,tQ) under eP<=a,eQ<=b for real (a,b) in [0,1]^2, or +infinity if infeasible.

Exact Bellman certificate:
lambdaP=17915904/217655
lambdaQ=11569812/217655
(thetaP,thetaQ)=(0,1)
H=44960725931/846242640.

Five complete (eP,eQ,tP,tQ) vectors in counterclockwise error-plane order:

C4=(2121300017/23219011584,6793355215/8707129344,3571492913/967458816,3001418801/725594112)
C5=(1692824803/15479341056,4308598685/5804752896,2711460067/644972544,2260130659/483729408)
C12=(25325973227/139314069504,10403158555/17414258688,34493690603/5804752896,9303029477/1451188224)
B12=(13392328801/69657034752,5104265215/8707129344,16809787489/2902376448,4457228801/725594112)
B4=(2315791267/23219011584,6715503965/8707129344,3454944163/967458816,2845990051/725594112).

R260 is their projected error-pair convex hull, a strictly convex rational pentagon of exact area 536059353705078125/606512811305166962688. For ALL REAL a,b in [0,1], including irrational boundary points:

V12(a,b)=H-lambdaP*a-lambdaQ*b  IF AND ONLY IF  (a,b) belongs to R260.

All five supporting policies and all their mixtures satisfy tQ>tP. Thus thetaP=0 and thetaQ=1 on the entire region.

The B4--B12 edge is exactly the full C4--C12 edge of Stage259 in ALL FOUR observables, on 2a+b=33809389661/34828517376. Stage259 lies on >= side and Stage260 on <= side, with disjoint interiors. The opposite C5--C12 edge lies on 2a+b=22312869149/23219011584; Stage260 lies on its >= side.

For the frozen cap a*=6349626716117/43535646720000, b*=984980765/1451188224, exact Stage259-edge gap 33809389661/34828517376-(2a*+b*)=3/10000, and:

V12(a*,b*)=82993854248339957/16450956921600000 ≈ 5.044925632220796.

Exact achieving policy: choose independently at root between C4, B12, B4 with positive weights respectively 3265173504/85021484375, 1803256470623293/3593177972656250, 1651928739406909/3593177972656250; weights sum to 1. Both errors saturate, tP=1851794737526929603/394822966118400000 < tQ=V12.

## Exact dual and equality-fiber proof

For ordered history h of symbol counts s=(i,j,k), Q(h)/P(h)=L(s)=(2/3)^i*2^j. Normalize by P-history mass. With continuation disallowed at depth 12, Bellman recursion is

H(s)=min{lambdaQ*L(s) [decide P], lambdaP [decide Q], L(s)+sum_z P_z H(s+unit_z) [continue]}.

At each ordered history, randomized continuation obeys backward-induction lower bound tQ+lambdaP*eP+lambdaQ*eQ>=H(0,0,0), so V12(a,b)>=H-lambdaP*a-lambdaQ*b.

Exact Python Fraction code checks ALL 455 count states, 1274 possible action costs, 810 strict alternative action gaps and root H above. Ties comprise only eight all-neutral states (0,0,k), k=4..11, with actions P/C, and the unique state (0,1,4) with Q/C: nine ties. Every other state has a unique minimizer. At (0,0,k), k<4, continue is uniquely optimal.

Full-history policy reduction is mathematically scoped: aggregate the positive P-weighted visiting/action masses over all ordered histories with a fixed count s. Each constituent Q mass is L(s) times its P mass, including the same action-coin law. Dividing aggregated P action masses by aggregated P visit mass gives a legal randomized count-state policy preserving the full four-vector (eP,eQ,tP,tQ), with P and Q positive mass conservation. The acyclic count graph allows pre-sampling its finite action random variables, giving a convex mixture of deterministic count-state policies. This does NOT preserve arbitrary path-level or future P000 joint-relation observations.

Zero Bellman slack forces every effective deterministic policy to be D_(k,M): k in {4,...,12} is the first all-neutral depth with P stop, and at the only special tie (0,1,4), M is either Q or C; all remaining actions are the unique Bellman minimizer. Let B_k be the complete four-vector for M=Q, C_k for M=C. Exact recursion checks each of the 18 policies, tQ>tP and tQ+lambdaP*eP+lambdaQ*eQ=H.

A separate unmerged ordered-history DFS (separate P/Q positive masses, every original ordered branch, unit terminal masses) checks all 18 and agrees exactly with suffix DP in all four outputs; cumulative 6234 nodes and 4162 terminal history branches. Exact vector interpolation verifies B_4,...,B_12 lie on four-observer segment B4--B12; C_5,...,C_12 lie on C5--C12; C4 adds a fifth corner. For all four observables, C4-B4=(4/5)*(C5-B5), and Ck-Bk=C5-B5 for k>=5. The 4/5 factor is source-order fidelity: of five positions for one symbol-one event before total depth five, one history is cut off after four neutrals by k=4, whereas all five reach the special tie for k>=5. Aggregating unordered prefix paths without multiplicity would break this exact relation.

All five cyclic turn determinants are strictly positive (the exact verifier prints them). Shoelace formula gives the asserted nonzero area. The equality fiber's error projection is therefore exactly R260 and every constituent has tQ>tP. Any real point of R260 admits a finite convex mixture reaching the lower bound, proving sufficiency.

Conversely the finite product of full-history action simplexes is compact, so any feasible infimum is attained. Since lambdaP,lambdaQ>0, equality to the dual lower bound requires exact error cap saturation, zero Bellman slack and tQ=max(tP,tQ). The equality-fiber characterization forces (a,b) in R260. This proves the all-real necessary direction, including infeasible points and boundary cases.

## Actual computation and evidence limits

The included runnable STAGE260_EXACT_FACE.py was ACTUALLY EXECUTED with Python standard-library fractions.Fraction. Observed log stored in STAGE260_EXECUTED_STDOUT.txt. Its terminal rows include:
STAGE260_BELLMAN_PASS 455 1274 810 9
ORDERED_DFS 6234 4162
STAGE260_EXACT_ALL_REAL_FACE_PASS

Executed source SHA256 (local): 3d40ef7bf6fbe3f2d5d98b9f08e3738e23ad212c812450754ceec5741a9dfc57.

Exact rational computation and complete finite-horizon induction are evidence for the stated finite IID model, full ordered-history strategies and four outputs. They do not prove native P000 X6/heartbeat dynamics, other models, physical correspondence, Lean formal verification or independent scientific admission. Numerical optimization was used only for candidate discovery, never as proof.

Native gateway em_status returned research_authority_granted=false, control_quota 5/5 and CODE_REVIEW_REQUIRED. Explicit owner inventory returned CONTROL_QUOTA, leaving actual active owner unverified. No native CLAIM, Source Result, independent Driver review, session or official task publication is claimed.

## Next question

Stage261: cross the opposite C5--C12 edge 2a+b=22312869149/23219011584 by 3/10000, test exact feasibility and identify new Bellman support and exact source-labelled primal or rational impossibility certificate. NEXT_TASK_PACKET_261.md specifies the algebraic candidate, scope and acceptance conditions.
