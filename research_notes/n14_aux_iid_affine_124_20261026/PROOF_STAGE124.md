# Enterprise Math / R1-N14 auxiliary Stage124 — exact all-real affine interval

**Evidence tier:** author-proved finite-model theorem, independently *implemented* author cross-check; **not** independently reviewed, natively CLAIMed, frozen or promoted. All claims concern an **external** finite iid model, not P000, native X6 or Heartbeat dynamics.

## 1. Mother problem and immutable inputs

A sequential randomized decision between two ternary iid laws, horizon N=14:

- P=(1/8, 1/24, 5/6), Q=(1/12, 1/12, 5/6).
- eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau).
- V14(alpha)=min max(tP,tQ) over **all** randomized policies on literal ordered histories with 0<=tau<=14 and eP,eQ<=alpha.

Highest inherited author theorem: Stage123, file `research_notes/n14_aux_iid_affine_123_20261026/PROOF_STAGE123.md`, version at EM main@520517d398d10a46c55d6f106cee1db5a0e82a69.

alpha123=2573845365525582162925/7411551152237344456704;
V123=377878052586265662571445/29646204608949377826816.

Global rules read as one immutable `GLOBAL_KNOWLEDGE_V1` main@e8d65b2492cf35be071c32b0c9852487f100be07. Project P000 projection blob c6d4d2d79b09537bdae55253baef9c28583e44dc agrees with canonical P000 original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` (metadata checked). EM `docs/PORTABLE_RESEARCH_PROTOCOL.md` blob ca5de2d680d2439ff4b67c2c55fbd4159813cd5c and native project protocol apply to provenance, not as mathematical axioms.

## 2. Theorem (all real parameters)

Define

    eta124=8596140125/8578184203978407936,
    K124=1245231873/1658336,
    L124=36440256/51823,
    S124=K124+L124=2411320065/1658336.

Then **for every real** delta in [0, eta124]:

    V14(alpha123+delta) = V123 - S124*delta.

In particular, the exact right endpoint and value are

    alpha124=2573845372952647230925/7411551152237344456704,
    V124=377878009388672358128945/29646204608949377826816.

The affine supporting line is **right-sharp**: for every alpha in (alpha124,1],

    V14(alpha) > H124(0,0,0) - S124*alpha.

This is a statement about the support line, not infeasibility of the test beyond the endpoint.

## 3. Full-history Bellman lower bound

For s=(n,a,b), the count state of any ordered prefix (a counts symbol 0 and b counts symbol 1), the likelihood ratio is

    Q(prefix)/P(prefix) = 2^(a+b)/3^a.

Set H14(s)=min(K124*Q(prefix)/P(prefix), L124). Backward for n<14,

    H(s)=min { K124*2^(a+b)/3^a [declare P],
               L124               [declare Q],
               1+sum_j P_j H(s+e_j) [continue] }.

**Exact rational exhaustive result:** 680 count states, 1238 strictly positive nonchosen action gaps, no negative gaps, minimum strict gap `294166217221/39614118100992`. There are precisely two action ties:

- A=(9,3,0), declare P / continue.
- T=(14,7,4), declare P / declare Q.

Root:

    H0=5878829162353591081475135/11355563791072559628288
      =V123+S124*alpha123.

Bellman induction applies to arbitrary word-dependent randomized policies: within a given count state the prefix likelihood ratio and future iid suffix law are identical. Writing eP,eQ,tP for the four declared observables gives

    H0 <= tP + L124*eP + K124*eQ
       <= max(tP,tQ) + S124*alpha,

hence V14(alpha)>=H0-S124*alpha for all feasible alpha.

## 4. Literal branch provenance and the exact two-parameter strategy

At A, stop/declare P with probability y, else continue; at terminal T, declare P with probability z and Q with probability 1-z; at all other states take the unique Bellman-optimal action, in particular J=(10,5,4) now uniquely declares Q. All other actions remain deterministic.

Under the deterministic non-stopping-at-A skeleton, literal **first-hit ordered** histories give:

| State | first-hit words | P mass | Q mass |
| --- | ---: | ---: | ---: |
| A=(9,3,0) | 84 | 109375/1990656 | 109375/6718464 |
| T=(14,7,4) | 7962 | 165875/25048249270272 | 165875/26748301344768 |

A cannot be an ancestor of T: A to T would require (7-3)+(4-0)=8 counted draws within only 14-9=5 remaining observations. T is too deep to precede A. Thus the two ordered-prefix path cones are disjoint, including under probabilistic stopping, and no yz interaction survives in the four specified moments. BRC is actually reused here as finite explicit **positive rational weighted ordered paths** with separate P and Q weights, multiplicities and retained branch identity. The count quotient is admissible only for this iid four-observer, fixed-future horizon; no quotient to native P000 dynamics is asserted.

Define the moment vector M=(eP,eQ,tP,tQ). Let M00=M(0,0), dA=M(1,0)-M00, dT=M(0,1)-M00. Two independently written exact algorithms obtained

    M00=(
       608919703452600011/1752976676930715648,
       55715889515225/160489808068608,
       2798007941169380921/219122084616339456,
       161747615623729/13374150672384),
    dA=(
      -1921609375/7925422620672,
       259765625/835884417024,
      -20758609375/330225942528,
      -1476453125/69657034752),
    dT=(
      -165875/25048249270272,
       165875/26748301344768,
       0, 0).

All four corners have exact identity `M(1,1)=M00+dA+dT`, and by the disjoint-cone argument this holds for all **real** y,z in [0,1]: `M(y,z)=M00+y*dA+z*dT`.

Both error constraints bind if and only if

    y(z)=151548960415319/415627392000000
         -(160567/6927123200)*z.

Throughout the full real interval 0<=z<=1, this is a legal probability (0<y<1). The common error equals

    alpha(z)=alpha123+eta124*(1-z).

At z=1: y=151539326395319/415627392000000, M has error alpha123 and tP=V123, hence exactly agrees with the inherited Stage123 endpoint. At z=0: y=151548960415319/415627392000000, common error alpha124 and tP=V124.

The time differences at z=1 and z=0 are respectively

    19564551641189828171621/29646204608949377826816 >0,
    19564523009155753489121/29646204608949377826816 >0.

The difference tP-tQ is affine in z and strictly positive throughout [0,1]. Therefore max(tP,tQ)=tP. Every selected action Bellman-minimizes, so exact equality to the universal lower bound holds for each member of the continuum of strategies. Since z=1-delta/eta124 gives any real delta in [0,eta124], the theorem follows.

## 5. Right-sharpness

The finite-horizon tree contains finitely many histories, and its product of finite randomized action simplices is compact. An optimal feasible policy exists for each feasible alpha. Were a policy for alpha>alpha124 to attain the *same* supporting line H0-S124*alpha, all nonnegative gaps in the Bellman induction would have to vanish; positive K124,L124 would force eP=eQ=alpha, and tP=max(tP,tQ).

Only the two listed action ties are available. For arbitrary history-specific randomization within a count fiber, its occupancy-weighted effective stopping/terminal-decision probability can be averaged: Q-weight at each such prefix is a fixed positive likelihood ratio times P-weight, while future suffix laws coincide. Both error and time observers are preserved by this aggregation. Because A and T have disjoint path cones, the reduced observers must have the above `M(y,z)` form for some y,z in [0,1]. Tight error balance then forces y=y(z), and `alpha(z)=alpha123+eta124*(1-z)<=alpha124`, contradiction. Therefore the support line is sharply terminated at alpha124.

## 6. Actual author-side computation and limits

`VERIFY_STAGE124.py`: exact Python `Fraction` bottom-up Bellman over all 680 states; 1238 positive gaps; all tie identities; all four affine observer moments; inherited and new endpoints; strict P-time dominance; lower-bound equality; exact dual sweep. **Executed locally: PASS.**

`INDEPENDENT_ORDERED_STAGE124.py`: separately written integer-weight, literal ordered-prefix DFS using P=(3,1,20)/24 and Q=(1,1,10)/12, with exact terminal masses. All four deterministic (y,z) corners agree with the main checker; visits respectively 815542, 815542, 810502, 810502, and first hits A=84, T=7962 in every corner. **Executed locally: PASS.**

Author-side distinct implementations are *not* independent Research Driver reviews. No Lean formalization, native P000/X6 bridge or claim of actual physical-world law. No source-native Result freeze.

## 7. A non-promoted Stage125 candidate and explicit next unit

At Stage124's right edge z=0 (T uniquely declares Q), keep the A P/continue tie along the dual direction

    dK/dt=-1, dL/dt=-608000/474363.

For every strictly positive frozen-policy Bellman gap with negative derivative, compare its first zero `-gap/(d gap/dt)`. The first collision occurs exactly at

    t=13731333106707/1006541960224,
    U=(12,7,5), competing declare Q / continue.

The resulting **dual candidate only** is

    K125=3579845625/4855672,
    L125=416181048/606959.

Fresh 680-state exact Bellman at (K125,L125) finds ties A=(9,3,0) P/continue and U=(12,7,5) Q/continue, 1238 strictly positive gaps, no negative gaps, and minimum strict gap `578968738307/115991671209984`. A *primal* optimal interval is **not** yet established. Next calculate U's ordered first-hit mass, disjointness or intersection with A (A->U would require 9 counted draws in 3 steps, so ancestry is already excluded), exact four-moment increments, legal balancing interval and right-sharpness; then author and separate Driver checks as required.

## 8. Identity, authority and persistence boundary

Authenticated connected GitHub identity: `awdawmip`, with repository push/admin privilege; this proves the GitHub writer, *not* native Researcher/Owner. Source-native task inventory returned `CONTROL_QUOTA`; native session start returned `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. Thus live owner, native CLAIM, native Result and independent Driver acceptance are **unverified**. This author research checkpoint must not be represented as an accepted formal task result; no access-control restriction was bypassed or attempted via Drive.
