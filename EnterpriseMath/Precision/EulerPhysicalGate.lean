import EnterpriseMath.Precision.EulerCellRadiusBisector

namespace EnterpriseMath.Precision.EulerPhysicalGate

open EnterpriseMath.Precision.EulerCellRadiusBisector

section

variable {A : Type*} [CommRing A]
variable (R r : A)

/-- The physical gate displacement is one Cell radius times the unit gate-ray character. -/
def physicalGate : A := r * gateRotor R r

/-- Under the Cell-radius relation, the physical gate is exactly one third of
    the sum of its two adjacent unit center directions. -/
theorem three_mul_physicalGate
    (hr : 3 * r ^ 2 = 1) :
    3 * physicalGate R r = 2 + R := by
  unfold physicalGate gateRotor
  calc
    3 * (r * (r * (2 + R))) = (3 * r ^ 2) * (2 + R) := by ring
    _ = 2 + R := by rw [hr]; ring

/-- Equivalently, any `g` satisfying `3g = 2+R` is the same physical gate
    whenever multiplication by three is cancellable. -/
theorem physicalGate_unique
    [NoZeroSMulDivisors ℕ A]
    (hr : 3 * r ^ 2 = 1)
    {g : A}
    (hg : 3 * g = 2 + R) :
    g = physicalGate R r := by
  have hgate : 3 * physicalGate R r = 2 + R :=
    three_mul_physicalGate (R := R) (r := r) hr
  have hthree : (3 : A) * g = (3 : A) * physicalGate R r := by
    simpa only [Nat.cast_ofNat] using hg.trans hgate.symm
  exact (nsmul_left_cancel (R := A) (n := 3) (by norm_num) hthree)

end

end EnterpriseMath.Precision.EulerPhysicalGate
