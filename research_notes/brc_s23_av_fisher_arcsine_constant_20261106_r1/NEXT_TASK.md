# Next research unit — fixed-z Fisher minimax coefficient and legal S23 mother bridge

Validated starting point: the author-side shared-Jeffreys kernel attains a *uniform* local-overlap constant 2/I_(l,u) for any fixed padded interval around lawful r in [1/57,1/3]. Therefore `liminf sqrt(n/log n)(1-delta_n) >= 8/(I_*sqrt(15)) = 2.139905...`. This is a lower bound on the optimal asymptotic overlap constant, and its full minimax value remains open.

1. For a *fixed* compressed probability z, derive the exact feasible r-fiber from a,c∈[1/2,7/8]. Compute its Fisher length `I(z)=integral_(rmin(z))^(rmax(z)) [r(1-r)]^-1/2 dr`. Optimize `I(z)*sqrt(1-z)` over lawful z; develop a measurable prior based on the compressed word's z estimator, with boundary error controlled at the `sqrt(log n/n)` scale.
2. Derive a matching multi-hypothesis or integral-prior *upper bound* on the leading overlap constant. Distinguish the lower bound delivered by a construction from the unknown minimax limit.
3. Independently audit the beta-posterior local-limit uniformity, Chernoff tail scale, endpoints and exchange of `inf` with the uniform limit; if needed produce a formal or interval-certified finite-n lower bound.
4. Continue the frozen six-source/ten-label S23 mother problem `R_beh(k,10)` with lawful source selection and encoder/decoder, preserving the exact observation and quantifier orders.

Control: native service session registration returned FAILED/OSError and current task list WAITING_RESOURCE/EVENT_COLLECTION_IO in this session; no formal CLAIM/Owner was established. The present work was persisted on the existing Draft PR #1777 as author-side independent research, for future controlled intake and mathematical review.
