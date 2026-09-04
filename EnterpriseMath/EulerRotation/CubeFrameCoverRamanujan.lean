import EnterpriseMath.EulerRotation.FccO2ChiralityGlobalization
import EnterpriseMath.EulerRotation.TetrahedralSphericalHolonomy

namespace EnterpriseMath.EulerRotation.CubeFrameCoverRamanujan

namespace TH

open TetrahedralSphericalHolonomy

/-- One of the eight states in the central half-turn frame cover. -/
@[ext]
structure FrameState where
  slice : Slice
  sheet : Bool
  deriving DecidableEq, Fintype

/-- Boolean sign code for one vertex of the three-cube. `true` denotes a minus sign. -/
@[ext]
structure CubeCode where
  x : Bool
  y : Bool
  z : Bool
  deriving DecidableEq, Fintype

/-- The four zero-sheet tetrahedral codes. -/
def baseCubeCode : Slice → CubeCode
  | .A => ⟨false, true, true⟩
  | .B => ⟨true, false, true⟩
  | .C => ⟨true, true, false⟩
  | .D => ⟨false, false, false⟩

def complementCode (c : CubeCode) : CubeCode :=
  ⟨!c.x, !c.y, !c.z⟩

/-- The sheet bit is represented by the antipodal map of the cube. -/
def cubeCode (s : FrameState) : CubeCode :=
  if s.sheet then complementCode (baseCubeCode s.slice) else baseCubeCode s.slice

/-- Deck transformation of the two-sheet frame cover. -/
def deck (s : FrameState) : FrameState :=
  ⟨s.slice, !s.sheet⟩

/-- One lifted K₄ edge changes the slice and toggles the central frame sheet. -/
def liftedAdjacent (left right : FrameState) : Prop :=
  left.slice ≠ right.slice ∧ left.sheet ≠ right.sheet

instance (left right : FrameState) : Decidable (liftedAdjacent left right) :=
  inferInstance

def bitDistance (left right : Bool) : Nat :=
  if left = right then 0 else 1

def hammingDistance (left right : CubeCode) : Nat :=
  bitDistance left.x right.x + bitDistance left.y right.y + bitDistance left.z right.z

def cubeAdjacent (left right : CubeCode) : Prop :=
  hammingDistance left right = 1

instance (left right : CubeCode) : Decidable (cubeAdjacent left right) :=
  inferInstance

/-- The eight frame states are exactly the eight cube vertices. -/
theorem cubeCode_injective : Function.Injective cubeCode := by
  native_decide

theorem cubeCode_surjective : Function.Surjective cubeCode := by
  native_decide

/-- Explicit finite equivalence between the K₄ frame cover and Q₃ vertices. -/
noncomputable def frameCubeEquiv : FrameState ≃ CubeCode :=
  Equiv.ofBijective cubeCode ⟨cubeCode_injective, cubeCode_surjective⟩

/-- Cover edges are exactly cube edges. -/
theorem liftedAdjacent_iff_cubeAdjacent :
    ∀ left right : FrameState,
      liftedAdjacent left right ↔ cubeAdjacent (cubeCode left) (cubeCode right) := by
  native_decide

/-- The deck involution is encoded by the antipodal/complement map. -/
theorem cubeCode_deck :
    ∀ state : FrameState,
      cubeCode (deck state) = complementCode (cubeCode state) := by
  native_decide

/-- Lift one base edge by toggling the frame sheet. -/
def liftStep (state : FrameState) (target : Slice) : FrameState :=
  ⟨target, !state.sheet⟩

/-- Endpoint of a lifted triangular face path. -/
def faceLiftEnd (source middle target : Slice) (sheet : Bool) : FrameState :=
  liftStep (liftStep (liftStep ⟨source, sheet⟩ middle) target) source

/-- Every three-edge face path reaches the deck partner, not the original sheet. -/
theorem faceLiftEnd_eq_deck :
    ∀ source middle target : Slice, source ≠ middle → middle ≠ target → target ≠ source →
      ∀ sheet : Bool,
        faceLiftEnd source middle target sheet = deck ⟨source, sheet⟩ := by
  native_decide

/-- The scaled tangent half-turn is an involution after division by three. -/
theorem scaledHalfTurn_squared :
    ∀ source : Slice,
      matMul (scaledHalfTurn source) (scaledHalfTurn source) = matScale 9 matId := by
  native_decide

/-- Shortest edge transport carries the source half-turn to the target half-turn. -/
theorem scaledRotation_intertwines_halfTurn :
    ∀ source target : Slice, source ≠ target →
      matMul (scaledRotation source target) (scaledHalfTurn source) =
        matMul (scaledHalfTurn target) (scaledRotation source target) := by
  native_decide

/-- A two-edge path through a third tetrahedral vertex differs from the direct
edge by the source tangent half-turn. -/
theorem scaled_two_edge_shortcut :
    ∀ source middle target : Slice,
      source ≠ middle → middle ≠ target → target ≠ source →
      matMul (scaledRotation middle target) (scaledRotation source middle) =
        matMul (scaledRotation source target) (scaledHalfTurn source) := by
  native_decide

/-- The normalized vector face holonomy has order two.  Both sides carry the
common scale `27²=729`. -/
theorem scaled_face_holonomy_order_two :
    ∀ source middle target : Slice,
      source ≠ middle → middle ≠ target → target ≠ source →
      matMul (scaledFaceHolonomy source middle target)
        (scaledFaceHolonomy source middle target) = matScale 729 matId := by
  native_decide

/-- The normalized Spin face holonomy has order four: the displayed integral
identity has scale `(3*sqrt 3)^4=729`. -/
theorem faceSpinor_fourth_power :
    ∀ source middle target : Slice,
      source ≠ middle → middle ≠ target → target ≠ source →
      let q := faceSpinor source middle target
      qmul (qmul q q) (qmul q q) = ⟨729, 0, 0, 0⟩ := by
  native_decide

end TH

namespace CurvatureClass

open FccO2ChiralityGlobalization

/-- The fully symmetric central phase cochain: every K₄ edge has value one. -/
def allEdgeParity : EdgeCochain :=
  ⟨true, true, true, true, true, true⟩

def zeroHolonomy : HolonomyCode := ⟨false, false, false⟩
def allFaceHolonomy : HolonomyCode := ⟨true, true, true⟩

/-- Adjacent transposition A↔B on edge cochains. -/
def swapAB (e : EdgeCochain) : EdgeCochain :=
  ⟨e.ab, e.bc, e.bd, e.ac, e.ad, e.cd⟩

/-- Adjacent transposition B↔C on edge cochains. -/
def swapBC (e : EdgeCochain) : EdgeCochain :=
  ⟨e.ac, e.ab, e.ad, e.bc, e.cd, e.bd⟩

/-- Adjacent transposition C↔D on edge cochains. -/
def swapCD (e : EdgeCochain) : EdgeCochain :=
  ⟨e.ab, e.ad, e.ac, e.bd, e.bc, e.cd⟩

/-- Being fixed as a gauge class by the three adjacent transpositions generating S₄. -/
def FixedByS4Generators (e : EdgeCochain) : Prop :=
  holonomyCode (swapAB e) = holonomyCode e ∧
  holonomyCode (swapBC e) = holonomyCode e ∧
  holonomyCode (swapCD e) = holonomyCode e

instance (e : EdgeCochain) : Decidable (FixedByS4Generators e) :=
  inferInstance

/-- The all-edge parity class has nonzero holonomy on every tetrahedral face. -/
theorem allEdgeParity_code :
    holonomyCode allEdgeParity = allFaceHolonomy := by
  native_decide

/-- In H¹(K₄;F₂), the only classes fixed by the full tetrahedral permutation
group are zero and the all-face half-turn class. -/
theorem unique_nonzero_S4_fixed_class :
    ∀ e : EdgeCochain,
      FixedByS4Generators e ↔
        holonomyCode e = zeroHolonomy ∨ holonomyCode e = allFaceHolonomy := by
  native_decide

end CurvatureClass

namespace AbstractPathUpdate

/-- Power by one Boolean bit. -/
def bitPow {G : Type*} [Group G] (h : G) : Bool → G
  | false => 1
  | true => h

section

variable {G V : Type*} [Group G]
variable (T : V → V → G) (H : V → G)

/-- Appending an edge to a third endpoint toggles the central half-turn bit. -/
theorem extend_to_third
    (source middle target : V) (phase : Bool) (P : G)
    (hpath : P = T source middle * bitPow (H source) phase)
    (htriangle : T middle target * T source middle = T source target * H source)
    (hhalf : H source * H source = 1) :
    T middle target * P = T source target * bitPow (H source) (!phase) := by
  cases phase <;> simp [bitPow] at hpath ⊢
  · rw [hpath, ← mul_assoc, htriangle]
  · rw [hpath, ← mul_assoc, htriangle]
    group

/-- Returning along the direct inverse edge preserves the current bit; as a
closed-path exponent this is the same as adding two. -/
theorem extend_back_to_source
    (source middle : V) (phase : Bool) (P : G)
    (hpath : P = T source middle * bitPow (H source) phase)
    (hback : T middle source * T source middle = 1) :
    T middle source * P = bitPow (H source) phase := by
  rw [hpath, ← mul_assoc, hback]
  simp

end

end AbstractPathUpdate

end EnterpriseMath.EulerRotation.CubeFrameCoverRamanujan
