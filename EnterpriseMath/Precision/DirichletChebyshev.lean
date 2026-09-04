import EnterpriseMath.Precision.SpectralPrecision
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Chebyshev.RootsExtrema

namespace EnterpriseMath.Precision

open Polynomial

/--
Finite effective compatibility bridge for the #1159 Dirichlet carrier.

The native continuant remains recurrence-defined.  This theorem is a downstream
classical readout: its value is the Chebyshev polynomial of the second kind at
`1 - z/2`.  No Chebyshev/trigonometric input is used by the native determinant,
decimation, or compact-error theorems.
-/
theorem dirichletContinuant_eq_chebyshevU (z : ℝ) (n : ℕ) :
    dirichletContinuant z n =
      (Polynomial.Chebyshev.U ℝ (n : ℤ)).eval (1 - z / 2) := by
  induction n using Nat.twoStepInduction with
  | zero =>
      simp [dirichletContinuant]
  | one =>
      simp [dirichletContinuant]
      ring
  | more n ih0 ih1 =>
      rw [dirichletContinuant]
      have h2 : ((n + 2 : ℕ) : ℤ) = (n : ℤ) + 2 := by omega
      have h1 : ((n + 1 : ℕ) : ℤ) = (n : ℤ) + 1 := by omega
      rw [h2, Polynomial.Chebyshev.U_add_two]
      simp only [eval_sub, eval_mul, eval_ofNat, eval_X]
      rw [← h1, ← ih1, ← ih0]
      ring

end EnterpriseMath.Precision
