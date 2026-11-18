# EC49FAN — H5-or-H6-rooted nine-window signed-X6/BRC optimum

**2026-11-04.** Author analytic finite proof + executed exact integer census; portable research draft, **not independently reviewed/admitted**.

## Parent, pinned model and result

Continue EC49FAM at immutable author checkpoint `68e01832937215505a692bac5ea0a3c45955c606`. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Behavioral rules follow current normative context, not the science pin. P000/ACTIVE worldview are untouched.

Keep every H2–H7 selected word in each of four EC49FAB schedules (source ranks **1512, 1513, 2200, 2203**), hence precisely 72 distinct nonempty native signed-X6 primitive prefixes, four full positive six-coordinate BRC cache keys and six observation signatures. For each of H8 and H9 independently, allow a word to descend from **any selected H5 or H6 word**, with arbitrary ordered zero-net suffix of the required operation length; do not require descent from H7 or even the same prior root. Retain the seven original signed six-axis operation codes, exact 9-start/5-bucket observation DFA, one complete key per horizon, total five keys, global at most six signatures, and rational observation rank nine at every horizon.

**Theorem (exact four-family optimum):**

\[
\boxed{E^*_{\mathrm{fixed}\ H2\ldots H7,\ H5\lor H6\mathrm{-rooted}\ H8,H9}=94}
\]

for each of the four fixed early schedules. This is a strict extension of EC49FAL's H6-only rooted theorem. The unrestricted mother problem retains its author-side range `80 <= E*_H9 <= 94`.

## Exact finite proof

For original primitive code `a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`, enumerate *all* 7^m ordered suffixes and retain exactly those with signed displacement zero in **all six axes**. For suffix lengths m=2,3,4, the resulting complete counts are **18, 88, 454**. Concatenation to any fixed H5/H6 selected root preserves endpoint displacement `(2,0,0,0,0,0)`. Filter words by the six original nine-history observation signatures; any new signature would violate the global six-signature ceiling.

Compute every candidate's complete six-coordinate positive BRC key. For each horizon/key, the rank of the matrix formed by all eligible words is an upper bound for rank achievable by any subset. The exact census yields the following **rank-nine key counts**:

| Fixed rank | H8 keys | H9 keys | Old keys with rank nine | Common eligible *new* keys |
|---|---:|---:|---:|---:|
| 1512 | 13 | 22 | 0 | 7 |
| 1513 | 13 | 22 | 0 | 7 |
| 2200 | 17 | 28 | 0 | 13 |
| 2203 | 17 | 28 | 0 | 13 |

Thus both new horizons must use **the same fifth full key**. There are precisely 40 candidate key classes across four fixed cases (7+7+13+13), enumerated in `EXACT_CERTIFICATE_EC49FAN.json`.

For each such class K, let P0 be the fixed 72-edge native prefix set, W8(K)/W9(K) the *complete* eligible word pools, and `Pref(W)` all distinct nonempty **signed primitive-step** prefixes. Set

\[
d_8(K)=\min_{A\subseteq W_8(K),\ \mathrm{rank}(A)=9}
     |\mathrm{Pref}(A)\setminus P_0|.
\]

To obtain a rigorous, optimistic lower bound for additional H9 edges, allow H9 to reuse **every prefix from every eligible H8 word for free**, even if that H8 word was not selected:

\[
d_9^+(K)=\min_{B\subseteq W_9(K),\ \mathrm{rank}(B)=9}
 |\mathrm{Pref}(B)\setminus(P_0\cup\mathrm{Pref}(W_8(K)))|.
\]

For any actual H8 choice A, `Pref(A) ⊆ Pref(W8(K))`, hence the exact total cost satisfies

\[
\boxed{E\ge72+d_8(K)+d_9^+(K).}
\]

The executable verifier computes both minima **exactly** using a signed-primitive prefix trie. At each trie node, dynamic-programming state `mask` records which of the six inherited observation signatures are represented by selected terminal words beneath the node. Sibling states combine by bitwise OR with additive cost; charge one for a nonempty prefix absent from the free-prefix set whenever its subtree contributes a nonzero mask. Rank-nine masks are precomputed exactly. This exhausts all terminal selections without enumerating exponential word subsets.

Each observation matrix is nine rows with 0/1 entries and five output buckets per selected word. A nonzero 9×9 integer minor has absolute determinant at most `3^9=19683` by Hadamard's bound, less than prime `1000003`. Therefore a rank-nine result over this finite field is **equivalent** to rank nine over Q; the code uses only exact integer modular elimination.

All 40 key-class lower bounds are **at least 94**. The unique 94 lower-bound class per fixed schedule is K=(5,5,1), (7,3,1), (5,5,1), (7,3,1), respectively; the full per-class values and pool sizes are in the compact certificate. The existing verified EC49FAJ 94-edge construction (`H8 = {p+c,p+d : p∈H7}`, `H9 = {p+fg : p∈H7}`) belongs to the H5-or-H6-rooted family and achieves equality in each case. Hence 94 is the exact family optimum.

## Actual tests, provenance and verification scope

Run `python VERIFY_EC49FAN.py > EXACT_REPORT_EC49FAN.json`. The program independently checks H2–H7 signed endpoint/key/rank/72-edge invariants; complete zero-net suffix enumerations; every admissible pool; rank-nine key census; all 40 exact trie-DP lower bounds; and all four upper-bound witnesses. Executed with Python integer arithmetic: `result=PASS`. Full locally executed expanded report SHA256: `2d38a9843329010f6d524f381dfc0d0cfcbe1596d2df2c8df79c4512002b4d9a`; exact program Git blob SHA1: `9bc361de00f4a71a5c42d4490d84881512078a46`.

An independent cross-check of the rank-1512 key (5,5,1) used **all 64** signature masks with Python `Fraction` rational elimination versus modular ranks; exhaustive selection of **4095** H8 subsets and **255** H9 subsets gave the same exact minima d8=16 and d9+=6. Recovered EC49FAL's H6-only d8 values 16,20,30. Cross-check code and expanded reports also remain in the execution evidence package.

## Next discriminating question — EC49FAO

Keep the frozen six-axis operations, cache key and observer. With H2–H7 fixed, permit H8 or H9 to depart from selected roots **at H4 or earlier**; compute the same exact prefix-trie/observation lower bounds, or exhibit a complete <=93-edge witness. Alternatively change the early H2–H7 schedule in a properly identified new search branch. This theorem closes only its declared four rooted families, leaving the broader nine-window mother optimum open.

**Status:** Author-side theorem and exact finite computation; no native CLAIM/Result/independent Driver review. GitHub Source preservation is not mathematical admission.
