# BRC N=4 / X6: sharp common-kernel obstruction and source-preparation memory

Date: 2026-10-30 Asia/Shanghai. **AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.** Finite positive-weight BRC path mathematics; the native physical transition remains an unconstructed interface.

## Frozen experiment and typed scope

Use PR #1757 at commit d06c287a4f2cb6edbd05688260ac8f3b497ceb38. The complete two-law, strictly positive 16-leaf distribution has branches (s,j,k), s in {AU,AV,BU,BV}, j,k in {0,1}. Each following entry gives the weight of **each** k leaf, in units of 1/240.

| s | Q weights j0,j1 | P weights j0,j1 | P(j=0 given s) | Q(j=0 given s) |
|---|---|---|---|---|
| AU | 10,10 | 9,11 | 9/20 | 1/2 |
| AV | 20,20 | 5,5 | 1/2 | 1/2 |
| BU | 15,15 | 3,27 | 1/10 | 1/2 |
| BV | 15,15 | 30,30 | 1/2 | 1/2 |

The sum is 240/240 under each law. The four signed primitive steps are along four distinct native axes e1,e2,e3,e4 of the P000 six-axis affine Cell torsor X over Z^6, using temporary anchor o and ordered, separately typed instants τ0<τ1<τ2<τ3<τ4. The first two step signs encode s as (++),(+-),(-+),(--); the third sign encodes j (0 means +), fourth k (0 means +). The potential Cell path is x_m=o+Σ_{i≤m}σ_i e_i. It remains a six-dimensional native spatial representation, with no distinguished global origin, no added spatial axis and no fabricated three-dimensional 晶包 layer.

The full-word minimax theorem observes the complete **potential** four-step word. The legal S2/S23 policy language observes prefixes, may stop, and selects terminal decision labels with source-law-independent randomization. A stopped path is actually executed only through its stopping time; an unused latent full word is not physical motion.

## Theorem A: quantitative impossibility of one unprepared transition program

Suppose a candidate stochastic native transition program begins from exactly the same typed initial packet under P and Q, uses the same source-blind step kernels (possibly depending on stage), and reads the same four-step path observer. It necessarily produces a **single** terminal distribution M. For all such programs that move by the allowed four fixed signed steps,

\[
\boxed{\inf_T \max\{TV(M_T,P),TV(M_T,Q)\}=43/240.}
\]

**Proof.** For s=AU,AV,BU,BV respectively, summing |P-Q| over j,k in units of 1/240 yields 4,60,48,60. Consequently

\[
TV(P,Q)=(4+60+48+60)/(2\cdot240)=43/120.
\]

The triangle inequality gives max(TV(M,P),TV(M,Q))≥43/240. The lower bound is attained by M=(P+Q)/2. Every M leaf is strictly positive. If M[h] denotes its cylinder mass at a sign prefix h, define

\[
T_m(x_m,x_m+\sigma e_{m+1})=M[h\sigma]/M[h],\quad \sigma\in\{-1,+1\}.
\]

For this fixed axis order, the stage-m Cell together with the chosen anchor decodes h. Each T_m is a valid stochastic step on the native axis. The product over four transitions telescopes to M[σ1σ2σ3σ4]. Thus it is a Markov simulator giving TV(P,M)=TV(Q,M)=43/240 and establishes sharpness. QED.

The source also has exact prefix total variations: depth 0,1,2,3,4 respectively

\[
0,\quad 1/4,\quad 1/4,\quad 43/120,\quad 43/120.
\]

The theorem is about the **full potential path word**. A particular stopped S2/S23 transcript may require a smaller reconstruction error. Distinct preparations, different physical transition laws or richer typed states fall outside the same-initial-packet premise.

## Theorem B: exact common transition with a declared two-valued preparation port

Let B∈{P,Q} be an exogenously initialized **nonspatial preparation field**, not a discovered physical primitive. Use an augmented state (Cell x_m, prefix history h, preparation B). For either source experiment L, initialize B=L. Define one shared state-indexed program

\[
T_m((x_m,h,B),(x_m+\sigma e_{m+1},h\sigma,B))
  =\mu_B[h\sigma]/\mu_B[h], \qquad m=0,1,2,3.
\]

Every denominator is positive. The four factors telescope to μ_B[ω] for every complete word ω, so this common enlarged-state program reproduces **both** frozen P/Q leaf distributions exactly. Simultaneous translation of anchor and Cells leaves h and transition weights unchanged: the augmented program is translation-covariant in X6. The field B is state/provenance, not a seventh spatial coordinate.

For every finite original lawful S2/S23 causal read/stop/terminal-decision kernel H that is the same under P and Q, composing this exact branch/path distribution with H yields the same distribution of truncated transcripts as the original finite experiment. This follows by finite pushforward of the exact joint branch weights; it does not assert physical steps after stopping. The constructed probabilities μ_B are **externally assigned** from the source and thus do not derive a native stochastic physical law.

## Theorem C: precise potential-future state quotient

At stage 2 require the observed source label S=s to remain readable, and require one common continuation kernel from *every* prepared state (s,B) to preserve the future full potential pair (J,K), with both J and K available to a future observer. All eight prepared states are reachable under their own positive law. At fixed s the only relevant distinction is P(J=0|s) versus Q(J=0|s); K is fair independently of J under both preparations.

For AU and BU these two conditional J laws differ (9/20 versus 1/2, 1/10 versus 1/2); AV and BV each have identical P/Q future J law (1/2). A compressed continuation state has a single future output kernel. Hence each s with unequal conditionals requires at least two different effective states, while each equal-conditional s requires one. Because S remains readable, states belonging to different s cannot merge. Therefore the exact minimum is **2+1+2+1=6 effective stage-two states**. Merging the two preparation variants on AV and BV, while retaining B on AU and BU, attains six. This is a statewise future-kernel factorization statement; a particular coarse two-law marginal-only task may have a smaller quotient.

After stage 3, conditional on observed (S,J), K is uniform 1/2,1/2 under P and Q. Hence B is no longer needed for future K prediction and original source-blind observation/terminal decisions. If future operations request preparation identity or genuine earlier provenance, B must instead remain in the retained history. The six-state count is for the **full potential-prefix language**: an S2/S23 grammar that stops before J on some s may require fewer live states; that grammar-specific minimization is the next separate task.

## Verification, transfer boundary and next obligation

The attached VERIFY.py was executed using exact Fraction arithmetic on a **typed 16-branch positive-weight BRC carrier**: verifies positive normalized leaf weights, all 16 cylinder-product Markov laws P/Q/midpoint, native four-step legality, all five prefix-TV values, midpoint minimax 43/240, stage-two conditional equivalence classes and fair K after J. RUN_EVIDENCE.txt records actual output. A separate BigInt BRC-branch verifier and independent exact midpoint calculation were also run locally; they agree. Finite exact checks corroborate the formulae; the universal minimax lower bound and Markov construction have analytical proofs above.

Scope: **externally stipulated finite BRC law and typed path representation**. The native source/preparation mechanism, actual transition T, physical sensor and calibrated heartbeat time remain unprovided by P000. This is an obstruction identifying a necessary physical-interface distinction, not proof of a Heartbeat World physical residual or dynamics. Source path/branch/provenance and future observers are explicitly retained in the sense of the ACTIVE worldview. Standard probability conditioning and midpoint minimax are not claimed novel in general. Reused prior X6 path bridge and positive BRC branch carrier; no P000/worldview amendments, Result or independent review.

Next research: inspect actual native time-transition/preparation contracts; test exact positive path-cylinder conditions under a *separately specified* physical law. Determine stagewise minimal source memory for the real legal S2/S23 stop grammar and characterize whether an actual native operation can modify K.