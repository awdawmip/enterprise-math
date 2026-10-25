# N14 auxiliary iid Stage130 — exact full-real affine optimum, author-side proof

**Evidence grade:** AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF, two locally executed exact implementations. Independent Research Driver review, native CLAIM and Result are **not** established. External finite iid model only; not a native P000 six-axis / Heartbeat theorem.

## Full real theorem

For N=14, iid ternary P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6), arbitrary stopping and randomized decisions on **literal ordered histories** are allowed. Write eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau). Let V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

From the author-verified Stage129 endpoint

- alpha129=36696744060534746695/105616844785075617792;
- V129=660257055729711878827/52808422392537808896,

take K130=522693/802, L130=244736/401, S130=1012165/802 and eta130=126866375/550087733255602176.

**Theorem. For every real 0<=delta<=eta130,**

```
V14(alpha129+delta)=V129-(1012165/802)*delta.
```

The new right endpoint and optimum are

- **alpha130=36696744084893090695/105616844785075617792**;
- **V130=660257040358974188827/52808422392537808896**.

The same affine support is **right-sharp**, without asserting global infeasibility above alpha130.

## Exact dual for the full ordered-history class

At count state s=(n,a,b), a=#symbol0 and b=#symbol1, every ordered prefix has Q/P likelihood ratio r=2^(a+b)/3^a. The P-weighted exact Bellman offers are terminal P: K*r; terminal Q: L; and continuation (if n<14): 1+sum(P_j H(child_j)). Exact rational backward recursion visits every one of the 680 finite count states; it finds **1238 strictly positive nonchosen-action gaps**, no negative gaps, smallest strict gap 517/28872. Exactly two ties:

- B=(11,0,1), Q/continue;
- T=(14,7,4), terminal P/Q.

The root lower-bound certificate is

```
H(root)=52838467869186182216021/117157274574869495808.
```

The conditional iid suffix and exact ratio r depend only on count, so applying Bellman separately to every literal history proves for **all** randomized ordered-history tests

```
H(root) <= tP + L*eP + K*eQ
        <= max(tP,tQ)+(K+L)*alpha.
```

This four-observer iid argument does **not** collapse or assert equivalence for native P000/X6 observers.

## Literal BRC branch provenance and four-observer quotient

An independently implemented top-down **literal ordered-word integer-product DFS**, retaining positive branch weights until final observation, gives these actual first-hit carriers under tie B continuing and tie T selecting Q:

| state | literal first hits | P mass | Q mass |
|---|---:|---|---|
| B=(11,0,1) | 11 | 107421875/1451188224 | 107421875/725594112 |
| T=(14,7,4) | 7593 | 316375/50096498540544 | 316375/53496602689536 |

The two descendant cones are disjoint. T cannot precede B (14>11). If B occurred by n=11, its zero-count a=0 can increase by at most 3 before n=14, not to T's a=7. All positive word/branch provenance is retained before the following **declared four-observer** quotient.

Let w denote immediate Q-stop probability at B (otherwise continue), and v denote terminal P-decision probability at T (otherwise decide Q). All other actions are uniquely optimal. For **all real** w,v in [0,1] define M=(eP,eQ,tP,tQ). Exact Bellman moment recursion and an independent integer-weight literal-history DFS check the four deterministic corners and prove

```
M(w,v)=M00+w*dB+v*dT
M11-M10-M01+M00=(0,0,0,0)
M00=(
 2432101725154245569/7011906707722862592,
 446766714763241/1283918464548864,
 10981948818473021711/876488338465357824,
 1282024322461333/106993205379072)
dB=(
 4619140625/2229025112064,
 -751953125/417942208512,
 -25673828125/278628139008,
 -17939453125/104485552128)
dT=(
 -316375/50096498540544,
 316375/53496602689536,
 0,0).
```

The time effect of T is exactly zero because it is a terminal decision at depth14. The independent literal DFS visits 775522,775522,775390,775390 prefix nodes for corners 00,01,10,11, and respectively 517015,517015,516927,516927 completed literal histories. These are finite exhaustive exact counts, not Monte Carlo estimates.

## Primal interpolation for all real parameters

Solving eP=eQ yields the **exact** balancing relation

```
w(v) = 23520679218203837/81438720000000000
     + (194887/61696000000)*v,   0<=v<=1.
```

The interval is legal: 0<w(0)<w(1)=23520936469043837/81438720000000000<1. Exact substitution gives

```
eP=eQ=alpha129+(126866375/550087733255602176)*v;
tP=V129-(1012165/802)*(126866375/550087733255602176)*v.
```

The exact margins tP-tQ at v=0 and v=1 are

- 90328531682230099607/158425267177613426688 >0;
- 90328571491797589607/158425267177613426688 >0.

By affineness this remains positive for every real v in [0,1]; max(tP,tQ)=tP. Every reached decision Bellman-minimizes, so tP+K*eQ+L*eP=H(root); the universal dual lower bound is achieved throughout the full closed real segment.

## Proof of right-sharpness, including arbitrary prefix-specific tie coins

The finite behavioral policy space is compact. If an optimal policy attained the **same** dual affine line at alpha>alpha130, equality in its positive-coefficient lower bound would force eP=eQ=alpha, tP=max(tP,tQ), and only Bellman-zero-gap actions at every positively visited history. Exact strict gap enumeration leaves only B and T variable. Prefix-specific tie coins can be replaced, for the declared four observers, by effective stop probabilities w,v∈[0,1]: all prefixes of a fixed count have identical iid suffix laws and a fixed Q/P mass ratio; moreover the B and T descendant cones are disjoint. The resulting moments obey the displayed affine law, so balancing errors imposes w(v) above. It follows alpha=alpha129+eta130*v<=alpha130 because v<=1, contradicting alpha>alpha130. Thus this support is right-sharp for the **unrestricted literal-history class**.

## Verified scope and next question

Two locally run author-side Python stdlib exact rational programs PASS: a bottom-up 680-state Bellman + four-corner moment checker, and a separately constructed top-down Bellman + integer-numerator ordered DFS; their outputs match all four corners, first hits and both endpoint identities. No independent Research Driver review or formal proof assistant check; GitHub publication is **storage**, not remote execution.

A third exact affine-gap scanner locates Stage131 **DUAL CANDIDATE ONLY**: starting from T=P (v=1) and B mixed, keep B Q/C tie along dK=-1, dL=-112/129. First strictly positive gap closes at t=48619197/4735810, at A=(12,7,3) where P/C tie. K131=3787884/5905; L131=3551272/5905; root=38329289789453267095823/86261060643965632512; 1238 strictly positive gaps, least 13530313/2204029440; only ties A P/C and B Q/C. Stage131 real primal interval remains open.

**Fixed inputs:** GLOBAL_KNOWLEDGE_V1 main@363cc21deb56c429a3d1304e62bde6fd4c35452e; locked P000 original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; predecessor Stage129 published at EM main@6e879a2644d66fe73e03ebc178ee852d3416b3bf, research_notes/n14_aux_iid_affine_129_20261026/PROOF_STAGE129.md. GitHub connected actor awdawmip; native task query CONTROL_QUOTA, native session creation STATIC_READONLY_SCOPE_DENIED with operation_sent=false, so active native owner/CLAIM and independent mathematical acceptance remain **unverified**.
