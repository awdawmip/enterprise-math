# Stage234–235: two exact, full-real supporting intervals in the N=14 ternary IID problem

2026-10-28 · PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED · Author identifier EM-R2-20261028-1311 is a local portable label, not a native Source-registered Researcher ID.

## Model, prior frontier, and result

A randomized policy observes the entire ordered ternary IID history, chooses a stopping time at most 14, and decides P or Q, where P=(3,1,20)/24 and Q=(2,2,20)/24. Let eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP=E_P(stopping time), tQ=E_Q(stopping time). Define V14(alpha)=inf_{eP,eQ<=alpha} max(tP,tQ). The quantification is over ALL ordered-history-dependent, privately randomized policies, and EVERY REAL error budget in each interval (including irrational budgets).

At the independently reused Stage233 author endpoint (not Driver-admitted),

\[
\alpha_{233}=\frac{1160041464109745}{3183518045011968},\qquad
V_{233}=\frac{3286774073290327}{397939755626496}.
\]

**Stage234 theorem.** For all real \(0\le\delta\le4665541022923375/3912750016452255744\),

\[
\boxed{V_{14}(\alpha_{233}+\delta)=V_{233}-\frac{493228}{3745}\delta}.
\]

Its exact right endpoint is

\[
\boxed{\alpha_{234}=\frac{2535185885996015}{6934653851959296}},\qquad
\boxed{V_{234}=\frac{7023447357787519}{866831731494912}}.
\]

**Stage235 theorem.** For all real \(0\le\delta\le30236820126025/33209821861254144\),

\[
\boxed{V_{14}(\alpha_{234}+\delta)=V_{234}-\frac{122232}{955}\delta}.
\]

Its exact right endpoint is

\[
\boxed{\alpha_{235}=\frac{237666670990705}{648489579282432}},\qquad
\boxed{V_{235}=\frac{647346693246113}{81061197410304}}.
\]

The slopes increase strictly: \(-15634/115<-493228/3745<-122232/955\). The two new intervals have positive width and exact endpoint continuity.

## Proof kernel: universal dual inequality

For the count state \(s=(n,a,b)\), every individual surviving ordered prefix ending at \(s\) has Q/P likelihood ratio \(r(s)=2^{a+b}/3^a\). For positive non-symmetric penalties \(\lambda_P,\lambda_Q\), define the exact finite Bellman recursion:

\[
B(s)=\min\{\lambda_Q r(s)\quad(P\text{ decision}),\
\lambda_P\quad(Q\text{ decision}),\
1+\sum_{j=0}^2 P_j B(s+j)\quad(\text{continue if }n<14)\}.
\]

At the terminal time only decisions exist. Backwards conditioning on any full ordered-history policy gives

\[
t_P+\lambda_P e_P+\lambda_Q e_Q\ge H:=B(0,0,0).
\]

Therefore \(V_{14}(\alpha)\ge H-(\lambda_P+\lambda_Q)\alpha\) for all feasible policies. The proof does not first assume Markov policies are universal.

For every prefix ending at the same count state, the Q/P likelihood ratio is the same, even after multiplying by hypothesis-independent private action kernels. Thus the P-conditional and Q-conditional action probabilities at that state agree; using them as a count-state Markov kernel preserves all P/Q state-action occupancy measures by forward induction on this finite DAG. Consequently eP,eQ,tP,tQ are preserved. This is a four-observable-specific reduction, NOT a lossless quotient of arbitrary histories, physical paths or X6/Cell information.

Bellman tightness with strictly positive P branch masses implies that any minimizing policy must choose minimizing actions at its reached states. The finite count-state occupancy polytope is the convex hull of deterministic policies. When there are k binary Bellman ties and all other states have a unique minimum, the optimal face's observation vectors lie in the convex hull of the \(2^k\) deterministic tie-bit policy corners. Conversely a random seed at the root implements any such corner mixture. All these corners satisfy dual equality.

Intersecting the tie-bit mixing simplex with the hyperplane eP-eQ=0, every vertex is either a balanced deterministic corner or a convex mixture of two corners whose error-difference signs oppose. Exhaustive rational enumeration of those vertices supplies *both* the minimal and maximal balanced error for that fixed dual supporting face. In both stages every deterministic corner obeys tP>tQ, so every mixture does; \(max(tP,tQ)=tP\). Root mixtures between the smallest and largest balanced vertices attain any real common error in their closed interval. They saturate the universal dual inequality, proving both V formulas and the maximality of the RIGHT endpoint for its fixed dual supporting face. No statement about the true V to the right of the last endpoint follows.

## Stage234 exact support and primal construction

The *exact*, independently checked asymmetric support is
\(\lambda_P=243496/3745,\ \lambda_Q=35676/535,\ H=78610072990571/1397494259712\).
Exactly 680 Bellman states; the sole ties are (9,1,0) P/continue and (11,1,1) Q/continue. There are 1,238 strictly positive nonminimal action gaps, minimum 10/2247.

For the four bit policies 00,01,10,11, independent exact rational suffix DP and unmerged ordered integer-mass DFS return identical four-observable vectors. DFS visits: 3013,3337,3148,3553, total **13,051**. Mixed finite difference across the four corners is NONZERO:

\[
(-259765625/247669456896,\ 119140625/139314069504,\
115234375/10319560704,\ 162109375/11609505792).
\]

Hence using a fake independent-coin affine parametrization would be unsound. Exactly FOUR balanced edge vertices exist; their sorted errors are

\[
1160041464109745/3183518045011968,\quad
35600460459545/97537262911488,\quad
1120016491638205/3068374966566912,\quad
2535185885996015/6934653851959296.
\]

The minimum uses policies 01 and 11, weights \(14902785173/42846328125\) and \(27943542952/42846328125\); it reproduces the Stage233 endpoint exactly. The maximum uses 00 and 10, weights \(68002835971/93332109375\) and \(25329273404/93332109375\). At the two endpoints the strict tP-tQ margins are \(512965541498779/795879511252992\) and \(1084521510921313/1733663462989824\).

## Stage235 six-tie convex hull and primal construction

The next *exact* asymmetric support is
\(\lambda_P=60024/955,\ \lambda_Q=62208/955,\ H=34234473198397/623648139264\).

Exactly SIX binary Bellman ties occur: (9,1,0) P/C; (10,1,0) P/C; (10,1,1) Q/C; (11,1,0) P/C; (12,1,0) P/C; (13,1,0) P/C. The other 1,234 action gaps are strictly positive, minimum \(25/6876\).

All **64 tie-bit corners** are exhaustively computed by exact rational suffix DP and an independent DFS of full ordered P/Q integer-mass branches. All four observation coordinates agree at each corner. DFS visits total **182,998**. Every corner satisfies exact dual equality and strict tP>tQ. No corner is already balanced.

Among the \(64\choose2\)=2016 unordered pairs, exactly **583** opposite-error-sign edges yield balanced vertices; these represent 529 distinct exact errors. Re-enumerating all 583 proves that the minimum common error equals alpha234 and the maximum equals alpha235. The minimum mixes 001000 and 101000 with weights \(68002835971/93332109375\) and \(25329273404/93332109375\), giving V234. The maximum mixes 000000 and 001000 with weights \(6332318351/8727890625\) and \(2395572274/8727890625\), giving V235. Endpoint tP-tQ margins are \(1084521510921313/1733663462989824\) and \(99253794949631/162122394820608\), both strictly positive.

The maximum common error on this entire six-tie dual face is alpha235, so the Stage235 interval is exact and maximal for that support. The dual lower bound and primal root mixtures establish the V theorem for the entire real interval.

## Executed reproducibility, source and limits

The Python file PORTABLE_REPRO_STAGE234_235.py on this same immutable PR branch is directly executable with Python 3 and standard-library Fraction. It independently computes rational Bellman over 680 states per stage, suffix DP and unmerged ordered P/Q integer-mass DFS for 4+64 deterministic policies, enumerates the balancing edges, asserts all exact dual contacts, strict tP>tQ, endpoint identities and segment continuity, and writes PORTABLE_EXACT_CERT_STAGE234_235.json. Its local actual run printed:

STAGE 234 PASS 13051 vertices 4 right_alpha 2535185885996015/6934653851959296
STAGE 235 PASS 182998 vertices 583 right_alpha 237666670990705/648489579282432
STAGE234_235_PORTABLE_EXACT_PASS 196049

Separate independent certificate-algebra scripts CHECK_STAGE234_CERT.py and CHECK_STAGE235_CERT.py were executed locally and returned PASS; the complete 18-member original sources, certificates, execution logs and SHA256 manifest are in the portable delivery archive supplied alongside this report. Discovery-only numerical LP did NOT enter the exact proof.

The BRC-compatible positive-branch-fidelity principle is preserved: independent P and Q integer path masses are carried along each *ordered* prefix; any count quotient is justified solely for the declared four observables. This is NOT an actual native heartbeat BRC numerical evaluation or a theorem about P000's six-dimensional native Cell dynamics. The X6 bridge requires a typed six-axis state embedding, three-dimensional slice semantics when relevant, explicit readout and proof of preserved joint branch relations and declared updates.

Global immutable read pin: awdawmip/chatgpt-global-knowledge main effc21073f497ef53baf39091b67918d75b9c072. Enterprise Math control pin: main 4a729c315568b0b61240013dccaf49adb84b2728. Prior Stage233 immutable proof: 359177370abebd9903d3022a1eb1b92f33385259 in Draft PR #1571. Native research authority FALSE; owner lookup CONTROL_QUOTA; no native CLAIM, formal Source Result, independent Driver review, or project admission. The above is exactly **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. Next bounded research unit: NEXT_TASK_PACKET_236.md.