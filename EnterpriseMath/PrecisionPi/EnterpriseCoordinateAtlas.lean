import Mathlib

namespace EnterpriseMath.PrecisionPi

/-- The six unoriented nearest-neighbour line families of the selected FCC
coordinate carrier.  They are carrier labels, not an identification with the
six native P000 axes. -/
inductive FCCLineFamily
  | L1 | L2 | L3 | L4 | L5 | L6
  deriving DecidableEq, Fintype, Repr

/-- The four overlapping `120°` three-line slice charts of the FCC carrier. -/
inductive FCCSliceChart
  | SA | SB | SC | SD
  deriving DecidableEq, Fintype, Repr

/-- Carrier-line content of each overlapping slice chart. -/
def FCCSliceChart.lines : FCCSliceChart → Finset FCCLineFamily
  | .SA => {.L1, .L3, .L6}
  | .SB => {.L1, .L4, .L5}
  | .SC => {.L2, .L3, .L5}
  | .SD => {.L2, .L4, .L6}

/-- Slice-chart endpoints of each carrier line family. -/
def FCCLineFamily.slices : FCCLineFamily → Finset FCCSliceChart
  | .L1 => {.SA, .SB}
  | .L2 => {.SC, .SD}
  | .L3 => {.SA, .SC}
  | .L4 => {.SB, .SD}
  | .L5 => {.SB, .SC}
  | .L6 => {.SA, .SD}

/-- There are exactly four slice charts in the selected carrier atlas. -/
theorem card_FCCSliceChart : Fintype.card FCCSliceChart = 4 := by
  native_decide

/-- There are exactly six stable unoriented line families. -/
theorem card_FCCLineFamily : Fintype.card FCCLineFamily = 6 := by
  native_decide

/-- Every carrier slice contains exactly three line families. -/
theorem slice_lines_card (s : FCCSliceChart) : s.lines.card = 3 := by
  cases s <;> native_decide

/-- Every carrier line family belongs to exactly two slice charts. -/
theorem line_slices_card (l : FCCLineFamily) : l.slices.card = 2 := by
  cases l <;> native_decide

/-- The two incidence tables are exact transposes of one another. -/
theorem carrier_incidence_duality :
    ∀ s : FCCSliceChart, ∀ l : FCCLineFamily,
      l ∈ s.lines ↔ s ∈ l.slices := by
  native_decide

/-- Any two distinct slice charts share exactly one line family.  Thus the
four charts are the vertices and the six line families are the edges of a
complete tetrahedral incidence graph `K₄`. -/
theorem distinct_slices_share_one_line :
    ∀ s t : FCCSliceChart, s ≠ t → (s.lines ∩ t.lines).card = 1 := by
  native_decide

/-- Conversely, each line family is the unique edge joining its two incident
slice charts. -/
theorem distinct_lines_have_distinct_slice_pairs :
    ∀ l r : FCCLineFamily, l ≠ r → l.slices ≠ r.slices := by
  native_decide

/-- The total slice-line incidence count is `4*3=12=6*2`. -/
theorem carrier_incidence_count :
    (∑ s : FCCSliceChart, s.lines.card) =
      ∑ l : FCCLineFamily, l.slices.card := by
  native_decide

end EnterpriseMath.PrecisionPi
