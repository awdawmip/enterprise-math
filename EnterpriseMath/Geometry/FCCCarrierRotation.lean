import EnterpriseMath.Geometry.FCCSliceAngles
import EnterpriseMath.Geometry.FCCSliceRotation

namespace EnterpriseMath.PrecisionPi.FCCCarrierRotation

open FCCSliceAngles FCCSliceIncidence FCCSliceRotation

/-- Order-three coordinate rotation `(x,y,z) ↦ (z,x,y)`. -/
def rotateCarrier3 (v : CarrierVec) : CarrierVec :=
  ![v 2, v 0, v 1]

/-- Order-four orientation-preserving signed permutation `(x,y,z) ↦ (-z,y,x)`. -/
def rotateCarrier4 (v : CarrierVec) : CarrierVec :=
  ![-v 2, v 1, v 0]

/-- Inverses of the two displayed rotations. -/
def rotateCarrier3Inv (v : CarrierVec) : CarrierVec :=
  ![v 1, v 2, v 0]

def rotateCarrier4Inv (v : CarrierVec) : CarrierVec :=
  ![v 2, v 1, -v 0]

/-- Both carrier maps are genuine bijections. -/
theorem rotateCarrier3_inverse_left (v : CarrierVec) :
    rotateCarrier3Inv (rotateCarrier3 v) = v := by
  funext c
  fin_cases c <;> rfl

theorem rotateCarrier3_inverse_right (v : CarrierVec) :
    rotateCarrier3 (rotateCarrier3Inv v) = v := by
  funext c
  fin_cases c <;> rfl

theorem rotateCarrier4_inverse_left (v : CarrierVec) :
    rotateCarrier4Inv (rotateCarrier4 v) = v := by
  funext c
  fin_cases c <;> simp [rotateCarrier4Inv, rotateCarrier4]

theorem rotateCarrier4_inverse_right (v : CarrierVec) :
    rotateCarrier4 (rotateCarrier4Inv v) = v := by
  funext c
  fin_cases c <;> simp [rotateCarrier4Inv, rotateCarrier4]

/-- Both rotations preserve the integral dot product. -/
theorem rotateCarrier3_dot (x y : CarrierVec) :
    dot (rotateCarrier3 x) (rotateCarrier3 y) = dot x y := by
  simp [dot, rotateCarrier3]
  ring

theorem rotateCarrier4_dot (x y : CarrierVec) :
    dot (rotateCarrier4 x) (rotateCarrier4 y) = dot x y := by
  simp [dot, rotateCarrier4]
  ring

/-- Consequently both rotations preserve squared norm. -/
theorem rotateCarrier3_normSq (x : CarrierVec) :
    normSq (rotateCarrier3 x) = normSq x := by
  exact rotateCarrier3_dot x x

theorem rotateCarrier4_normSq (x : CarrierVec) :
    normSq (rotateCarrier4 x) = normSq x := by
  exact rotateCarrier4_dot x x

/-- Local signs needed because line families are unoriented. -/
def rotate3LineSign : Line → ℤ := ![1, 1, 1, -1, 1, -1]
def rotate4LineSign : Line → ℤ := ![1, -1, -1, 1, -1, 1]

/-- The order-three rotation realizes the declared line-family permutation. -/
theorem rotateCarrier3_canonicalLine :
    ∀ l : Line, ∀ c : Fin 3,
      rotateCarrier3 (canonicalLine l) c =
        rotate3LineSign l * canonicalLine (rotate3Line l) c := by
  native_decide

/-- The order-four rotation realizes the declared line-family permutation. -/
theorem rotateCarrier4_canonicalLine :
    ∀ l : Line, ∀ c : Fin 3,
      rotateCarrier4 (canonicalLine l) c =
        rotate4LineSign l * canonicalLine (rotate4Line l) c := by
  native_decide

/-- Three applications of `R₃` return every carrier vector. -/
theorem rotateCarrier3_order_three (v : CarrierVec) :
    rotateCarrier3 (rotateCarrier3 (rotateCarrier3 v)) = v := by
  funext c
  fin_cases c <;> rfl

/-- Four applications of `R₄` return every carrier vector. -/
theorem rotateCarrier4_order_four (v : CarrierVec) :
    rotateCarrier4 (rotateCarrier4 (rotateCarrier4 (rotateCarrier4 v))) = v := by
  funext c
  fin_cases c <;> simp [rotateCarrier4]

end EnterpriseMath.PrecisionPi.FCCCarrierRotation
