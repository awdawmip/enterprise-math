# Stage176 — exact full-real primal continuation (external N14 IID)

**Scientific status:** AUTHOR_EXACT / NOT_ADMITTED. Model: external ternary IID sequential minimax, not the P000/X6 native world. This note proves a full real interval; neither Source task CLAIM nor independent Driver admission exists.

## Source authority and exact problem

Frozen account `GLOBAL_KNOWLEDGE_V1 main@e3216935b09dc101e4df54f6fe52effbb110da69`; EM source `main@bcb3a31c94f4461a592fa50cb177f9d8717f11d6`; corrected Stage175 parent immutable `a89b84fb9e2275b4fec80c5cc6411d795afdf6cc`, files `NEXT_TASK_PACKET_176.md` and `dual176.json`. P000 projection matched original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`; ACTIVE worldview and `docs/PORTABLE_RESEARCH_PROTOCOL.md` were read. No native transfer.

For stopping/decision policies on all ordered histories of length at most 14 under P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6), define `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P(tau)`, `tQ=E_Q(tau)`. Let `V14(alpha)=min_{eP,eQ<=alpha} max(tP,tQ)`. The feasible policies are finite products of compact simplices, so the minimum is attained.

## Bellman dual certificate

For count state s=(n,a,b), where a is symbol-0 count and b symbol-1 count, Q/P likelihood ratio is `ell(s)=2^(a+b)/3^a`. Define `h(s)=min(K*ell(s),L,1+sum_i P_i h(s+i))` (continuation absent at n=14), with

`K176=1696807920718753587/7487608294325270`

`L176=168348947995801752/748760829432527`

`H176=1733492029996286794626721771839535/10254377114019668494551279992832`.

Exact rational backward recursion scans all 680 count states. Only ties: W=(4,1,2) chooses Q or C; T=(8,2,0) chooses P or C. All other 1,238 nonwinning gaps are strictly positive; minimum `152464420746873000396113/4292712684503529027010560`, no negatives; root Bellman value equals H176. The Bellman inequality applies separately at each ordered prefix, hence any history-dependent randomized policy obeys `tP+K*eQ+L*eP>=H`. Since K,L>0, `V14(alpha)>=H-(K+L)*alpha`.

## Construct the primal witness

Choose Q at W with probability w (else C), and P at T with probability t (else C). Elsewhere follow the unique Bellman winner. No history reaching W can extend to T: W already has two symbol-1s and T has none; T has greater depth. Their first-hit cones are disjoint. W first-hit: 8 ordered paths with P mass 5/3456 and Q mass 5/1296; T: 28 paths with P mass 109375/746496 and Q mass 109375/1679616.

Thus the observable vector M=(eP,eQ,tP,tQ) is exactly `M(w,t)=M00+w*dW+t*dT`, with zero mixed term, where

`M00=(153168173405691179/438244169232678912, 27937973841605/80244904034304, 633778557697110149/54780521154084864, 74740581988693/6687075336192)`

`dW=(166578227395/4057816381784064, -1153241975/40122452017152, -1377728139575/507227047723008, -6440281555/1114512556032)`

`dT=(-1210671875/1114512556032, 2319296875/1253826625536, -16248859375/92876046336, -9353640625/104485552128)`.

These values were independently obtained for all four deterministic corners by (1) exact Fraction suffix DP and (2) unmerged ordered-history integer-numerator DFS (each P path weight = integer/24^n; Q weight = integer/12^n). All 4x4 observables agree exactly and terminal masses under P and Q each sum to 1; ordered DFS nodes 282916+279052+267580+263716 = 1093264. No floating tolerance was used.

Solving `eP=eQ` gives exactly

`t(w)=1768756796217217/3860125696000000 + (4588038935639/193006284800000)*w`.

Both coins are legal for **every real w in [0,1]**. At w=0, t agrees with Stage175 and `alpha175=5147935054057228427975/14750257906470044565504`, `V175=338938781942537717887145/29500515812940089131008`. At w=1 the new endpoint is

`alpha176=5148159682306058186075/14750257906470044565504`

`V176=338735964098497111620725/29500515812940089131008`.

The common error increases strictly by `Delta_alpha=18719020735813175/1229188158872503713792>0`, while `tP` decreases. Exact endpoint P-time-minus-Q-time margins are `10425404935270598468897/29500515812940089131008` and `10455836014844563234957/29500515812940089131008`, both positive. Exact endpoint Bellman tightness `tP+K*eQ+L*eP=H` holds. All conditions persist over the entire real interval by affine interpolation.

### Theorem

For every real `0 <= delta <= 18719020735813175/1229188158872503713792`,

`V14(alpha175+delta) = V175 - (3380297400676771107/7487608294325270)*delta`.

Proof: the universal Bellman lower bound and the explicit equal-error, tP-dominant, Bellman-tight strategy coincide. No grid argument is used.

**Strict right support-line sharpness:** if equality with `H-(K+L)*alpha` occurred for alpha>alpha176, attainment and K,L>0 force `eP=eQ=alpha`, `max(tP,tQ)=tP`, and Bellman-optimal actions at every reached positive-mass history. All non-tied actions are forced. At a common count state, Q/P likelihood ratio is constant, so history-dependent tie decisions can be P-weighted averaged without changing either P- or Q-observables; disjoint W/T cones yield effective w,t in [0,1]. Error balance forces the displayed t(w), whose largest common error is alpha176, contradiction. This bounds **the support line**, not the whole value function's future.

## Verified evidence, scientific limit and next step

Actual executed local `VERIFY_STAGE176.py` returned `STAGE176_AUTHOR_EXACT_FULL_REAL_PASS`; 680 Bellman states/1238 strict gaps, 4 DP-vs-DFS corners, mixed zero, legal real coins, exact Stage175 boundary, both dual identities and P-time dominance checked. Actual `SCAN_STAGE177.py` returned `STAGE177_DUAL_SCAN_PASS`. Scripts, exact JSON certificates and stdout logs are preserved in the local author portable ZIP; GitHub reference source/readback is *storage* evidence, not remote execution.

Stage177 **dual-only**: `K177=1870855299/8461318`, `L177=911522328/4230659`, `H177=148336146012983121522325/905303534551638736896`; ties T=(8,2,0) P/C and U=(12,5,2) P/C. U may descend from T; the next proof must account for non-disjoint tie cones and possible bilinear coin observations. See `NEXT_TASK_PACKET_177.md`. BRC method applied to labeled positive-rational ordered paths and distinct P/Q masses; no native BRC-Shor or P000 theorem. Live native owner unknown (CONTROL_QUOTA), native session start STATIC_READONLY_SCOPE_DENIED; no formal CLAIM/Source Result/review.
