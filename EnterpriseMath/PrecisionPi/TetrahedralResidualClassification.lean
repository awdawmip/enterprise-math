import EnterpriseMath.PrecisionPi.TetrahedralResidualCore

namespace EnterpriseMath.PrecisionPi.TetrahedralResidualClassification

open TetrahedralResidualCore

/-- Coordinatewise difference of six-edge variations. -/
def edgeSub (x y : EdgeChange) : EdgeChange :=
  ⟨x.e12 - y.e12, x.e13 - y.e13, x.e14 - y.e14,
    x.e23 - y.e23, x.e24 - y.e24, x.e34 - y.e34⟩

/-- Coordinatewise difference of matching residuals. -/
def matchingSub (m n : MatchingChange) : MatchingChange :=
  ⟨m.m1 - n.m1, m.m2 - n.m2, m.m3 - n.m3⟩

@[simp]
theorem matching_edgeSub (x y : EdgeChange) :
    matching (edgeSub x y) = matchingSub (matching x) (matching y) := by
  ext <;> simp [matching, edgeSub, matchingSub] <;> ring

@[simp]
theorem edgeTotal_edgeSub (x y : EdgeChange) :
    edgeTotal (edgeSub x y) = edgeTotal x - edgeTotal y := by
  simp [edgeTotal, edgeSub]
  ring

/-- The endpoint-sum map is injective over the integers. -/
theorem delta_injective : Function.Injective delta := by
  intro v w h
  have h12 : v.v1 + v.v2 = w.v1 + w.v2 := by
    simpa [delta] using congrArg EdgeChange.e12 h
  have h13 : v.v1 + v.v3 = w.v1 + w.v3 := by
    simpa [delta] using congrArg EdgeChange.e13 h
  have h14 : v.v1 + v.v4 = w.v1 + w.v4 := by
    simpa [delta] using congrArg EdgeChange.e14 h
  have h23 : v.v2 + v.v3 = w.v2 + w.v3 := by
    simpa [delta] using congrArg EdgeChange.e23 h
  ext <;> linarith

/-- Two edge configurations are equivalent when their difference is induced by
one balanced integral slice variation. -/
def BalancedEquivalent (x y : EdgeChange) : Prop :=
  ∃ v : VertexChange, vertexTotal v = 0 ∧ delta v = edgeSub x y

/-- Equal matching residuals force the edge difference into the parity fiber. -/
theorem matching_edgeSub_eq_zero_of_eq {x y : EdgeChange}
    (h : matching x = matching y) :
    matching (edgeSub x y) = zeroMatching := by
  rw [matching_edgeSub, h]
  ext <;> simp [matchingSub, zeroMatching]

/-- For configurations with the same free `A₂` residual, the remaining
obstruction to balanced equivalence is exactly one parity bit. -/
theorem balancedEquivalent_iff_parity_of_matching_eq {x y : EdgeChange}
    (h : matching x = matching y) :
    BalancedEquivalent x y ↔
      ∃ t : ℤ,
        (x.e12 - y.e12) + (x.e13 - y.e13) + (x.e14 - y.e14) = 2 * t := by
  unfold BalancedEquivalent
  simpa [edgeSub] using
    matching_zero_in_balanced_range_iff (edgeSub x y)
      (matching_edgeSub_eq_zero_of_eq h)

/-- The free matching residual is invariant under balanced slice changes. -/
theorem matching_invariant_of_balancedEquivalent {x y : EdgeChange}
    (h : BalancedEquivalent x y) : matching x = matching y := by
  rcases h with ⟨v, hv, hd⟩
  have hz : matching (edgeSub x y) = zeroMatching := by
    rw [← hd]
    exact matching_delta_of_balanced v hv
  have hs := matching_edgeSub x y
  rw [hs] at hz
  apply MatchingChange.ext
  · have := congrArg MatchingChange.m1 hz
    simp [matchingSub, zeroMatching] at this
    linarith
  · have := congrArg MatchingChange.m2 hz
    simp [matchingSub, zeroMatching] at this
    linarith
  · have := congrArg MatchingChange.m3 hz
    simp [matchingSub, zeroMatching] at this
    linarith

/-- A balanced equivalence between zero-matching shapes is completely
classified by the evenness of the sum of their first three edge coordinates. -/
theorem zero_matching_equivalence_classifier {x y : EdgeChange}
    (hx : matching x = zeroMatching) (hy : matching y = zeroMatching) :
    BalancedEquivalent x y ↔
      ∃ t : ℤ,
        (x.e12 - y.e12) + (x.e13 - y.e13) + (x.e14 - y.e14) = 2 * t := by
  apply balancedEquivalent_iff_parity_of_matching_eq
  rw [hx, hy]

end EnterpriseMath.PrecisionPi.TetrahedralResidualClassification
