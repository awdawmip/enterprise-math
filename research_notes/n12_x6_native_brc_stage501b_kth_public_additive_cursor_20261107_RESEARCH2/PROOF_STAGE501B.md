# Stage501-B — k-th-public deletion: additive provenance cursor theorem

Date: 2026-11-07. Scope: signed native X6 path histories with source-tagged tokens; AUTHOR_PROOF / EXACT_INTEGER_TESTED / INDEPENDENT_REVIEW_PENDING.

## Scientific provenance and exact model

Frozen science inputs: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Stage500-B predecessor commit `452c6a63332f91f34f4a1625a93448606d99170c`; its F-monoid and previous rightmost-one theorem are reused. The current normative context was read independently; these science pins are preserved.

A nonempty token word w has symbols (d,src), where d is one of 12 signed native X6 directions ±e_i, i=1,...,6, and src is O (original) or P (public). The observer F(w)=(D(w),E(w)) comprises six signed displacement integers and 144 directed pair counts E_ab. Tags are not directly observed. As in Stage500, F(empty) is the concatenation identity and F(uv)=F(u)⊙F(v), including the one new boundary edge [last(u),first(v)]; F of a nonempty segment recovers its length and both endpoint directions.

A legal action preserves nonemptiness. Commands: POP deletes the last token; SET3C changes the third-last direction to C preserving its tag; INSERT2C inserts a public C before the last two tokens (uncapped, or capped by n<8); DELETE2 removes the second-last token; DELETE_K deletes the kth P-tagged token from the right of the entire word, for a *fixed integer k≥2*. Define x~_h y to mean matching legality and all F prefix observations for every action trace of length ≤h.

## Theorem 501.1: additive k+h−1 provenance cursor

Fix k≥2, h≥1, L=h+3 and R=k+h−1. Split w=c t where c is a nonempty core and t is the fully tagged length-L suffix. Mark the rightmost r=min(R,#P(c)) public tokens of c: p_1,...,p_r, in left-to-right order. Uniquely write

    c=A p_1 B_1 p_2 B_2 ... p_r B_r

where B_i are O-only runs (possibly empty). A is allowed to contain hidden P only when #P(c)>R. Define

    K_{h,k}(w)=(F(A), ((dir(p_i),F(B_i)))_{i=1}^r, t).

For all nonempty-core words x,y, equality K_{h,k}(x)=K_{h,k}(y) implies x~_h y, for both versions of INSERT2C. Its streaming construction costs O(n) operations for n tokens and retains at most R+1 F summaries, R marked directions and L fully tagged directions. With 150 integer fields in each F and fixed alphabet its bit-storage bound is O((k+h)log(n+1)+k+h).

**Proof.** After j<h steps maintain the same kind of representation with a mutable explicit suffix t_j and a summarized untouched core. Every operation shrinks t_j by at most one, so |t_j|≥h+3−j≥4 at the moment the next command is applied. POP, SET3C, INSERT2C and DELETE2 therefore act only on the explicit suffix; all updates and legality, including the capped insertion total-length test, are exactly computable. DELETE_K first counts q public tokens in t_j. For q≥k its target is in t_j. Otherwise it targets the (k−q)th public marker from the right of the core, an index not exceeding k.

If A originally contains hidden public markers, the cursor initially retained exactly R markers. In the j preceding operations at most j of these core markers could have been deleted: only DELETE_K reaches the core and each operation deletes at most one. Thus at least R−j≥k retained core markers remain. Every possible core target is among those retained. If A contains no hidden public markers, the cursor contains *all* core P markers, so legal absence and the target are computable. Removing a retained P merges adjacent O-only run summaries by ⊙ and includes the exposed boundary edge. A subsequent visible suffix action likewise updates exact F. Hence the cursor determines all legality/observations and the next cursor until depth h; induction on trace length proves the claim. □

**Rank-transport interpretation.** Repeated DELETE_K, with no suffix P markers, removes the initial kth, (k+1)th, ..., (k+h−1)th public tokens from the right, not h disjoint blocks of k. Public insertions into the suffix increase q and reduce the immediate core rank k−q, already covered by the bound. Thus k+h−1 is smaller than kh for k,h>1.

## Proposition 501.2: sharpness of marker count for this representation

Let U=A A_P B A and V=A B_P A A, with just the second gadget token tagged P. They have F(U)=F(V): displacement 3A+B, directed edge multiset {AA,AB,BA}, same endpoints A. Write R=k+h−1. Form X=U (C_P)^(R−1) (C_O)^(h+3) and Y=V (C_P)^(R−1) (C_O)^(h+3). When the cursor retains only R−1 rightmost core public markers, the hidden prefixes have equal F; therefore the resulting shorter cursors coincide.

Apply DELETE_K h times. The first h−1 steps remove identical trailing C_P tokens and retain matching F. The hth removes the gadget's second public token, leaving gadget paths ABA versus AAA. Their F now differ. So R−1 markers fail for horizon h, and **R=k+h−1 is worst-case sharp within the stated last-markers-plus-F representation.** No claim is made about a globally smallest alternative encoder. The witness works for every integer k≥2,h≥1, including both insertion policies because it uses no insertion.

## Exact computation and independent scope

Executable lossless source: `REPRO_STAGE501B_PUBLIC.py.gz.b64` (deterministic gzip/base64). Decode with:
```sh
python3 -c 'import base64,gzip,pathlib; p=pathlib.Path("REPRO_STAGE501B_PUBLIC.py.gz.b64"); pathlib.Path("REPRO_STAGE501B_PUBLIC.py").write_bytes(gzip.decompress(base64.b64decode(p.read_text())))'
python3 REPRO_STAGE501B_PUBLIC.py
```
Decoded source SHA256: `c6aa1bf1b2b37e64d9eb3f848a9de967064294492edf8e06f9bc4af461e51ddb`. Actual executed stdout is saved as `REPRO_STAGE501B_PUBLIC_EXECUTED.json`: 40 explicit sharpness traces (k=2..5, h=1..5, capped/uncapped INSERT), 2,560 full-operation-tree equal-cursor family comparisons, 96,875 enumerated tagged words of lengths 5..7 from five listed types {A_O,B_O,C_O,C_P,A_P} and 10,000 duplicate-cursor comparisons in the valid h=1,2;k=2,3 domains. Every assertion passed. Finite tests are implementation checks; the unbounded 12-direction statement follows from the proof.

BRC source relation: ordered native steps and source provenance remain typed, the F observer retains all directed adjacency counts, and the cursor is an exact future-operation-bounded quotient rather than a complete-state or physical-time claim.

## Next question

Stage502-B: allow an adaptive selector DELETE_K(k) for k in a finite set S. Test the conservative max(S)+h−1 bound and seek sharper conditional cursor sizes that account for visible suffix public markers and consumed depths. A separate priority remains all-144-active-edge Euler–BRC identical-input direct-recount versus one-solve ranking costs, including full big-integer bit/time/memory/output accounting. Native task/Result/Driver dispositions remain subject to actual authenticated source authority.