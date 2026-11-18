# Stage274 — Exact Bellman optimum and complete real-parameter equality quadrilateral

Date: 2026-10-29. Result level: **PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. Scope: finite *external ternary IID sequential-decision auxiliary model* only. This is not a theorem about P000 native X6/heartbeat dynamics and is not a native Source CLAIM, Result, independent review or task acceptance.

Parent: Stage273 at immutable commit 90b7a69c5cf6d8b4893b8529930170d822ed7646, Enterprise Math Draft PR #1571. Fixed GLOBAL_KNOWLEDGE_V1 read main@6b4d9d4cd4624b6d5b14eafbad2fc321c20f1fcf and Enterprise Math main read 7077ed6a37db2b05bf0e43aa640e56f8fb0024c5. The global P000 original/mirror (blob 770e1b15..., V4) and project P000 original (blob bcc2590d..., V5) are different revisions; the current project P000 and ACTIVE native-worldview constraints were also read and retained as separate project premises. No P000 or protected worldview file is changed. Current service v0.6.11 reports research_authority_granted=false and the live owner query returned CONTROL_QUOTA, so author-side GitHub evidence is not a formally owned execution.

## 1. Exact finite problem and Bellman certificate

Let P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6) be IID laws on alphabet {0,1,2}. A policy, possibly randomized and dependent on the **entire ordered history**, must stop and declare P or Q by observation N=12. Define the four observers eP=P(declare Q), eQ=Q(declare P), tP=E_P[observations], tQ=E_Q[observations]. For real caps a,b in [0,1], V12(a,b) is inf max(tP,tQ) over policies with eP<=a,eQ<=b, and +infinity when infeasible.

The exact supporting Bellman multipliers are:

~~~text
lambdaP = 445906494464/2706255861 > 0
lambdaQ = 76440567684/902085287 > 0
(thetaP,thetaQ) = (0,1)
H = 1758667527952600918633/20945528728608964608.
~~~

At count state s=(i,j,k), let p_s=(1/8)^i(1/24)^j(5/6)^k and q_s=(1/12)^(i+j)(5/6)^k. At each ordered prefix of these counts, the Lagrangian action costs are

~~~text
D_P(s)=lambdaQ*q_s            # declare P
D_Q(s)=lambdaP*p_s            # declare Q
D_C(s)=q_s+sum_x B(s+e_x)    # continue, only for |s|<12
B(s)=min available D(s).
~~~

For each *individual ordered prefix*, reverse induction shows B(s) is the minimum continuation Lagrangian cost over all suffix policies, including full-history randomized policies. IID makes the two unnormalized prefix masses and future suffix law depend only on counts, so the count-state recursion is a lossless computation of the **optimum**, not an assumption that the allowed policies are count-measurable. At the root B(0,0,0)=H. Every cap-feasible policy obeys

~~~text
max(tP,tQ)>=tQ>=H-lambdaP*eP-lambdaQ*eQ>=H-lambdaP*a-lambdaQ*b.
~~~

The **actually executed**, standalone stdlib Fraction script REPRO_STAGE274.py checks all 455 states, all 1,274 legal action costs, exactly 817 strictly positive action gaps, smallest strictly positive gap 3894944411/10724110709047789879296, and precisely two equal-minimum action pairs: T=(0,0,5) has P/C, S3=(1,2,6) has Q/C. Former Stage273 S2=(1,2,5) now uniquely continues; S4=(1,2,7) uniquely declares Q. There are no uninspected states or floating-point tie predicates.

## 2. Four exact equality policies and source/path preservation

At every non-tie state choose the unique Bellman minimizer. Define the four deterministic policies K=(T:P,S3:Q), J=(T:C,S3:Q), Jnew=(T:C,S3:C), M=(T:P,S3:C). Their exact observed vectors, always in order (eP,eQ,tP,tQ), are:

~~~text
K    =(557277756283/7925422620672,4579991515/5804752896,
       13841471030731/2972033482752,64078877045/11609505792)
J    =(630262400033/7925422620672,71000536115/92876046336,
       5097921299827/990677827584,47070914905/7739670528)
Jnew =(624774025033/7925422620672,213315452095/278628139008,
       5105360174827/990677827584,141645900965/23219011584)
M    =(183995918761/2641807540224,13758880795/17414258688,
       13862981030731/2972033482752,21429209015/3869835264).
~~~

The separate **unmerged complete ordered-history** DFS finds S3 on exactly 80 reached prefixes when T stops and 83 when T continues. Exactly 3 of the latter 83 histories descend from the unique T prefix word 22222. This nesting invalidates any assumption of an independent rectangular two-coin parameter domain.

Let r in [0,1] be the continuation probability at T. Among the 80 always-reached S3 words plus the three T-descendant words (whose survival weight is r), let k be the summed *conditional continuation weight*, normalized in units of one reached S3 word's prefix mass. The exactly realizable domain is

~~~text
0 <= r <= 1; 0 <= k <= 80+3*r.
~~~

Why the four observers factor through r,k: every S3 prefix has the same pair of rational p_S3,q_S3 source masses, and (after that state) every allowed continuation has the same modelled suffix observers. Therefore every S3-continuation event has one identical four-observer increment per unit of reached-prefix probability. The 80 always-reached words contribute their conditional coins, and the 3 T-descendant words contribute r times their conditional coins. The complete four-observer family is exactly

~~~text
Obs(r,k) = K + r*(J-K) + (k/80)*(M-K).
~~~

In particular, 80*(Jnew-J)=83*(M-K) in **all four coordinates**, checked exactly. Conversely for any (r,k) satisfying the domain, use coin r at T, then coin k/(80+3r) at each reached S3 history. The denominator is >=80. This constructs the desired observers for every parameter pair. Necessity holds for any full-history randomized policy, by conditional expectation and the common source-prefix masses; path identifiers and conditional survival are retained through this argument.

## 3. Strictly convex all-real optimality region

Let R274 be the convex hull of the first two error coordinates of (K,J,Jnew,M) in that cyclic order. The four consecutive exact oriented turns are:

~~~text
-3655912051806640625/552061438912436417593344
-3655912051806640625/552061438912436417593344
-220235665771484375/34503839932027276099584
-220235665771484375/34503839932027276099584.
~~~

All turns are strictly negative, so R274 is a nondegenerate strictly convex **non-parallelogram** quadrilateral, area

~~~text
area(R274) = 7179682704150390625/1104122877824872835186688.
~~~

It shares the entire K--J side with Stage273's R273 and has disjoint interior: orient(K,J,M)=-220235665771484375/34503839932027276099584, while Stage273's Gplus satisfies orient(K,J,Gplus)=+372502265673828125/69007679864054552199168. Both polygons are convex on opposite sides of that supporting line.

All four corner policies have tQ>tP, and by convexity every equality policy also has tQ>tP. Thus the central theorem is:

**For every real (a,b) in [0,1]^2,**

~~~text
V12(a,b) = H-lambdaP*a-lambdaQ*b    iff    (a,b) belongs to R274.
~~~

Sufficiency: the exact (r,k) trapezoid maps affinely onto R274, with every point realized by a full ordered-history zero-gap policy saturating eP=a and eQ=b. Its tQ=max(tP,tQ) matches the dual lower bound. Necessity: the finite ordered-history randomized policy space is a compact product of finite action simplices; continuous four-observer maps and closed error caps imply an attaining minimizer whenever feasible. Equality in the dual chain, with lambdaP,lambdaQ both strictly positive, forces both caps to saturate and every reached prefix to use only a Bellman-minimizing action. The complete equality observer family then requires (a,b) in R274. Infeasible caps have +infinity value, not the finite affine expression. Hence the iff covers **all real error caps**, not sampled grid points.

At the Stage274 prescribed point

~~~text
a274 = 131763207049/1761205026816
b274 = 865980121505/1114512556032
~~~

the legal strictly positive policy mixture (49/100)K+(49/100)J+(1/50)M saturates both caps and has

~~~text
tP = 3234116608093/660451885056
tQ = 538252197985/92876046336
tQ-tP = 5341091198203/5944066965504 > 0.
~~~

The exact identity tQ=H-lambdaP*a274-lambdaQ*b274 matches the global dual bound. Therefore

**V12(a274,b274)=538252197985/92876046336 (approximately 5.795382331820538).**

## 4. Actually executed cross-checks, evidence level and next open unit

REPRO_STAGE274.py checks count-state observers against an **independent unmerged full-word DFS**, without compressing word identities. Four corner policies traverse 37,948 nodes and 25,300 terminal words; each has *both P and Q terminating mass exactly 1*. A fifth Stage275 witness increases the audit to 48,521 nodes and 32,349 terminals across all five strategies. The captured verbatim output REPRO_STAGE274_EXECUTED_STDOUT.txt contains STAGE274_EXACT_ALL_REAL_FACE_PASS. The proof's universal real-cap statement depends on Bellman induction, the exact two-tie characterization, the source/probability-preserving parameterization, and compactness, not on checking finitely many real caps.

BRC reuse here is exactly labelled **positive rational P/Q source mass**, ordered path identity and multiplicity, with state quotient justified only for this stated finite observer/suffix law. There is no signed phase-cancellation claim, native 3D slice embedding, native X6 event reconstruction, physical time calibration, or infinite horizon statement. Independent mathematical review, formal Lean checking and Source admission remain open. The GitHub author-side evidence does not imply task ownership.

**Stage275 exterior feasible witness:** at S4=(1,2,7) the Stage274 action is uniquely Q. Change only S4 from Q to C in M to form M2:

~~~text
M2=(545662756283/7925422620672,9188342405/11609505792,
    13885256030731/2972033482752,64511064545/11609505792).
~~~

An independent full-word DFS for M2 visits 10,573 nodes and 7,049 terminal words; P/Q terminal masses are 1. Its Stage274-dual Lagrangian slack is **strictly positive** 1798033664453125/654547772769030144. A legal mixture (49/100)M+(49/100)Jnew+(1/50)M2 has

~~~text
a275 = 1175053055941/15850845241344
b275 = 867218405255/1114512556032
tP275 = 1079662613531/220150628352
tQ275 = 539955234235/92876046336 > tP275.
~~~

orient(M,Jnew,(a275,b275))=-39140485205078125/276030719456218208796672 < 0 while orient(M,Jnew,K)>0: this is strictly exterior to R274 across the M--Jnew side. Hence **only** the feasible upper bound V12(a275,b275)<=539955234235/92876046336 is presently proved, not optimality. The next unit should derive a new exact dual (try T and S4), verify the complete action gap/tie set, preserve nested ordered-prefix reach weights, and give a matching primal or a certified obstruction. Full frozen inputs and acceptance criteria are in NEXT_TASK_PACKET_275.md.
