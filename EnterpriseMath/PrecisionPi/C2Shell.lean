import EnterpriseMath.PrecisionPi.PairedPell
import EnterpriseMath.PrecisionPi.TetrahedralNormalForm

namespace EnterpriseMath.PrecisionPi.C2Shell

open PairedPell

/-- The two signed residual shells carried by one `C₂` label. -/
def signedShell (ε : Bool) (u : ℚ) : ℚ :=
  if ε then 1 + u else 1 - u

/-- `C₂` conjugation exchanges the two shell signs. -/
def conjugate (ε : Bool) : Bool := !ε

@[simp] theorem conjugate_involutive (ε : Bool) :
    conjugate (conjugate ε) = ε := by
  cases ε <;> rfl

/-- The scalar norm of the two conjugate shells is `1-u²`. -/
theorem signedShell_norm (ε : Bool) (u : ℚ) :
    signedShell ε u * signedShell (conjugate ε) u = 1 - u ^ 2 := by
  cases ε <;> simp [signedShell, conjugate] <;> ring

/-- Averaging the two shell amplitudes removes the odd residual coordinate. -/
theorem signedShell_trace (u : ℚ) :
    (signedShell false u + signedShell true u) / 2 = 1 := by
  simp [signedShell]

/-- Their difference isolates the odd residual coordinate. -/
theorem signedShell_antitrace (u : ℚ) :
    (signedShell true u - signedShell false u) / 2 = u := by
  simp [signedShell]

/-- At a Pell residual `u=P⁻²`, the `C₂` norm is exactly the quartic shell `1-P⁻⁴`. -/
theorem pell_residual_shell_norm {P : ℚ} (hP : P ≠ 0) (ε : Bool) :
    signedShell ε (1 / P ^ 2) *
      signedShell (conjugate ε) (1 / P ^ 2) =
      1 - 1 / P ^ 4 := by
  rw [signedShell_norm]
  field_simp [hP]
  ring

/-- The N=58 shell norm is the exact quartic residual at `P=99`. -/
theorem n58_shell_norm (ε : Bool) :
    signedShell ε (1 / (99 : ℚ) ^ 2) *
      signedShell (conjugate ε) (1 / (99 : ℚ) ^ 2) =
      1 - 1 / (99 : ℚ) ^ 4 := by
  exact pell_residual_shell_norm (by norm_num) ε

/-- The shell label and the tetrahedral normal-form parity use the same abstract two-state
carrier, without asserting that the two native invariants have already been identified. -/
def shellOfNormalFormParity (ε : Bool) (u : ℚ) : ℚ :=
  signedShell ε u

@[simp] theorem shellOfNormalFormParity_false (u : ℚ) :
    shellOfNormalFormParity false u = 1 - u := by
  simp [shellOfNormalFormParity, signedShell]

@[simp] theorem shellOfNormalFormParity_true (u : ℚ) :
    shellOfNormalFormParity true u = 1 + u := by
  simp [shellOfNormalFormParity, signedShell]

end EnterpriseMath.PrecisionPi.C2Shell
