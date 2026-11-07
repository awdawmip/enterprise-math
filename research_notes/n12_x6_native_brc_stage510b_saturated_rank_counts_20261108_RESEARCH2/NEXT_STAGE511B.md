# Stage511-B continuation — exact symbolic direct-target exposure

Date: 2026-11-08. Inherit frozen scientific pins GK `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`.

Consume Stage509 `94f52374ed15a2a8cb41a7bf8b5aca163e8c1370` and Stage510's proof that exact hidden #P may be replaced by `min(K,#P)` for K=max(S), **after** full-provenance D_h has been calculated. Stage510 still stores full 6D displacement and 144 ordered-edge counts; it does not compute D_h faster.

Primary unit: construct and prove a genuinely more efficient exact algorithm/transducer computing D_h for POP, DELETE2, INSERT2(P), SET_END and DELETE_KTH_PUBLIC. Start with S={1}, one remote SET, then S={1,3} and two offsets. Give soundness and completeness of the mask, and compare preprocessing states, wall time and peak memory on identical n=19/h=3 and n=28/h=2 inputs versus Stage509's skeleton BFS.

Secondary: decide whether actual D_h-safe opaque intervals can be capped below K. Test K=3, h=1/2, S={3} versus S={1,3}; a generic rank-router lower bound is not already a D_h-safe-gap lower bound. Supply a true two-history collision or a proof with precise scope.

Separate open line: full 12 signed X6 directions/144 active directed edges, heterogeneous repeated-edge Euler–BRC **exact rank and unrank** benchmarks with all big-int, precomputation, time, RSS and verification costs on identical inputs; do not substitute path enumeration timings.

Review/authority: Stage510 proof is author-side; native task owner, CLAIM and independent Driver Review require fresh authenticated Source verification.
