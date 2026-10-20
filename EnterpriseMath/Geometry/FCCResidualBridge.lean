import EnterpriseMath.Geometry.FCCSliceIncidence
import EnterpriseMath.Precision.TetrahedralResidual

namespace EnterpriseMath.PrecisionPi.FCCResidualBridge

open FCCSliceIncidence

abbrev Edge := Fin 6

/-- Residual edge order `01,02,03,23,13,12` to canonical line order `L₁,…,L₆`. -/
def edgeToLine : Edge → Line :=
  ![0, 2, 5, 1, 3, 4]

/-- The inverse order conversion. -/
def lineToEdge : Line → Edge :=
  ![0, 3, 1, 4, 5, 2]

theorem lineToEdge_edgeToLine : ∀ e : Edge,
    lineToEdge (edgeToLine e) = e := by
  native_decide

theorem edgeToLine_lineToEdge : ∀ l : Line,
    edgeToLine (lineToEdge l) = l := by
  native_decide

/-- Endpoints in the residual edge order. -/
def edgeEndpoints : Edge → Finset Slice :=
  ![({0, 1} : Finset Slice),
    ({0, 2} : Finset Slice),
    ({0, 3} : Finset Slice),
    ({2, 3} : Finset Slice),
    ({1, 3} : Finset Slice),
    ({1, 2} : Finset Slice)]

theorem edgeEndpoints_card_two : ∀ e : Edge,
    (edgeEndpoints e).card = 2 := by
  native_decide

/-- The residual endpoints equal the two FCC charts containing the carrier line. -/
theorem incidentSlices_edgeToLine : ∀ e : Edge,
    incidentSlices (edgeToLine e) = edgeEndpoints e := by
  native_decide

theorem incidentSlices_eq_edgeEndpoints (l : Line) :
    incidentSlices l = edgeEndpoints (lineToEdge l) := by
  rw [← incidentSlices_edgeToLine (lineToEdge l)]
  rw [edgeToLine_lineToEdge]

/-- The unique common line of two distinct charts has exactly those endpoints. -/
theorem common_line_has_expected_endpoints :
    ∀ s t : Slice, s ≠ t →
      ∀ l : Line, l ∈ commonLines s t → incidentSlices l = {s, t} := by
  native_decide

end EnterpriseMath.PrecisionPi.FCCResidualBridge
