# Stage145 — exact N=14 full-real affine optimum (AUTHOR COMPUTATION-ASSISTED PROOF)

**Statement, scope and provenance.** The result concerns an **external** three-symbol iid sequential decision problem, not native Enterprise Math P000/X6/Heartbeat nor BRC–Shor. Independently verified author computations do not constitute independent Research Driver review or native Result admission. Frozen source: GLOBAL_KNOWLEDGE_V1 \`eddc59ec31a539546c71e1e3aacd4ce43cc06a00\`; initial Enterprise Math \`7830c42b911508d114c9550d05eb98c4fc649a84\`; exact Stage144 predecessor author proof at \`bc33991a8dda3a29975c9b2e5541fed11899e657\`.

For P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), maximum stopping depth N=14, allow randomized strategies based on **all complete ordered ternary histories**. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau and V14(alpha)=min max(tP,tQ) under eP,eQ<=alpha. The Stage144 author endpoint is

alpha144=11043651203155499027/31745312008792178688,
V144=192050982046273350485/15872656004396089344.

**Theorem (new).** For every real number

0 <= delta <= eta145=14352537267262223320799/730252970868387684393418752

one has the **exact equality**

V14(alpha144+delta) = V144 - (141756976212/175207181)*delta.

The right endpoint is

alpha145=61650988568176660266901/177207634216336528244736,
V145=34260854261470059183743591/2835322147461384451915776.

The associated support is **strictly below** V14(alpha) at every alpha>alpha145, i.e., cannot be extended to the right.

## Universal dual certificate

Let state s=(n,a,b) record depth and numbers of the first two outcomes. The ordered prefix likelihood ratio is r(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a. For K=72079793676/175207181 and L=69677182536/175207181, let H(s) be the backward min of decision P cost K*r(s), decision Q cost L, and 1+sum_i P_i H(child_i) if n<14. An exact Fraction calculation over **all 680 count states** gives

Hroot=704405532029576180110108633/2399485171279518914052096.

The *only* ties are R=(11,2,0), P/continue, and T=(7,1,2), Q/continue; the remaining **1238** nonchosen action gaps are strictly positive, smallest 13737326062879/1569497517453312. No negative gaps. By iid suffix sufficiency and historywise conditional minimization, backward induction bounds *all* randomized ordered-history policies, not only count-Markov policies:

Hroot <= tP+L*eP+K*eQ <= max(tP,tQ)+(K+L)*alpha.

## Fully ordered branch-aware original optimizer

At R let u be the immediate decision-P coin; at T let v be immediate decision-Q coin. Else follow a strict Bellman minimizer, notably B=(11,0,1) fixed Q-stop. The R/T cones are disjoint: T at depth7 has b=2, R at depth11 has b=0, so monotonicity excludes T preceding R, and depth excludes R preceding T.

Independent forward integer-weight literal-word DFS, with P weights (3,1,20)/24 and Q (1,1,10)/12, confirms first-hit inventories:

R: 55 literal words; P-mass 107421875/644972544; Q-mass 107421875/1451188224.
T: 70 literal words; P-mass 21875/2985984; Q-mass 21875/1119744.

For the full four-observer M=(eP,eQ,tP,tQ), complete disjoint cones yield an **exact affine** formula M(u,v)=M00+u*dR+v*dT, with

M00:
305381727585151333/876488338465357824;
3480191251019/10030613004288;
1344180058302820519/109561042308169728;
4354504136185/371504185344.

dR:
-5048828125/8916100448256;
2470703125/2507653251072;
-66923828125/371504185344;
-17939453125/208971104256.

dT:
1191246875/9393093476352;
-1878471875/20061226008576;
-377661353125/31701690482688;
-44855715625/1671768834048.

A separately implemented forward ordered-history integer DFS exactly matches backward Fraction four-observer values at all four deterministic corners, (u,v)=(0,0),(1,0),(0,1),(1,1), visiting 608476,607816,592726,592066 nodes respectively. The four-corner mixed interaction M11-M10-M01+M00 equals (0,0,0,0) as exact fractions.

Solving eP=eQ gives the exact feasible compensation

u(v) = 3833927448329263/4079680000000000 + (1449219877/10199200000)*v.

At v=0, this matches the prior Stage144 terminal R coin. Since u(1)=4413615399129263/4079680000000000>1, R reaches u=1 first at

vmax=245752551670737/579687950800000, with 0<vmax<1.

For every real 0<=v<=vmax, both coins lie in [0,1], and their common error rises exactly from alpha144 to alpha145, continuously and affinely; tP decreases with slope -(K+L). At v=0, tP-tQ=2427895767318664589/5290885334798696448>0; at v=vmax, tP-tQ=434302292346744026388749/945107382487128150638592>0, so tP=max(tP,tQ) for the whole segment. At both ends the exact dual equality tP+L*eP+K*eQ=Hroot holds, and by exact affinity it holds everywhere. This provides a primal optimum attaining the universal dual lower bound at every real alpha in the theorem.

## Right-end sharpness

The finite-horizon randomized policy polytope is compact. If alpha>alpha145 attained the same support, positivity of K,L and equality in the dual chain force eP=eQ=alpha and every action used at a positive-probability prefix to be a Bellman minimizer. The 1238 strictly positive gaps prohibit any non-minimizing action. Since all histories of a tied state have the same Q/P likelihood ratio and iid suffix, any history-specific randomization has the same four-observer effect as a single effective coin at that state. R/T first-hit cones are disjoint. Consequently eP=eQ forces u=u(v), while the feasibility u<=1 gives v<=vmax. The common error is thus <=alpha145, contradiction. Therefore the line is strictly below V14 for every alpha>alpha145.

## Verification scope, execution and next question

The locally executed author program \`EM_stage145_verify.py\` implements exact Fraction Bellman and four-observer recursion plus separately implemented literal integer-weight DFS, all four deterministic corner comparisons, tie/gap enumeration, exact endpoint equality and branch-first-hit inventories. Its output is \`PASS_STAGE145_ALL_EXACT_RATIONAL\`; the executed source/log/certificate are in the local evidence bundle. A portable runnable verifier is stored alongside this proof for replay, but saving code to GitHub is **not** a remote execution claim. No independent Driver mathematical review or native CLAIM/Result has been obtained; the active native Owner remains unverified.

A new separately executed exact dual-ray scan discovers Stage146 candidate K146=580442338958517/1418470016864, L146=52669253445512/132981564081, ties T=(7,1,2) Q/C and U=(8,6,2) P/C; the next **original primal interval** is unproven. See NEXT_TASK_PACKET_146.md.
