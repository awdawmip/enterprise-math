import Mathlib

namespace EnterpriseMath.PrecisionPi

/-- Two Pell shells at one longitudinal coordinate multiply to a quartic shell.

This is the integer identity underlying the paired Ramanujan coordinates:
`(P^2 - 1)(P^2 + 1) = P^4 - 1` after substituting the positive and
negative Pell equations. -/
theorem doublePell_quartic_fusion
    (P dPos qPos dNeg qNeg : ℤ)
    (hPos : P ^ 2 - dPos * qPos ^ 2 = 1)
    (hNeg : P ^ 2 - dNeg * qNeg ^ 2 = -1) :
    dPos * dNeg * (qPos * qNeg) ^ 2 = P ^ 4 - 1 := by
  have hPos' : dPos * qPos ^ 2 = P ^ 2 - 1 := by
    linarith
  have hNeg' : dNeg * qNeg ^ 2 = P ^ 2 + 1 := by
    linarith
  rw [mul_pow]
  calc
    dPos * dNeg * (qPos ^ 2 * qNeg ^ 2) =
        (dPos * qPos ^ 2) * (dNeg * qNeg ^ 2) := by ring
    _ = (P ^ 2 - 1) * (P ^ 2 + 1) := by rw [hPos', hNeg']
    _ = P ^ 4 - 1 := by ring

/-- Paired positive and negative Pell shells produce a norm-one quadratic datum
whose half-trace is the integer square `P^2`. -/
theorem doublePell_squareHalfTrace_norm_one
    (P dPos qPos dNeg qNeg : ℤ)
    (hPos : P ^ 2 - dPos * qPos ^ 2 = 1)
    (hNeg : P ^ 2 - dNeg * qNeg ^ 2 = -1) :
    (P ^ 2) ^ 2 - dPos * dNeg * (qPos * qNeg) ^ 2 = 1 := by
  have hfusion :=
    doublePell_quartic_fusion P dPos qPos dNeg qNeg hPos hNeg
  calc
    (P ^ 2) ^ 2 - dPos * dNeg * (qPos * qNeg) ^ 2 =
        P ^ 4 - dPos * dNeg * (qPos * qNeg) ^ 2 := by ring
    _ = 1 := by linarith

/-- Abstract `C₂` shell norm: conjugate signed quadratic shells cancel all odd
residual powers and leave the quartic shell. -/
theorem signedShell_norm (u : ℚ) :
    (1 - u ^ 2) * (1 + u ^ 2) = 1 - u ^ 4 := by
  ring

/-- The `N = 58` double-Pell fusion certificate. -/
theorem doublePell58_quartic_fusion :
    (2 : ℤ) * 58 * (70 * 13) ^ 2 = 99 ^ 4 - 1 := by
  exact doublePell_quartic_fusion 99 2 70 58 13
    (by norm_num) (by norm_num)

/-- The associated `N = 58` square-half-trace datum has norm one. -/
theorem doublePell58_squareHalfTrace_norm_one :
    ((99 : ℤ) ^ 2) ^ 2 - 2 * 58 * (70 * 13) ^ 2 = 1 := by
  exact doublePell_squareHalfTrace_norm_one 99 2 70 58 13
    (by norm_num) (by norm_num)

/-- The squarefree class-invariant presentation of the same norm-one datum. -/
theorem classInvariant58_norm_one :
    (9801 : ℤ) ^ 2 - 29 * 1820 ^ 2 = 1 := by
  norm_num

/-- The `P = 7` paired shell in Ramanujan's quartic table. -/
theorem doublePell7_quartic_fusion :
    (3 : ℤ) * 2 * (4 * 5) ^ 2 = 7 ^ 4 - 1 := by
  exact doublePell_quartic_fusion 7 3 4 2 5
    (by norm_num) (by norm_num)

/-- The `P = 3` paired shell in Ramanujan's quartic table. -/
theorem doublePell3_quartic_fusion :
    (2 : ℤ) * 10 * (2 * 1) ^ 2 = 3 ^ 4 - 1 := by
  exact doublePell_quartic_fusion 3 2 2 10 1
    (by norm_num) (by norm_num)

end EnterpriseMath.PrecisionPi
