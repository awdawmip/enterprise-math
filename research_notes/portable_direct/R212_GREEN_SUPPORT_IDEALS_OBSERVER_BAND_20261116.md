# R212 — Exact Green ideals and Boolean support lattice of the paired-observer right-regular band

Date: 2026-11-16 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Frozen science: \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`; dependencies R200, R209, R210 and R211. The scientific object is the full-tail idempotent ideal E of the selected-source/full-paired-tail quotient J_(m,k,L), not the entire physical BRC state or full native X6 history.

## Product and source supports

Use m>=1 directions, k>=0 selected source labels, one neutral provenance, and L>=1. Source last-occurrence order s is a partial permutation of [k] (oldest to newest); tail t contains L complete event pairs. For e=(s,t), f=(u,v) in E, R211 proves the chronological multiplication

    e·f = (s ⊙ u,v),
    s ⊙ u = (s without labels appearing in u) followed by u.

Let supp(e) be the *set* of selected sources in s. All full-tail elements are idempotent. Right/left/two-sided principal ideals and Green relations below are computed in the semigroup E itself (with its implicit identity adjunction for ideals).

## Theorem R212-A — Right ideals, exact R-classes and support lattice

For every e∈E with S=supp(e),

    eE = { y∈E : supp(y)⊇S }.

Consequently e and f are Green-R equivalent **iff** supp(e)=supp(f). The R-classes are in bijection with all 2^k subsets of selected-source labels. Principal right-ideal inclusion reverses subset inclusion:

    eE ⊆ fE    iff    supp(e) ⊇ supp(f).

**Proof.** For every y=e z, its source support is supp(e)∪supp(z), hence contains S. Conversely, for any y with supp(y)⊇S, all labels of s already appear in the source order u of y; appending u erases every old source label from s, so s⊙u=u. The right tail of e y is the entire tail of y. Thus e y=y, so y∈eE. Equality and inclusion of ideals now correspond exactly to source-set equality and reverse containment, with every support subset realized by a prefix followed by a fixed neutral L-tail. QED.

## Theorem R212-B — Left ideals are source-order suffix cones, L-triviality

For e=(s,t)∈E with r=|s|,

    E e = { (p concatenated s, t) : p is any partial permutation
            of a subset of [k] \ supp(e) }.

Every such member is reachable. Therefore

    |E e| = N_(k-r) = Σ_(j=0)^(k-r) (k-r)!/(k-r-j)!,

and Green-L classes are **singletons**: E is L-trivial.

**Proof.** Multiplication f e preserves the complete tail t of the right factor. Its source-order output is (u without sources of s) followed by s, so it has the specified form. Conversely, for any distinct-label prefix p disjoint from s, choose a full-tail f=(p,z^L), where z is a neutral paired event. Then f e=(p concatenated s,t). This proves the exact left ideal and count. If E e = E f, then the two source orders must both be a suffix of the other and their tails equal; hence e=f. QED.

## Theorem R212-C — Two-sided ideals and exact Green class sizes

The two-sided principal ideal satisfies E e E = eE; hence Green-J and Green-R coincide on E, while Green-H is the identity relation.

Write P(n,j)=n!/(n-j)!, C(r,L)=Σ_(j=0)^min(r,L) {L+1 \brace j+1}, where {·\brace·} is a Stirling number of the second kind. R209 gives m^L C(r,L) full tails per fixed source order of length r. Thus for S⊆[k] with r=|S|,

    |R_S| = r! m^L C(r,L),
    |eE|  = Σ_(u=r)^k binom(k-r,u-r) u! m^L C(u,L),
    |Ee|  = N_(k-r).

**Proof.** By R212-A, eE consists exactly of states whose support contains S and is therefore stable under left multiplication as well as right multiplication. Since e is idempotent, eE⊆E e E and the reverse inclusion follows from left stability, so E e E=eE. R/L/H/J classifications follow. For each support T of size u, there are u! orders and m^L C(u,L) admissible complete event tails. There are binom(k-r,u-r) supports T containing S. Summing proves the formulas. QED.

## Native six-axis observer (m=12 signed directions, k=6 independent sources, L=2)

The full-tail ideal contains 1,407,600 idempotent observer-action states, forming exactly 64 Green-R (and Green-J) classes, one per subset of six provenance labels, and 1,407,600 singleton Green-L classes. Class size and principal-ideal counts depend only on r=|S|:

| r | Number of R-classes | Size of each R-class | |E e| | |e E| |
|---:|---:|---:|---:|---:|
| 0 | 1 | 144 | 1,957 | 1,407,600 |
| 1 | 6 | 576 | 326 | 1,174,176 |
| 2 | 15 | 1,440 | 65 | 986,400 |
| 3 | 20 | 4,320 | 16 | 833,760 |
| 4 | 15 | 17,280 | 5 | 708,480 |
| 5 | 6 | 86,400 | 2 | 604,800 |
| 6 | 1 | 518,400 | 1 | 518,400 |

This lattice yields a constant-size 6-bit support test for right-ideal reachability after the source observer has been decoded. The arbitrary target action/state still requires its complete paired tail; a support membership test is not a lossless replacement for the R209 21-bit action code or the typed native BRC physical effects.

## Reproduction / boundary

Run \`node R212_green_support_ideal_check.mjs\` and compare its exact JSON with \`R212_verification.json\`. The checker enumerates all E states for 18 finite models m=1..2,k=0..2,L=1..3 using the R210 word-length k+L coverage lemma. It exhaustively constructs left/right principal ideals of all full-tail states, checks their descriptions, counts, R-class and L-trivial claims, and crosschecks the six-axis formulas using BigInt. General validity rests on the symbolic argument; no installed native \`enterprise_math.brc_transport\` integration or independent mathematical review is asserted.

## Next science

Determine Green relations for the full monoid J including short-tail elements and build fast right-ideal filters for packed action IDs; separately connect the stable full-tail/Green structure to an actual native BRC histogram adapter and measure end-to-end runtime/memory/serialization costs without discarding provenance, weights, multiplicity, physical action or ports. No Task CLAIM or Result/Review was created.
