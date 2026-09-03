import EnterpriseMath.Precision.EulerCellRadiusBisector

namespace EnterpriseMath.Precision.EulerCayleyBridge

section

variable {A : Type*} [CommRing A]
variable (c s t J : A)

/-- The two Cayley factors associated with the parameter `t`. -/
def cayleyNumerator : A := 1 + J * t

def cayleyDenominator : A := 1 - J * t

/-- Under `J^2=-1`, conjugate Cayley factors have scalar product `1+t^2`. -/
theorem cayley_factor_product (hJ : J ^ 2 = -1) :
    cayleyNumerator t J * cayleyDenominator t J = 1 + t ^ 2 := by
  unfold cayleyNumerator cayleyDenominator
  calc
    (1 + J * t) * (1 - J * t) =
        1 + t ^ 2 - t ^ 2 * (J ^ 2 + 1) := by ring
    _ = 1 + t ^ 2 := by
      rw [hJ]
      ring

/-- A unit state `c+sJ` is reconstructed by its Cayley half-phase coordinate,
    in a denominator-free cross-multiplied form. -/
theorem cayley_reconstruct_cross
    (hJ : J ^ 2 = -1)
    (hunit : c ^ 2 + s ^ 2 = 1) :
    ((1 + c) - s * J) * (c + s * J) = (1 + c) + s * J := by
  calc
    ((1 + c) - s * J) * (c + s * J) =
        ((1 + c) + s * J) + (c ^ 2 + s ^ 2 - 1) -
          s ^ 2 * (J ^ 2 + 1) := by ring
    _ = (1 + c) + s * J := by
      rw [hunit, hJ]
      ring

/-- The finite lower/upper squeeze width identity, written without division. -/
theorem squeeze_width_cross
    {P Q : A}
    (hQ : Q * (1 + c) = 2 * P) :
    (Q - P) * (1 + c) = P * (1 - c) := by
  calc
    (Q - P) * (1 + c) = Q * (1 + c) - P * (1 + c) := by ring
    _ = 2 * P - P * (1 + c) := by rw [hQ]
    _ = P * (1 - c) := by ring

/-- The half-phase square is `(1-c)/(1+c)`, again cross-multiplied. -/
theorem half_phase_square_cross
    (hunit : c ^ 2 + s ^ 2 = 1)
    (ht : t * (1 + c) = s) :
    t ^ 2 * (1 + c) ^ 2 = (1 - c) * (1 + c) := by
  have hs : s ^ 2 = 1 - c ^ 2 := by
    calc
      s ^ 2 = (c ^ 2 + s ^ 2) - c ^ 2 := by ring
      _ = 1 - c ^ 2 := by rw [hunit]
  calc
    t ^ 2 * (1 + c) ^ 2 = (t * (1 + c)) ^ 2 := by ring
    _ = s ^ 2 := by rw [ht]
    _ = 1 - c ^ 2 := hs
    _ = (1 - c) * (1 + c) := by ring

end

end EnterpriseMath.Precision.EulerCayleyBridge
