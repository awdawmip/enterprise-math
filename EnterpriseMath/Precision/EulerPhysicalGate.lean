import EnterpriseMath.Precision.EulerCellRadiusBisector

namespace EnterpriseMath.Precision.EulerPhysicalGate

open EnterpriseMath.Precision.EulerCellRadiusBisector

section

variable {A : Type*} [CommRing A]
variable (R r : A)

/-- The physical gate displacement is one Cell radius times the unit gate-ray character. -/
def physicalGate : A := r * gateRotor R r

/-- Under the Cell-radius relation, the physical gate is exactly one third of
    the sum of its two adjacent unit center directions, expressed without division. -/
theorem three_mul_physicalGate
    (hr : 3 * r ^ 2 = 1) :
    3 * physicalGate R r = 2 + R := by
  unfold physicalGate gateRotor
  calc
    3 * (r * (r * (2 + R))) = (3 * r ^ 2) * (2 + R) := by ring
    _ = 2 + R := by rw [hr]; ring

end

end EnterpriseMath.Precision.EulerPhysicalGate
