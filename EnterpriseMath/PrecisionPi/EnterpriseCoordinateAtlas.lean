import Mathlib

namespace EnterpriseMath.PrecisionPi

/-- The six unoriented nearest-neighbour line families of the selected FCC
coordinate carrier.  They are carrier labels, not an identification with the
six native P000 axes. -/
inductive FCCLineFamily
  | L1 | L2 | L3 | L4 | L5 | L6
  deriving DecidableEq, Repr

/-- The four overlapping `120°` three-line slice charts of the FCC carrier. -/
inductive FCCSliceChart
  | SA | SB | SC | SD
  deriving DecidableEq, Repr

/-- Explicit finite carrier-line universe. -/
def allFCCLineFamilies : Finset FCCLineFamily :=
  {.L1, .L2, .L3, .L4, .L5, .L6}

/-- Explicit finite slice-chart universe. -/
def allFCCSliceCharts : Finset FCCSliceChart :=
  {.SA, .SB, .SC, .SD}

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

/-- The explicit selected carrier atlas contains exactly four slices. -/
theorem card_allFCCSliceCharts : allFCCSliceCharts.card = 4 := by
  native_decide

/-- The explicit selected carrier atlas contains exactly six line families. -/
theorem card_allFCCLineFamilies : allFCCLineFamilies.card = 6 := by
  native_decide

/-- Every declared slice occurs in the explicit atlas universe. -/
theorem mem_allFCCSliceCharts (s : FCCSliceChart) :
    s ∈ allFCCSliceCharts := by
  cases s <;> native_decide

/-- Every declared line occurs in the explicit carrier universe. -/
theorem mem_allFCCLineFamilies (l : FCCLineFamily) :
    l ∈ allFCCLineFamilies := by
  cases l <;> native_decide

/-- Every carrier slice contains exactly three line families. -/
theorem slice_lines_card (s : FCCSliceChart) : s.lines.card = 3 := by
  cases s <;> native_decide

/-- Every carrier line family belongs to exactly two slice charts. -/
theorem line_slices_card (l : FCCLineFamily) : l.slices.card = 2 := by
  cases l <;> native_decide

/-- The two incidence tables are exact transposes of one another. -/
theorem carrier_incidence_duality
    (s : FCCSliceChart) (l : FCCLineFamily) :
    l ∈ s.lines ↔ s ∈ l.slices := by
  cases s <;> cases l <;>
    native_decide

/-- Any two distinct slice charts share exactly one line family.  Thus the
four charts are the vertices and the six line families are the edges of a
complete tetrahedral incidence graph `K₄`. -/
theorem distinct_slices_share_one_line
    (s t : FCCSliceChart) (h : s ≠ t) :
    (s.lines ∩ t.lines).card = 1 := by
  cases s <;> cases t <;>
    simp_all [FCCSliceChart.lines]

/-- Conversely, each line family is the unique edge joining its two incident
slice charts. -/
theorem distinct_lines_have_distinct_slice_pairs
    (l r : FCCLineFamily) (h : l ≠ r) :
    l.slices ≠ r.slices := by
  revert h
  cases l <;> cases r <;>
    native_decide

/-- The total slice-line incidence count is `4*3=12=6*2`. -/
theorem carrier_incidence_count :
    (∑ s ∈ allFCCSliceCharts, s.lines.card) =
      ∑ l ∈ allFCCLineFamilies, l.slices.card := by
  native_decide

end EnterpriseMath.PrecisionPi
