# R708 — Rooted BRC holonomy invisible to every unrooted cyclic-window census

Date: 2026-11-11 Asia/Shanghai. Scope: independent author-side exact theorem in the pinned V17/V20/V36/V38/V39 model, UNREVIEWED.
Parent task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142.
Inherited frozen scientific input locator: a72226e2430ffa4786321ac86e7f0c599d5f0389. P000 and triadic-balance blobs were individually read at that ref; the native continuation packet flags this historical locator as absent from its immutable source manifest. Do not treat that manifest uncertainty as verified admission of this derivation.
Exact new source: R707, immutable 696c2e3d698105447b77c64ecee631b91e052dcc. Group histogram: R706, immutable 16fd003aaaa88d221db442c9e048f9af6878487d.
Underlying existing model premises: V17 slot replacement; V20 unique-max pure-triadic coupling; V29 nonnegative PASS/TRANSFER; V36 synchronous directed-copy ring; V38 two based loop packets; V39 pointed S3 future-operation observation.

## Question and BRC typing

R707 constructs one fixed directed m-Cell topology for every ordering of oriented packet multiset (k A,k A^-1,l B,l B^-1), but different words require different initial Cell fields. How much does the exact observer lose when it retains all spatial single-time occupancies or every unrooted cyclic window, while discarding the starting Cell's chosen packet position?

Use the finite positive unit-weight BRC carrier whose branch identities are the oriented words w in {A,a,B,b}, where lowercase a,b denote reversed loops A^-1,B^-1. Each branch has exact weight one, with ordering, orientation, original packet identity and initial Cell configuration retained until an observer is explicitly applied. The future-operation observer is V39's pointed holonomy h(w) in S3, not a signed amplitude. The positive weighted BRC histogram is the integer multiset of (observable signature,h) pairs; its exact count is an information-fiber result, not physical sampling probability. No pi, trigonometric propagation or continuum approximation occurs.

The four native triad packets, expressed as three Cell transitions from/to based triad 012, are

    A : 012 -> 013 -> 023 -> 012
    a : 012 -> 023 -> 013 -> 012
    B : 012 -> 023 -> 123 -> 012
    b : 012 -> 123 -> 023 -> 012

Their ordered S3 holonomies satisfy H(A)=H(a)=(0,2,1)=s and H(B)=H(b)=(1,0,2)=t; s,t are distinct transpositions. The equal counts k,k,l,l imply q=2(k+l) even and m=3q=6(k+l). The V36 ring initial field is the triad word W(w) on m labeled Cells, and its Cell-0 V39 holonomy is the ordered packet product h(w).

Define the full directed first-order ring census M(w) by the multiplicities of every triad S and every directed adjacent triad pair S->T along this m-Cell ring. Define the cyclic radius-r deck D_r(w) as the multiset, including multiplicities, of all m cyclic windows (S_i,S_(i+1),...,S_(i+r-1)), for arbitrary r >= 1. The unrooted necklace observer N(w) remembers W(w) up to cyclic Cell rotation. All windows are spatial initial-field observations, not separate time ticks.

## Theorem 1 — identical complete directed transition census, three pointed outcomes

For every k,l >= 0 with k+l>0, all oriented packet words with the prescribed multiplicities share exactly the same M(w). The nonzero triad occupancies are

    #012 = 2(k+l),  #013 = 2k,  #023 = 2(k+l),  #123 = 2l.

The complete directed-edge multiset is the sum of k copies each of the A and a packet edge triples and l copies each of B and b, independent of packet order. In particular, no directed one-step transition matrix, even with every native triad label and its exact count, distinguishes different packet orders. R707's identical V29 matched-transfer overlay may also be included without changing this statement.

If k,l>0, this exact census fiber contains all three pointed holonomies {identity,c,c^-1}, where c=st is a 3-cycle. Thus the minimum worst-case auxiliary fixed-length state for answering h from M plus R707's V29 overlay is exactly ceil(log2 3)=2 bits. Sufficiency stores the three-valued holonomy; necessity follows from the three explicit attainable pointed states in R703/R706/R707. This is an observer-specific fixed-length information bound.

Proof: every packet has exactly one 012 start and its own fixed three directed edges. Packet boundaries use the shared 012 state; concatenation introduces no extra edge. Summing each packet's contributions therefore proves M invariance. Since q is even, h is even. For k,l>0 the exact R706 histogram has positive multiplicities for identity and both nonidentity 3-cycles, so all three occur under the R707 construction.

## Theorem 2 — cyclic rooting changes holonomy while preserving every window census

Let rho rotate the packet word one packet to the left. Then

    W(rho(w)) = shift_by_3_cells(W(w))
    D_r(rho(w)) = D_r(w) for EVERY integer r >= 1.

Nevertheless,

    h(rho(w)) = H(first_packet)^(-1) h(w) H(first_packet).

Because the first packet holonomy is a transposition, it fixes identity but interchanges the two nonidentity even 3-cycles. Consequently, for h(w)!=identity, the two pointed initial configurations w and rho(w) have identical D_r for all r simultaneously — including r=m or longer, which retains the entire unrooted cyclic triad necklace — but different exact V39 pointed holonomies.

The packet word can be recovered from a rooted W(w): exactly the packet boundaries contain triad 012 (its two intermediate triads are never 012), and each 3-step rooted motif identifies A,a,B or b uniquely. If W(w') is a cyclic Cell rotation of W(w) and both begin at 012, that Cell rotation is by a multiple of three and corresponds to a packet rotation. Hence each unrooted necklace has a pointed-holonomy fiber equal to {identity} if flat or {c,c^-1} if nonflat, with no other cases. One extra binary state bit is necessary and sufficient to resolve pointed h from the COMPLETE unrooted necklace: it distinguishes the two nonflat orientations and may take an arbitrary fixed value on flat necklaces.

Proof: the full group product is H(p1)H(p2)...H(pq). Rotating p1 to the end gives H(p1)^(-1)h(w)H(p1); H(p1)^2=identity. Conjugation of a nontrivial element in the normal A3 subgroup by any transposition swaps the two inverse 3-cycles. The triad boundary observation proves the converse classification.

## Corollary 3 — exact balance within each nonflat cyclic BRC necklace

On the finite orbit of a packet word under rho, rho is a bijection. For every nonflat orbit, rho exchanges the pointed classes c and c^-1. Therefore the two classes occur with EQUAL exact branch multiplicity inside EACH nonflat necklace, not merely after pooling all words. A flat necklace contributes only identity. In particular, no nonflat word has an odd packet-rotation period. This gives an orbitwise exact positive-BRC count balance without postulating a stochastic physical ensemble.

By Burnside counting, the number of oriented packet necklaces is

    N(k,l) = (1/[2(k+l)]) *
             sum_{d divides gcd(k,l)} phi(d) *
             (2(k+l)/d)! / [(k/d)!^2 (l/d)!^2]

for k,l>0. This enumerates necklaces, not pointed h outcomes. The proof counts words fixed by rotations with repetition factor d. It is independent of any conjecture about physical dynamics.

## An explicit 12-Cell all-radius witness

Use w=A;b;a;B (string AbaB) and rho^-1(w)=B;A;b;a (string BAba). They have k=l=1 and identical spatial cyclic-window decks for EVERY r, and the same R707 compatible full V29 overlay. Their pointed holonomies under the V17/V37 display convention are

    h(AbaB)=(1,2,0);  h(BAba)=(2,0,1).

Both initial fields begin with triad 012 at Cell 0; they differ by a cyclic spatial shift of 3 Cells. The shared unrooted necklace therefore does not select which 012 occurrence is the labeled Cell-0 root. The exact 1-bit distinction is an observer-specific root/frame residual, not an extra X6 spatial axis or an independently established physical force.

## Verification and limits

The standalone JavaScript checker enumerates every oriented branch for (k,l)=(1,1),(1,2),(2,1),(2,2), with exact integer branch totals 24+180+180+2520=2904. It checks one M profile per parameter pair, the orbitwise holonomy classification and c/c^-1 equality, one-packet conjugation, the Burnside necklace counts and the R706 full histogram. It checks the explicit 12-Cell witness at radii 1,2,3,4,6,12,24,25,48. The all-r claim is established by the cyclic-shift proof, not inferred from those finite radii.

Observed necklace counts are 6,30,30,318; nonflat necklaces 2,12,12,154. The exact checker verdict is R708_EXACT_BRC_NECKLACE_PASS.

This is a model-internal author theorem. The V29 event overlay is declared, not generated by an autonomous inventory-sensitive scheduler. R707's distinct initial microstates remain distinct. The historic task scientific locator's source-manifest warning remains unresolved. No formal native CLAIM, source semantic checkpoint, Result, independent review, Working Truth or Foundation promotion is asserted by this note.

## Smallest next scientific unit

Construct a native coupled scheduler with explicit Link/Port stock and Cell-state dependence, and test whether its allowed set of initial configurations is closed under packet-root rotation rho. If it is, the nonflat one-bit pointed root residual survives that scheduler; if it is not, calculate the restricted orbit and holonomy image exactly. In either case preserve the actual frozen pin and actual source version, and distinguish raw event-order requirements from observer-induced compression.
