import Mathlib

namespace EnterpriseMath.PrecisionPi.TraceAntitrace

variable {K : Type*} [Field K] [CharZero K]

def halfTrace (u : K) : K := (u + u⁻¹) / 2
def halfAntiTrace (u : K) : K := (u - u⁻¹) / 2

theorem trace_antitrace_identity (u : K) (hu : u ≠ 0) :
    halfTrace u ^ 2 - halfAntiTrace u ^ 2 = 1 := by
  unfold halfTrace halfAntiTrace
  field_simp [hu]
  ring

theorem square_halfTrace_forces_fourth_residual
    (u P : K) (hu : u ≠ 0) (htrace : halfTrace u = P ^ 2) :
    halfAntiTrace u ^ 2 = P ^ 4 - 1 := by
  have h := trace_antitrace_identity u hu
  calc
    halfAntiTrace u ^ 2 = halfTrace u ^ 2 - 1 := by linarith
    _ = (P ^ 2) ^ 2 - 1 := by rw [htrace]
    _ = P ^ 4 - 1 := by ring

theorem fourth_residual_shell_factorization (P : K) :
    P ^ 4 - 1 = (P ^ 2 - 1) * (P ^ 2 + 1) := by
  ring

theorem square_halfTrace_double_shell
    (u P : K) (hu : u ≠ 0) (htrace : halfTrace u = P ^ 2) :
    halfAntiTrace u ^ 2 = (P ^ 2 - 1) * (P ^ 2 + 1) := by
  rw [square_halfTrace_forces_fourth_residual u P hu htrace]
  exact fourth_residual_shell_factorization P

theorem halfTrace_inv (u : K) : halfTrace u⁻¹ = halfTrace u := by
  unfold halfTrace
  rw [inv_inv]
  ring

theorem halfAntiTrace_inv (u : K) : halfAntiTrace u⁻¹ = -halfAntiTrace u := by
  unfold halfAntiTrace
  rw [inv_inv]
  ring

end EnterpriseMath.PrecisionPi.TraceAntitrace
