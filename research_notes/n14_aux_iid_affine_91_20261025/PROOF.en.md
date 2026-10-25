# N=14 auxiliary iid sequential tests — exact affine segment 91

**Date:** 2026-10-25. **Evidence status:** author-side exact finite-model proof with two locally executed exact-rational checks. Neither a native Task CLAIM / frozen Result nor an independent Research Driver review. No native BRC/X6/Heartbeat/P000 correspondence is asserted.

## Definition and theorem

Under iid hypotheses P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6) on alphabet {0,1,2}, allow **all** ordered-history-dependent randomized stopping/decision tests T<=14. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P T, tQ=E_Q T, and

V14(alpha)=inf { max(tP,tQ): eP<=alpha and eQ<=alpha }.

Fix the exact stage90 author-side endpoint and its inherited deterministic decisions, including immediate Q at A90=(7,2,3):

alpha90=5172392575267656743/14900301753911083008,
V90=24307271485812814529/1862537719238885376,
s90=29733408254700427/41779200000000000 at B=(12,0,1) (s means probability of immediately deciding Q).

**Theorem:** for **every real** delta in the interval
0<=delta<=eta91=7004684375/1616786214617088,

**V14(alpha90+delta)=V90-(8201136150/2241499)delta**.

Therefore alpha91=5172457130438856743/14900301753911083008 and
V14(alpha91)=24277747395672814529/1862537719238885376.
The displayed supporting line is sharp at its right endpoint.

## I. Universal Bellman dual over all ordered histories

Let lambdaQ=K91=4256337294/2241499, lambdaP=72+(8/9)K91=3944798856/2241499, Gamma=lambdaP+lambdaQ=8201136150/2241499. For state z=(n,a,b), meaning n samples, a zeros and b ones, the likelihood ratio Q/P is 2^(a+b)/3^a. Work with P-normalized conditional value D(z). At n<14 it is the minimum of:
- decide P: lambdaQ*2^(a+b)/3^a;
- decide Q: lambdaP;
- continue: 1+sum_i P_i*D(z+e_i).
At n=14 continuation is unavailable. Enumerating all 680 states with exact rational values yields 1240 alternative-action comparisons against the inherited deterministic table; 1238 have strictly positive gaps, 0 negative, and exactly two equalities: **C=Q at A91=(6,0,2) and C=Q at B=(12,0,1)**. The minimum strictly positive gap is 40045614911/35696427466752. Independent recursive min-Bellman calculation returns

D(0,0,0)=1260452162613076445424707977/982323867090880548569088
         =V90+Gamma*alpha90.

For every allowed history-dependent policy, the conditional iid suffix problem depends on the observed prefix only through (n,a,b). Consequently this recursion is globally minimizing, not merely a comparison within the inherited policy class. For every feasible test,
D(root)<=tP+lambdaP*eP+lambdaQ*eQ<=max(tP,tQ)+Gamma*alpha.
Hence V14(alpha)>=D(root)-Gamma*alpha.

## II. Exact BRC-style positive ordered path accounting

A91=(6,0,2) has 15 nominal ordered prefixes, and **all 15 first reach this state** without earlier termination. Direct first-hit DFS produces exact positive masses
pA=3125/248832; qA=3125/62208.
The original continue branch has 281 terminal suffix words (34 terminal state/action classes), so immediate stopping truncates **4215** complete ordered histories (not a probability mass). The old continuation's conditional tuple (P-error,Q-error,E_P further steps,E_Q further steps) is

RA=(338147645/339738624, 47177/53747712,
    66866185/42467328, 11952325/8957952).

For B=(12,0,1), 12 first-hit ordered prefixes have
pB=48828125/725594112; qB=48828125/362797056,
RB=(63/64,1/144,9/8,13/12), and five terminal suffix words.

**Disjoint cones:** any extension of A has at least two symbol-1 observations, whereas B has exactly one; B at depth 12 cannot occur before A at depth 6. Thus the two randomized choices never interact. Ordered multiplicity and separate exact P/Q positive rational masses are retained; this is typed weighted-BRC method reuse, not an assertion that this iid model is native Enterprise BRC.

## III. A primal witness for every real parameter in the interval

Let u in [0,1] be immediate-Q probability at A and s that at B. All other actions remain fixed. Put

X=pA*(1-RA[P-error])=4971809375/84537841287168,
Y=qA*RA[Q-error]=147428125/3343537668096,
E=pB*(1-RB[P-error])=48828125/46438023168,
H=qB*RB[Q-error]=48828125/52242776064.

Disjointness proves the following **symbolic exact identities**, not numerical interpolation:

eP=alpha90+X*u+E*(s-s90);
eQ=alpha90-Y*u-H*(s-s90).

The equal-risk line is
s=s90+h91*u, h91=-(X+Y)/(E+H)=-45097559/870400000.

Substituting gives eP=eQ=alpha90+eta91*u, eta91=7004684375/1616786214617088>0. At u=1,
s91=27568725422700427/41779200000000000;
indeed 0<s91<s90<1, so all real intermediate u yield probabilities in [0,1].

Sample-time difference tP-tQ is also affine in u, and its exact endpoints are
u=0: 2167774451913429905/3725075438477770752>0,
u=1: 2330264683137429905/3725075438477770752>0.
Thus tP dominates throughout. Every utilized decision minimizes the **same** Bellman recurrence, including both randomized ties, giving
tP+lambdaP*eP+lambdaQ*eQ=D(root).
Therefore tP=D(root)-Gamma*(alpha90+eta91*u), attaining the universal lower bound for **every real u in [0,1]** and proving the theorem.

## IV. Right-end sharpness for arbitrary randomized history dependence

All finite-horizon randomized tests have a finite occupation-measure polytope, so optimal solutions exist. Suppose for alpha>alpha91 equality were attained in this same dual supporting line. Both multipliers are positive, hence both errors must equal alpha and every reached action must be dual-minimizing. The above exact Bellman gaps force all actions except the two ties to be deterministic. History-dependent randomness across distinct prefixes sharing A or B can be replaced by their P-mass-weighted aggregate u,s: the same count-state has a common Q/P likelihood ratio and the same frozen conditional continuation. This retains eP,eQ,tP,tQ. Disjoint cones then force s=s90+h91*u and alpha=alpha90+eta91*u<=alpha91, contradiction. The line cannot remain attained to the right.

## Exact checks, inheritance, and scope

Locally execute `python derive91.py` and `python crosscheck91.py` with unchanged predecessors `derive90.py`, `derive89.py`, `derive88.py`. `derive91.py` performs exact-rational global Bellman comparisons and forward probability/time propagation; `crosscheck91.py` independently enumerates ordered first hits and terminal suffix words, and recomputes 680-state min-Bellman. Both pass, including independent archive-extraction reruns, and agree on all fractions above. They share the inherited stop table and are **not independent Driver review**. The locally archived expanded proof and Chinese summary are supplied in the user research package.

Provenance: GLOBAL_KNOWLEDGE_V1 main c05ac6c5ad57a109c2d5bd71d7822b5be2abbd87; project control read main 90494b2b08a18150d701db1ca0e04182ad83facc. Parent stage90 source c7d817f58665248c3269c5cbe78e4d3acd1e17f8; its `derive90.py` Git blob is b4ce38a74fac162647d01279215c0c26d622a5a3. Native owner read returned CONTROL_QUOTA; attempted native session start was denied STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Hence ownership, formal CLAIM and independent acceptance are **unverified**, not implied by this source note.

**Next candidate only:** K92=551124/295 at A92=(12,8,3), C versus immediate P. This is not a proven 92nd affine interval.
