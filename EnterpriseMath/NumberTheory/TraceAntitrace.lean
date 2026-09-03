import Mathlib

namespace EnterpriseMath.PrecisionPi.TraceAntitrace

variable {K : Type*} [Field K]

/-- Symmetric coordinate of an invertible CM/unit parameter. -/
def halfTrace (u : K) : K := (u + u⁻¹) / 2

/-- Antisymmetric coordinate of an invertible CM/unit parameter. -/
def halfAntiTrace (u : K) : K := (u - u⁻¹) / 2

/-- The two signed shells are the two linear factors of the fourth residual. -/
theorem fourth_residual_shell_factorization (P : K) :
    P ^ 4 - 1 = (P ^ 2 - 1) * (P ^ 2 + 1) := by
  ring

/-- Reversal `u ↦ u⁻¹` fixes half-trace and negates half-antitrace. -/
theorem halfTrace_inv (u : K) :
    halfTrace u⁻¹ = halfTrace u := by
  unfold halfTrace
  rw [inv_inv]
  ring

theorem halfAntiTrace_inv (u : K) :
    halfAntiTrace u⁻¹ = -halfAntiTrace u := by
  unfold halfAntiTrace
  rw [inv_inv]
  ring

section CharacteristicZero

variable [CharZero K]

/-- The trace-antitrace hyperbola identity. -/
theorem trace_antitrace_identity (u : K) (hu : u ≠ 0) :
    halfTrace u ^ 2 - halfAntiTrace u ^ 2 = 1 := by
  unfold halfTrace halfAntiTrace
  field_simp [hu]
  ring

/-- Equivalent norm-one form of the trace-antitrace identity. -/
theorem halfTrace_sq_eq_one_add_halfAntiTrace_sq (u : K) (hu : u ≠ 0) :
    halfTrace u ^ 2 = 1 + halfAntiTrace u ^ 2 := by
  have h := trace_antitrace_identity u hu
  linear_combination h

/--
If the half-trace is an exact square `P²`, then the squared half-antitrace is
forced to be `P⁴-1`.
-/
theorem square_halfTrace_forces_fourth_residual
    (u P : K) (hu : u ≠ 0) (htrace : halfTrace u = P ^ 2) :
    halfAntiTrace u ^ 2 = P ^ 4 - 1 := by
  have h := trace_antitrace_identity u hu
  calc
    halfAntiTrace u ^ 2 = halfTrace u ^ 2 - 1 := by
      linear_combination -h
    _ = P ^ 4 - 1 := by
      rw [htrace]
      ring

/-- Combined square-trace and shell-factorization statement. -/
theorem square_halfTrace_double_shell
    (u P : K) (hu : u ≠ 0) (htrace : halfTrace u = P ^ 2) :
    halfAntiTrace u ^ 2 = (P ^ 2 - 1) * (P ^ 2 + 1) := by
  rw [square_halfTrace_forces_fourth_residual u P hu htrace]
  exact fourth_residual_shell_factorization P

end CharacteristicZero

end EnterpriseMath.PrecisionPi.TraceAntitrace
