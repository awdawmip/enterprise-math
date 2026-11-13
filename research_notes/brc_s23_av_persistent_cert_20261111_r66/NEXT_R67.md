# R67 continuation: cached exact subtree certificates and full-cost frontier

Frozen science pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Consume R66 author result (proof, exact oracle tests, branch-preserving persistent treap, 4,397/4,400 certified queries) with precise scope.

1. Implement a cache keyed by exact immutable subtree identity, target label, observation (j,x), certified parent parameter interval and history order. Reuse only on contained intervals and unmodified version-specific subtree aggregates. Stress-test equal-time distinct branch deletions and old roots.
2. At a fixed immutable tree and matched query set, compare direct oracle, per-newer-source affine boundary checks, R63 point-phase index and R66 subtree certification. Count phase conversion, timestamp/denominator bit widths, build and updates, rational operations and sizes, certificate leaf fallback, oracle validation, plus reproducible wall-clock measurements.
3. Use frozen S23/AV sparse labels and time ~10^18 as separate regimes. For intervals that straddle exact rational collision roots, identify closed endpoints individually; avoid asserting full-interval stability from local samples.
4. Save executable program, proof and all evidence. Shared CLAIM/Result and independent review require actual native Source authority.