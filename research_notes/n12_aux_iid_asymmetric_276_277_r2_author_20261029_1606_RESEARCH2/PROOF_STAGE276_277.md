# Stages 276–277: two exact adjacent Bellman faces in the external N=12 ternary IID problem

2026-10-29 · author derivation, exact finite certificate · **PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. This is a finite, external sequential-decision theorem, **not** a result about native P000 X6/heartbeat dynamics. No native CLAIM, Source Result, independent review or Foundation promotion is asserted.

## Immutable input and authority

Canonical GLOBAL_KNOWLEDGE_V1 read: `awdawmip/chatgpt-global-knowledge main@6629bd6fe79d111d72f54b1b01ec1e031254bf64`; canonical Enterprise Math source read: `awdawmip/enterprise-math main@3168a61827f6ae43f20d501cadbb02fa2767fd97`. Current project `p000_reality_foundation.json`, ACTIVE protected worldview, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, joint-relation preservation, and `docs/PORTABLE_RESEARCH_PROTOCOL.md` were read as scope and observer constraints. Earlier Stage275 immutable author frontier: `61863c12dd7f3faada4963950c68f508c4211b3b`, in Draft PR #1571. Current native service status is version 0.6.11 with `research_authority_granted=false`, `CODE_REVIEW_REQUIRED` and 5/5 active-job quota; therefore this is *portable independent author work*, not a formally claimed source task. Local contributor identity means this actual execution, not a borrowed service session.

## 1. Mathematical problem and exact general lower bound

Alphabet `{0,1,2}`; source laws `P=(1/8,1/24,5/6)` and `Q=(1/12,1/12,5/6)`; independent outcomes conditional on the respective source, with at most `N=12` observations. All (possibly randomized) policies depending on the **entire ordered prefix** are permitted. They terminate declaring `P` or `Q`. Let `eP=P(declare Q)`, `eQ=Q(declare P)`, `tP=E_P(length)`, `tQ=E_Q(length)`, and `V12(a,b)=min max(tP,tQ)` over `eP<=a,eQ<=b` for real `a,b∈[0,1]`, setting `+∞` if infeasible.

For `s=(i,j,k)`, `|s|<=12`, let `p_s=(1/8)^i(1/24)^j(5/6)^k`, `q_s=(1/12)^(i+j)(5/6)^k`, and `B(s)` the minimum *unnormalized* Lagrangian suffix cost. For rational positive `λP,λQ` and time weights `(0,1)`, the Bellman recursion is

```
D_P(s)=λQ q_s
D_Q(s)=λP p_s
D_C(s)=q_s + Σ_z B(s+e_z)     (|s|<12 only)
B(s)=min available D(s).
```

Backward induction is valid **for each individual ordered word**, because all words with the same count triple have the same two source prefix masses and the same remaining IID suffix laws. It therefore yields the true optimum among all history-sensitive policies; it does **not** assert every strategy can be made count-only without loss of its four observers. For any cap-feasible policy and `H=B(0,0,0)`,

`max(tP,tQ) >= tQ >= H−λP eP−λQ eQ >= H−λP a−λQ b`.

The exact reproducibility program independently checks all 455 count triples, all 1,274 legal action costs, exactly two two-way ties, and 817 strictly positive off-optimal action gaps. Four extreme equality policies are evaluated both by a separate count-observer recursion and by an **unmerged ordered-word DFS** retaining both rational source masses and every path identity; each P and Q total termination mass is exactly 1.

## 2. Stage276: global optimum, stronger than previous upper bound

The Stage275 handoff's target is

```
a276 = 1162027955941/15850845241344
b276 = 868777330255/1114512556032
Stage275 feasible upper = 541791009235/92876046336.
```

An exact supporting Bellman dual is

```
λP = 2145488384/11690591
λQ = 1072744192/11690591
H  = 16434433593089254321/180962645235204096.
```

The **only ties** are `T=(0,0,5)` with actions `(P,C)` and `S=(0,1,11)` with actions `(P,Q)`. Note `S` is terminal (length 12), unlike the later `S5` of Stage277. Other actions have strictly positive gaps, minimum `539830163/833875869243820474368`.

Let `U=(T:P,S:P)`, `V=(T:C,S:P)`, `W=(T:C,S:Q)`, `X=(T:P,S:Q)`, using the unique Bellman action elsewhere. Their four complete observers `(eP,eQ,tP,tQ)` are:

```
U=(2910964806547/71328803586048, 29518152215/34828517376,
   13885256030731/2972033482752, 64511064545/11609505792)
V=(1054312075099/23776267862016, 77488067365/92876046336,
   5113190174827/990677827584, 47372383655/7739670528)
W=(206034675011/2641807540224, 23746022455/30958682112,
   5113190174827/990677827584, 47372383655/7739670528)
X=(545662756283/7925422620672, 9188342405/11609505792,
   13885256030731/2972033482752, 64511064545/11609505792)
```

The ordered DFS reaches `S` on exactly five words if `T` stops and six words if it continues; precisely one of those six descends from the word `22222` at `T`. All reached words at `S` have **identical two positive source masses**, `p_S,q_S`. For an arbitrary zero-Bellman-gap history-randomized strategy let `r∈[0,1]` be the chance of continuing at `T`, and `k` the total conditional weight of choosing `Q` at `S`, in units of one reached word. Then the *necessary and sufficient* domain and complete four-observer family are

```
0<=r<=1, 0<=k<=5+r,
Obs(r,k)=U+r(V−U)+(k/5)(X−U),
5(W−V)=6(X−U) in all four coordinates.
```

Sufficiency is constructive: continue at `T` with probability `r`, and choose `Q` at every reached `S` word with conditional probability `k/(5+r)`; this parameter lies in `[0,1]`. Necessity follows from ordered-prefix conditional probabilities; there is no independent rectangle of two coins because of nested reachability.

Let `R276` be `conv(U,V,W,X)` in the first two error coordinates, in that cyclic order. Its four exact signed turns are positive, two equal to `1783842620849609375/8625959983006819024896`, two to `8919213104248046875/51755759898040914149376`. Thus it is a strictly convex **non-parallelogram** quadrilateral with exact area

`19622268829345703125/103511519796081828298752`.

Stage275's `Jplus` and `M2` are exactly `W` and `X` here: the program independently reconstructs Stage275 Bellman actions and checks the common edge `W−X`. Exact orientations place Stage275 and Stage276 on opposite sides of that edge, so interiors are disjoint.

For the target caps, a *strictly positive* deterministic-policy mixture

```
weight(V) = 169151113/233811820000
weight(W) = 343659922061/701435460000
weight(X) = 1786340423/3507177300
```

sums to one and has exact observers

```
(eP,eQ,tP,tQ)=(1162027955941/15850845241344,
                868777330255/1114512556032,
                1024013855345369032501/208468967310955118592,
                19001515155589573655/3257327614233673728).
```

Here `tQ−tP=192083114612363681419/208468967310955118592>0`; the strict primal equality `tQ=H−λP*a276−λQ*b276` proves

**`V12(a276,b276)=19001515155589573655/3257327614233673728 ≈ 5.833467616999254`.**

This improves the Stage275 handoff's merely feasible upper bound by the **strictly positive exact** amount `3508358828125/203582975889604608 ≈ 0.0000172330658435185`.

For **every real** `(a,b)∈[0,1]^2`, not merely rational cap pairs,

`V12(a,b)=H−λP*a−λQ*b  iff  (a,b)∈R276`.

Sufficiency uses the explicitly complete `r,k` construction and the fact `tQ>tP` at all corners, hence throughout the convex region. For necessity, the finite ordered-history randomized strategy simplex is compact and the observers are continuous, so any feasible caps have an attained minimum. Equality in the displayed lower-bound chain and strict positive `λP,λQ` force both caps to bind and every reached action to be Bellman-minimizing; the exact `r,k` characterization forces the error pair into `R276`. Infeasible caps have value `+∞`, so cannot satisfy the finite affine equality.

## 3. Stage277: next adjacent exact face

The next dual is also an exact rational solution:

```
λP = 8245757952/44495173
λQ = 4104296772/44495173
H  = 7860156606936445891/86094494776590336.
```

The 455-state check yields precisely two ties: `T=(0,0,5)` with `(P,C)` and `S5=(1,2,8)` with `(Q,C)`; all other 817 action gaps are strictly positive. Define the four equality policies analogously:

`U=(T:P,S5:Q)`, `V=(T:C,S5:Q)`, `W=(T:C,S5:C)`, `X=(T:P,S5:C)`.

Their exact observer vectors are printed verbatim in the executed verification log. Full ordered DFS counts 145 reached `S5` words if `T` stops and 155 if it continues, with 10 descendants from the `T` prefix; `145(W−V)=155(X−U)` in all four coordinates. Consequently all zero-gap policies have the **exact** observer domain

`Obs(r,k)=U+r(V−U)+(k/145)(X−U),  0<=r<=1, 0<=k<=145+10r`.

The cyclic quadrilateral `R277=conv(U,V,W,X)` has strictly negative turns (all four checked rationally) and exact area `1357884918212890625/207023039592163656597504`. It shares the **whole U−V edge** with `R276` (the two observer vectors match in all four coordinates), with strictly opposite oriented interiors. Again all corner policies have `tQ>tP`, and the same compactness/Bellman argument yields for **all real** `(a,b)∈[0,1]^2`:

`V12(a,b)=H277−λP277*a−λQ277*b  iff  (a,b)∈R277`.

A strictly positive `(49/100)U+(49/100)V+(1/50)X` yields the exact new point

```
a277=674027955941/15850845241344
b277=937402330255/1114512556032
V12(a277,b277)=541791009235/92876046336.
```

It lies strictly outside `R276` across the common `U−V` edge; it is an exact global optimum at *its own caps*, not the Stage276 input caps.

## 4. Execution and scope

`REPRO_STAGE276.py` was actually executed using CPython with only Python standard-library `fractions.Fraction`, `collections.Counter`, exact integer comparisons and recursive complete ordered history traversal. The captured original stdout is `REPRO_STAGE276_277_EXECUTED_STDOUT.txt`. It prints both `STAGE276_EXACT_ALL_REAL_FACE_PASS` and `STAGE277_EXACT_ALL_REAL_FACE_PASS`. In Stage276, four DFS policies visit **42,616 nodes / 28,412 terminals**; in Stage277, **43,516 nodes / 29,012 terminals**. All eight checks independently give exact total P mass 1 and Q mass 1, and count recurrence equals full-word DFS. No floating point or extrapolation enters the published proof or verification.

**BRC scope:** the finite positive rational two-source masses and separately labeled ordered-path multiplicities are retained; state-count compression is justified only for the declared IID Bellman minimum and its fixed suffix observer. The P000 native X6 Cell source, future operation interface, signed/phase behavior, physical time and a native reconstruction bridge are *not* claimed or tested. Separate mathematical review and canonical source registration/admission remain open obligations, not inferred from remote Git storage.

**New frontier:** derive the next adjacent supporting dual past `R277`, and independently seek a native-X6 BRC source/observer bridge with a theorem stating precisely which future operations permit aggregation of ordered histories. Both may progress independently without changing P000 or expanding claim authority.
