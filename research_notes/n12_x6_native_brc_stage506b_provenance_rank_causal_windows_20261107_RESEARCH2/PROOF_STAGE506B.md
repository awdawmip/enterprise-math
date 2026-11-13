# Stage506-B — Source-ranked deletion plus moving causal-window BRC compression

2026-11-07 · AUTHOR_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED.
Parent: Stage505-B `91f1b11ecbe824220b8b1b279ff11425a05844c6`. Frozen scientific inputs remain account `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current rules are separately refreshed. All twelve signed X6 native directions, all six displacement counters and all 144 ordered relation counters are retained. This is an exact discrete relational BRC observer, not a physical heartbeat model.

## Model

A word has tokens `(direction,tag)` with direction from the twelve native ±axes and provenance tag O (original) or P (public). `F(w)=(n,D6,E144)`, where E counts all directed adjacent pairs. The associative BRC interface `F(uv)=F(u)⊙F(v)` combines gap summaries using boundary endpoints recovered from F. Tags are invisible to F but operative for the source-ranked deletion.

For horizon h≥1 and finite sets R,J,T of nonnegative end-offsets and S of positive public-source ranks, operations are:
* SET_FROM_END(r,a), r∈R, overwrites direction and preserves tag.
* POP removes the last token.
* INSERT_BEFORE_FROM_END(q,a), q∈J, inserts a new P token immediately before the token currently at offset q.
* DELETE_FROM_END(d), d∈T, deletes the token at offset d.
* DELETE_KTH_PUBLIC(k), k∈S, removes the kth P-tagged token **counted from the right, one-based**, and is illegal if fewer than k public tags remain.

Every operation is legal only when its index/rank exists. Choices are adaptive. Observe F after each valid step and observe legality.

Set `Q={0}∪R∪J∪T`, `K=max(S)` when S nonempty and `M=K+h−1` (when S empty, M=0). Build K* from an original word by exposing: (a) every original token whose end offset lies at distance ≤h+1 from Q; and (b) the last `min(M, #P)` original P-tagged tokens. Keep the individual exposed directions/tags in their original order and replace every maximal contiguous unexposed interval by its **complete** F=(length,D6,E144) summary.

**Theorem 506.1 (position+source-rank finite future quotient).** If two initial histories x,y have equal K* records, every common adaptive sequence of at most h operations above has equal validity/legality and identical full F observations at every prefix. The record K* can be updated exactly using only stored exposed/new tokens and immutable gap summaries.

**Proof.** Give original tokens immutable identities. At time t after ≤h−1 steps, the current end-offset of any surviving original token differs from its initial end-offset by at most t: INSERT shifts it by 0/+1, any DELETE or surviving POP by 0/−1, SET by 0. An original token outside the exposed Q-windows originally has distance at least h+2 from each q∈Q, hence at time t it still has distance at least h+2−t≥3; it cannot be the target of any index-sensitive SET, POP, INSERT-before, or DELETE_FROM_END.

For an initial P token of one-based right rank j, its current right P-rank while it survives is at least j−t. Every original P token that was not among the last M has initial rank j>M. At time t≤h−1 its rank therefore exceeds M−t≥K and cannot be selected by `DELETE_KTH_PUBLIC(k)` for any k∈S. Newly inserted P tokens are always explicitly represented; an existing token never changes O/P tag. If a kth public exists, its rank≤K forces it to be exposed/new. Thus the ranked deletion's target and legality can be determined entirely from the explicitly represented P tokens. If the explicit P count were below k while a hidden P existed at rank k, it would contradict the rank inequality. This argument also covers the case fewer than M original P tokens exist (then all are exposed).

Consequently **no operation can touch an original unexposed token during the horizon**. No INSERT splits a hidden gap: it always inserts before an explicit target, so each hidden contiguous block preserves its complete F and length. Operation legality and indexed target are determined by explicit block lengths, and public-rank legality by explicit P count. Legal edits update only explicit tokens. Induction on prefixes preserves equal K* states; the full observer is obtained from the exact BRC product of token and gap F factors. QED.

**Size bound.** Let q=|Q|. The windows expose ≤q(2h+3) original tokens, while the ranked cursor contributes ≤M additional tokens. There are ≤q+M+1 hidden gap summaries. A gap has 151 O(log(n+1))-bit counters and each exposed O/P-tagged direction token uses O(1) bits for fixed 12-direction input. Thus a sufficient deterministic state takes `O(q(h+1)+M+151(q+M+1)log(n+1)) bits`. For fixed q,h,K this grows only logarithmically with n even when indexed ports and public tags are arbitrarily remote. This bound is sufficient, not claimed optimal.

## Executed exact evidence

The source `REPRO_STAGE506B.py.gz.b64` is lossless gzip+base64 of executed Python 3 code (standard library, exact integers), requiring the Stage505 `REPRO_STAGE505B.py` in the same directory at execution time. Source SHA256: `d38a4a303e0aa37b195f4ac52722ea532fb50b4dca7b51c92b251e6f61490dce`; gzip SHA256 `186dd02a2d191f9b597e3e25fe54efebe427b907855cf5340229b7d96ed79ce7`. Executed output saved as `REPRO_STAGE506B_EXECUTED.json`.

All 9,330 tagged histories length 1–5 over three direction letters and O/P tags were exhausted, with 121,290 single-step legality/F transition comparisons. Constructed three different-history/same-K* pairs with hidden rearranged AABA/ABAA direction blocks **and an additional hidden older P tag differing between the histories**. At lengths n=120,160,500 (h=3,3,2) every legal three-letter operation prefix was checked: 2,379+2,379+182=4,940 comparisons; only 19,18,16 original tokens respectively were individually exposed. A further 40 seeded histories with full 12-direction random provenance underwent 200 mixed operations. All exact assertions passed. The general theorem is established by induction, while finite computation checks the implementation and examples.

## Remaining research

Stage507: sharpen the M=K+h−1 source-marker budget by subtracting P tokens already included in windows, while accounting for adaptive rank deletion. Derive a precise formula or strict counterexample. Separate open Euler–BRC benchmark: same all-144-active heterogeneous edge inventory for Stage494 determinant recount and Stage495 one-solve rank/unrank, with complete input, operand bit lengths, wall time, RSS, recovery and independent reranking. Native Gateway still reports `BACKEND_IDENTITY_OR_VERSION_MISMATCH` and `operation_sent=false`; this is an author-side proof, not an authenticated Owner/CLAIM, Result or independent Driver review.
