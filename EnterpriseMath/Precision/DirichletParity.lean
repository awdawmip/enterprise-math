import EnterpriseMath.Precision.SpectralPrecision

namespace EnterpriseMath.Precision

/--
WSR-L13: addition law for the finite Dirichlet continuants.

This is the transfer-matrix multiplication law written entirely at recurrence level:
`D_(m+n+2) = D_(m+1) D_(n+1) - D_m D_n`.
-/
theorem dirichletContinuant_addition (z : ℝ) (m n : ℕ) :
    dirichletContinuant z (m + n + 2) =
      dirichletContinuant z (m + 1) * dirichletContinuant z (n + 1) -
        dirichletContinuant z m * dirichletContinuant z n := by
  induction n using Nat.twoStepInduction with
  | zero =>
      simp only [Nat.add_zero]
      rw [show m + 2 = m + 2 by rfl, dirichletContinuant]
      simp [dirichletContinuant]
      ring
  | one =>
      norm_num only [Nat.reduceAdd]
      change dirichletContinuant z (m + 3) =
        dirichletContinuant z (m + 1) * dirichletContinuant z 2 -
          dirichletContinuant z m * dirichletContinuant z 1
      rw [show m + 3 = (m + 1) + 2 by omega, dirichletContinuant]
      rw [dirichletContinuant]
      simp [dirichletContinuant]
      ring
  | more n ih0 ih1 =>
      have ih0' :
          dirichletContinuant z (m + n + 2) =
            dirichletContinuant z (m + 1) * dirichletContinuant z (n + 1) -
              dirichletContinuant z m * dirichletContinuant z n := by
        simpa [Nat.add_assoc] using ih0
      have ih1' :
          dirichletContinuant z (m + n + 3) =
            dirichletContinuant z (m + 1) * dirichletContinuant z (n + 2) -
              dirichletContinuant z m * dirichletContinuant z (n + 1) := by
        simpa [Nat.add_assoc] using ih1
      have hn2 :
          dirichletContinuant z (n + 2) =
            (2 - z) * dirichletContinuant z (n + 1) - dirichletContinuant z n := by
        rw [dirichletContinuant]
      have hn3 :
          dirichletContinuant z (n + 3) =
            (2 - z) * dirichletContinuant z (n + 2) - dirichletContinuant z (n + 1) := by
        change dirichletContinuant z ((n + 1) + 2) = _
        rw [dirichletContinuant]
      change dirichletContinuant z (m + n + 4) =
        dirichletContinuant z (m + 1) * dirichletContinuant z (n + 3) -
          dirichletContinuant z m * dirichletContinuant z (n + 2)
      rw [show m + n + 4 = (m + n + 2) + 2 by omega, dirichletContinuant]
      rw [ih1', ih0', hn3, hn2]
      ring

/--
WSR-L14: odd-length Dirichlet characteristic continuants factor into the two
midpoint-reflection parity factors without introducing trigonometric eigenvectors.
-/
theorem dirichletContinuant_odd_factorization (z : ℝ) (n : ℕ) :
    dirichletContinuant z (2 * n + 3) =
      dirichletContinuant z (n + 1) *
        (dirichletContinuant z (n + 2) - dirichletContinuant z n) := by
  have h := dirichletContinuant_addition z (n + 1) n
  rw [show (n + 1) + n + 2 = 2 * n + 3 by omega] at h
  nlinarith

/-- At zero spectral parameter, the first parity factor is exactly `n+2`. -/
theorem dirichletParityFirst_zero (n : ℕ) :
    dirichletContinuant 0 (n + 1) = ((n + 2 : ℕ) : ℝ) := by
  rw [dirichletContinuant_zero]
  push_cast
  ring

/-- At zero spectral parameter, the complementary parity factor is exactly `2`. -/
theorem dirichletParitySecond_zero (n : ℕ) :
    dirichletContinuant 0 (n + 2) - dirichletContinuant 0 n = 2 := by
  rw [dirichletContinuant_zero, dirichletContinuant_zero]
  push_cast
  ring

/--
The zero-parameter odd-chain determinant factorization has parity-sector values
`n+2` and `2`; with `q=n+2`, these are the #1159 factors `q` and `2`.
-/
theorem dirichletContinuant_odd_zero_factorization (n : ℕ) :
    dirichletContinuant 0 (2 * n + 3) = ((n + 2 : ℕ) : ℝ) * 2 := by
  rw [dirichletContinuant_odd_factorization,
    dirichletParityFirst_zero, dirichletParitySecond_zero]

end EnterpriseMath.Precision
