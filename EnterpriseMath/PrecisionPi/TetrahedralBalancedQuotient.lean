import EnterpriseMath.PrecisionPi.TetrahedralNormalForm

namespace EnterpriseMath.PrecisionPi.TetrahedralBalancedQuotient

open TetrahedralResidual TetrahedralMatching TetrahedralParity
  TetrahedralInjectivity TetrahedralCosets TetrahedralQuotient
  TetrahedralNormalForm

/-- Zero-total-weight six-line-family states. -/
abbrev BalancedEdge := {x : EdgeData // edgeSum x = 0}

/-- Delta equivalence restricted to balanced edge states. -/
def balancedSetoid : Setoid BalancedEdge where
  r x y := DeltaEquivalent x.1 y.1
  iseqv := ⟨
    fun x => deltaEquivalent_refl x.1,
    fun h => deltaEquivalent_symm h,
    fun hxy hyz => deltaEquivalent_trans hxy hyz⟩

/-- Balanced tetrahedral residual quotient. -/
abbrev BalancedQuotient := Quotient balancedSetoid

/-- Explicit normal coordinates: two free integer directions and one parity bit. -/
abbrev NormalCoordinate := (ℤ × ℤ) × Bool

/-- Balanced edge representative of one normal coordinate. -/
def normalBalanced (t : NormalCoordinate) : BalancedEdge :=
  ⟨normalRepresentative t.1.1 t.1.2 t.2,
    edgeSum_normalRepresentative t.1.1 t.1.2 t.2⟩

/-- Map normal coordinates into the balanced quotient. -/
def normalClass (t : NormalCoordinate) : BalancedQuotient :=
  Quotient.mk balancedSetoid (normalBalanced t)

/-- Every balanced quotient class has a normal coordinate. -/
theorem normalClass_surjective : Function.Surjective normalClass := by
  intro q
  refine Quotient.inductionOn q ?_
  intro x
  rcases zeroSum_exists_normalRepresentative x.1 x.2 with ⟨p, q, ε, h⟩
  refine ⟨((p, q), ε), ?_⟩
  apply Quotient.sound
  exact deltaEquivalent_symm h

/-- Distinct normal coordinates determine distinct balanced quotient classes. -/
theorem normalClass_injective : Function.Injective normalClass := by
  rintro ⟨⟨p, q⟩, ε⟩ ⟨⟨p', q'⟩, ε'⟩ h
  have hrel : DeltaEquivalent
      (normalRepresentative p q ε)
      (normalRepresentative p' q' ε') := by
    exact Quotient.exact h
  rcases normalRepresentative_coordinates_unique hrel with ⟨hp, hq, hε⟩
  subst p'
  subst q'
  subst ε'
  rfl

/-- Formal set-level classification of the balanced residual quotient by `ℤ² × C₂`. -/
def normalCoordinateEquiv : NormalCoordinate ≃ BalancedQuotient :=
  Equiv.ofBijective normalClass ⟨normalClass_injective, normalClass_surjective⟩

/-- The zero normal coordinate is represented by the zero edge state. -/
theorem normalRepresentative_zero_false :
    normalRepresentative 0 0 false = edgeZero := by
  rfl

/-- The nonzero parity coordinate over the zero `A₂` point is the basic generator. -/
theorem normalRepresentative_zero_true :
    normalRepresentative 0 0 true = basicGenerator := by
  ext <;> norm_num [normalRepresentative, matchingLift, a2Matching,
    edgeAdd, basicGenerator, edgeZero, edgePattern]

/-- The two parity points over the zero `A₂` coordinate are distinct in the quotient. -/
theorem zero_fiber_two_classes :
    normalClass ((0, 0), false) ≠ normalClass ((0, 0), true) := by
  intro h
  apply basicGenerator_not_equiv_zero
  have hrel : DeltaEquivalent
      (normalRepresentative 0 0 false)
      (normalRepresentative 0 0 true) := Quotient.exact h
  rw [normalRepresentative_zero_false, normalRepresentative_zero_true] at hrel
  exact deltaEquivalent_symm hrel

end EnterpriseMath.PrecisionPi.TetrahedralBalancedQuotient
