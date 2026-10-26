# Stage163: exact full-real minimax support and sharp right endpoint (R1 author)

**Claim type:** author exact-rational computation-assisted proof for an **external ternary iid N=14 sequential testing model**. The local checked code and run evidence are in the local Stage163 ZIP; this GitHub source is an independently versioned portable adaptation of the already-published Stage162 code, and is not claimed byte-identical to the locally executed code. No independent Research Driver review, native session/CLAIM/Result, or P000 X6 transfer is claimed.

## Inputs and provenance

GLOBAL_KNOWLEDGE_V1 verified current frozen input: `main@26a5b1b309aee44516bb5ee17ae76620521fe9de` (bootstrap, manual, project bootstrap, P000, ACTIVE worldview, research/BRC/portable and persistence protocols). EM input: `main@2fc58c45f2d48259be0e236f01ff0a44dfea51ef`; exact prior materials: `research_notes/n14_aux_iid_affine_162_r1_author_20261026/PROOF_STAGE162.md`, `NEXT_TASK_PACKET_163.md`, `candidate163_summary.json`. GitHub identity: `awdawmip`. Native dispatch failed `CONTROL_QUOTA`; session start failed `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. Formal owner/CLAIM unknown.

Take at most 14 **ordered** iid observations with
```
P = (1/8, 1/24, 5/6)
Q = (1/12, 1/12, 5/6)
```
and full-history randomized stopping/decisions. Let `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P(tau)`, `tQ=E_Q(tau)`, and `V14(alpha)=min_{eP,eQ<=alpha} max(tP,tQ)`.

**Theorem.** For every **real** `0<=delta<=69268826375/26145969225596928`,
```
V14(alpha162+delta) = V162 - (138328698737/237493119)*delta
alpha162 = 440625031179621048365/1265046575011281764352
V162 = 2138966145833987829541/180720939287325966336
alpha163 = 440628382682516376365/1265046575011281764352
V163 = 2138687275177334037541/180720939287325966336
```
The same affine support is **strictly below** the actual optimum for every `alpha>alpha163`, provided alpha remains in the nontrivial error-bound domain.

## Exact Bellman lower bound

For count state `s=(n,a,b)`, `n<=14`, where a and b count first and second symbols, the ordered-prefix likelihood ratio is `ell(s)=2^(a+b)/3^a`. Set
```
K = 163900037061/554150611
L = 476600779976/1662451833
K+L = 138328698737/237493119
```
and `H(s)=min(K*ell(s), L, 1+sum_j P_j*H(child(s,j)))` with no continuation at n=14. Exact Fraction enumeration of all 680 states yields exactly the nontrivial action ties `R=(10,0,1): Q/continue`, `Y=(8,4,1): P/continue`, and 1238 strictly positive other action gaps with minimum `1577397669610597/79424873185738752`. Root:
```
H(0) = 9776752862063305564417447471/45534988902651828797177856
```
Bellman induction on complete ordered histories and the exact Q/P change of measure yields universally
```
H(0) <= tP + K*eQ + L*eP <= max(tP,tQ)+(K+L)*alpha .
```
Thus `H(0)-(K+L)*alpha` is a lower bound for arbitrary ordered-history randomized policies, not merely count-state policies.

## BRC ordered carrier and attainable primal interval

Retain each **ordered, labeled path prefix**, positive rational P/Q weights, first-hit tie port, decision, and observation depth. The declared observer is the four-tuple `M=(eP,eQ,tP,tQ)`; count compression is justified only for this declared iid suffix future because equal-count prefixes have the same conditional future under P and Q and the same likelihood ratio. No native X6 quotient follows.

Let r be the probability of immediate Q at R, y the probability of immediate P at Y, continuing otherwise. Fix the strict optimal action elsewhere. Independent literal integer-weight prefix DFS gives:
```
tie                 ordered first hits     P first-hit mass        Q first-hit mass
R=(10,0,1)                 10               9765625/120932352       9765625/60466176
Y=(8,4,1)                 168              875/884736              875/2239488
```
The first-hit cones are disjoint: R has depth 10>8, while Y's first-symbol count 4 cannot decrease to R's count 0. Thus `M(r,y)=M00+r*dR+y*dY` exactly; the corner mixed difference `M11-M10-M01+M00=(0,0,0,0)`.

The exact four-observer coefficient vectors in order `(eP,eQ,tP,tQ)`:
```
M00 = (608980572829895015/1752976676930715648,
       28011719403025/80244904034304,
       2600662244346814961/219122084616339456,
       17058155693101/1486016741376)
dR  = (4521484375/1486016741376,
      -3232421875/1253826625536,
      -61181640625/557256278016,
      -20751953125/104485552128)
dY  = (-615115375/84537841287168,
        36976625/3343537668096,
       -4173890875/3522410053632,
       -5606125/10319560704)
```
Four corners were checked by both an exact count-suffix recursion and an independent **unmerged ordered integer-weight DFS** with node totals `473080,445864,472840,445624` in `(00,01,10,11)` order. Both P and Q total terminal masses equal exactly 1 at each corner. See `certificate163.json` for all rational corner outputs.

Solving `eP=eQ` gives the entire legal balanced segment
```
r(y) = 1766864861392271/5911808000000000
     + (430465623/131960000000)*y,   0<=y<=1.
```
Both coins remain in [0,1], and common error strictly increases between alpha162 at y=0 and alpha163 at y=1. At the two endpoints,
```
tP-tQ (left)  = 526240831439401052735/1265046575011281764352 > 0
tP-tQ (right) = 525795582839779772735/1265046575011281764352 > 0 .
```
Exact substitution at **both** endpoints gives `tP+K*eQ+L*eP=H(0)`. Because all four observables are affine in y, the dual equality and positivity of tP-tQ hold for **every real y** between endpoints. Hence `max(tP,tQ)=tP=H(0)-(K+L)*alpha`, achieving the bound for the entire interval.

## Strict right sharpness

Finite complete-history randomized policies comprise a finite product of compact simplices; continuous probability/time outputs imply a feasible minimum is attained. If the same support were attained at any alpha>alpha163, positivity K,L would force eP=eQ=alpha and equality in the Bellman induction at every positively reached state. The 1238 strict gaps exclude every nonoptimal action, leaving only R and Y tie randomization. Even if full histories choose distinct coins at the same count state, equal conditional suffix laws and same Q/P likelihood ratio permit their mass-weighted averages to be represented by one r and one y without changing the four outputs. Disjoint first-hit cones make the exact affine M apply. Error equality forces the displayed r(y), with y<=1 giving common alpha<=alpha163 — contradiction. The attained optimum must therefore be **strictly higher** than that support to the right.

## Evidence boundary and next science

The locally actually executed author verifier produced `PASS Stage163 author exact interval + sharpness`, with independent count/ordered DFS exact equality and certificate. `VERIFY_STAGE163.py` in this GitHub folder is a **portable adaptation** of the Stage162 checker; the local downloaded evidence ZIP carries the exact executed file and logs. Source publication does not mean remote execution. Stage163 remains author-checked/unreviewed and external; native P000/X6 observer bridge is unproved.

Exact forward **dual-only** scan gives Stage164 parameters `K164=211248/725`, `L164=615448/2175` and ties R=(10,0,1) Q/C, S=(13,5,2) P/C; 680 states, 1238 strictly positive gaps and none negative. Its **primal** interval and sharpness remain open. The next unit is calculating exact first-hit cones and all four observer corners at R and S, and proving balance/feasibility or reporting a rational obstruction; see `NEXT_TASK_PACKET_164.md`.
