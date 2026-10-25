# Stage98: exact affine minimax interval in the auxiliary N=14 iid sequential test

**Status:** author exact-rational computation-assisted finite-model proof, pending independent Research Driver review and native Result admission. This is an **external positive-weight iid auxiliary model**, not a P000/X6/Heartbeat-native theorem or a BRC-native arithmetic run. No native owner or CLAIM is asserted.

**Frozen read sources:** GLOBAL_KNOWLEDGE_V1 `dca4319404d29afc12774cd488926733e49782c4`; Enterprise Math `74e2c8f184d60242747a4756a84703e2ceeb967f`; Stage97 precursor `research_notes/n14_aux_iid_affine_97_20261025/PROOF.en.md`, Git blob `cb36d5fac02fcd326838633627dfdcc1679a4d5f`. P000 source blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matches its startup projection; ACTIVE worldview and current portable protocol were read. Native tasks returned `CONTROL_QUOTA`; native session creation returned `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`.

## Exact theorem

For iid `P=(1/8,1/24,5/6)` and `Q=(1/12,1/12,5/6)` on alphabet `{0,1,2}`, consider all randomized tests using **full ordered histories** and stopping time `tau<=14`. With error probabilities `eP=P(decide Q)`, `eQ=Q(decide P)`, put

`V14(alpha)=min max(E_P tau,E_Q tau)` subject to `eP,eQ<=alpha`.

The Stage97 endpoint has

```text
alpha97 = 2586269934456514327 / 7450150876955541504
V97     = 757686080746453135 / 58204303726215168
s97     = 12365744850625211 / 20889600000000000
```

Define `K98=17496/13`, `lambdaP=16488/13`, `lambdaQ=17496/13`, `Gamma98=33984/13`, and `eta98=4993625/12934289716936704`.

**For every real `0<=delta<=eta98`**,

```text
V14(alpha97+delta) = V97 - (33984/13)*delta.
alpha98 = 2586269937332842327 / 7450150876955541504
V98     = 757686022002985135 / 58204303726215168.
```

The same supporting line is **sharp on the right**: it cannot attain `V14(alpha)` for `alpha>alpha98`.

## Complete dual lower bound

For the count triple `v=(n,a,b)`, `n<=14`, likelihood ratio `Q(w)/P(w)=2^(a+b)/3^a`. Backward Bellman induction gives

```text
D(n,a,b)=min{
   lambdaQ*2^(a+b)/3^a,  [immediately decide P]
   lambdaP,              [immediately decide Q]
   1+P0*D(n+1,a+1,b)+P1*D(n+1,a,b+1)+P2*D(n+1,a,b)
}
```

Continuation is absent at `n=14`. This minimizes `tP+lambdaP*eP+lambdaQ*eQ` over **all** randomized history-dependent tests because iid conditional action costs depend only on `(n,a,b)`; it does **not** identify distinct ordered-word probability paths.

The complete exact rational enumeration has **680 states and 1240 nonchosen actions**; 1238 gaps are strictly positive (minimum `1/156`), none negative, and **only two ties**: `A98=(13,6,4)` (continue vs decide Q) and `B=(12,0,1)` (continue vs decide Q). Thus

```text
D(root) = 81941716076224522891/89018346875387904
        = V97 + Gamma98*alpha97,
V14(alpha) >= D(root) - Gamma98*alpha.
```

At the Stage97 primal endpoint `A98` immediately decides Q, `B` decides Q with probability `s97`, and all other states follow their unique Bellman minimizing action. In particular `A97=(4,4,0)` is frozen to P, not a K98 tie.

## Ordered first-hit cones and exact weights

Exact first-hit propagation preserves every ordered history's distinct positive P and Q weights. At `A98` there are **18438 actual ordered first-hit words**, with aggregate `pA=384125/3131031158784`, `qA=384125/2229025112064`. At `B` there are **12** with `pB=48828125/725594112`, `qB=48828125/362797056`.

When continuing at either critical state, the conditional suffix vector `(P-error,Q-error,P-extra-time,Q-extra-time)` is exactly

```text
RA=(7/8,1/12,1,1)                 [3 terminal suffix words]
RB=(63/64,1/144,9/8,13/12)       [5 terminal suffix words].
```

The cones are disjoint: at observation 12 every `B` history has zero `0` symbols, whereas by observation 13 every `A98` history has six. Thus no single ordered path can encounter both critical states.

Set

```text
X=pA*(1-RA.Perror)=384125/25048249270272
Y=qA*RA.Qerror    =384125/26748301344768
E=pB*(1-RB.Perror)=48828125/46438023168
H=qB*RB.Qerror    =48828125/52242776064.
```

## Primal construction, every real parameter

For arbitrary real `u in [0,1]`, at `A98` continue with probability `u` and otherwise decide Q; at `B` immediately decide Q with probability `s=s97+h98*u`, otherwise continue; freeze all other actions. Disjoint cones give exact affine identities for **every** such real pair:

```text
eP=alpha97 - X*u + E*(s-s97)
eQ=alpha97 + Y*u - H*(s-s97).
```

Take

```text
h98=(X+Y)/(E+H)=2602831/174080000000
s98=s97+h98=12366057190345211/20889600000000000
eta98=E*h98-X=Y-H*h98=4993625/12934289716936704 > 0.
```

Here `0<s97<s98<1`, so all `u in [0,1]` are admissible and `eP=eQ=alpha97+eta98*u`. All used actions attain the Bellman minimum, whence

`tP+lambdaP*eP+lambdaQ*eQ=D(root)`.

The four metrics are affine in `u`. At the endpoints, exact `tP-tQ` is respectively

```text
u=0: 1207593511071079775/1862537719238885376 > 0
u=1: 1207595370727759775/1862537719238885376 > 0.
```

Therefore `tP>tQ` on the entire real interval and `tP=D(root)-Gamma98*(alpha97+eta98*u)`. This achieves the universal dual lower bound, proving the theorem.

**Sharpness:** If the same line were achieved at any `alpha>alpha98`, both positive dual multipliers would force `eP=eQ=alpha` and only Bellman-minimal actions could be reached. The finite randomized policy occupation polytope is compact, so the optimum is attained. Only `A98` and `B` have zero action gaps. Any arbitrary ordered-history mixing within one of their count fibers can be P-arrival-averaged: Q/P is constant inside that fiber and all continuations have identical iid conditionals. The disjoint cones then enforce an effective `u,s in [0,1]` and `s=s97+h98*u`, so `alpha=alpha97+eta98*u<=alpha98`, a contradiction.

## Executable evidence and next question

The locally executed portable stdlib Fraction checker `CHECKER.py` verified all 680 states, 1240 action gaps, 18438/12 ordered first hits, exact branch suffix vectors, dual-root equality, endpoint/interior rational identities and the next affine dual crossing. A separate author implementation, `independent98.py`, explicitly walked 684557–739871 reached ordered terminal paths for `u in {0,1/5,1/2,1}`, checking P/Q errors, times, first hits and cone disjointness. **This is two author implementations, not independent Driver review.** The all-real theorem follows from the exact affine identities and endpoint inequalities, not from extrapolation of the four samples.

The largest fixed-policy dual crossing below K98 is **K99=6696/5**, candidate `A99=(11,3,0)`, with C/P tie. At K99 only A99 and B are tied. This is **a dual candidate only**: no Stage99 primal interval is claimed. Next: determine true A99 first-hit/suffix weights, cone overlap with B, type-error balancing, sign of `tP-tQ` and sharp endpoint. See `NEXT_TASK_PACKET_99.md`.

Native owner/CLAIM/Result and independent mathematical acceptance are **unverified**, so this artifact is an author evidence frontier, not formal Source Result/Working Truth/Foundation.
