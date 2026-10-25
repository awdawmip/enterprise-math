# N14 external auxiliary iid Stage131 — full-real exact optimality (author proof)

**Scope:** external ternary iid randomized sequential test at horizon N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), unrestricted stopping and decisions on literal ordered histories. Author-exact finite-computation-assisted proof; no native P000/X6/Heartbeat transfer or independent Driver acceptance.

Define eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau). V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

## Stage131 theorem

From the author-verified Stage130 endpoint
- alpha130 = 36696744084893090695/105616844785075617792;
- V130 = 660257040358974188827/52808422392537808896,

the following identity holds for **every real** 0<=delta<=eta131:

eta131 = **1623875/22920322218983424**,

**V14(alpha130+delta) = V130 - (7339156/5905)*delta.**

Right endpoint:
- **alpha131 = 36696744092375906695/105616844785075617792**;
- **V131 = 660257035708884947227/52808422392537808896**.

The affine support is **right-sharp**, but this does not assert infeasibility beyond alpha131.

## Exact unrestricted-history Bellman lower bound

For any ordered word h with count state s=(n,a,b), the ratio Q(h)/P(h)=2^(a+b)/3^a. Write r_s for this ratio. With K=3787884/5905 and L=3551272/5905 define the P-weighted Bellman value

H(s)=min{ K*r_s (declare P), L (declare Q), 1+sum_j P_j H(s+e_j) (continue, only if n<14)}.

The future conditional iid distribution and likelihood ratio are constant over ordered histories of the same count. Therefore this recurrence can be applied at every individual ordered prefix, **without assuming that the test is count-based**. Exhaustive exact Fraction recursion visits 680 states, finds 1238 strictly positive nonchosen-action gaps, no negative gaps, minimum strict gap 13530313/2204029440, and exactly two ties:
- B=(11,0,1): Q versus continue;
- A=(12,7,3): P versus continue.

The exact root value is H(0,0,0)=38329289789453267095823/86261060643965632512. Every unrestricted ordered-history policy satisfies

H(root) <= tP + L*eP + K*eQ <= max(tP,tQ)+(K+L)*alpha.

## Positive-weight ordered BRC carrier

Keep literal prefix/branch identity, exact P/Q positive-rational branch weight products, declared action and stopping depth until the four outputs M=(eP,eQ,tP,tQ) have been computed. This uses the existing weighted-BRC alternative/serial composition law in its exact positive-rational scope. A total-only quotient before the stopping/first-hit observer would lose data, and no signed/phase or P000 observer equivalence is asserted.

An independently coded **top-down integer numerator literal-word DFS** under the Stage131 strict Bellman actions and the two tie coins gives actual first-hit carriers:

| Tie | Literal first hits | P mass | Q mass |
|---|---:|---|---|
| B=(11,0,1) | 11 | 107421875/1451188224 | 107421875/725594112 |
| A=(12,7,3) | 3168 | 275/3623878656 | 275/7739670528 |

The two cones are disjoint: A at depth12 cannot precede B at depth11; a path through B at depth11 has zero symbol-0 occurrences, so its single next step cannot produce A's seven symbol-0 occurrences.

Let w be immediate Q-stop probability at B (else continue), and u immediate P-stop probability at A (else continue). With all other actions strictly fixed, the exact four-observer vector for **all real w,u in [0,1]** is

M(w,u)=M00 + w*dB + u*dA,

where the following exact rational vectors were independently obtained:

M00 = (
 2432101680871869569/7011906707722862592,
 446766722356241/1283918464548864,
 10981948818473021711/876488338465357824,
 1282024322461333/106993205379072)

dB = (
 4619140625/2229025112064,
 -751953125/417942208512,
 -25673828125/278628139008,
 -17939453125/104485552128)

dA = (
 -275/2087354105856,
 275/1114512556032,
 -6875/86973087744,
 -3575/92876046336).

The interaction M11-M10-M01+M00 is exactly (0,0,0,0) by path cone disjointness and by exact computation. Literal DFS prefix visits for corners (w,u)=(0,0),(0,1),(1,0),(1,1) are 775522,756514,775390,756382; terminal literal word counts are 517015,504343,516927,504255.

## Full continuum primal certificate

Solving eP=eQ gives the exact balancing law

**w(u) = 23520936469043837/81438720000000000 + (18849/192800000000)*u, 0<=u<=1.**

In particular 0<w(0)<w(1)=23520944430861437/81438720000000000<1. The resulting policy family has

eP=eQ=alpha130 + [1623875/22920322218983424]*u,

tP=V130 - [504566975/5730080554745856]*u
   =V130 - [(7339156/5905)*(1623875/22920322218983424)]*u.

The margins tP-tQ at u=0 and u=1 are, respectively,

90328571491797589607/158425267177613426688
and
90328566298908296807/158425267177613426688,

strictly positive. All four observables are affine on the real segment, hence tP>tQ everywhere. Every used action minimizes its Bellman offer, so tP + L*eP + K*eQ=H(root) throughout the segment. The unrestricted-history lower bound is attained at every real u, establishing the theorem.

## Right-sharpness, including history-specific randomized coins

The finite behavioral-policy cube is compact; the infimum is attained. If any policy for alpha>alpha131 attained the **same support line**, equality in H<=tP+L*eP+K*eQ<=max(tP,tQ)+(K+L)*alpha (K,L>0) would force eP=eQ=alpha, tP=max(tP,tQ), and only zero-gap Bellman actions at each positive-mass history. The 1238 positive gaps exclude all actions except ties at A and B. Although the remaining tie coins may depend on the individual ordered prefix, every prefix with the same count has the same likelihood ratio and same future iid suffix. Its P-mass-weighted effective stopping probability reproduces all four observers. The disjoint path cones eliminate any mixed term. Hence all candidate equality policies reduce observationally to effective w,u in [0,1], and error equality forces the displayed w(u); therefore alpha=alpha130+eta131*u<=alpha131, contradiction. This proves right-sharpness for unrestricted literal-history randomized policies.

## Evidence and authority

Two independent-in-implementation (but both author-side) exact programs have been actually run locally: bottom-up Fraction Bellman plus four-corner moments and top-down Bellman plus integer product literal-history DFS. The programs and computer-readable evidence are adjacent. These calculations cover the **entire declared finite count-state domain and literal-word deterministic corners**, with algebra proving interpolation over real coin parameters; they do not prove native dynamics correspondence.

Fixed input pins: GLOBAL_KNOWLEDGE_V1 main@90a2dbab9e17c77b3a4c74bea4785e6f0e240321; P000 original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; Enterprise Math source control@49f0bdada7acc91157a9967b5d6374219cd9de25; predecessor PROOF_STAGE130.md. Connected GitHub actor awdawmip. Real native inventory/dispatch returned CONTROL_QUOTA; real session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No active owner or CLAIM was verified. This repository research note is **not** a native Result or independent Driver acceptance.

## Stage132 next dual candidate only

At Stage131 endpoint u=1, B stays mixed. An exact affine gap scan of K+t*(-1), L+t*(-112/129) finds first new gap closure at t=125669547144/44663654405, giving K132=4830610068/7563701 and L132=4530338888/7563701. New P/continue tie E=(8,3,0); B remains Q/continue. At the candidate 1238 gaps are strict positive with least gap 27060626/5513938029, root H=244470485409835455673973219/552457976844897119895552. This is **DUAL_CANDIDATE_ONLY**; see NEXT_TASK_PACKET_132.md for the precise next work.