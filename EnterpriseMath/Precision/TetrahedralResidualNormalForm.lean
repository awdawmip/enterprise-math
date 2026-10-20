import EnterpriseMath.Precision.TetrahedralResidualClassification

namespace EnterpriseMath.PrecisionPi.TetrahedralResidual

/-- Pointwise addition of six-edge weights. -/
def edgeAdd (x y : EdgeWeights) : EdgeWeights := fun i => x i + y i

/-- The integer parity expression representing the intrinsic `C₂` coordinate. -/
def parityExpression (x : EdgeWeights) : ℤ := x 0 + x 1 + x 2

/-- Canonical even representative over an `A₂` matching coordinate. -/
def canonicalEvenLift (m : MatchingWeights) : EdgeWeights :=
  ![m 0, m 1, m 2, 0, 0, 0]

/-- Canonical odd representative obtained by adding the basic parity kernel class. -/
def canonicalOddLift (m : MatchingWeights) : EdgeWeights :=
  edgeAdd (canonicalEvenLift m) (kernelEdge 1 0 0)

/-- The canonical even representative has the prescribed matching coordinate. -/
theorem matchingSums_canonicalEvenLift (m : MatchingWeights) :
    matchingSums (canonicalEvenLift m) = m := by
  funext i
  fin_cases i <;> simp [matchingSums, canonicalEvenLift]

/-- The canonical odd representative has the same matching coordinate. -/
theorem matchingSums_edgeAdd (x y : EdgeWeights) :
    matchingSums (edgeAdd x y) =
      fun i => matchingSums x i + matchingSums y i := by
  funext i
  fin_cases i <;> simp [matchingSums, edgeAdd] <;> ring

theorem matchingSums_canonicalOddLift (m : MatchingWeights) :
    matchingSums (canonicalOddLift m) = m := by
  rw [canonicalOddLift, matchingSums_edgeAdd]
  funext i
  rw [matchingSums_canonicalEvenLift]
  simp [matchingSums_kernelEdge]

/-- Their total edge weights both equal the total matching weight. -/
theorem edgeSum_canonicalEvenLift (m : MatchingWeights) :
    edgeSum (canonicalEvenLift m) = m 0 + m 1 + m 2 := by
  simp [edgeSum, canonicalEvenLift]
  ring

theorem edgeSum_edgeAdd (x y : EdgeWeights) :
    edgeSum (edgeAdd x y) = edgeSum x + edgeSum y := by
  simp [edgeSum, edgeAdd]
  ring

theorem edgeSum_canonicalOddLift (m : MatchingWeights) :
    edgeSum (canonicalOddLift m) = m 0 + m 1 + m 2 := by
  rw [canonicalOddLift, edgeSum_edgeAdd,
    edgeSum_canonicalEvenLift, edgeSum_kernelEdge]
  ring

/-- Exact parity values of the two canonical representatives. -/
theorem parityExpression_canonicalEvenLift (m : MatchingWeights) :
    parityExpression (canonicalEvenLift m) = m 0 + m 1 + m 2 := by
  simp [parityExpression, canonicalEvenLift]
  ring

theorem parityExpression_canonicalOddLift (m : MatchingWeights) :
    parityExpression (canonicalOddLift m) = m 0 + m 1 + m 2 + 1 := by
  simp [parityExpression, canonicalOddLift, edgeAdd,
    canonicalEvenLift, kernelEdge]
  ring

/-- Every even representative over `m` has a unique zero-sum slice-potential lift. -/
theorem even_normal_form_unique
    (x : EdgeWeights) (m : MatchingWeights)
    (hxmatch : matchingSums x = m)
    (hm : m 0 + m 1 + m 2 = 0)
    (heven : Even (parityExpression x)) :
    ∃! v : VertexWeights,
      vertexSum v = 0 ∧ delta v = edgeSub x (canonicalEvenLift m) := by
  have hmatch : matchingSums x = matchingSums (canonicalEvenLift m) := by
    rw [hxmatch, matchingSums_canonicalEvenLift]
  apply existsUnique_zeroSum_lift_of_same_matching_even x (canonicalEvenLift m) hmatch
  rw [parityExpression_canonicalEvenLift, hm]
  simpa [parityExpression] using heven

/-- Every odd representative over `m` has a unique zero-sum lift to the odd normal form. -/
theorem odd_normal_form_unique
    (x : EdgeWeights) (m : MatchingWeights)
    (hxmatch : matchingSums x = m)
    (hm : m 0 + m 1 + m 2 = 0)
    (hodd : Odd (parityExpression x)) :
    ∃! v : VertexWeights,
      vertexSum v = 0 ∧ delta v = edgeSub x (canonicalOddLift m) := by
  have hmatch : matchingSums x = matchingSums (canonicalOddLift m) := by
    rw [hxmatch, matchingSums_canonicalOddLift]
  apply existsUnique_zeroSum_lift_of_same_matching_even x (canonicalOddLift m) hmatch
  rw [parityExpression_canonicalOddLift, hm]
  rcases hodd with ⟨k, hk⟩
  refine ⟨k, ?_⟩
  dsimp [parityExpression] at hk ⊢
  omega

/-- The two canonical lifts lie in distinct slice-potential classes. -/
theorem canonicalOdd_not_congruent_canonicalEven
    (m : MatchingWeights) (hm : m 0 + m 1 + m 2 = 0) :
    ¬ ∃ v : VertexWeights,
      vertexSum v = 0 ∧
        delta v = edgeSub (canonicalOddLift m) (canonicalEvenLift m) := by
  have hmatch :
      matchingSums (canonicalOddLift m) = matchingSums (canonicalEvenLift m) := by
    rw [matchingSums_canonicalOddLift, matchingSums_canonicalEvenLift]
  apply no_lift_of_same_matching_odd
    (canonicalOddLift m) (canonicalEvenLift m) hmatch
  rw [parityExpression_canonicalOddLift,
    parityExpression_canonicalEvenLift, hm]
  norm_num

/-- Adding the basic parity class toggles the parity expression by one. -/
theorem parity_toggle (x : EdgeWeights) :
    parityExpression (edgeAdd x (kernelEdge 1 0 0)) = parityExpression x + 1 := by
  simp [parityExpression, edgeAdd, kernelEdge]
  ring

end EnterpriseMath.PrecisionPi.TetrahedralResidual
