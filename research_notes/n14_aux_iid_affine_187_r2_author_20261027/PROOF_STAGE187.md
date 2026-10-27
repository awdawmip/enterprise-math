# Stage187 — exact full-real N14 auxiliary-model optimum; interacting tie cones

2026-10-27, author-level proof and exact executable checks. This is an **external ternary IID stopping model**, not a native P000 X6 Cell dynamics theorem, formal proof, independent Driver review, or accepted project result. Source: immutable Stage186 authored proof at `enterprise-math@210e25cc4c80f3053bf00ae14e6d9dfbf6d40436:research_notes/n14_aux_iid_affine_186_r2_author_20261027/PROOF_STAGE186.md` (Git blob `6dd79b5cd668afa49d3f58843eee5939df1aed8b`). Frozen current global read: `chatgpt-global-knowledge/main@b93af5fa5d1f56cff9a63f730c86247619d79b86`; EM source main at initiation: `28ecdefbfebe8418383794ebe1635617fd1df069`. Connected GitHub login: `awdawmip`. Native control-task inventory returned `CONTROL_QUOTA`; native session start refused `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. Local RA is bookkeeping, not a CLAIM.

## Problem, exact theorem

Let the horizon be 14. At each observation the symbol is 0, 1 or 2, with independent probabilities
[
P=(1/8,1/24,5/6),qquad Q=(1/12,1/12,5/6).
]
Every ordered-history-dependent randomized rule stops by 14 and outputs P or Q. Write `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P[T]`, `tQ=E_Q[T]`, and
[
V_{14}(alpha)=min_{eP,eQlealpha}max(tP,tQ).
]
At the previously author-established Stage186 boundary
[
alpha_{186}=rac{880819177025099228444495}{2513951372772311530733568},quad
V_{186}=rac{15842003227930467204041319427}{1448035990716851441702535168},
]
the next exact weights and Bellman root are
[
K=rac{30912926277555}{175004717024},quad
L=rac{948381852216}{5468897407},quad
H=rac{20011003723884904564897099291}{149794525046841680093773824}.
]
**Author-level theorem.** For *every real*
[
0ledeltale
Delta=rac{5947690894506310000401604043}{7176849460674877056318920028290285568}
]
the exact value is
[
oxed{V_{14}(alpha_{186}+delta)=V_{186}-
rac{61261145548467}{175004717024}delta.}
]
The right endpoint is
[
oxed{alpha_{187}=rac{47564236941933996508186187}{135753377754634620902572032}},quad
oxed{V_{187}=rac{47526009692613945133124984819}{4344108088148307868882305024}}.
]
For all real `alpha>alpha187`, the same fixed Stage187 dual supporting line is strictly below `V14(alpha)`.

## Exact Bellman dual certificate

Represent counts by `s=(n,a,b)`: `n` samples, `a` zeros and `b` ones. Under the declared IID measures
[
ell(s)=Q(omega)/P(omega)=2^{a+b}/3^a.
]
For `n<14`,
[
h(s)=minleft{Kell(s), L, 1+sum_{i=0}^2P_i h(s+e_i)ight};
]
at `n=14` omit continue. Here `e_0=(1,1,0)`, `e_1=(1,0,1)`, `e_2=(1,0,0)`. Exactly 680 count states were visited. Ties are **only**
[
R=(5,2,0): P/C,qquad T=(13,6,4):Q/C.
]
There are 1,238 strictly positive alternative-action gaps and zero negative gaps, with minimum
[
rac{464592386670727}{29031182497677312}>0.
]
At the root `h(0,0,0)=H`. Backward induction on the full ordered history tree, using its exact probability weights, yields for every randomized rule
[
t_P+K e_Q+L e_Pge H,qquad V_{14}(alpha)ge H-(K+L)alpha.
]

## Nonzero R→T interaction: four exact corner observations

Let `r` be the probability of deciding P at R (otherwise continue) and `t` the probability of deciding Q at T (otherwise continue). All other states use their unique Bellman-minimizing action. For `O=(eP,eQ,tP,tQ)`, independent exact suffix-DP and unmerged integer-weight ordered-history DFS obtain:
[
O(r,t)=B+rD_R+tD_T+rtC
]
where the **exact rational vectors**, componentwise in the above order, are
[
egin{aligned}
B={}&(614327151481393049/1752976676930715648, 
112420430604569/320979616137216, 
2399458174541646935/219122084616339456, 
285698065347565/26748301344768),\
D_R={}&(-4034771294375/4565043429507072, 
5111681875/3343537668096, 
-22213166676875/190210142896128, 
-13144174375/208971104256),\
D_T={}&(17875/6262062317568, 
-17875/6687075336192, 
-17875/782757789696, 
-17875/557256278016),\
C={}&(-625/18786186952704, 
625/20061226008576, 
625/2348273369088, 
625/1671768834048).
end{aligned}
]
**The mixed coefficient is nonzero.** There are 40 realized T-first-arrival ordered histories descending from R under the continue/continue baseline, alongside 3,392 T histories not passing through R. The four deterministic corner DFS traversals visit respectively 207250, 196954, 196750 and 186574 distinct ordered-history nodes, 787528 in total; all four output vectors agree *exactly* with suffix DP. Dropping the ancestry/provenance term `rtC` would give a false theorem.

## Exact primal attainment for the entire real interval

Solving `eP=eQ` with the mixed term retained gives
[
oxed{r(t)=rac{29069040000t+1085119418920651}
{80000(4235t+158600461647)}},qquad 0le tle1.
]
In particular, `r(0)=1085119418920651/12688036931760000` reproduces the Stage186 endpoint and
[
r(1)=1085148487960651/12688037270560000,
]
so `0<r(0)<r(1)<1`. The common error is
[
oxed{alpha(t)=
rac{1382578638172183457t+47564235559355358336002730}
{855945643032576(4235t+158600461647)}}.
]
It increases *strictly* on the whole real interval, since
[
alpha'(t)=
rac{5947690894506310000401604043}
{285315214344192(4235t+158600461647)^2}>0.
]
Direct symbolic simplification also gives
[
t_P-t_Q=
rac{1150048844006343543963931657-464927064418088234390t}
{27390260577042432(4235t+158600461647)}>0
]
for every `0<=t<=1`. Every minimizing action at each count state attains Bellman equality, hence `tP+K eQ+L eP=H` for the full bilinear polynomial and every real pair `(r,t)`. Thus `max(tP,tQ)=tP=H-(K+L)alpha(t)`. Strict monotonicity of `alpha(t)` and its exact two endpoints cover every real alpha in the claimed interval.

**History-dependent tie policies.** The right-sharpness claim is not restricted to count-dependent coins. Under any Bellman-equality strategy, strict-gap states have forced actions. All reachable R histories have equal conditional future observation laws, equal individual P masses and constant Q/P likelihood ratio; aggregating their stop-P probabilities defines one `r in [0,1]`. T is downstream of R for some paths, so its total incoming P mass is a fixed baseline minus a fixed coefficient times this `r`. Its incoming Q/P ratio is constant at the common T state. Weighted averaging its stop-Q probabilities over all *actually reached* T histories defines `t in [0,1]`. Downstream non-tie actions are unique, giving precisely the displayed bilinear `O(r,t)` even when the original coins depend on full histories. This is a finite IID observer-sufficiency certificate, not a general BRC or native-X6 information-erasure license.

## Right-sharpness

The finite randomized history-tree policy space is compact; all observation probabilities are positive. If a rule at `alpha>alpha187` attained equality in
[
max(tP,tQ)ge tPge H-KeQ-LePge H-(K+L)alpha,
]
then, since K,L>0, it would have `eP=eQ=alpha` and attain every Bellman-minimizing action at all reached histories. The preceding history-sensitive reduction applies: its effective `(r,t)` is legal, must satisfy the exact balance equation, and hence `alpha=alpha(t)<=alpha(1)=alpha187`, a contradiction. Therefore the Stage187 fixed support line is strictly below the true optimum for all `alpha>alpha187`.

## Stage188 dual-only scan and next exact task

At the right endpoint `t=1` (the **Q coin at T** saturates; R remains interior). Follow the directional perturbation `dK=-29050354413/50249878528`, `dL=-1`, preserving the R P/C tie while making T's Q action strictly optimal. Inspect every previously strict Bellman action gap as an exact affine function of the perturbation. The first closure is at
[
arepsilon=rac{729553468601176190107808}{1240617250081039376022727},
quad X=(8,0,1):Q/C.
]
This gives the **Stage188 dual-only candidate**
[
K_{188}=rac{39993714743501421}{226849611128761},L_{188}=rac{39205434834768424}{226849611128761},H_{188}=rac{552023450050793309312530706424493}{4142313307078339047903008391168}.
]
Independent new-weight Bellman recomputation confirms exactly two ties R P/C and X Q/C, 1,238 strictly positive alternative gaps, minimum `1858369546682908/55124455504288923`, no negative gaps, and root H188. The Stage187 endpoint strategy achieves equality at these new dual weights. **Stage188 primal interval and right-sharpness remain open.** R's zero-symbol count 2 exceeds X's count 0, hence the R/X first-hit cones are disjoint; the next unit is to derive exact four corners, error-balancing coins and full-real primal interval using that explicitly proved nonancestor relation, while retaining P/Q positive masses and observer scope.

## Evidence, limitations, and interfaces

The local executed exact script (Python `fractions.Fraction`, `sympy` only for optional rational simplification) performed 680-state Bellman sweeps, four suffix-DP corners and a separate 787,528-node integer-weight DFS, symbolic monotonicity, exact Stage186 endpoint continuity and an independent Stage188 Bellman recomputation. Output sentinel: `STAGE187_AUTHOR_EXACT_FULL_REAL_PASS`. The complete executed script, raw stdout, certificate and SHA manifest are also in `EM_STAGE187_AUTHOR_EXACT_PORTABLE_20261027.zip`; GitHub copy/reference, when present, must be distinguished from the executable original by its actual content identity. No Lean checker or independent Research Driver result was obtained. This author result concerns only the explicitly declared external IID model.

BRC reuse: positive-rational branch masses, multiplicities, ordered-path provenance, and exact observer/future-operation sufficiency; `POSITIVE_MASS != SIGNED_AMPLITUDE`. The model's count-state Bellman representation has a task-scoped IID sufficiency argument; full ordered histories were retained in the independent check, and R→T mixing was not erased.
