# Stage433-B — Exact adjacent-budget future-quotient splitting and codebook cost

2026-11-04 · Research2 · **AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

Scientific inputs remain frozen at GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Parent Stage432-B is `50aa9195118514f569a2a158454fa151c266f2e4`. Current method/rules were separately consulted on main. Primitive directions A=+E1, B=-E1, C=+E2 are embedded in the full signed-native-X6 domain of twelve directions; chart-relative six-vectors are internal spatial displacements, not final cell addresses.

## Definition and general monotonicity lemma

Fix one current-observer fiber F of ordered word pairs P in D^m, Q in D^n with identical lengths, both native-six-vector endpoints, complete ordered directed adjacency histograms JP/JQ and index-matched K. P is frozen. A future operation word may perform at most p legal Q-POP and r arbitrary Q-APPEND over all twelve directions; all legal interleavings and every intermediate complete observer are tested. Let q_F(p,r) be the exact number of all-future observational-equivalence classes on F.

**Lemma 433.1 (monotone refinement; unconditional).** Whenever the budgets and same fiber are valid, q_F(p+1,r)>=q_F(p,r) and q_F(p,r+1)>=q_F(p,r). Every operation word admitted under the smaller budget remains admitted under the larger budget. Thus larger-budget future equivalence refines smaller-budget equivalence. No monotonicity in the other direction is asserted.

Under the *author-side Stage431-B boundary classification*, for n>=p+2, m>=n+r+1, the representative key is
T_(p,r)=(Q[n-p..n];P[n-p+1..n+r]), with one-based inclusive indices.
Increasing p adds **two** native direction symbols, Q[n-p-1] and P[n-p]; increasing r adds **one** symbol P[n+r+1]. Hence the further conditional bounds are
q_F(p,r)<=q_F(p+1,r)<=144 q_F(p,r) and
q_F(p,r)<=q_F(p,r+1)<=12 q_F(p,r).
These upper bounds use Stage431-B boundary completeness, which is still awaiting independent Driver review. The following exact small-fiber theorem is proved directly without that assumption.

## Theorem 433.2 (a completely enumerated native-X6 split under either budget increase)

Take m=5,n=2, and fix Q=CC, P=AAABA. The common current observer O has:
- x(P)=3E1, x(Q)=2E2, JP={AA:2, AB:1, BA:1}, JQ={CC:1}, and K=0.
- Its **entire** native twelve-direction word-pair fiber F consists of precisely (AAABA,CC), (AABAA,CC), (ABAAA,CC).

Proof of completeness: the endpoint/J residual of Stage432 recovers first directions A and C. Q has a single CC edge, hence Q=CC. The only P edges are two AA, one AB and one BA. Starting at A, the unique B can appear at position 2, 3 or 4, and the return BA must follow it; these are precisely the three displayed P words. All directions outside {A,B,C} have zero adjacency and cannot appear. Their first two P letters are A or B, so K(P,CC)=0 for every pair.

Direct future classification in this *same* observer fiber:

| Q budget (p,r) | classes by T key and population | q_F | minimum fixed label |
|---|---|---:|---:|
| (0,1) | C\|A:2; C\|B:1 | 2 | 1 bit |
| (1,1) | CC\|AA:1; CC\|AB:1; CC\|BA:1 | 3 | 2 bits |
| (0,2) | C\|AA:1; C\|AB:1; C\|BA:1 | 3 | 2 bits |
| (1,2) | CC\|AAB:1; CC\|ABA:1; CC\|BAA:1 | 3 | 2 bits |

These are **exact future equivalence counts**, not merely syntactic boundary counts: all smaller-budget operation words can inspect only the corresponding P positions, while future Q endpoint/J/length are shared because Q starts identically and undergoes identical actions. For (0,1), both AAABA and ABAAA have P3=A, hence no allowed one-step APPEND distinguishes them; AABAA has P3=B and is separated by APPEND(A). At (1,1), the pair AAABA/ABAAA is separated by POP,APPEND(A). At (0,2) it is separated by APPEND(A),APPEND(B). All three histories therefore form distinct classes at both expanded budgets; a fiber with three elements cannot have more than three classes. This proves **strict** growth 2->3 under p:0->1 and separately r:1->2.

## Full distinguishing state traces

For X0=(P=AAABA,Q=CC), X1=(P=ABAAA,Q=CC), initial Q=CC, xQ=2E2, JQ={CC:1}, K=0. P is unchanged in every row with xP=3E1 and JP={AA:2,AB:1,BA:1}.

**Additional POP:** Q POP to C gives xQ=E2, JQ={}, K=(0,0). APPEND(A) to CA gives xQ=E1+E2, JQ={CA:1}, final K=(1,0) for X0,X1 respectively. Both intermediate and final lengths and Q observers are identical across histories.

**Additional APPEND:** Q APPEND(A) to CCA gives xQ=E1+2E2, JQ={CC:1,CA:1}, K=(1,1). Next APPEND(B) to CCAB gives xQ=2E2, JQ={CC:1,CA:1,AB:1}, K=(2,1). Again all non-K observer fields match.

The executable checker saves **all complete intermediate observers** (not just K) and verifies these traces verbatim. It independently enumerates all 12^5 P words and 12^2 Q words against the fixed endpoint/J values, crosschecks directed-Euler enumeration, and compares every allowable operation word until a distinguishing witness is found. Tested budgets have respectively 13,38,157,614 admissible operation words.

## BRC residual and cost accounting

The three native histories carry nonnegative integral mass one each. The coarse (0,1) quotient has class masses (2,1), while either one-step larger horizon has (1,1,1). The extra bit needed at the larger horizon is the exact new future-discriminating residual, not a numerical approximation. For any finite fiber with q classes, an injective fixed-length class label needs ceil(log2 q) bits; this is a label-only bound, excluding common complete-observer storage, codebook and source-to-label conversion.

For this example, a naive 4-bit native direction ID per letter uses 4(m+n)=28 raw bits per history before shared-observer compression. The class labels use respectively 1 or 2 bits per history, **provided** the exact fiber and a map from histories or T keys to class IDs are available. Extracting T from an indexed source requires O(p+r) symbol accesses; scanning input takes O(m+n); the key contains 2p+r+1 labels (=4(2p+r+1) bits under the same naive codec). A finite codebook needs q entries with keys and output IDs. Constructing a universal codebook by enumerating full JP/JQ Euler histories can have exponential cost, and original-word recovery requires a separate witness lookup. This exact small-fiber result establishes information growth, not a general runtime speedup. The direct 12-symbol exhaustive test examines 12^5+12^2=248,976 raw candidate words; the directed-Euler enumerator avoids most candidates for this instance but has its own input/state/verification costs.

## Validation, status, next

`REPRO_STAGE433B.js` is self-contained and runs under Node.js (or a plain JS evaluator). Its actual executed JSON is in `REPRO_STAGE433B_EXECUTED.json`. The checker verified exact equality of the full fiber under two independent enumeration methods, all class masses, the 12-direction APPEND alphabet, and complete future-observation signatures for each compared pair. All arithmetic is integer/boolean with exact direction vectors; there are no floating-point tolerances.

The general monotone-refinement lemma is a direct proof. The finite fiber is exhaustive for the specified complete observer and horizons. Formal independent review and Source admission are separate pending governance steps.

**Next Stage434-B:** compute a family of variable-size fibers with strict successive class splits, investigate exact q_F(p,r) as a function of budgets and witness-dependent codebook construction cost, and connect empirical q measurements to the full Euler/J/K/T DP without treating the codebook as free.