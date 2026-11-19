# EC49FTM — exact joint law of the optimized q140 discount and BRC16943 exchange gap

**2026-11-19 · independent portable mathematical follow-up · AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED.**

**Frozen scientific input:** `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (310 configurations, 141 individually named profiles, 228 original-index observations). **Mathematical parents:** EC49FTH PR #2774 (`999bf1069403306b3813e0e390dae4435d7b4b8c`) for native Bellman optima, EC49FTK PR #2776 (`c8a24ab9f007c8d6348f45c60e9806c2fbfe238e`) for the unique optimizer, and EC49FTL PR #2779 (`e01a4fa023ffaabdf21fdbd640094bb8f011906f`) for separate marginal laws. This note derives the *joint* law. Native optimality inherits the parents' author-proof review status.

## Precisely typed question

The external price variables a and b are independently uniform over A=[3/4,49/64] and B=[7/16,57/128]. The q140 discount z is optimized over [11/16,3/4]. Let M=max_z(D-S) (normalized exchange-cost units) and Z=z_* (dimensionless discount). Randomness here is solely the external price-design measure, never the 141 response-profile frequencies or BRC branch multiplicities. No native observer quotient or input repin is performed.

The inherited exact premise on the full closed box is

    D = min(329-36a-68b-141z, 334-141a-62b-45z, 326-141a-47b-43z)
    S = 332-141a-8b-105z
    T(a,b) = (105a-6b-5)/96
    Z = min(3/4,T)
    a_c(b) = (77+6b)/105
    M = (525a-462b-9)/8   if a < a_c(b)
    M = 47-54b             if a >= a_c(b)

The formulas agree on the boundary. Throughout the external price rectangle, 11/16<T(a,b), so the optimizer lies in the allowed interval.

## Theorem 1: complete mixed-dimensional joint law

Let Omega consist of all (m,z) satisfying the inverse constraints

    a(m,z) = (47-m)/945 + (44/45)z
    b(m,z) = 1/27 - m/54 + (10/9)z
    3/4 <= a(m,z) <= a_c(b(m,z))
    7/16 <= b(m,z) <= 57/128
    z < 3/4.

Assignment of boundaries is immaterial for the two-dimensional density. For **every bounded measurable test function** phi(m,z), the joint pushforward is exactly

    E[phi(M,Z)]
      = (131072/945) * integral_Omega phi(m,z) dm dz
      + integral_[1469/64,187/8] [64(64m-1055)/25515] phi(m,3/4) dm.

The absolutely continuous interior component has mass **23/42**, and the singular line component at z=3/4 has mass **19/42**. Hence Z has an atom at 3/4, while M has no atom: the latter's singular joint component is spread continuously along m=47-54b.

**Proof.** On a<a_c(b), the map (a,b)->(M,Z) is nonsingular, with Jacobian

    J = det[[525/8,-231/4],[35/32,-1/16]] = 945/16.

Its inverse is displayed above. The uniform source rectangle has density 1/((1/64)(1/128))=8192, so the interior density is 8192/J=131072/945 on Omega. On a>=a_c(b), Z=3/4 and M=47-54b. Integrate each uniform a-fiber and substitute b=(47-m)/54 to obtain

    dP_singular/dm = (8192/54)*(49/64-a_c((47-m)/54))
                   = 64(64m-1055)/25515,

on the interval [47-54(57/128),47-54(7/16)]=[1469/64,187/8]. Its exact integral is 19/42. The complementary probability is 23/42. The identity holds for any bounded measurable phi by the ordinary change-of-variables formula and one-dimensional pushforward on the clipped region.

## Theorem 2: exact joint dependence

The following new cross-moment, covariance and correlation are exact:

    E[M Z]      = 13634293007/792723456
    Cov(M,Z)    = 1329833/2312110080 > 0
    Corr(M,Z)^2 = 1768455807889/2515608496192
    Corr(M,Z)   > 0 (approximately 0.8384469310).

Conditional means separate the two mechanisms:

    E[M | Z=3/4] = 140851/6080
    E[M | Z<3/4] = 1347257/58880.

**Proof.** On a<a_c(b), multiply the affine functions ((525a-462b-9)/8)*((105a-6b-5)/96). On a>=a_c(b), multiply (47-54b)*(3/4). Integrate each polynomial on the exact split rectangle and divide by area 1/8192. This yields E[MZ]. Subtract E[M]E[Z] using E[M]=494813/21504 and E[Z]=964373/1290240, both independently recomputed by the attached checker. The checked variances Var(M)=60097/1204224 and Var(Z)=654049/69363302400 yield the stated correlation squared. Divide restricted first moments by their component masses for the conditional means.

## Theorem 3: clipping probability conditional on achieved gap

Put m2=1469/64 and m3=187/8. For almost every m in the support of M, the regular conditional probability obeys

    P(Z=3/4 | M=m) = 0,                                  if m < m2;
    P(Z=3/4 | M=m) = 5(64m-1055)/(102437-4288m),          if m2 < m < m3.

The right limit at m2 is **115/223**; the left limit at m3 is **1**. Pointwise endpoint versions may be assigned by those limits.

**Proof.** Divide Theorem 1's singular line density by the marginal density f_M(m) given in EC49FTL. For m2<m<m3 the marginal density is (6555968-274432m)/127575. The ratio simplifies to the stated function. The singular line contributes no probability below m2. This explains the upper-region density jump without introducing an atom into M.

## Exact verification and limitations

`EC49FTM_JOINT_LAW_VERIFY.py` is a standalone pure-Python `fractions.Fraction` checker. It integrates polynomial monomials across the rational split a=a_c(b); checks joint moments, component masses, affine Jacobian and conditional endpoints; and tests the inverse map at 31x31 exact rational grid points (961 cases). `EC49FTM_JOINT_LAW_CERT.json` captures the actual computation. Run with `python3 EC49FTM_JOINT_LAW_VERIFY.py` without downloading datasets. The analytic pushforward proof establishes the universal measure identity; finite checks are regression evidence.

This is a new theorem on exactly specified **parent affine observables**, conditional for native Bellman semantics on the source-backed but unreviewed parent. No 228-observer native Bellman rerun, formal Result/Review/CLAIM, Activity mutation, owner change, source repin, P000 modification or physical-state probability interpretation is asserted.

**Next questions:** derive the full conditional distribution of Z given M=m (continuous conditional density plus clipping atom) and the monotonicity of its conditional mean; test the mixed-dimensional law in an independently verified native region below z=11/16; consider typed nonuniform external-price designs and whether the clipping mass increases or decreases.
