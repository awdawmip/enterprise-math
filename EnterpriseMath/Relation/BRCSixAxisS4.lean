import EnterpriseMath.Relation.BRCCountAtlas
import Mathlib.Data.Fintype.Powerset
import Mathlib.Data.Fintype.Perm
import Mathlib.Data.Finset.Image
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- The four K4 chart vertices used by the executable six-axis atlas source. -/
abbrev K4Vertex := Fin 4

/-- The complete vertex-permutation frame group, i.e. S4. -/
abbrev K4Frame := Equiv.Perm K4Vertex

/-- A six-axis label is an unordered two-element subset of the four K4 vertices.
This is the structural version of the executable source ordering
`(AB, AC, AD, BC, BD, CD)`; no native Cell ontology is asserted here. -/
abbrev K4Axis := {s : Finset K4Vertex // s.card = 2}

/-- K4 has exactly six unordered edges/derived axis labels. -/
theorem k4Axis_card : Fintype.card K4Axis = 6 := by
  rw [Fintype.card_finset_len]
  native_decide

/-- The complete K4 vertex-frame group has 24 elements. -/
theorem k4Frame_card : Fintype.card K4Frame = 24 := by
  rw [Fintype.card_perm]
  norm_num

/-- A concrete axis witness, used only to expose nonemptiness to the generic
CountAtlas minimum construction. -/
def k4Axis01 : K4Axis :=
  ⟨{(0 : K4Vertex), (1 : K4Vertex)}, by decide⟩

instance : Nonempty K4Axis := ⟨k4Axis01⟩

/-- A vertex permutation transports an unordered K4 edge by finite-set image. -/
noncomputable def k4AxisPerm (g : K4Frame) : Equiv.Perm K4Axis :=
  (g.finsetCongr).subtypeEquiv (fun s => by
    simp [Equiv.finsetCongr_apply])

@[simp] theorem k4AxisPerm_apply_val (g : K4Frame) (e : K4Axis) :
    (k4AxisPerm g e).1 = g.finsetCongr e.1 := rfl

@[simp] theorem k4AxisPerm_one :
    k4AxisPerm (1 : K4Frame) = 1 := by
  apply Equiv.ext
  intro e
  apply Subtype.ext
  simp [k4AxisPerm, Equiv.finsetCongr_apply]

@[simp] theorem k4AxisPerm_mul (g h : K4Frame) :
    k4AxisPerm (g * h) = k4AxisPerm g * k4AxisPerm h := by
  apply Equiv.ext
  intro e
  apply Subtype.ext
  simp [k4AxisPerm, Equiv.finsetCongr_apply, Finset.map_map,
    Equiv.Perm.mul_apply]

/-- The executable source's `edge_action` is structurally a group homomorphism
from S4 vertex frames to permutations of the six unordered K4 edges. -/
noncomputable def k4AxisAction : K4Frame →* Equiv.Perm K4Axis where
  toFun := k4AxisPerm
  map_one' := k4AxisPerm_one
  map_mul' := k4AxisPerm_mul

/-- Pull back count coordinates along a declared permutation action.  This is the
generic algebraic form of executable `rotate_axes`: old coordinates are moved to
their permuted axis labels. -/
noncomputable def coordinateActionOfPermHom {G ι : Type*} [Monoid G]
    (σ : G →* Equiv.Perm ι) : CoordinateAction G (CountAtlas ι) where
  act g n i := n ((σ g).symm i)
  one_act n := by
    funext i
    change n (((σ 1)⁻¹) i) = n i
    rw [map_one]
    rfl
  mul_act g h n := by
    funext i
    change n (((σ (g * h))⁻¹) i) =
      n (((σ h)⁻¹) (((σ g)⁻¹) i))
    rw [map_mul, mul_inv_rev, Equiv.Perm.mul_apply]
  act_zero g := by
    funext i
    rfl
  act_add g n m := by
    funext i
    rfl

/-- A pullback action induced by axis permutations satisfies the exact
`CoordinateReindexing` hypothesis required by the generic CountAtlas theorems. -/
theorem coordinateActionOfPermHom_reindexing {G ι : Type*} [Monoid G]
    (σ : G →* Equiv.Perm ι) :
    CoordinateReindexing (coordinateActionOfPermHom σ) := by
  intro g
  refine ⟨(σ g).symm, ?_⟩
  intro n i
  rfl

/-- Concrete S4 action on the six K4-derived count axes. -/
noncomputable def k4CountAction : CoordinateAction K4Frame (CountAtlas K4Axis) :=
  coordinateActionOfPermHom k4AxisAction

/-- The concrete S4/K4 six-axis action discharges the generic reindexing
hypothesis without an enumerated 24-by-6 action table. -/
theorem k4CountAction_reindexing : CoordinateReindexing k4CountAction := by
  exact coordinateActionOfPermHom_reindexing k4AxisAction

/-- Common depth is invariant under the concrete S4 six-axis action. -/
theorem k4_commonDepth_invariant (g : K4Frame) (n : CountAtlas K4Axis) :
    commonDepth (k4CountAction.act g n) = commonDepth n := by
  exact commonDepth_act k4CountAction k4CountAction_reindexing g n

/-- Canonical six-axis normalization commutes with the concrete S4 action. -/
theorem k4_normalizeAtlas_equivariant (g : K4Frame) (n : CountAtlas K4Axis) :
    normalizeAtlas (k4CountAction.act g n) =
      k4CountAction.act g (normalizeAtlas n) := by
  exact normalizeAtlas_act k4CountAction k4CountAction_reindexing g n

/-- The common-depth BRC carry for the concrete S4 six-axis action is
nonnegative. -/
theorem k4_commonDepthCarry_nonneg {W : Type*} [Monoid W]
    (a b : FramedPath W K4Frame (CountAtlas K4Axis) k4CountAction) :
    0 ≤ commonDepthCarry a b := by
  exact commonDepthCarry_nonneg k4CountAction_reindexing a b

/-- The concrete S4 six-axis common-depth carry is invariant under global frame
relabeling. -/
theorem k4_commonDepthCarry_relabel {W : Type*} [Monoid W]
    (s : K4Frame)
    (a b : FramedPath W K4Frame (CountAtlas K4Axis) k4CountAction) :
    commonDepthCarry (FramedPath.relabel k4CountAction s a)
        (FramedPath.relabel k4CountAction s b) =
      commonDepthCarry a b := by
  exact commonDepthCarry_relabel k4CountAction_reindexing s a b

end EnterpriseMath.BranchRecoalescence
