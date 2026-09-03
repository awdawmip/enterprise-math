import EnterpriseMath.Geometry.FCCResidualBridge
import EnterpriseMath.Geometry.FCCSliceIncidence
import EnterpriseMath.NumberTheory.DoublePellFusion
import EnterpriseMath.Precision.GeometricTailBound
import EnterpriseMath.Precision.PositiveSeriesAcceleration
import EnterpriseMath.Precision.TetrahedralMajorization
import EnterpriseMath.Precision.TetrahedralResidual
import EnterpriseMath.Precision.TetrahedralResidualClassification
import EnterpriseMath.Precision.TetrahedralSmithCertificate

/-!
# Precision-pi paper II formalization surface

This module aggregates the finite carrier geometry, integer residual
classification, Pell-shell arithmetic, majorization certificate, positive
reciprocal acceleration, and geometric tail-bound lemmas used by the proposed
second paper.

The FCC results are explicitly carrier-level.  No statement in this module
identifies a carrier line family with a native P000 spatial axis.
-/
