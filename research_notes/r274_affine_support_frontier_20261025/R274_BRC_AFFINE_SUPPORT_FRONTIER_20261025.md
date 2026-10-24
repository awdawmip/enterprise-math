# R274 — Exact affine-support frontier and eight provenance-isolating fibers

Date: 2026-10-25. Status: AUTHOR MATHEMATICAL DERIVATION / EXACT FINITE CHECK / NOT FORMALLY ADMITTED.

## Source and declared mathematical model

Pinned GLOBAL_KNOWLEDGE_V1 canonical main: 70f6a475782287ea2e2cbfa90088febb820fbfb7. Enterprise Math Source: 220ee1ba360f21152912d0b4c1abdf867a1e4496. Original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched its startup projection; P000 remains ACTIVE_LOCKED. Reuses the R273 positive formal BRC at ff4b4e36a2cef19745ccad3f20700ebca7049c0a. This auxiliary six-slot affine action has not been shown to implement native P000 X6 dynamics; formal step count n is not calibrated heartbeat time. R193 source/time-port correspondence remains pending.

Each bit a=0 or a=1 at control state q selects a unit-positive-weight edge (next q, eta, b):

| q | a=0 | a=1 |
|---|---|---|
|0|(2,-1,-1)|(2,+1,-1)|
|1|(0,-1,-1)|(0,+1,-1)|
|2|(1,+1,+1)|(2,+1,-1)|

The chronological affine update is (eps,k) → (eta eps, eta k+b). It formally acts on six slots by (z1,z2,z3,z4,z5,z6) → (eps z1+k,eps z2,z3,z4,z5,z6). The ordered-path provenance monitor has r=0 if 00 has not appeared and the last bit is 1 (or start), r=1 if 00 has not appeared and the last bit is 0, r=2 once 00 has appeared. For inputs 0,1 its transitions are respectively r0→(1,0), r1→(2,0), r2→(2,2). Initial state (q,r,eps,k)=(0,0,+1,0). Let P_n be the exact integer word-multiplicity of each full state. Define A_n(q,eps,k)=P_n(q,0,eps,k)+P_n(q,1,eps,k) and B_n(q,eps,k)=P_n(q,2,eps,k). The terminal observer retains q, eps, k and the yes/no query “has 00 appeared?”. A no-hit-isolating fiber has A>0 and B=0.

## Theorem 1: closed-form support of the entire exact BRC

For every integer n≥10, exactly the following seven (q,r) carriers are reachable, and for each eps=±1 the support of k is the *full* step-two progression
I_n(q,r) = {−n+u, −n+u+2, ..., n+v}:

| (q,r) | u | v |
|---|---:|---:|
|(0,0)|2|−8|
|(0,2)|4|−4|
|(1,1)|2|−6|
|(1,2)|4|−4|
|(2,0)|0|−6|
|(2,1)|8|−4|
|(2,2)|2|−6|

Proof. At n=10 the positive integer recurrence from the stated initial state gives exactly these 14 sign-specific support progressions. Exhaustive enumeration of all 1,024 ten-bit words independently checks this finite base. For induction, one input interval [−n+u,n+v]_2 maps under edge (eta,b) to [−n+u+b,n+v+b]_2 when eta=+1, or [−n−v+b,n−u+b]_2 when eta=−1. Since both input effect signs have equal support, the image support for either output sign is the same union of these parity progressions.

For each target (q,r), the incoming image-offset pairs [L,R] encode intervals [−n+L,n+R]_2 at depth n+1:

| target | incoming offsets | required [u−1,v+1] |
|---|---|---|
|(0,0)|[1,−7]|[1,−7]|
|(0,2)|[5,−3]; [3,−5]; [3,−5]|[3,−3]|
|(1,1)|[1,−5]|[1,−5]|
|(1,2)|[9,−3]; [3,−5]|[3,−3]|
|(2,0)|[1,−9]; [−1,−7]; [7,−5]|[−1,−5]|
|(2,1)|[7,−3]|[7,−3]|
|(2,2)|[3,−5]; [3,−5]; [1,−7]|[1,−5]|

The leftmost and rightmost endpoint offsets agree with the required target offsets for all seven rows. The union of the incoming step-two intervals is gapless at n=10, verified directly from this explicit finite table. Each interval expands by one unit at each end when n rises by one; the parity lattice shifts consistently, so any overlap or adjacency at n=10 persists for all n>10. No other target carrier is reachable by the edge table. Thus the union equals I_(n+1) for every target and output sign, proving the statement by induction, not by extrapolation of a finite test. QED.

## Theorem 2: eight and only eight pure no-hit fibers, all depths

For each integer n≥5 there are precisely eight triples (q,eps,k) with A_n>0, B_n=0. For either eps=−1 or +1 the four (q,k) pairs are:

(0, 2−n), (1, 2−n), (2, −n), (2, n−4).

Each of these eight fibers has A_n=1 and B_n=0.

Proof. For n≥10, subtract hit support from no-hit support at fixed q,eps using Theorem 1. At q=0 the only no-hit state is r=0, whose support begins one step-two point below the r=2 hit support, hence the only pure fiber has k=2−n. The same holds at q=1, with r=1 no-hit. At q=2 the no-hit union of r=0 and r=1 extends outside the r=2 hit support at exactly k=−n (left) and k=n−4 (right). This classifies the complete support difference, not only selected examples.

At n=10 the exact word recurrence gives unit count to the following full-state boundary entries for each eps: (0,0,eps,2−n), (1,1,eps,2−n), (2,0,eps,−n), (2,1,eps,n−4). Their only possible incoming edges when advancing from n to n+1 are respectively: (1,1)→(0,0) on bit 1 (low→low); (2,0)→(1,1) on bit 0 (low→low); (2,0)→(2,0) on bit 1 (low→low); (0,0)→(2,1) on bit 0 with eta=−1 (low→high). The other incoming source intervals miss these endpoints. All edge weights equal one. Therefore these unit boundary masses persist by induction. Exact enumeration at the finite depths 5,6,7,8,9 supplies the remaining base cases. QED.

## Corollary: a time-only decoder is never exactly optimal at late finite depths

R273 already proved the majority-decoder formula M_n=Σ_(q,eps,k) min(A_n,B_n) and the total no-hit mass Σ A_n=F_(n+2), with F_0=0,F_1=1. For n≥4 the time-only classifier says “hit” for every word and therefore errs on exactly F_(n+2) ordered words. Theorem 2 shows eight disjoint, exactly one-word effect fibers on which a corrected effect-aware decoder can output “no-hit” without introducing any error. Consequently for every n≥5:

M_n ≤ F_(n+2)−8, and TV_n^* ≤ [F_(n+2)−8]/2^n < F_(n+2)/2^n.

This rigorously separates asymptotically vanishing relative error from exact finite-depth optimality. Eight is a conservative improvement; additional mixed-fiber majorities may increase the gain. This DOES NOT settle the distinct open problem whether a legal exact positive aggregate BRC with six controls exists.

## Reuse, executable evidence, limits, next unit

The companion Python verifier uses only integer arithmetic. It tests the symbolic interval-image closure relation; enumerates all 8,191 words of lengths 0..12; propagates exact BRC weights through n=128; checks all 14 support sets at each n=10..128, all eight pure fibers at n=5..128, and all eight full-state boundary unit counts at n=10..128. Result PASS. These computations validate the finite base and implementations; the induction supplies the infinite-depth argument.

BRC reuse: exact positive path histogram and affine THEN rule (REUSE_APPLIED); reduction keeps q, eps, k, source monitor and ordered-word mass. Scope is a formal declared observer, not a native six-dimensional spatial-propagation or physical-time theorem. Native ControlPacket.from_edges/then/EffectHistogram, true R193 provenance/ports, formal checker, service-issued CLAIM and independent Driver review were not executed or obtained. Paper/verification are author-side evidence, not official Result acceptance.

Next mathematical unit: exploit the seven closed support frontiers to derive endpoint-transition consistency obligations for any six-control positive aggregate BRC with time/effect-conditioned decoding. Either exhibit a lawful exact six-control representation for the entire joint output/effect histogram or prove an explicit no-go with its representation class. Separately validate the true R193 observer and native P000 X6 transfer without assuming it.
