# Stage272 — exact full-real Bellman face across Stage271 G–Hcorner

**Status (2026-10-29): PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.** External ternary IID auxiliary model; no P000-native X6 correspondence or native BRC operations asserted. This is author evidence, not Source CLAIM/Result or Driver acceptance.

## Provenance and model

Frozen parent: Stage271 immutable commit 7baad56778920772e5ebc447822b7b2bf6481d48, Enterprise Math Draft PR #1571, research_notes/n12_aux_iid_asymmetric_271_r2_author_20261029_1159_RESEARCH2/PROOF_STAGE271.md and NEXT_TASK_PACKET_272.md. Current read pins: GLOBAL_KNOWLEDGE_V1 main@f061d573d7c6f17357ad591aa8b33a89cd9901f4, Enterprise Math main@216aacba1f26493122830eb0d4c241318d208bc3. Global entry/manual, project router, P000 original (blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc) and matching startup projection, ACTIVE worldview, mathematical/source/code policies and portable research rules were read. Native v0.6.11 returned research_authority_granted=false; owner query em_control_tasks returned CONTROL_QUOTA. Consequently no native owner/CLAIM is asserted.

Observations are IID under P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), alphabet {0,1,2}; maximum horizon N=12. Arbitrary randomized sequential decisions based on the **entire ordered observation history** are permitted. Observers are (eP,eQ,tP,tQ) with eP=P(declare Q), eQ=Q(declare P), and tP,tQ the two expected observation counts. For real caps a,b in [0,1], V12(a,b)=min max(tP,tQ) over policies with eP<=a,eQ<=b, infinity if infeasible.

## Point theorem: exact global optimum

At
~~~
a272=2401128349757/31701690482688
b272=288133328335/371504185344
~~~
the optimal value is EXACTLY
~~~
V12(a272,b272)=535594465735/92876046336
             =5.766766425407112...
~~~
Matching global dual:
~~~
lambdaP=7694718574592/50961738459 > 0
lambdaQ=1351613187036/16987246153 > 0
thetaP=0, thetaQ=1
H=1945350813734366428859/24651691575422902272.
~~~

A feasible exact randomized policy has
~~~
(eP,eQ,tP,tQ)=
(2401128349757/31701690482688,
 288133328335/371504185344,
 6452413254061/1320903770112,
 535594465735/92876046336).
tQ-tP=10484372327531/11888133931008 > 0.
~~~
Both errors saturate their caps and tQ=H-lambdaP*a272-lambdaQ*b272, proving primal–dual equality. This upgrades Stage271's certified *upper bound* into a Stage272 *global optimum*.

## Four exact Bellman equality policies and all-real theorem

Stage271's G-corner has action C at U=(1,2,3), P at T=(0,0,5). New tie S=(1,2,4): Q/C. Define r to choose C rather than P at T and u to choose C rather than Q at S. The unique Stage272 Bellman choice is used at all other states. The four complete ordered-history deterministic policy observers (eP,eQ,tP,tQ) are:
~~~
G=Obs(0,0):
1129087690691/15850845241344,146299619105/185752092672,
27612319764587/5944066965504,84999370435/15479341056

Hcorner=Obs(1,0):
1275209290691/15850845241344,425214557315/557256278016,
10172067121529/1981355655168,93698270435/15479341056

Gplus=Obs(0,1):
187155450011/2641807540224,219610483345/278628139008,
13822107249481/2972033482752,127792519715/23219011584

Hplus=Obs(1,1):
211509050011/2641807540224,212768333345/278628139008,
5091349349827/990677827584,140840869715/23219011584
~~~
All four vector coordinates satisfy Hplus-Hcorner=Gplus-G. The projected error geometry is the strictly convex parallelogram
~~~
R272=conv(G,Hcorner,Hplus,Gplus).
area=1161237529990234375/276030719456218208796672 > 0.
~~~
**For EVERY real (a,b) in [0,1]^2:**
~~~
V12(a,b)=H-lambdaP*a-lambdaQ*b
          IF AND ONLY IF (a,b) belongs to R272.
~~~
The shared G—Hcorner edge with R271 is *complete*. Relative to directed G—Hcorner, the old E vertex and new Gplus vertex have opposite, nonzero orientations:
~~~
orient(G,Hcorner,Old_E)=
 +101268766501953125/34503839932027276099584
orient(G,Hcorner,Gplus)=
 -1161237529990234375/276030719456218208796672.
~~~
The regions' interiors do not overlap.

## Proof for ALL randomized ordered-history strategies

For count state s=(i,j,k), use unnormalized likelihoods p_s=(1/8)^i(1/24)^j(5/6)^k, q_s=(1/12)^(i+j)(5/6)^k. For any ordered word with counts s, the Bellman recurrence is
~~~
B_s=min{lambdaQ*q_s (declare P),
        lambdaP*p_s (declare Q),
        q_s+sum_{x=0,1,2} B_{s+e_x} (continue)}.
~~~
Continuation is not legal at depth 12. Every ordered prefix with counts s has identical source likelihoods and child-action recurrence. Backward induction proves the count quotient gives the **full-history** optimum: the state quotient does not assume strategies are count-measurable. The root is exactly H. Therefore for EVERY full-history randomized policy:
~~~
lambdaP*eP+lambdaQ*eQ+tQ >= H,
max(tP,tQ)>=H-lambdaP*a-lambdaQ*b
~~~
whenever error caps are met.

Exhaustive exact Fraction Bellman recurrence covers 455 count states and 1274 legal action costs. 817 action gaps are strictly positive, with minimum 110379031/934938228638261182464, and the ONLY ties are T=(0,0,5):P/C and S=(1,2,4):Q/C. The two tie families are **incomparable** as T already contains 5 symbol-2 occurrences but S has only 4; T cannot precede S and S is deeper than T, so S cannot precede T. Under the otherwise unique optimal decisions T is reached by 1 ordered prefix and S by 35. Every S prefix has identical likelihood and identical optimal suffix observations. Any arbitrary history-specific randomization on these S words therefore has the same four observers as their mean continuation coin u in [0,1]. T contributes an independent coin r; no mixed r*u coefficient survives. Hence the **entire four-observer equality set** is exactly
~~~
Obs(r,u)=G+r*(Hcorner-G)+u*(Gplus-G),
0<=r,u<=1.
~~~
At the point caps the exact parameters are r=49/100,u=1/50, both interior. Each deterministic corner has tQ>tP and this inequality is preserved by all convex mixtures.

For any (a,b) in R272, choose its r,u and attain the dual equality with the cap errors. Conversely, equality to the affine lower bound forces tQ to support the max, both errors to saturate (both lambdas >0), and all positive-mass actions to have zero Bellman gap; the projected errors must therefore lie in R272. A finite ordered-history randomized decision tree has compact product action simplices and continuous observers, so feasible minima are attained: no exterior limiting equality is possible. This closes the real-parameter iff rather than checking finitely many caps.

## Executed certificate and source boundaries

REPRO_STAGE272.py is the exact **actually executed** standard-library Python Fraction program; REPRO_STAGE272_EXECUTED_STDOUT.txt is its verbatim stdout. Both source-labelled P/Q positive rational masses are propagated by (a) count-state integer ordered-word multiplicity flow and (b) independent unmerged ordered-word DFS. All four deterministic corners match exactly; P and Q terminal masses each equal 1. Full DFS traversed 27,304 word nodes and 18,204 terminal branches over four corners. Execution reports STAGE272_EXACT_ALL_REAL_FACE_PASS. SHA256 of executed source: a65f25cba3f9805e70fc41ae0c1ff52b945e02e93e221ca5828c9aa9bd49cfd9. SHA256 of stdout: 0476d4775db35add71383554f8e04dcf0bb90cfe7f257309c8cc7d6c4d79cf9f.

This is a BRC-compatible **provenance/multiplicity handling principle**, not native typed BRC arithmetic. It neither proves observer preservation under arbitrary future X6 updates nor a P000-native three-dimensional-slice transfer. A native bridge needs six-axis ordered path encoding, third-coordinate semantics, typed joint/phase residual carrier, readout and operation-composition preservation.

## Exact next exterior witness: Stage273

Starting from Gplus, change action at S2=(1,2,5) from Q to C on all 55 reached ordered prefixes (all other actions unchanged), giving K:
~~~
K=(557277756283/7925422620672,
   4579991515/5804752896,
   13841471030731/2972033482752,
   64078877045/11609505792).
~~~
Independent ordered DFS checks 8,953 nodes, 5,969 leaves and exact P/Q mass. Mix 49/100 Gplus +49/100 Hplus +1/50 K, yielding
~~~
a273=298591185079/3962711310336
b273=48058313785/61917364224
tP=807441417617/165112971264
tQ=89462343935/15479341056 > tP.
~~~
This proves **feasibility only**: V12(a273,b273)<=89462343935/15479341056. It is strictly outside R272 across the Gplus—Hplus edge, since orient(Gplus,Hplus,(a273,b273))=-14900090626953125/138015359728109104398336, while G is on the positive side. K's old Stage272 Lagrangian slack is +267636139496515625/197213532603383218176. The next unit must find a matching *new* Bellman dual and all-real equality set, or an exact obstruction; see NEXT_TASK_PACKET_273.md.
