# Stage503-B — adaptive public rank k=1 and sharp suffix radius in native X6 BRC history compression

2026-11-07. AUTHOR_PROOF / EXACT_FINITE_EXECUTED / UNREVIEWED. Prior Stage502-B: `5d69343073b7de8628068005ef92923f4b7b254e`, `research_notes/n12_x6_native_brc_stage502b_adaptive_suffix_cursor_20261107_RESEARCH2/PROOF_STAGE502B.md`.
Frozen scientific sources unchanged: account `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; frozen P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current normative context was separately read on 2026-11-07.

## Model and BRC observer
The native alphabet comprises the twelve signed axes ±E1,...,±E6, in the six-dimensional X6 spatial model. Each history token is (direction,origin), origin O or P. The observation F(w) is the six exact signed displacement counts D plus 144 exact ordered direction-pair counts E_ab; token provenance is deliberately hidden from F. For path concatenation, F(uv)=F(u)⊙F(v) adds D and E and the one cross-boundary pair [last(u),first(v)]. Empty segments use the identity. A nonempty segment's length and end directions are recovered from F through edge counts and signed displacement. This ⊙ is associative and preserves precisely the stated relation observation.

Fix h≥1 future operations, max zero-based suffix edit radius d≥2, and finite nonempty adaptive public-deletion selector set S⊂{1,2,...}; let K=max S. Operations: POP, SET_FROM_END(2,C), SET_FROM_END(d,C), INSERT2C (public C before last two; optionally capped when current length≥8), DELETE2, and DELETE_K(k) (delete kth public-origin token from right) for k∈S; all require legal nonempty results. A future observation includes legality and F at every operation prefix up to h. All non-public-rank operations touch only suffix offsets ≤d and remove at most one token; SET preserves origin.

## Theorem 503.1 (sufficient compression with k=1 and improved suffix length)
Put L=h+d, split w=c t with nonempty core c and verbatim tagged suffix t of length L, let q=#P(t), and let
`R=max(0,K+h−1−q)`.
Retain in c its min(R,#P(c)) most recent public-origin markers with directions, the complete F of each intervening O-only run, the F of the potentially source-mixed prefix preceding these markers, and the verbatim t. Denote the signature K_{h,d}^S(w).

**Claim:** for any two histories x,y of the declared type, equality K_{h,d}^S(x)=K_{h,d}^S(y) implies equality of legality and F along *every* adaptive operation prefix of length ≤h. This includes k=1 and both INSERT2C policies.

**Proof.** After j<h operations the explicit mutable suffix has at least L−j≥d+1 tokens: a permitted non-ranked operation accesses only it, and its legality and F updates follow from its explicit tags and the associative F law. For ranked deletions let p count removed original suffix-P tokens and e count removed retained original core-P markers. Since each operation removes at most one token, p+e≤j. The current suffix contains at least q−p public markers. If R=0 then q≥K+h−1, so at every j<h the suffix has ≥q−j≥K markers: DELETE_K always stays in the suffix. If R>0 and the core has fewer than R P tokens, all are retained and the public inventory is known. Otherwise all R marked core tokens exist initially; R−e remain. If a chosen DELETE_K(k) requires core rank k−q_current>0, then
`R−e=K+h−1−q−e≥K−q+p≥k−q_current`.
Therefore the requested marker lies among those retained. Remove it and merge adjacent O-only F summaries using ⊙, updating the explicit suffix and new F exactly. This also establishes legality when hidden earlier public markers exist: R retained plus available suffix supply at least K before each of the h decisions. Induction gives matching future observation trees. QED.

An O(n) scan builds the state; at fixed 12-direction alphabet it uses O((R+1)log(n+h)+h+d) bits (F has fixed 6+144 integer counters). For d=2 the prior h+3 suffix reduces to h+2. Example h=2,d=3,S={1,3},q=0 has L=5 and R=4.

## Theorem 503.2 (two independent sharpness witnesses for this signature form)
**Marker budget.** Suppose R=K+h−1−q>0, 0≤q≤L. Choose distinct signed native directions A,B,C,D. Let U=A_O A_P B_O A_O, V=A_O B_P A_O A_O. Both have identical F (D=3A+B; E=[AA]+[AB]+[BA]). Form
`X=U (C_P)^{R−1}(D_O)^{L−q}(D_P)^q`,
`Y=V (C_P)^{R−1}(D_O)^{L−q}(D_P)^q`.
They share the signature if only R−1 core markers are retained. Set p=max(0,q−K+1), perform POP^p and then DELETE_K(K)^{h−p}. All earlier observations agree, while the hth delete removes the gadget's different P token and leaves distinguishing ABA versus AAA subsequences. This includes K=1.

**Suffix budget.** Let L'=h+d−1, U0=A_O A_O B_O A_O and V0=A_O B_O A_O A_O, and append the identical all-O suffix D^{L'} to both. The signatures with explicit suffix L' coincide for any public-marker budget (the core has no P and F(U0)=F(V0)). POP^(h−1) leaves a suffix of length d; SET_FROM_END(d,C) then touches the core's last A. The changed core histories become AABC and ABAC, with unequal edge counts; hence L' is insufficient. Thus L=h+d is worst-case sharp for this last-markers-plus-F model. QED.

Both sharpness constructions have exactly equal initial F; the differences arise under the declared future operation language, not under a different observer.

## Exact execution and coverage
The lossless Python-standard-library code is `REPRO_STAGE503B.py.gz.b64` (gzip+base64). Decode with:
`python3 -c 'import pathlib,base64,gzip; p=pathlib.Path("REPRO_STAGE503B.py.gz.b64"); pathlib.Path("REPRO_STAGE503B.py").write_bytes(gzip.decompress(base64.b64decode(p.read_text())))'`
then `python3 REPRO_STAGE503B.py`; compare with `REPRO_STAGE503B_EXECUTED.json`.

The executed code uses all 144 directed edge counters and six exact integer components. It tests h=1,2,3; d=2,3,4; S={1},{1,2},{1,3},{2,4},{1,2,4}; every q=0..L; both capped and uncapped insertion. It compared full future trees for 540 same-signature pairs (15,011 paired states), verified 342 marker-budget counterexample traces and 9 suffix-length counterexample traces, all assertions passing. Four positive native directions A,B,C,D are used for the *finite* witness checks; the theorem's alphabet is all twelve signed directions.

## Frontier
The result extends Stage502-B to public rank 1 and sharpens the explicit suffix length, including arbitrary fixed suffix edit radius d. Further research: an unbounded/adaptive edit radius, origin relabeling in the core, and the still-open same-input all-144-active heterogeneous Euler–BRC rank/unrank end-to-end cost comparison (factorial preprocessing, exact bit lengths, time and peak memory). No benchmark timings are asserted in this stage.

Research status: author-side result saved to project; native owner/CLAIM/Result and independent review depend on authenticated service access, independently of this source artifact.
