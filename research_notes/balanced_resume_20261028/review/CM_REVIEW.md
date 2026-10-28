# Nondecisive mathematical review: multipoint endpoint decoder

Reviewer: EM-REVIEW-58D6A2. Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Date: 2026-10-28, Asia/Shanghai.
Finding: the explicit D-base-field-scalar decoder and its stated local
coefficient threshold follow in the declared ambient carrier for D<=m.
No unresolved mathematical defect was found after the finite-jet wording
clarification. This is a researcher review, not a Driver disposition.

Reviewed file: `cm/CM24_MULTIPOINT_TRACE_ENDPOINT_DECODER.md`.
Final SHA256: `d85a69d5e20438ab63a653e3aea6ffbbddfebbbd8ec92435e8a85d7b9c3f970c`.
First submitted SHA256: `3df0130f7a13015b669ac0e5cdf7ddd339bffc588d0d1bd93430943b54b06ef9`.
The revision only clarifies that other-point and conjugate local data are
the prescribed finite jets through order d_j-1; no infinite full-jet
information lower bound is asserted.

I also read the selected original minimal endpoint manuscript, whose
SHA256 is `9df43a752608954cc2d103e40a4db911064c3e5fbad0d9fae1a2bc0690436df8`,
and verified its low-degree invisible subspace and original x=4 construction.
Its lower-bound authorship is preserved rather than re-counted as new.

## Independent derivation checks

The cubic q has derivative (3/4)(x-1)(x-3), so ramification can occur only
above a=1 or 0. The prescribed roots 4 and 0 avoid it and satisfy
q'=9/4. Elsewhere any irreducible factor yields a separable extension of
degree 1,2 or 3. Since p>=13, neither these degrees nor 24,4,9 vanish.
In particular e^(-1)Tr is well-defined, a point that would fail without
the characteristic restriction.

Multiplying T by x^N before expanding at alpha=0 removes the actual Laurent
pole. The remaining denominator alpha-3+t is a unit at every chosen root.
For the full carrier, exact cancellation gives B(a+H_alpha(t)); the Taylor
coefficients lambda=(3/4)(alpha-1)(alpha-3) and mu=(3/4)(alpha-2) are correct.
The triangular system has diagonal lambda^k. Hasse coefficients avoid all
factorial divisions and remain valid in the stated characteristic.

The E-valued central and outer summands may individually leave F_p. Their
normalized traces are genuine F_p-linear single scalars, and the full
target is fixed by normalized trace. Therefore the proposed construction
really uses D base-field coordinates, rather than hiding up to 3D output
coordinates under extension-field notation. Trace is applied to a complete
linear decomposition, not to an assumed cancellation of unrelated data.

For D<=m, Hermite polynomials of degree<D belong to the permitted V and
their Q_W degree is at most 3D-2<=N-2. They are consequently invisible to
the complete central projection. The Hasse target map on this D-dimensional
subspace is an isomorphism. This proves independence modulo central data
and the same alphabet bound on every nonempty affine central fiber.

For local sharpness, the Hermite witness with only its i-th highest jet
equal to one vanishes to order d_j at all other endpoints. At every chosen
preimage and conjugate, H has order one and the other prefactor is a unit.
It therefore hides exactly in all lower prescribed local jets. For alpha=0
this is correctly a coefficient of x^N W, or Laurent exponent -N+d_i-1,
not an ordinary Taylor jet of an undefined Laurent value. The d_i=1 empty
jet convention is correct. This proof does not survive supplying arbitrary
unbounded jets at another point, which the revised statement now excludes.

The degree bound deg Q_T<=6N-2 and truncated Horner cost O(ND+D^2) are
consistent. Factor finding and field representation are expressly charged
separately; no free preprocessing or physical cost conclusion is inferred.

## Verification grade and reuse

This review is an independent paper derivation check. I inspected the
author's finite-check description but did not rerun its script; its 21,366
reported equalities are author evidence, not my independent computation.
The universal conclusion relies on the explicit algebra above, not finite
samples. Neither Lean nor another proof kernel was used.

Reuse resolution: COMPOSE_APPLIED, composing the inherited kernel/Hermite
lower bound and triangular pullback with standard finite-field trace.
The new bounded upper construction is RESULT_ONLY_STANDARD_COMPOSE and
does not justify a new global tool family or external novelty claim.

The ambient enlarged-carrier result supplies no missing outer data for
fixed forcing and no values of h_div, Y, Z or kappa. D>m and new future
operation languages remain outside scope. The arithmetic field is an
external observer model, not a native spatial dimension.

Shared control/source context is disclosed. Reviewer did not author the
construction and is not a clean-blind reviewer. Source persistence,
mathematical review, formal Result admission and parent closure remain
distinct; this report grants only the stated nondecisive research finding.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
