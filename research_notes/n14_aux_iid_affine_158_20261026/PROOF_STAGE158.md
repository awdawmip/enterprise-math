# Stage158 — exact asymmetric Bellman interval in the external N14 iid model

**Evidence:** author exact-rational, computation-assisted proof of a whole-real interval and strict right sharpness; independent Research Driver review, native CLAIM/Result, and P000/X6 transfer are **not** established.

## Frozen sources and inherited frontier

GLOBAL_KNOWLEDGE_V1 canonical `main@a110753fc8aef4d7c4206eebe63931b32c298bda`; Enterprise Math input `main@90e8a926574233d61d7e0be2db8ee1358a235b82`. Read both global rule entries, EM project and task bootstraps, P000 startup and full foundation (matching original Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`), ACTIVE worldview, math/code research rules, and `docs/PORTABLE_RESEARCH_PROTOCOL.md`. Reconciled the concurrently published Stage157 author proof `63d33c52d365259eecd062770e7674d2dfb4de4d`, whose endpoint matches the independently reproduced value below; do not repeat it as a new Stage157 result.

Model: full **ordered-history** behavioral policies stopping by observation 14, with ternary iid
[
P=(1/8,1/24,5/6),qquad Q=(1/12,1/12,5/6).
]
Let (e_P=P(mathrm{decide} Q)), (e_Q=Q(mathrm{decide} P)), (t_P=E_P	au), (t_Q=E_Q	au), and (V_{14}(alpha)=inf_{pi:e_P,e_Qlealpha}max(t_P,t_Q)).

Stage157 inherited author endpoint:
[
alpha_{157}=rac{763084945158127578305}{2192919042319171190784},qquad
V_{157}=rac{3298586218925748578843}{274114880289896398848}.
]

## New theorem: all real points, not merely corners

For **every real** (0ledeltaleDelta_{158}),
[
oxed{V_{14}(alpha_{157}+delta)=V_{157}
-rac{53344114423224}{86511167249}delta},
qquad
oxed{Delta_{158}=rac{54069479530625}{1427681668176543744}}.
]
The exact right endpoint is
[
oxed{alpha_{158}=rac{763167995878686618305}{2192919042319171190784}},qquad
oxed{V_{158}=rac{3292184925194961698843}{274114880289896398848}}.
]
The same supporting line is **strictly below the optimum** for all (alpha>alpha_{158}).

### 1. Global dual support and 680-state exact census

For (s=(n,a,b)), (R(s)=Q(s)/P(s)=2^{a+b}/3^a).
At
[
K=rac{26880449139504}{86511167249},qquad
L=rac{26463665283720}{86511167249},
]
the finite Bellman recursion is
[
H(s)=min{K R(s) [mathrm{decide} P],L [mathrm{decide} Q],1+	extstylesum_{i=1}^{3}P_iH(s+e_i) [mathrm{continue}]},
]
omitting continuation at (n=14). Exact `Fraction` evaluation of all **680** count states yields exactly two ties:
[
H=(6,1,2): Q/C,qquad J=(10,2,0): P/C.
]
There are **1238 strictly positive** nonminimal action gaps; smallest
(874625881143787/32290120153354752), and zero negative gaps. The root is
[
H(0)=rac{67118306721229522289887399231}{296195426721776135565213696}.
]

For any **arbitrary ordered-history randomized strategy**, induction along each history using the same likelihood ratio gives the uniform bound
[
oxed{H(0)le t_P+K e_Q+L e_P
le max(t_P,t_Q)+(K+L)alpha.}
]
The asymmetric ordering (K e_Q+L e_P) is essential: the cost (KR) corresponds to P-decision (Q-side error).

The dual candidate comes from retaining J's P/continue tie and selecting T=(14,0,0) strictly Q after Stage157 terminal P coin saturates at zero. Along
[
(K,L)=(3342600/10529,3342600/10529)+t(-1,-25280/14751),
]
the first strictly positive gap closure is
(t_*=6147978656669784/910876079964721), which produces the stated K,L and new tie H. A separate exact Bellman evaluation at the endpoint confirms the census above.

### 2. Ordered BRC-style first hits and exact four-observer law

Use labeled ordered positive-rational prefixes, retain distinct P/Q masses and path multiplicity, and only then take the iid observer-specific quotient. Under strict Bellman actions except at the two ties, literal unmerged ordered-path DFS finds:

| First-hit state | Ordered histories | P mass | Q mass |
|---|---:|---|---|
| H=(6,1,2) | 40 | 625/124416 | 625/46656 |
| J=(10,2,0) | 45 | 1953125/11943936 | 1953125/26873856 |

H cannot lead to J since H already has 2 observations of symbol 2 while J requires 0; J occurs later than H. Thus their reached ordered path cones are disjoint. At any first-hit count state, iid suffix laws and the Q/P prefix ratio agree across all reached labeled prefixes; allowing history-specific coins changes none of the four observers beyond the corresponding effective two coins.

Let (h) be probability to immediately decide Q at H (otherwise continue), and (j) probability to immediately decide P at J (otherwise continue). For (M=(e_P,e_Q,t_P,t_Q)), every observer is exactly affine:
[
M(h,j)=M_{00}+h,d_H+j,d_J,
]
where
```
M00 = (1220395842171464035/3505953353861431296,
       223259694920365/641959232274432,
       5285134543382516317/438244169232678912,
       619867204468061/53496602689536)
dH = (26338176875/253613523861504,
      -754323125/10030613004288,
      -266343576875/31701690482688,
      -15586953125/835884417024)
dJ = (-3201171875/3962711310336,
      771484375/557256278016,
      -30224609375/165112971264,
      -4150390625/46438023168).
```
Two structurally distinct author algorithms agree **exactly** on all four deterministic corners: (i) `Fraction` conditional suffix recurrence on count states and (ii) literal unmerged ordered-prefix DFS with integer likelihood numerators (P=(3,1,20)/24; Q=(1,1,10)/12). Four respective DFS node counts: 465880, 448000, 464800, 446920. Their mixed four-vector (M_{11}-M_{10}-M_{01}+M_{00}) is **zero**.

### 3. Error equalization, time dominance, endpoint identities

Solving (e_P=e_Q) yields the exact affine compensation
[
oxed{j(h)=rac{660136987826389}{4611571200000000}
+rac{5885193739}{72055800000}h},quad 0le hle1.
]
Both coins remain legal, and J's P coin stays **strictly interior** even at (h=1). For (h=0), the four-observer vector equals Stage157's exact endpoint, including (V_{157}); for (h=1) it gives (alpha_{158},V_{158}). Common error grows strictly with h and covers the entire real interval.

At (h=0,1), (t_P-t_Q) is, respectively,
[
rac{251826953459549368715}{548229760579792797696}>0,qquad
rac{253249280016335608715}{548229760579792797696}>0.
]
Affineness gives (t_P>t_Q) throughout. Direct exact arithmetic gives
(t_P+K e_Q+L e_P=H(0)) at both endpoints, therefore for every real h. Combining with the universal dual lower bound proves the theorem and slope (K+L=53344114423224/86511167249).

### 4. Strict right sharpness

The finite ordered-history behavioral-policy cube is compact, all four observers continuous, so an optimizer exists. Equality to the same support beyond (alpha_{158}) would require both positive-penalty errors to equal (alpha), time maximizer (t_Pge t_Q), and Bellman-minimal actions at every positive-mass reached prefix. The strict gap census leaves only H and J. Because their cones are disjoint and first-hit prefixes have constant ratio and identical conditional suffix, every full-history equality policy has the same four observables as some ((h,j)in[0,1]^2) above. Equal errors force the given j(h). Its common error grows strictly with (h), and the greatest feasible (h=1) yields exactly (alpha_{158}). No equality case exists farther right. This proves strict support separation, **not** a theorem about P000-native dynamics.

## 3. Next new candidate (dual only): Stage159

Once H's Q coin saturates at h=1, retain J's tie along the same exact dual direction. The next first-gap ray closure is
[
t_{159}=rac{43776221891215860882}{12563497839079943249},qquad
oxed{K_{159}=rac{580027221414}{1887912013}},qquad
oxed{L_{159}=rac{566236422120}{1887912013}}.
]
New tie I=(9,5,4) Q/continue; J=(10,2,0) P/continue persists. Fresh 680-state exact Bellman scan: two ties, 1238 strictly positive gaps, smallest (20367756/1887912013), none negative. **This is a dual candidate only; no Stage159 primal interval has been proved.**

## Actual verification and limits

One real local run of portable exact-rational recurrence and ordered integer DFS verified Stage157 and Stage158 independently from the preceding author research outputs; separate author Stage158 exact checker and Stage159 scan were also run. Full expanded local programs, JSON certificates, logs and SHA manifest are in the accompanying local evidence archive. Portable `VERIFY_STAGE157_158.py` and `SCAN_STAGE159.py` give the essential remote reproducibility. GitHub-source publication is not remote execution; two author checks are not independent Driver review. These are results in an **external finite iid** auxiliary model only.

Authenticated GitHub actor was `awdawmip`. Native `em_control_tasks` returned `CONTROL_QUOTA`; native RESEARCHER `session_start` was refused with `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. Native active owner, formal session/CLAIM/Result and independent review remain unknown. This publication is an author research note, not a Source-native Result or permission escalation.