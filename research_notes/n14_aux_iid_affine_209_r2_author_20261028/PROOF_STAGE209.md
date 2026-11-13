# Stage209: exact full-real optimum interval for external ternary IID N14

**Classification:** PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. This is mathematics of an explicitly external finite IID sequential decision problem, not native P000/X6 Cell dynamics, physical calibration or a formally admitted Source Result.

## Precise theorem

P=(3,1,20)/24, Q=(2,2,20)/24 are IID laws on ordered ternary histories; policies may randomize using arbitrary real probabilities depending on all ordered history, stop by n=14, and declare P or Q. Let eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau) and V14(alpha)=inf_{eP,eQ<=alpha} max(tP,tQ).

Freeze Stage208 right endpoint alpha208=1243660577111416115/3505953353861431296 and V208=2138786643677228573/219122084616339456. Let K209=134136/1231, H209=366957863356152849587/4214676346292404224 and Delta209=154336625/5135673858195456.

**Theorem:** For every real 0<=delta<=Delta209, including irrational delta,
V14(alpha208+delta)=V208-(268272/1231)*delta.
The exact new endpoint is alpha209=3730982047415656345/10517860061584293888 and V209=2138785208600876573/219122084616339456.

## Bellman universal lower bound

For a complete ordered prefix h, with n length and counts a=#symbol0,b=#symbol1, all P/Q masses are positive and Q(h)/P(h)=rho(n,a,b)=2^(a+b)/3^a. Under K=K209, the conditional Lagrangian tP+K(eP+eQ) obeys B(s)=min{K*rho(s),K,1+sum_j P_j B(child_j(s))}, omitting continue at n=14; actions respectively declare P, declare Q and continue. IID makes conditional suffix laws identical at ordered words with the same count state. Backward induction and linearity under arbitrary real history randomization give **for every full ordered-history policy** tP+K(eP+eQ)>=B(0,0,0)=H209. Thus V14(alpha)>=H209-2*K209*alpha for all real alpha.

Exactly C(17,3)=680 count states, 1238 strictly positive action gaps (minimum 1547/177264), no negative gaps, and two ties occur at T=(10,4,3), Q/continue, and terminal Z=(14,0,0), P/Q.

## Complete real-optimal policy witness

At T declare Q with probability u in [0,1] and otherwise continue. At Z declare P with probability z in [0,1], otherwise Q; choose the unique Bellman minimizer elsewhere. Ordered words cannot visit both T and Z: T has 4 symbol-0 and 3 symbol-1 counts, which never decrease on extension, but Z has zero of each; Z is terminal. Therefore O(u,z)=(eP,eQ,tP,tQ) has **zero** u*z interaction for every real pair of coins:
O(u,z)=O0+u*DT+z*DZ,
O0=(657780909167598899/1752976676930715648,11919752358883/35664401793024,2138786643677228573/219122084616339456,242620099985735/26748301344768);
DT=(213875/1174136684544,-612125/5015306502144,-2883625/440301256704,-435125/46438023168);
DZ=(-6103515625/78364164096,6103515625/78364164096,0,0).

Every vector coefficient agrees exactly between conditional Fraction suffix DP and independently unmerged full-ordered integer-mass DFS of four deterministic corners (66394+66394+56482+56482=245752 nodes). All path identities/multiplicities and separate strictly positive P/Q integer-weight products are retained, normalizing terminal masses by 24^14. Count compression is justified for this finite IID model and its four readouts only, not for native X6 spatial states.

Solving eP=eQ yields z(u)=215703723671345049/819200000000000000+(6249221/3200000000000)*u, with 0<z(0)<z(1)=215705323471921049/819200000000000000<1. So all real u in [0,1] produce legal balanced errors. Their common error is the strictly increasing affine alpha(u)=alpha208+Delta209*u. Endpoint time gaps tP-tQ are 151242784594087453/219122084616339456 and 151243402695079453/219122084616339456, both positive. Since the gap is affine, max(tP,tQ)=tP throughout.

All witness actions are Bellman minimizers; tP(u)+K209*(eP(u)+eQ(u))=H209, so tP(u)=H209-2*K209*alpha(u). This exactly meets the universal lower bound. The affine bijection u->alpha(u) covers **all real** alpha in [alpha208,alpha209]. Exact endpoint checks produce V208 and V209. This proves the theorem over the full real interval, not a sampled grid.

## Strict-right separation of the fixed Stage209 support

The next exact first-switch scan gives **dual-only** K210=258616/2395, H210=6798931418530161042091/78719608898419949568; the new Q/continue tie is (8,2,2), terminal Z stays P/Q. Exactly 680 states with 1238 positive gaps (minimum 1540319/125708760) and the exact contact identity H210=H209+2*alpha209*(K210-K209). As K210<K209, for every alpha>alpha209:
V14(alpha)>=H210-2*K210*alpha=H209-2*K209*alpha+(5798848/2948245)*(alpha-alpha209)>H209-2*K209*alpha.
This proves strict-right separation of the **old fixed supporting line**, not Stage210 primal optimality.

## Executed checks, sources, authority and next unit

Locally executed verify_stage209.py -> STAGE209_AUTHOR_EXACT_FULL_REAL_PASS 245752; audit_stage209.py (arithmetic-only, no Bellman/DFS) -> STAGE209_CERTIFICATE_ALGEBRA_CROSSCHECK_PASS; scan_stage210.py -> STAGE210_DUAL_SCAN_PASS. Complete executed scripts, exact corner and dual certificates, logs and SHA256 manifest are stored in the attached Stage209 portable archive SHA256 93ff280e6bcbdfc9e58ec067b7ea94f5d00dbd48105548f013cf10914a07dae3; GitHub code publication does not evidence remote execution.

Frozen verified GLOBAL_KNOWLEDGE_V1 main@75eb1260e8d5d61a1f075ab675984d3f94d4ea55; Enterprise Math main@55abd52563ee8b722ecbdd770547eda9fe64d678; global P000 canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches startup projection; Enterprise P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Exact scientific Stage208 parent commit 1cc8bf4a44dbb14518ea5d659fe7ce22480088eb. em_status v0.6.11 research_authority_granted=false and owner-listing CONTROL_QUOTA; no native CLAIM, Source Result, independent Driver acceptance, Lean proof or P000-X6 transfer claimed.

**Next unresolved mathematical unit:** Stage210 ties (8,2,2) Q/C and (14,0,0) P/Q; calculate four exact ordered-history corners, mixed interaction, balanced real coin interval, time dominance, and next primal segment or a rational obstruction.