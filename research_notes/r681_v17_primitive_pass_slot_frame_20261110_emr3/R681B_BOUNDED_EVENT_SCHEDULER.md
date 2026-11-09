# R681-B｜一次性三 PASS 的最小整数自主调度器

This appendix uses the exact R681/R680 model, not an independent new P000 law. Source input is the six R679 starting biases and the three licensed internal one-shot PASS labels A=(0->1), B=(1->2), C=(2->0). All update events act on four internal field/port coordinates at one chosen native X6 Cell, not on the six original spatial axes.

## 1. Constructive bounded policy

Retain the V29 nonnegative ledger M and impose the explicit auxiliary one-shot capacity that event e=(a,b) is eligible iff M_ab=0. This is part of the finite experimental task, not a theorem that V29 alone creates a physical one-shot resource.

At each event instant, let u be the *current* four-field discrepancy, and use the already source-backed R680 covector w=(-1,1,-2,-1). Compute an integer event score

G_e(u,M) = 2*(u_a-u_b) + (w_a-w_b)

for each currently eligible e; choose a highest-scoring event and then perform the native nonnegative V29 PASS update M_ab<-M_ab+1, u_a<-u_a+1, u_b<-u_b-1. After the PASS, apply R680's exact unique V27 triad successor and the R681 inherited ordered V17 slot update.

Thus once the initial (u0,M=0,F0) is supplied, both the event order and the triad/slot evolution are deterministic functions of the current state, **without a separately supplied PASS word**.

## 2. Exact selection theorem and sharp multiplier within this domain

A full prefix census contains 6*(1+3+6)=60 state-labeled nonterminal PASS histories. For each of those states, all eligible event scores G_e are distinct at the maximum. More strongly, if primary event preference is D_e=u_a-u_b, then for **every pair of eligible events**, D_e>D_f implies G_e>G_f.

For general positive integer multiplier K in place of 2, complete exact comparison over all 60 states yields:

| K | Ties for best event | Strict primary comparisons not preserved |
|---|---:|---:|
| 1 | 0 | 8 |
| 2 | 0 | 0 |
| 3–7 | 0 | 0 |

Consequently **K=2 is the minimum positive integer preserving *all pairwise strict primary preferences* in this exact restricted family**. K=1 already selects a unique best event everywhere; the sharper K=2 claim is about preservation of *every strict pair comparison*, not just uniqueness of the argmax.

The 60-state complete exhaustive proof is produced by R681_SCHEDULER_VERIFY.py. It uses no floating point and the already verified R681 V23/V27/V29 types and ordered-slot transition.

## 3. Generated event words and final frame evidence

For the six initial biases, the bounded autonomous policy chooses:

| Initial discrepancy u0 | Deterministic PASS order | Non-sorted final V17 frames among 20 starts |
|---|---|---:|
| (-4,-3,-2,10) | CBA | 8 |
| (-3,-2,-4,10) | BCA | 13 |
| (-2,-4,-3,10) | ABC | 11 |
| (2,4,3,-10) | BCA | 9 |
| (3,2,4,-10) | CAB | 14 |
| (4,3,2,-10) | BAC | 9 |

All 120 complete trajectories change their unordered active triad. In 64/120 of them, the final inherited slot frame is not the sorted terminal triad, demonstrating nontrivial slot ordering under a deterministic current-state event scheduler.

Conservation within this PASS batch: the increments of the three port discrepancies sum to zero at each step, and the complete A+B+C cycle restores the initial four-field discrepancy u0. The three nonnegative V29 channel entries each increase from zero to one. This is a local integer event-conservation assertion, not a V39 current closure theorem.

## 4. Typed equivariance

Let P be any simultaneous permutation of port labels and associated discrepancy/covector coordinates; transport each directed PASS edge (a,b) to (Pa,Pb). If u'=Pu and w'=Pw, then G_{Pe}(u',M')=G_e(u,M), with eligible-event sets carried by the same port permutation. Hence whenever the maximizer is unique, event selection commutes with the typed relabeling. The subsequent V27 triad update is covered by the source-typed R676 covariance premise when all V23 code and active-triad objects are transformed consistently.

This is a precise port/field covariance of the declared finite policy. It is not a proof of the unimplemented full six-axis geometric rotation action, nor of an intrinsic multi-Cell autonomous X6 event clock.

## 5. BRC status and next work

The candidate event policy reduces the six source-labeled unit-weight PASS branches for each initial bias to one deterministic selected word. The larger exact BRC carrier from R681 remains available to assess consequences of different admissible schedulers. Such policy selection is a declared dynamical choice; it does not prove that all original branches are physically absent.

Next: replace the auxiliary capacity rule by actual sourced local eligibility/credit in a many-Cell licensed network, couple TRANSFER and V39 loop current j, and compute the observer-future quotient and rotation/continuity constraints.

Verification: R681_SCHEDULER_VERIFY.py + R681_SCHEDULER_EVIDENCE.json. Status: author-side bounded exact constructive rule; no formal CLAIM or independent Driver admission.