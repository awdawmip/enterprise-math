import EnterpriseMath.Geometry.FCCSliceIncidence
import EnterpriseMath.Geometry.FCCOrientedSlices
import EnterpriseMath.Geometry.TetrahedralResidualParity
import EnterpriseMath.Geometry.TetrahedralResidualKernel
import EnterpriseMath.Geometry.TetrahedralResidualClassification
import EnterpriseMath.Geometry.TetrahedralResidualInvariant
import EnterpriseMath.Geometry.TetrahedralResidualFreeA2
import EnterpriseMath.Geometry.TetrahedralResidualRationalLift
import EnterpriseMath.PrecisionPi.SquareTraceDoublePell
import EnterpriseMath.PrecisionPi.MajorizationCore
import EnterpriseMath.PrecisionPi.TetrahedralWallisRatio
import EnterpriseMath.PrecisionPi.Ramanujan58RatioBound

/-!
# Precision-pi paper II formalization entry point

This module collects the formalized algebraic and finite-geometric layer used
by the second precision-pi manuscript:

* the FCC four-slice/six-line `K₄` carrier incidence;
* integral `120°` certificates for each three-line slice;
* the free `A₂` residual coordinate and its parity obstruction;
* disappearance of the parity obstruction after rational scalar extension;
* square-half-trace units produced by paired positive/negative Pell shells;
* finite prefix-gap certificates for the Gamma-majorization argument;
* strict contraction of the tetrahedral Wallis blocks;
* an explicit geometric ratio bound for the positive `N=58` Ramanujan terms.

All statements are carrier-level or algebraic.  No theorem in this module
identifies an FCC carrier line with a native P000 axis, and no analytic
Ramanujan identity is introduced as an axiom.
-/
