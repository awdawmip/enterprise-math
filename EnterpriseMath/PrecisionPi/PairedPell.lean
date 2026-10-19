import Mathlib

namespace EnterpriseMath.PrecisionPi.PairedPell

/-- A positive Pell shell at longitudinal coordinate `P`. -/
def PositiveShell (P d y : ℤ) : Prop :=
  P ^ 2 - d * y ^ 2 = 1

/-- A negative Pell shell at the same longitudinal coordinate `P`. -/
def NegativeShell (P d y : ℤ) : Prop :=
  P ^ 2 - d * y ^ 2 = -1

/-- Positive and negative shells at one longitudinal coordinate multiply to a norm-one unit
whose rational coordinate is the square `P²`. -/
theorem paired_shells_compose_to_square_trace
    {P dPlus yPlus dMinus yMinus : ℤ}
    (hPlus : PositiveShell P dPlus yPlus)
    (hMinus : NegativeShell P dMinus yMinus) :
    (P ^ 2) ^ 2 - (dPlus * dMinus) * (yPlus * yMinus) ^ 2 = 1 := by
  have hp : dPlus * yPlus ^ 2 = P ^ 2 - 1 := by
    unfold PositiveShell at hPlus
    linarith
  have hm : dMinus * yMinus ^ 2 = P ^ 2 + 1 := by
    unfold NegativeShell at hMinus
    linarith
  calc
    (P ^ 2) ^ 2 - (dPlus * dMinus) * (yPlus * yMinus) ^ 2 =
        (P ^ 2) ^ 2 - (dPlus * yPlus ^ 2) * (dMinus * yMinus ^ 2) := by ring
    _ = (P ^ 2) ^ 2 - (P ^ 2 - 1) * (P ^ 2 + 1) := by rw [hp, hm]
    _ = 1 := by ring

/-- The two Pell shells are exactly the two factors of the square-trace norm equation. -/
theorem paired_shell_factorization
    {P dPlus yPlus dMinus yMinus : ℤ}
    (hPlus : PositiveShell P dPlus yPlus)
    (hMinus : NegativeShell P dMinus yMinus) :
    P ^ 4 - 1 = (dPlus * dMinus) * (yPlus * yMinus) ^ 2 := by
  have h := paired_shells_compose_to_square_trace hPlus hMinus
  calc
    P ^ 4 - 1 = (P ^ 2) ^ 2 - 1 := by ring
    _ = (dPlus * dMinus) * (yPlus * yMinus) ^ 2 := by linarith

/-- Polynomial form of the fused residual-shell norm. -/
theorem shell_norm_polynomial (P : ℤ) :
    (P ^ 2 - 1) * (P ^ 2 + 1) = P ^ 4 - 1 := by
  ring

/-- Rational normalized form: the product of the two signed quadratic shells is quartic. -/
theorem shell_norm_rational {P : ℚ} (hP : P ≠ 0) :
    (1 - 1 / P ^ 2) * (1 + 1 / P ^ 2) = 1 - 1 / P ^ 4 := by
  field_simp [hP]
  ring

/-- N=58 positive shell at `P=99`. -/
theorem n58_positive_shell : PositiveShell 99 2 70 := by
  norm_num [PositiveShell]

/-- N=58 negative shell at `P=99`. -/
theorem n58_negative_shell : NegativeShell 99 58 13 := by
  norm_num [NegativeShell]

/-- The paired N=58 shells produce the norm-one square-trace coordinate `99²`. -/
theorem n58_square_trace_norm :
    ((99 : ℤ) ^ 2) ^ 2 - (2 * 58) * (70 * 13) ^ 2 = 1 := by
  exact paired_shells_compose_to_square_trace
    n58_positive_shell n58_negative_shell

/-- N=18 positive shell at `P=7`. -/
theorem n18_positive_shell : PositiveShell 7 3 4 := by
  norm_num [PositiveShell]

/-- N=18 negative shell at `P=7`. -/
theorem n18_negative_shell : NegativeShell 7 2 5 := by
  norm_num [NegativeShell]

/-- N=10 positive shell at `P=3`. -/
theorem n10_positive_shell : PositiveShell 3 2 2 := by
  norm_num [PositiveShell]

/-- N=10 negative shell at `P=3`. -/
theorem n10_negative_shell : NegativeShell 3 10 1 := by
  norm_num [NegativeShell]

end EnterpriseMath.PrecisionPi.PairedPell
