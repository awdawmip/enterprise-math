# EC48H — Two-free-decoder switching theorem for seedless BRC ROC preservation

Status: author-side mathematical proof plus exact-rational verification, 2026-10-27. Research activity RA-EMR4-20261027-1138-EC48H-MATCH; researcher EM-R004-EC48H-20261027-1138-LOCAL (locally assigned, no Source-native CLAIM). Proof awaiting independent Driver review and mathematical admission.

Frozen GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge main@2b67737ee24d9cdb3c2c7ee176e86c1bbf83df39 (bootstrap/manual/P000 V4/ACTIVE worldview). Enterprise Math initial source: awdawmip/enterprise-math main@03a7ce964fcc3993fd0736dafc69f16858a8d6d3, with AGENTS.md, docs/PORTABLE_RESEARCH_PROTOCOL.md and research_persistence_policy.json. Mathematical predecessor: EC48G@fd08c300cde18245565ce3b27d7ced523d35b627.

## 1. Model and exact question

Fix nonempty finite history set H and later-observation set Y. Strictly positive source arrays p(h,y),q(h,y) each have total mass 1. A seedless K-state observer privately encodes each history with a row-stochastic distribution pi_h(m) over memory states m=1,...,K; after seeing y it declares source P with probability u_m(y) in [0,1]. Its effective decision array is w(h,y)=sum_m pi_h(m)u_m(y), yielding ROC coordinates (alpha,beta)=(sum p*w,sum q*w). The reachable set is S_K. The complete-history zonotope Z=sum_(h,y)[0,(p(h,y),q(h,y))]. No persistent common random seed is allowed. Define K_hull=min{K:conv(S_K)=Z} and K_seed=min{K:S_K=Z}.

At a critical source-likelihood ratio r=p(h,y)/q(h,y)>0, the tied histories T_r contain some equality p=rq, while non-tied histories have forced binary decoder rows c_h(y)=1[p(h,y)>rq(h,y)]. Let C_r be the set of their distinct rows, c=|C_r|. For every tied history h put b_h(y)=1[p(h,y)>rq(h,y)] and a_h(y)=1[p(h,y)>=rq(h,y)]. Thus b_h<=a_h componentwise; only its equality cells may vary. Let B_r={b_h:h in T_r}\C_r and A_r={a_h:h in T_r}\C_r. Build the bipartite outside-to-outside graph E_r with an edge (b_h,a_h) when b_h,a_h both lie outside C_r. Let B*_r,A*_r be the sets of endpoints incident to at least one edge of E_r, and let t_r=K_hull-c.

By the exact EC48A strict-signature-chamber lemma, the maximum number of distinct forced binary decoder rows at noncritical ratios is exactly K_hull. Taking the two chambers next to r shows |B_r|<=t_r and |A_r|<=t_r: a convex combination of decoder rows can equal a binary word only if each decoder row with positive mixing weight equals it coordinatewise. Therefore the full binary b and a endpoints each fit in K_hull states.

## 2. Theorem EC48H.1

At a fixed critical r, the entire exposed optimal face F_r={(alpha,beta) in Z: alpha-r beta=V_r}, V_r=sum_(h,y)max(p-rq,0), is attainable by a K_hull-state seedless observer if E_r satisfies at least one of:

(A) E_r is a matching, i.e. no two distinct edges share a source or target word (the empty graph qualifies).
(B) E_r has a common Boolean pivot: v=OR(B*_r) <= AND(A*_r) coordinatewise.
(C) Both endpoint sets satisfy |B*_r|<=2 and |A*_r|<=2.

Consequently, if every critical r satisfies at least one condition, K_seed=K_hull. In particular:

**Theorem EC48H.2. For every finite strictly positive two-stage BRC observer model with K_hull<=2, K_seed=K_hull, regardless of the number of tied histories or future labels.** The same holds for arbitrary K_hull if t_r<=2 at every critical r.

### Constructive proof

Allocate c fixed decoder rows to C_r. At the all-b endpoint allocate the remaining t_r rows to all distinct B_r words, with unused rows arbitrary. Non-tied histories use their fixed rows; tied histories encode deterministically to their b_h. Because |B_r|<=t_r, this is possible.

First process each tied history with a_h in C_r. Its b_h row is available, so privately interpolate its encoder from b_h to the fixed decoder a_h, while keeping all decoder rows fixed. The interpolation changes only equality cells and ends with this history permanently independent of the free decoders. Histories whose b_h is in C_r but a_h is outside C_r remain on their original fixed decoder until the last phase. Exactly the histories corresponding to outside-to-outside graph edges now depend on free rows.

Case (A), matching: for each graph edge (b,a), take the unique free row carrying b and move that decoder linearly from binary b to binary a. No two edges use the same original or target word. Every attached history has this same admissible transition, so all strictly signed cells remain forced, and equality cells vary monotonically. Free rows unused by graph histories can be assigned to remaining target words in A_r. The |A_r|<=t_r bound guarantees capacity.

Case (B), common pivot: let v=OR(B*_r). Every active source word b satisfies b<=v, while v<=a for every active target a. Move every free row with attached graph histories from its b to v; each attached history has admissible endpoints b<=v<=a and so its strictly signed cells remain forced. Configure unused rows to v also. When all free rows coincide at v, freely reassign each graph history's private encoder to its designated target slot; the effective row is unchanged at this reassignment. Move each target slot from v to the appropriate a; each graph history on it sees an admissible v<=a interpolation. Target slots can cover all A_r words under the adjacent-chamber bound. Rows not needed for graph histories can be configured while unused.

Case (C), at most two graph source and two graph target words: if E is a matching, use (A). If there is only one active source or target, the source or target itself yields a common pivot; use (B). If both sides have two vertices and all four edges, each b is <= each a, implying OR(B*)<=AND(A*); use (B). The only remaining nonempty nonmatching bipartite graph on a 2-by-2 vertex set is the 3-edge fork/join, after relabeling:

E={(b1,a1),(b1,a2),(b2,a2)}.

Keep the free decoder at b1 fixed. First interpolate the second free decoder b2->a2, serving its attached (b2,a2) histories. Second privately interpolate the history encoders attached to edge (b1,a2) from the row b1 to the now available a2 decoder. Finally move the now uniquely used decoder b1->a1 for its (b1,a1) histories. All three stages preserve the signed-cell constraints and monotonically turn equality cells from 0 toward 1. This works with exactly two free rows.

After the graph is processed, place any still unused free rows at remaining target words A_r. Finally interpolate each tied history with b_h in C_r and a_h outside C_r from its permanent fixed row to the now available target decoder a_h. Every tied history now reaches its a_h endpoint. At every stage, memory has no more than c+t_r=K_hull states; only private encoder stochasticity and continuous decoder parametrization are used, with no common random seed.

The ROC support functional alpha-r beta is V_r throughout, since each cell with p>rq is held at w=1 and each cell with p<rq is held at w=0. Along the continuous monotone constructed path, equality-cell q-mass z=sum_{p=rq}q*w varies continuously from 0 to Q_r=sum_{p=rq}q. Every intermediate z in [0,Q_r] is attained by the intermediate-value theorem. On the face alpha-r beta=V_r all tied generators have slope r, so the z-coordinate parametrizes the *entire* one-dimensional exposed face. Thus F_r subset S_K.

When each positive critical face is reachable, every boundary segment of the planar positive-generator zonotope Z is reachable, including complementary faces obtained by replacing all decoders u_m(y) by 1-u_m(y), which reflects (alpha,beta) about (1/2,1/2). Every boundary vertex is attainable as a strict-sign chamber optimal binary decision. Scaling all decoder probabilities by tau in [0,1] contracts any attained point radially to the origin, hence S_K is star-shaped. Every point of convex Z lies on a segment from the origin to its far boundary, so S_K=Z. Since K_hull<=K_seed by definition, K_seed=K_hull follows. Finally |B*_r|<=|B_r|<=t_r and similarly for A*, so t_r<=2 automatically gives case (C); K_hull<=2 implies t_r<=2. QED.

## 3. Exact witnesses

### W3: nonmatching and NO common pivot, still two-state seedless preservation

P_raw=[[3,2,2,1],[3,1,2,2],[2,1,2,3]], total 23; Q_raw is three rows [2,2,2,2], total 24. Normalize p=P_raw/23, q=Q_raw/24. Exact Khull=2. At r=24/23 the fixed set C is empty and the distinct graph edges are 1000->1100, 1000->1011 and 0001->1011. There is no pivot because OR{1000,0001}=1001 is not <= AND{1100,1011}=1000. The 3-edge switching construction gives three consecutive segments:

alpha=(9+4s)/23, beta=(6+4s)/24;
alpha=(13+4t)/23, beta=(10+4t)/24;
alpha=(17+2v)/23, beta=(14+2v)/24,
with s,t,v in [0,1]. Each lies on alpha-(24/23)beta=3/23. Beta covers [1/4,2/3] exactly, with shared endpoints. All other faces are covered by the theorem, hence K_seed=Khull=2 for this entire model.

### W4: full K2,2 collision and common pivot

P_raw=[[3,2,2,1],[3,2,1,2],[2,3,2,1],[2,3,1,2]], total 32. Q_raw is four rows [2,2,2,2], total 32. Khull=2, r=1. The collision graph connects B*={1000,0100} completely to A*={1110,1101}, and pivot v=1100. ROC segments:

alpha=3/8+s/4, beta=1/4+s/4;
alpha=5/8+t/4, beta=1/2+t/4,
s,t in [0,1]. Beta covers [1/4,3/4], with support alpha-beta=1/8.

## 4. Computation and exact status

The accompanying EC48H_VERIFY.py checker implements Fraction-based strict threshold chambers, exact signs/graph classification, explicit row-stochastic history encoders, decoder moves, forced-bit constraints, the support identity, and the monotonic tied-mass coverage. EC48H_REPORT.json contains 8,140 model structural scans (7,290 exhaustive fixed-Q integer arrays and 850 seeded nonuniform-Q random instances). Exactly 7,757 models met the stated all-faces sufficient condition. The criterion classified 30,700 critical faces. Exact rational factorization paths were checked for 202 selected models, 965 faces, 156,848 cell-level assertions, plus exact W3 and W4 witnesses. All declared checks passed. Remaining models were not certified by this sufficient condition and are not counterexamples. Finite tests check the implementation; the all-model conclusion above rests on the explicit combinatorial construction. Python standard library Fraction implements rational arithmetic, not signed/phase BRC or native heartbeat operations.

BRC tool reuse: REUSE_APPLIED for EC48A chamber signature and EC48C–G face/encoder framework; EXTEND_EXISTING_TOOL for two-free path construction. Scope is a single two-stage positive-weight source/observation horizon. The ROC-only quotient discards fuller branch provenance; it is justified only for this declared terminal ROC readout. No X6 dynamics, spatial slice, physical clock, or signed-amplitude correspondence is inferred.

Native control observation (2026-10-27): em_control_tasks returned CONTROL_QUOTA. em_session_start(RESEARCHER) returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Thus current active owner/CLAIM cannot be verified, and the author-side GitHub research artifact is not a native Result, independent Driver review, Working Truth or Foundation acceptance.

## 5. Next research unit EC48I

Search Khull>=3, Khull<|H| and a critical r with t_r>=3 whose graph is neither matching nor pivot-compatible and with >=3 incident words on some side. A small exact candidate is P_raw=[[2,2,5],[4,6,7],[2,3,6],[6,2,6]], Q_raw=[[1,2,5],[3,3,4],[1,4,1],[1,5,3]], H=4,Y=3, Khull=3, r=22/17, c=0. Compute all reachable optimal-face intervals through the EC48C encoder-component algorithm and produce an uncovered rational interval with an independently reproducible full component certificate if any; otherwise find another constructive decoder reconfiguration. A failed sufficient-condition test is not itself a ROC gap.

Local complete proof, executed original checker and full report are additionally preserved in bundle EM_R4_EC48H_TWO_FREE_20261027.zip, SHA-256 986048d40acccfada750f6f73af8e223864a3369b231dff09bb04819626aeb83.
