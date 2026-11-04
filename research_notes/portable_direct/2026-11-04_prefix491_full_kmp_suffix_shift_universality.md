# PREFIX-491 — Full-KMP suffix shift and exact source-support interface

Date: 2026-11-04 Asia/Shanghai. Researcher: EM-DIRECT-4A9075 (native activity RA-DF789B9970E5F77F84420542; Source session registered, no formal CLAIM).
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Scientific input frozen: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor: PREFIX-490, research_notes/portable_direct/2026-11-04_prefix490_five_signed_source_masks_and_gate_exception.md.
Behavioral rules read separately at current global and EM canonical main.

## Exact scope and observer

The parent native space is P000 Heartbeat X6, six spatial axes plus separately typed time. The present **restricted observer** holds the sixth special direction to zero occurrences, retaining the five ordinary signed axes a/A,b/B,c/C,d/D,e/E and all ordered-path provenance before the Boolean-source projection. No independent lower-dimensional native geometry, force law or physical dynamics is asserted. A path is any ordered word, with **no global pattern avoidance**. For lowercase/uppercase occupancies u_i,v_i, put y_i=u_i-v_i, p_i=min(u_i,v_i), n=sum_i(u_i+v_i), m=sum_i p_i=(n-sum_i|y_i|)/2. The BRC cancellation observer is V=p_b+2p_d+p_e, W=p_c+p_e. Each fiber is counted once, irrespective of word multiplicity or positive weight.

Let g be any **nonempty signed ordinary-direction word** of length L. KMP terminal state q_g is the length of the longest suffix equal to a prefix of g, *including* full match q_g=L. Source tag N means no b/B/c/C yet, B means b/B occurred first, C means c/C occurred first.

## Lemma 1: integer polygon saturation

For p_i>=0, sum p_i=m, the attainable (V,W) are exactly P_m={(v,w) integer:0<=w<=m,0<=v<=2m-w}. Necessity follows from W<=m and V+W<=2m. For a prescribed w,v with v<=2(m-w), set p_c=w, p_e=0, p_d=floor(v/2), p_b=v mod 2, p_a=m-w-p_d-p_b. If 2(m-w)<v<=2m-w, set p_d=m-w, p_e=v-2(m-w), p_c=w-p_e, p_a=p_b=0. This constructs every lattice point. Thus K_m=(m+1)(3m+2)/2, with K(t)=sum_{m>=0}K_m t^m=(1+2t)/(1-t)^3.

## Theorem 1: exact full-match suffix-shift universality

For every fixed nonempty gate g over the ten signed directions, the number A_g(n) of distinct fibers (n,y,V,W,q_g=L) has generating function

    F_g(z) = z^L (1+z)^2 (1+2z^2)/(1-z)^8.

This depends only on L, not on gate letters/order. For n<L, A_g(n)=0. For n>=L (binomial terms with negative lower input are zero),

    A_g(n) = C(n-L+7,7)+2C(n-L+6,7)+3C(n-L+5,7)
             +4C(n-L+4,7)+2C(n-L+3,7).

For fixed L, A_g(n)=n^7/420+O_L(n^6).

*Proof.* Let h_i^+,h_i^- be the number of signed i/I letters in g. A raw occupancy vector admits a word ending in g if and only if u_i>=h_i^+ and v_i>=h_i^- for every i, because all remaining letters may be ordered freely in the prefix. Such a word has q_g=L regardless of its prefix.

For fixed y_i, write u_i=p_i+max(y_i,0), v_i=p_i+max(-y_i,0). The forced suffix is equivalent to p_i>=alpha_i, where alpha_i=max(0,h_i^+-max(y_i,0),h_i^--max(-y_i,0)). Write p_i'=p_i-alpha_i>=0. At fixed y the BRC output image is *a translate of* P_{m'}, where m'=m-sum_i alpha_i; its size is K_{m'} for m'>=0. The minimum word length contribution from coordinate i equals

    |y_i|+2alpha_i=h_i^++h_i^-+|y_i-(h_i^+-h_i^-)|.

Indeed, reserving the suffix leaves u_i',v_i'>=0 with u_i'-v_i'=y_i-(h_i^+-h_i^-); the minimal sum u_i'+v_i' is its absolute value. Hence the fixed-y fiber series is z^{sum_i (|y_i|+2alpha_i)} K(z^2). Summing over all y_i in Z gives, for each i,

    sum_{y_i in Z} z^{|y_i|+2alpha_i}
      = z^{h_i^++h_i^-} sum_{k in Z} z^{|k|}
      = z^{h_i^++h_i^-}(1+z)/(1-z).

Multiplying all five independent factors yields z^L((1+z)/(1-z))^5 K(z^2), which simplifies to F_g(z). Expanding its numerator 1+2z+3z^2+4z^3+2z^4 yields the coefficient formula and the asymptotic. QED.

**Important interface:** This is a theorem about **distinct complete BRC observer fibers**, not about ordered path counts, weights, signed amplitudes, or the other KMP states q<L. The shift factor does not claim that deleting g from an *individual* word preserves V,W; rather the fixed-y cancellation polygon is translated. This is an exact observer-scoped equality.

## Theorem 2: full-suffix source-mask interface

For an occupancy vector x=(u_i,v_i) admitting g as suffix, subtract its signed symbol-count vector h and let b',c' be the numbers of b/B and c/C remaining in its prefix multiset. Let chi(g) be the first among b/B/c/C within g, if present, otherwise N. The set of attainable *first-source tags* in all words with this occupancy and suffix g is exactly:
- {B,C} if b'>0 and c'>0;
- {B} if b'>0 and c'=0;
- {C} if b'=0 and c'>0;
- {chi(g)} if b'=c'=0.

Proof: prefix letters can be permuted to put any present first-source family first; if no prefix source exists, the suffix fixes the first source. All such words end in g and therefore have KMP terminal q=L. Taking the union over all occupancy witnesses satisfying the fixed (n,y,V,W) observer equations gives the exact Boolean mask of that fiber. Consequently, two gates with the **same signed Parikh vector and same chi(g)** have pointwise identical full-match source masks, for every n,y,V,W, not merely equal aggregate counts.

For the original gates aab and aba, both conditions hold: h=(a twice,b once), chi=B. Therefore their **q=3** source masks agree pointwise at every BRC fiber and every n, even though their q=0 distributions (PREFIX-490) differ in a finite boundary case. No equality for q=1 or q=2 is inferred.

## Exact executed certificate and measured coverage

A Python 3 standard-library, exact-integer certificate was executed, separately:
1. Enumerating the complete p-vector lattice for m=0..12, checking polygon saturation exactly.
2. Checking the unrestricted rational-series coefficients using independent signed-displacement+polygon summation for n=0..10.
3. Enumerating every count-vector prefix, appending a fixed gate, deriving the exact first-source mask and comparing total fibers to Theorem 1 for gates aab, aba, aa, aB, aAc, bca, n up to 10.
4. Running a second **raw ordered-word KMP+first-source automaton DP**, retaining all ten signed symbol counts, and checking **every observer fiber and source mask** against the prefix calculation for each of those six gates at all n=0..7.
5. Checking pointwise equality of source masks aab/aba for n=3..10.

All executed assertions passed; local original log ended ALL_CHECKS_PASS. For aab and aba, full-match fiber totals for n=3..10 were 1, 10, 55, 220, 712, 1972, 4842, 10800. At n=8 source masks were B-only=768, C-only=528, BC=676; no N. These are exact finite results; arbitrary n follows from the proofs above, not from the bounded code.

The executed full Python certificate, original log, and larger derivation are supplied in the separately preserved PREFIX491 local evidence archive; the repository mathematical report is fully self-contained. Independent Driver review and project admission have not occurred.

## Next PREFIX-492

Resolve intermediate terminal KMP states q=1,2, starting with m=0, y_b=1,y_c=0 and y_a=k>=0 in gates aab vs aba. Derive exact reachable q-state sets for all k and locate finite versus infinite differences. Then lift to signed a/b and nonzero cancellation counts, maintaining the same BRC/source observer and using the q=3 formula as a strong cross-check. Frozen scientific pin and P000 remain unchanged.

## Current provenance and limits

Global normative entries: awdawmip/chatgpt-global-knowledge canonical main 00_BOOTSTRAP.md, OPERATING_MANUAL.md, MATH_RESEARCH_POLICY.json, CODE_GENERATION_POLICY.json, OUTPUT_TEMPORAL_SEMANTICS_POLICY.json, ACTIVE worldview and EM P000 projection. EM normative entries: docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context, docs/PORTABLE_RESEARCH_PROTOCOL.md, research_priorities/research_method.json, p000_reality_foundation.json and Heartbeat World/JOIN observer preservation. This is author-side proof, not external mathematics or physical-model acceptance. Native session registration is not a formal Task CLAIM, Result freeze or independent Review.
