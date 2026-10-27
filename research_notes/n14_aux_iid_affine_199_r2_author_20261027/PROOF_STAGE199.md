# Stage199 — full-real optimal segment in the external N14 ternary IID helper

Status: **PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM**.
Scientific parent: Stage198 in draft PR #1571, immutable commit `266b09a3738ed43c01ad997ce652078ff61e912a`.
Verified control/science reads on 2026-10-27: GLOBAL_KNOWLEDGE_V1 main `edbbe204c4417149655022554f50f0d0004eb179`, Enterprise Math main `26176ded01b1bb6227b66c6dae612081a1a114df`. Verified GLOBAL P000_STARTUP projection: canonical original Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. ACTIVE worldview and portable research protocol apply as scope constraints; this external model is **not** a native P000 X6 physics result.

## Problem, theorem, scope
Take N=14 IID observations on {0,1,2} with P=(3,1,20)/24 and Q=(2,2,20)/24. A behavioral stopping/decision policy may depend on *all ordered observations* and may randomize. Let eP=P(report Q), eQ=Q(report P), tP=E_P[T], tQ=E_Q[T], and
`V14(alpha)=min_(eP,eQ<=alpha) max(tP,tQ)` for 0<=alpha<=1.

Exact left contact (previously proved at Stage198):
`alpha198 = 1849166499307598953/5258930030792146944`;
`V198 = 1152738710673976045/109561042308169728`.

**Theorem (all real delta):** for every real
`0 <= delta <= 166582609375/285315214344192`,

`V14(alpha198+delta) = V198 - (426576848/1523041)*delta`.

New endpoint:
`alpha199 = 1852236949963598953/5258930030792146944`;
`V199 = 1134822483057976045/109561042308169728`.
For alpha199<alpha<=1, the **fixed Stage199** supporting line is strictly below V14(alpha); this does not identify the subsequent optimal segment.

## Universal lower bound
State s=(n,a,b) records elapsed time and counts of symbols 0 and 1. The Q/P prefix likelihood ratio is `ell(s)=2^(a+b)/3^a`. Put
`K=L=213288424/1523041`,
`H=13641932749948792109334011/125149469578557848027136`.
Define Bellman cost under P by h(s)=min{K*ell(s) [report P], L [report Q], 1+sum_i P_i*h(s+i) [continue]}, omitting continue at n=14. Exact rational backwards induction on all 680 count-states yields h(0,0,0)=H, exactly 1238 strictly positive action gaps (minimum 2057512212551/276277395483648), and only two ties:
B=(7,0,1), Q/continue; Z=(14,0,0), P/Q. Every other action is uniquely minimizing.

Under either hypothesis the conditional suffix is IID after each *full ordered prefix*; Bellman induction is therefore valid even for arbitrary history-dependent randomized actions. It gives
`tP+K*eQ+L*eP >= H`, hence
`V14(alpha) >= H-(K+L)*alpha`.

## Exact primal family and decisive ancestor obstruction
At B choose **Q with probability u**, otherwise continue. At Z choose P with probability z, otherwise Q. Follow the unique Bellman action elsewhere. Let O=(eP,eQ,tP,tQ). Exact rational suffix DP gives:

`O(u,z)=O00 + u*DB + z*DZ + u*z*C`, where
`O00=(309576127029214243/876488338465357824, 56179084364011/160489808068608, 1152738710673976045/109561042308169728, 137343347570071/13374150672384)`,
`DB=(256404203125/47552535724032, -4708046875/1114512556032, -2916052671875/17832200896512, -229709703125/835884417024)`,
`DZ=(-6103515625/78364164096, 6103515625/78364164096, 0, 0)`,
`C=(0,0,0,0)`.

The zero mixed term has a *structural proof*: at B there is one observed symbol-1 (`b=1`), whereas at Z there are zero (`b=0`). Prefix counts cannot decrease, so **B can never precede Z**. Since Z is terminal, Z cannot precede B either. This resolves the previously open Stage199 ancestor question without discarding ordered path provenance.

Solving eP=eQ gives
`z(u)=1658052573537301/81920000000000000 + (790181343/12800000000)*u`.
All real 0<=u<=1 have 0<z(u)<1; z(1)=6715213168737301/81920000000000000. The common error increases *affinely and strictly* from alpha198 to alpha199. Exact time dominance checks:
`tP-tQ|_{u=0}=27622007379954413/109561042308169728>0`,
`tP-tQ|_{u=1}=13271429990651471/36520347436056576>0`.
This difference stays positive throughout by affine interpolation. Every selected action attains its Bellman minimum; thus tP+K eQ+L eP=H. Choosing u=delta/(alpha199-alpha198) yields primal and dual equality for **each real delta** in the asserted interval.

## Fixed supporting line becomes strict to the right
Behavioral randomizations on the finite ordered tree form a compact finite product of probability simplexes. Risk and expectation observables are continuous, so constrained optima are attained. Equality with H-(K+L)alpha would require eP=eQ=alpha and Bellman equality everywhere on positive-mass prefixes (K,L>0). The only variable actions then occur at B and Z. Distinct ordered prefixes with the same count-state have identical P and Q masses and the same IID suffix law, so history-specific coins can be averaged into one effective u and z without changing the four observables. Their two cones are disjoint by the integer-count proof above. Balancing errors forces the displayed z(u) with u∈[0,1] and shared error <=alpha199. Thus for alpha>alpha199 fixed-line equality is impossible.

## Exact computational witness and BRC scope
Executed `verify_stage199.py` with Fraction suffix DP and a separate unmerged full ordered-history DFS. DFS carried independent positive integer P/Q masses, symbol weights P:(3,1,20), Q:(2,2,20), terminal denominator 24^14. All four deterministic corners matched **exactly** in all four observables. DFS nodes: u,z=00:104410, 01:104410, 10:103087, 11:103087, **414994 total**. First-arrival ordered paths: B=7, Z=1, B-then-Z=0. Local program returned `STAGE199_AUTHOR_EXACT_FULL_REAL_PASS`. A separately publishable reference checker is `REPRO_STAGE199.py`. Counting-state Bellman compression is justified only for this finite IID observer/horizon, and does not assert equivalence of native residual/X6 paths.

## Next frontier: Stage200 dual-only
Independent exact directional scan at the saturated Stage199 policy gives K200=L200=`1358449620408/10345594439`, H200=`1821575844832789801808808179/17710532969288194722889728`; first new closure at (7,5,2), continue/P, downward K-step `137621064921653408/15756764499968999`. The terminal Z=(14,0,0) stays P/Q tied; the 680-state candidate has 1238 strictly positive gaps, minimum `136269916/10345594439`. **Stage200 primal proof remains the next task.**

Native em_status 0.6.11 observed read-only Sites client `research_authority_granted=false`, `registered_session_count=0` and full-snapshot verification pending. No current Task owner, native CLAIM, Source Result, independent review or mathematical admission is asserted.
