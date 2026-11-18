# Stage273 — Exact global optimum and the entire real-parameter equality quadrilateral

2026-10-29. Scientific grade: PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. **Scope is solely an external ternary IID sequential-decision auxiliary model**. Neither a P000 native X6 theorem nor an approved Source CLAIM, Result or Driver review is asserted.

## Fixed sources, premises, and observer semantics

Parent: Stage272 exact author theorem at immutable Enterprise Math commit 4d077327bc4607ef9c59b50f1ff6610580d3fb4c, research_notes/n12_aux_iid_asymmetric_272_r2_author_20261029_1208_RESEARCH2/, Draft PR #1571. Current global read pin: 6be34baa3208779113a29ebb71bdccdfbe61770a. Current project-main read pin: 36d759ac27fdf4413bfe0c88e3774e64bf696409. The global P000_STARTUP projection references old canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, whereas the actually read original p000_reality_foundation.json at pinned project main has blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Consequently the original P000 and active native-X6/heartbeat, joint-observer and residual-preservation contracts were consulted instead of claiming that the old projection still byte-matched the live original. None is silently replaced by the auxiliary IID model.

Two IID sources P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6) emit alphabet {0,1,2}; the maximum number of observations is 12. **Any complete ordered-history randomized** stopping/decision policy is admitted. Observers are eP=P(declare Q), eQ=Q(declare P), tP=E_P[number of observations], tQ=E_Q[number]. For real caps a,b in [0,1], define V12(a,b) as the minimum max(tP,tQ) subject to eP<=a and eQ<=b, infinity when infeasible. These real caps do not claim native coordinates or physically calibrated time.

## Theorem 1: exact point optimum

At a273=298591185079/3962711310336, b273=48058313785/61917364224:

V12(a273,b273) = 89462343935/15479341056 (approximately 5.779467201565612).

Exact supporting Bellman multipliers and root value:

~~~text
lambdaP = 326994117632/2080594473 > 0
lambdaQ = 56789098740/693531491 > 0
(thetaP,thetaQ) = (0,1)
H = 1307211413240495165209/16103115723397791744
~~~

The explicit legal policy mix (49/100)Gplus+(49/100)Hplus+(1/50)K has the exact observer vector

~~~text
eP = 298591185079/3962711310336
eQ = 48058313785/61917364224
tP = 807441417617/165112971264
tQ = 89462343935/15479341056
tQ-tP = 440470753069/495338913792 > 0.
~~~

Both error caps are saturated and tQ = H-lambdaP*a273-lambdaQ*b273. The global dual bound below therefore matches the feasible primal value exactly.

## Theorem 2: exact Bellman dual over all ordered histories

For count state s=(i,j,k) write p_s=(1/8)^i(1/24)^j(5/6)^k and q_s=(1/12)^(i+j)(5/6)^k. At any single ordered prefix having counts s the two likelihoods equal p_s,q_s. Define the backwards Bellman recurrence:

~~~text
B_s = min{
  lambdaQ*q_s,                      declare P,
  lambdaP*p_s,                      declare Q,
  q_s + sum_{x=0,1,2} B_{s+e_x}    continue
}
~~~

The third action is unavailable at |s|=12. Backward induction **per ordered prefix**, not by presupposing a count-based decision policy, proves that the root B_(0,0,0)=H is the infimum of lambdaP*eP+lambdaQ*eQ+tQ over all complete ordered-history policies. For any cap-feasible policy:

~~~text
max(tP,tQ) >= tQ
          >= H-lambdaP*eP-lambdaQ*eQ
          >= H-lambdaP*a-lambdaQ*b.
~~~

The actually executed standard-library Fraction verifier covers **all 455 count states, 1274 legal action costs and 817 strictly positive action gaps**, with minimum positive gap 626146193/2748265083459889790976. The **only** exact ties are:

~~~text
T=(0,0,5): P or C;
S2=(1,2,5): Q or C.
~~~

There is no third tie hidden at any unreachable count state. Each deterministic equality policy chooses the unique Bellman action except at T and S2.

## Theorem 3: nested ties produce a full convex quadrilateral, not the old independent-coin parallelogram

T has just one reachable ordered history 22222. Under all fixed non-tie choices, there are exactly 55 ordered histories reaching S2 when T stops, and exactly 56 when T continues. Exactly one of those 56 S2 histories descends from T. These are exact count-versus-unmerged-path facts checked independently. Consequently these ties are **nested**, unlike the two incomparable ties at Stage272.

For any stochastic ordered-history equality policy, let r∈[0,1] be the probability of continuation at T. Let k be the total conditional continuation weight at S2 summed over all reached S2 histories, normalized by one full S2 word's unnormalized source likelihood. The preservation of both P and Q likelihood and the unchanged downstream suffix choices gives the precise feasible domain:

~~~text
0 <= r <= 1,
0 <= k <= 55+r.
~~~

Every (r,k) in this trapezoid is realizable: choose the T coin r, and choose the same conditional continuation probability k/(55+r) at all reachable S2 histories. Conversely, each full-history strategy obeys these bounds regardless of individual S2-history randomizations. Because all S2 words share exactly the same pair of unnormalized source likelihoods, their continuation increments coincide and their aggregate is linear in k. Hence the **entire four-observer equality set** is

~~~text
Obs(r,k)=Gplus + r*(Hplus-Gplus) + (k/55)*(K-Gplus).
~~~

The scaling is independently checked by the identity J-Hplus=(56/55)*(K-Gplus). It would be mathematically wrong to fix a universal S2 count of 55 after allowing continuation at ancestor T.

The four deterministic observer vectors, in order (eP,eQ,tP,tQ), are:

~~~text
Gplus=(187155450011/2641807540224,219610483345/278628139008,
       13822107249481/2972033482752,127792519715/23219011584)
Hplus=(211509050011/2641807540224,212768333345/278628139008,
       5091349349827/990677827584,140840869715/23219011584)
J=(630262400033/7925422620672,71000536115/92876046336,
   5097921299827/990677827584,47070914905/7739670528)
K=(557277756283/7925422620672,4579991515/5804752896,
   13841471030731/2972033482752,64078877045/11609505792)
~~~

Let R273 be their convex hull in the first two coordinates, with cyclic order Gplus, Hplus, J, K. The exact checker proves all four consecutive turn determinants are strictly negative. Its exact area is

~~~text
area(R273)=250592433271484375/46005119909369701466112 > 0.
~~~

It is a strictly convex **non-parallelogram**. Each corner has tQ>tP, hence every equality strategy has tQ>tP. We now have the complete all-real theorem:

**For every real (a,b) in [0,1]^2, V12(a,b)=H-lambdaP*a-lambdaQ*b if and only if (a,b) belongs to R273.**

For sufficiency, any cap pair in R273 corresponds to an admissible point (r,k) of the trapezoid, hence to a feasible full-history zero-gap policy saturating eP=a,eQ=b with tQ>tP. For necessity, equality forces exact saturation of both error caps because both lambdas are strictly positive, forces tQ=max(tP,tQ), and forces Bellman minimizers at every reached ordered prefix. The complete Bellman equality observer family projects exactly to R273. Since the finite ordered-history randomized strategy space is a compact product of finite simplices with continuous four-observers, the constrained optimum is attained whenever feasible, ruling out an exterior limiting equality. This establishes both directions of the **global** iff statement, not merely a finite set of sample caps.

R273 and the predecessor R272 share the *entire* Gplus—Hplus boundary: orient(Gplus,Hplus,Old_G)=+1161237529990234375/276030719456218208796672 and orient(Gplus,Hplus,K)=-372502265673828125/69007679864054552199168, with J on the same strict exterior side as K. Their interiors do not intersect.

## Independently executed verification and precise claim boundary

REPRO_STAGE273.py, the **actually executed** stdlib Fraction certificate, checks all action comparisons, four exact corners, dual-primal equality, the geometry and source-labelled probability normalization. An independent **unmerged ordered-history DFS** traversed 33328 word nodes and 22220 terminal branches for four deterministic corners, reproducing the count-state observer outputs and both P and Q terminal masses **exactly 1** for every policy. It also verified S2 reached-history counts 55 and 56, the one T-descendant S2 word, and the cross-policy factor 56/55. The verbatim stdout is saved as REPRO_STAGE273_EXECUTED_STDOUT.txt. The script uses no floating-point predicates and makes no assertion of a formal assistant checker, independent Driver review, unlimited horizon, physically measured randomness, or native BRC/X6 equivalence.

The BRC-compatible scientific use here retains both separately labelled positive rational P/Q masses and every ordered history multiplicity until the finite observer/suffix factorization is proved. Signed/complex cancellations, native X6 time, three-dimensional Cell layer, joint relation and Detector semantics were not reduced to this auxiliary model; a separate faithful bridge theorem remains necessary.

## Stage274 precise exterior witness: a new scientific problem

From the K policy, S3=(1,2,6) is reached on 80 ordered histories. K's action there is Q; changing S3 to continue on all 80 prefixes gives deterministic legal policy M:

~~~text
M=(183995918761/2641807540224,13758880795/17414258688,
   13862981030731/2972033482752,21429209015/3869835264).
~~~

Unmerged ordered DFS for M visits 9913 nodes and 6609 leaves, with both source masses exactly 1. Relative to the current dual its Lagrangian slack is strictly positive, 124418778359375/62902795794522624. The legal mixture 49/100 K +49/100 J +1/50 M gives

~~~text
a274=131763207049/1761205026816
b274=865980121505/1114512556032
tP=3234116608093/660451885056
tQ=538252197985/92876046336 > tP
~~~

Thus **V12(a274,b274) <= 538252197985/92876046336** is an *upper bound only*. The point is strictly across R273's K—J edge: orient(K,J,(a274,b274))=-8809426630859375/69007679864054552199168<0 while Gplus lies on the positive side. Stage274 must construct and check a *new* exact Bellman dual and full real equality region, or a rigorous obstruction. See NEXT_TASK_PACKET_274.md for the complete frozen input.

Scientific status: author exact for the declared finite external model, independent mathematical admission pending. Native service v0.6.11 reported research_authority_granted=false and em_control_tasks returned CONTROL_QUOTA, so no active owner confirmation, formal CLAIM, Source Result, or Driver acceptance is asserted.
