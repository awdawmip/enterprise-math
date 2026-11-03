# Stage406-B — sharp asymmetric sufficient history windows for one asynchronous POP and one synchronized inverse-pair CANCEL

Date: 2026-11-03, Asia/Shanghai. Parent: Stage405-B at `826638e9d94f885d46c3dbc51b24301beb41ed12`; Research2 Draft PR #1736. Status: **PORTABLE_AUTHOR_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

Scientific pins retained: Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, locked P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. P000/ACTIVE worldview unchanged. Current behavioral rules were read separately.

## Scope, question and observer

Let `D = {+E_i,-E_i:1<=i<=6}`. Histories `(P,Q)` initially have the same finite length `m`, and retain source order. The current complete observer consists of separate lengths, signed X6 endpoint displacements, **all ordered adjacent-pair histograms** `J_P,J_Q`, their endpoint-derived BRC counts and typed positive BRC masses and coordinate/triple readouts, and absolute-index coincidence `K(P,Q)=sum_{i<=min(|P|,|Q|)} 1[P_i=Q_i]`. When specified, a signed multiplicative direction-local trace uses **nonzero scalar factors**, distinct from positive mass.

Future operations are arbitrary `APP(a,b)` (one append to each source), at most one `POP_Q` (one last Q label removed), and at most one `CANCEL` (remove the final **inverse pair** in *both* sources simultaneously). Enabledness and observer after every action are visible.

The Stage403 universal bound used four paired terminal labels. The question is whether asymmetric operation permissions permit a smaller **coordinatewise** universal suffix representation.

## Theorem 406.1 — asymmetric sufficient suffix (proved, arbitrary future length)

For two initially aligned histories with identical complete current observers, equality of their last **three P labels** and last **four Q labels** is sufficient for all finite legal future traces to have identical enabledness and observations:

```
T(P,Q) = (suffix_3(P), suffix_4(Q)), with all of a shorter word kept.
```

This holds over all twelve signed native directions, at every future APP/POP_Q/CANCEL ordering, including when the original Q terminal pair or its post-POP pair is inverse.

**Proof.** In any reachable word, separate the surviving original prefix from the surviving appended suffix. Because removals occur at the end, write

```
P_t = prefix(P, m-r_P) + u
Q_t = prefix(Q, m-r_Q) + v,
0<=r_P<=2, 0<=r_Q<=3.
```

The appended strings `u,v` are determined solely by the common action trace, and therefore are identical across the two compared histories. Original-prefix removal counts are the same by induction once transition enabledness is shown equal.

For each `r_P<=2`, the initial P endpoint, full directed J, and three terminal labels determine the endpoint, J and last label of `prefix(P,m-r_P)`: subtract the final r_P direction increments and the final r_P incident adjacency edges; the first edge to remove needs the `(r_P+1)`st last symbol. Similarly the initial Q observer plus its four terminal labels recovers these data for all `r_Q<=3`. Length is known. Nonzero direction-local multiplicative traces update by division by removed nonzero factors. Endpoint-derived native BRC counts/masses remain functions of the recovered endpoint and length, not signed cancellation. Appended strings update J and endpoints using only this recovered last label.

For coincidence K, the two original retained prefixes overlap through `l=m-max(r_P,r_Q)>=m-3`. Their coincidence count on positions 1..l equals the **initial** K minus the coincidences at positions `l+1..m`, which lie among the final three original labels of *both* words and hence are known. Beyond l, any retained original letters are confined to the last three positions of P or the last two positions of Q, since `r_P<=2,r_Q<=3`; all remaining letters are in the known appended strings. Therefore all new aligned-position comparisons and K are determined and equal, including the async one-position length difference.

The last two labels of each current word, together with the POP/CANCEL budget, determine enabledness. They are determined from the reconstructed terminal original prefix and appended strings. Thus both executions permit the same next operation, reconstruct equal observers, and preserve the same decomposition data. Induction on arbitrary finite trace length proves the theorem. (When `m<4`, keeping the whole shorter word suffices.)

## Theorem 406.2 — coordinatewise sharpness (two exact counterexamples)

**P needs three, not two terminal labels.** Let `A=+E_1`, `B=-E_1`. Compare
```
(P,Q)  = (AABAB, AAAAB)
(P',Q) = (ABAAB, AAAAB).
```
P/P' have the same endpoint `E_1`, J=`{AA:1,AB:2,BA:1}`, the same terminal 2 labels `AB`, and the same direction-local products. Q is identical (hence its last four labels agree); both have `K=4`. Original terminal pairs in both sources are inverse, so one immediate `CANCEL` is legal. It leaves P prefixes `AAB` and `ABA`, whose directed J differ. Thus shortening only the P window from 3 to 2 can lose an immediately observable residual. Length five is shortest for this P-tail-2/J ambiguity over any direction alphabet.

**Q needs four, not three terminal labels.** Compare
```
(P,Q)  = (AAAAAB, AABABA)
(P,Q') = (AAAAAB, ABAABA).
```
Q/Q' have the same endpoint `2E_1`, J=`{AA:1,AB:2,BA:2}`, and last three labels `ABA`; P is identical (so its last three agree). Both have `K=3` and the same signed direction-local product. First `POP_Q` (removes final A), then `CANCEL`: P's tail `AB` and each Q's post-POP tail `AB` are inverse. The resulting Q prefixes are `AAB` versus `ABA`, with different directed J. No length <=5 admits two distinct words with identical directed J and identical terminal three labels over **any** alphabet: after fixing the final three, at most two earlier edges remain and a two-edge directed walk ending at the fixed next label is uniquely reconstructed from its edge multiset. Hence length six is minimal for this Q-tail-3 ambiguity.

These witnesses prove **coordinatewise** optimality of the uniform raw suffix lengths (3,4), not minimal bit-count on every complete-observation fiber. Stage405's smaller quotient remains valid on its own fiber.

## Exact checks, source reuse and boundaries

`REPRO_STAGE406B_COMPACT.py` actually executed with Python exact integers. It checks both complete current observers and separating traces; exhausts all four-letter words of length <=5 for Q-tail-3 uniqueness and <=4 for P-tail-2 uniqueness; separately runs all 12 signed native BRC directions with branch weights `w(+E1)=2,w(-E1)=3,w(other)=1`.

Results: `N5(E1)=1660, W5(E1)=7020; N5(3E1)=105,W5(3E1)=1040; N6(2E1)=4665,W6(2E1)=32760; N6(4E1)=156,W6(4E1)=2976`. The broader local supplemental checker (`REPRO_STAGE406B.py`) also performed 740 exact bounded transition comparisons on a nontrivial same-key pair, with 153 visited compared states through depth four over `APP` labels A/B. These are finite cross-checks; the all-directions/all-finite-futures assertion follows from the proof, not the exhaustive finite sample.

BRC: `REUSE_APPLIED` to native signed X6 endpoint branch-count recurrence; observer K, source identities, complete directed adjacency and positive mass versus signed word products kept distinct. Theorem is within the **Path-formal model** and neither a native physical evolution rule nor a promoted Foundation result.

## Next unit: Stage407-B

Build the finite *exact minimal* future-equivalence quotient on a general `(m,z_P,z_Q,J_P,J_Q,K)` fiber, using Stage404 residual-Euler counts plus the new asymmetric (3,4) terminal key. Instead of enumerating all complete source pairs, enumerate feasible terminal keys and compute a canonical finite future-test signature, or exhibit a minimal separating counterexample to any proposed coarser key. Prove the validity of any shortcut, including K alignment when Q becomes shorter, and measure bit complexity against a binary-encoded input J. Preserve the existing native admission boundary.
