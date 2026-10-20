import EnterpriseMath.Geometry.FCCSliceAngles
import EnterpriseMath.Geometry.FCCSliceRotation

namespace EnterpriseMath.PrecisionPi.FCCCarrierRotation

open FCCSliceAngles FCCSliceIncidence FCCSliceRotation

def rotateCarrier3 (v : CarrierVec) : CarrierVec := ![v 2, v 0, v 1]
def rotateCarrier4 (v : CarrierVec) : CarrierVec := ![-v 2, v 1, v 0]
def rotateCarrier3Inv (v : CarrierVec) : CarrierVec := ![v 1, v 2, v 0]
def rotateCarrier4Inv (v : CarrierVec) : CarrierVec := ![v 2, v 1, -v 0]

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

theorem rotateCarrier3_dot (x y : CarrierVec) :
    dot (rotateCarrier3 x) (rotateCarrier3 y) = dot x y := by
  simp [dot, rotateCarrier3]
  ring

theorem rotateCarrier4_dot (x y : CarrierVec) :
    dot (rotateCarrier4 x) (rotateCarrier4 y) = dot x y := by
  simp [dot, rotateCarrier4]
  ring

theorem rotateCarrier3_normSq (x : CarrierVec) :
    normSq (rotateCarrier3 x) = normSq x := rotateCarrier3_dot x x

theorem rotateCarrier4_normSq (x : CarrierVec) :
    normSq (rotateCarrier4 x) = normSq x := rotateCarrier4_dot x x

def rotate3LineSign : Line → ℤ := ![1, 1, 1, -1, 1, -1]
def rotate4LineSign : Line → ℤ := ![1, -1, -1, 1, -1, 1]

theorem rotateCarrier3_canonicalLine :
    ∀ l : Line, ∀ c : Fin 3,
      rotateCarrier3 (canonicalLine l) c =
        rotate3LineSign l * canonicalLine (rotate3Line l) c := by
  native_decide

theorem rotateCarrier4_canonicalLine :
    ∀ l : Line, ∀ c : Fin 3,
      rotateCarrier4 (canonicalLine l) c =
        rotate4LineSign l * canonicalLine (rotate4Line l) c := by
  native_decide

theorem rotateCarrier3_order_three (v : CarrierVec) :
    rotateCarrier3 (rotateCarrier3 (rotateCarrier3 v)) = v := by
  funext c
  fin_cases c <;> rfl

theorem rotateCarrier4_order_four (v : CarrierVec) :
    rotateCarrier4 (rotateCarrier4 (rotateCarrier4 (rotateCarrier4 v))) = v := by
  funext c
  fin_cases c <;> simp [rotateCarrier4]

end EnterpriseMath.PrecisionPi.FCCCarrierRotation
