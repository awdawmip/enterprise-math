import EnterpriseMath.Precision.DirichletPolynomial

namespace EnterpriseMath.Precision

open Polynomial

/--
Second-order Pascal identity matching the two-step Dirichlet spectral-polynomial recurrence.
-/
theorem choose_second_order (N k : ℕ) :
    Nat.choose (N + 2) (k + 2) + Nat.choose N (k + 2) =
      2 * Nat.choose (N + 1) (k + 2) + Nat.choose N k := by
  have h1 :
      Nat.choose (N + 2) (k + 2) =
        Nat.choose (N + 1) (k + 1) + Nat.choose (N + 1) (k + 2) := by
    simpa [Nat.add_assoc] using Nat.choose_succ_succ' (N + 1) (k + 1)
  have h2 :
      Nat.choose (N + 1) (k + 1) =
        Nat.choose N k + Nat.choose N (k + 1) := by
    simpa [Nat.add_assoc] using Nat.choose_succ_succ' N k
  have h3 :
      Nat.choose (N + 1) (k + 2) =
        Nat.choose N (k + 1) + Nat.choose N (k + 2) := by
    simpa [Nat.add_assoc] using Nat.choose_succ_succ' N (k + 1)
  rw [h1, h2, h3]
  omega

/--
WSR-L29: exact binomial coefficient formula for every coefficient of the monic
Dirichlet spectral polynomial.

The sign is written as `(-1)^(n+j)` rather than `(-1)^(n-j)` to avoid
truncated natural subtraction; the two exponents have the same parity.
-/
theorem dirichletSpectralPoly_coeff_choose :
    ∀ n j : ℕ,
      (dirichletSpectralPoly n).coeff j =
        (-1 : ℝ) ^ (n + j) *
          (Nat.choose (n + 1 + j) (2 * j + 1) : ℝ) := by
  intro n
  induction n using Nat.twoStepInduction with
  | zero =>
      intro j
      cases j with
      | zero => norm_num [dirichletSpectralPoly]
      | succ k =>
          have hlt : 0 + 1 + (k + 1) < 2 * (k + 1) + 1 := by omega
          rw [Nat.choose_eq_zero_of_lt hlt]
          simp [dirichletSpectralPoly, coeff_one]
  | one =>
      intro j
      cases j with
      | zero => norm_num [dirichletSpectralPoly]
      | succ k =>
          cases k with
          | zero => norm_num [dirichletSpectralPoly]
          | succ k =>
              have hlt : 1 + 1 + (k + 2) < 2 * (k + 2) + 1 := by omega
              rw [Nat.choose_eq_zero_of_lt hlt]
              have hne : k + 2 ≠ 1 := by omega
              simp [dirichletSpectralPoly, coeff_X_of_ne_one hne]
  | more n ih0 ih1 =>
      intro j
      cases j with
      | zero =>
          simpa [Nat.choose_one_right] using dirichletSpectralPoly_coeff_zero (n + 2)
      | succ k =>
          rw [dirichletSpectralPoly, sub_mul, coeff_sub, coeff_sub,
            coeff_X_mul, coeff_C_mul, ih1 k, ih1 (k + 1), ih0 (k + 1)]
          have hs0 :
              (-1 : ℝ) ^ (n + 1 + k) =
                (-1 : ℝ) ^ (n + 2 + (k + 1)) := by
            calc
              (-1 : ℝ) ^ (n + 1 + k)
                  = (-1 : ℝ) ^ (n + 1 + k) * (-1 : ℝ) ^ 2 := by norm_num
              _ = (-1 : ℝ) ^ ((n + 1 + k) + 2) := by rw [← pow_add]
              _ = (-1 : ℝ) ^ (n + 2 + (k + 1)) := by congr 1 <;> omega
          have hs1 :
              (-1 : ℝ) ^ (n + 1 + (k + 1)) =
                -((-1 : ℝ) ^ (n + 2 + (k + 1))) := by
            have h : n + 2 + (k + 1) = (n + 1 + (k + 1)) + 1 := by omega
            rw [h, pow_succ]
            ring
          have hs2 :
              (-1 : ℝ) ^ (n + (k + 1)) =
                (-1 : ℝ) ^ (n + 2 + (k + 1)) := by
            calc
              (-1 : ℝ) ^ (n + (k + 1))
                  = (-1 : ℝ) ^ (n + (k + 1)) * (-1 : ℝ) ^ 2 := by norm_num
              _ = (-1 : ℝ) ^ ((n + (k + 1)) + 2) := by rw [← pow_add]
              _ = (-1 : ℝ) ^ (n + 2 + (k + 1)) := by congr 1 <;> omega
          rw [hs0, hs1, hs2]
          have hcNat := choose_second_order (n + k + 2) (2 * k + 1)
          have hc :
              (Nat.choose (n + k + 4) (2 * k + 3) : ℝ) +
                  (Nat.choose (n + k + 2) (2 * k + 3) : ℝ) =
                2 * (Nat.choose (n + k + 3) (2 * k + 3) : ℝ) +
                  (Nat.choose (n + k + 2) (2 * k + 1) : ℝ) := by
            exact_mod_cast hcNat
          linear_combination (norm := ring_nf)
            ((-1 : ℝ) ^ (n + 2 + (k + 1))) * hc

end EnterpriseMath.Precision
