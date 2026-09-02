import EnterpriseMath.Precision.TetrahedralResidual

namespace EnterpriseMath.PrecisionPi.TetrahedralResidual

/-- Pointwise difference of two six-line-family weight vectors. -/
def edgeSub (x y : EdgeWeights) : EdgeWeights := fun i => x i - y i

theorem matchingSums_edgeSub (x y : EdgeWeights) :
    matchingSums (edgeSub x y) =
      fun i => matchingSums x i - matchingSums y i := by
  funext i
  fin_cases i <;> simp [matchingSums, edgeSub] <;> ring

theorem edgeSum_edgeSub (x y : EdgeWeights) :
    edgeSum (edgeSub x y) = edgeSum x - edgeSum y := by
  simp [edgeSum, edgeSub]
  ring

theorem edgeSub_eq_kernelEdge_of_matchingSums_eq
    (x y : EdgeWeights) (hxy : matchingSums x = matchingSums y) :
    edgeSub x y = kernelEdge (x 0 - y 0) (x 1 - y 1) (x 2 - y 2) := by
  apply (matchingSums_eq_zero_iff (edgeSub x y)).mp
  rw [matchingSums_edgeSub]
  funext i
  have hi := congrFun hxy i
  simp [hi]

/-- The incidence map is injective on zero-sum integer slice potentials. -/
theorem delta_injective_on_zero_sum
    (v w : VertexWeights)
    (hv : vertexSum v = 0) (hw : vertexSum w = 0)
    (hdelta : delta v = delta w) :
    v = w := by
  have h0 := congrFun hdelta (0 : Fin 6)
  have h1 := congrFun hdelta (1 : Fin 6)
  have h2 := congrFun hdelta (2 : Fin 6)
  simp [delta] at h0 h1 h2
  dsimp [vertexSum] at hv hw
  funext i
  fin_cases i <;> omega

/-- Same `A₂` coordinate is liftable exactly when the parity difference is even. -/
theorem same_matching_liftable_iff_even_parity_difference
    (x y : EdgeWeights) (hxy : matchingSums x = matchingSums y) :
    (∃ v : VertexWeights,
        vertexSum v = 0 ∧ delta v = edgeSub x y) ↔
      Even ((x 0 + x 1 + x 2) - (y 0 + y 1 + y 2)) := by
  have hedge := edgeSub_eq_kernelEdge_of_matchingSums_eq x y hxy
  rw [hedge]
  have hbase := exists_zeroSum_delta_eq_kernelEdge_iff_even
    (x 0 - y 0) (x 1 - y 1) (x 2 - y 2)
  constructor
  · intro hlift
    have he := hbase.mp hlift
    convert he using 1 <;> ring
  · intro he
    apply hbase.mpr
    convert he using 1 <;> ring

/-- Same matching coordinate and even parity difference give a unique lift. -/
theorem existsUnique_zeroSum_lift_of_same_matching_even
    (x y : EdgeWeights)
    (hxy : matchingSums x = matchingSums y)
    (heven : Even ((x 0 + x 1 + x 2) - (y 0 + y 1 + y 2))) :
    ∃! v : VertexWeights, vertexSum v = 0 ∧ delta v = edgeSub x y := by
  have hex : ∃ v : VertexWeights, vertexSum v = 0 ∧ delta v = edgeSub x y :=
    (same_matching_liftable_iff_even_parity_difference x y hxy).2 heven
  rcases hex with ⟨v, hvsum, hvdelta⟩
  refine ⟨v, ⟨hvsum, hvdelta⟩, ?_⟩
  intro w hw
  exact delta_injective_on_zero_sum w v hw.1 hvsum (hw.2.trans hvdelta.symm)

/-- Odd parity difference is precisely the obstruction to a lift. -/
theorem no_lift_of_same_matching_odd
    (x y : EdgeWeights)
    (hxy : matchingSums x = matchingSums y)
    (hodd : ¬ Even ((x 0 + x 1 + x 2) - (y 0 + y 1 + y 2))) :
    ¬ ∃ v : VertexWeights, vertexSum v = 0 ∧ delta v = edgeSub x y := by
  intro h
  exact hodd ((same_matching_liftable_iff_even_parity_difference x y hxy).1 h)

end EnterpriseMath.PrecisionPi.TetrahedralResidual
