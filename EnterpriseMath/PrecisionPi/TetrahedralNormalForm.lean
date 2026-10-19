import EnterpriseMath.PrecisionPi.TetrahedralQuotient

namespace EnterpriseMath.PrecisionPi.TetrahedralNormalForm

open TetrahedralResidual TetrahedralMatching TetrahedralParity
  TetrahedralInjectivity TetrahedralCosets TetrahedralQuotient

/-- Edge sums are additive. -/
theorem edgeSum_edgeAdd (x y : EdgeData) :
    edgeSum (edgeAdd x y) = edgeSum x + edgeSum y := by
  simp [edgeSum, edgeAdd]
  ring

/-- Canonical representative of one `A₂ × C₂` coordinate. -/
def normalRepresentative (p q : ℤ) : Bool → EdgeData
  | false => matchingLift (a2Matching p q)
  | true => edgeAdd (matchingLift (a2Matching p q)) basicGenerator

@[simp] theorem edgeSum_basicGenerator : edgeSum basicGenerator = 0 := by
  simp [basicGenerator]

@[simp] theorem edgeSum_normalRepresentative (p q : ℤ) (ε : Bool) :
    edgeSum (normalRepresentative p q ε) = 0 := by
  cases ε <;> simp [normalRepresentative, edgeSum_edgeAdd]

@[simp] theorem matching_normalRepresentative (p q : ℤ) (ε : Bool) :
    matching (normalRepresentative p q ε) = a2Matching p q := by
  cases ε
  · simp [normalRepresentative]
  · simpa [normalRepresentative] using
      matching_add_basicGenerator (matchingLift (a2Matching p q))

/-- Every zero-sum edge state is equivalent to one canonical `A₂ × C₂` representative. -/
theorem zeroSum_exists_normalRepresentative
    (x : EdgeData) (hx : edgeSum x = 0) :
    ∃ p q : ℤ, ∃ ε : Bool,
      DeltaEquivalent x (normalRepresentative p q ε) := by
  have hm0 :
      (matching x).m1 + (matching x).m2 + (matching x).m3 = 0 := by
    rw [matching_total]
    exact hx
  let p : ℤ := (matching x).m1
  let q : ℤ := (matching x).m2
  let y : EdgeData := matchingLift (a2Matching p q)
  have hmatch : matching x = matching y := by
    rw [matching_matchingLift]
    exact balanced_matching_eq_a2 (matching x) hm0
  rcases matching_fiber_at_most_two x y hmatch with h | h
  · exact ⟨p, q, false, by simpa [normalRepresentative, y] using h⟩
  · exact ⟨p, q, true, by simpa [normalRepresentative, y] using h⟩

/-- Equivalent normal representatives have identical integer and parity coordinates. -/
theorem normalRepresentative_coordinates_unique
    {p q p' q' : ℤ} {ε ε' : Bool}
    (h : DeltaEquivalent
      (normalRepresentative p q ε)
      (normalRepresentative p' q' ε')) :
    p = p' ∧ q = q' ∧ ε = ε' := by
  have hm := ((deltaEquivalent_iff_matching_and_even
    (normalRepresentative p q ε)
    (normalRepresentative p' q' ε')).mp h).1
  have hp : p = p' := by
    have hp' := congrArg MatchingData.m1 hm
    simpa using hp'
  have hq : q = q' := by
    have hq' := congrArg MatchingData.m2 hm
    simpa using hq'
  subst p'
  subst q'
  have he : ε = ε' := by
    cases ε <;> cases ε'
    · rfl
    · exfalso
      have hbad : DeltaEquivalent
          (edgeAdd (matchingLift (a2Matching p q)) basicGenerator)
          (matchingLift (a2Matching p q)) := by
        simpa [normalRepresentative] using deltaEquivalent_symm h
      exact (matching_fiber_C2_certificate
        (matchingLift (a2Matching p q))).1 hbad
    · exfalso
      have hbad : DeltaEquivalent
          (edgeAdd (matchingLift (a2Matching p q)) basicGenerator)
          (matchingLift (a2Matching p q)) := by
        simpa [normalRepresentative] using h
      exact (matching_fiber_C2_certificate
        (matchingLift (a2Matching p q))).1 hbad
    · rfl
  exact ⟨rfl, rfl, he⟩

/-- Exact classification of canonical representatives. -/
theorem normalRepresentative_equiv_iff
    (p q p' q' : ℤ) (ε ε' : Bool) :
    DeltaEquivalent
      (normalRepresentative p q ε)
      (normalRepresentative p' q' ε') ↔
      p = p' ∧ q = q' ∧ ε = ε' := by
  constructor
  · exact normalRepresentative_coordinates_unique
  · rintro ⟨rfl, rfl, rfl⟩
    exact deltaEquivalent_refl _

/-- The balanced tetrahedral quotient is coordinatized by `ℤ × ℤ × Bool`. -/
theorem zeroSum_normal_form_classification :
    (∀ x : EdgeData, edgeSum x = 0 →
      ∃ p q : ℤ, ∃ ε : Bool,
        DeltaEquivalent x (normalRepresentative p q ε)) ∧
    (∀ p q p' q' : ℤ, ∀ ε ε' : Bool,
      DeltaEquivalent
        (normalRepresentative p q ε)
        (normalRepresentative p' q' ε') →
      p = p' ∧ q = q' ∧ ε = ε') := by
  exact ⟨zeroSum_exists_normalRepresentative,
    fun _ _ _ _ _ _ => normalRepresentative_coordinates_unique⟩

end EnterpriseMath.PrecisionPi.TetrahedralNormalForm
