# Stage425-B — Symbolic Euler-cache count, K alignment and restricted k-source bounds

Parent Stage424-B author evidence, 2026-11-04, Draft PR #1736. Frozen science: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.

Proved: typed directed-edge remaining-Euler pair DP counts complete ordered word pairs exactly, preserving full J, endpoints, absolute K and terminal tails. n=11..100 gives 304080 original pairs, 24 output categories and full classwise agreement with explicit enumeration. Minimal all-future class status is conditional on unreviewed Stage422. A k-source deletion event of arity (0,2,...,2) simultaneously saturates Stage423's per-source correction.

Unit A: classify the reachable DP keys for n>=11. Prove or refute the observed 68n-463 cached-state formula and 85n-628 transition formula for n>=12 (n=11 is 308) under the exact program's memo/pruning semantics. Provide induction or a minimal exact failure.

Unit B: extend the Euler/J/K compiler to unequal source lengths with a declared alignment map. Derive the correct update for K on asynchronous append/POP; construct a short counterexample to a naïve [x=y] update that conflates unequal absolute positions.

Unit C: fix a multi-source deletion incidence hypergraph excluding (0,2,...,2). Seek a stronger joint deletion frontier, with exact tight constructions or counterexamples, keeping signed X6 directions and inverse-pair legality.

Deliver an actual theorem/certificate, verified program/evidence and remote readback. Preserve original P000, source pins and independence of formal Source CLAIM, Result and Driver admission.
