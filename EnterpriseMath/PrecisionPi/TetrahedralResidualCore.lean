import Mathlib

namespace EnterpriseMath.PrecisionPi.TetrahedralResidualCore

/-- Integer variations of the four tetrahedral slice labels. -/
@[ext]
structure VertexChange where
  v1 : ℤ
  v2 : ℤ
  v3 : ℤ
  v4 : ℤ
  deriving DecidableEq

/-- Integer variations of the six shared line families, in edge order
`12, 13, 14, 23, 24, 34`. -/
@[ext]
structure EdgeChange where
  e12 : ℤ
  e13 : ℤ
  e14 : ℤ
  e23 : ℤ
  e24 : ℤ
  e34 : ℤ
  deriving DecidableEq

/-- The three sums over opposite edge pairs. -/
@[ext]
structure MatchingChange where
  m1 : ℤ
  m2 : ℤ
  m3 : ℤ
  deriving DecidableEq

def vertexTotal (v : VertexChange) : ℤ :=
  v.v1 + v.v2 + v.v3 + v.v4

def edgeTotal (x : EdgeChange) : ℤ :=
  x.e12 + x.e13 + x.e14 + x.e23 + x.e24 + x.e34

def matchingTotal (m : MatchingChange) : ℤ :=
  m.m1 + m.m2 + m.m3

/-- Endpoint summation from the four slice labels to the six shared line labels. -/
def delta (v : VertexChange) : EdgeChange :=
  ⟨v.v1 + v.v2, v.v1 + v.v3, v.v1 + v.v4,
    v.v2 + v.v3, v.v2 + v.v4, v.v3 + v.v4⟩

/-- Coordinates on the three opposite-edge matchings. -/
def matching (x : EdgeChange) : MatchingChange :=
  ⟨x.e12 + x.e34, x.e13 + x.e24, x.e14 + x.e23⟩

def zeroMatching : MatchingChange := ⟨0, 0, 0⟩

/-- Every vertex occurs in exactly three tetrahedral edges. -/
theorem edgeTotal_delta (v : VertexChange) :
    edgeTotal (delta v) = 3 * vertexTotal v := by
  simp [edgeTotal, delta, vertexTotal]
  ring

/-- All three opposite-edge sums of an induced variation equal the vertex total. -/
theorem matching_delta (v : VertexChange) :
    matching (delta v) = ⟨vertexTotal v, vertexTotal v, vertexTotal v⟩ := by
  ext <;> simp [matching, delta, vertexTotal] <;> ring

/-- A balanced slice variation has zero matching residual. -/
theorem matching_delta_of_balanced (v : VertexChange) (h : vertexTotal v = 0) :
    matching (delta v) = zeroMatching := by
  rw [matching_delta, h]
  rfl

/-- The three matching coordinates sum to the six-edge total. -/
theorem matchingTotal_matching (x : EdgeChange) :
    matchingTotal (matching x) = edgeTotal x := by
  simp [matchingTotal, matching, edgeTotal]
  ring

/-- Normal form of the zero-matching fiber. -/
def kernelShape (a b c : ℤ) : EdgeChange :=
  ⟨a, b, c, -c, -b, -a⟩

@[simp]
theorem matching_kernelShape (a b c : ℤ) :
    matching (kernelShape a b c) = zeroMatching := by
  ext <;> simp [matching, kernelShape, zeroMatching]

@[simp]
theorem edgeTotal_kernelShape (a b c : ℤ) :
    edgeTotal (kernelShape a b c) = 0 := by
  simp [edgeTotal, kernelShape]
  ring

/-- Zero opposite-edge sums force the antisymmetric normal form. -/
theorem eq_kernelShape_of_matching_eq_zero (x : EdgeChange)
    (h : matching x = zeroMatching) :
    x = kernelShape x.e12 x.e13 x.e14 := by
  have h1 : x.e12 + x.e34 = 0 := by
    simpa [matching, zeroMatching] using congrArg MatchingChange.m1 h
  have h2 : x.e13 + x.e24 = 0 := by
    simpa [matching, zeroMatching] using congrArg MatchingChange.m2 h
  have h3 : x.e14 + x.e23 = 0 := by
    simpa [matching, zeroMatching] using congrArg MatchingChange.m3 h
  ext <;> simp [kernelShape] <;> linarith

/-- Explicit integral lift when the parity obstruction vanishes. -/
def vertexLift (t a b c : ℤ) : VertexChange :=
  ⟨t, a - t, b - t, c - t⟩

theorem vertexTotal_vertexLift {t a b c : ℤ} (h : a + b + c = 2 * t) :
    vertexTotal (vertexLift t a b c) = 0 := by
  simp [vertexTotal, vertexLift]
  linarith

theorem delta_vertexLift {t a b c : ℤ} (h : a + b + c = 2 * t) :
    delta (vertexLift t a b c) = kernelShape a b c := by
  ext <;> simp [delta, vertexLift, kernelShape] <;> linarith

/-- Exact parity obstruction on the zero-matching fiber. -/
theorem kernelShape_in_balanced_range_iff (a b c : ℤ) :
    (∃ v : VertexChange, vertexTotal v = 0 ∧ delta v = kernelShape a b c) ↔
      ∃ t : ℤ, a + b + c = 2 * t := by
  constructor
  · rintro ⟨v, hv, hd⟩
    have h12 : v.v1 + v.v2 = a := by
      simpa [delta, kernelShape] using congrArg EdgeChange.e12 hd
    have h13 : v.v1 + v.v3 = b := by
      simpa [delta, kernelShape] using congrArg EdgeChange.e13 hd
    have h14 : v.v1 + v.v4 = c := by
      simpa [delta, kernelShape] using congrArg EdgeChange.e14 hd
    refine ⟨v.v1, ?_⟩
    simp [vertexTotal] at hv
    linarith
  · rintro ⟨t, ht⟩
    exact ⟨vertexLift t a b c, vertexTotal_vertexLift ht, delta_vertexLift ht⟩

/-- The nonzero parity representative `e₁₂-e₃₄`. -/
def torsionCandidate : EdgeChange := kernelShape 1 0 0

/-- The parity representative is not induced by any balanced integral slice variation. -/
theorem torsionCandidate_not_in_balanced_range :
    ¬ ∃ v : VertexChange, vertexTotal v = 0 ∧ delta v = torsionCandidate := by
  intro h
  have hp : ∃ t : ℤ, (1 : ℤ) + 0 + 0 = 2 * t :=
    (kernelShape_in_balanced_range_iff 1 0 0).1 (by
      simpa [torsionCandidate] using h)
  rcases hp with ⟨t, ht⟩
  omega

/-- Twice the parity representative is induced by a balanced integral slice variation. -/
theorem twice_torsionCandidate_in_balanced_range :
    ∃ v : VertexChange, vertexTotal v = 0 ∧ delta v = kernelShape 2 0 0 := by
  exact (kernelShape_in_balanced_range_iff 2 0 0).2 ⟨1, by norm_num⟩

/-- A balanced six-edge representative for two free `A₂` coordinates. -/
def residualEdge (p q : ℤ) : EdgeChange :=
  ⟨p, q, -p - q, 0, 0, 0⟩

@[simp]
theorem edgeTotal_residualEdge (p q : ℤ) :
    edgeTotal (residualEdge p q) = 0 := by
  simp [edgeTotal, residualEdge]
  ring

/-- Every integral zero-sum matching triple has a balanced edge representative. -/
theorem matching_surjective_on_balanced (m : MatchingChange)
    (hm : matchingTotal m = 0) :
    ∃ x : EdgeChange, edgeTotal x = 0 ∧ matching x = m := by
  refine ⟨residualEdge m.m1 m.m2, edgeTotal_residualEdge _ _, ?_⟩
  apply MatchingChange.ext
  · simp [matching, residualEdge]
  · simp [matching, residualEdge]
  · simp [matching, residualEdge, matchingTotal] at hm ⊢
    linarith

/-- On every zero-matching edge shape, liftability is precisely the parity test. -/
theorem matching_zero_in_balanced_range_iff (x : EdgeChange)
    (hx : matching x = zeroMatching) :
    (∃ v : VertexChange, vertexTotal v = 0 ∧ delta v = x) ↔
      ∃ t : ℤ, x.e12 + x.e13 + x.e14 = 2 * t := by
  have hk : x = kernelShape x.e12 x.e13 x.e14 :=
    eq_kernelShape_of_matching_eq_zero x hx
  constructor
  · rintro ⟨v, hv, hd⟩
    exact (kernelShape_in_balanced_range_iff x.e12 x.e13 x.e14).1
      ⟨v, hv, hd.trans hk⟩
  · intro hp
    rcases (kernelShape_in_balanced_range_iff x.e12 x.e13 x.e14).2 hp with
      ⟨v, hv, hd⟩
    exact ⟨v, hv, hd.trans hk.symm⟩

end EnterpriseMath.PrecisionPi.TetrahedralResidualCore
