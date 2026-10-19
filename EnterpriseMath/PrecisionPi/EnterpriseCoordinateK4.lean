import EnterpriseMath.PrecisionPi.EnterpriseCoordinateIncidence

namespace EnterpriseMath.PrecisionPi.EnterpriseCoordinateK4

open EnterpriseCoordinateIncidence

/-- Unordered pairs of distinct Enterprise-coordinate slice charts. -/
abbrev SlicePair := {s : Finset SliceChart // s.card = 2}

/-- A carrier line family is sent to the two slice charts containing it. -/
def lineToSlicePair (l : LineFamily) : SlicePair :=
  ⟨incidentSlices l, incidentSlices_card l⟩

/-- Incidence is recovered exactly from the associated slice pair. -/
theorem mem_lineToSlicePair_iff (l : LineFamily) (s : SliceChart) :
    s ∈ (lineToSlicePair l : Finset SliceChart) ↔ l ∈ sliceLines s := by
  simp [lineToSlicePair, incidentSlices]

/-- The six line families are exactly the six unordered pairs of four slice charts. -/
theorem lineToSlicePair_bijective : Function.Bijective lineToSlicePair := by
  native_decide

/-- Explicit `K₄` edge equivalence for the selected Enterprise coordinate carrier. -/
def lineFamilyEquivSlicePair : LineFamily ≃ SlicePair :=
  Equiv.ofBijective lineToSlicePair lineToSlicePair_bijective

/-- The `K₄` edge set has six elements in this carrier realization. -/
theorem slicePair_card : Fintype.card SlicePair = 6 := by
  calc
    Fintype.card SlicePair = Fintype.card LineFamily :=
      Fintype.card_congr lineFamilyEquivSlicePair.symm
    _ = 6 := lineFamily_card

/-- Two distinct slice charts determine the unique line family represented by their pair. -/
def sharedLineOfPair (p : SlicePair) : LineFamily :=
  lineFamilyEquivSlicePair.symm p

@[simp] theorem lineToSlicePair_sharedLineOfPair (p : SlicePair) :
    lineToSlicePair (sharedLineOfPair p) = p := by
  exact lineFamilyEquivSlicePair.apply_symm_apply p

@[simp] theorem sharedLineOfPair_lineToSlicePair (l : LineFamily) :
    sharedLineOfPair (lineToSlicePair l) = l := by
  exact lineFamilyEquivSlicePair.symm_apply_apply l

/-- The abstract `K₄` incidence condition is identical to the explicit FCC slice-line condition. -/
theorem sharedLine_incident_iff
    (p : SlicePair) (s : SliceChart) :
    s ∈ (p : Finset SliceChart) ↔
      sharedLineOfPair p ∈ sliceLines s := by
  rw [← lineToSlicePair_sharedLineOfPair p]
  exact mem_lineToSlicePair_iff _ _

end EnterpriseMath.PrecisionPi.EnterpriseCoordinateK4
