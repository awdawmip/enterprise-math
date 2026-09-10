# Raw Vortex interface: what must be preserved

The inspected spectralDNS source has `getConvection()` producing a raw nonlinear term, followed by `add_pressure_diffusion()` computing a scalar pressure observer from that raw term and applying the projection. The inspected blob for `spectralDNS/solvers/NS.py` is `6a11909d1e2c1d529d382952c4c9d77e7073645c`.

Let R_k = F(u × curl u)_k. With complex bilinear dot products, the ordered (p,q) contribution is

    i [ q (u_p · u_q) - (q · u_p) u_q ],  p+q=k.

Combining p!=q gives

    i [ k (u_p · u_q) - (q · u_p) u_q - (p · u_q) u_p ].

For p=q, use the ordered expression once. Keeping the first term matters: it is a gradient. The Leray projection removes it from the velocity RHS, but the scalar

    sigma_k = (k · R_k) / |k|^2,  k != 0,

still observes it. sigma here denotes the matching Fourier pressure-projection interface observable. It is NOT a claim to have reconstructed physical pressure under every convective convention, gauge, forcing or boundary condition. Production normalization and modified/physical pressure conventions still need verification.

The supplied old prototype returned an already projected advective result. That was valid for its stated projected velocity-only comparison. It is NOT a drop-in replacement for the unprojected Vortex callback: using it there makes sigma nearly zero. The nine new random-state tests reproduce this loss (relative difference approximately one) and validate the new raw Vortex output plus separate projection (relative raw/velocity/sigma differences below 8e-16 in this run).

This is standard vector/Fourier algebra and an application of the project's observer-preservation discipline, not a claimed new vector identity or an accepted project theorem. Positive mass/count BRC cannot replace these complex amplitudes. The permitted branch aggregation is only for matching output wavevector and operator semantics, with self-pair multiplicity and conjugate partners preserved.

The hybrid dispatch uses exact binary64 zero/nonzero support detection, a frozen budget of 128 full signed modes, and a one-way dense latch per trajectory. It never removes tiny amplitudes to make the sparse benchmark favorable. Latching is purely a performance decision. Tiny nonzero amplitudes and roundoff-generated mean leakage may therefore be counted in the reported support; no threshold has been used to hide them.
