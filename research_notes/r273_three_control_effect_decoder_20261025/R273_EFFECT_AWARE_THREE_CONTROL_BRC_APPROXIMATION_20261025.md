# R273 — Exact optimal source-query decoding after three-control affine BRC projection

**Date:** 2026-10-25. **Status:** AUTHOR DERIVATION / EXACT FINITE VERIFICATION; UNREVIEWED, NOT NATIVE-ADMITTED.

## Source and model

Pinned account knowledge: awdawmip/chatgpt-global-knowledge main@8d181121b901304f11f99b84614ac726b0e2a263, original P000 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, matching startup projection. P000 remains ACTIVE_LOCKED. Pinned Enterprise Math control Source: main@f3bbaf6384adeb47bf2296bf7f16afcd4b65027f. Reuse: R270 author certificate at ae394b2d4846e14763af593a49c1129fa1f9a25e, especially its 30-word-block reset count, checked independently again here. This is a **formal six-slot affine BRC**, NOT a verified native six-dimensional spatial update, physical heartbeat, or real R193 time-port/source observer.

Selectors a∈{0,1}, unit positive weight, initial control q=0. Per-step (target q, sign eta, bias b) table:

|q|a=0|a=1|
|--|--|--|
|0|(2,-1,-1)|(2,+1,-1)|
|1|(0,-1,-1)|(0,+1,-1)|
|2|(1,+1,+1)|(2,+1,-1)|

Full formal affine effect g=(eps,k) acts on formal slots as (eps*z1+k, eps*z2, z3,z4,z5,z6). Chronological composition (eps,k) THEN (eta,b)=(eta*eps,eta*k+b). The monitor r=0 means no 00 and last bit nonzero/start; r=1 means no 00 and last bit zero; r=2 means 00 occurred. Transition delta for a=0,1 is r0→(1,0), r1→(2,0), r2→(2,2). Initial full state (q,r,g)=(0,0,(+1,0)). Define P_n(q,r,g) exact ordered-word multiplicities at depth n, A_n(q,g)=P_n(q,0,g)+P_n(q,1,g), B_n(q,g)=P_n(q,2,g). The original terminal six-channel histogram is H_n(q,h,g) with h=0:A_n and h=1:B_n. The unmarked 3-control BRC retains only q,g, with total count U_n(q,g).

## Theorem A: precise optimality inside the unchanged three-control projection class

For all n≥0, q and g,

**U_n(q,g)=A_n(q,g)+B_n(q,g).**                                           (1)

Proof: removing the monitor from the full BRC recurrence is legitimate for the unmarked observer because q,g update depends only on (q,g,a), not r. Summing the exact recurrence over r and inducting from the common initial point mass proves (1) for **all finite n**, preserving exact endpoint/effect multiplicity, not merely support.

Let C3 consist of exactly this unmodified 3-control mass carrier together with an arbitrary deterministic terminal label decoder D(q,n,g)∈{0,1}. It may inspect full effect and length but must assign the whole same-state/effect fiber to one label. Normalize each six-channel joint histogram by 2^n. Then

**min_{D∈C3} TV_n(D) = M_n/2^n,  M_n = Σ_{q,g} min(A_n(q,g),B_n(q,g)).**    (2)

A minimizer is the per-fiber posterior-majority decoder: output 0 when A_n(q,g)≥B_n(q,g), otherwise 1.

Proof: in a fixed fiber write a=A_n,b=B_n. The exact channel pair is (a,b). D=0 emits (a+b,0), generating L1 error 2b; D=1 emits (0,a+b), generating L1 error 2a. Thus the attainable minimum is 2min(a,b), independent across fibers. Sum and divide by 2·2^n to get (2). This is both a lower bound **and an explicit decoder attaining it**. QED.

**Scope:** The theorem optimizes only C3, not all 3- or 6-state alternative BRC transition schemes. The MAP readout requires a potentially unbounded precomputed table indexed by n and effect; it is not a finite-state online monitor or a solved exact future-source representation.

## Theorem B: exact first collision and persistence

**M_0=M_1=M_2=0; M_n>0 for every n≥3.**

Finite words of length 0..2 are checked directly: no (q,g) fiber mixes hit/no-hit. At n=3, 000 has full state (q,r,g)=(0,2,(+1,-1)) while 101 has (0,0,(+1,-1)); hence the common (q,g) fiber mixes labels and has M_3≥1; exact enumeration gives M_3=1. For every later n, append the same (n−3)-length all-one suffix to both histories. Identical q,g propagates identically while the first monitor remains hit and the second remains no-hit. Thus a mixed fiber exists for every n≥3. QED.

## Theorem C: a three-control exact-effect model with asymptotically vanishing normalized error

Let F_0=0,F_1=1,F_{m+2}=F_{m+1}+F_m. The number of binary length-n words avoiding 00 equals F_{n+2}, by the exhaustive first-word decomposition (leading 1 or 01, with empty/boundary cases). Thus

Σ_{q,g} A_n(q,g)=F_{n+2},     Σ_{q,g} B_n(q,g)=2^n−F_{n+2}.             (3)

Keep the exact 3-state BRC U but use the **simple length-only deterministic decoder** D_time(q,n,g)=0 for n≤3, and 1 for n≥4. Then, for **every n**,

**TV_n(D_time)= min(F_{n+2}, 2^n−F_{n+2}) / 2^n.**                       (4)

Proof: when D_time=0 the only mismatched source labels are hit-00 paths; when D_time=1 they are no-00 paths. These have the exact masses in (3). Their global majority switches at n=4, where F_6=8=2^3. The ratio F_{n+2}/2^n decreases strictly from n≥1 because F_{n+3}<2F_{n+2}; it is ≤1/2 for n≥4. Equation (4) follows, including n=0 and n=1. For n≥4, TV_n=F_{n+2}/2^n. By Binet's recurrence solution this decays exponentially at rate phi/2<1 with phi=(1+sqrt(5))/2. Since the optimal decoder does at least as well, M_n/2^n→0 too. This is a **normalized** statement; the unnormalized L1 error of D_time is 2F_{n+2} for n≥4 and grows exponentially. QED.

The entire full affine-effect marginal is nevertheless reproduced exactly at every n. Therefore "nonzero absolute information loss" and "asymptotically zero normalized global total-variation error" are compatible.

## Theorem D: exponentially growing absolute ambiguity of even the best C3 decoder

R270's exact finite reset certificate gives P_30(0,0,(+1,-4))=16482 and six-channel base vectors for common effects at lengths j=7,8,9:
b7=(2,2,3,1,1,9), b8=(1,6,1,9,2,16), b9=(1,19,2,20,4,28), in (q0h0,q0h1,q1h0,q1h1,q2h0,q2h1) order.

For n≥7 put K=floor((n−7)/30), t=n−30K, j=7+((t−7) mod 3), h=(t−j)/3. Repeating any of the 16482 compatible 30-step reset words K times, then the reset word 101 h times, then a base j-word constructs at **one exact common effect** g_n=(eps_j,k_j−eps_j(4K+h)) at least 16482^K·b_j(c) distinct ordered words in *each* channel c. Fixed-length parsing proves injection; affine THEN proves identical g_n. Hence

M_n≥Σ_{q=0}^2 min(A_n(q,g_n),B_n(q,g_n))
≥ L_j·16482^K,
where L_7=L_8=4, L_9=7, because Σ_q min(b_j(q,0),b_j(q,1))=(4,4,7). Also M_n≤ΣA_n=F_{n+2}. Thus

**L_j·16482^K ≤ M_n ≤ F_{n+2} for every n≥7.**                  (5)

This is an all-depth proof conditional only on the explicitly finite R270 reset/base exact counts, independently rechecked in the attached code. Despite an exponentially growing **absolute** optimal error, TV_n*=M_n/2^n→0 exponentially by (3). No extrapolation from depth-128 tests is needed for (1)–(5). QED.

## Verification, interpretation and unresolved obligations

Exact local author verification: Python integer recurrence n=0..128, independent projected recurrence, brute all 8191 words of lengths 0..12, first collision, 30-step reset multiplicity 16482, six-channel base vectors, and lower bounds. Independent Boost C++17 big-integer recurrence n=0..96 rechecks the 16482 coefficient and selected minority counts. Samples: M3=1, M7=20, M8=36, M9=64, M20=17416, M30=2176446, M60=4052739183615, M80=61305790715800460. A standalone ZIP with the full executed programs, JSON report, SHA-256 file manifest and cold-start verification accompanies this result outside the branch. The files in this branch are research evidence/source, not a native Result.

**Reused interface:** exact positive-BRC multiset recurrence and chronological affine THEN law (REUSE_APPLIED); previously verified R270 reset certificate (REUSE_APPLIED and rechecked). Native Enterprise Math ControlPacket.from_edges / then / EffectHistogram NOT EXECUTED; formal six-slot effect does NOT validate native P000-X6 dynamics. No experimental physics claim, no formal Lean checker and no independent Driver approval.

**Next smallest unsolved unit:** either produce an actual 6-control exact all-depth positive affine BRC with legal time/effect-conditioned decoder for the whole H_n, or prove its impossibility under an exact transition/decoder contract. Separately quantify the online memory/program complexity of implementing the majority readout (2) without an unbounded lookup, and establish the R193 native source/time-port and P000-X6 correspondence. Neither the 6-vs-7 exact question nor native acceptance is resolved by this approximation theorem.

Research status: author-side mathematical proof with finite exact executable checks; no active owner/CLAIM verified for this turn, no canonical Result or independent Driver review.