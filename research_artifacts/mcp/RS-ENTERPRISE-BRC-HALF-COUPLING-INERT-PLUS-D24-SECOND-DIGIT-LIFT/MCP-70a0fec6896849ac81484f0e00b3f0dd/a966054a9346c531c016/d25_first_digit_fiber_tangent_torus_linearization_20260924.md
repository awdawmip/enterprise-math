# D25 LIFT — the first-digit unit fiber is a discrete torus of affine JT2 tangent charts

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24
Consumed Source frontier: awdawmip/enterprise-math@526477f8e6da10fac0c0be6bc8c68ce73b8f68da

## 0. Why this is the next reduction

The preceding synchronized two-layer checkpoint proved that the repaired valuation-one middle stream and the valuation-two reflected stream superpose affinely at the JT2 observer. This unit identifies the exact general reason and classifies which kind of deformation can still produce genuinely new second-digit interaction.

Work over Z_p. The accepted first digit supplies units G,h with

    G h == 1 (mod p).

Define the live divided-second-digit observer on the first-digit fiber by

    D(G,h) := (G h - 1)/p  (mod p),

whenever G h == 1 (mod p).

## 1. Exact increment identity

Let alpha,beta in Z_p and suppose both (G,h) and (G+alpha,h+beta) lie on the first-digit fiber. Then the numerator identity is exact:

    (G+alpha)(h+beta)-Gh
      = G beta + h alpha + alpha beta.

Hence

    BOXED:
    D(G+alpha,h+beta)-D(G,h)
      = [G beta+h alpha+alpha beta]/p                 (mod p).   (F1)

The right side is integral as a whole precisely because the perturbed pair is still on the first-digit fiber. Formula (F1) is not a Taylor approximation.

## 2. Tangent-chart linearization theorem

If the perturbation stays at the same residue point of the fiber, write

    alpha=p a,  beta=p b,

with a,b in Z_p. Then (F1) becomes

    D(G+p a,h+p b)-D(G,h)
      = G b + h a + p a b                            (mod p),

so

    BOXED:
    D(G+p a,h+p b)
      == D(G,h) + Gbar b + hbar a                    (mod p).   (F2)

Therefore the JT2 observer is exactly affine on the entire p-adic tangent neighborhood of a fixed first-digit residue point. Its differential is the labelled linear form

    BOXED: L_{G,h}(a,b)=hbar a+Gbar b.                (F3)

For two tangent perturbations (a1,b1),(a2,b2), the mixed second difference is p(a1 b2+a2 b1), hence zero modulo p. There is no hidden JT2-visible bilinear term inside a fixed tangent chart.

This proves, independently of the shapes of the source ports, the valuation selection rule that explained the preceding source-specific affine theorem.

## 3. Source-valuation translation

Recall that G=g/p. A raw source perturbation delta g of valuation at least 2 induces

    alpha=delta g/p in p Z_p.

A raw perturbation delta h of valuation at least 1 induces

    beta=delta h in p Z_p.

Thus every coupling of a p^2-valued g-layer with a p-valued h-layer lies inside one tangent chart and is forced by (F2) to be affine at JT2, regardless of the detailed hypergeometric port shapes. In raw source variables the mixed product contributes

    delta g * delta h / p^2,

whose valuation is at least one and is therefore invisible modulo p.

The synchronized middle/top checkpoint is the special case

    alpha_s = -T^g_s/p in p Z_p,
    beta_s  = -(M^h_s+T^h_s) in p Z_p,

and (F2) recovers its absence of a JT2-visible bilinear cross term.

This is stronger than a negative result for one cutoff: it removes the entire class of same-residue p-small deformations from the search for nonlinear JT2 repair.

## 4. Why the unrepaired p-valued g path failed

A raw valuation-one g perturbation delta g=p a with a a p-unit changes the normalized factor by

    alpha=a,

which is residue-scale rather than tangent-scale. If h is held fixed modulo p, then

    (G+a)h-Gh == a h != 0 (mod p),

so the perturbed pair leaves the first-digit fiber and D is not p-integral. This is exactly the structural reason the previously tested naive p-band divided residual acquired a first-digit jump.

Repairing that path by restoring the original normalized G sends it back to alpha in p Z_p, where theorem (F2) forces tangent linearity. Thus there is a sharp trichotomy:

1. unrepaired valuation-one g movement: can be nonlinear but generally leaves the first-digit fiber, so the divided observer is illegal;
2. repaired/same-residue movement: legal but affine at JT2;
3. a genuinely new legal nonlinear route must move to a different residue point while co-deforming both normalized factors so the first digit remains fixed.

## 5. Global first-digit fiber = finite residue torus + affine tangent coordinates

The third case can be classified exactly. Let (G',h') be any other unit pair with

    G' h' == 1 == G h (mod p).

There is a unique residue unit

    u := G'/G in F_p^x,

and automatically h'/h == u^{-1} (mod p). Choose any exact unit lift uhat in Z_p^x and its exact inverse. Then uniquely for some a,b in Z_p,

    G' = uhat G + p a,
    h' = uhat^{-1} h + p b.

Multiplying gives the exact identity

    G'h' = Gh
           + p(uhat G b + uhat^{-1} h a)
           + p^2 a b.

Therefore

    BOXED:
    D(G',h')
      == D(G,h) + u Gbar b + u^{-1} hbar a            (mod p).   (F4)

So the whole first-digit fiber is naturally stratified by one discrete residue coordinate

    u in F_p^x,

and, after u is retained, the remaining JT2 data are affine tangent coordinates (a,b). The putative nonlinearity is not an unlabelled quadratic mass; it is the transition between residue-torus strata. Within each stratum the JT2 observer again linearizes exactly.

This is a BRC-minimal sufficient state for deformation search at this digit: retain (u,a,b), not only the scalar product Gh.

## 6. Consequence for the live proof search

The current repaired middle/top construction has u=1. Therefore no further rearrangement of those same p-small source bands can manufacture a new nonlinear JT2 interaction; their complete effect must be captured by the additive Green endpoint pairing and its initial mismatch coordinates.

A genuinely different deformation can matter only if it supplies a source-derived residue-torus motion u!=1 together with the compensating h-coordinate (or an equivalent Frobenius/parameter port) so that the first-digit unit relation survives. This turns the vague instruction 'try a parameter/Frobenius deformation' into a precise target: construct a lawful source family (G_s,h_s) with a nontrivial residue coordinate u_s and then identify its tangent lifts a_s,b_s.

No claim is made here that such a family exists or that it closes LIFT. The theorem only proves what information any successful family must carry.

## 7. BRC audit and next action

Observer: D=(Gh-1)/p mod p on the accepted first-digit fiber.
Population/state: normalized source factors G,h; residue-torus coordinate u; tangent residuals a,b; fixed prime/residue-class provenance.
Safe quotient: within a fixed u-chart, replace the product by the affine form (F4), because the discarded ab term is multiplied by p after division and is JT2-invisible.
Forbidden quotient: forget u before comparing different residue points; apply D to a path that has left the first-digit fiber; infer that all higher digits are affine. The discarded p a b term becomes visible one digit deeper.
BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.

Next action remains the canonical one, now sharpened: first derive the complete additive finite-Green endpoint pairing for the existing u=1 synchronized path, including initial Q/U/V mismatch. If that does not close identically, any alternative parameter/Frobenius construction must explicitly exhibit a nontrivial source-derived u-coordinate and its compensating tangent data; another u=1 p-small cutoff is ruled out by (F2).
