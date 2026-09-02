import Mathlib

namespace EnterpriseMath.PrecisionPi.EnterpriseCoordinateIncidence

/-- The six stable unoriented line families of the selected FCC coordinate carrier. -/
inductive LineFamily
  | L1 | L2 | L3 | L4 | L5 | L6
  deriving DecidableEq, Fintype, Repr

/-- The four overlapping three-line slice charts. -/
inductive SliceChart
  | A | B | C | D
  deriving DecidableEq, Fintype, Repr

open LineFamily SliceChart

/-- Exact FCC carrier incidence used by the Enterprise-coordinate correspondence. -/
def sliceLines : SliceChart → Finset LineFamily
  | A => {L1, L3, L6}
  | B => {L1, L4, L5}
  | C => {L2, L3, L5}
  | D => {L2, L4, L6}

/-- Every slice chart contains exactly three line families. -/
theorem sliceLines_card (s : SliceChart) : (sliceLines s).card = 3 := by
  fin_cases s <;> decide

/-- Slice incidence set of a line family. -/
def incidentSlices (l : LineFamily) : Finset SliceChart :=
  Finset.univ.filter fun s => l ∈ sliceLines s

/-- Every line family occurs in exactly two slice charts. -/
theorem incidentSlices_card (l : LineFamily) :
    (incidentSlices l).card = 2 := by
  fin_cases l <;> decide

/-- Any two distinct slice charts share exactly one line family. -/
theorem distinct_slice_intersection_card
    (s t : SliceChart) (hst : s ≠ t) :
    ((sliceLines s) ∩ (sliceLines t)).card = 1 := by
  fin_cases s <;> fin_cases t <;> simp_all [sliceLines]

/-- Any two distinct slice charts have a unique shared line family. -/
theorem existsUnique_sharedLine
    (s t : SliceChart) (hst : s ≠ t) :
    ∃! l : LineFamily, l ∈ sliceLines s ∧ l ∈ sliceLines t := by
  fin_cases s <;> fin_cases t <;> simp_all [sliceLines]

/-- The six unordered slice pairs recover the six line-family labels. -/
theorem shared_line_table :
    (L1 ∈ sliceLines A ∧ L1 ∈ sliceLines B) ∧
    (L3 ∈ sliceLines A ∧ L3 ∈ sliceLines C) ∧
    (L6 ∈ sliceLines A ∧ L6 ∈ sliceLines D) ∧
    (L5 ∈ sliceLines B ∧ L5 ∈ sliceLines C) ∧
    (L4 ∈ sliceLines B ∧ L4 ∈ sliceLines D) ∧
    (L2 ∈ sliceLines C ∧ L2 ∈ sliceLines D) := by
  decide

/-- The carrier incidence has four slice states. -/
theorem sliceChart_card : Fintype.card SliceChart = 4 := by
  decide

/-- The carrier incidence has six line-family states. -/
theorem lineFamily_card : Fintype.card LineFamily = 6 := by
  decide

/-- Double-counting the incidence flags gives `4·3 = 6·2`. -/
theorem incidence_double_count :
    Fintype.card SliceChart * 3 = Fintype.card LineFamily * 2 := by
  norm_num [sliceChart_card, lineFamily_card]

end EnterpriseMath.PrecisionPi.EnterpriseCoordinateIncidence
