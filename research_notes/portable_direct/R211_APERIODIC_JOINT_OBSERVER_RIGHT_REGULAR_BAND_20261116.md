# R211 — Aperiodic paired-event observer monoid and right-regular idempotent ideal

Date: 2026-11-16 Asia/Shanghai. Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

Frozen scientific pin: \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Exact antecedents: R200 finite paired observer, R209 exact Stirling cardinalities, R210 faithful reachable-action codec. Native basis: P000 signed X6 Heartbeat World, six axes and twelve signed directions. This result concerns the declared finite observer quotient only.

## Objects and chronological product

For m>=1 direction labels, k>=0 selected provenance labels plus neutral 0, and L>=1, let A=[m]×({0}∪[k]); a=m(k+1). A history w has s(w), the distinct selected provenance labels ordered by *last occurrence* oldest to newest, and t_L(w), the final min(L,|w|) **full paired events**. Write J=J_(m,k,L)={F(w)=(s(w),t_L(w)):w∈A*}.

For x=(s,t), y=(u,v), the chronological product is

    x·y = (s ⊙ u, suffix_L(t concatenated v)),
    s ⊙ u = (s with all labels in u removed) concatenated u.

This formula holds even if y is a full-tail state with an older prefix contributing to u; then |v|=L so the last L events are precisely v. Define h(x)=|t|, identity 1=((),()).

## Theorem R211-A: exact idempotents and uniform exponent

For L>=1, the subset E={x:h(x)=L} is a two-sided ideal of J and each e∈E is idempotent. The complete idempotent set is {1}∪E. Every x satisfies

    x^L = x^(L+1).

More precisely the *least* n>=1 for which x^n=x^(n+1) is

    ν(x) = 1                         if x=1 or h(x)=L,
           ceil(L/h(x))              if 1<=h(x)<L.

Consequently J is a finite aperiodic monoid (it contains no nontrivial subgroup).

**Proof.** Product tail lengths satisfy h(xy)=min(L,h(x)+h(y)), so E is an ideal. Any full-tail element e is represented by a history w of length at least L. The selected-source last-occurrence order of w^n equals s(w) for all n>=1: the final copy of w controls the order. The last L paired events of w^n equal t_L(w) for all n>=1: the final copy already supplies L events. Thus e²=e. For a nonempty short-tail element x, its unique representing history has length h<L; x^n has tail length min(L,nh). Before n=ceil(L/h), this length increases strictly at each multiplication, proving x^n≠x^(n+1). At and after that threshold, the final L events of the periodic history and the selected-source order are stable. The empty history is the identity. Since every subgroup member g obeys g^L=g^(L+1), cancellation by g^(-L) within that subgroup yields g=1_group, establishing aperiodicity. QED.

## Theorem R211-B: right-regular band structure and source fibres

The ideal E is a **right-regular band** in chronological convention:

    e²=e,          e f e = f e       (all e,f∈E).

For each fixed admissible source order s, the full-tail fibre

    E_s = { (s,t)∈E }

is a right-zero semigroup: for e,f∈E_s, e f=f. More generally E_s E_u ⊆ E_(s⊙u), and for e=(s,t), f=(u,v) in E,

    e f=(s⊙u,v).

**Proof.** The source-order monoid (partial permutations with last-occurrence update) satisfies s⊙s=s and (s⊙u)⊙s=u⊙s. The latter holds because a final copy of s controls its own labels' last occurrences, while labels only in u keep their order; both source words sus and us have exactly those last-occurrence orders. For full-tail elements, right multiplication provides the entire new tail v. Therefore ef and fe have tails v and t respectively, and efe and fe have the same source component and tail t. With equal s=u, the source component s⊙s=s, so ef=f. QED.

## Theorem R211-C: exact decomposition and six-axis counts

Let P(k,r)=k!/(k-r)!, and C(r,L)=sum_(j=0)^min(r,L) {L+1 \brace j+1} with Stirling numbers of the second kind. R209 established that for a fixed source order s of length r, |E_s|=m^L C(r,L). Hence

    |E|=m^L sum_(r=0)^k P(k,r) C(r,L),
    |Idem(J)|=1+|E|,
    |J \ Idem(J)|=sum_(h=1)^(L-1) a^h.

For the native X6 observer m=12 signed directions (not spatial dimensions), k=6 independently chosen source tags and L=2: a=84, |J|=1,407,685, |E|=1,407,600, |Idem(J)|=1,407,601, and the *only* non-idempotent states are the 84 one-event short-tail states. For each of the 720 full source orders of length six, E_s has 12²·(1+3+1)=720 states.

The L=0 boundary is the source-order monoid itself, a right-regular band with all elements idempotent. At L=1, the full J is a right-regular band (the identity adjoins E).

## BRC transport consequence and boundary

By the faithful action map in R210, every full-tail reachable *observer affine action* is idempotent and any repeated reachable observer action stabilizes after ν(x) repetitions. This permits a cached observer-side power operation without expanding R201's dense affine representation.

A BRC histogram atom also carries a physical Affine effect, an exact positive rational weight and multiplicity. Those components follow their own convolution laws. For a single weight 2/3, multiplicity 2 and identity physical action, n serial copies have weight (2/3)^n and multiplicity 2^n even when the observer action stabilizes at n=2. Thus only the finite observer-action component is collapsed. Pairwise provenance, native paths, signed phase and hidden conditional ports remain subject to their own typed observers.

## Reproduction and validation

Run \`node R211_aperiodic_band_check.mjs\`, comparing the standard-output JSON with \`R211_verification.json\`. The checker independently enumerates every J state via all words of length <=k+L, checks the R209 Stirling total, exactly classifies idempotents and shortest stabilization exponents, exhaustively verifies the right-regular identity on E×E and the right-zero source fibres, and runs bounded associativity checks. Exact BigInt arithmetic is used for cardinalities and positive rational demonstrators. Coverage: m=1..2, k=0..2, L=1..3 (18 complete finite models). The general statements follow from the proofs above, not from finite testing. Independent mathematical review=NOT_REVIEWED.

## Next executable science

Explore Green relations and exact right/left ideal cardinalities of the full-tail band to support faster compressed-action composition; implement the R210 packed action adapter against the pinned native \`EffectHistogram\` API and measure end-to-end bit/time/memory cost, retaining physical BRC effects. The pinned native module was read; no installed-package integration test is claimed in this work.

Control: independent portable research; no active Task CLAIM, native Result/Review or protected P000 mutation asserted.
