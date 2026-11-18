# EC49FCF — Target for the remaining four-slot configurations

Frozen model and witness are unchanged: science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, candidate generator `5b10f1c296cb8826d4b69f6fd83dba89d765df1c`, witness `b3b43ef6abe2fd816d979792d18a67ee5d0aad50`.

The author-side exact checked frontier now covers 4,015/4,845 four-slot choices. Remaining 830 are entirely among 1 early H4–H6 slot and 3 late H7–H9 slots. Complete the H7/H7/H8 case at deterministic indices 210..239 (30 groups), then the other 800; obtain exact groupwise lower bounds or a legal construction using <=157 distinct native prefixes.

High-cost group bottleneck: direct nested bitset enumeration became slow for some H6+H7+H7+H8 combinations; retain prefix sets, native signed step order, BRC key/signed X6 endpoint and the nine-state observer. Try an exact pair-union meet-in-the-middle: for fixed prefixes F and cut c, precompute distinct residual pair unions of the first two slots with cardinality < c, and pair unions of the last two. Test `|U union V|<c` with a length/cardinality bucket lower bound before expensive union. Preserve explicit witness words for any improvement. Compare the calculation cost and memory against monotone nested search.

After four-slot completion, change research axis rather than treating local rigidity as global optimality: five-or-more coordinated replacements and alternate cache-key schedules remain live. The broader mother problem's earlier <=94 bound has a different search domain.
