# Stage258 — complete adjacent five-vertex all-real Bellman face (author exact)

2026-10-29. **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. This is an *external* ternary IID sequential testing model, not P000-native X6 / Heartbeat dynamics. Parent Stage257 immutable author research commit `97516f343bdc3fe6579fd64eda9044093e1b6385` in Draft PR #1571.

## Exact theorem

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon N=12. Allow all randomized stop/decision policies based on *complete ordered histories*, including irrational randomization. Write eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP=E_P[depth], tQ=E_Q[depth], and V12(a,b)=min max(tP,tQ) subject to eP<=a,eQ<=b, with +infinity if infeasible. Caps (a,b) are **all real** pairs in [0,1]^2.

The new exact one-sided Bellman support is
```
lambdaP=644972544/8007455
lambdaQ=418575732/8007455
thetaP=0; thetaQ=1; H=30134718329/576536760.
```
Define five four-observer vectors (eP,eQ,tP,tQ) in cyclic order:
```
C2  = (2762849059/46438023168, 15047799005/17414258688,
       4070710051/1934917632, 3347355427/1451188224)
C3  = (661800839/7739670528, 2348630905/2902376448,
       917102471/322486272, 745221767/241864704)
C12 = (14080778551/69657034752, 5014749965/8707129344,
       16378493239/2902376448, 4266808051/725594112)
Q12 = (29383188527/139314069504, 9874231855/17414258688,
       31963078703/5804752896, 8184999377/1451188224)
Q2  = (1011440903/15479341056, 4981428985/5804752896,
       1298095367/644972544, 1038314759/483729408)
```
Let R258=conv{error(C2),error(C3),error(C12),error(Q12),error(Q2)}. The five consecutive exact cross products are strictly positive, hence R258 is a genuine strictly convex pentagon, with exact area `245333081919015625/202170937101722320896`.

**Theorem:** for every real (a,b)∈[0,1]^2,
```
V12(a,b)=H-lambdaP*a-lambdaQ*b   IF AND ONLY IF   (a,b)∈R258.
```
R258 and Stage257's pentagon share **the complete edge Q2--Q12**, where `2a+b=22960038649/23219011584`. R258 is on the <= side and Stage257 is on the >= side; their interiors are disjoint.

An explicit *strictly exterior to Stage257* feasible cap point is
```
a*=12018216825031/87071293440000
b*=7754698736957/10883911680000
old_support_line-(2a*+b*)=3/10000
V12(a*,b*)=28372647518343096989/7262702750131200000
tP=109497793172713451801/29050811000524800000 < tQ=V12.
```

## Exact universal dual

For every ordered history h with symbol-count state s=(i,j,k), `Q(h)/P(h)=(2/3)^i*2^j=:L(s)`. The P-normalized Bellman recursion for `tQ+lambdaP*eP+lambdaQ*eQ` is
```
H(s)=min{lambdaQ L(s) [decide P],
         lambdaP [decide Q],
         L(s)+sum_z P(z) H(s+e_z) [continue]}.
```
The continue action is omitted at depth 12. The executable exact Fraction certificate checks **455 states and 1,274 available action costs**, with precisely **808 strictly positive alternative gaps**. There are only **11 two-action tie states**: neutral `(0,0,k)` for `2<=k<=11` (P/continue), and `(0,1,2)` (Q/continue); the root and first neutral state uniquely continue. Its rational root value equals exactly H above. The induction covers every randomized full ordered-history policy and proves
```
max(tP,tQ) >= tQ >= H-lambdaP*eP-lambdaQ*eQ
                        >= H-lambdaP*a-lambdaQ*b.
```
Both error multipliers are strictly positive.

## Complete equality fiber, typed BRC source mass, and primal witness

An arbitrary full-history policy's P-weighted action mass can be grouped by count s. For all histories with those counts, the Q/P source-likelihood ratio is identically L(s). Thus grouped Q action mass is L(s) times grouped P action mass, and grouped continued P mass at successor s+e_z is P(z) times grouped P continuation mass at s. Dividing grouped action mass by grouped visiting mass constructs an admissible count-Markov randomized policy preserving exactly **(eP,eQ,tP,tQ)**. This is an observer-specific sufficient state reduction, with positive P/Q path provenance retained in its proof; it is *not* a general claim to preserve all historical observables. Independent pre-sampling of the count-state randomized action table expresses it as a finite convex mixture of deterministic count policies.

By the exact tie list, the complete deterministic Bellman-equality policy family (up to unreachable actions) is the **22 policies** D_(k,M), k=2,...,12, M∈{Q,C}: on a neutral-only prefix continue until k neutrals, then decide P; at (0,1,2) take decision M=Q or M=continue; at every other state use its unique minimizing action. Define `Q_k=obs(D_(k,Q))`, `C_k=obs(D_(k,C))`. Every Q_k lies on the entire **four-observer** segment Q2--Q12, every C_k for k>=3 lies on C3--C12, and C2 is the fifth exposed vertex. Their exact displacement is
```
C_k-Q_k=(-135736825/15479341056, +51756025/5804752896,
         +88211975/644972544, +116205575/483729408), k>=3,
C2-Q2=(2/3)*(C3-Q3).
```
The k=2 factor is a source-order fact: the tie state (0,1,2) at depth 3 has exactly three equiprobable (under each source separately) ordered paths (1,2,2), (2,1,2), (2,2,1). A k=2 neutral stop suppresses only the last, preserving two of three; for k>=3 all remain. This exact positive-branch-multiplicity calculation gives a concrete BRC provenance-preservation witness rather than cancellation by scalar signs.

Therefore the Bellman equality policies' error convex hull is precisely R258; the non-degenerate pentagon and area follow by exact cross products and shoelace arithmetic. **Every one** of these 22 policies has tQ>tP, and that remains strict in every convex mixture. Thus any real point in R258 is attained by a Bellman equality mixture saturating both caps and the global lower bound.

Conversely, finite-horizon randomized policy space is compact, so an optimum exists whenever caps are feasible. Equality with this affine lower bound (positive lambdaP/lambdaQ) forces the two error rates to saturate both caps and all positive-source reached actions to be Bellman minimizing. The four-observer count compression then forces the error pair into R258. This completes the all-real iff theorem, including boundaries and irrational parameters. The Stage257 common edge follows because Q2/Q12 are exactly its previous U2/U3 vertices and the polygons lie on opposite sides of the displayed line.

For the strict-exterior point, choose independent root coins:
```
u=3702061401486841727/7541641324012500000
v=120762919703/125116484375.
```
Use neutral cutoff 3 with probability u, otherwise 8; at (0,1,2) decide Q with probability v, otherwise continue. Equivalently mix `D_(3,Q),D_(3,C),D_(8,Q),D_(8,C)` with weights `uv,u(1-v),(1-u)v,(1-u)(1-v)`. They are all strictly positive and sum to one. The exact four-observer value is
```
(a*,b*,109497793172713451801/29050811000524800000,
     28372647518343096989/7262702750131200000).
```
Both errors saturate, tQ>tP, and tQ=H-lambdaP*a*-lambdaQ*b*, proving global optimality.

## Actually executed verification and next question

`STAGE258_EXACT_FACE.py` is standalone Python 3 stdlib `Fraction` code (numerical LP was discovery only). It independently computes all 22 policies via suffix dynamic recursion and **unmerged complete ordered-history DFS** with separate positive P/Q mass; both source terminal masses equal exactly one. It verifies four observers, equality support, 455 Bellman states, 808 strict gaps and 11 ties, provenance 2/3 factor, pentagon area, strict adjacency and positive mixed optimum. Across 22 policies, it visited **3,394 full ordered-history nodes** and **2,270 terminal branches**. Saved actual stdout prints `STAGE258_EXACT_ALL_REAL_FACE_PASS` and `STAGE258_PROOF_CERTIFICATE_PASS`.

Pinned science input: GLOBAL_KNOWLEDGE_V1 main@e1a6307dd59f5e1290a1fa151115a72dee4dc886; Enterprise Math main@12274cc63b1f127e5db9fadebc83f21c77224075; P000 original/blob startup match `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, ACTIVE worldview unchanged. Native owner check returned `CONTROL_QUOTA`, em_status `research_authority_granted=false`; no native CLAIM, Source Result, independent Driver admission or P000 transfer. This is **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**.

**Stage259**: Cross the opposite full edge C3--C12, `2a+b=11379926137/11609505792`. Exact candidate caps `a=6257204592203/43535646720000`, `b=942101660479/1360488960000` are below that line by 3/10000. Prove feasibility or exact rational obstruction, recover next matched primal/dual Bellman region, and test when dual time weight thetaP first becomes positive. See the companion Stage259 packet.
