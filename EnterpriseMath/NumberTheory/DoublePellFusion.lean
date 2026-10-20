import Mathlib

namespace EnterpriseMath.PrecisionPi.DoublePellFusion

/-- The two signed residual shells multiply to the even fused shell. -/
theorem signed_shell_norm {R : Type*} [CommRing R] (u : R) :
    (1 - u) * (1 + u) = 1 - u ^ 2 := by
  ring

/-- At inverse-square residual `u = P⁻²`, fusion starts at fourth order. -/
theorem inverse_square_shell_norm (P : ℚ) :
    (1 - (1 / P) ^ 2) * (1 + (1 / P) ^ 2) =
      1 - (1 / P) ^ 4 := by
  ring

/--
If one longitudinal coordinate supports a positive and a negative Pell shell,
the product of their transverse squared lengths is exactly `P⁴ - 1`.
-/
theorem paired_pell_factorization
    {P dPos yPos dNeg yNeg : ℤ}
    (hPos : P ^ 2 - dPos * yPos ^ 2 = 1)
    (hNeg : P ^ 2 - dNeg * yNeg ^ 2 = -1) :
    (dPos * yPos ^ 2) * (dNeg * yNeg ^ 2) = P ^ 4 - 1 := by
  have hp : dPos * yPos ^ 2 = P ^ 2 - 1 := by
    linarith
  have hn : dNeg * yNeg ^ 2 = P ^ 2 + 1 := by
    linarith
  rw [hp, hn]
  ring

/-- The positive and negative shells at `P = 99`. -/
theorem n58_paired_pell :
    (99 : ℤ) ^ 2 - 2 * 70 ^ 2 = 1 ∧
      (99 : ℤ) ^ 2 - 58 * 13 ^ 2 = -1 := by
  norm_num

/-- Their product is the fourth-order fused residual numerator. -/
theorem n58_transverse_product :
    ((2 : ℤ) * 70 ^ 2) * (58 * 13 ^ 2) = 99 ^ 4 - 1 := by
  exact paired_pell_factorization n58_paired_pell.1 n58_paired_pell.2

/-- The N=58 CM residual denominator is the fourth power of the Pell projection. -/
theorem n58_fourth_power : (99 : ℕ) ^ 4 = 96_059_601 := by
  norm_num

/-- Ramanujan's denominator `396` is four times the Pell projection `99`. -/
theorem n58_396 : (396 : ℕ) = 4 * 99 := by
  norm_num

/-- The standard denominator square is the same Pell projection squared. -/
theorem n58_9801 : (9_801 : ℕ) = 99 ^ 2 := by
  norm_num

end EnterpriseMath.PrecisionPi.DoublePellFusion
