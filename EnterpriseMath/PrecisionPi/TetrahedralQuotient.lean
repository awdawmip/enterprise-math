import EnterpriseMath.PrecisionPi.TetrahedralCosets

namespace EnterpriseMath.PrecisionPi.TetrahedralQuotient

open TetrahedralResidual TetrahedralMatching TetrahedralParity
  TetrahedralInjectivity TetrahedralCosets

/-- Zero slice potential. -/
def vertexZero : VertexData := ⟨0, 0, 0, 0⟩

/-- Coordinatewise negation of a slice potential. -/
def vertexNeg (v : VertexData) : VertexData :=
  ⟨-v.v1, -v.v2, -v.v3, -v.v4⟩

/-- Coordinatewise addition of slice potentials. -/
def vertexAdd (v w : VertexData) : VertexData :=
  ⟨v.v1 + w.v1, v.v2 + w.v2, v.v3 + w.v3, v.v4 + w.v4⟩

@[simp] theorem vertexSum_vertexZero : vertexSum vertexZero = 0 := by
  norm_num [vertexSum, vertexZero]

@[simp] theorem vertexSum_vertexNeg (v : VertexData) :
    vertexSum (vertexNeg v) = -vertexSum v := by
  simp [vertexSum, vertexNeg]
  ring

@[simp] theorem vertexSum_vertexAdd (v w : VertexData) :
    vertexSum (vertexAdd v w) = vertexSum v + vertexSum w := by
  simp [vertexSum, vertexAdd]
  ring

/-- Delta equivalence is reflexive. -/
theorem deltaEquivalent_refl (x : EdgeData) : DeltaEquivalent x x := by
  refine ⟨vertexZero, vertexSum_vertexZero, ?_⟩
  ext <;> norm_num [edgeAdd, delta, vertexZero]

/-- Delta equivalence is symmetric. -/
theorem deltaEquivalent_symm {x y : EdgeData} :
    DeltaEquivalent x y → DeltaEquivalent y x := by
  rintro ⟨v, hv, hxy⟩
  refine ⟨vertexNeg v, ?_, ?_⟩
  · rw [vertexSum_vertexNeg, hv]
    norm_num
  · rw [hxy]
    ext <;> simp [edgeAdd, delta, vertexNeg] <;> ring

/-- Delta equivalence is transitive. -/
theorem deltaEquivalent_trans {x y z : EdgeData} :
    DeltaEquivalent x y → DeltaEquivalent y z → DeltaEquivalent x z := by
  rintro ⟨v, hv, hxy⟩ ⟨w, hw, hyz⟩
  refine ⟨vertexAdd w v, ?_, ?_⟩
  · rw [vertexSum_vertexAdd, hw, hv]
    norm_num
  · rw [hxy, hyz]
    ext <;> simp [edgeAdd, delta, vertexAdd] <;> ring

/-- The actual quotient of six-line-family states by zero-sum four-slice potentials. -/
def deltaSetoid : Setoid EdgeData where
  r := DeltaEquivalent
  iseqv := ⟨deltaEquivalent_refl, deltaEquivalent_symm, deltaEquivalent_trans⟩

/-- Quotient state space before restricting to the zero-total-weight slice. -/
abbrev EdgeQuotient := Quotient deltaSetoid

/-- The perfect-matching coordinate descends to the quotient. -/
def quotientMatching : EdgeQuotient → MatchingData :=
  Quotient.lift matching (by
    intro x y hxy
    exact ((deltaEquivalent_iff_matching_and_even x y).mp hxy).1)

/-- The residual `C₂` coordinate descends to the quotient. -/
def quotientParity : EdgeQuotient → ZMod 2 :=
  Quotient.lift residualParity (by
    intro x y hxy
    rcases hxy with ⟨v, hv, hxy⟩
    rw [hxy]
    exact residualParity_edgeAdd_delta y hv)

/-- Combined free-plus-torsion coordinate readout. -/
def quotientCoordinates : EdgeQuotient → MatchingData × ZMod 2 :=
  fun q => (quotientMatching q, quotientParity q)

@[simp] theorem quotientMatching_mk (x : EdgeData) :
    quotientMatching (Quotient.mk deltaSetoid x) = matching x := rfl

@[simp] theorem quotientParity_mk (x : EdgeData) :
    quotientParity (Quotient.mk deltaSetoid x) = residualParity x := rfl

@[simp] theorem quotientCoordinates_mk (x : EdgeData) :
    quotientCoordinates (Quotient.mk deltaSetoid x) =
      (matching x, residualParity x) := rfl

/-- The basic generator and zero define distinct quotient points. -/
theorem basicGenerator_quotient_ne_zero :
    Quotient.mk deltaSetoid basicGenerator ≠
      Quotient.mk deltaSetoid edgeZero := by
  intro h
  have hrel : DeltaEquivalent basicGenerator edgeZero :=
    Quotient.exact h
  exact basicGenerator_not_equiv_zero hrel

/-- Adding the basic generator twice returns to the zero quotient class. -/
theorem twice_basicGenerator_quotient_eq_zero :
    Quotient.mk deltaSetoid (edgeAdd basicGenerator basicGenerator) =
      Quotient.mk deltaSetoid edgeZero := by
  exact Quotient.sound basicGenerator_add_self_equiv_zero

/-- The quotient parity visibly separates the basic generator from zero. -/
theorem quotientParity_basicGenerator :
    quotientParity (Quotient.mk deltaSetoid basicGenerator) = 1 := by
  change residualParity basicGenerator = 1
  simpa [basicGenerator] using basic_parity_value

@[simp] theorem quotientParity_zero :
    quotientParity (Quotient.mk deltaSetoid edgeZero) = 0 := by
  norm_num [quotientParity, residualParity, residualSum, edgeZero]

end EnterpriseMath.PrecisionPi.TetrahedralQuotient
