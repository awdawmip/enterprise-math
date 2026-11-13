# R734 — Sharp nine-step onset and all-length three-state BRC holonomy fibers

2026-11-12 · author-side exact result · independent review pending.
Task locator: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`.
Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\` (P000 V5; unchanged).
Derived carrier: the two 15-arc rooted CNB/V17 networks A=\`211733226574\`, B=\`5363347296468\` from R730.
Source predecessors: [R732 #2124](https://github.com/awdawmip/enterprise-math/pull/2124) and [R733 #2125](https://github.com/awdawmip/enterprise-math/pull/2125). V29 is the separately declared count-event candidate, not a primitive force law.

## Exact question

R732 gave a length-12 same-count fiber realizing all three even S3 holonomies. R733 recovered the full fifteen directed-arc counts N from the *pooled* four-port/two-PASS ledger Y and the known start/end triads. At what **first prescribed history length** must the same count/ledger fiber support three distinct named holonomies? Does the ambiguity persist at every later length?

The ten vertices are sorted 3-subsets of \`01234\`; the sixty possible arcs replace exactly one label. The selected carrier has fifteen arcs ordered as a subsequence of the global sorted 60-arc enumeration. A rooted cyclic-nonbacktracking history of length m is
\`w=(S0,...,Sm)\` with \`S0=Sm=012\`, every directed step in the carrier, and \`S_(j-1) != S_(j+1)\` cyclically, **including the closing seam**. The V17 slot rule moves the vacated original slot ID onto the entering label. Its terminal ordered frame is \`h(w)∈S3\`.

Let \`N(w)∈N^15\` count each directed arc and let the authentic pooled twelve-counter four-port readout be \`Y=C N\`, where \`C[r,i] = [r=floor(i/12)]+[r=i mod 12]\` (both PASS letters increment the same counter). For each carrier X define

\[
K_X(m)=\max_{n}\left|\{h(w): w \text{ is rooted CNB of length }m,\ N(w)=n\}\right|,
\]
with maximum over an empty collection equal to 0. Define \`K_X^{port}\` analogously using the complete twelve-counter ledger Y.

## Theorem: the exact sharp function at every length

For **each** X in {A,B},

\[
\boxed{K_X(m)=K_X^{port}(m)=
\begin{cases}
0,&m=1,2,\\
1,&3\le m\le5,\\
2,&6\le m\le8,\\
3,&m\ge9.
\end{cases}}
\]

In particular, the three-value C3 residual proved necessary and sufficient in R732/R733 is already necessary at length **9**, and at **every** subsequently prescribed length. Its length-9 onset is sharp.

### Universal upper bound

For each arc e let \`ε_e\` be the sign of its local V17 slot permutation. The sign homomorphism gives
\[
\epsilon(h(w))=\sum_e N_e(w)\epsilon_e\pmod2.
\]
Thus within a fixed N-fiber every holonomy has the **same parity**, and each of the two S3 parity classes contains precisely three elements; \`K_X(m)\le3\` for every m.

The R733 exact flow/ledger determinant (A: −2, B: +2) establishes \`ker_Q C ∩ ker_Q B_E={0}\`, hence \`(Y,S0,Sm)\` uniquely determines N for every finite directed history. Since all histories considered start/end at 012, their N- and Y-fiber partitions coincide. This proves \`K_X^{port}=K_X\` for all lengths.

### Exhaustive finite base

The attached executable verifier constructs exactly the ordered 60 arcs, applies the two fifteen-arc masks, enumerates every rooted closed nonbacktracking path up to length 11, calculates the actual transported frame, full N and pooled Y, and groups by each of these count maps. Immediate reversals are pruned; cyclic seam and endpoint are explicitly checked. Integer sign is separately checked against arc-count sign for every enumerated history.

| m | A histories | A count fibers | A K | B histories | B count fibers | B K |
|---:|---:|---:|---:|---:|---:|---:|
|1|0|0|0|0|0|0|
|2|0|0|0|0|0|0|
|3|3|3|1|3|3|1|
|4|7|7|1|7|7|1|
|5|8|8|1|8|8|1|
|6|13|10|2|14|11|2|
|7|42|19|2|43|20|2|
|8|97|41|2|97|42|2|
|9|163|60|3|169|62|3|
|10|309|82|3|329|85|3|
|11|721|115|3|751|125|3|

The number of *three-holonomy count fibers* at m=9,10,11 is respectively **(1,6,21)** for A and **(2,8,24)** for B. The accompanying JSON gives the same-count seeds for all three base lengths on both carriers, with concrete ordered paths, holonomies, complete N and pooled Y. For example, at length 9 carrier A has common N:
\`(0,1,1,0,1,0,0,1,1,0,1,0,1,2,0)\`,
common Y:
\`(7,6,1,0,1,0,0,1,1,0,1,0)\`,
and the following **three distinct** holonomies:

- \`012\`: \`012>023>013>123>012>024>034>023>123>012\`
- \`120\`: \`012>024>034>023>013>123>012>023>123>012\`
- \`201\`: \`012>023>123>012>024>034>023>013>123>012\`

Each is a seam-legal rooted nine-step CNB history with identical directed-arc multiplicities and final pooled port ledger.

### Three-step pumping lemma

Let \`P_A=(012,014,013,012)\` and \`P_B=(012,123,124,012)\`, both legal three-step rooted CNB excursions.

Carrier A has root outgoing neighbors \`{014,023,024}\`, incoming \`{013,123}\`. The last non-root vertex \`013\` of \`P_A\` is not an outgoing root neighbor; its first \`014\` is not an incoming root neighbor. For B, outgoing neighbors are \`{023,123}\`, incoming are \`{013,014,124}\`; likewise the last \`124\` is not outgoing and first \`123\` not incoming. Thus \`P_X w\` is seam-legal rooted CNB for **every** rooted CNB w, and \`P_X\` may be repeated.

If \`w_1,w_2,w_3\` have the same N and three distinct final S3 frames, then \`P_X w_i\` all have the same new N \`N(P_X)+N(w_i)\` and pooled ledger. Concatenation composes all three frames with the **same invertible** permutation \`h(P_X)\`, so the three remain distinct. Therefore

\[
K_X(m)=3 \Longrightarrow K_X(m+3)=3.
\]

The three independently certified bases at m=9,10,11 and induction in increments of 3 imply \`K_X(m)=3\` for every m≥9. Together with parity and the complete finite base m≤8, this proves the theorem. ∎

## Reproduction and scientific boundary

Run \`python3 R734_SHARP_HOLONOMY_FIBER_VERIFY.py > R734_SHARP_HOLONOMY_FIBER_RESULTS.json\`.
The checker uses Python stdlib integers/finite sets, asserts every m≤11 fiber maximum, all m=9..11 three-holonomy seeds and all prefix-pump seams, and prints \`status=PASS\`. The infinite statement follows from the parity bound and three-step pumping, not from finite extrapolation.

This is an **abstract positive BRC/V17 CNB theorem** with a fixed frozen parent science pin. Native X6 three nonzero signed-force actions, \`TRIADIC_CLOSURE_E\` incidence and an event-time/legal V29 scheduler remain the relevant next objective. GitHub file storage and author execution are distinct from Source CLAIM/Result and independent mathematical acceptance.
