# Stage185 — full-real affine optimum of the full-history N14 ternary IID stopping model

**Status: AUTHOR EXACT PROOF; two independently executed exact algorithms; no native CLAIM, Source Result, Driver review or theorem admission.**

## Inputs and theorem

Frozen GLOBAL_KNOWLEDGE_V1 main: 968db47fa025cb6727542a945fdd54890f95dd78. Frozen Enterprise Math main: 3100006d98e989d452c3eafb683a68456fb731a7. Predecessor Stage184 immutable author commit 61a8afb7baefad66addf70238af4cd33c981f5cc. The original Stage184 portable ZIP supplied the dual-only Stage185 candidate. All results are confined to the **external auxiliary model**, not P000 native X6 dynamics.

Fix N=14, independent ternary observations with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). A policy may depend on the complete ordered history, randomize stopping and its P/Q decision, and must stop by time 14. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau) and V14(alpha)=inf max(tP,tQ) subject to eP,eQ<=alpha.

Put alpha184=6302854731325816791787/17990936586642819907584,
V184=49268185437698746127021/4497734146660704976896,
D185=67855772623365068983/6908519649270842844512256,
M185=23401296/62533.

**Theorem (author-level).** For every real delta in [0,D185],

    V14(alpha184+delta)=V184-M185*delta.

The new exact endpoint is

    alpha185=3684877789469437643/10517860061584293888,
    V185=2399458174541646935/219122084616339456.

The same fixed Stage185 support H185-M185*alpha is strictly below V14(alpha) for alpha>alpha185; no global claim is made about the next optimal segment.

## Bellman lower bound for arbitrary ordered-history policies

For prefix counts x=(n,a,b) of the first two symbols, the Q/P likelihood ratio of **every individual compatible ordered prefix** is ell(x)=2^(a+b)/3^a. Set K185=L185=11700648/62533. With P-normalization, let

    B(x)=min { K185*ell(x) [choose P], L185 [choose Q],
               1+sum_i P_i B(x+e_i) [continue, n<14] }.

Backward induction on each ordered prefix, using the likelihood identity, proves the universal bound

    tP+K185*eQ+L185*eP >= B(0,0,0)
      = H185=60828835377977479173913/428198791166048600064.

Therefore V14(alpha)>=H185-(K185+L185)*alpha. The exact Fraction recursion covers all 680 count states. Only S=(9,0,1) has Q/continue equality and Z=(14,0,0) has P/Q equality; the other 1,238 action gaps are strictly positive, smallest 3713241817841/107552181583872. The count-state Bellman quotient is sufficient for this particular IID objective, not for arbitrary BRC/native future observers.

## Complete-history construction and saturation

Use every strict Bellman action, and at S choose Q with probability s (otherwise continue); at terminal Z choose P with probability z (otherwise Q). There is no ordered prefix that visits both tie states: S has one symbol-1 occurrence whereas Z has none, and Z is terminal. The observable tuple (eP,eQ,tP,tQ) thus has the exact **zero mixed term** form base+s*dS+z*dZ.

For four deterministic corners (s,z)=(0,0),(0,1),(1,0),(1,1), an exact rational suffix DP was independently cross-checked by unmerged ordered-history integer-weight DFS, using separate P=(3,1,20)/24 and Q=(1,1,10)/12 branch weights. The four DFS node counts were 207682,207682,207250,207250 (total **829864**). First hit of S: 9 ordered paths, P mass=390625/4478976 and Q mass=390625/2239488. First hit of Z: 1 path, P=Q=6103515625/78364164096. Thus both coin variables have genuine positive-mass effects.

The exact error-balance relation is

    s(z)=36748691781079349/37833811200000000
         +(128000000/5911533)*z.

The simultaneous legal-coin interval is precisely

    0<=z<=1085119418920651/819200000000000000 =: zmax.

At z=0, the S coin exactly matches Stage184's final S coin, and (eP,tP)=(alpha184,V184). At z=zmax, **s=1**, yielding (alpha185,V185). eP=eQ grows strictly, tP decreases strictly with z. Endpoint tP-tQ values are respectively
149857900062857106545/562216768332588122112 and
6557735912710495/24346898290704384, both strictly positive.
All chosen actions attain the Bellman infimum; tP+K185*eQ+L185*eP=H185. Therefore max(tP,tQ)=tP and the dual lower bound is attained on **every real** parameter in the complete interval (not just sampled rationals).

## Strict right-hand sharpness

The finite decision-tree policy space is compact and the infimum is attained. If for alpha>alpha185 some feasible policy attained the Stage185 affine lower bound, K185,L185>0 would force eP=eQ=alpha and tP>=tQ, and equality in the Bellman decision at each reached P-positive ordered prefix. All non-ties are strict, so only S,Z can randomize. The nine S prefixes share their likelihood and continuation law, hence their history-dependent coins aggregate to one effective s for all four observables; Z has only one ordered prefix. Their tie cones are disjoint, giving exactly base+s*dS+z*dZ. Balance forces the relation above, and legal coins force z<=zmax and alpha<=alpha185, contradiction. Hence the fixed support is strict to the right.

## Verification, provenance and scientific boundary

Complete executed source, exact certificate and raw logs: locally portable Stage185 archive (VERIFY_STAGE185.py, certificate185.json, verify185.log). The shorter REPRO_STAGE185.py in this Git tree **was also executed** in the same local finite arithmetic environment; it rechecks 680 states, 1,238 positive gaps, four suffix/DFS corners, 829864 nodes, both first-hit states, the affine relation, error equality, endpoint continuity, time dominance and dual equality. Stage186 is a **dual-only** successor (see NEXT_TASK_PACKET_186.md and dual186_summary.json); it is not yet primal proved. All arithmetic is exact rational, no floating-point calibration and no external physical inference. No Lean formalization or independent review was performed.

BRC scope: integer-labeled ordered paths, path multiplicities and independent positive rational P/Q masses are retained through the DFS. Count-state projection is justified only for the stated IID observer and finite horizon; it is not general provenance-lossless compression, signed-amplitude BRC, or native P000 X6 dynamics. Gateway returned em_control_tasks=CONTROL_QUOTA and em_session_start=STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Native current owner unverified; no formal CLAIM/Source Result or independent Driver acceptance.