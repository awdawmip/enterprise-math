import EnterpriseMath.PrecisionPi.EnterpriseCoordinateRotation
import EnterpriseMath.PrecisionPi.TetrahedralNormalForm

namespace EnterpriseMath.PrecisionPi.EnterpriseCoordinateResidualBridge

open EnterpriseCoordinateIncidence EnterpriseCoordinateK4
  EnterpriseCoordinateRotation
open TetrahedralResidual TetrahedralMatching TetrahedralParity
  TetrahedralCosets TetrahedralNormalForm

/-- Read one of the four slice coordinates. -/
def sliceValue (v : VertexData) : SliceChart → ℤ
  | .A => v.v1
  | .B => v.v2
  | .C => v.v3
  | .D => v.v4

/-- Bind the six FCC line-family labels to the six `K₄` edge coordinates. -/
def lineValue (x : EdgeData) : LineFamily → ℤ
  | .L1 => x.e12
  | .L2 => x.e34
  | .L3 => x.e13
  | .L4 => x.e24
  | .L5 => x.e23
  | .L6 => x.e14

/-- The explicit line labels reproduce the `K₄` edge table. -/
theorem lineValue_edge_table (x : EdgeData) :
    lineValue x .L1 = x.e12 ∧
    lineValue x .L3 = x.e13 ∧
    lineValue x .L6 = x.e14 ∧
    lineValue x .L5 = x.e23 ∧
    lineValue x .L4 = x.e24 ∧
    lineValue x .L2 = x.e34 := by
  rfl

/-- Every induced line value is the sum of its two incident slice values. -/
theorem lineValue_delta_eq_incident_slice_sum
    (v : VertexData) (l : LineFamily) :
    lineValue (delta v) l =
      ∑ s in incidentSlices l, sliceValue v s := by
  fin_cases l <;>
    simp [lineValue, delta, incidentSlices, sliceLines, sliceValue] <;> ring

/-- The three matching coordinates are the three opposite-line-pair sums
`(L1,L2)`, `(L3,L4)`, and `(L6,L5)`. -/
theorem matching_eq_opposite_line_sums (x : EdgeData) :
    matching x =
      ⟨lineValue x .L1 + lineValue x .L2,
       lineValue x .L3 + lineValue x .L4,
       lineValue x .L6 + lineValue x .L5⟩ := by
  rfl

/-- A zero-sum slice potential contributes zero to each opposite-line-pair sum. -/
theorem opposite_line_sums_delta_zero
    {v : VertexData} (hv : vertexSum v = 0) :
    lineValue (delta v) .L1 + lineValue (delta v) .L2 = 0 ∧
    lineValue (delta v) .L3 + lineValue (delta v) .L4 = 0 ∧
    lineValue (delta v) .L6 + lineValue (delta v) .L5 = 0 := by
  have hm := matching_delta_of_vertexSum_zero hv
  have h1 := congrArg MatchingData.m1 hm
  have h2 := congrArg MatchingData.m2 hm
  have h3 := congrArg MatchingData.m3 hm
  simpa [matching_eq_opposite_line_sums] using And.intro h1 (And.intro h2 h3)

/-- The carrier-labelled matching coordinate is invariant under a zero-sum slice update. -/
theorem opposite_line_coordinate_invariant
    (x : EdgeData) {v : VertexData} (hv : vertexSum v = 0) :
    matching (edgeAdd x (delta v)) = matching x :=
  matching_edgeAdd_delta_zero x hv

/-- Every balanced carrier-line state has a unique `ℤ² × C₂` normal-form coordinate. -/
theorem balanced_carrier_state_normal_form :
    (∀ x : EdgeData, edgeSum x = 0 →
      ∃ p q : ℤ, ∃ ε : Bool,
        DeltaEquivalent x (normalRepresentative p q ε)) ∧
    (∀ p q p' q' : ℤ, ∀ ε ε' : Bool,
      DeltaEquivalent
        (normalRepresentative p q ε)
        (normalRepresentative p' q' ε') →
      p = p' ∧ q = q' ∧ ε = ε') :=
  zeroSum_normal_form_classification

end EnterpriseMath.PrecisionPi.EnterpriseCoordinateResidualBridge
