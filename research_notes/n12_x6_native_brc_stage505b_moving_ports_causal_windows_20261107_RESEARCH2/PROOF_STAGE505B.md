# Stage505-B: Finite causal windows for moving ports, POP and INSERT (native X6 / BRC)

Date: 2026-11-07. Status: AUTHOR_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED.
Parent: Stage504-B `eb89cae0fa37cb55d8d14d2184ca87b4bdb26018`, `NEXT_TASK_PACKET_505B.md`.
Frozen scientific pins unchanged: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current normative rules separately read from canonical main. The model preserves all 144 directed native-X6 adjacent-pair counters; time orders operations, not an additional spatial axis.

## Observer and exact BRC composition

Let A consist of the 12 signed native spatial directions `±E1,...,±E6`, injectively mapped to signed unit chart increments `v(a)∈Z⁶`. For a tagged direction word w, define `F(w)=(n,D,E)`: length n, exact six-coordinate displacement `D=Σv(w_i)`, and all 144 integer ordered-edge counts `E[a,b]=#{i: (w_i,w_{i+1})=(a,b)}`. The original/public tag O/P is recorded for explicitly represented tokens but is not part of F. For every nonempty word, `v(first)=D-Σ E[a,b]v(b)` and `v(last)=D-Σ E[a,b]v(a)`. Since v is injective, these endpoints are determined by F. The associative exact BRC product `F(u)⊙F(v)=F(uv)` adds D,n,E plus one cross-boundary edge `[last(u),first(v)]` for nonempty factors. Empty word is identity.

## Exact operation language

Fix a horizon h≥0 and finite sets R,J⊂N of end-relative offsets; use zero-based offset `r=0` for the last token.

* `SET_FROM_END(r,a)`: r∈R, 0≤r<n; overwrite direction at absolute position n−1−r with a∈A; keep its existing O/P tag.
* `POP`: remove last token when n>0.
* `INSERT_BEFORE_FROM_END(q,a)`: q∈J, 0≤q<n; insert a new P-tagged token immediately **before** the existing token at n−1−q (not after it).

The observer reads F after every legal operation, and legality is observed. No tag-sensitive deletion belongs to this language.

Let `Q={0}∪R∪J`. For an original length-n history w, let the original end-offset of token i be `ρ(i)=n−1−i`. Expose every original token satisfying `dist(ρ(i),Q)≤h+1`. Keep direction, tag and order of each exposed token. Summarize every maximal **unexposed** contiguous gap by its complete F=(length,D6,E144). The resulting interleaved token/gap record is `K_{R,J,h}(w)`.

**Theorem 505.1 (moving-port causal-window factorization).** For every n,h,R,J and every pair of histories x,y over the 12-direction alphabet,
`K_{R,J,h}(x)=K_{R,J,h}(y)`
implies equal legality and equal complete F observations after every common adaptive sequence of at most h legal operations from the preceding language. Every step can be simulated exactly on K using explicit tokens and immutable gap summaries.

**Proof.** Give each initial token a persistent identity. During t operations, the end-offset of any surviving initial token changes by at most t, since each INSERT changes that offset by either 0 or +1, each surviving POP by −1, and SET by 0. For an unexposed initial token with original offset ρ, we have `|ρ−q|≥h+2` for all q∈Q. Immediately before operation t+1 with t≤h−1, its current offset ρ_t obeys `|ρ_t−q|≥h+2−t≥3`. Therefore no unexposed initial token can be the target of SET at r∈R, POP at 0 or INSERT before offset q∈J. Newly inserted tokens are explicitly represented. Since an INSERT always targets an explicit token or a previously inserted one, the operation occurs between entire blocks and never splits an unexposed gap. No originally unexposed token is changed or deleted, so each gap retains its complete F summary and length throughout the horizon. Given a K record, block lengths determine total length and operation legality/target block. All valid updates modify only the explicit token list and may be represented exactly. By induction, equal K records produce equal updated records after every common legal operation. Their readouts are equal because the associative product of explicit one-token F factors and unmodified gap F factors is the exact whole-word F. QED.

**Storage and construction.** Put q=|Q|. Initial exposed offsets lie in the union of at most q integer intervals of radius h+1, hence there are at most min(n,q(2h+3)) explicit tokens and at most q+1 summary gaps. Each gap stores 151 integer counters (one length, six signed displacement, 144 relation counts), with O(log(n+1)) bits per counter. With fixed 12-direction and binary O/P tags, the state uses `O(q(h+1)+151(q+1)log(n+1)) bits`. Construction scans n tokens. Exact update/recomposition may traverse the explicit tokens and q gaps; a balanced product tree can reduce the number of compositions for a local edit. These are representation/counter-operation bounds, not a benchmarked bit-time bound.

## Theorem 505.2: an undersized window loses the relational boundary

Let all 60 tokens initially be A=+E1 except an interior four-token block at original end-offsets 9,8,7,6. Form x by substituting AABA and y by ABAA there, with B=−E1. Both share F: both blocks have the same displacement, endpoints and counts AA=AB=BA=1. Set R={5}, J=∅, h=3. A naive zero-radius representation exposes only original end-offsets 0 and 5 and replaces the intervening/rest gaps by their F summaries. The two words have equal such records. All one-step options POP and SET_FROM_END(5,a), a∈{A,B,C}, preserve equality of F. After `POP; SET_FROM_END(5,C)` with C=+E2, the new D is identically (56,1,0,0,0,0), but the 144-edge matrices differ at zero-based indices `0:55/54`, `2:0/1`, `12:0/1`, `14:1/0`. Thus the shortened cache is not 2-future-sufficient. An edit can expose a hidden *neighbor* even when the overwritten direction agrees. The theorem gives a sufficient radius; this example does not prove its minimality.

## Exact executed evidence

The source is recoverable byte-for-byte from `REPRO_STAGE505B.py.gz.b64` using `base64.b64decode` and `gzip.decompress`, then run Python 3 standard library. Exact original source SHA256: `f3e81db6b97716796fd13d48dc395f54a4dba2747d01a2a388823f0139e6e430`; gzip SHA256: `0a5e1255af53b3f04a290d2249b08e6f60718c6e7d4e713c4e9029e2cce33f3f`. Actual captured stdout: `REPRO_STAGE505B_EXECUTED.json`.

Executed assertions: 3,279 complete histories of length 1–7 on a 3-direction alphabet; 32,790 one-step operations; 32 seeded full-12-direction histories with 160 mixed steps; three distinct-history/same-K pairs at n=80,100,500 with complete operation-prefix tree checks totaling 2,330 legal transitions; 700 exact 12-direction monoid associativity checks; and the 2-step under-window relation witness. The three pair examples exposed respectively 17,21,18 explicit original tokens. All assertions passed. Universal theorem follows the proof; finite calculation checks the specific instances and implementation.

## Status and next dependency

Native Enterprise Math status/owner query on 2026-11-07 returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH` and `operation_sent=false`; the separate Site status was `CONFIGURED_NOT_LIVE_VERIFIED` and `research_authority_granted=false`. GitHub login `awdawmip` has repository admin permission, not native CLAIM/Driver authority. This remains author-side proof/exact computation, unreviewed.

Next: add indexed DELETE and rank-sensitive public-source deletion; prove a moving causal window with provenance cursor, or exhibit a minimal exact BRC counterexample. Independently benchmark Stage494 determinant recount versus Stage495 single-solve all-144-active Euler–BRC exact rank/unrank with the same heterogeneous inventory and full input/output/bit/RSS costs. See NEXT_TASK_PACKET_506B.md.
