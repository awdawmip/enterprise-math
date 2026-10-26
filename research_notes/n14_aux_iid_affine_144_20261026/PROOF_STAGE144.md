# Stage144 — full-real exact N=14 affine optimum (AUTHOR computation-assisted proof)

**Scope and proof status.** This is a completed author exact-rational computation-assisted proof in an **external** ternary iid sequential decision model. It is not a P000, X6, Heartbeat, or native BRC–Shor theorem. Native task ownership, Result admission, and independent Research Driver review are not claimed.

## Statement

Take P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), maximum observation horizon N=14, and allow all policies using the **complete ordered history**, with randomized stopping/decisions. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), V14(alpha)=min max(tP,tQ) under eP,eQ<=alpha. Stage143 verified author endpoint is alpha143=1529836197244652353/4400701866044817408, V143=1503998623662640921/122241718501244928 (prior proof blob 28333392fa3ecda1721789b95f5f2a4d5375c3b8).

**Theorem.** For every real 0<=delta<=3799422101294299633/15301240388237830127616,

V14(alpha143+delta) = V143 - (814144/991)*delta.

The right endpoint is exactly alpha144=11043651203155499027/31745312008792178688, V144=192050982046273350485/15872656004396089344. This support is **strict** for every alpha>alpha144: it cannot be extended rightwards.

## Universal dual certificate

For s=(n,a,b), where a,b are counts of outcomes 0,1, Q(prefix)/P(prefix)=r(s)=2^(a+b)/3^a. Let K=412200/991 and L=401944/991. Recursively for all 680 count states, set H(s) to the minimum of K*r(s) (immediate decision P), L (immediate decision Q), and 1+sum_i P_i H(s+symbol_i) (continue, n<14). Backward exact Fraction recursion gives

Hroot=1347680099447446704127/4523958038641508352,

with precisely two action ties: B=(11,0,1), decision Q versus continue, and R=(11,2,0), decision P versus continue. The other 1238 nonchosen action gaps are strictly positive; the smallest is 392134385/79895973888, and none is negative.

This inequality applies to **any ordered-history policy**, not just count-Markov strategies: at every history the iid suffix law and likelihood-ratio-weighted cost are determined by the count state, and the policy is free to select its own conditional action. Thus the Bellman root is a universal lower bound

Hroot <= tP+L*eP+K*eQ <= max(tP,tQ)+(K+L)*alpha.

## Exact primal path computation

Use B immediate-Q coin w and R immediate-P coin z; everywhere else take the unique minimizing action. Both tied states have depth 11 and distinct counts, so no ordered history can hit both. Literal first-hit inventories, independently checked by integer-weight ordered-word DFS (P integer weights (3,1,20)/24, Q (1,1,10)/12), are:

B: 11 words, P mass 107421875/1451188224, Q mass 107421875/725594112.
R: 55 words, P mass 107421875/644972544, Q mass 107421875/1451188224.

Their masses independently agree with 11*P1*P2^10, 11*Q1*Q2^10, 55*P0^2*P2^9, 55*Q0^2*Q2^9. Same-depth disjoint cones imply zero mixed interaction and exact affine four-observer formula M(w,z)=M00+w*dB+z*dR, where M=(eP,eQ,tP,tQ). The vectors are:

M00:
303565407585151333/876488338465357824;
3498238126019/10030613004288;
1354275418302820519/109561042308169728;
39764599725665/3343537668096.

dB:
4619140625/2229025112064;
-751953125/417942208512;
-25673828125/278628139008;
-17939453125/104485552128.

dR:
-5048828125/8916100448256;
2470703125/2507653251072;
-66923828125/371504185344;
-17939453125/208971104256.

Independent literal ordered DFS checks all four deterministic corners (w,z)=(0,0),(1,0),(0,1),(1,1), visiting respectively 608608,608476,607948,607816 prefix nodes, and reproduces the four exact Fraction backward vectors. The four-corner mixed term equals (0,0,0,0).

From eP=eQ follows the **exact** coin compensation:

w(z) = 6345912551670737/10179840000000000 + (1159/2892)*z.

At z=0 it agrees exactly with Stage143's endpoint B coin. The unrestricted value w(1)=3475197517223579/3393280000000000 is >1, so **B saturates before R** at

zmax=3833927448329263/4079680000000000 (strictly between 0 and 1), w(zmax)=1.

For all real z in [0,zmax] both coins are feasible. The common error increases affinely by eta144 across this interval and tP decreases by (K+L)*eta144. At z=0, tP-tQ=80069565131574865/154712174978138112>0; at z=zmax, tP-tQ=2427895767318664589/5290885334798696448>0. Hence tP=max(tP,tQ) throughout the **whole real interval**. At both endpoints the exact equality tP+L*eP+K*eQ=Hroot holds, and by affinity it holds between them. This constructs a primal optimizer attaining the universal dual lower bound for every real alpha in the theorem.

## Strict right endpoint

The finite-horizon randomized policy space is compact. Were the same support attained for alpha>alpha144, positivity of K,L would force eP=eQ=alpha and every positive-probability selected action to minimize the local Bellman cost. The 1238 strict gaps prohibit mixing beyond B,R. A history-specific mixture at one tied count state is observationally equivalent to a single weighted effective coin because the prefix likelihood ratio and iid continuation observables agree for all its histories; the two tied first-hit cones are disjoint. Error equality forces w=w(z). Feasibility w<=1 implies z<=zmax, and the common error is then <=alpha144. Contradiction. Thus the support is strictly below the true V14 to the right.

## Evidence, limitations and next work

Actual local execution: exact Fraction Bellman for all states/gaps; Fraction backward four-observer recursions; a separate integer-weight ordered-prefix DFS for all four coin corners; exact first-hit combinatorics; endpoint dual equalities; whole-real affine interpolation; and right-sharpness argument. The executed package also contains the independent Stage145 dual-ray scan. Local validation printed PASS_STAGE144_ALL_EXACT_RATIONAL. The portable GitHub checker is **stored source**, not a claim of remote execution or independent review.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@eddc59ec31a539546c71e1e3aacd4ce43cc06a00, EnterpriseMath initial main@7830c42b911508d114c9550d05eb98c4fc649a84, Stage143 proof blob 28333392fa3ecda1721789b95f5f2a4d5375c3b8, P000 projected/original matched blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Authenticated GitHub actor is awdawmip, not a verified native Researcher/Owner. The external model has no proven observer-safe X6 mapping; formal project admission and independent mathematical review are pending. Next: Stage145 dual candidate and its original primal feasibility, in NEXT_TASK_PACKET_145.md.
