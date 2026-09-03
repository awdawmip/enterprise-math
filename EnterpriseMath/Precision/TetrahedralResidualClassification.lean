import EnterpriseMath.Precision.TetrahedralResidual

namespace EnterpriseMath.PrecisionPi.TetrahedralResidual

/-- Pointwise difference of two six-line-family weight vectors. -/
def edgeSub (x y : EdgeWeights) : EdgeWeights := fun i => x i - y i

/-- Opposite-pair coordinates commute with subtraction. -/
theorem matchingSums_edgeSub (x y : EdgeWeights) :
    matchingSums (edgeSub x y) =
      fun i => matchingSums x i - matchingSums y i := by
  funext i
  fin_cases i <;> simp [matchingSums, edgeSub] <;> ring

/-- Total edge weight commutes with subtraction. -/
theorem edgeSum_edgeSub (x y : EdgeWeights) :
    edgeSum (edgeSub x y) = edgeSum x - edgeSum y := by
  simp [edgeSum, edgeSub]
  ring

/-- Equal opposite-pair coordinates force the difference into kernel normal form. -/
theorem edgeSub_eq_kernelEdge_of_matchingSums_eq
    (x y : EdgeWeights) (hxy : matchingSums x = matchingSums y) :
    edgeSub x y = kernelEdge (x 0 - y 0) (x 1 - y 1) (x 2 - y 2) := by
  apply (matchingSums_eq_zero_iff (edgeSub x y)).mp
  rw [matchingSums_edgeSub]
  funext i
  have hi := congrFun hxy i
  simp [hi]

/-- The vertex-to-edge map is injective on zero-sum integer slice potentials. -/
theorem delta_injective_on_zero_sum
    (v w : VertexWeights)
    (hv : vertexSum v = 0) (hw : vertexSum w = 0)
    (hdelta : delta v = delta w) :
    v = w := by
  have h0 : v 0 + v 1 = w 0 + w 1 := by
    simpa [delta] using congrFun hdelta (0 : Fin 6)
  have h1 : v 0 + v 2 = w 0 + w 2 := by
    simpa [delta] using congrFun hdelta (1 : Fin 6)
  have h2 : v 0 + v 3 = w 0 + w 3 := by
    simpa [delta] using congrFun hdelta (2 : Fin 6)
  have hv' : v 0 + v 1 + v 2 + v 3 = 0 := by
    simpa [vertexSum] using hv
  have hw' : w 0 + w 1 + w 2 + w 3 = 0 := by
    simpa [vertexSum] using hw
  have hv0 : v 0 = w 0 := by
    linarith [h0, h1, h2, hv', hw']
  have hv1 : v 1 = w 1 := by
    linarith [h0, hv0]
  have hv2 : v 2 = w 2 := by
    linarith [h1, hv0]
  have hv3 : v 3 = w 3 := by
    linarith [h2, hv0]
  funext i
  fin_cases i
  · exact hv0
  · exact hv1
  · exact hv2
  · exact hv3

/--
Concrete quotient classification: among states with the same `A₂` matching
coordinate, equality modulo a zero-sum slice potential is exactly equality of
the residual parity class.
-/
theorem same_matching_liftable_iff_even_parity_difference
    (x y : EdgeWeights) (hxy : matchingSums x = matchingSums y) :
    (∃ v : VertexWeights,
        vertexSum v = 0 ∧ delta v = edgeSub x y) ↔
      Even ((x 0 + x 1 + x 2) - (y 0 + y 1 + y 2)) := by
  rw [edgeSub_eq_kernelEdge_of_matchingSums_eq x y hxy]
  have hrewrite :
      (x 0 - y 0) + (x 1 - y 1) + (x 2 - y 2) =
        (x 0 + x 1 + x 2) - (y 0 + y 1 + y 2) := by
    ring
  constructor
  · intro h
    have he := (exists_zeroSum_delta_eq_kernelEdge_iff_even
      (x 0 - y 0) (x 1 - y 1) (x 2 - y 2)).1 h
    rw [hrewrite] at he
    exact he
  · intro he
    apply (exists_zeroSum_delta_eq_kernelEdge_iff_even
      (x 0 - y 0) (x 1 - y 1) (x 2 - y 2)).2
    rw [hrewrite]
    exact he

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
  exact delta_injective_on_zero_sum w v hw.1 hvsum
    (hw.2.trans hvdelta.symm)

/-- Odd parity difference is precisely the obstruction to a slice-potential lift. -/
theorem no_lift_of_same_matching_odd
    (x y : EdgeWeights)
    (hxy : matchingSums x = matchingSums y)
    (hodd : ¬ Even ((x 0 + x 1 + x 2) - (y 0 + y 1 + y 2))) :
    ¬ ∃ v : VertexWeights, vertexSum v = 0 ∧ delta v = edgeSub x y := by
  intro h
  exact hodd
    ((same_matching_liftable_iff_even_parity_difference x y hxy).1 h)

end EnterpriseMath.PrecisionPi.TetrahedralResidual
