# Stage509-B continuation — finite exact BRC exposure without exponential tag-skeleton expansion

Frozen pins remain GK `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Science predecessor is Stage508-B PROOF_STAGE508B.md, and Stage507-B unchanged immutable @7d53c1741c5bec29886b43d7d7d27c0e68ff6370. Current behavioral rules refresh independently.

Verified: an identity/tag reachability BFS over all legal pre-action prefixes of length <h computes exactly the original positions directly exposed through POP, DELETE2, SET_END(r), INSERT2 boundary and DELETE_KTH_PUBLIC(k) with inserted P tokens. The subset is included in Stage507 conservative positional-halo/rightmost-P union. Keeping its singletons + complete 6D-displacement/144-edge F summaries is future-lossless for the declared operator grammar/horizon. Example n=19,h=3,R={2,11},S={1,3} retains 12 singletons instead of 15. A nontrivial n=28 pair with older P source positions 0 vs 1 has identical compressed states. The compact checker used the immutable Stage507 proof engine: 10,889 roots, 185,991 all-prefix nodes, 226,470 transitions; all PASS.

**Smallest new research unit:** derive an exact symbolic reachability transformer avoiding complete BFS over identity/tag skeletons, prove a sound/complete abstraction and compare time/space against exact T_h for n=19/h=3 and n=28/h=2. Independently test whether both INSERT2 neighbors truly require explicit retention under the full F concatenation algebra, or whether a smaller boundary representation is sufficient (counterexample or exact proof).

The independent full-12-direction/144-active-heterogeneous-edge Euler–BRC rank/unrank comparison remains open (full bit-cost, preprocessing, wall time, peak RSS on identical inputs).

Native Owner, CLAIM, Result and Driver review not confirmed: em_status and em_control_tasks returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`. GitHub author-side branch persistence is evidence, not task-control admission.
