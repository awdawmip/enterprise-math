# R5 extension — DFS-balanced-parentheses Fenwick aggregate: exact 6,277 updates

Status: author-side conditional algorithmic theorem, 2026-11-12. Uses the frozen 1,065 selected path words and 2,880-node trie of PR #2152/#2155. Reuses the exact three-frontier active set proved in RESEARCH.md in this PR. No new 28-coordinate science pins.

## Theorem and correctness

Let T be a **prefix trie with distinct terminal words**; a terminal may be an ancestor of another terminal. Number all terminal words in depth-first lexicographic order `0,...,T-1`. For every trie node v define `[l(v),h(v))` as the half-open interval of terminal indices contained in its descendant subtree (including v itself when terminal). Depth-first traversal makes this interval contiguous.

Maintain a standard one-based Fenwick array F of size T, initially zero. Each selected word is activated once at its exact threshold and adds +1 at its terminal index in F. At a threshold with multiple ties, apply every constituent update before exposing the new state. Then **for every parameter r and every prefix v**:

`C_v(r) = fenwick_prefix_sum(h(v)) - fenwick_prefix_sum(l(v))`.

**Proof.** The depth-first interval is exactly the set of terminal words extending prefix v. By the R5 right-persistence theorem, each word is activated iff its threshold is ≤r. Fenwick point updates maintain indicator sums over all terminal indices; subtracting the two prefix sums counts exactly the active terminals in this interval. This includes the case where v is terminal and also has terminal descendants. QED.

This dynamic representation has T=1065 Fenwick counter fields instead of N=2880 per-prefix counter fields. Both need 11-bit unsigned exact counters (largest possible total is 1065). Individual event updates and arbitrary prefix aggregate queries require O(log T) integer additions, unlike direct trie prefix counters whose queries are O(1) after finding the node.

## Exact full-sweep mutation count

Every terminal index 1..T is activated exactly once, regardless of activation order. Fenwick cell j stores the interval of input indices `(j-lowbit(j),j]`, so receives exactly `lowbit(j)` updates over the full sweep. Consequently the cumulative number of Fenwick counter increments is the exact combinatorial identity

`sum(j=1..T) lowbit(j)`.

For **T=1065** this equals **6,277** counter increments, versus **7,444** root-and-prefix increments of the predecessor trie sweep: **1,167 fewer increments**. A paired 27-bit three-frontier state reconstructs individual activity flags if requested, so no mutable flag vector is required for the defined activation-observer interface. The event list has 953 groups; those groups may cause 1–3 Fenwick updates each.

This is an exact count of integer counter mutations, not CPU cycles, cache misses, compressed bit manipulations, or end-to-end latency.

## One explicit packed representation and full structural cost caveat

A depth-first balanced-parentheses (BP) encoding of the rooted trie uses 2N bits for open/close parentheses; preorder edge labels occupy 4E bits; one terminal marker per node occupies N bits. Thus structural bit payload is `2N+4E+N = 20,156` bits for N=2,880, E=2,879, one bit larger than the predecessor LOUDS payload 20,155 bits. Store a 0-based terminal index for each of the 1,065 pair keys in 11 bits; Fenwick's 1,065 11-bit counters plus the three 27-bit frontier counts give:

`20156 + 11(1065) + 11(1065) + 27 = 43613 bits = 5452 packed bytes`.

Under the **same logical-width accounting**, the predecessor's indexed active-counter trie uses:

`20155 + 12(1065) + 1065 flags + 11(2880) = 65680 bits = 8210 packed bytes`.

The new payload is **2,758 bytes smaller** in this model, with the distinction that the BP alternative needs matching-parentheses navigation, rank/select on terminal markers, and a correct label-to-terminal map for efficient queries. The predecessor LOUDS also requires navigation support for random-access word retrieval. These structures, event-key tables, input conversion, integer arithmetic, RAM and runtime overheads are not included in either bare packed comparison. A static BP index and Fenwick update/query implementation should be measured on the original corpus before claiming end-to-end performance or memory gains.

A generic exact prefix-query test deliberately includes one terminal that is the ancestor of other terminals; `VERIFY_FENWICK_COST.py` checks Fenwick interval queries against direct active-prefix counting after each test activation, the exact 6,277/7,444 mutation identities, and both packed-width totals. The full 1,065-word corpus is available from the pinned predecessor `VERIFY_TRIE_CODEC.py`; the frozen actual trie counts are reused, while this script's correctness theorem applies to any such trie.

**Next executable unit:** implement rank/select BP decoding for the actual 2,880-node predecessor corpus and measure total static navigation overhead and query latency; compare to directly indexed LOUDS and the earlier prefix-counter array, preserving all original labeled paths.
