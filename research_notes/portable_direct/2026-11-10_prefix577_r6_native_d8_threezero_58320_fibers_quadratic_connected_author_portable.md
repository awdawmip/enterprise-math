# BRC-X6 original native D8: exact-three-missing-action quadratic fiber connectivity

**2026-11-10 · AUTHOR_PROVED / FINITE_EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.**

**Frozen science:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`, 96 original ports, four signed native sources `(6,7,28,29)` with `(+,-,-,+)`, six distinct labelled actions/source, 38 original nine-root joint-flow-legal deterministic policies. `C∈{0,1}^{24×38}` denotes their exactly sourced binary action-incidence matrix, one occupied action per source. The full original nine-root signed conservation is checked separately against the frozen source: `C` is a finite observer, not an invented replacement validity axiom.

## Finite theorem

For **every** `b∈Z_{≥0}^{24}` with all four source-action six-entry sums equal to **8**, lying in `col_Q(C)`, and having **exactly three zero action coordinates**, the integer nonnegative degree-eight fiber

`F_8(b) = {n∈Z_{≥0}^{38}: Cn=b, Σ_j n_j=8}`

is **nonempty and connected** by valid two-policy exchanges `e_i+e_j ↔ e_k+e_l` with `C_i+C_j=C_k+C_l`. There are **58,320** distinct qualifying rational-span target vectors, and **7,598,688** legal eight-policy multiset representations. A zero triple wholly within one source never occurs in this exact domain; triples spread over **two sources** generate **15,576** target vectors, and triples spread over **three sources** generate **42,744** targets. Exactly **228 of 2,024** unordered missing-action triples are present.

Combining this new exact stratum with the separately certified D8 all-positive, one-zero and two-zero strata (immutable commits `0e6c727d8080cf4d7c315be88b52a386167c2ae0`, `fbf2c9f5c3e3408c4d324e7add7dc632c77ce7b4`, `73b8f361ca172fbdf042692bec91fd4adcffb3dd`) gives **nonempty quadratic fiber connectivity for all degree-eight rational-span integer targets with at least 21 of 24 action coordinates positive**: precisely **81,841 distinct target fibers and 14,346,052 multiset representations**.

## Exhaustive finite proof and independent arithmetic checks

1. Enumerate all weakly increasing degree-eight tuples over the original 38 legal policies. A partial tuple with `r` unused slots and `m_s` unseen native action labels/source cannot finish with fewer than `Σ_s max(m_s-r,0)` missing labels. Prune only when this exceeds three. This exact safe recursion visits **124,831,125** nodes, prunes **87,547,180**, and retains **7,598,688** tuples with exactly three missing labels; each has one unique unordered missing-label triple.
2. The 741 unordered two-policy choices fall into 605 exact 24-action-count classes. Enumerate **every** alternative in a class for **every** unordered choice of two positions in every retained tuple. Every neighbor is checked by lossless combinatorial rank against the same missing-label triple's complete state set. Exactly **86,015,856 directed exchange occurrences**, **7,540,368 successful DSU unions** and **58,320 components** occur. Full exact 24-action-count integer targets number 58,320; no target is split across two DSU roots. Thus all represented fibers are connected.
3. Independently compute exact `rank_Q(C)=13`, with 11 rational left-nullspace relations. For each one of `binom(24,3)=2024` missing-label triples, enumerate the positive six-action source compositions of eight with those labels set to zero. Count four-source zero-nullspace-signature combinations by 2+2 integer meet-in-the-middle. This enumerates the **entire rational-column-span target population**, independently of the DSU: **58,320** targets, broken down **0 / 15,576 / 42,744** across one/two/three missing-label source counts. Equality with the DSU target census proves nonempty fibers for every rational-span target in the theorem.
4. A third exact C++ checker independently computes the support-mask occupancy distribution of degree-eight multisets using 24-bit subset zeta/Möbius inversion of `binom(k(T)+7,8)`. The exactly-three-missing stratum is independently **7,598,688** states, agreeing with the graph enumeration. Predecessor strata zero/one/two missing also match 465,292 / 794,256 / 5,487,816 states.
5. A fourth checker reconstructs the 38 native policies by exact 96-port signed joint-flow conservation at all nine frozen roots, proving the list matches the graph and independent span counters in lexicographic order.

Companion **11-file exact executable local bundle**: `BRC_X6_NATIVE_D8_EXACT_THREEZERO_QUADRATIC_AUTHOR_PORTABLE_20261110.zip`, SHA-256 `8d5daf536b24860f81bedfc1ae603267680c22ed9698d4b6426492e38f00a2fc`. Contains complete C++ exhaustive DSU checker, independent 24-bit subset transform, SymPy exact rational-span checker, original frozen native 96-port module and nine-root policy-rebuild verifier, terminal logs, detailed theorem and SHA manifest. The graph run ends `CERTIFICATE_STATUS=PASS_DEGREE8_EXACT_THREE_ZERO_FIBER_CONNECTIVITY`.

**Next minimal scientific unit:** classify all degree-eight targets with exactly **four** missing labelled actions under the same native 38-policy frozen source, and check for split integer fibers via complete support-mask DSU and independent span census. Native D25/LIFT/JT2 ownership and the UR V2 exact original bundle/writer recovery stay distinct; no native Source Task CLAIM/checkpoint/Result or mathematical admission is asserted by this author evidence.
