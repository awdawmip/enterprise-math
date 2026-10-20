import EnterpriseMath.Precision.TetrahedralResidual

namespace EnterpriseMath.PrecisionPi.TetrahedralResidual

/-- Pointwise difference of two six-line-family weight vectors. -/
def edgeSub (x y : EdgeWeights) : EdgeWeights := fun i => x i - y i

/-- Kernel normal forms are closed under pointwise subtraction. -/
theorem kernelEdge_sub (a b c a' b' c' : ℤ) :
    edgeSub (kernelEdge a b c) (kernelEdge a' b' c') =
      kernelEdge (a - a') (b - b') (c - c') := by
  funext i
  fin_cases i <;> simp [edgeSub, kernelEdge]

/--
Two matching-zero residual representatives differ by an integral zero-sum
slice potential exactly when the difference of their parity sums is even.
This is the concrete `C₂` coset-classification statement.
-/
theorem kernelEdge_difference_liftable_iff_even
    (a b c a' b' c' : ℤ) :
    (∃ v : VertexWeights,
        vertexSum v = 0 ∧
          delta v = edgeSub (kernelEdge a b c) (kernelEdge a' b' c')) ↔
      Even ((a + b + c) - (a' + b' + c')) := by
  rw [kernelEdge_sub]
  constructor
  · intro h
    have he :=
      (exists_zeroSum_delta_eq_kernelEdge_iff_even
        (a - a') (b - b') (c - c')).mp h
    simpa only [sub_add_sub_comm, sub_eq_add_neg] using he
  · intro he
    apply
      (exists_zeroSum_delta_eq_kernelEdge_iff_even
        (a - a') (b - b') (c - c')).mpr
    rcases he with ⟨t, ht⟩
    refine ⟨t, ?_⟩
    omega

/-- Every doubled matching-zero kernel residual is slice-induced. -/
theorem doubled_kernelEdge_liftable (a b c : ℤ) :
    ∃ v : VertexWeights,
        vertexSum v = 0 ∧ delta v = kernelEdge (2 * a) (2 * b) (2 * c) := by
  apply
    (exists_zeroSum_delta_eq_kernelEdge_iff_even
      (2 * a) (2 * b) (2 * c)).mpr
  refine ⟨a + b + c, ?_⟩
  ring

/--
The basic nonzero parity representative becomes trivial after doubling,
which is the exact order-two statement required by the paper.
-/
theorem basicParityClass_exact_order_two :
    (¬ ∃ v : VertexWeights,
        vertexSum v = 0 ∧ delta v = kernelEdge 1 0 0) ∧
      (∃ v : VertexWeights,
        vertexSum v = 0 ∧ delta v = kernelEdge 2 0 0) := by
  exact ⟨basicParityClass_not_liftable, twice_basicParityClass_liftable⟩

end EnterpriseMath.PrecisionPi.TetrahedralResidual
