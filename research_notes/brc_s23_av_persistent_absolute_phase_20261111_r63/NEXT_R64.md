# R64 — exact interval-adaptive persistent sparse queries

Science pin stays `43ec6098b1330ae86d0a7863be336c5d97f6ef34` and original P000/X6 semantics remain unchanged. Consume R63's verified rational auxiliary index and its predecessor R62 (#2058), without treating either author's Draft PR as an independently reviewed Task Result.

1. Determine a sufficient exact certificate on `theta in [p/q,(p+1)/q]` for one latest-age query, using the search comparisons actually needed plus R62's winning-source/younger-source boundary noncollisions; derive its bit costs. An unrelated phase collision should not necessarily invalidate a sparse query.
2. Examine old versions and a changed observation `(j,x)`; if the original tree's relative source-phase order crosses over the interval, test whether a query-specific predecessor certificate or a non-indexed verified fall-back repairs this exact case. Use frozen `p=262204504569236716045286,q=10^24`, `m=128,H=225`, and the R62 age-`q` counterexample.
3. Extend source keys to same-t different branch IDs; distinguish latest-age observation (max over branch) from provenance-preserving future deletion and branch-sensitive queries.
4. Compare complete multi-precision costs of parameter enclosure, m-arc preprocessing, n source-key initialization, U persistent updates, Q sparse queries, output and verification against R49/R56/R58/R59/R60/R61/R62. Provide a concrete test with a winning and a losing implementation regime.

Output a precise lemma or counterexample and locally executed checker; publish smallest source-bearing durable artifact and verify immutable readback. No formal CLAIM/Result without current Source authorization.
