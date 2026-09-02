import EnterpriseMath.Geometry.FCCSliceIncidence
import EnterpriseMath.Precision.TetrahedralResidual

namespace EnterpriseMath.PrecisionPi.FCCResidualBridge

open FCCSliceIncidence

/-- Tetrahedral edge labels in the order used by the residual matrix. -/
abbrev Edge := Fin 6

/--
Convert the residual edge order `01,02,03,23,13,12` to the canonical carrier
line order `L₁,…,L₆` (zero based).
-/
def edgeToLine : Edge → Line :=
  ![0, 2, 5, 1, 3, 4]

/-- The inverse conversion from carrier line order to residual edge order. -/
def lineToEdge : Line → Edge :=
  ![0, 3, 1, 4, 5, 2]

/-- The two order conversions are inverse in the edge-to-line direction. -/
theorem lineToEdge_edgeToLine (e : Edge) :
    lineToEdge (edgeToLine e) = e := by
  fin_cases e <;> native_decide

/-- The two order conversions are inverse in the line-to-edge direction. -/
theorem edgeToLine_lineToEdge (l : Line) :
    edgeToLine (lineToEdge l) = l := by
  fin_cases l <;> native_decide

/-- The endpoint charts of each residual edge. -/
def edgeEndpoints : Edge → Finset Slice :=
  ![({0, 1} : Finset Slice),
    ({0, 2} : Finset Slice),
    ({0, 3} : Finset Slice),
    ({2, 3} : Finset Slice),
    ({1, 3} : Finset Slice),
    ({1, 2} : Finset Slice)]

/-- Each residual edge has exactly two slice-chart endpoints. -/
theorem edgeEndpoints_card_two (e : Edge) : (edgeEndpoints e).card = 2 := by
  fin_cases e <;> native_decide

/--
The endpoints assigned by the residual matrix are exactly the two FCC charts
containing the corresponding carrier line family.
-/
theorem incidentSlices_edgeToLine (e : Edge) :
    incidentSlices (edgeToLine e) = edgeEndpoints e := by
  fin_cases e <;> native_decide

/-- Every carrier line obtains exactly the endpoints of its inverse edge label. -/
theorem incidentSlices_eq_edgeEndpoints (l : Line) :
    incidentSlices l = edgeEndpoints (lineToEdge l) := by
  rw [← incidentSlices_edgeToLine (lineToEdge l)]
  rw [edgeToLine_lineToEdge]

/-- Two distinct charts are the endpoints of their unique common line. -/
theorem common_line_has_expected_endpoints
    (s t : Slice) (hst : s ≠ t) :
    ∀ l ∈ commonLines s t, incidentSlices l = {s, t} := by
  intro l hl
  have hls : l ∈ sliceLines s := by
    exact (Finset.mem_inter.mp hl).1
  have hlt : l ∈ sliceLines t := by
    exact (Finset.mem_inter.mp hl).2
  have hs : s ∈ incidentSlices l := (mem_incidentSlices_iff l s).2 hls
  have ht : t ∈ incidentSlices l := (mem_incidentSlices_iff l t).2 hlt
  apply Finset.eq_of_subset_of_card_le
  · intro u hu
    simp only [Finset.mem_insert, Finset.mem_singleton] at hu ⊢
    rcases hu with rfl | rfl
    · exact hs
    · exact ht
  · simpa [line_incidence_card_two l]

end EnterpriseMath.PrecisionPi.FCCResidualBridge
