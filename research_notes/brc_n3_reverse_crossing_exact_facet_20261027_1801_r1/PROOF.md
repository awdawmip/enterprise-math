# BRC N=3 reverse-crossing: exact rational facet, gap 1, and a certified open neighborhood

2026-10-27. Author-side portable TASK_RESEARCH, local Researcher-ID EM-R1-1801A (not a native MCP-issued session/CLAIM). UNREVIEWED / NOT_ADMITTED. External finite two-law probability-tree mathematics; a native P000 X6 Cell/time-dynamics translation is an independent proof obligation.

## Frozen sources and typed question
GLOBAL_KNOWLEDGE_V1 main@2414567d90987b6d6a679499b53217b6734a6bb2 (Bootstrap, Manual, ACTIVE worldview and P000); Enterprise Math input main@c886dd8068ee104b855d6a567fe0323655a7726b (p000_reality_foundation.json, HEARTBEAT_WORLD_NATIVE_X6_TIME.json, JOINT_RELATION_OBSERVER_PRESERVATION and portable-research protocol). Direct predecessor: [2026-10-27 high-side proof](https://github.com/awdawmip/enterprise-math/blob/6af784d967caee16ac1aec4d002bc6de41b94292/research_notes/brc_n3_highside_one_sided_support_phase_20261027_emr1_r11/PROOF.md). The remaining rational point was (s_a,s_b)=(2/5,1/3); the predecessor support vector has zero gap there.

Declare two strictly positive laws P,Q, stopping horizon N=3, ordered branch histories, common stop-P/stop-Q/continue behavioral policies, independent fresh random action at each current-state visit, and terminal observer
O=(P(D=Q), Q(D=P), E_P[T], E_Q[T]).
The compressed strategy sees only (t,r=P/Q), not the ordered prefix, and carries no persistent hidden seed. Complete-history strategies see the prefix. BRC use: positive rational branch mass plus labeled provenance, with the quotient tested against the declared observer and future-action class.

Frozen exact model (Q,P masses in units 1/240):
| prefix | t | state | Q | P | children |
|---|---:|---:|---:|---:|---|
| root |0|0|240|240|a,b|
| a |1|2|120|180|ax,ay|
| b |1|1|120|60|bu,bv|
| ax |2|4|60|60|axL,axM,axH|
| ay |2|5|60|120|ayT|
| bu |2|4|30|30|buL,buM,buH|
| bv |2|3|90|30|bvT|
| axL,axM,axH |3|7,8,9|24,12,24|12,12,36|leaves|
| ayT |3|10|60|120|leaf|
| buL,buM,buH |3|7,8,9|10,10,10|5,10,15|leaves|
| bvT |3|6|90|30|leaf|

At ax and bu, the common current r=1 and state 4 erase their distinct Q-conditional future probabilities (2/5,1/5,2/5) and (1/3,1/3,1/3), although both have child r=(1/2,1,3/2). Every path weight is positive and both mass-conservation identities hold.

## Theorem 1 (sharp rational supporting inequality and strict witness)
For every compressed behavioral policy,
\[
\boxed{874O_1+1131O_2+121O_3-53O_4\ge 851.}\tag{1}
\]
There is a complete-history strategy giving
\[
\boxed{O_F=(7/20,7/20,19/8,21/8),\quad J(O_F)=850.}\tag{2}
\]
Consequently the sharp support gap for this normal is exactly 1 and O_F lies outside even the compressed observation convex hull.

Proof. Normalize local Bellman costs by the prefix Q mass and put r=P/Q. The immediate decision costs at a node are 1131 (stop-P) and 874r (stop-Q). Continuing one observation adds 121r−53 plus the next Q-conditional Bellman value. A terminal ratio r has m(r)=min(1131,874r), in particular m(1/2),m(1),m(3/2)=(437,874,1131).

For a collision-history state (t=2,r=1) with conditional branch probabilities (s,1−2s,s), the three action costs are exactly
(stop-P, stop-Q, continue) = (1131,874,942−180s).
Thus at ax the three numbers are (1131,874,870), while at bu they are (1131,874,882). Independently, the noncollision states ay and bv have values 1131 and 836/3, respectively. If a or b continues, its additional time costs are 257/2 and 15/2, and its Q-conditional child probabilities are (1/2,1/2) and (1/4,3/4).

Full-history optimization chooses continue at ax, stop-Q at bu, giving V(a)=1129, V(b)=435, and root value 68+(1129+435)/2=850, below immediate root stop-Q cost 874.

Compression forces ax and bu to use the same action. Enumerating the forced action as stop-P, stop-Q, continue and optimizing all remaining state actions by Bellman gives root minima, respectively, 852, 851 and 851. Hence the compressed minimum is exactly 851.

A complete-history policy reaching 850 is: root,a,b,ax,bv continue; ay stop-P; bu stop-Q; terminal axL,axM,buL,buM,bvT stop-Q; axH,buH,ayT stop-P. Under this policy (whether or not the unreachable bu children are assigned), direct rational accumulation yields 240 O=(84,84,570,630), proving (2).

Each time-labelled compressed state is visited at most once per trajectory. For any fixed values of other randomized action tables, J is affine in one state's action probabilities. Its minimum over the product of state-action simplices is therefore attained at deterministic vertices. Equivalently, independent pre-drawing of each state's pure action represents behavioral observations as a mixture of deterministic tables. This establishes (1) for every real randomized policy in the declared seedless class. QED.

## Theorem 2 (genuine four-dimensional facet)
There are 6 compressed nonterminal states, each with 3 actions, and 5 compressed terminal states, each with 2 decisions. All 3^6*2^5=23,328 pure tables were enumerated with exact integer arithmetic (scale 240); their 326 distinct four-dimensional observer vectors have minimum J=851. Exactly four distinct vectors attain equality, in unscaled integer 240O coordinates:
(84,84,480,420), (60,120,330,450), (120,60,510,570), (69,94,600,660).
Relative to the first vector, the other three difference vectors' first-three-column determinant equals −95400, hence the supporting face has affine dimension 3. Five reachable vectors
(0,240,0,0),(240,0,0,0),(0,240,240,240),(180,120,240,240),(0,240,420,360)
have full 4x4 difference determinant 207360000, proving the convex hull has dimension 4. Therefore (1) defines a proper facet rather than only a non-sharp inequality.

## Theorem 3 (explicit certified parameter neighborhood)
Preserve the same tree and likelihood-ratio labels while allowing (s_a,s_b) throughout 0<s_a,s_b<1/2. Write C and F for the two exact minimum J values. Then
\[
\boxed{C(s_a,s_b)-F(s_a,s_b)\ge
1-347|s_a-2/5|-(347/2)|s_b-1/3|.}\tag{3}
\]
Every parameter pair in the corresponding strict-positive open diamond retains observable compression loss.

Proof. For any fixed pure strategy, dependence on each s occurs only in the three terminal descendants of the corresponding collision history, or vanishes when the history is not continued to those descendants. At time 3 the two possible terminal costs per unit Q mass at r=1/2,1,3/2 are respectively (459.5,1153.5), (1078,1335), (1516.5,1696.5). Therefore |f(1/2)−2f(1)+f(3/2)|<=694 for all terminal decision combinations. Multiplying by the Q masses 1/4 for ax and 1/8 for bu bounds the slopes of every pure strategy by 347/2 and 347/4. Minima of a finite family of functions with these uniform coordinatewise Lipschitz bounds satisfy the same bounds. Both C and F therefore differ from their central values by at most (347/2)|Δa|+(347/4)|Δb|. Their central difference is 1, and subtracting the two deviations gives (3). The multi-affine reduction extends this to real behavioral randomization. QED.

## Verification, method reuse and limits
VERIFY.py is a reproducible standard-library exact-rational/integer checker. It checks positive probability masses, conservation, all 23,328 pure compressed tables, 326 distinct vectors, the four facet equality points, rational affine dimensions 3 and 4, full-history Bellman and witness, and the three forced shared collision actions. RESULT.json records its expected exact values. The formula for the entire open neighborhood follows from the analytic slope bound rather than a finite grid.

Method resolution: REUSE_APPLIED, prior BRC ordered-weighted paths and finite backward Bellman from the frozen [high-side proof](https://github.com/awdawmip/enterprise-math/blob/6af784d967caee16ac1aec4d002bc6de41b94292/research_notes/brc_n3_highside_one_sided_support_phase_20261027_emr1_r11/VERIFY.py); no novel general-purpose tool interface claimed. The external finite tree has no proved native six-dimensional X6 Cell/three-dimensional-slice/time-preserving translation, no native CLAIM/Result, no independent Driver review or Lean check. Preserve P000 ontology, unique Cell/address semantics and native triadic closure without promoting this auxiliary proof to physical law.
