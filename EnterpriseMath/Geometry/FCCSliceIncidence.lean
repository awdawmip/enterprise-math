import Mathlib

namespace EnterpriseMath.PrecisionPi.FCCSliceIncidence

abbrev Line := Fin 6
abbrev Slice := Fin 4

/-- The four canonical overlapping 120-degree FCC carrier slices. -/
def sliceLines : Slice → Finset Line :=
  ![({0, 2, 5} : Finset Line),
    ({0, 3, 4} : Finset Line),
    ({1, 2, 4} : Finset Line),
    ({1, 3, 5} : Finset Line)]

theorem slice_card_three (s : Slice) : (sliceLines s).card = 3 := by
  fin_cases s <;> native_decide

def incidentSlices (l : Line) : Finset Slice :=
  Finset.univ.filter fun s => l ∈ sliceLines s

theorem line_incidence_card_two (l : Line) : (incidentSlices l).card = 2 := by
  fin_cases l <;> native_decide

def commonLines (s t : Slice) : Finset Line :=
  sliceLines s ∩ sliceLines t

theorem commonLines_card (s t : Slice) :
    (commonLines s t).card = if s = t then 3 else 1 := by
  fin_cases s <;> fin_cases t <;> native_decide

theorem distinct_slices_share_exactly_one (s t : Slice) (hst : s ≠ t) :
    (commonLines s t).card = 1 := by
  rw [commonLines_card, if_neg hst]

theorem mem_incidentSlices_iff (l : Line) (s : Slice) :
    s ∈ incidentSlices l ↔ l ∈ sliceLines s := by
  simp [incidentSlices]

theorem total_slice_incidence :
    ∑ s : Slice, (sliceLines s).card = 12 := by
  native_decide

theorem total_line_incidence :
    ∑ l : Line, (incidentSlices l).card = 12 := by
  native_decide

theorem incidence_double_count :
    ∑ s : Slice, (sliceLines s).card =
      ∑ l : Line, (incidentSlices l).card := by
  rw [total_slice_incidence, total_line_incidence]

theorem unordered_slice_pair_count :
    (Finset.univ.filter fun p : Slice × Slice => p.1 < p.2).card = 6 := by
  native_decide

end EnterpriseMath.PrecisionPi.FCCSliceIncidence
