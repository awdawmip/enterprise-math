import Mathlib

namespace EnterpriseMath.PrecisionPi.CMFiniteTransform

/-- Ordinary power-series truncation through degree `M`. -/
def ordinaryPartial (c : ℕ → ℝ) (z : ℝ) (M : ℕ) : ℝ :=
  ∑ n in Finset.range (M + 1), c n * z ^ n

/-- Euler-derivative truncation through degree `M`. -/
def thetaPartial (c : ℕ → ℝ) (z : ℝ) (M : ℕ) : ℝ :=
  ∑ n in Finset.range (M + 1), (n : ℝ) * c n * z ^ n

/-- Finite CM differential functional. -/
def cmPartial (A B : ℝ) (c : ℕ → ℝ) (z : ℝ) (M : ℕ) : ℝ :=
  ∑ n in Finset.range (M + 1),
    (A + B * (n : ℝ)) * c n * z ^ n

/-- Linearity of the finite Euler differential functional. -/
theorem linear_functional_eq_cmPartial
    (A B : ℝ) (c : ℕ → ℝ) (z : ℝ) (M : ℕ) :
    A * ordinaryPartial c z M + B * thetaPartial c z M =
      cmPartial A B c z M := by
  rw [ordinaryPartial, thetaPartial, cmPartial,
    Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro n _
  ring

/-- Appending one coefficient to the finite CM functional. -/
theorem cmPartial_succ
    (A B : ℝ) (c : ℕ → ℝ) (z : ℝ) (M : ℕ) :
    cmPartial A B c z (M + 1) =
      cmPartial A B c z M +
        (A + B * ((M + 1 : ℕ) : ℝ)) * c (M + 1) * z ^ (M + 1) := by
  simp [cmPartial, Finset.sum_range_succ]

/-- The transformed truncation written directly in terms of a lifted precision sequence. -/
def precisionTransformPartial
    (A B z κ : ℝ) (density precision : ℕ → ℝ) (M : ℕ) : ℝ :=
  A + ∑ j in Finset.range M,
    κ * ((j + 1 : ℕ) : ℝ) * density (j + 1) * precision (j + 1) *
      (A + B * ((j + 1 : ℕ) : ℝ)) * z ^ (j + 1)

/-- Appending one positive-depth precision term. -/
theorem precisionTransformPartial_succ
    (A B z κ : ℝ) (density precision : ℕ → ℝ) (M : ℕ) :
    precisionTransformPartial A B z κ density precision (M + 1) =
      precisionTransformPartial A B z κ density precision M +
        κ * ((M + 1 : ℕ) : ℝ) * density (M + 1) * precision (M + 1) *
          (A + B * ((M + 1 : ℕ) : ℝ)) * z ^ (M + 1) := by
  simp [precisionTransformPartial, Finset.sum_range_succ]
  ring

/-- Any coefficient law of the form
`cₙ = κ n · densityₙ · precisionₙ` lifts the CM functional to an explicit weighted
transform of the finite precision sequence. -/
theorem cmPartial_eq_precisionTransformPartial
    (A B z κ : ℝ)
    (c density precision : ℕ → ℝ)
    (hc0 : c 0 = 1)
    (hlift : ∀ n : ℕ, 0 < n →
      c n = κ * (n : ℝ) * density n * precision n)
    (M : ℕ) :
    cmPartial A B c z M =
      precisionTransformPartial A B z κ density precision M := by
  induction M with
  | zero => simp [cmPartial, precisionTransformPartial, hc0]
  | succ M ih =>
      rw [cmPartial_succ, precisionTransformPartial_succ, ih,
        hlift (M + 1) (Nat.zero_lt_succ M)]
      ring

/-- Combining the previous two identities gives the finite boundary-to-CM transform. -/
theorem differential_partial_eq_precision_transform
    (A B z κ : ℝ)
    (c density precision : ℕ → ℝ)
    (hc0 : c 0 = 1)
    (hlift : ∀ n : ℕ, 0 < n →
      c n = κ * (n : ℝ) * density n * precision n)
    (M : ℕ) :
    A * ordinaryPartial c z M + B * thetaPartial c z M =
      precisionTransformPartial A B z κ density precision M := by
  rw [linear_functional_eq_cmPartial]
  exact cmPartial_eq_precisionTransformPartial
    A B z κ c density precision hc0 hlift M

end EnterpriseMath.PrecisionPi.CMFiniteTransform
