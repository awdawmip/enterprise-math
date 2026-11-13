# Stages 221–222 — exact full-real minimax optimality, auxiliary IID N14

Classification: `PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED`. These are auxiliary finite IID claims; neither a native X6 theorem nor a Source Result, formal CLAIM, independent Driver admission or P000 update.

## Exact setting and theorems
Each letter 0,1,2 is IID under P=(3,1,20)/24 or Q=(2,2,20)/24. A possibly randomized, full ordered-history-dependent policy stops by N=14 and declares P or Q. Let eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau), V14(alpha)=inf max(tP,tQ) subject to eP,eQ<=alpha.

**Stage221.** With alpha220=234533154377083721/657366253849018368 and V220=127935693438908681/13695130288521216, for every real 0<=delta<=282306875/106993205379072:

`V14(alpha220+delta) = V220 - (417562128/2258455)*delta`.

New endpoint alpha221=234534888870523721/657366253849018368, V221=127929012444860681/13695130288521216. K221=208781064/2258455; H221=1164595201473697679395993/15464917737881091440640.

**Stage222.** For every real 0<=delta<=28086603125/2567836929097728:

`V14(alpha221+delta) = V221 - (1176072048/6419795)*delta`.

New endpoint alpha222=234542079040923721/657366253849018368, V222=127901570763740681/13695130288521216. K222=588036024/6419795; H222=410483428040280012261601/5494995559412316241920.

The intervals include irrational parameters, not only a finite rational grid.

## Global dual lower bound
At s=(n,a,b), a=#0, b=#1, the history-specific Q/P ratio is rho(s)=2^(a+b)/3^a. For K>0, set B_K(s)=min{K*rho(s) [declare P], K [declare Q], 1+sum_j P_j*B_K(next_j(s)) [continue, n<14]}. Backwards induction on *every ordered history* proves that H_K=B_K(0,0,0) is the minimum of tP+K(eP+eQ) over all adaptive randomized history-dependent policies. Thus any feasible policy obeys max(tP,tQ)>=tP>=H_K-2*K*alpha.

Exact Fraction enumeration of the full 680 count-state finite DAG gives the stated H values and exactly 1,238 strict positive action gaps per stage, with minimum gaps 22638313/6585654780 for Stage221 and 121200629/9360061110 for Stage222. The only optimal ties are T221=(6,2,2):Q/C and Z=(14,0,0):P/Q, or T222=(7,3,1):P/C and Z:P/Q. The state quotient is justified for this finite IID suffix functional, not for arbitrary future observers or native dynamics.

## Global primal equality on each real interval
Let u be the chance of the first tie action at T (Q at Stage221, P at Stage222), and z the chance of declaring P at Z. Choose unique Bellman minimizers otherwise. Track O=(eP,eQ,tP,tQ). Both T states have b>0 while Z has b=0; b cannot decrease and Z is terminal. Hence no path can contain both randomized states; the coefficient of u*z is identically zero. For every real u,z in [0,1], O(u,z)=O00+u*(O10-O00)+z*(O01-O00).

All four deterministic corner vectors were checked with exact Fraction suffix dynamic programming and a second unmerged, positive-integer P/Q ordered-history DFS, 46,186 visited nodes at Stage221 and 38,956 at Stage222. Each pair of calculated vectors agrees exactly; total 85,142 visited nodes. The source reproducer contains all four corner/endpoint checks, strict gap counts and minimum gaps.

The unique equal-error balancing coins are:

`z221(u) = 20613104997354313/51200000000000000 + (36649221/200000000000)*u`.

`z222(u) = 20622487197930313/51200000000000000 - (200284091/320000000000)*u`.

z(0),z(1) are strictly between zero and one at both stages, hence every real u in [0,1] is legal. Along each balanced arc the common error increases strictly from its inherited alpha left endpoint to its stated right endpoint. The exact positive endpoint differences (tP-tQ) are Stage221: 4187448225889027/4565043429507072, 4188530390369027/4565043429507072; Stage222: 4188530390369027/4565043429507072, 1395206178283009/1521681143169024. By affinity tP>tQ everywhere on both arcs.

Every chosen action attains the Bellman minimum, so tP+K(eP+eQ)=H, max(tP,tQ)=tP, and tP=H-2K*alpha, attaining the universal dual lower bound. The two stages share the exact alpha221/V221 contact, and Stage221 shares the exact alpha220/V220 contact with inherited Stage220. This completes both full-real primal global optimality proofs without assuming order-invariant policies.

## Strict-right boundary and next candidate
K221<K220 and H221=H220+2*alpha220*(K221-K220); K222<K221 and H222=H221+2*alpha221*(K222-K221). Therefore for alpha above either contact the newer dual lower bound strictly exceeds the older fixed support: 2*(K_old-K_new)*(alpha-alpha_contact)>0. This is a strict-right test of that support, not by itself a complete new primal construction.

Exact Stage223 **dual-only** first switch: K223=472392/5245, H223=165229233763072546009/2244717448852930560, Bellman ties T223=(12,6,4):Q/C and Z=(14,0,0):P/Q, 680 states, 1,238 positive gaps, minimum gap 3955909/293652864. Exact contact H223=H222+2*alpha222*(K223-K222). Stage223 primal interval remains UNPROVED.

## Method, scope, sources
Separate integer P/Q branch weights on every ordered path retain multiplicity and provenance before division by 24^14 (typed BRC positive-branch discipline). Count quotient is used only after a finite horizon, declared two-error/two-time observer and IID suffix factorization proof; no X6 path embedding, three-dimensional-slice third coordinate, native time/update law or joint-relation preservation bridge was established.

Source pins: GLOBAL_KNOWLEDGE_V1 main@20265f0e5e1d6561043fd2b1505e486e1be38425; Enterprise Math main@d2c0c9157cc89f1c08c9db7c321b4c4702278703; predecessor author proof commit 7281c83a9970b288bc19dba8d44db0918ba4bfe9; P000 canonical Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches startup projection. `em_control_tasks` returned `CONTROL_QUOTA`; current authoritative owner unknown. GitHub author-side storage is not native activity/CLAIM/Result admission.

Author execution: `REPRO_STAGE221.py` and `REPRO_STAGE222.py` (actual run logs/certificates in downloadable companion research package) passed full exact dual/primal checks and dual successor scans. The directly runnable `PORTABLE_REPRO_STAGE221_222.py` stored here is derived from predecessor source at immutable Git blob cf924b30c6b4f5692b44f080a38dc531de663c7b with frozen Stage221/222 parameters; it is an additional **reproduction artifact**, not falsely described as the byte-identical primary executed file.
