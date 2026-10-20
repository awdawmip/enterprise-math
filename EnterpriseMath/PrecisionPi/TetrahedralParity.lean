import EnterpriseMath.PrecisionPi.TetrahedralMatching
import Mathlib.Data.ZMod.Basic

namespace EnterpriseMath.PrecisionPi.TetrahedralParity

open TetrahedralResidual TetrahedralMatching

/-- Integer residual coordinate complementary to the chosen matching lift. -/
def residualSum (x : EdgeData) : ℤ :=
  -x.e34 - x.e24 - x.e23

/-- The surviving integral parity bit. -/
def residualParity (x : EdgeData) : ZMod 2 :=
  (residualSum x : ZMod 2)

@[simp] theorem residualSum_edgePattern (a b c : ℤ) :
    residualSum (edgePattern a b c) = a + b + c := by
  simp [residualSum, edgePattern]
  ring

/-- On a zero-sum slice potential, the residual sum is twice the first slice coordinate. -/
theorem residualSum_delta_of_vertexSum_zero
    {v : VertexData} (hv : vertexSum v = 0) :
    residualSum (delta v) = 2 * v.v1 := by
  have hv' := hv
  simp [vertexSum] at hv'
  simp [residualSum, delta]
  omega

/-- Hence every zero-sum slice-induced fluctuation has trivial `C₂` parity. -/
theorem residualParity_delta_of_vertexSum_zero
    {v : VertexData} (hv : vertexSum v = 0) :
    residualParity (delta v) = 0 := by
  rw [residualParity, residualSum_delta_of_vertexSum_zero hv]
  push_cast
  norm_num

/-- The residual sum is additive. -/
theorem residualSum_edgeAdd (x y : EdgeData) :
    residualSum (edgeAdd x y) = residualSum x + residualSum y := by
  simp [residualSum, edgeAdd]
  ring

/-- The `C₂` residual is additive. -/
theorem residualParity_edgeAdd (x y : EdgeData) :
    residualParity (edgeAdd x y) = residualParity x + residualParity y := by
  simp [residualParity, residualSum_edgeAdd]

/-- Adding a zero-sum slice potential cannot change the parity bit. -/
theorem residualParity_edgeAdd_delta
    (x : EdgeData) {v : VertexData} (hv : vertexSum v = 0) :
    residualParity (edgeAdd x (delta v)) = residualParity x := by
  rw [residualParity_edgeAdd,
    residualParity_delta_of_vertexSum_zero hv, add_zero]

/-- The basic opposite-edge difference carries the nonzero `C₂` value. -/
theorem basic_parity_value :
    residualParity (edgePattern 1 0 0) = 1 := by
  norm_num [residualParity]

/-- Every doubled kernel pattern has trivial parity. -/
theorem doubled_edgePattern_parity_zero (a b c : ℤ) :
    residualParity (edgePattern (2 * a) (2 * b) (2 * c)) = 0 := by
  simp [residualParity]
  push_cast
  norm_num

/-- Membership in the zero-sum slice image forces trivial parity. -/
theorem residualParity_eq_zero_of_mem_zeroSum_delta
    {x : EdgeData}
    (h : ∃ v : VertexData, vertexSum v = 0 ∧ delta v = x) :
    residualParity x = 0 := by
  rcases h with ⟨v, hv, rfl⟩
  exact residualParity_delta_of_vertexSum_zero hv

/-- The basic class is detected simultaneously by non-membership and nonzero parity. -/
theorem basic_class_certificate :
    (¬ ∃ v : VertexData,
      vertexSum v = 0 ∧ delta v = edgePattern 1 0 0) ∧
      residualParity (edgePattern 1 0 0) = 1 := by
  exact ⟨basic_parity_class_not_mem, basic_parity_value⟩

/-- Its double is in the slice image and has zero parity. -/
theorem twice_basic_class_certificate :
    (∃ v : VertexData,
      vertexSum v = 0 ∧ delta v = edgePattern 2 0 0) ∧
      residualParity (edgePattern 2 0 0) = 0 := by
  refine ⟨twice_basic_parity_class_mem, ?_⟩
  simpa using doubled_edgePattern_parity_zero 1 0 0

end EnterpriseMath.PrecisionPi.TetrahedralParity
