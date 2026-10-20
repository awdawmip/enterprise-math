import EnterpriseMath.Geometry.FCCCarrierRotation
import EnterpriseMath.Geometry.FCCResidualBridge
import EnterpriseMath.Geometry.FCCResidualRotation
import EnterpriseMath.Geometry.FCCSliceAngles
import EnterpriseMath.Geometry.FCCSliceIncidence
import EnterpriseMath.Geometry.FCCSliceRotation
import EnterpriseMath.NumberTheory.DoublePellFusion
import EnterpriseMath.NumberTheory.TraceAntitrace
import EnterpriseMath.Precision.GeneralMajorizationArithmetic
import EnterpriseMath.Precision.GeneratingLift
import EnterpriseMath.Precision.GeometricTailBound
import EnterpriseMath.Precision.N58RatioBound
import EnterpriseMath.Precision.PositiveSeriesAcceleration
import EnterpriseMath.Precision.TetrahedralMajorization
import EnterpriseMath.Precision.TetrahedralRationalSplittingChecked
import EnterpriseMath.Precision.TetrahedralResidual
import EnterpriseMath.Precision.TetrahedralResidualClassification
import EnterpriseMath.Precision.TetrahedralResidualMetric
import EnterpriseMath.Precision.TetrahedralSmithCertificate

/-!
# Checked precision-pi formalization root

This root collects the formalized finite combinatorics, FCC carrier geometry,
rotation-equivariant residual structure, `A₂ + C₂` classification,
rational splitting, determinant certificates, Pell-shell fusion, finite
generating lift, positive reciprocal acceleration, and geometric tail bounds.

All geometry statements are carrier-level correspondences.  No theorem here
identifies FCC line families with the native P000 axes.
-/
