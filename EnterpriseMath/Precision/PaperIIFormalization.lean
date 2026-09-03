import EnterpriseMath.Geometry.FCCCarrierRotation
import EnterpriseMath.Geometry.FCCResidualBridge
import EnterpriseMath.Geometry.FCCResidualRotation
import EnterpriseMath.Geometry.FCCSliceAngles
import EnterpriseMath.Geometry.FCCSliceIncidence
import EnterpriseMath.Geometry.FCCSliceRotation
import EnterpriseMath.NumberTheory.DoublePellFusion
import EnterpriseMath.NumberTheory.TraceAntitrace
import EnterpriseMath.Precision.GeneratingLift
import EnterpriseMath.Precision.GeometricTailBound
import EnterpriseMath.Precision.N58RatioBound
import EnterpriseMath.Precision.PositiveSeriesAcceleration
import EnterpriseMath.Precision.TetrahedralMajorization
import EnterpriseMath.Precision.TetrahedralRationalSplitting
import EnterpriseMath.Precision.TetrahedralResidual
import EnterpriseMath.Precision.TetrahedralResidualClassification
import EnterpriseMath.Precision.TetrahedralResidualMetric
import EnterpriseMath.Precision.TetrahedralSmithCertificate

/-!
# Precision-pi paper II formalization root

This root collects the finite combinatorics, FCC carrier geometry,
rotation-equivariant `A₂ + C₂` residual structure, rational splitting,
Smith and Gram certificates, Pell/trace fourth-order fusion, finite generating
lift, positive reciprocal acceleration, and certified geometric-tail tools.

All geometry statements are carrier-level correspondences.  No theorem here
identifies an FCC carrier line family with a native P000 spatial axis.
-/
