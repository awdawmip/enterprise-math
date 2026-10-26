# Stage158 — exact off-diagonal real optimality segment in an external N14 iid model

**Status:** AUTHOR_EXACT; exact finite proof with two structurally independent rational observer algorithms. No native CLAIM, Source Result freeze, independent Driver admission or P000-native inference.

## Frozen scientific sources and scope

GLOBAL_KNOWLEDGE_V1 canonical main `a511c0782dae1f31e85e1d1c545039355fd018fc`: both normative entry files; Enterprise Math project/TASK router; original locked P000 and matching startup projection (canonical P000 Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`); ACTIVE worldview; math/code/BRC policy. Enterprise Math scientific input main `4f1ceac47ab3b65fa69d0b4695b253bdda2f44e0`: `docs/PORTABLE_RESEARCH_PROTOCOL.md`, ordinary Chat control, `research_notes/n14_aux_iid_affine_157_20261026/{PROOF_STAGE157.md,certificate157.json,NEXT_TASK_PACKET_158.md}`.

External model, **not** P000 native Cell dynamics: 14 iid observations in {0,1,2}, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Full ordered-history randomized stopping/decision strategies; eP=P(decide Q), eQ=Q(decide P), tP=E_P[tau], tQ=E_Q[tau]. Define V14(alpha) as the minimum of max(tP,tQ) subject to eP,eQ <= alpha.

## Theorem

Let alpha157=763084945158127578305/2192919042319171190784 and V157=3298586218925748578843/274114880289896398848 (the author's Stage157 proven endpoint). Define

- K*=26880449139504/86511167249, L*=26463665283720/86511167249, both positive and L*<K*;
- Delta*=54069479530625/1427681668176543744;
- H*=67118306721229522289887399231/296195426721776135565213696.

For **every real** 0<=delta<=Delta*,

```
V14(alpha157+delta) = V157 - (53344114423224/86511167249)*delta.
alpha158 = 763167995878686618305/2192919042319171190784.
V158 = 3292184925194961698843/274114880289896398848.
```

For every alpha>alpha158, the **same** supporting line `H*-(K*+L*)*alpha` is strictly below V14(alpha). This statement of right sharpness does not deny another support line after this endpoint.

## Exact dual derivation and complete Bellman certificate

At count state s=(n,a,b), Q/P likelihood ratio lambda=2^(a+b)/3^a. For nonnegative K,L define H_{K,L}(s) as the min of `K*lambda` (decide P), `L` (decide Q), and `1+sum_i P_i H(s_child_i)` (continue, only if n<14). This count dynamic program is valid for **all full ordered-history policies**, since conditional likelihood ratio and future iid suffix depend only on counts; for every such policy,

```
H_{K,L}(root) <= tP+K*eQ+L*eP
              <= max(tP,tQ)+(K+L)*alpha.
```

Start from Stage157 diagonal k=3342600/10529. Its two ties were J=(10,2,0), decide-P/continue, and T=(14,0,0), decide-P/decide-Q. The exact J P-minus-continue affine gap under the other strict actions is

```
D_J(K,L) = -15475/13824 + (395/46656)*K - (1639/331776)*L.
```

The ray `K=k-epsilon, L=k-(25280/14751)*epsilon` keeps J tied. For positive epsilon it has L<K, so T strictly decides Q. A complete **exact rational affine** gap scan of all 680 count states along this ray has its first new closure at

```
epsilon* = 6147978656669784/910876079964721,
U=(6,1,2), decide-Q/continue.
```

At epsilon*, independent recomputation of all 680 Bellman states shows exactly J (P/C) and U (Q/C) tied; all **1,238** other nonminimal available gaps strictly positive (zero negative). The root is H* above. Thus only J and U may be randomized in an equality policy. This exhaustive finite Bellman fact is verified by the included standalone exact checker and certificate.

## Ordered-history first-hit identities and affine observers

At J, stop/decide P with probability j (otherwise continue). At U, stop/decide Q with probability u (otherwise continue). Strict optimal actions everywhere else. Direct ordered integer-weight DFS first-hit results:

- J: 45 ordered first-hit prefixes, P mass 1953125/11943936, Q mass 1953125/26873856;
- U: 40 ordered first-hit prefixes, P mass 625/124416, Q mass 625/46656.

Their cones are disjoint: U has two observation-1 labels (b=2); J has b=0, so neither can be on an ordered prefix of the other. Consequently M=(eP,eQ,tP,tQ) depends exactly affinely:

```
M(j,u)=M00 + j*dJ + u*dU.
dU=(
26338176875/253613523861504,
-754323125/10030613004288,
-266343576875/31701690482688,
-15586953125/835884417024
).
```

M00 and dJ exactly equal the frozen Stage157 certificate. Four deterministic corners are checked using two different arithmetic realizations: (a) memoized rational suffix dynamic programming, and (b) literal ordered integer-weight DFS without count-state collapse. All 16 observable values agree exactly, all four mixed interaction differences vanish, and the ordered DFS visits respectively 465880, 448000, 464800, 446920 prefix nodes at (j,u)=(0,0),(0,1),(1,0),(1,1), a total of **1,825,600**. The signed differences are in observer totals, not native BRC positive-weight cancellation.

## Full real primal construction

The exact error equality eP=eQ gives

```
j(u)=660136987826389/4611571200000000
    +(5885193739/72055800000)*u,
j(1)=1036789387122389/4611571200000000.
```

For all real u in [0,1], 0<j(0)<j(u)<j(1)<1, except endpoints with the expected weak inequalities; u itself is an admissible probability. Along this family common error is a strictly increasing affine function from alpha157 to alpha158. At the two endpoints tP-tQ respectively equals

```
251826953459549368715/548229760579792797696 > 0,
253249280016335608715/548229760579792797696 > 0.
```

Thus max time is tP throughout. Exact endpoint identities

```
H* = V157+(K*+L*)*alpha157
   = V158+(K*+L*)*alpha158
```

extend affinely to every real u in [0,1]; together with the universal Bellman lower bound they prove the exact value formula for **every real delta in the segment**.

## Strict right-sharpness

There are finitely many ordered histories through depth 14; their behavioral policy probability cube is compact, with continuous observables. If equality with the same supporting line held at any alpha>alpha158, K*,L*>0 would force both errors equal alpha, tP=max time, and every reached action minimizing the Bellman recursion. Strict gaps rule out any deviations beyond J and U. All finite ordered histories have strictly positive P/Q mass. Every prefix arriving at the same tie count state has the same likelihood ratio and iid suffix distribution; averaging arbitrary history-specific choices at each tie therefore preserves the four observer totals. Since J/U first-hit cones are disjoint, each such policy has some effective j,u in [0,1] and the exact affine M(j,u). Error equality forces j=j(0)+beta*u, and common error <=alpha158. Contradiction. Hence no equality with this support beyond alpha158.

## Reproducibility and exact boundaries

All fractions have integer numerator/denominator, no tolerance comparisons. Verified finite facts: 680 Bellman states, first off-diagonal closure, 1,238 strict gaps, 45+40 labeled first hits, four corners by independent integer-DFS/rational-suffix algorithms, zero mixed terms, both error-time endpoint equalities, right sharpness from proven compactness/strict supports. Local full checker: `VERIFY_STAGE158.py`; complete rational evidence `certificate158.json`, distributed in the accompanying portable scientific package, and may also be stored here. Source math remains author-verified, not native Source-admitted. Native `em_control_tasks` and `em_control_dispatch` returned `CONTROL_QUOTA`; live active Owner and CLAIM were not determined. The scope is the **external finite ternary iid model**; retaining native P000 six-space, slice, BRC typed branch provenance, sign/phase and future-observer residuals requires separate transfer proof.

**Stage159 next unit:** At Stage158 endpoint u=1, keep J P/C tied and make U strictly Q with a fresh admissible off-diagonal ray; scan all gaps for the next exact first closure and determine whether another full real primal segment can be proved (or give exact obstruction). No duplicate Stage157/158 proof effort.
