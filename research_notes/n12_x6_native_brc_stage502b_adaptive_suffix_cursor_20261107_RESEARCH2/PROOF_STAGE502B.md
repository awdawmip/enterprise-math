# Stage502-B: Adaptive provenance deletion and a suffix-conditioned sharp cursor
Date: 2026-11-07. Classification: AUTHOR_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED. Parent Stage501-B commit `989e805170509b796bcf81b70ea8f07f3a013fa9`. Frozen science: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 original blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current normative source is read separately.

## Typed observer and action domain
Let w be a nonempty word of tokens (direction, origin), direction one of the 12 signed primitive native X6 directions and origin O or P. F(w) is six integer signed displacement components and 144 ordered adjacency counts. Origins are hidden in F but retained in the actual word. The observer is a composable BRC relation: `F(uv)=F(u)⊙F(v)` where composition adds the cross-boundary edge [last(u),first(v)]. Length and endpoint directions can be recovered from F of any nonempty word:
`|w|=1+sum_{a,b}E_ab`, `v(first)=D-sum E_ab v(b)`, `v(last)=D-sum E_ab v(a)`. The empty word supplies the composition identity.

Operations: POP (remove last); SET3C (replace third-last direction by native C and keep origin); INSERT2C (insert public C before last two, uncapped or capped at current n<8); DELETE2 (remove second-last); DELETE_K(k) (remove kth public-origin token from the right), k chosen adaptively at every step from a fixed finite nonempty S⊂{2,3,...}. Illegal actions, including removal of the last remaining token, are observed as illegal. Define x~_h y to mean equal legality and F along every common action-prefix of length at most h.

## Theorem 502.1 — sharply conditioned sufficient cursor
Fix h≥1, K=max S, L=h+3. Split w=c t into nonempty core c and fully tagged suffix t of length L. Let q=#P(t), and set
```
R=max(0,K+h-1-q).
```
Mark the rightmost r=min(R,#P(c)) public-origin core tokens p1,...,pr, in left-to-right order. Write c=A p1 B1 ... pr Br, where each Bi is O-only; A may hide older public tokens. Retain
```
K_h^S(w)=(F(A), ((direction(pi), F(Bi)))_{i=1..r}, t).
```
**Claim:** equality of these signatures implies x~_h y for all valid native X6 histories, both INSERT2C policies, and any adaptive k∈S. This retains at most R core provenance markers. If q≥K+h−1 then R=0 and the core's F alone is sufficient.

**Proof.** At step j<h, maintain the exact mutable tagged suffix of length ≥L−j≥4, and the original core's F-runs separated by retained source markers. All operations except DELETE_K target only this suffix; their legality and F updates are exact. Let p count original suffix public markers removed in j preceding operations, and d count retained original core public markers removed. We have p+d≤j, while the current suffix public count q_j≥q−p (public insertion can only raise the count, and only deletions lower it). DELETE_K(k) targets the suffix if q_j≥k, otherwise it needs the (k−q_j)th public core token from the right. If R=0, q≥K+h−1 implies q_j≥q−j≥K; no core target can occur. If R>0 and hidden core-public markers exist, exactly R original rightmost markers were retained, and at least R−d remain. For j≤h−1:
```
R−d = K+h−1−q−d ≥ K−q+p ≥ k−q_j.
```
Hence the targeted core token, if any, is retained. When no hidden public token exists, all core markers were retained and legality is known. Deleting a retained marker merges neighboring O-only run summaries by the exact associative F-boundary law, so the update and observation remain computable. Induction through all j≤h proves the claim. QED.

An O(n)-visit scan builds the cursor, retaining at most R+1 F summaries with 150 integer counters each, R directions, and h+3 tagged suffix directions. Fixed-alphabet representation uses O((R+1)log(n+h+1)+h) bits, with a fixed 150-dimensional multiplicative constant. No minimality across all possible encoders is asserted.

## Theorem 502.2 — exact worst-case marker budget for this representation
For every h≥1, finite S⊂{2,3,...}, K=max S, and suffix-public count 0≤q≤h+3 with R=K+h−1−q>0, retaining R−1 (rather than R) core markers in the last-markers-plus-F representation is insufficient.

**Proof and counterexample.** Choose distinct native directions A,B,C and the two 4-token gadgets
```
U=A_O A_P B_O A_O,      V=A_O B_P A_O A_O.
```
They have identical F: displacement 3A+B and adjacency multiset {AA,AB,BA}, with the same endpoints and exactly one public token at position 2. Let
```
X=U (C_P)^(R-1) (C_O)^(L-q) (C_P)^q,
Y=V (C_P)^(R-1) (C_O)^(L-q) (C_P)^q.
```
Their signatures retaining only R−1 core markers are identical because the differing gadget belongs to the summarized prefix and F(U)=F(V). Set p=max(0,q−K+1)≤h−1. Apply p POPs, removing only matching trailing public C tokens, and then h−p repetitions of DELETE_K(K). If q<K, the repeated deletions advance through original core ranks K−q,...,K−q+h−1=R; if q≥K, the p POPs first leave K−1 suffix public tokens, and the core deletions remove original core ranks 1,...,h−p=R. In either case, only common C tokens are removed in steps 1..h−1. The h-th step removes the gadget's P token, leaving ABA versus AAA and distinct F. Thus R is worst-case sharp for this representation. QED.

The original Stage501 unconditioned bound K+h−1 is the q=0 instance; every visible suffix public marker improves the separate core-marker budget by one until it reaches zero. Adaptive selection cannot increase the maximum rank beyond K, and the witness uses the permitted k=K.

## Exact computation, material and remaining questions
Executable Python source is saved losslessly as `REPRO_STAGE502B.py.gz.b64`. Decode:
```sh
python3 -c 'import base64,gzip,pathlib; p=pathlib.Path("REPRO_STAGE502B.py.gz.b64"); pathlib.Path("REPRO_STAGE502B.py").write_bytes(gzip.decompress(base64.b64decode(p.read_text())))'
python3 REPRO_STAGE502B.py
```
SHA256 of executed decoded source: `44bb66357d83b560a30d05de9017b68cdf01383213cb76cff1f9e76c46df70ba`. Output is `REPRO_STAGE502B_EXECUTED.json`. Standard-library exact integers, no floating-point approximations. For h=1..3, S∈{{2,3},{2,4},{3,5},{2,3,5}}, q=0..h+3 and both insertion policies, it checked 144 witness-family future responses (15,530 visited tree nodes), 63 strictly different reduced-marker traces, and 18 R=0 cases. It enumerated 109,375 tagged finite-alphabet words and checked 360 pairs sharing a cursor (2,520 nodes). All asserts passed. The finite check uses three positive directions embedded into native X6 with remaining displacement/adjacency fields zero; universal scope comes from the proof, not the finite check.

Next: Stage503-B investigate selector k=1 and an enlarged action language with an interior edit approaching the explicit suffix boundary. Separately execute identical-input full-144-edge heterogeneous Euler–BRC Stage494 determinant recount versus Stage495 one-solve exact rank/unrank with full bit, time and memory accounting. Formal native owner/CLAIM/Result/Driver acceptance is independent.
