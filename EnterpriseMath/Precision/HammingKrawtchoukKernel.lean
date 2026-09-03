import Mathlib.Algebra.Polynomial.Derivative

namespace EnterpriseMath.Precision

open Polynomial

/--
Two-sided binomial generating polynomial.  In shell coordinates `j` for an
`m`-cube, the choice `a=j`, `b=m-j` gives
`(1-X)^j (1+X)^(m-j)`.
-/
def hammingBasisPoly (a b : ℕ) : ℚ[X] :=
  (1 - X) ^ a * (1 + X) ^ b

/--
WSR-L44: interior Hamming-shell generating identity, written in offset
coordinates `a=j-1`, `b=m-j-1` so no truncated subtraction appears.
-/
theorem hammingBasisPoly_interior_kernel (a b : ℕ) :
    C ((a + 1 : ℕ) : ℚ) * hammingBasisPoly a (b + 2) +
        C ((b + 1 : ℕ) : ℚ) * hammingBasisPoly (a + 2) b =
      C ((a + b + 2 : ℕ) : ℚ) * hammingBasisPoly (a + 1) (b + 1) -
        C (2 : ℚ) * (X * derivative (hammingBasisPoly (a + 1) (b + 1))) := by
  unfold hammingBasisPoly
  simp [Polynomial.derivative_mul, Polynomial.derivative_pow_succ]
  ring

/-- Left endpoint (`j=0`) generating identity. -/
theorem hammingBasisPoly_left_kernel (b : ℕ) :
    C ((b + 1 : ℕ) : ℚ) * hammingBasisPoly 1 b =
      C ((b + 1 : ℕ) : ℚ) * hammingBasisPoly 0 (b + 1) -
        C (2 : ℚ) * (X * derivative (hammingBasisPoly 0 (b + 1))) := by
  unfold hammingBasisPoly
  simp [Polynomial.derivative_mul, Polynomial.derivative_pow_succ]
  ring

/-- Right endpoint (`j=m`) generating identity. -/
theorem hammingBasisPoly_right_kernel (a : ℕ) :
    C ((a + 1 : ℕ) : ℚ) * hammingBasisPoly a 1 =
      C ((a + 1 : ℕ) : ℚ) * hammingBasisPoly (a + 1) 0 -
        C (2 : ℚ) * (X * derivative (hammingBasisPoly (a + 1) 0)) := by
  unfold hammingBasisPoly
  simp [Polynomial.derivative_mul, Polynomial.derivative_pow_succ]
  ring

/-- Coefficient of the Euler operator `X d/dX`. -/
theorem coeff_X_mul_derivative (p : ℚ[X]) (k : ℕ) :
    (X * derivative p).coeff k = (k : ℚ) * p.coeff k := by
  cases k with
  | zero => simp
  | succ k =>
      rw [show Nat.succ k = k + 1 by rfl, coeff_X_mul, coeff_derivative]
      push_cast
      ring

/-- Krawtchouk-mode coefficient in two-sided exponent coordinates. -/
def hammingModeCoeff (a b k : ℕ) : ℚ :=
  (hammingBasisPoly a b).coeff k

/--
WSR-L45: coefficient form of the interior shell eigen-recurrence.
Here `m=a+b+2` and `j=a+1`.
-/
theorem hammingModeCoeff_interior (a b k : ℕ) :
    ((a + 1 : ℕ) : ℚ) * hammingModeCoeff a (b + 2) k +
        ((b + 1 : ℕ) : ℚ) * hammingModeCoeff (a + 2) b k =
      (((a + b + 2 : ℕ) : ℚ) - 2 * (k : ℚ)) *
        hammingModeCoeff (a + 1) (b + 1) k := by
  have h := congrArg (fun p : ℚ[X] => p.coeff k)
    (hammingBasisPoly_interior_kernel a b)
  simp only [coeff_add, coeff_sub, coeff_C_mul, hammingModeCoeff] at h
  rw [coeff_X_mul_derivative] at h
  push_cast at h ⊢
  linarith

/-- Coefficient form of the left boundary eigen-recurrence. -/
theorem hammingModeCoeff_left (b k : ℕ) :
    ((b + 1 : ℕ) : ℚ) * hammingModeCoeff 1 b k =
      (((b + 1 : ℕ) : ℚ) - 2 * (k : ℚ)) *
        hammingModeCoeff 0 (b + 1) k := by
  have h := congrArg (fun p : ℚ[X] => p.coeff k)
    (hammingBasisPoly_left_kernel b)
  simp only [coeff_sub, coeff_C_mul, hammingModeCoeff] at h
  rw [coeff_X_mul_derivative] at h
  push_cast at h ⊢
  linarith

/-- Coefficient form of the right boundary eigen-recurrence. -/
theorem hammingModeCoeff_right (a k : ℕ) :
    ((a + 1 : ℕ) : ℚ) * hammingModeCoeff a 1 k =
      (((a + 1 : ℕ) : ℚ) - 2 * (k : ℚ)) *
        hammingModeCoeff (a + 1) 0 k := by
  have h := congrArg (fun p : ℚ[X] => p.coeff k)
    (hammingBasisPoly_right_kernel a)
  simp only [coeff_sub, coeff_C_mul, hammingModeCoeff] at h
  rw [coeff_X_mul_derivative] at h
  push_cast at h ⊢
  linarith

end EnterpriseMath.Precision
