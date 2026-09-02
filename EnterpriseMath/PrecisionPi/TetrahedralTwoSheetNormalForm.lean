import EnterpriseMath.PrecisionPi.TetrahedralResidualClassification

namespace EnterpriseMath.PrecisionPi.TetrahedralTwoSheetNormalForm

open TetrahedralResidualCore
open TetrahedralResidualClassification

/-- Coordinatewise addition of six-edge variations. -/
def edgeAdd (x y : EdgeChange) : EdgeChange :=
  ⟨x.e12 + y.e12, x.e13 + y.e13, x.e14 + y.e14,
    x.e23 + y.e23, x.e24 + y.e24, x.e34 + y.e34⟩

@[simp]
theorem edgeTotal_edgeAdd (x y : EdgeChange) :
    edgeTotal (edgeAdd x y) = edgeTotal x + edgeTotal y := by
  simp [edgeTotal, edgeAdd]
  ring

@[simp]
theorem matching_edgeAdd (x y : EdgeChange) :
    matching (edgeAdd x y) =
      ⟨(matching x).m1 + (matching y).m1,
        (matching x).m2 + (matching y).m2,
        (matching x).m3 + (matching y).m3⟩ := by
  ext <;> simp [matching, edgeAdd] <;> ring

/-- The two independent free matching coordinates. -/
def freeP (x : EdgeChange) : ℤ := x.e12 + x.e34

def freeQ (x : EdgeChange) : ℤ := x.e13 + x.e24

/-- Canonical free representative with no parity-sheet displacement. -/
def freeRepresentative (x : EdgeChange) : EdgeChange :=
  residualEdge (freeP x) (freeQ x)

/-- Canonical representative on the other parity sheet. -/
def shiftedRepresentative (x : EdgeChange) : EdgeChange :=
  edgeAdd (freeRepresentative x) torsionCandidate

/-- A balanced edge state and its free representative have identical matching coordinates. -/
theorem matching_freeRepresentative_of_balanced (x : EdgeChange)
    (hx : edgeTotal x = 0) :
    matching x = matching (freeRepresentative x) := by
  have hm : matchingTotal (matching x) = 0 := by
    rw [matchingTotal_matching, hx]
  apply MatchingChange.ext
  · simp [matching, freeRepresentative, freeP, residualEdge]
  · simp [matching, freeRepresentative, freeQ, residualEdge]
  · simp [matching, freeRepresentative, freeP, freeQ, residualEdge,
      matchingTotal] at hm ⊢
    linarith

/-- The parity-shifted representative has the same free matching coordinates. -/
theorem matching_shiftedRepresentative_of_balanced (x : EdgeChange)
    (hx : edgeTotal x = 0) :
    matching x = matching (shiftedRepresentative x) := by
  rw [shiftedRepresentative, matching_edgeAdd]
  have hfree := matching_freeRepresentative_of_balanced x hx
  rw [← hfree, matching_kernelShape]
  rfl

/-- Both canonical representatives are balanced. -/
theorem edgeTotal_freeRepresentative (x : EdgeChange) :
    edgeTotal (freeRepresentative x) = 0 := by
  simp [freeRepresentative]

theorem edgeTotal_shiftedRepresentative (x : EdgeChange) :
    edgeTotal (shiftedRepresentative x) = 0 := by
  simp [shiftedRepresentative, torsionCandidate]

/-- Even parity selects the unshifted free representative. -/
theorem equivalent_freeRepresentative_of_even {x : EdgeChange}
    (hx : edgeTotal x = 0) {t : ℤ}
    (hpar : x.e12 + x.e13 + x.e14 = 2 * t) :
    BalancedEquivalent x (freeRepresentative x) := by
  apply (balancedEquivalent_iff_parity_of_matching_eq
    (matching_freeRepresentative_of_balanced x hx)).2
  refine ⟨t, ?_⟩
  simp [freeRepresentative, freeP, freeQ, residualEdge]
  linarith

/-- Odd parity selects the shifted representative. -/
theorem equivalent_shiftedRepresentative_of_odd {x : EdgeChange}
    (hx : edgeTotal x = 0) {t : ℤ}
    (hpar : x.e12 + x.e13 + x.e14 = 2 * t + 1) :
    BalancedEquivalent x (shiftedRepresentative x) := by
  apply (balancedEquivalent_iff_parity_of_matching_eq
    (matching_shiftedRepresentative_of_balanced x hx)).2
  refine ⟨t, ?_⟩
  simp [shiftedRepresentative, edgeAdd, freeRepresentative, freeP, freeQ,
    residualEdge, torsionCandidate, kernelShape]
  linarith

/-- The two parity-sheet representatives with the same free coordinates are inequivalent. -/
theorem free_not_equivalent_shifted (x : EdgeChange) :
    ¬ BalancedEquivalent (freeRepresentative x) (shiftedRepresentative x) := by
  intro h
  have hmatch : matching (freeRepresentative x) =
      matching (shiftedRepresentative x) := by
    rw [shiftedRepresentative, matching_edgeAdd, matching_kernelShape]
    rfl
  have hp := (balancedEquivalent_iff_parity_of_matching_eq hmatch).1 h
  rcases hp with ⟨t, ht⟩
  simp [shiftedRepresentative, edgeAdd, freeRepresentative, freeP, freeQ,
    residualEdge, torsionCandidate, kernelShape] at ht
  omega

/-- Two parity shifts are induced by a balanced slice variation, hence the
sheet-switching class has order two. -/
theorem double_shift_equivalent_free (x : EdgeChange) :
    BalancedEquivalent
      (edgeAdd (shiftedRepresentative x) torsionCandidate)
      (freeRepresentative x) := by
  unfold BalancedEquivalent
  rcases twice_torsionCandidate_in_balanced_range with ⟨v, hv, hd⟩
  refine ⟨v, hv, ?_⟩
  rw [hd]
  ext <;> simp [edgeSub, edgeAdd, shiftedRepresentative, torsionCandidate,
    kernelShape, freeRepresentative, residualEdge, freeP, freeQ]

end EnterpriseMath.PrecisionPi.TetrahedralTwoSheetNormalForm
