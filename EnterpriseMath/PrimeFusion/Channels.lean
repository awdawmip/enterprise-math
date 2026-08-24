import Mathlib

namespace EnterpriseMath.PrimeFusion

/-- The Gaussian / native squared-length channel. -/
def N (a b : ℤ) : ℤ := a ^ 2 + b ^ 2

/-- The Eisenstein / triangular-carrier channel. -/
def C (a b : ℤ) : ℤ := a ^ 2 - a * b + b ^ 2

/-- Sum diagonal coordinate. -/
def u (a b : ℤ) : ℤ := a + b

/-- Difference diagonal coordinate. -/
def v (a b : ℤ) : ℤ := a - b

/-- T1: `2N = u² + v²`. -/
theorem two_mul_N_eq_u_sq_add_v_sq (a b : ℤ) :
    2 * N a b = u a b ^ 2 + v a b ^ 2 := by
  simp [N, u, v]
  ring

/-- T1: `4C = u² + 3v²`. -/
theorem four_mul_C_eq_u_sq_add_three_v_sq (a b : ℤ) :
    4 * C a b = u a b ^ 2 + 3 * v a b ^ 2 := by
  simp [C, u, v]
  ring

/-- T1 converse: `u² = 3N - 2C`. -/
theorem u_sq_eq_three_N_sub_two_C (a b : ℤ) :
    u a b ^ 2 = 3 * N a b - 2 * C a b := by
  simp [N, C, u]
  ring

/-- T1 converse: `v² = 2C - N`. -/
theorem v_sq_eq_two_C_sub_N (a b : ℤ) :
    v a b ^ 2 = 2 * C a b - N a b := by
  simp [N, C, v]
  ring

/-- The exact T1 square pair, exported for later reconstruction work. -/
theorem diagonal_square_pair (a b : ℤ) :
    u a b ^ 2 = 3 * N a b - 2 * C a b ∧
      v a b ^ 2 = 2 * C a b - N a b :=
  ⟨u_sq_eq_three_N_sub_two_C a b, v_sq_eq_two_C_sub_N a b⟩

end EnterpriseMath.PrimeFusion
