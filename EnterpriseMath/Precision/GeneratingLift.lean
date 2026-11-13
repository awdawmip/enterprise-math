import Mathlib

namespace EnterpriseMath.PrecisionPi.GeneratingLift

variable {K : Type*} [Field K] [CharZero K]

/-- Scaled precision coefficient comparing two nonzero balance channels. -/
def scaledPrecision
    (scale : K) (source target : ℕ → K) (n : ℕ) : K :=
  scale * source n / ((n : K) * target n)

/-- Recover the source coefficient exactly from precision and target weight. -/
theorem source_eq_scaledPrecision_lift
    (scale : K) (source target : ℕ → K) (n : ℕ)
    (hscale : scale ≠ 0) (hn : n ≠ 0) (htarget : target n ≠ 0) :
    source n = scale⁻¹ * (n : K) * target n *
      scaledPrecision scale source target n := by
  have hnK : (n : K) ≠ 0 := Nat.cast_ne_zero.mpr hn
  unfold scaledPrecision
  field_simp [hscale, hnK, htarget]
  ring

theorem weighted_coefficient_lift
    (scale : K) (source target : ℕ → K) (response : ℕ → K)
    (z : K) (n : ℕ)
    (hscale : scale ≠ 0) (hn : n ≠ 0) (htarget : target n ≠ 0) :
    source n * response n * z ^ n =
      (scale⁻¹ * (n : K) * target n *
        scaledPrecision scale source target n) * response n * z ^ n := by
  rw [source_eq_scaledPrecision_lift scale source target n hscale hn htarget]

/-- Exact finite weighted generating lift for indices `1,…,M`. -/
theorem finite_weighted_generating_lift
    (scale : K) (source target : ℕ → K) (response : ℕ → K)
    (z : K) (M : ℕ)
    (hscale : scale ≠ 0)
    (htarget : ∀ n, n ≠ 0 → target n ≠ 0) :
    (∑ j in Finset.range M,
        source (j + 1) * response (j + 1) * z ^ (j + 1)) =
      ∑ j in Finset.range M,
        (scale⁻¹ * ((j + 1 : ℕ) : K) * target (j + 1) *
          scaledPrecision scale source target (j + 1)) *
            response (j + 1) * z ^ (j + 1) := by
  apply Finset.sum_congr rfl
  intro j hj
  exact weighted_coefficient_lift scale source target response z (j + 1)
    hscale (by omega) (htarget (j + 1) (by omega))

/-- Unweighted finite generating lift. -/
theorem finite_generating_lift
    (scale : K) (source target : ℕ → K) (z : K) (M : ℕ)
    (hscale : scale ≠ 0)
    (htarget : ∀ n, n ≠ 0 → target n ≠ 0) :
    (∑ j in Finset.range M, source (j + 1) * z ^ (j + 1)) =
      ∑ j in Finset.range M,
        scale⁻¹ * ((j + 1 : ℕ) : K) * target (j + 1) *
          scaledPrecision scale source target (j + 1) * z ^ (j + 1) := by
  simpa using finite_weighted_generating_lift
    scale source target (fun _ => 1) z M hscale htarget

end EnterpriseMath.PrecisionPi.GeneratingLift
