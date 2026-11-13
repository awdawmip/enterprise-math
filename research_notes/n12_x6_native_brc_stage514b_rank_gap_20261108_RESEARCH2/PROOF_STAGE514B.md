# Stage514-B — sharp rank-gap threshold for arbitrary source-rank query sets

Date: 2026-11-08 Asia/Shanghai. Status: author-side mathematical proof plus executed finite exact tests; independent Driver review pending; Native Result not asserted.

## Frozen science and exact model
Scientific inputs unchanged: GK bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Predecessors: Stage512-B exact D_h structural quotient at 4657873f539da8f64efa2ca4454f4eb70f2a51d6 and Stage513-B rank-one-assisted cap at c73fdf95252901c9981f0ff3ee4184d2907ee799.

Native X6 has 12 signed spatial directions ±E1,...,±E6. Original tokens retain distinct identities, directions and P/O source tags. A history's full BRC F contains length, exact signed Z^6 displacement, all 144 ordered-direction adjacency counts, and the first/last direction; concatenation is associative and adds exactly one junction adjacency. Legal operations: POP last; DELETE2 third-from-last; INSERT2(a) new P before last two; SET_END(r,a) for r in finite R; DELETE_KTH_PUBLIC(k) for k in nonempty finite S. Directions do not influence action legality or target. Horizon h finite. D_h is the exact set of original identities that can be directly SET or deleted in some legal <=h future, with targets selected at a pre-action depth <h. Every D_h original and every inserted token remains explicit; maximal other original runs are opaque gaps g containing complete F(g) and a source count c(g). Exact total P count is not directly observed.

## Theorem 514.1 — exact sufficient cap for any finite S

Write S={s_1<...<s_t}, s_0=0, K=s_t, and define
    T(S)=max_{1<=j<=t}(s_j-s_(j-1)-1).
For every original history, h>=0 and finite R, retaining
    c(g)=min(T(S), #P(g))
in each D_h-safe opaque gap and complete F(g) is sufficient for exact legality and complete native F after EVERY legal future prefix of length <=h. In particular S={1,2,...,K} gives T=0 (no P-count metadata per hidden gap).

Proof: By definition of D_h, no original within an opaque gap can be directly SET or removed within the horizon. INSERT2 cannot split such a gap: for n>=3 its left insertion neighbour is the third-from-last original, a legitimate DELETE2 target at the same reachable pre-action state, hence necessarily explicit; at n=2 insertion is at the word start. Ordinary exposed edits preserve hidden intervals except harmless merging, with F joining exactly and saturated counts composing via min(T,p+q)=min(T,min(T,p)+min(T,q)).

Take any opaque gap g with true P population p>T in any reachable pre-action state, and let m be the number of P tokens strictly to its right. Assume m<K. Let s_j be the smallest rank in S strictly greater than m. Then s_(j-1)<=m<s_j, and its residual rank r=s_j-m satisfies 1<=r<=s_j-s_(j-1)<=T+1<=p. A legal DELETE_KTH_PUBLIC(s_j) would therefore remove an original P from hidden g, contradicting D_h. Thus all hidden gaps with p>T have m>=K. Every available rank k<=K is already satisfied to their right.

To establish correctness of the compressed rank router, select the RIGHTMOST truncated gap with p>T. All gaps strictly to its right have P counts <=T and hence are stored exactly; exposed tokens are exact. Therefore the compressed right-suffix rank count equals true m>=K and the router never visits that truncated gap. Inductively the same holds for earlier truncated gaps. Every gap crossed by any permitted source-rank query has exact stored count, and every selectable original is explicit. This agrees on target AND illegality for all queries. Every structural operation and BRC F update are exact; induction over the finite future completes the proof. QED.

This is a D_h-safe codec theorem, not a generic saturated rank search theorem. Its bit budget for a hidden gap of length l is ceil(log2(min(l,T)+1)) source-count bits, excluding F itself and the full D_h preprocessing cost.

## Theorem 514.2 — uniform cap sharpness in this representation class

Let d=max_j(s_j-s_(j-1))=T+1. If d=1, T=0 is trivially minimal. If d>=2, histories exist at horizon h=1 with the same D_1 explicit mask, identical exposed token bytes and identical F(g) for every hidden gap, which become identical when the cap is changed to T-1=d-2, but a legal source-rank deletion yields different signed displacement (and directed adjacency). Thus T is the smallest NONNEGATIVE UNIFORM threshold sufficient for all allowed histories in this stated codec; no global information-theoretic minimality for arbitrary encodings is claimed.

Construction: fix j attaining d, m=s_(j-1), g=max(4,d), n=2+g+5+m. Start with two distinct, public native prefix directions (+E1,+E2), add g identical +E3 directions, then five O-tagged and m P-tagged suffix directions. History a makes d-2 middle tokens public; history b makes d-1 middle tokens public. All native directions and original identities otherwise coincide. Choose R to allow SET on the two prefix originals and EVERY suffix original but none of the g middle originals. POP and DELETE2 only touch suffix. Since there is no allowed rank between m and m+d=s_j, any source-rank deletion either removes suffix P, targets one of the explicitly preserved prefix P directions, or is illegal; no hidden original is touched. Therefore D_1 is identical and excludes the gap in both histories. Both F(g) are identical; under cap d-2 the middle counts d-2 and d-1 collide. However rank s_j=m+d deletes +E1 from a and +E2 from b. Their signed displacement differs by (1,-1,0,0,0,0), with optional further adjacency differences. An identical compressed state cannot produce both. QED.

Corollaries: S={1,K} -> T=max(0,K-2) (Stage513-B); S={K} -> T=K-1 (Stage511-B); consecutive S={1,...,K} -> T=0. The first corollary's K=1 boundary is included.

## Exact execution
REPRO_STAGE514B.py uses Python stdlib, loads the actual Stage513-B F, join, D_h and edit implementation from sibling research_notes directory; raw observed output is STAGE514B_EXECUTED.json. Enumerated all O/P histories n=2..6, horizons 1,2 and every nonempty S subset whose maximum K=2,3,4 for fixed R={0,2,n-1}; also deterministic n=7,9,12, h=3 and diverse S. **3568 roots, 38413 pre-action states, 473961 full-vs-capped transitions, 12249 structural preprocessing-state scans**, all assertions PASS. Explicit strict lower-cap witnesses succeeded for S={3},{1,3},{1,4},{2,4},{1,2,4},{2,5},{1,3,6}. Displacement and full 144-dimensional adjacency F are recomposed at every test state. Finite coverage is exactly as declared; all-S all-h universality relies on proof, not finite counts.

## Authority, limitations and next
These are author-side mathematical arguments and exact executable evidence, not independently accepted proof or native Result. GitHub login awdawmip has admin repo permission, but the authenticated Enterprise Math native backend em_status/em_control_tasks returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE and operation_sent=false; current native owner/CLAIM and Driver review could not be checked. No protected P000, worldview or frozen scientific inputs were changed.

Stage515-B: derive GAP-SPECIFIC lower caps from the actual reachable residual rank profiles for h,R,S, while accounting for full D_h preparation cost; try a symbolic interval/rank automaton avoiding exponential structural-state enumeration. Independently continue full 12-direction/all-144-active-relation heterogeneous Euler-BRC exact rank/unrank cost benchmarking.