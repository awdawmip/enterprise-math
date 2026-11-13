import EnterpriseMath.PrecisionPi.TetrahedralInjectivity

namespace EnterpriseMath.PrecisionPi.TetrahedralCosets

open TetrahedralResidual TetrahedralMatching TetrahedralParity
  TetrahedralInjectivity

/-- The zero edge datum. -/
def edgeZero : EdgeData := ⟨0, 0, 0, 0, 0, 0⟩

/-- The distinguished generator of the parity obstruction. -/
def basicGenerator : EdgeData := edgePattern 1 0 0

/-- Two edge states are equivalent when they differ by a zero-sum slice-induced state. -/
def DeltaEquivalent (x y : EdgeData) : Prop :=
  ∃ v : VertexData, vertexSum v = 0 ∧ x = edgeAdd y (delta v)

/-- Exact coordinate classification of the delta equivalence relation. -/
theorem deltaEquivalent_iff_matching_and_even
    (x y : EdgeData) :
    DeltaEquivalent x y ↔
      matching x = matching y ∧
      ∃ k : ℤ,
        (x.e12 - y.e12) + (x.e13 - y.e13) + (x.e14 - y.e14) = 2 * k := by
  constructor
  · rintro ⟨v, hv, hxy⟩
    constructor
    · rw [hxy]
      exact matching_edgeAdd_delta_zero y hv
    · refine ⟨v.v1, ?_⟩
      have hv' := hv
      simp [vertexSum] at hv'
      have h12 := congrArg EdgeData.e12 hxy
      have h13 := congrArg EdgeData.e13 hxy
      have h14 := congrArg EdgeData.e14 hxy
      simp [edgeAdd, delta] at h12 h13 h14
      omega
  · rintro ⟨hm, ⟨k, hk⟩⟩
    let a : ℤ := x.e12 - y.e12
    let b : ℤ := x.e13 - y.e13
    let c : ℤ := x.e14 - y.e14
    have habc : a + b + c = 2 * k := by
      simpa [a, b, c] using hk
    have hm1 := congrArg MatchingData.m1 hm
    have hm2 := congrArg MatchingData.m2 hm
    have hm3 := congrArg MatchingData.m3 hm
    simp [matching] at hm1 hm2 hm3
    have hpattern : x = edgeAdd y (edgePattern a b c) := by
      ext <;> simp [edgeAdd, edgePattern, a, b, c] <;> omega
    refine ⟨vertexWitness a b c k,
      vertexSum_vertexWitness_of_even habc, ?_⟩
    rw [delta_vertexWitness_of_even habc]
    exact hpattern

/-- Every integer is either an even or an odd residual coordinate. -/
theorem int_even_or_odd (z : ℤ) :
    (∃ k : ℤ, z = 2 * k) ∨ (∃ k : ℤ, z = 2 * k + 1) := by
  omega

/-- Adding the basic generator preserves the matching coordinate. -/
theorem matching_add_basicGenerator (y : EdgeData) :
    matching (edgeAdd y basicGenerator) = matching y := by
  rw [matching_edgeAdd]
  simp [basicGenerator]

/-- Every matching fiber contains at most two delta-equivalence classes. -/
theorem matching_fiber_at_most_two
    (x y : EdgeData) (hm : matching x = matching y) :
    DeltaEquivalent x y ∨
      DeltaEquivalent x (edgeAdd y basicGenerator) := by
  let s : ℤ :=
    (x.e12 - y.e12) + (x.e13 - y.e13) + (x.e14 - y.e14)
  rcases int_even_or_odd s with hs | hs
  · left
    apply (deltaEquivalent_iff_matching_and_even x y).2
    exact ⟨hm, hs⟩
  · right
    apply (deltaEquivalent_iff_matching_and_even x (edgeAdd y basicGenerator)).2
    constructor
    · calc
        matching x = matching y := hm
        _ = matching (edgeAdd y basicGenerator) :=
          (matching_add_basicGenerator y).symm
    · rcases hs with ⟨k, hk⟩
      refine ⟨k, ?_⟩
      dsimp [s] at hk
      simp [edgeAdd, basicGenerator, edgePattern]
      omega

/-- The basic generator is not delta-equivalent to zero. -/
theorem basicGenerator_not_equiv_zero :
    ¬ DeltaEquivalent basicGenerator edgeZero := by
  intro h
  rcases h with ⟨v, hv, hxy⟩
  apply basic_parity_class_not_mem
  refine ⟨v, hv, ?_⟩
  simpa [basicGenerator, edgeZero, edgeAdd] using hxy.symm

/-- Two copies of the basic generator are delta-equivalent to zero. -/
theorem basicGenerator_add_self_equiv_zero :
    DeltaEquivalent (edgeAdd basicGenerator basicGenerator) edgeZero := by
  rcases twice_basic_parity_class_mem with ⟨v, hv, hd⟩
  refine ⟨v, hv, ?_⟩
  rw [hd]
  ext <;> norm_num [edgeAdd, basicGenerator, edgeZero, edgePattern]

/-- The parity obstruction has exactly two possibilities in every fixed matching fiber. -/
theorem matching_fiber_C2_certificate (y : EdgeData) :
    (¬ DeltaEquivalent (edgeAdd y basicGenerator) y) ∧
    DeltaEquivalent
      (edgeAdd (edgeAdd y basicGenerator) basicGenerator) y := by
  constructor
  · intro h
    have hc := (deltaEquivalent_iff_matching_and_even
      (edgeAdd y basicGenerator) y).1 h
    rcases hc.2 with ⟨k, hk⟩
    simp [edgeAdd, basicGenerator, edgePattern] at hk
    omega
  · rcases twice_basic_parity_class_mem with ⟨v, hv, hd⟩
    refine ⟨v, hv, ?_⟩
    rw [hd]
    ext <;> simp [edgeAdd, basicGenerator, edgePattern] <;> ring

end EnterpriseMath.PrecisionPi.TetrahedralCosets
