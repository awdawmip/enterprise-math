import EnterpriseMath.Precision.HammingParityDeterminant
import Mathlib.Data.Nat.Prime.Basic

namespace EnterpriseMath.Precision

open scoped BigOperators

/--
Arithmetic prime-birth indices inside the genuine finite Krawtchouk spectrum
`0,1,...,m`.  This is deliberately distinct from the historical #1159 name
`hammingEvenPrimeIndex`, where "prime" meant the positive-even/pseudodeterminant
block rather than arithmetic primality.
-/
def HammingArithmeticBirthIndex (m : ℕ) :=
  {k : Fin (m + 1) // Nat.Prime k.val}

/-- Inclusion of arithmetic prime-birth indices into the full Krawtchouk basis. -/
def hammingArithmeticBirthIndex (m : ℕ) :
    HammingArithmeticBirthIndex m ↪ Fin (m + 1) where
  toFun k := k.1
  inj' := by
    intro a b h
    exact Subtype.ext h

/-- Every selected arithmetic birth index is genuinely prime. -/
theorem hammingArithmeticBirthIndex_prime
    (m : ℕ) (k : HammingArithmeticBirthIndex m) :
    Nat.Prime (hammingArithmeticBirthIndex m k).val := by
  exact k.2

/-- Every arithmetic birth basis vector remains a genuine Krawtchouk eigenvector. -/
theorem hammingArithmeticBirthBasis_eigen
    (m : ℕ) (k : HammingArithmeticBirthIndex m) :
    hammingShellKFin m
        (hammingKrawtchoukBasis m (hammingArithmeticBirthIndex m k)) =
      ((hammingArithmeticBirthIndex m k).val : ℚ) •
        hammingKrawtchoukBasis m (hammingArithmeticBirthIndex m k) := by
  simpa only [hammingKrawtchoukBasis_apply] using
    hammingShellKFin_mode m (hammingArithmeticBirthIndex m k).val (by omega)

/--
Literal arithmetic prime-birth block of the actual finite Hamming/Krawtchouk
operator, expressed as the corresponding principal submatrix in the proved
Krawtchouk eigenbasis.
-/
noncomputable def hammingArithmeticBirthRestrictedMatrix (m : ℕ) :
    Matrix (HammingArithmeticBirthIndex m)
      (HammingArithmeticBirthIndex m) ℚ :=
  (hammingKrawtchoukMatrix m).submatrix
    (hammingArithmeticBirthIndex m) (hammingArithmeticBirthIndex m)

/-- The arithmetic birth block is exactly diagonal on the selected prime modes. -/
theorem hammingArithmeticBirthRestrictedMatrix_eq_diagonal (m : ℕ) :
    hammingArithmeticBirthRestrictedMatrix m =
      Matrix.diagonal fun k => ((hammingArithmeticBirthIndex m k).val : ℚ) := by
  classical
  unfold hammingArithmeticBirthRestrictedMatrix
  rw [hammingKrawtchoukMatrix_eq_diagonal,
    Matrix.submatrix_diagonal _ _ (hammingArithmeticBirthIndex m).injective]
  rfl

/--
The literal determinant of the arithmetic birth block is the exact finite
product of all prime Krawtchouk eigenvalues visible at cutoff `m`.
-/
theorem hammingArithmeticBirthRestrictedMatrix_det (m : ℕ) :
    (hammingArithmeticBirthRestrictedMatrix m).det =
      ∏ k : HammingArithmeticBirthIndex m,
        ((hammingArithmeticBirthIndex m k).val : ℚ) := by
  classical
  rw [hammingArithmeticBirthRestrictedMatrix_eq_diagonal, Matrix.det_diagonal]

/-- Every diagonal eigenvalue in the arithmetic birth block is nonzero. -/
theorem hammingArithmeticBirthRestrictedMatrix_diag_ne_zero
    (m : ℕ) (k : HammingArithmeticBirthIndex m) :
    ((hammingArithmeticBirthIndex m k).val : ℚ) ≠ 0 := by
  have hp := hammingArithmeticBirthIndex_prime m k
  exact_mod_cast hp.ne_zero

end EnterpriseMath.Precision
