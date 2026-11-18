# Stage208: exact all-real optimality interval (external N14 ternary IID)

Status: PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. Not a P000 native-X6 theorem, a physical-time result, a BRC-Shor arithmetic computation, a native Source Result, or an independent Driver admission.

## Theorem and scope

Let the ordered ternary sequence have IID laws P=(3,1,20)/24 and Q=(2,2,20)/24, with stopping at n<=14 and possibly arbitrary real randomized actions based on the complete ordered history. The terminal action declares P or Q. Put eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=inf{max(tP,tQ):eP,eQ<=alpha}.

The Stage207 author frontier is alpha207=1243470457111416115/3505953353861431296 and V207=2141397262877228573/219122084616339456.

For every **real** 0<=delta<=46416015625/855945643032576 (irrational delta included):

V14(alpha207+delta)=V207-(38448/175)*delta.

The new endpoint is alpha208=1243660577111416115/3505953353861431296 and V208=2138786643677228573/219122084616339456.

## Universal dual lower bound

At any ordered history h, let s=(n,a,b), where a counts symbol 0 and b counts symbol 1. Positivity and IID imply Q(h)/P(h)=rho(s)=2^(a+b)/3^a. For K=19224/175, define B(n,a,b)=min{K*rho(s), K, 1+sum_j P_j*B(child_j(s))}, omitting continuation at n=14. These costs are respectively for declare P, declare Q and continue, for tP+K*(eP+eQ). Although policies may distinguish full ordered histories, all conditional IID suffix laws depend only on s and all actions have those conditional Lagrangian costs. Finite backward induction plus linearity under real randomization prove for every allowed history policy:
tP+K*(eP+eQ)>=B(0,0,0)=H208=168140201472112396231/1917318240392970240.
Therefore V14(alpha)>=H208-2*K*alpha for every real alpha.

Exact Fraction enumeration covers C(17,3)=680 states, finds 1238 strictly positive unused action gaps with minimum 3757/340200 and no negative gaps. The only ties are T=(11,3,1), declare P / continue, and Z=(14,0,0), declare P / declare Q.

## Constructed optimal policy, valid on entire real interval

At T declare P with probability u, otherwise continue. At Z declare P with probability z, otherwise declare Q. Everywhere else use the unique Bellman minimizer. Set O(u,z)=(eP,eQ,tP,tQ).

There can be no ordered trajectory visiting both T and Z: T has 3 symbol-0 and 1 symbol-1 counts while Z has neither, and counts never decrease on extension; Z is terminal. Thus O(u,z) is affine without any u*z mixed term:
O(u,z)=O0+u*DT+z*DZ,
O0=(658405278767598899/1752976676930715648, 35709544576649/106993205379072, 2141397262877228573/219122084616339456, 26980287498415/2972033482752);
DT=(-5645703125/15850845241344, 1553515625/3343537668096, -23605859375/1981355655168, -6327734375/835884417024);
DZ=(-6103515625/78364164096, 6103515625/78364164096, 0, 0).

These four corner coefficients agree **exactly** between conditional Fraction suffix dynamic programming and independent integer-mass DFS on unmerged ordered histories. Individual corner visits were 72214, 72214, 66394, 66394 nodes (total 277216), and every path retained its ordered branch identity, multiplicity, and separate positive P/Q rational masses (integer products divided by 24^14). Count-state compression is certified for this finite IID model and these readouts only; no native X6 state/readout/future-operation bridge is asserted.

Solving eP=eQ gives:
z(u)=220020301271345049/819200000000000000 -(2697861/512000000)*u.
The endpoint rational inequalities are 0<z(1)=215703723671345049/819200000000000000<z(0)=220020301271345049/819200000000000000<1. Hence all real u in [0,1] give valid real coins. The common error alpha(u)=alpha207+(46416015625/855945643032576)*u is strictly increasing. Exact time gaps at u=0 and u=1 are 152194626194087453/219122084616339456 and 151242784594087453/219122084616339456, both >0. By affine dependence tP>tQ throughout, so max(tP,tQ)=tP. Every witness action is Bellman-optimal; tP(u)+K*(eP(u)+eQ(u))=H208. The witness exactly attains the universal dual lower bound. Since alpha(u) maps the full real [0,1] bijectively to [alpha207,alpha208], the claimed optimum holds for **all real alpha in that interval**, not a finite grid.

## Fixed-support strictness and next dual-only candidate

The next exact first-switch scan from Stage208's high-alpha endpoint gives K209=134136/1231, H209=366957863356152849587/4214676346292404224. Its new tie is (10,4,3) between Q/continue; terminal Z remains P/Q. At K209, 680 Bellman states have 1238 positive gaps, smallest 1547/177264, and exact contact H209=H208+2*alpha208*(K209-K208). Since K209<K208, for alpha>alpha208:
V14(alpha)>=H209-2*K209*alpha
=H208-2*K208*alpha+(381888/215425)*(alpha-alpha208)
>H208-2*K208*alpha.
This is strict separation from the **fixed Stage208 support**; Stage209 primal optimality is not yet proved.

## Verification, provenance and next question

Executed locally with exact arbitrary-precision Fraction and integer arithmetic: main checker STAGE208_AUTHOR_EXACT_FULL_REAL_PASS 277216; independent arithmetic-only certificate audit STAGE208_CERTIFICATE_ALGEBRA_CROSSCHECK_PASS; Stage209 exact dual scan STAGE209_DUAL_SCAN_PASS. Original executed scripts, complete corner/dual certificates, logs, SHA256 manifest and this extended proof are in the conversation's Stage208 portable archive (SHA256 264e6650a9298a65a77f69f1935a28b9b2e5bab690795e9d221392005abf364b). Published GitHub source is reproduction material, not evidence of remote execution.

Fixed verified source read: GLOBAL_KNOWLEDGE_V1 main@75eb1260e8d5d61a1f075ab675984d3f94d4ea55 and Enterprise Math main@55abd52563ee8b722ecbdd770547eda9fe64d678; global canonical P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched startup projection; Enterprise original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Scientific parent Stage207 immutable commit 7a2f5547eadca8050e24617fdcee16b954136173. Native em_status v0.6.11 reports research_authority_granted=false, and current owner query returned CONTROL_QUOTA. No native CLAIM, Source Result, independent Driver acceptance, Lean proof or P000 transfer is asserted.

Next unit: Stage209 ties (10,4,3) Q/C and (14,0,0) P/Q — four corner observations, mixed term, exact real balanced coin interval, time dominance and the next primal segment or rational obstruction.