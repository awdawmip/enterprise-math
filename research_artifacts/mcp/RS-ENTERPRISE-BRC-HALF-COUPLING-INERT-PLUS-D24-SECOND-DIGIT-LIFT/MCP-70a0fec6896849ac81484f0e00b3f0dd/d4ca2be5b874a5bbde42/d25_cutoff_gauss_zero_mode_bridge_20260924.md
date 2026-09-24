# D25 LIFT — the absolute unit-core zero mode is exactly a cutoff finite-Gauss parameter jet

Status: PROVED_STRICT_BRIDGE_AND_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24

## 0. Consumed frontier

Consume the accepted D24 UR/JT0 Result, the durable D25 finite-Gauss deformation and its universal terminal -2 source, the durable finite-adjoint/SBP no-new-constraint checkpoint, and the recovered absolute unit-core source decomposition

    Delta_p = Z_T + Gbar A + hbar Y  (mod p),

where p=6m+1, B_k is the original p-adic source,

    S = sum_{k=0}^{2m} B_k,       G_T=S/p,
    H_U = sum_{k=0}^{m}(12k+1)B_k,
    Z_T=(G_T H_U-1)/p              (mod p),

and A,Y are respectively the labelled valuation-one weighted middle-band and valuation-two unweighted high-band corrections.

The recovered unit-core decomposition is source algebra, but its next action still required an exact bridge from Z_T to a terminating/parameter/Frobenius coordinate. This unit supplies that bridge without differentiating the already-closed adjoint again.

## 1. Finite-Gauss deformation and cutoff jets

Let

    F(a,z)=sum_{k=0}^{p-1} c_k(a) z^k,
    c_k(a)=(-m+a)_k(-2m+2a)_k/(k!)^2,

and evaluate at z=1/2. At a=p/6 this is the original source:

    c_k(p/6) 2^{-k}=B_k.

Write

    F_r^{<=t} = sum_{k=0}^{t} c_k^{(r)}(0) 2^{-k},

and let F_r mean the full sum t=p-1. Put

    H_1^{<=m}
      = sum_{k=0}^{m}(12k+1)c_k'(0)2^{-k},

    Psi
      = sum_{k=0}^{m}(12k+1)c_k(0)2^{-k}.

The upper limit m in Psi is exact because c_k(0)=0 for k>m. Likewise c_k'(0)=0 for k>2m.

Use the already-proved parent coordinate

    a_parent = F_0/p + F_1/6.

All denominators k!, 2 and 6 are p-units for k<p, so Taylor expansion at a=0 is p-adically legitimate term by term.

## 2. Exact cutoff expansions

Because a=p/6, all Taylor orders >=3 are p^3-divisible. On the range k<=2m,

    S
      = F_0 + (p/6)F_1 + (p^2/72)F_2^{<=2m}
        (mod p^3).

Dividing by p and using the definition of a_parent gives

    BOXED:
    G_T
      = a_parent + p F_2^{<=2m}/72
        (mod p^2).                                      (1)

For the weighted unit band k<=m only the first Taylor correction is needed:

    BOXED:
    H_U
      = Psi + p H_1^{<=m}/6
        (mod p^2).                                      (2)

Accepted UR gives a_parent Psi == 1 (mod p). Multiplying (1) and (2), subtracting 1, dividing by p and reducing modulo p yields the exact bridge

    BOXED:
    Z_T
      = [a_parent Psi-1]/p
        + a_parent H_1^{<=m}/6
        + Psi F_2^{<=2m}/72
        (mod p).                                        (3)

Thus the previously abstract absolute unit-core second digit is not an additional fitted Frobenius scalar. It is exactly the divided product digit of a finite-Gauss cutoff parameter jet.

## 3. Middle and high corrections are precisely the omitted derivative supports

Let

    H_1 = sum_{k=0}^{p-1}(12k+1)c_k'(0)2^{-k}.

The source identity h=H_U+pA (mod p^2), together with the full Taylor expansion

    h = Psi + p H_1/6 (mod p^2),

and (2) gives

    BOXED:
    A = (H_1-H_1^{<=m})/6  (mod p).                    (4)

Similarly, the source identity g=S+p^2Y (mod p^3), together with

    g = F_0 + (p/6)F_1 + (p^2/72)F_2  (mod p^3)

and the expansion of S gives

    BOXED:
    Y = (F_2-F_2^{<=2m})/72  (mod p).                  (5)

Consequently the valuation-band source decomposition is exactly the support decomposition of the same finite-Gauss parameter jet. Combining (3)-(5),

    Z_T + a_parent A + Psi Y
      = [a_parent Psi-1]/p
        + a_parent H_1/6
        + Psi F_2/72
        (mod p),                                        (6)

which is the already-frozen global second-digit formula, since H_1=-Psi_x and F_2=Phi_xx.

Equation (6) is not a numerical coincidence and does not identify two coordinates by analogy: it is forced by the zero-factor support of c_k(0), c_k'(0), and the exact Taylor orders of the source deformation.

## 4. BRC information audit

Population: the finite-Gauss source ports k=0,...,p-1 with parameter-derivative order and p-adic valuation band retained.

Observer: the divided second digit Delta_p modulo p after accepted UR.

Safe compression proved here:
- the absolute unit-core carrier Z_T factors through ([a_parent Psi-1]/p, H_1^{<=m}, F_2^{<=2m});
- the valuation-one middle correction is exactly the omitted first-derivative support (4);
- the valuation-two high correction is exactly the omitted second-derivative support (5).

Preserved residual/provenance: the cutoffs m and 2m, derivative order, signed coefficients, the product digit, and the middle/high corrections remain distinct until equations (4)-(6) prove how they recombine.

Forbidden compression:
- do not replace H_1^{<=m} by H_1 or F_2^{<=2m} by F_2 before paying A or Y;
- do not identify Z_T with a supersingular/Frobenius repair scalar by analogy;
- do not discard the terminal -2 source in any later global adjoint calculation;
- do not turn finite regression into the all-prime proof.

BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.

## 5. Deterministic falsification/regression

The companion checker independently reconstructs the derivative jets c_k(0), c_k'(0), c_k''(0) modulo p^3 from the exact coefficient recurrence and reconstructs B_k directly from its source recurrence. For every target prime p<5000 (166 total, 83 in each residue class) it verifies with zero failures:

1. equation (3), the Z_T cutoff-jet bridge;
2. equation (4), the middle-band/first-derivative support identity;
3. equation (5), the high-band/second-derivative support identity;
4. equation (6), agreement of the cutoff decomposition with the global second digit.

This scan is falsification/regression only. The all-target proof is the exact Taylor/support argument in Sections 1-3.

## 6. Narrow next action

LIFT/JT2 remains open, but the source-bridge problem for Z_T is closed. The live scalar can now be attacked entirely inside the terminating cutoff jet

    [a_parent Psi-1]/p
      + a_parent H_1^{<=m}/6
      + Psi F_2^{<=2m}/72,

with the explicit correction target R_p-a_parent A-Psi Y.

Next derive a terminating contiguous/WZ or Frobenius identity for this cutoff jet. Any Frobenius formulation must be proved equal to (3), not introduced as a new coordinate. Do not differentiate the same evaluation adjoint again and do not reopen accepted D24 UR/JT0.
