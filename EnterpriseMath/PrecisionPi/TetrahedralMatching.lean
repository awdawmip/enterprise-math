import EnterpriseMath.PrecisionPi.TetrahedralResidual

namespace EnterpriseMath.PrecisionPi.TetrahedralMatching

open TetrahedralResidual

/-- Coordinatewise addition of edge data. -/
def edgeAdd (x y : EdgeData) : EdgeData where
  e12 := x.e12 + y.e12
  e13 := x.e13 + y.e13
  e14 := x.e14 + y.e14
  e23 := x.e23 + y.e23
  e24 := x.e24 + y.e24
  e34 := x.e34 + y.e34

@[simp] theorem edgeAdd_e12 (x y : EdgeData) : (edgeAdd x y).e12 = x.e12 + y.e12 := rfl
@[simp] theorem edgeAdd_e13 (x y : EdgeData) : (edgeAdd x y).e13 = x.e13 + y.e13 := rfl
@[simp] theorem edgeAdd_e14 (x y : EdgeData) : (edgeAdd x y).e14 = x.e14 + y.e14 := rfl
@[simp] theorem edgeAdd_e23 (x y : EdgeData) : (edgeAdd x y).e23 = x.e23 + y.e23 := rfl
@[simp] theorem edgeAdd_e24 (x y : EdgeData) : (edgeAdd x y).e24 = x.e24 + y.e24 := rfl
@[simp] theorem edgeAdd_e34 (x y : EdgeData) : (edgeAdd x y).e34 = x.e34 + y.e34 := rfl

/-- The perfect-matching readout is additive. -/
theorem matching_edgeAdd (x y : EdgeData) :
    matching (edgeAdd x y) =
      ⟨(matching x).m1 + (matching y).m1,
       (matching x).m2 + (matching y).m2,
       (matching x).m3 + (matching y).m3⟩ := by
  ext <;> simp [matching, edgeAdd] <;> ring

/-- A section of the perfect-matching readout. -/
def matchingLift (m : MatchingData) : EdgeData where
  e12 := m.m1
  e13 := m.m2
  e14 := m.m3
  e23 := 0
  e24 := 0
  e34 := 0

@[simp] theorem matching_matchingLift (m : MatchingData) :
    matching (matchingLift m) = m := by
  ext <;> simp [matching, matchingLift]

@[simp] theorem edgeSum_matchingLift (m : MatchingData) :
    edgeSum (matchingLift m) = m.m1 + m.m2 + m.m3 := by
  simp [edgeSum, matchingLift]

/-- Every balanced matching coordinate has a zero-sum edge lift. -/
theorem matching_surjective_on_zero_sum
    (m : MatchingData) (hm : m.m1 + m.m2 + m.m3 = 0) :
    ∃ x : EdgeData, edgeSum x = 0 ∧ matching x = m := by
  refine ⟨matchingLift m, ?_, matching_matchingLift m⟩
  simpa using hm

/-- Standard two-coordinate parametrization of the `A₂` matching lattice. -/
def a2Matching (p q : ℤ) : MatchingData :=
  ⟨p, q, -p - q⟩

@[simp] theorem a2Matching_balanced (p q : ℤ) :
    (a2Matching p q).m1 + (a2Matching p q).m2 + (a2Matching p q).m3 = 0 := by
  simp [a2Matching]

/-- Every balanced matching triple is uniquely determined by its first two coordinates. -/
theorem balanced_matching_eq_a2
    (m : MatchingData) (hm : m.m1 + m.m2 + m.m3 = 0) :
    m = a2Matching m.m1 m.m2 := by
  ext <;> simp [a2Matching] <;> omega

/-- Zero-sum vertex potentials have vanishing perfect-matching readout. -/
theorem matching_delta_of_vertexSum_zero
    {v : VertexData} (hv : vertexSum v = 0) :
    matching (delta v) = ⟨0, 0, 0⟩ := by
  have hv' := hv
  simp [vertexSum] at hv'
  ext <;> simp [matching, delta] <;> omega

/-- Every edge datum is the sum of its matching lift and a canonical kernel pattern. -/
theorem edge_eq_matchingLift_add_pattern (x : EdgeData) :
    x = edgeAdd (matchingLift (matching x))
      (edgePattern (-x.e34) (-x.e24) (-x.e23)) := by
  ext <;> simp [edgeAdd, matchingLift, matching, edgePattern] <;> ring

/-- A zero-sum edge fluctuation decomposes into an `A₂` matching coordinate and a kernel pattern. -/
theorem zeroSum_edge_decomposition
    (x : EdgeData) (hx : edgeSum x = 0) :
    ∃ p q : ℤ,
      matching x = a2Matching p q ∧
      x = edgeAdd (matchingLift (a2Matching p q))
        (edgePattern (-x.e34) (-x.e24) (-x.e23)) := by
  have hm : (matching x).m1 + (matching x).m2 + (matching x).m3 = 0 := by
    rw [matching_total]
    exact hx
  refine ⟨(matching x).m1, (matching x).m2,
    balanced_matching_eq_a2 (matching x) hm, ?_⟩
  rw [← balanced_matching_eq_a2 (matching x) hm]
  exact edge_eq_matchingLift_add_pattern x

/-- The free matching coordinate is unaffected by adding a zero-sum slice-induced fluctuation. -/
theorem matching_edgeAdd_delta_zero
    (x : EdgeData) {v : VertexData} (hv : vertexSum v = 0) :
    matching (edgeAdd x (delta v)) = matching x := by
  rw [matching_edgeAdd, matching_delta_of_vertexSum_zero hv]
  ext <;> simp

end EnterpriseMath.PrecisionPi.TetrahedralMatching
