import Mathlib

namespace EnterpriseMath.FCCSliceIncidence

/-- Four overlapping three-line slice charts in the selected FCC carrier. -/
abbrev Slice := Fin 4

/-- Six stable unoriented FCC line families. -/
abbrev Line := Fin 6

/-- The four carrier slices, in the order
`A={L₁,L₃,L₆}`, `B={L₁,L₄,L₅}`, `C={L₂,L₃,L₅}`,
`D={L₂,L₄,L₆}`. -/
def sliceLines : Slice → Finset Line :=
  ![({0, 2, 5} : Finset Line),
    ({0, 3, 4} : Finset Line),
    ({1, 2, 4} : Finset Line),
    ({1, 3, 5} : Finset Line)]

/-- Each slice contains exactly three line families. -/
theorem sliceLines_card (s : Slice) : (sliceLines s).card = 3 := by
  fin_cases s <;> native_decide

/-- The two slices incident with each line family.  These are exactly the six
unordered pairs of four slice labels. -/
def lineSlices : Line → Finset Slice :=
  ![({0, 1} : Finset Slice),
    ({2, 3} : Finset Slice),
    ({0, 2} : Finset Slice),
    ({1, 3} : Finset Slice),
    ({1, 2} : Finset Slice),
    ({0, 3} : Finset Slice)]

/-- Each line family is shared by exactly two slices. -/
theorem lineSlices_card (l : Line) : (lineSlices l).card = 2 := by
  fin_cases l <;> native_decide

/-- The two incidence tables are mutually consistent. -/
theorem mem_sliceLines_iff_mem_lineSlices (s : Slice) (l : Line) :
    l ∈ sliceLines s ↔ s ∈ lineSlices l := by
  fin_cases s <;> fin_cases l <;> native_decide

/-- Distinct carrier slices share exactly one line family. -/
theorem distinct_slices_inter_card_one (s t : Slice) (h : s ≠ t) :
    ((sliceLines s) ∩ (sliceLines t)).card = 1 := by
  fin_cases s <;> fin_cases t <;> simp_all [sliceLines]

/-- Strong form: two distinct slices have a unique shared line family. -/
theorem existsUnique_sharedLine (s t : Slice) (h : s ≠ t) :
    ∃! l : Line, l ∈ sliceLines s ∧ l ∈ sliceLines t := by
  obtain ⟨l, hl⟩ :=
    Finset.card_eq_one.mp (distinct_slices_inter_card_one s t h)
  refine ⟨l, ?_, ?_⟩
  · have hlmem : l ∈ (sliceLines s) ∩ (sliceLines t) := by
      rw [hl]
      simp
    exact Finset.mem_inter.mp hlmem
  · intro m hm
    have hmmem : m ∈ (sliceLines s) ∩ (sliceLines t) :=
      Finset.mem_inter.mpr hm
    rw [hl] at hmmem
    simpa using hmmem

/-- No two line labels encode the same unordered pair of slices. -/
theorem lineSlices_injective : Function.Injective lineSlices := by
  native_decide

/-- Every unordered pair of distinct slices is represented by a unique line
family.  This is the exact `K₄` vertex-edge incidence statement. -/
theorem existsUnique_line_of_distinct_slices (s t : Slice) (h : s ≠ t) :
    ∃! l : Line, lineSlices l = {s, t} := by
  rcases existsUnique_sharedLine s t h with ⟨l, ⟨hls, hlt⟩, _⟩
  have hsl : s ∈ lineSlices l :=
    (mem_sliceLines_iff_mem_lineSlices s l).1 hls
  have htl : t ∈ lineSlices l :=
    (mem_sliceLines_iff_mem_lineSlices t l).1 hlt
  have hsubset : ({s, t} : Finset Slice) ⊆ lineSlices l := by
    intro u hu
    simp only [Finset.mem_insert, Finset.mem_singleton] at hu
    rcases hu with rfl | rfl
    · exact hsl
    · exact htl
  have hpairCard : ({s, t} : Finset Slice).card = 2 := by
    simp [h]
  have hline : lineSlices l = {s, t} := by
    symm
    apply Finset.eq_of_subset_of_card_le hsubset
    rw [lineSlices_card, hpairCard]
  refine ⟨l, hline, ?_⟩
  intro m hm
  apply lineSlices_injective
  exact hm.trans hline.symm

/-- Double-counting the carrier incidences gives `4·3 = 6·2 = 12`. -/
theorem incidence_double_count : 4 * 3 = 6 * 2 := by
  norm_num

end EnterpriseMath.FCCSliceIncidence
