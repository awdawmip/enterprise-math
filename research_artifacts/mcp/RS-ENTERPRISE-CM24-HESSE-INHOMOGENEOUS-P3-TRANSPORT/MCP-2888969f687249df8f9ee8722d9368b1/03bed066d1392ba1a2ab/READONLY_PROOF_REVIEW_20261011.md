# Readonly proof review of the parameter-jet and harmonic-boundary preparations

Reviewer: /root/number_theory_next_unit/hypergeometric_parameter_jet/harmonic_boundary_review.
The reviewer is a separate agent in shared, nonblind context. No native Task,
computation regression, provider query, or remote write was performed. This is
a bounded preparation proof check, not a frozen Source Driver review or final
mathematical acceptance.

Main preparation, sections 3 and 4: BOUNDED_PROOF_CHECK_PASS.
The exact ratio has factor 2^(1−p), including the removed 2p/p contribution.
The six carry classes and pairing r with p−r are correct. The three V₁ pair
contributions are −3/r+2p/r², 2p/r² and −p/r²; the V₂ weights are
−29,−20,4. These give exactly −3T₆+12T₃+(33/2)T₂ in HB.
All three factor-entry layers agree with direct differentiation, including
−δ(3p+δ)R_n(t) in the double-factor layer. BOUND and UNIT are valid, so
the known mod-p² comparison proves the divisibility needed by HB.

One minor wording correction: main section 2 reverses the verbal factor 4
between differential operators. The exact relation is
D_H(F∘q)=4(D_G F)∘q. The frozen main text remains unchanged; the
companion CM0 appendix contains the explicit erratum. The quadratic identity
and later formulas are unaffected.

CM0 value-observer appendix: CONDITIONAL_BOUNDED_PROOF_CHECK_PASS.
Assuming the parent residual ODE and degree bound, the recurrence denominators
are units and the homogeneous solution truncates after degree 2m. Thus
J−J*=J(0)H₀. The top-degree ODE condition is inherited from the actual J
and its homogeneous difference, and creates no second free coefficient.
Inherited unit16 and CM0 imply H₀(x±)=0 mod p, so J(x±)=J*(x±).
The exact-lift divided-value correction therefore needs no boundary scalar.
Changing J by cH₀ changes the derivative by cH₀'(x±), generally nonzero
under inherited SIMPLE, so the cancellation cannot be extended to derivative
observers or full polynomial reconstruction.

Reviewer boundaries: parent residual ODE, inherited CM0/SIMPLE, and finite
regression were not independently verified by this reviewer. Both preparation
texts remain nonexecuted; the main HB formula is algebraically checked and
the CM0 point formula is conditional on the explicitly stated premises.
The reviewer's finite readonly assignment is complete.
