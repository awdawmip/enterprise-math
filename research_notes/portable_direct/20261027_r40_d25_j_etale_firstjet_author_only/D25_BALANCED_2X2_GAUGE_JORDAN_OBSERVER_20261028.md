# D25/LIFT portable author theorem — balanced 2+2 gauge and Jordan repair

2026-10-28. AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. Existing task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged. This finite-field model is auxiliary, not an H0/B0 or P000 native X6/6+1 computation.

## Exact carrier, prior result and observer

The prior author-only repeated-block (m+1) theorem gives q+3 full-centralizer orbits for m>=2 when the second eigenspace is one-dimensional. That dimension-one condition is essential. Here we test two eigenspaces of equal dimension. The marked source carries A, B, the eigenspace labels, X, Y, signed second-jet K and the permitted gauge group. Future operations include multiplication/squaring of K. A scalar quotient is valid only if the declared current and future observers descend.

Let k=F_q, a!=b, and A=diag(a I_m,b I_m). For B in M_{2m}(k), define

  K=[B,A]=((0,X),(Y,0));
  X=(b-a) B12,  Y=(a-b) B21.

All X,Y in M_m(k) occur. The map B -> K has kernel of dimension 2m^2, so each fixed K has q^(2m^2) marked B-sources. The full centralizer GL_m(k) x GL_m(k) acts by

  (P,Q): (X,Y) -> (P X Q^{-1}, Q Y P^{-1}).

## Theorem 1 (all m, all finite fields)

On the stratum det(X)!=0, the above full-centralizer orbits are in exact bijection with similarity classes of C=YX in M_m(k).

Proof. Choose P=X^{-1}, Q=I, so X becomes I and Y becomes C=YX. Any gauge preserving X=I has P=Q and acts on C by conjugation. Conversely similar C yield equivalent normalized pairs. This proves an orbit bijection, not merely a necessary invariant. The claim assumes the FULL residual centralizer and square invertible X; an unknown native subgroup or singular X is outside this classification.

## Theorem 2 (m=2, odd q)

The det(X)!=0 stratum contains exactly q^2+q full-centralizer orbits. A complete orbit observer is

  (t,d,j) = (tr(YX), det(YX), Jordan flag),

where j=1 if t^2-4d=0 and YX!=(t/2)I, and j=0 otherwise. For a two-by-two matrix, its quadratic characteristic polynomial determines its conjugacy class except on a repeated-root polynomial, where scalar lambda I and nontrivial Jordan lambda I + E12 are distinct. Thus the observer is complete.

Count monic characteristic polynomials: q repeated-root polynomials with TWO classes each; q(q-1)/2 split distinct-root polynomials, one class each; and (q^2-q)/2 irreducible quadratic polynomials, one class each. Total

  2q + q(q-1)/2 + (q^2-q)/2 = q^2+q.

Exactly q+1 classes are singular: zero scalar, nonzero nilpotent Jordan, and diag(0,lambda) for lambda!=0. Hence q^2-1 classes on the further det(Y)!=0 stratum.

## Exact counterexample and future-observer failure (p=373)

Put A=diag(0I2,1I2), X=I2, Y0=I2 and Y1=I2+E12. Both jets Ki=((0,I2),(Yi,0)) occur from legitimate marked source matrices with B12=I2 and B21=-Yi.

Both arrows are invertible; both states have identical nonzero-presence flags and ranks; both have tr(Ki^2)/2=tr(Yi)=2 and det(Ki)=det(Yi)=1. But C0=I2 is scalar and C1=I2+E12 is a nontrivial Jordan block, so the pairs are NOT gauge-equivalent even under the full centralizer. Moreover

  K0^2=I4,
  K1^2=diag(I2+E12, I2+E12) != I4.

The proposed scalar/rank quotient is therefore not safe for the specified next multiplication and matrix observation; the repeated-root Jordan bit is an exact minimal repair on this invertible-X stratum. For q=373 the count is 373^2+373=139502, a CONDITIONAL auxiliary count, not a count of native original H0/B0 objects.

## Author verification and limited inference

The companion standard-library checker enumerates every 2x2 matrix over F_p for p=3,5,7,11,13,19, partitions the full GL2 similarity orbits using elementary transvections and a primitive determinant generator, verifies one (trace, determinant, Jordan flag) per orbit and no duplicate labels, and confirms p^2+p classes in all six finite universes. It checks the displayed p373 exact witness. Totals: 176630 matrices and 529890 generator transitions, all PASS. The universal result is proved above, not inferred from the finite scan. This checker and proof share an author context; no independent review or Source admission is asserted.

## Native and provenance boundaries

The mother objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains OPEN. Existing original-class native evaluator intake #1559 still needs actual p373 H0/B0 [X]U mod p^2, Frobenius rank/direction/eta, true A and allowed gauge H, source-fixed signed ports, kappa and Delta_p-R_p, plus independently reviewable raw versioned data. Only if a lawful native source proves the balanced-block hypotheses may this auxiliary similarity test be transported. Other-lane E3 p^3 computations are author diagnostics, not the required original H0/B0 benchmark.

The earlier four-file UR V2 bundle remains UNVERIFIED_BYTES: historical size 94687 and SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76; do not reconstruct or repeat completed math. Current native direct em_status/continuation reads report BACKEND_IDENTITY_CHECK_UNAVAILABLE with operation_sent=false; Sites is static_machine_readonly/write_relay_enabled=false, no granted research executor authority; own checkpoints are inaccessible. This draft is neutral GitHub preservation, not a Source CLAIM, OPEN, checkpoint, Result, review or completed predecessor research. If a current-input-only Source seed is returned, completed_units must remain [] until Source verifies real predecessor completion.
