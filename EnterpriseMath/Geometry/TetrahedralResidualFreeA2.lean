import EnterpriseMath.Geometry.TetrahedralResidualClassification

namespace EnterpriseMath.TetrahedralResidual

/-- A simple edge lift of three opposite-pair coordinates. -/
def matchingLift (m : Fin 3 → ℤ) : Edge6 :=
  ![m 0, m 1, m 2, 0, 0, 0]

/-- The simple lift realizes the prescribed opposite-pair coordinates. -/
theorem matchingSums_matchingLift (m : Fin 3 → ℤ) :
    matchingSums (matchingLift m) = m := by
  funext i
  fin_cases i <;> simp [matchingSums, matchingLift]

/-- The total edge weight of the simple lift is the sum of its three
matching coordinates. -/
theorem edgeSum_matchingLift (m : Fin 3 → ℤ) :
    edgeSum (matchingLift m) = m 0 + m 1 + m 2 := by
  simp [edgeSum, matchingLift]

/-- Opposite-pair coordinates are surjective before imposing the zero-sum
condition. -/
theorem matchingSums_surjective : Function.Surjective matchingSums := by
  intro m
  exact ⟨matchingLift m, matchingSums_matchingLift m⟩

/-- The integral `A₂` matching lattice. -/
def A2Data := {m : Fin 3 → ℤ // m 0 + m 1 + m 2 = 0}

/-- Zero-total edge configurations. -/
def ZeroEdge := {x : Edge6 // edgeSum x = 0}

/-- The free residual coordinate of a zero-total edge configuration. -/
def matchingA2 (x : ZeroEdge) : A2Data :=
  ⟨matchingSums x.1, by
    rw [matchingSums_total]
    exact x.2⟩

/-- Every integral `A₂` coordinate has a zero-total edge lift. -/
def liftA2 (m : A2Data) : ZeroEdge :=
  ⟨matchingLift m.1, by
    rw [edgeSum_matchingLift]
    exact m.2⟩

/-- The chosen lift is a right inverse to the free residual map. -/
theorem matchingA2_liftA2 (m : A2Data) : matchingA2 (liftA2 m) = m := by
  apply Subtype.ext
  exact matchingSums_matchingLift m.1

/-- The free `A₂` residual map is surjective. -/
theorem matchingA2_surjective : Function.Surjective matchingA2 := by
  intro m
  exact ⟨liftA2 m, matchingA2_liftA2 m⟩

/-- Coordinatewise addition of edge configurations. -/
def addEdge (x y : Edge6) : Edge6 := fun i => x i + y i

/-- Opposite-pair sums are additive. -/
theorem matchingSums_add (x y : Edge6) :
    matchingSums (addEdge x y) =
      fun i => matchingSums x i + matchingSums y i := by
  funext i
  fin_cases i <;> simp [matchingSums, addEdge] <;> ring

/-- Total edge weight is additive. -/
theorem edgeSum_add (x y : Edge6) :
    edgeSum (addEdge x y) = edgeSum x + edgeSum y := by
  simp [edgeSum, addEdge]
  ring

/-- Adding an edge and then subtracting the original recovers the added
edge. -/
theorem subEdge_add_left (x y : Edge6) :
    subEdge (addEdge x y) x = y := by
  funext i
  simp [subEdge, addEdge]

/-- Add the primitive parity representative without changing the free
matching coordinate. -/
def parityTwist (x : Edge6) : Edge6 := addEdge x primitiveParityEdge

/-- The primitive parity twist preserves all opposite-pair sums. -/
theorem matchingSums_parityTwist (x : Edge6) :
    matchingSums (parityTwist x) = matchingSums x := by
  rw [parityTwist, matchingSums_add, primitiveParityEdge_in_kernel]
  funext i
  simp

/-- The primitive parity twist preserves total edge weight. -/
theorem edgeSum_parityTwist (x : Edge6) :
    edgeSum (parityTwist x) = edgeSum x := by
  rw [parityTwist, edgeSum_add]
  simp [primitiveParityEdge, edgeSum_kernelEdge]

/-- The parity twist of a zero-total edge is again zero-total. -/
def parityTwistZero (x : ZeroEdge) : ZeroEdge :=
  ⟨parityTwist x.1, by rw [edgeSum_parityTwist, x.2]⟩

/-- The two lifts have the same free `A₂` coordinate. -/
theorem matchingA2_parityTwistZero (x : ZeroEdge) :
    matchingA2 (parityTwistZero x) = matchingA2 x := by
  apply Subtype.ext
  exact matchingSums_parityTwist x.1

/-- The primitive parity twist is not induced by an integral zero-sum slice
potential, despite preserving the free `A₂` coordinate. -/
theorem parityTwist_not_deltaEquivalent (x : Edge6) :
    ¬ DeltaEquivalent (parityTwist x) x := by
  intro h
  apply primitiveParityEdge_not_in_delta
  rcases h with ⟨v, hv, hdelta⟩
  refine ⟨v, hv, ?_⟩
  simpa [parityTwist, subEdge_add_left] using hdelta

end EnterpriseMath.TetrahedralResidual
