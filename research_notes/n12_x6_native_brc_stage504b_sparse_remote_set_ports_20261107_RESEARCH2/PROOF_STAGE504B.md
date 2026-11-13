# Stage504-B — Nonlocal SET ports and exact X6 BRC history compression

2026-11-07 · AUTHOR_PROOF / EXACT_FINITE_EXECUTED / UNREVIEWED.

Parent: Stage503-B, `31d299b69f84ca710701d418ba4631820ac7c13e`, `NEXT_TASK_PACKET_504B.md`.
Frozen scientific inputs **unchanged**: account `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, frozen P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current normative policies loaded separately. This is an exact combinatorial typed BRC relation observer, not a claimed physical heartbeat update.

## 1. Model and observer

The direction alphabet A consists of the 12 signed primitive native axes ±E1,…,±E6 of the six-dimensional X6 spatial Cell chart. The injection v:A→Z⁶ maps ±Ei to ±ei. Time is distinct, not an additional spatial axis. For a finite word w of length n, define F(w)=(n,D(w),E(w)), with D(w)=Σ_i v(w_i), and E_ab(w) counting occurrences of each of all 144 ordered adjacent pairs (a,b). Tags O/P are not observed by F; the SET-only theorem below does not query or change tags.

For every nonempty word, the first and last direction recover from F:

v(first(w))=D(w)−Σ_(a,b) E_ab(w)v(b),

v(last(w))=D(w)−Σ_(a,b) E_ab(w)v(a).

These identities hold because the target ends of all edges enumerate every direction except the first, and the source ends enumerate every direction except the last. Since v is injective, the endpoints are determined. Define the associative directed-relation BRC product F(u)⊙F(v)=F(uv) by adding n,D,E and the one cross-boundary edge [last(u),first(v)] if both segments are nonempty; empty segment is identity. This exact product is Stage496's reusable interface. No real-number, π, trigonometric or continuous propagator computation enters this study.

## 2. Theorem 504.1: exact sparse nonlocal editable-port compression

Fix n≥1, a known set of immutable absolute site identifiers S={s₁<⋯<s_k}⊆{0,…,n−1}, and allow the operation SET(i,a) only for i∈S,a∈A. The operation replaces one direction token and leaves length and tags unchanged. The same result applies to a fixed set of end-offset ranks R via s=n−1−r. The number of future SET operations may be arbitrary and adaptive, and their sites may lie arbitrarily far from either end.

Factor the word uniquely as w=g₀ a₁ g₁ a₂ … a_k g_k where a_j=w_{s_j} and each g_j is the immutable word between successive accessible sites. Define

**K_S(w)=(S; F(g₀),a₁,F(g₁),…,a_k,F(g_k)).**

**Claim:** For any x,y with K_S(x)=K_S(y), every legal finite adaptive sequence of SET operations from x and y has the same legality and the same F observation at each prefix.

**Proof:** Every SET changes one port a_j to the same requested direction in both states and cannot change any gap g_j. Initially all port directions and all gap F summaries agree. By induction, after any number of common SET operations the port directions remain equal and all gap summaries remain equal. The exact associative ⊙ product reconstructs the full F observation from the interleaved components, therefore observers match after each prefix. Valid indices are fixed by n and S, so legality also matches. QED.

A left-to-right construction processes n tokens; for fixed 12-direction alphabet, each of k+1 gap summaries holds at most 150 displacement/edge counters plus its length. At fixed k, storage is O((k+1)·150·log(n+1)+k log 12) bits; include O(k log(n+1)) if S must itself be stored. Naive full-observer recomputation takes O((k+1)·144) exact counter operations, or O(log(k+1)) summary-node products using a balanced compositional tree. Integer bit complexity depends on word length; these are counter-operation bounds.

**Nontrivial witness:** U=AABA and V=ABAA (A=+E1,B=−E1) share F. X=AABAC and Y=ABAAC with C=+E2 have equal K_{ {4} }: their four-letter gap F agrees and their last editable token is C. All future operations confined to SET(4,a) preserve equal readouts, although X≠Y.

## 3. Theorem 504.2: unrestricted remote SET exposes every direction word in one step

For n≥3, admit SET_FROM_END(r,c) for each end-offset r∈{2,…,n−1}, with at least one available c∈A. This is precisely unrestricted access to positions i∈{0,…,n−3}; F is observed before and after an operation.

**Claim:** Two length-n direction words are one-step future-equivalent if and only if they are identical. For n=0,1,2 the current F already separates all words.

**Proof:** Suppose F(x)=F(y) but x≠y. If the first n−2 tokens agreed, then the endpoint identity forces their final tokens equal, and equality of D forces their penultimate tokens equal. Thus some i≤n−3 differs. Choose r=n−1−i≥2 and perform the same SET at i to c in each word. New displacements are D(x')=D(x)−v(x_i)+v(c) and D(y')=D(y)−v(y_i)+v(c). Original D vectors are equal but v(x_i)≠v(y_i), so new D differ. This single operation distinguishes x,y. For n=1 injectivity of v handles the case; for n=2 the sole ordered edge E_ab determines both directions; n=0 has only empty word. QED.

**Information consequence:** With every provenance tag fixed O there are 12ⁿ distinct length-n words. Any deterministic exact state supporting F plus this unrestricted one-step response language must have at least 12ⁿ distinguishable states, hence requires **ceil(n·log₂12) bits** in the worst case. This applies to this observer/operation pair; fixed sparse sites admit the smaller K_S above.

**Exact 4-token witness:** x=AABA, y=ABAA share F. With C=+E2, SET_FROM_END(2,C) targets index 1. The resulting D values are (1,1,0,0,0,0) and (3,1,0,0,0,0), respectively.

## 4. Executed certificate

The archived lossless UTF-8 Python source is `REPRO_STAGE504B.py.gz.b64`: decode via `python3 -c 'import base64,gzip,pathlib;p=pathlib.Path("REPRO_STAGE504B.py.gz.b64");pathlib.Path("REPRO_STAGE504B.py").write_bytes(gzip.decompress(base64.b64decode(p.read_text())))'`; run `python3 REPRO_STAGE504B.py`. The recorded direct output is `REPRO_STAGE504B_EXECUTED.json`.

Finite exact coverage: all 1,092 histories of lengths 1..6 over {+E1,−E1,+E2}, 8,628 word/site states across deduplicated site families, 208,152 single-SET comparisons with all twelve replacement directions, 27,000 double-SET checks for n≤4, 175 associativity tests, and 280 updates in deterministic seeded tests using all twelve signed directions. One-step response signature class counts for n=1..6 are 3,9,27,81,243,729 respectively (all histories distinct). Across site-set families there are 1,002 counted unordered same-signature distinct-word pairs; families may overlap. All executable assertions passed. These are finite checker results; general statements follow the proofs above.

## 5. Frontier

Long-range access distance alone does not set the compression budget: the number/placement of mutable ports and whether those ports move determines the observer-sufficient state. This advances Stage503's bounded suffix to arbitrary remote fixed SET sites and exhibits a linear information bound for fully unrestricted sites.

Open unit for Stage505-B: combine sparse remote SET with POP, INSERT, indexed DELETE, and provenance-based ranked deletion, where site indices shift and gaps can be split; derive a typed mutable-port frontier or a shortest exact counterexample. The parallel all-144-active heterogeneous Euler–BRC exact rank/unrank full-cost benchmark remains pending (preprocessing, bit size, time, peak memory, output verification). Native Owner/CLAIM/Result and independent Driver review are separate from this author-side proof.