# D25 LIFT — supersingular Frobenius second-digit repair coordinate and a proved information-loss boundary

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Source pin: 621bd918cfe4eea9f0c0ae20aa82def82fbc87bc
Date: 2026-09-24

## 0. Consumed frontier and source isolation

Consume the durable D25 frontier through the universal-prefix first-order factor chain and the theorem-level prior-art audit. Do not reopen D24 UR/JT0, the shell/global-jet/Clausen/Green/symmetric-mass/adjoint units, or the finite scans. The live target remains the second digit only.

This unit examines one alternative source-faithful route that the prior-art audit exposed: the supersingular formal-group argument underlying Chisholm--Deines--Long--Nebe--Swisher, Proposition 16. It does not claim that their modulo-p^2 theorem already proves LIFT. Instead it derives exactly what one additional p-adic digit of that argument would have to retain, and proves that the degree-p^2 Frobenius scalar/Katz recurrence by itself is an information-losing quotient for the p^3 observer.

External source used only for the formal-group setup: Chisholm et al., *p-Adic Analogues of Ramanujan Type Formulas for 1/pi* (2013), Proposition 16 and equation (5.1). In the supersingular case their proof uses a degree-p square-root lift with matrix M=(u v; w -u), u in pA, v in pA, w a unit, -u^2-vw=b_2, and coefficient comparisons v b(p-1)/p == 1 (mod p), w a(p-1)/p == 1 (mod p).

## 1. Retain the first-order defects instead of only the modulo-p comparisons

Write

  A_p := a(p-1),   B_p := b(p-1).

Let the degree-p square-root Frobenius lift have matrix

  M = [[u,v],[w,-u]],

with

  u in pA,  v in pA,  w in A^x,  -u^2-vw=b_2.           (1)

The Proposition-16 coefficient comparison gives

  v B_p / p == 1 (mod p),
  w A_p / p == 1 (mod p).                                (2)

Therefore the following residue-class coordinates are well-defined:

  alpha_p := (v B_p/p - 1)/p        (mod p),
  beta_p  := (w A_p/p - 1)/p        (mod p).              (3)

They are not new axioms; they are the exact first neglected digits of the two source comparisons already used in the proof.

Also put

  Lambda_p := p^2/(v w).                                  (4)

Since v has valuation one and w is a unit, Lambda_p is p-integral of valuation one. The first-digit argument gives Lambda_p == -b_2 (mod p^2) in the supersingular normalization, so define the determinant/mixing repair coordinate

  delta_p := (Lambda_p + b_2)/p^2    (mod p).             (5)

## 2. Exact one-more-digit product formula

From (3), in A/p^3A,

  v B_p = p(1+p alpha_p) + O(p^3),
  w A_p = p(1+p beta_p)  + O(p^3).

Multiplying and using that Lambda_p has valuation one gives

  A_p B_p
    == Lambda_p [1+p(alpha_p+beta_p)]                    (mod p^3).   (6)

Subtract the accepted supersingular first digit -b_2 and divide by p^2. Because Lambda_p/p == -b_2/p (mod p), we obtain the canonical second-digit repair scalar

  BOXED:
  (A_p B_p + b_2)/p^2
    == delta_p - (b_2/p)(alpha_p+beta_p)                  (mod p).    (F)

This is an identity, not a fit. It separates the one-extra-digit obstruction into exactly two typed contributions:

- delta_p: determinant/Frobenius-mixing correction;
- alpha_p+beta_p: first-order coefficient-comparison correction.

Only their combination is canonical. Individual alpha_p,beta_p depend on the chosen square-root lift/basis, but the right side of (F) is choice-independent because it equals the source coefficient product on the left.

In the common normalization b_2^2=p^2 (in particular b_2=e p with e^2=1), write u=p u_1. From (1),

  v w = -b_2-p^2 u_1^2.

Expanding (4) one digit gives

  delta_p == u_1^2                                      (mod p),

so (F) sharpens to

  BOXED:
  (A_p B_p + b_2)/p^2
    == (u/p)^2 - (b_2/p)(alpha_p+beta_p)                 (mod p).    (F')

Thus even when the Frobenius determinant/eigenvalue is known exactly, one still needs the summed coefficient-comparison defect alpha_p+beta_p unless an independent identity kills or determines it.

## 3. The degree-p^2 Frobenius is provably too coarse for this observer

The matrix M has trace zero, so exactly

  M^2 = (u^2+vw) I = -b_2 I.                             (7)

Hence passing from the degree-p square-root lift phi to the commuting degree-p^2 Frobenius Phi=phi^2 collapses the full labelled matrix (u,v,w) to the single scalar -b_2. This quotient is safe for the first digit but is not safe for the p^3 product observer.

A direct separation witness is available without constructing a new elliptic curve: keep M and B_p fixed and replace an admissible A_p by A_p(1+p c), c in A. Equation (2) is unchanged modulo p, M^2 is unchanged exactly, and all Proposition-16 first-digit data are unchanged, but beta_p shifts by c modulo p and A_pB_p changes at order p^2. Therefore the data retained by M^2 together with the modulo-p coefficient comparisons do not logically determine the p^3 digit.

Consequently the Katz relation attached only to Phi (including equation (5.1) at its published precision) cannot by itself close the present LIFT. Any successful formal-group proof must supply additional source information equivalent to the invariant repair scalar in (F), or retain a finer degree-p lift/deformation from which alpha_p+beta_p and delta_p can be computed.

## 4. Interaction with the current D25 frontier

The current canonical D25 route asks for a legitimate source-derived cutoff extension Q_s whose labelled curvature transport matches the universal R_s chain. Formula (F) gives an independent BRC requirement on any formal-group realization of such an extension: a construction that sees only the degree-p^2 Frobenius eigenvalue/determinant has already quotiented away a p^3-visible repair coordinate.

Thus the formal-group route is now narrowed as follows. A useful Q_s / creative-microscoping deformation must retain, in some equivalent coordinates, the first-order source-comparison defect represented by alpha_p+beta_p and the determinant/mixing defect delta_p. If those coordinates are absent, matching the universal first-order curvature chain cannot certify LIFT even if the degree-p^2 Frobenius/Katz recurrence matches perfectly.

There is one additional bridge caution: Chisholm's weighted hypergeometric theorem uses a twist and a truncated-hypergeometric comparison only to the precision needed for modulo p^2. For a direct p^3 proof via this route, the first p-adic correction of that bridge must also be derived, not silently replaced by its Legendre-symbol reduction. This note does not identify that bridge correction with the already-derived C_m without a proof.

## 5. BRC audit

Observer: one additional p-adic digit of the supersingular formal-group coefficient product, and only its relevance as a source route toward D25 LIFT.

Preserved provenance: degree-p square-root lift, matrix entries u,v,w, the two coefficient comparisons, determinant relation, and their p-adic valuations.

Safe quotient: (delta_p,alpha_p,beta_p) may be compressed to the single invariant combination in (F) only after (F) is proved.

Forbidden quotient: replacing phi by Phi=phi^2 before the p^3 repair scalar is reconstructed. Equation (7) proves that this erases information visible to the observer.

BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.

## 6. Narrow next action

Do not try to lift the published Katz degree-p^2 recurrence alone. Either:

1. derive the degree-p square-root lift / equivalent creative-microscoping deformation for the D=-24, lambda=1/2 specialization to first order and compute the invariant combination in (F), including the first p-adic twist/bridge correction; or
2. stay on the current universal-prefix route and construct Q_s directly, but verify that its source coordinates retain an equivalent of this repair scalar before quotienting.

A failure to recover that scalar is now a proved information-loss obstruction, not merely a lack of ingenuity in recurrence matching.
