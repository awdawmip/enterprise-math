import EnterpriseMath.Precision.HammingFiniteOperator
import EnterpriseMath.Precision.HammingSpectralWallis
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Matrix.Diagonal
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

namespace EnterpriseMath.Precision

open scoped BigOperators
open Module

/-- Matrix of the genuine finite Hamming shell operator in the Krawtchouk eigenbasis. -/
noncomputable def hammingKrawtchoukMatrix (m : ℕ) :
    Matrix (Fin (m + 1)) (Fin (m + 1)) ℚ :=
  LinearMap.toMatrix (hammingKrawtchoukBasis m) (hammingKrawtchoukBasis m)
    (hammingShellKFin m)

/-- In the Krawtchouk basis, the genuine finite operator is exactly `diag(0,1,...,m)`. -/
theorem hammingKrawtchoukMatrix_eq_diagonal (m : ℕ) :
    hammingKrawtchoukMatrix m = Matrix.diagonal fun k => (k.val : ℚ) := by
  classical
  ext i j
  rw [hammingKrawtchoukMatrix, LinearMap.toMatrix_apply]
  have hK :
      hammingShellKFin m (hammingKrawtchoukBasis m j) =
        (j.val : ℚ) • hammingKrawtchoukBasis m j := by
    simpa only [hammingKrawtchoukBasis_apply] using
      hammingShellKFin_mode m j.val (by omega)
  rw [hK, map_smul, Basis.repr_self, Finsupp.smul_single, smul_eq_mul, mul_one]
  simp [Matrix.diagonal_apply, eq_comm]

/-- Positive reflection-even Krawtchouk indices `2,4,...,2n`; the zero even mode is omitted. -/
def hammingEvenPrimeIndex (n : ℕ) :
    Fin n ↪ Fin ((2 * n + 1) + 1) where
  toFun r := ⟨2 * r.val + 2, by omega⟩
  inj' := by
    intro a b h
    apply Fin.ext
    have hv := congrArg (fun x : Fin ((2 * n + 1) + 1) => x.val) h
    omega

/-- Reflection-odd Krawtchouk indices `1,3,...,2n+1`. -/
def hammingOddIndex (n : ℕ) :
    Fin (n + 1) ↪ Fin ((2 * n + 1) + 1) where
  toFun r := ⟨2 * r.val + 1, by omega⟩
  inj' := by
    intro a b h
    apply Fin.ext
    have hv := congrArg (fun x : Fin ((2 * n + 1) + 1) => x.val) h
    omega

/-- The selected positive-even basis vectors are genuinely reflection-even. -/
theorem hammingEvenPrimeBasis_reflection
    (n : ℕ) (r : Fin n) (j : Fin ((2 * n + 1) + 1)) :
    hammingKrawtchoukBasis (2 * n + 1) (hammingEvenPrimeIndex n r)
        ⟨2 * n + 1 - j.val, by omega⟩ =
      hammingKrawtchoukBasis (2 * n + 1) (hammingEvenPrimeIndex n r) j := by
  simp only [hammingKrawtchoukBasis_apply, hammingShellModeFin]
  have hk : Even (hammingEvenPrimeIndex n r).val := by
    convert even_two_mul (r.val + 1) using 1 <;> omega
  exact hammingShellMode_reflection_even (2 * n + 1)
    (hammingEvenPrimeIndex n r).val j.val (by omega) hk

/-- The selected odd basis vectors are genuinely reflection-odd. -/
theorem hammingOddBasis_reflection
    (n : ℕ) (r : Fin (n + 1)) (j : Fin ((2 * n + 1) + 1)) :
    hammingKrawtchoukBasis (2 * n + 1) (hammingOddIndex n r)
        ⟨2 * n + 1 - j.val, by omega⟩ =
      -hammingKrawtchoukBasis (2 * n + 1) (hammingOddIndex n r) j := by
  simp only [hammingKrawtchoukBasis_apply, hammingShellModeFin]
  have hk : Odd (hammingOddIndex n r).val := by
    simpa [hammingOddIndex] using odd_two_mul_add_one r.val
  exact hammingShellMode_reflection_odd (2 * n + 1)
    (hammingOddIndex n r).val j.val (by omega) hk

/-- Prime even parity block of the actual finite operator in its parity-adapted Krawtchouk basis. -/
noncomputable def hammingEvenPrimeRestrictedMatrix (n : ℕ) : Matrix (Fin n) (Fin n) ℚ :=
  (hammingKrawtchoukMatrix (2 * n + 1)).submatrix
    (hammingEvenPrimeIndex n) (hammingEvenPrimeIndex n)

/-- Odd parity block of the actual finite operator in its parity-adapted Krawtchouk basis. -/
noncomputable def hammingOddRestrictedMatrix (n : ℕ) :
    Matrix (Fin (n + 1)) (Fin (n + 1)) ℚ :=
  (hammingKrawtchoukMatrix (2 * n + 1)).submatrix
    (hammingOddIndex n) (hammingOddIndex n)

/-- The prime-even restricted block is diagonal on eigenvalues `2,4,...,2n`. -/
theorem hammingEvenPrimeRestrictedMatrix_eq_diagonal (n : ℕ) :
    hammingEvenPrimeRestrictedMatrix n =
      Matrix.diagonal fun r => ((hammingEvenPrimeIndex n r).val : ℚ) := by
  classical
  unfold hammingEvenPrimeRestrictedMatrix
  rw [hammingKrawtchoukMatrix_eq_diagonal,
    Matrix.submatrix_diagonal _ _ (hammingEvenPrimeIndex n).injective]
  rfl

/-- The odd restricted block is diagonal on eigenvalues `1,3,...,2n+1`. -/
theorem hammingOddRestrictedMatrix_eq_diagonal (n : ℕ) :
    hammingOddRestrictedMatrix n =
      Matrix.diagonal fun r => ((hammingOddIndex n r).val : ℚ) := by
  classical
  unfold hammingOddRestrictedMatrix
  rw [hammingKrawtchoukMatrix_eq_diagonal,
    Matrix.submatrix_diagonal _ _ (hammingOddIndex n).injective]
  rfl

/-- The literal prime-even restricted determinant is the positive-even spectral product. -/
theorem hammingEvenPrimeRestrictedMatrix_det (n : ℕ) :
    (hammingEvenPrimeRestrictedMatrix n).det = hammingEvenPositiveSpectralProduct n := by
  classical
  rw [hammingEvenPrimeRestrictedMatrix_eq_diagonal, Matrix.det_diagonal]
  change (∏ r : Fin n, (((2 * r.val + 2 : ℕ) : ℚ))) =
    hammingEvenPositiveSpectralProduct n
  rw [Fin.prod_univ_eq_prod_range]
  unfold hammingEvenPositiveSpectralProduct
  refine Finset.prod_congr rfl ?_
  intro r hr
  push_cast
  ring

/-- The literal odd restricted determinant is the odd spectral product. -/
theorem hammingOddRestrictedMatrix_det (n : ℕ) :
    (hammingOddRestrictedMatrix n).det = hammingOddSpectralProduct n := by
  classical
  rw [hammingOddRestrictedMatrix_eq_diagonal, Matrix.det_diagonal]
  change (∏ r : Fin (n + 1), (((2 * r.val + 1 : ℕ) : ℚ))) =
    hammingOddSpectralProduct n
  rw [Fin.prod_univ_eq_prod_range]
  unfold hammingOddSpectralProduct
  refine Finset.prod_congr rfl ?_
  intro r hr
  push_cast
  ring

/--
WSR-L51 / literal determinant form of WSR-T05.
For the actual odd Hamming shell `m=2n+1`, the Wallis partial product is the endpoint
factor times the squared ratio of the prime-even and odd parity restricted determinants.
-/
theorem wallisPartial_eq_hammingParityRestrictedDeterminants (n : ℕ) :
    wallisPartial n =
      (2 * (n : ℚ) + 1) *
        ((hammingEvenPrimeRestrictedMatrix n).det /
          (hammingOddRestrictedMatrix n).det) ^ 2 := by
  rw [hammingEvenPrimeRestrictedMatrix_det, hammingOddRestrictedMatrix_det]
  exact wallisPartial_eq_hammingParitySpectralProduct n

end EnterpriseMath.Precision
