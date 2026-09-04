import EnterpriseMath.Precision.HammingReflection
import EnterpriseMath.Precision.WallisPrecision

namespace EnterpriseMath.Precision

open scoped BigOperators

/-- Product of the positive reflection-even Hamming-shell eigenvalues `2,4,...,2n`. -/
def hammingEvenPositiveSpectralProduct (n : ℕ) : ℚ :=
  ∏ r in Finset.range n, (2 * (r : ℚ) + 2)

/-- Product of the reflection-odd Hamming-shell eigenvalues `1,3,...,2n+1`. -/
def hammingOddSpectralProduct (n : ℕ) : ℚ :=
  ∏ r in Finset.range (n + 1), (2 * (r : ℚ) + 1)

/--
Finite spectral Wallis invariant for the odd Hamming shell `m=2n+1`.
The zero even mode is omitted from the numerator product.
-/
def hammingParitySpectralInvariant (n : ℕ) : ℚ :=
  (2 * (n : ℚ) + 1) *
    (hammingEvenPositiveSpectralProduct n / hammingOddSpectralProduct n) ^ 2

/-- Every even spectral factor is realized by a genuine nonzero reflection-even shell mode. -/
theorem hammingEvenPositiveSpectralFactor_realized
    (n r : ℕ) (hr : r < n) :
    ∃ f : ℕ → ℚ,
      f ≠ 0 ∧
      (∀ j, j ≤ 2 * n + 1 →
        hammingShellK (2 * n + 1) f j =
          ((2 * (r + 1) : ℕ) : ℚ) * f j) ∧
      (∀ j, j ≤ 2 * n + 1 →
        f (2 * n + 1 - j) = f j) := by
  have hk : 2 * (r + 1) ≤ 2 * n + 1 := by omega
  refine ⟨hammingShellMode (2 * n + 1) (2 * (r + 1)),
    hammingShellMode_ne_zero _ _ hk, ?_, ?_⟩
  · intro j hj
    exact hammingShellK_mode _ _ _ hk hj
  · intro j hj
    exact hammingShellMode_reflection_even _ _ _ hj (even_two_mul (r + 1))

/-- Every odd spectral factor is realized by a genuine nonzero reflection-odd shell mode. -/
theorem hammingOddSpectralFactor_realized
    (n r : ℕ) (hr : r ≤ n) :
    ∃ f : ℕ → ℚ,
      f ≠ 0 ∧
      (∀ j, j ≤ 2 * n + 1 →
        hammingShellK (2 * n + 1) f j =
          ((2 * r + 1 : ℕ) : ℚ) * f j) ∧
      (∀ j, j ≤ 2 * n + 1 →
        f (2 * n + 1 - j) = -f j) := by
  have hk : 2 * r + 1 ≤ 2 * n + 1 := by omega
  refine ⟨hammingShellMode (2 * n + 1) (2 * r + 1),
    hammingShellMode_ne_zero _ _ hk, ?_, ?_⟩
  · intro j hj
    exact hammingShellK_mode _ _ _ hk hj
  · intro j hj
    exact hammingShellMode_reflection_odd _ _ _ hj (odd_two_mul_add_one r)

/-- The positive even spectral product is strictly positive. -/
theorem hammingEvenPositiveSpectralProduct_pos (n : ℕ) :
    0 < hammingEvenPositiveSpectralProduct n := by
  unfold hammingEvenPositiveSpectralProduct
  exact Finset.prod_pos fun r _ => by positivity

/-- The odd spectral product is strictly positive. -/
theorem hammingOddSpectralProduct_pos (n : ℕ) :
    0 < hammingOddSpectralProduct n := by
  unfold hammingOddSpectralProduct
  exact Finset.prod_pos fun r _ => by positivity

/-- One-step growth of the positive reflection-even spectral product. -/
theorem hammingEvenPositiveSpectralProduct_succ (n : ℕ) :
    hammingEvenPositiveSpectralProduct (n + 1) =
      hammingEvenPositiveSpectralProduct n * (2 * (n : ℚ) + 2) := by
  unfold hammingEvenPositiveSpectralProduct
  rw [Finset.prod_range_succ]

/-- One-step growth of the reflection-odd spectral product. -/
theorem hammingOddSpectralProduct_succ (n : ℕ) :
    hammingOddSpectralProduct (n + 1) =
      hammingOddSpectralProduct n * (2 * (n : ℚ) + 3) := by
  unfold hammingOddSpectralProduct
  rw [Finset.prod_range_succ]
  push_cast
  ring

/--
The true Hamming parity spectral invariant has exactly the same one-step multiplier
as the Wallis partial product.
-/
theorem hammingParitySpectralInvariant_succ (n : ℕ) :
    hammingParitySpectralInvariant (n + 1) =
      hammingParitySpectralInvariant n * wallisStep n := by
  unfold hammingParitySpectralInvariant
  rw [hammingEvenPositiveSpectralProduct_succ,
    hammingOddSpectralProduct_succ]
  unfold wallisStep
  have hO : hammingOddSpectralProduct n ≠ 0 :=
    ne_of_gt (hammingOddSpectralProduct_pos n)
  have h1 : 2 * (n : ℚ) + 1 ≠ 0 := by positivity
  have h3 : 2 * (n : ℚ) + 3 ≠ 0 := by positivity
  push_cast
  field_simp [hO, h1, h3]
  ring

/--
WSR-L50 / spectral-product form of WSR-T05: the finite Hamming reflection-sector
spectral product is exactly the rational Wallis partial product.
-/
theorem hammingParitySpectralInvariant_eq_wallisPartial (n : ℕ) :
    hammingParitySpectralInvariant n = wallisPartial n := by
  induction n with
  | zero =>
      norm_num [hammingParitySpectralInvariant,
        hammingEvenPositiveSpectralProduct, hammingOddSpectralProduct, wallisPartial]
  | succ n ih =>
      rw [hammingParitySpectralInvariant_succ, wallisPartial, ih]

/-- Expanded parity spectral-product statement for the odd shell `m=2n+1`. -/
theorem wallisPartial_eq_hammingParitySpectralProduct (n : ℕ) :
    wallisPartial n =
      (2 * (n : ℚ) + 1) *
        (hammingEvenPositiveSpectralProduct n / hammingOddSpectralProduct n) ^ 2 := by
  symm
  exact hammingParitySpectralInvariant_eq_wallisPartial n

end EnterpriseMath.Precision
