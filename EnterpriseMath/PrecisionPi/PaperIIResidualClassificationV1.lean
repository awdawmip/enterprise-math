import EnterpriseMath.PrecisionPi.PaperIIKernelV1

namespace EnterpriseMath.PrecisionPi.PaperIIResidualClassificationV1

open EnterpriseMath.PrecisionPi.PaperIIKernelV1

/-! ## 1. Exact residual equivalence -/

/-- Coordinatewise difference of two six-line states. -/
def edgeSub (x y : EdgeData) : EdgeData := fun i => x i - y i

/-- Opposite-pair coordinates commute with subtraction. -/
theorem matching_edgeSub (x y : EdgeData) :
    matching (edgeSub x y) = fun i => matching x i - matching y i := by
  funext i
  fin_cases i <;> simp [matching, edgeSub] <;> ring

/-- Total edge weight commutes with subtraction. -/
theorem edgeSum_edgeSub (x y : EdgeData) :
    edgeSum (edgeSub x y) = edgeSum x - edgeSum y := by
  simp [edgeSum, edgeSub]
  ring

/-- Vanishing opposite-pair coordinates are exactly the three-parameter
kernel pattern `(p,q,r,-r,-q,-p)`. -/
theorem matching_eq_zero_iff_pattern (x : EdgeData) :
    matching x = 0 ↔ x = pattern (x 0) (x 1) (x 2) := by
  constructor
  · intro h
    have h0 := congrFun h (0 : Fin 3)
    have h1 := congrFun h (1 : Fin 3)
    have h2 := congrFun h (2 : Fin 3)
    simp [matching] at h0 h1 h2
    funext i
    fin_cases i <;> simp [pattern] <;> omega
  · intro h
    rw [h]
    exact matching_pattern _ _ _

/-- Two edge states are equivalent when their difference is induced by a
zero-sum integral slice potential. -/
def DeltaEquivalent (x y : EdgeData) : Prop :=
  ∃ v : VertexData, vertexSum v = 0 ∧ delta v = edgeSub x y

/-- A slice-induced zero-sum difference preserves all opposite-pair data. -/
theorem matching_eq_of_deltaEquivalent {x y : EdgeData}
    (h : DeltaEquivalent x y) : matching x = matching y := by
  rcases h with ⟨v, hv, hd⟩
  have hzero : matching (edgeSub x y) = 0 := by
    rw [← hd]
    exact matching_delta_of_zero_sum hv
  rw [matching_edgeSub] at hzero
  funext i
  have hi := congrFun hzero i
  simp at hi
  linarith

/-- A slice-induced zero-sum difference has even first-three coordinate sum. -/
theorem even_firstThree_of_deltaEquivalent {x y : EdgeData}
    (h : DeltaEquivalent x y) :
    ∃ k : ℤ, edgeSub x y 0 + edgeSub x y 1 + edgeSub x y 2 = 2 * k := by
  rcases h with ⟨v, hv, hd⟩
  have h0 : v 0 + v 1 = edgeSub x y 0 := by
    simpa [delta] using congrFun hd (0 : Fin 6)
  have h1 : v 0 + v 2 = edgeSub x y 1 := by
    simpa [delta] using congrFun hd (1 : Fin 6)
  have h2 : v 0 + v 3 = edgeSub x y 2 := by
    simpa [delta] using congrFun hd (2 : Fin 6)
  have hv' : v 0 + v 1 + v 2 + v 3 = 0 := by
    simpa [vertexSum] using hv
  refine ⟨v 0, ?_⟩
  rw [← h0, ← h1, ← h2]
  omega

/-- Equality of opposite-pair coordinates puts the difference in the matching
kernel. -/
theorem matching_edgeSub_eq_zero_of_eq {x y : EdgeData}
    (h : matching x = matching y) : matching (edgeSub x y) = 0 := by
  rw [matching_edgeSub, h]
  funext i
  simp

/-- Complete integral classification criterion: equality modulo zero-sum slice
potentials is exactly equality of the three opposite-pair coordinates together
with one parity condition. -/
theorem deltaEquivalent_iff_matching_eq_and_even (x y : EdgeData) :
    DeltaEquivalent x y ↔
      matching x = matching y ∧
        ∃ k : ℤ,
          edgeSub x y 0 + edgeSub x y 1 + edgeSub x y 2 = 2 * k := by
  constructor
  · intro h
    exact ⟨matching_eq_of_deltaEquivalent h,
      even_firstThree_of_deltaEquivalent h⟩
  · rintro ⟨hm, heven⟩
    have hzero := matching_edgeSub_eq_zero_of_eq hm
    have hpattern := (matching_eq_zero_iff_pattern (edgeSub x y)).mp hzero
    have himage :=
      (pattern_in_image_iff_even
        (edgeSub x y 0) (edgeSub x y 1) (edgeSub x y 2)).mpr heven
    rcases himage with ⟨v, hv, hd⟩
    refine ⟨v, hv, ?_⟩
    rw [hpattern]
    exact hd

/-- Residual equivalence is reflexive. -/
theorem deltaEquivalent_refl (x : EdgeData) : DeltaEquivalent x x := by
  apply (deltaEquivalent_iff_matching_eq_and_even x x).mpr
  refine ⟨rfl, 0, ?_⟩
  simp [edgeSub]

/-- Residual equivalence is symmetric. -/
theorem deltaEquivalent_symm {x y : EdgeData}
    (h : DeltaEquivalent x y) : DeltaEquivalent y x := by
  rcases (deltaEquivalent_iff_matching_eq_and_even x y).mp h with
    ⟨hm, k, hk⟩
  apply (deltaEquivalent_iff_matching_eq_and_even y x).mpr
  refine ⟨hm.symm, -k, ?_⟩
  simp [edgeSub] at hk ⊢
  omega

/-- Residual equivalence is transitive. -/
theorem deltaEquivalent_trans {x y z : EdgeData}
    (hxy : DeltaEquivalent x y) (hyz : DeltaEquivalent y z) :
    DeltaEquivalent x z := by
  rcases (deltaEquivalent_iff_matching_eq_and_even x y).mp hxy with
    ⟨hmxy, k, hk⟩
  rcases (deltaEquivalent_iff_matching_eq_and_even y z).mp hyz with
    ⟨hmyz, l, hl⟩
  apply (deltaEquivalent_iff_matching_eq_and_even x z).mpr
  refine ⟨hmxy.trans hmyz, k + l, ?_⟩
  simp [edgeSub] at hk hl ⊢
  omega

/-- The exact integral residual relation as a setoid. -/
def deltaSetoid : Setoid EdgeData where
  r := DeltaEquivalent
  iseqv := ⟨deltaEquivalent_refl, deltaEquivalent_symm,
    deltaEquivalent_trans⟩

/-! ## 2. Canonical `Z² × C₂` normal forms on the zero-sum plane -/

/-- Integral representative of one Boolean parity bit. -/
def bitInt : Bool → ℤ
  | false => 0
  | true => 1

/-- Canonical zero-sum edge state with free coordinates `(p,q)` and parity
coordinate `ε`. -/
def normalForm (p q : ℤ) (ε : Bool) : EdgeData :=
  ![bitInt ε, 0, 0, -p - q, q, p - bitInt ε]

@[simp] theorem edgeSum_normalForm (p q : ℤ) (ε : Bool) :
    edgeSum (normalForm p q ε) = 0 := by
  cases ε <;> (simp [edgeSum, normalForm, bitInt]; ring)

@[simp] theorem matching_normalForm (p q : ℤ) (ε : Bool) :
    matching (normalForm p q ε) = ![p, q, -p - q] := by
  funext i
  fin_cases i <;> cases ε <;> simp [matching, normalForm, bitInt]

@[simp] theorem firstThree_normalForm (p q : ℤ) (ε : Bool) :
    normalForm p q ε 0 + normalForm p q ε 1 + normalForm p q ε 2 =
      bitInt ε := by
  cases ε <;> simp [normalForm, bitInt]

/-- Two canonical forms are residual-equivalent exactly when all three normal
coordinates agree. -/
theorem normalForm_deltaEquivalent_iff
    (p q p' q' : ℤ) (ε ε' : Bool) :
    DeltaEquivalent (normalForm p q ε) (normalForm p' q' ε') ↔
      p = p' ∧ q = q' ∧ ε = ε' := by
  constructor
  · intro h
    rcases
        (deltaEquivalent_iff_matching_eq_and_even
          (normalForm p q ε) (normalForm p' q' ε')).mp h with
      ⟨hm, k, hk⟩
    have hp : p = p' := by
      have h0 := congrFun hm (0 : Fin 3)
      simpa using h0
    have hq : q = q' := by
      have h1 := congrFun hm (1 : Fin 3)
      simpa using h1
    have he : ε = ε' := by
      cases ε <;> cases ε' <;>
        simp [edgeSub, normalForm, bitInt] at hk ⊢ <;> omega
    exact ⟨hp, hq, he⟩
  · rintro ⟨rfl, rfl, rfl⟩
    exact deltaEquivalent_refl _

/-- The sum of the three matching coordinates is exactly total edge weight. -/
theorem matching_sum_eq_edgeSum (x : EdgeData) :
    matching x 0 + matching x 1 + matching x 2 = edgeSum x := by
  simp [matching, edgeSum]
  ring

/-- Every zero-sum edge state is equivalent to a canonical form with two free
integer coordinates and one Boolean parity bit. -/
theorem exists_normalForm (x : EdgeData) (hx : edgeSum x = 0) :
    ∃ p q : ℤ, ∃ ε : Bool, DeltaEquivalent x (normalForm p q ε) := by
  have hsum := matching_sum_eq_edgeSum x
  have hthird : matching x 2 = -matching x 0 - matching x 1 := by
    rw [hx] at hsum
    linarith
  have hm (ε : Bool) :
      matching x = matching (normalForm (matching x 0) (matching x 1) ε) := by
    funext i
    fin_cases i
    · simp
    · simp
    · simpa using hthird
  obtain ⟨k, hk | hk⟩ := Int.even_or_odd' (x 0 + x 1 + x 2)
  · refine ⟨matching x 0, matching x 1, false, ?_⟩
    apply (deltaEquivalent_iff_matching_eq_and_even x
      (normalForm (matching x 0) (matching x 1) false)).mpr
    refine ⟨hm false, k, ?_⟩
    simp [edgeSub, normalForm, bitInt]
    omega
  · refine ⟨matching x 0, matching x 1, true, ?_⟩
    apply (deltaEquivalent_iff_matching_eq_and_even x
      (normalForm (matching x 0) (matching x 1) true)).mpr
    refine ⟨hm true, k, ?_⟩
    simp [edgeSub, normalForm, bitInt]
    omega

/-! ## 3. Quotient-level classification -/

/-- Zero-total edge states. -/
abbrev ZeroEdge := {x : EdgeData // edgeSum x = 0}

/-- Canonical zero-total representative. -/
def normalZeroEdge (p q : ℤ) (ε : Bool) : ZeroEdge :=
  ⟨normalForm p q ε, edgeSum_normalForm p q ε⟩

/-- Residual relation restricted to the zero-total plane. -/
def zeroDeltaSetoid : Setoid ZeroEdge where
  r := fun x y => DeltaEquivalent x.1 y.1
  iseqv := ⟨fun x => deltaEquivalent_refl x.1,
    fun h => deltaEquivalent_symm h,
    fun h₁ h₂ => deltaEquivalent_trans h₁ h₂⟩

/-- Zero-total tetrahedral residual quotient. -/
abbrev ZeroResidualQuotient := Quotient zeroDeltaSetoid

/-- Quotient class of one canonical normal form. -/
def normalClass (p q : ℤ) (ε : Bool) : ZeroResidualQuotient :=
  Quotient.mk zeroDeltaSetoid (normalZeroEdge p q ε)

/-- Every quotient class has a canonical representative. -/
theorem quotient_exists_normal (Q : ZeroResidualQuotient) :
    ∃ p q : ℤ, ∃ ε : Bool, Q = normalClass p q ε := by
  refine Quotient.inductionOn Q ?_
  intro x
  rcases exists_normalForm x.1 x.2 with ⟨p, q, ε, h⟩
  exact ⟨p, q, ε, Quotient.sound h⟩

/-- Canonical quotient representatives are equal exactly when their
`Z² × C₂` coordinates agree. -/
theorem normalClass_eq_iff
    (p q p' q' : ℤ) (ε ε' : Bool) :
    normalClass p q ε = normalClass p' q' ε' ↔
      p = p' ∧ q = q' ∧ ε = ε' := by
  constructor
  · intro h
    have hr := Quotient.exact h
    change DeltaEquivalent (normalForm p q ε) (normalForm p' q' ε') at hr
    exact (normalForm_deltaEquivalent_iff p q p' q' ε ε').mp hr
  · rintro ⟨rfl, rfl, rfl⟩
    rfl

/-- Coordinate-to-quotient normal-form map. -/
def normalClassMap : ((ℤ × ℤ) × Bool) → ZeroResidualQuotient :=
  fun c => normalClass c.1.1 c.1.2 c.2

/-- The normal-form map is bijective. -/
theorem normalClassMap_bijective : Function.Bijective normalClassMap := by
  constructor
  · rintro ⟨⟨p, q⟩, ε⟩ ⟨⟨p', q'⟩, ε'⟩ h
    rcases (normalClass_eq_iff p q p' q' ε ε').mp h with
      ⟨rfl, rfl, rfl⟩
    rfl
  · intro Q
    rcases quotient_exists_normal Q with ⟨p, q, ε, h⟩
    exact ⟨((p, q), ε), h.symm⟩

/-- Exact set-level classification of the zero-sum integral residual quotient
as two free integer coordinates plus one order-two bit. -/
noncomputable def normalCoordinateEquiv :
    ((ℤ × ℤ) × Bool) ≃ ZeroResidualQuotient :=
  Equiv.ofBijective normalClassMap normalClassMap_bijective

/-- The paper-facing orientation of the same exact classification. -/
noncomputable def zeroResidualQuotientEquiv :
    ZeroResidualQuotient ≃ ((ℤ × ℤ) × Bool) :=
  normalCoordinateEquiv.symm

end EnterpriseMath.PrecisionPi.PaperIIResidualClassificationV1
