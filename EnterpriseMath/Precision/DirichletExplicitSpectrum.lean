import EnterpriseMath.Precision.DirichletChebyshev
import EnterpriseMath.Precision.DirichletSpectrumBridge

namespace EnterpriseMath.Precision

open Polynomial
open scoped BigOperators

/-- The complete one-indexed classical readout of the finite Dirichlet spectrum. -/
noncomputable def dirichletModeRootFinset (M : ℕ) : Finset ℝ :=
  (Finset.range (M - 1)).image (fun j => dirichletModeRoot M (j + 1))

/-- The zero-indexed container `j ↦ u_{j+1,M}` is strictly increasing on its physical range. -/
theorem dirichletModeRoot_succ_strictMonoOn (M : ℕ) :
    StrictMonoOn (fun j : ℕ => dirichletModeRoot M (j + 1))
      (↑(Finset.range (M - 1)) : Set ℕ) := by
  intro a ha b hb hab
  have haM : a < M - 1 := by simpa using ha
  have hbM : b < M - 1 := by simpa using hb
  exact dirichletModeRoot_strictMono M (a + 1) (b + 1)
    (by omega) (by omega) (by omega)

/-- There are exactly `M-1` explicit interior mode roots. -/
theorem dirichletModeRootFinset_card (M : ℕ) :
    (dirichletModeRootFinset M).card = M - 1 := by
  classical
  unfold dirichletModeRootFinset
  rw [Finset.card_image_of_injOn (dirichletModeRoot_succ_strictMonoOn M).injOn]
  simp

/--
The complete roots multiset of the genuine monic finite spectral polynomial is exactly the
strictly ordered classical mode list.  This is a downstream finite compatibility theorem.
-/
theorem dirichletSpectralPoly_roots_eq_modeRootFinset (M : ℕ) :
    (dirichletSpectralPoly (M - 1)).roots =
      (dirichletModeRootFinset M).val := by
  classical
  apply Polynomial.roots_eq_of_natDegree_le_card_of_ne_zero
  · intro x hx
    rw [dirichletModeRootFinset] at hx
    rcases Finset.mem_image.mp hx with ⟨j, hj, rfl⟩
    have hjM : j + 1 < M := by
      have hj' := Finset.mem_range.mp hj
      omega
    rw [dirichletSpectralPoly_eval,
      dirichletContinuant_modeRoot_zero M (j + 1) (by omega) hjM, mul_zero]
  · rw [dirichletSpectralPoly_natDegree, dirichletModeRootFinset_card]
  · exact (dirichletSpectralPoly_monic (M - 1)).ne_zero

/-- Product of all roots of the monic finite spectral polynomial. -/
theorem dirichletSpectralPoly_roots_prod (n : ℕ) :
    (dirichletSpectralPoly n).roots.prod = ((n + 1 : ℕ) : ℝ) := by
  have hs := (dirichletSpectralPoly_splits n).coeff_zero_eq_prod_roots_of_monic
    (dirichletSpectralPoly_monic n)
  rw [dirichletSpectralPoly_coeff_zero, dirichletSpectralPoly_natDegree] at hs
  have hsign : ((-1 : ℝ) ^ n) ≠ 0 := by positivity
  exact (mul_left_cancel₀ hsign hs).symm

/-- The explicit physical root list has product exactly `M`. -/
theorem dirichletModeRootFinset_val_prod (M : ℕ) (hM : 0 < M) :
    (dirichletModeRootFinset M).val.prod = (M : ℝ) := by
  have hs := dirichletSpectralPoly_roots_prod (M - 1)
  rw [dirichletSpectralPoly_roots_eq_modeRootFinset] at hs
  have hsucc : M - 1 + 1 = M := by omega
  rw [hsucc] at hs
  exact hs

end EnterpriseMath.Precision
