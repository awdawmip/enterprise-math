# EC48G — Seedless two-stage BRC memory preservation at K_hull <= 2

Date: 2026-10-27 Asia/Shanghai. Status: AUTHOR-SIDE PROVED + EXACT FINITE VERIFIED; UNREVIEWED / NOT NATIVE-ADMITTED. This is an auxiliary positive-weight source observer, not native X6 dynamics or physical calibration.

## Authority and frozen inputs

GLOBAL_KNOWLEDGE_V1 canonical main at ebbd1173a4090c6dc6f948e8a145faf22cef94a2: 00_BOOTSTRAP.md, OPERATING_MANUAL.md, P000_STARTUP.json, P000_REALITY_FOUNDATION.json (verified Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE 我眼中的世界.md, math and BRC policies. Enterprise Math current control main at cd27ceac4fafdedbd9818e458f5cef7df8a2ca03: docs/PORTABLE_RESEARCH_PROTOCOL.md, control_plane/research_delivery_policy.json, research_persistence_policy.json, activity protocol. Scientific predecessor EC48F: immutable commit 795f9beabbd4fb10c973b3bd2976acaf76064aa4. Activity RA-EMR4-20261027-0844-EC48G-AUTO11; EM-R004-EC48G-20261027-LOCAL11 is a locally assigned author identifier, NOT a native Researcher-ID or CLAIM.

## Precise model

H,Y are nonempty finite sets. Joint laws p(h,y),q(h,y) are strictly positive and separately normalized. The first observation is a provenance-bearing history h. A private randomized encoder pi_h(m) stores one of K memory states. After the second observation y a decoder outputs P with probability u_m(y) in [0,1]. No persistent public/shared seed is supplied. Thus w(h,y)=sum_m pi_h(m)u_m(y), alpha=sum_(h,y) p(h,y)w(h,y), beta=sum_(h,y) q(h,y)w(h,y). Let S_K be the attainable (alpha,beta) region, Z=sum_(h,y)[0,(p(h,y),q(h,y))] the full-history zonotope. Define K_hull=min{K:conv(S_K)=Z}, K_seed=min{K:S_K=Z}. Decisions terminate at the same second-stage depth. The prior EC48A sign-profile formula for K_hull, EC48B/C exposed-face and encoder-graph criteria, and EC48F signature-bank sufficiency are used within their stated scopes.

## Theorem EC48G.1 — all finite alphabets, positive real weights

If K_hull <= 2, then K_seed = K_hull. No restriction is imposed on the number of cross-history likelihood-ratio collisions, future observation labels or distinct unabsorbed ordered transition types D_r. For K_hull>=3 universal equality remains open.

### Lemma: only one nontrivial strict-conflict component

Fix a critical r=p(h,y)/q(h,y)>0. Set d(h,y)=p(h,y)-r q(h,y), A(h)_y=1{d(h,y)>=0}, B(h)_y=1{d(h,y)>0}. The strict-conflict graph G_r joins histories h,k if d(h,y)d(k,y)<0 for some y. If the set of distinct A history words has size <=2, G_r has at most one connected component containing an edge.

Proof: Take a strict-conflict edge h-k witnessed at coordinate y, with h positive and k negative. Hence A(h)(y)=1 and A(k)(y)=0, so the only two possible A words are A(h) and A(k). Suppose another component contains an edge u-v. Neither u nor v can have a strict sign at y, since any positive sign conflicts with k and any negative sign conflicts with h; both must tie. Thus A(u)(y)=A(v)(y)=1, forcing A(u)=A(v)=A(h) as complete words. But the edge u-v witnesses a coordinate with opposite strict signs and hence different A words. Contradiction. QED.

### Proof of theorem

For fixed critical r, just below r the full-history strictly optimal history rows are A(h); just above r they are B(h). Their distinct counts are <=K_hull by the open-threshold sign-profile formula. Assign histories with equal A words to a common decoder memory state to realize full tied q-mass Q_r, and likewise equal B words to realize tied mass 0. Each endpoint thus has a valid deterministic K-state encoding (unused states are allowed).

For a deterministic encoder f:H->{1,...,K}, strict-optimality at r holds iff no memory/observation block mixes a positive and a negative d sign. A decoder in each block is forced to 1 for positive, 0 for negative, and otherwise can vary freely through [0,1]. Thus the set of admissible decoders over a fixed valid f is a connected product of intervals. Two valid encoders differing at a single history h share a strictly optimal decoder if the union of their strict-sign masks has no conflicting signs. With that common decoder one can privately interpolate the encoder of h between its old and new memory labels continuously; all resulting strategies still maximize alpha-r beta. This is the EC48C compatible-encoder edge condition.

If K=1, the A and B endpoint encoders coincide and their decoder fiber already connects tied masses Q_r and 0. If K=2, both endpoint encoders are proper 2-colorings of G_r. By the lemma this graph has at most one edge-containing connected component; all other histories are isolated vertices. The two proper colorings of a connected bipartite component agree after a global swap of the two memory labels. Align them by that harmless label swap, and change the colors of any remaining isolated histories one at a time. Because each isolated vertex has no opposing strict sign with any other history, every single-history recoloring has a compatible common decoder. Joining these recolorings with paths inside the convex decoder fibers gives a continuous family of genuine seedless support-optimal K-state policies from tied mass Q_r to 0.

The tied q-mass is continuous, hence every value in [0,Q_r] occurs by the intermediate-value theorem. All tied generating vectors have p=rq, so their contributions trace the complete exposed face of Z. This holds for every critical r. Complementing the terminal declaration covers opposite faces; strict positivity implies every nontrivial zonotope edge comes from one of these ratios. Finally S_K is star-shaped about (0,0): multiplying every decoder output probability by t in [0,1] scales (alpha,beta) by t. Radial segments from 0 to the complete boundary cover Z. Therefore S_K=Z. Conversely S_K=Z implies conv(S_K)=Z, so K_seed>=K_hull. Equality follows. QED.

Private randomization is used only within the encoder at the currently observed history; the proof does not mix two entire policies via a persistent shared random seed. The path need not change each tied bit monotonically.

## Exact positive rational witness beyond EC48F's |D_r|<=1 condition

Raw positive arrays, h=3 and y=2:

~~~text
P_raw = [[1,1],[2,2],[2,3]], total 11.
Q_raw = [[1,1],[1,1],[1,1]], total 6.
p=P_raw/11, q=Q_raw/6.
~~~

At r=12/11 the sign rows are (-,-), (0,0), (0,+). Open-threshold sign-profile maximum K_hull=2. The nontied-signature bank C_r={(0,0)} has size 1 and distinct unabsorbed tied transitions are (11,00) and (11,01), so |D_r|=2. The direct EC48F signature-bank construction would use B_r=|C_r|+|D_r|=3 states; this is a sufficient-bank count, not a lower bound.

A two-memory construction suffices for the entire critical face. Memory decoder 0 outputs (0,0), decoder 1 outputs (u,1). History 1 uses decoder 0, history 3 uses decoder 1, and history 2 selects decoder 1 with private probability v. With u,v in [0,1], tied raw q-mass T=u+v+uv, and

alpha=(3+2T)/11, beta=(1+T)/6, alpha-(12/11)beta=1/11.

Set u=0 and let v range from 0 to 1 to realize T in [0,1]. Then set v=1 and let u range from 0 to 1 to realize T in [1,3]. This covers every T in [0,Q_r(raw)]=[0,3] with two states. Hence for this model K_seed=K_hull=2 although the earlier direct bank uses 3 states.

## Executed verification

EC48G_VERIFY.py was executed using Python standard-library Fraction and exact integer sign comparisons, with deterministic seed 202610270848. It enumerated ALL 557,685 ternary sign tables in H,Y=(3,3),(4,2),(4,3). There were 21,321 tables with profile capacity <=2; 16,316 had >=2 distinct unabsorbed tied transitions. Every eligible case had at most one edge-containing strict-conflict component and a constructed compatible-encoder path. Independently, 1,200 strictly positive nonuniform rational source models built from two ratio-prototype types yielded 5,503 exact rational critical-face reconfiguration checks, all passing. Ten exact parameter checks established the displayed rational witness identities. Structured counts and limitations are preserved in EC48G_REPORT.json. The infinite-finite statement is supported by the proof, not by extrapolation from the finite tests.

Scope: This is a positive-weight, two-stage auxiliary BRC provenance/observer theorem. It does not implement or claim native X6 trajectory arithmetic, HEARTBEAT-BRC-Shor operations, a three-dimensional-slice embedding, or variable-stopping-time preservation. No Lean formal proof, independent Driver review, Source-native Result or admission has been obtained.

## Next EC48H

Investigate K_hull=3. Classify optimal A/B 3-coloring reconfiguration of strict-conflict graphs, then apply EC48C component-interval criterion; a disconnected graph alone is not a region gap. Either prove a valid three-state reconfiguration lemma or give an exact positive rational P,Q,r, all component intervals and a missing open rational tied-mass interval. Do not repeat the proved K<=2 case.
