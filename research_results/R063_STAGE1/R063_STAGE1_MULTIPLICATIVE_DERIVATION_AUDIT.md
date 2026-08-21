# R063 Stage 1 — Multiplicative derivation audit

The Gaussian factorization layer has a compositional structure not visible in the scalar norm alone.

For representable `A,B`, signed Gaussian root multiplication is surjective onto the signed root fiber of `AB`.  Prime-wise, every split-prime exponent allocation for `AB` can be decomposed into valid allocations for `A` and `B`; ramified and inert contributions are fixed, while Gaussian units distribute across the factors.

The deterministic audit covers every unordered pair from `[2, 5, 13, 17, 25, 65]` and all signed root multiplication channels.  All `21` product audits are surjective: `True`.

Multiple factor-pair channels can collapse to the same component root.  This multiplicative derivation multiplicity is a provenance enrichment above the deduplicated native trace and is **not** native path multiplicity.

Small deterministic separation witness:

`{"A": 2, "AB": 4, "B": 2, "component_root": [0, 2], "multiplicative_derivation_pair_count": 4, "native_path_multiplicity": 1}`.

No law identifying or multiplying algebraic derivation multiplicity with `binom(a+b,a)` is adopted.
