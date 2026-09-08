import EnterpriseMath.Relation.BRCSixAxisS4
import EnterpriseMath.Relation.BRCAtlasPolynomialEmission
import EnterpriseMath.Relation.BRCFiniteTransition
import Mathlib.Data.Fintype.Option
import Mathlib.Data.Fintype.Prod
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- The concrete K4-derived atlas polynomial has six axis variables plus one
raw-length variable.  Weight moments live in the coefficient character rather
than consuming additional polynomial variables. -/
theorem k4AtlasPolynomial_variable_card :
    Fintype.card (Option K4Axis) = 7 := by
  rw [Fintype.card_option, k4Axis_card]
  norm_num

/-- With the full S4 atlas frame group retained, a finite state set `S` expands
to exactly `24 * |S|` state/frame indices (written here in product order). -/
theorem k4_stateFrame_card (S : Type*) [Fintype S] :
    Fintype.card (S × K4Frame) = Fintype.card S * 24 := by
  rw [Fintype.card_prod, k4Frame_card]

/-- Concrete polynomial emission for the six K4-derived axes and their S4 frame
action. -/
noncomputable def k4AtlasPolynomialEmission
    {W R : Type*} [Monoid W] [CommSemiring R]
    (χ : W →* R) :
    FrameEmission W K4Frame (CountAtlas K4Axis)
      (AtlasPolynomial K4Axis R) k4CountAction :=
  atlasPolynomialEmission k4CountAction χ

/-- Whole positive framed BRC mapped to a 24-frame ordinary polynomial matrix
for the concrete K4/S4 derived atlas. -/
noncomputable def k4AtlasPolynomialFrameLiftNBRC
    {W R : Type*} [Monoid W] [CommSemiring R]
    (χ : W →* R) :
    FramedNBRC W K4Frame (CountAtlas K4Axis) k4CountAction →ₐ[ℕ]
      Matrix K4Frame K4Frame (AtlasPolynomial K4Axis R) :=
  atlasPolynomialFrameLiftNBRC k4CountAction χ

end EnterpriseMath.BranchRecoalescence
