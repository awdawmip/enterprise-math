# Auxiliary N=14 iid sequential testing: exact stage87 affine segment

**2026-10-25. Author-side exact finite-model proof.** This is not a native BRC–Shor, Heartbeat/X6, physical, independently reviewed Driver, Lean or formally frozen Result claim.

## Mathematical statement

An arbitrary ordered-history randomized stopping rule observes at most 14 iid symbols 0,1,2, distributed as P=(1/8,1/24,5/6) or Q=(1/12,1/12,5/6). Errors eP=P(decide Q), eQ=Q(decide P); expected lengths tP=E_P T and tQ=E_Q T. Let V14(alpha) be the infimum of max(tP,tQ) with both errors at most alpha. Ordered, not just count-based, policies are in the feasible class.

Fix the stage86 endpoint alpha86=5172378783158315543/14900301753911083008, V86=24313786683642713729/1862537719238885376 and balancing S86=9865487497784809/13926400000000000, including the stage86 deterministic decision P at (12,3,0).

**Theorem (all real parameters).** For every 0<=delta<=eta87=32166875/77605738301620224,

V14(alpha86+delta) = V86-(50508/13)*delta.

The sharp right endpoint for this affine support is alpha87=5172378789334355543/14900301753911083008, V87=24313783684225133729/1862537719238885376.

## Global Bellman lower bound

For a state (n,a,b), where a and b count symbols 0 and 1, Q(prefix)/P(prefix)=2^(a+b)/3^a. All ordered prefixes sharing this state have identical iid conditional suffix distributions and the same likelihood ratio. The 14-horizon count-state domain contains sum_{n=0}^{14}(n+1)(n+2)/2=680 states.

Put K87=lambdaQ=26244/13, lambdaP=72+8*K87/9=24264/13, Gamma=50508/13. P-normalized Bellman costs are: stop P = lambdaQ*2^(a+b)/3^a; stop Q = lambdaP; continue = 1+sum_i P_i D(child_i), when n<14. Continuing is disallowed at n=14.

The stage86 frozen stopping table with A87=(13,7,3) and B=(12,0,1) set to continue is verified by backward exact rational recursion: 680 states, 1240 nonselected comparisons, 1238 strictly positive, 0 negative, exactly 2 zero gaps (A87: continue/P; B: continue/Q). Minimum positive gap = 177199183/4968677376. The exact root is

D0=3879046196983221230495/2848587100012412928
  =V86+Gamma*alpha86.

Bellman induction applies to every ordered-prefix rule, not only count policies: D0<=tP+lambdaP*eP+lambdaQ*eQ<=max(tP,tQ)+Gamma*alpha. Thus V14(alpha)>=D0-Gamma*alpha globally.

## Ordered history and branch-mass audit

The nominal multinomial number of prefixes at A87=(13,7,3) is 34320, but ordered first-hit DFS with the inherited stopping rule finds **19795 truly reachable first-hit prefixes**, with P mass pA=2474375/6262062317568 and Q mass qA=2474375/13374150672384. The continuation conditional tuple (P-error, Q-error, extra P-time, extra Q-time) at A87 is RA=(1/24,11/12,1,1). Its suffix has 3 terminal words, hence immediate P truncates 19795*3=59385 previously complete ordered histories. This word count is distinct from either probability mass.

For B=(12,0,1), 12 first-hit prefixes give pB=48828125/725594112 and qB=48828125/362797056; continuation tuple RB=(63/64,1/144,9/8,13/12), with 5 terminal suffix words. A87 and B have disjoint ordered cones: one draw after B raises its zero-symbol count from 0 to at most 1, not 7. Hence risk and expectation functionals are jointly affine in the two randomized stopping probabilities.

## Feasible primal equality on an entire continuum

Let u be the immediate-P probability at A87 and s the immediate-Q probability at B. At u=0,s=S86 the inherited stage86 optimum applies. Define exact positive masses

X=pA/24=2474375/150289495621632,
Y=qA/12=2474375/160489808068608,
E=pB/64=48828125/46438023168,
H=qB/144=48828125/52242776064.

The two error changes obey exact identities:

eP-alpha86=-X*u+E*(s-S86),
eQ-alpha86=+Y*u-H*(s-S86).

Choose s=S86+h87*u with h87=(X+Y)/(E+H)=3353273/208896000000. Then both errors equal alpha86+eta87*u, where eta87=-X+E*h87=Y-H*h87=32166875/77605738301620224>0. This randomized strategy exists for **every real** u in [0,1] because 0<S86<=s<=S87=29597133147954427/41779200000000000<1.

Exact endpoint calculations yield tP-tQ=724865489797595435/1241691812825923584 at u=0 and tP-tQ=2174599878250146305/3725075438477770752 at u=1. Both are strictly positive, and their affine interpolation is strictly positive on [0,1]. All chosen positive-mass actions minimize the Bellman costs, so tP+lambdaP*eP+lambdaQ*eQ=D0 identically. Consequently max(tP,tQ)=tP=D0-Gamma*(alpha86+eta87*u). Setting u=delta/eta87 proves global equality for every real delta in the stated interval. Sample-point checks alone are not used as a continuum proof.

## Sharp right endpoint

For alpha>alpha87 equality with this same supporting line would force eP=eQ=alpha (both multipliers are positive) and all positively reached chosen actions Bellman-minimal. The only possible randomizations are A87 and B: all other nonselected action gaps are strictly positive. On each same-count fiber, any history-dependent mixing reduces to an effective probability because the two likelihood weights are proportional and the continuation law agrees. The disjoint cones entail the same error identities, so equality of errors forces s=S86+h87*u and alpha=alpha86+eta87*u<=alpha87 for 0<=u<=1, contradiction. Finite-horizon randomized tests have a compact policy space, so an equality optimum cannot be evaded by a nonattained limit. This proves only the right-endpoint sharpness of this affine support, not absence of later optimal segments.

## Evidence, limitations, continuation

The author locally ran exact-Fraction derive87 and ordered-DFS crosscheck87_compatible (both byte-identical to published GitHub scripts) and an additional exact Bellman-minimum and ordered-DFS local check. Verification contains 680-state exhaustive Bellman comparisons, first-hit/suffix counts and masses, and eight exact rational interpolation consistency cases. Both published scripts share the predecessor stopping-action map; they are not an independent Driver proof. Branch counts are distinct from P/Q weights; no quotient of hidden native BRC path residuals is asserted. No transfer to native Heartbeat/BRC arithmetic is claimed.

Native task inventory produced CONTROL_QUOTA and native session_start was denied by STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Hence active owner, native CLAIM, Source-frozen Result and independent Driver acceptance are unverified. This note is a mathematical research artifact, not V2 formal task publication.

The next **unproved** directional candidate under stage87 policy is K88=483272799336/245952751, A88=(6,4,0), continue versus immediate P. See NEXT_TASK_PACKET_88.md for exact first-hit, cone overlap and Bellman proof obligations.
