# R213 — Full Green relations of the paired-event observer monoid

Date: 2026-11-16 (Asia/Shanghai). Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Frozen scientific inputs: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34; exact antecedents R200, R209–R212 at branch commit 7b00144200715420076b93b56d10a1cf807c71ab. This concerns the declared finite paired-event observer of native X6, not all physical Heartbeat/BRC state.

## Definitions

Fix m>=1 directions, k>=0 selected source tags plus neutral tag 0, and tail depth L>=1. The full paired-event alphabet A=[m]×({0}∪[k]) has size a=m(k+1). An event history w determines F(w)=(s(w),t_L(w)), where s is the partial permutation of selected tags in order of their last occurrences (oldest to newest), and t_L is the last min(L,|w|) complete direction/source event pairs. Write J=F(A*) with chronological multiplication. Let E={z∈J: |t_L(z)|=L}, the full-tail idempotent ideal of R211.

Every state x outside E corresponds to exactly one literal word x∈A^h, 0<=h<L. Write S(x) for the support of its selected source tags, and E_{>=S}={e∈E: S(e)⊇S}. Green principal ideals below refer to the entire monoid J.

## R213-A: complete principal ideal formulas for short states

For every short x∈A^h, 0<=h<L:

  xJ = {u∈A^{<L}: u has x as a prefix} ∪ E_{>=S(x)}.

  Jx = {u∈A^{<L}: u has x as a suffix} ∪ {e∈E: t_L(e) has x as a suffix}.

  JxJ = {u∈A^{<L}: u has x as a contiguous factor} ∪ E_{>=S(x)}.

For x the empty word (the identity), these are all J.

Proof. The product of x with a later word, when shorter than L, is exactly its literal concatenation and so extends x as a prefix. When the product has full tail its selected-source support includes S(x). Conversely, for every full e with S(e)⊇S(x), append a representing history for e to x. The last L paired events are those of e and its last-source order is unchanged because all tags from x already occur in e; hence x·e=e. This proves the right-ideal formula. Left multiplication preserves the literal suffix x whenever the output tail is short or full. Conversely, any reachable full e whose tail ends in x has a representing history ending in x; split that history as vx to obtain e=F(v)x. This proves the left-ideal formula. Finally, any short product yxz is a literal word containing x, while a full product's support includes S(x). Conversely each short word containing x is yxz and each e∈E_{>=S(x)} already lies in xJ. QED.

## R213-B: all Green equivalences and the J preorder

For full e∈E, R212 gives eJ=JeJ=E_{>=S(e)} and
  Je = { (p concatenated s(e), t_L(e)) : p is a partial permutation of a subset of [k]\S(e) }.

For the complete J:
1. Every Green-L and Green-H equivalence class is a singleton (L-triviality).
2. Every short state x∈A^{<L} constitutes its own Green-R and Green-J class.
3. For full e,f∈E: e R f iff e J f iff S(e)=S(f).
4. No full state is Green-equivalent to a short state. Thus Green-R and Green-J coincide as equivalence relations on the entire monoid.

Consequently the number of Green-R/Green-J classes is
  Σ_{h=0}^{L-1} a^h + 2^k,
and the number of Green-L classes is |J|.

For the Green-J preorder, short elements are ordered by reverse contiguous-factor containment; full elements by reverse inclusion of source supports. A full e lies below a short x precisely when S(e)⊇S(x). No short element lies below a full element.

Proof. All products with e∈E remain full and only union source supports; eE already realizes all E_{>=S(e)}. For short x the right and two-sided ideals have x as the unique shortest short element. Equality of two short-generated right ideals, or mutual membership in their two-sided ideals, makes each short word a prefix or factor of the other, forcing equality. Full-generated ideals have no short elements. For left ideals the same shortest-element argument applies to short states via R213-A; R212-B proves L-triviality on full states. Distinct sectors have disjoint short/full left-ideal profiles. The formula for two-sided ideals supplies the preorder. QED.

## R213-C: exact cardinalities and overlap-sensitive ideal sizes

Put N_j=Σ_{i=0}^j j!/(j-i)!, r=|S(x)|, h=|x| and n=L-h for a short x.

  |xJ| = Σ_{i=0}^{L-h-1} a^i + |E_{>=S(x)}|.

  |Jx| = Σ_{i=0}^{L-h-1} a^i
       + m^n Σ_{d=0}^{min(k-r,n)} binom(k-r,d) N_{k-r-d}
           × Σ_{j=0}^d (-1)^j binom(d,j) (r+1+d-j)^n.

The second formula classifies the n earlier events by exactly d distinct selected tags outside S(x). The inner inclusion–exclusion term counts source words using all d new tags, with the r existing tags and neutral available. For a fixed completed tail, the number of admissible full last-occurrence orders is N_{k-(r+d)}. Directions independently contribute m^n. R212-C supplies |E_{>=S(x)}|.

The short portion of JxJ is a language of words containing literal factor x, whose count depends on the self-overlap of x. Hence its size is not determined by h and r alone. Exact witness m=1,k=1,L=4: x=11 and y=10 both have length 2 and support {1}; |JxJ|=20 and |JyJ|=21. Here 1 denotes the selected source event and 0 the neutral event.

## X6 instance and BRC query interface

With m=12 signed primitive X6 directions, k=6 selected source tags, L=2, the preceding R209/R212 counts give |J|=1,407,685 and |E|=1,407,600. There are exactly 85 short singleton R/J classes plus 64 full-tail support classes, or **149 Green-R and Green-J classes**; Green-L has 1,407,685 singleton classes.

For any one-event short x with neutral tag: |xJ|=1,407,601 and |Jx|=46,957. With a selected tag: |xJ|=1,174,177 and |Jx|=11,725.

The R209/R210 optimal rank code decodes to a complete source order and last L paired events. Right-ideal membership then reduces to a short prefix comparison or a full-state source-mask superset test; left membership to suffix/source-order checks and two-sided membership to factor/support checks. With k=6 a support mask fits six bits. This exact query compression applies to the declared paired-event observer and future chronological products; physical BRC Affine effects, positive rational weights, multiplicities, signed/phase ports and other future-sensitive history retain separate typed representation.

## Validation, evidence and next problems

The accompanying standard-library Python checker independently enumerates 14 complete small finite monoids, computes all principal right/left/two-sided ideals by products, and verifies their equality to the displayed prefix/suffix/factor/support descriptions. Totals: 387 enumerated reachable states and 43,958 left/right product membership checks, plus complete two-sided ideal comparisons; all PASS. It also verifies the overlap witness and the large X6 cardinalities by exact integer formulas. The general parameter results follow from the proofs, not extrapolation from finite checks. Run the verifier directly and compare its JSON output with R213_verification.json. Independent review=NOT_REVIEWED; installed native EffectHistogram integration=NOT_EXECUTED.

Next research: build a direct R209 rank-code membership index without materializing every tail; derive exact generating functions for full two-sided factor cones; and execute the pinned native BRC EffectHistogram adapter to measure packed observer action decode/compose/serialization and the R203 cross-moment law. This publication is independent portable research, without a formal Task CLAIM or Result/Review.
