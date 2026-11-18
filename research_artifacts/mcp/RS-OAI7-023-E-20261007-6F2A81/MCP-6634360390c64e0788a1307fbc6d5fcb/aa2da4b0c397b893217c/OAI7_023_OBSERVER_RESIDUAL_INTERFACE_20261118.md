# RS-OAI7-023-E / conditional observer-residual theorem

Evidence status: conditional algebraic consequence of the external frozen manuscript, not independent acceptance of its analytic proof or a native BRC transport.

Frozen external input: openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a, preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/paper.tex and build/sections/dispersion.tex. It asserts, for primary Eisenstein primes of norm ≤ X, normalized cubic Gauss sums G(pi), and b(X)=X^(5/6)/log(X), that A_0(X)=kappa b(X)+o(b(X)), kappa=(6/5)c_*, c_*=(2pi)^(2/3)/(3Gamma(2/3)), and A_l(X)=o_l(b(X)) for each fixed nonzero angular mode l, where A_l=sum G(pi)*(pi/|pi|)^l. This manuscript is EXTERNAL_SOURCE_RESEARCH_NOT_ADMITTED.

Let P(X)=the number of primary prime generators of norm ≤X. Prime ideal theorem yields P(X)~X/log(X). Define C_l=A_l/P(X) (prime-count observer) and D_l=A_l/b(X) (bias-scale observer). For every X>1 with P(X)>0 and every integer l the **exact** conversion is

    D_l(X) = [P(X)*log(X)/X^(5/6)] C_l(X).

Under the stated frozen source assertions, D_0→kappa, X^(1/6) C_0→kappa, and C_0→0. For each fixed l≠0, D_l→0 and X^(1/6) C_l→0. No claim for l growing with X follows from the fixed-mode result.

Quantitative conditional error propagation: Suppose A_l=K_l*b+E_l with |E_l|≤epsilon_l*b, and P(X)=(X/log X)(1+delta), |delta|≤eta<1. Then
    |D_l-K_l|≤epsilon_l,
    |X^(1/6) C_l-K_l|≤(epsilon_l+|K_l|*eta)/(1-eta).
For a FIXED finite angular-mode polynomial w(z)=sum_{l in F}c_l z^l, by linearity A_w=sum c_l*A_l, and the weighted error is at most b*sum |c_l| epsilon_l whenever each corresponding source estimate holds. This does not license arbitrary coefficients, weights varying without uniformity, or scalar-error bounds under nonconstant reweighting.

Provenance-preserving sufficient carrier: the complex-valued labelled atoms
    mu_X = sum_{pi} G(pi) delta_{(pi,pi/|pi|,N(pi),conjugacy-tag)}
allow A_l=int z^l dmu_X and arbitrary explicitly defined labelled reweighting. This carrier is generally complex, not a positive measure. The scalar collapse A_0, even augmented by total absolute mass, loses reweighting information.

Exact two-label witness preserving conjugacy and individual unit moduli: a=(3+4i)/5, a_bar=(3-4i)/5. v=(a,a_bar), v'=(a_bar,a) both have total 6/5, absolute masses 2, unit magnitude per atom and conjugate pairs. Under the positive weights w=(1,2), however,
    w·v=(9-4i)/5 != (9+4i)/5=w·v'.
This is an algebraic labelled-interface witness, not an asserted pair of actual cubic Gauss sums. Similarly errors (a,-a) cancel at scalar level but have nonzero w=(1,2) weighted residual. An l1-bound on labelled errors is sufficient for a uniform bounded-weight error inequality; a bound on their scalar sum is not.

BRC application boundary: a positive scalar carrier can record nonnegative masses but does not recover the discarded phase, conjugacy ordering or source labels. A signed/complex labelled carrier can express the algebraic observer identities. A claim of actual native BRC transport additionally requires a valid typed encoding, update and readout commuting with the allowed reweighting; none has been established here.

Minimal open problem: determine whether the exact current native BRC Cell/Port/Source contract admits a lossless encoding for this labelled complex measure and a chosen fixed finite family of weighted operators. Preserve source provenance, phase and contributor scope. The external analytic source's correctness remains a separate proof-review obligation.

Companion checker: check_oai7_023_residual_interface_20261118.py; it uses exact Fraction rational arithmetic.