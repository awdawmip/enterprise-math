# Stage167 — complete-real optimal interval, exact ordered-history certificate

**Status:** `STAGE167_AUTHOR_EXACT / PROOF_ASSISTED_BY_EXACT_COMPUTATION / NO_NATIVE_CLAIM / NOT_INDEPENDENTLY_REVIEWED`. Date 2026-10-26. This is a theorem **inside the declared external N14 ternary IID model**, not native P000/X6 mathematics.

## Provenance and input pins

GLOBAL_KNOWLEDGE_V1: `awdawmip/chatgpt-global-knowledge@1f73bff7ce37e663922e3c8dd29411441b0e37a7`. Bootstrap/manual, ACTIVE worldview, mathematics and BRC policies were read at that fixed snapshot. P000 startup projection at the same pin matches original P000 Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`.

Enterprise Math current-main scientific/control input: `5bb2fa911e40e26a72911a10241b2d329152425d`, including `docs/PORTABLE_RESEARCH_PROTOCOL.md`. Frozen predecessor Stage166: `afe5741b47c2a1eb5c9c36ff564cd96a33d11fec`, `research/r2-n14-stage166-full-real-20261026-t11`. Its `dual167.json` was a dual-only **candidate**. The current proof independently constructs the primal observers from the declared model.

## Exact theorem

Let `P=(1/8,1/24,5/6)`, `Q=(1/12,1/12,5/6)`. A randomized stopping-and-decision rule can inspect the complete ordered ternary history, must stop by depth 14, and decides either P or Q. Write `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P tau`, `tQ=E_Q tau`, and

`V14(alpha)=min_{eP,eQ<=alpha} max(tP,tQ)`.

The exact Stage166 endpoint is
`alpha166=881262643750052083615/2530093150022563528704`,
`V166=4276909130601160631957/361441878574651932672`.

For **every real** `0<=delta<=eta167` (including irrational delta),

```text
eta167 = 24019235264125/4392522829900283904
V14(alpha166 + delta) =
    V166 - (304356546634084/576461646339) * delta.
```

The exact endpoint is

```text
alpha167 = 881276478829564219615/2530093150022563528704
V167     = 4275865622441272343957/361441878574651932672
```

For alpha>alpha167, the **same affine Bellman support line** is strictly below the optimum. This does not mean V14 stops at alpha167.

## Universal Bellman bound, finite exhaustive check

For count state `s=(n,a,b)` with `a` zeros and `b` ones, the likelihood ratio is `ell(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a`. Set

```text
K=51166022460516/192153882113
L=150858479252536/576461646339
```

The Bellman recurrence is

`H_s=min(K*ell(s), L, 1+sum_i P_i H_child(s,i))`

with the continuation choice removed at n=14. Backward induction for arbitrary ordered-history randomized policies proves

`tP + K*eQ + L*eP >= H_root`.

Exact Fraction enumeration of all `sum_{n=0}^{14}(n+1)(n+2)/2=680` states gives

`H_root=12362030636126506094814337691297/63157738823584353992721825792`.

Only two states tie, and both ties are stop-Q/continue: `R=(10,0,1)` and `X=(5,1,2)`. All other active minimizers are unique; **1,238** nonminimizing action gaps are strictly positive, none negative, and the smallest is
`172366798507207447/5163915757745737728`.
With K,L>0 this supplies

`V14(alpha)>=H_root-(K+L)*alpha`.

## Primal construction and exact independent observers

At R choose stop-Q with probability r; at X choose stop-Q with probability x; otherwise take the unique Bellman action. The first-hit ordered-history sets are disjoint prefix cones: every R history has ten symbols and **no zero**, whereas every X history already has a zero by depth five. There are exactly 10 first-hit R paths and 20 first-hit X paths; their P/Q prefix masses are:

```text
R: (9765625/120932352, 9765625/60466176)
X: (125/41472, 125/15552)
```

This provenance-preserving branch decomposition makes the observer vector `M=(eP,eQ,tP,tQ)` affine:

`M(r,x)=M00 + r*dR + x*dX`.

The actual executed `VERIFY_STAGE167.py` in the companion portable package computes all four deterministic corners twice: (1) cached exact rational suffix recursion, (2) an **unmerged complete ordered-history DFS** using integer edge weights `P=(3,1,20)/24` and `Q=(1,1,10)/12`. Four DFS traversals cover **1,509,988 nodes**. All sixteen observer coordinates agree exactly, both terminal distributions have mass one, and `M11-M10-M01+M00=(0,0,0,0)`. The complete rational corners, deltas and execution checks are in the accompanying `certificate167.json`.

The coefficient of r in `D(M)=eP-eQ` is nonzero, so equal errors determine

`r(x)=3629376130799541/11823616000000000-(167005511153/7389760000000)*x`.

For every **real** x in [0,1], r(x) remains strictly between 0 and 1. At x=0, r equals the inherited Stage166 endpoint coin and both equal error and expected P-time match the prior endpoint exactly. At x=1, r equals `3362167312954741/11823616000000000`. For all such x,

`eP=eQ=alpha166+eta167*x`.

The exact time-dominance gaps at the endpoints are respectively

```text
(tP-tQ)(0) = 350562645358878053965/843364383340854509568 >0
(tP-tQ)(1) = 1062481681491670833895/2530093150022563528704 >0.
```

Both endpoints satisfy `tP+K*eQ+L*eP=H_root`. All four observers are affine in x, so strict tP dominance, dual equality, and the resulting minimax primal equality hold **throughout the real interval**, rather than only on rational grid points.

## Strict right-support sharpness

The finite full-history policy parameter space is compact. If any alpha>alpha167 attained the same Bellman lower line, equality in

`max(tP,tQ) >= tP >= H_root-K*eQ-L*eP >= H_root-(K+L)*alpha`

would force `eP=eQ=alpha` because K,L>0, and every reached-history action would be a Bellman minimizer because all three P symbol probabilities are positive. Outside R,X the action is unique. Each hit of a tied count state has the same Q/P prefix ratio and identical suffix observers, so replacing heterogeneous per-history tie coins by their **P-prefix-weighted average** preserves both P/Q errors and both expected times. The two first-hit cones are disjoint, hence every equality policy is observer-equivalent to a pair `(r,x) in [0,1]^2`. Error balance forces r=r(x), implying `alpha<=alpha167`, contradiction. This proves **sharpness of this supporting line**, not termination of the value function.

## Claim, method, and admission boundaries

All arithmetic was exact rational/integer; no tolerance-based test. The two algorithms share the model and selected Bellman minimizers, so this is an **author-side** proof/certificate, not an independent Driver review or a proof-assistant formalization. BRC reuse is precisely ordered **positive rational branch mass with separate P/Q observers and provenance**; it is not a proof of a native GF(2)-BRC/X6 mapping. Native P000 stays protected and unchanged.

Verified GitHub actor: `awdawmip`, repository write enabled. Native `em_control_tasks` and `em_control_dispatch` returned `CONTROL_QUOTA`; `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. Therefore current live owner, official CLAIM, Result and independent Driver admission remain **unverified/not performed**. This branch is source-side author evidence, not formal acceptance.

**Next unit:** Stage168 dual-only scan preserving R Q/C tie and choosing Q at saturated X. First new closure at `Z=(9,2,0)` P/C, candidate `K168=2152236456/8362241`, `L168=2125312232/8362241`; Stage168 primal interval and sharpness remain open. See `NEXT_TASK_PACKET_168.md`.
