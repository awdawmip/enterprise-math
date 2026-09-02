import EnterpriseMath.Geometry.TetrahedralResidualParity

namespace EnterpriseMath.TetrahedralResidual

/-- Vanishing opposite-pair sums are equivalent to the three-parameter kernel
normal form. -/
theorem matchingSums_eq_zero_iff_kernelEdge (x : Edge6) :
    matchingSums x = 0 ↔ ∃ a b c : ℤ, x = kernelEdge a b c := by
  constructor
  · intro h
    have h0 := congrFun h (0 : Fin 3)
    have h1 := congrFun h (1 : Fin 3)
    have h2 := congrFun h (2 : Fin 3)
    simp [matchingSums] at h0 h1 h2
    refine ⟨x 0, x 1, x 2, ?_⟩
    funext i
    fin_cases i <;> simp [kernelEdge] <;> linarith
  · rintro ⟨a, b, c, rfl⟩
    exact matchingSums_kernelEdge a b c

/-- Any zero-sum slice potential induces an edge whose first three
coordinates have even sum. -/
theorem even_firstThree_of_zeroSum_preimage (x : Edge6)
    (h : ∃ v : Vertex4, vertexSum v = 0 ∧ delta v = x) :
    Even (x 0 + x 1 + x 2) := by
  rcases h with ⟨v, hv, rfl⟩
  have hv' : v 0 + v 1 + v 2 + v 3 = 0 := by
    simpa [vertexSum] using hv
  refine ⟨v 0, ?_⟩
  change
    (v 0 + v 1) + (v 0 + v 2) + (v 0 + v 3) =
      v 0 + v 0
  omega

/-- On the opposite-pair kernel, the parity test is complete: it is the only
obstruction to an integral zero-sum slice potential. -/
theorem kernel_preimage_iff_even_firstThree (x : Edge6)
    (hkernel : matchingSums x = 0) :
    (∃ v : Vertex4, vertexSum v = 0 ∧ delta v = x) ↔
      Even (x 0 + x 1 + x 2) := by
  rcases (matchingSums_eq_zero_iff_kernelEdge x).1 hkernel with ⟨a, b, c, rfl⟩
  simpa [HasZeroSumPreimage, kernelEdge] using
    (hasZeroSumPreimage_iff_even a b c)

/-- A distinguished representative of the nonzero parity obstruction. -/
def primitiveParityEdge : Edge6 := kernelEdge 1 0 0

/-- The distinguished representative lies in the opposite-pair kernel. -/
theorem primitiveParityEdge_in_kernel :
    matchingSums primitiveParityEdge = 0 := by
  exact matchingSums_kernelEdge 1 0 0

/-- The distinguished representative has no integral zero-sum slice lift. -/
theorem primitiveParityEdge_not_in_delta :
    ¬ ∃ v : Vertex4, vertexSum v = 0 ∧ delta v = primitiveParityEdge := by
  simpa [primitiveParityEdge, HasZeroSumPreimage] using primitiveParity_noPreimage

/-- Coordinatewise doubling on edge data. -/
def doubleEdge (x : Edge6) : Edge6 := fun i => 2 * x i

/-- Doubling the primitive obstruction gives the even kernel normal form. -/
theorem double_primitiveParityEdge :
    doubleEdge primitiveParityEdge = kernelEdge 2 0 0 := by
  funext i
  fin_cases i <;> norm_num [doubleEdge, primitiveParityEdge, kernelEdge]

/-- The doubled primitive obstruction has an explicit integral zero-sum
slice lift. -/
theorem double_primitiveParityEdge_in_delta :
    ∃ v : Vertex4,
      vertexSum v = 0 ∧ delta v = doubleEdge primitiveParityEdge := by
  rw [double_primitiveParityEdge]
  exact doublePrimitiveParity_hasPreimage

end EnterpriseMath.TetrahedralResidual
