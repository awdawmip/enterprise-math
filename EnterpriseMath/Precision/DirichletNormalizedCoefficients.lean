import EnterpriseMath.Precision.DirichletExpansion

namespace EnterpriseMath.Precision

open scoped BigOperators

/-- The two half-products around the central mode pair into quadratic defects. -/
theorem descAscFactorial_pair_product (M j : ℕ) (hj : j < M) :
    (((M - 1).descFactorial j : ℕ) : ℝ) * (((M + 1).ascFactorial j : ℕ) : ℝ) =
      ∏ r in Finset.range j,
        ((M : ℝ) ^ 2 - (((r + 1 : ℕ) : ℝ) ^ 2)) := by
  induction j with
  | zero => simp
  | succ j ih =>
      have hj' : j < M := lt_trans (Nat.lt_succ_self j) hj
      have hM1 : 1 ≤ M := by omega
      have hsub : j ≤ M - 1 := by omega
      rw [Nat.descFactorial_succ, Nat.ascFactorial_succ, Finset.prod_range_succ]
      simp only [Nat.cast_mul, Nat.cast_add, Nat.cast_one]
      rw [Nat.cast_sub hsub, Nat.cast_sub hM1, ih hj']
      ring

/-- The centered odd ascending factorial splits into the central factor and paired halves. -/
theorem centeredAscFactorial_factorization (M j : ℕ) (hj : j < M) :
    (M - j).ascFactorial (2 * j + 1) =
      M * (M - 1).descFactorial j * (M + 1).ascFactorial j := by
  have hjle : j ≤ M := Nat.le_of_lt hj
  have hMj : M - j + j = M := Nat.sub_add_cancel hjle
  have hsplit := Nat.ascFactorial_mul_ascFactorial (M - j) j (j + 1)
  have hleft0 := Nat.add_descFactorial_eq_ascFactorial' (M - j) j
  rw [hMj] at hleft0
  have hleft : (M - j).ascFactorial j = (M - 1).descFactorial j := hleft0.symm
  have hright0 := Nat.ascFactorial_mul_ascFactorial M 1 j
  have hright : M.ascFactorial (j + 1) = M * (M + 1).ascFactorial j := by
    simpa [Nat.ascFactorial_succ, Nat.add_comm] using hright0.symm
  calc
    (M - j).ascFactorial (2 * j + 1) =
        (M - j).ascFactorial j * M.ascFactorial (j + 1) := by
      rw [show 2 * j + 1 = j + (j + 1) by omega]
      rw [← hsplit, hMj]
    _ = (M - 1).descFactorial j * (M * (M + 1).ascFactorial j) := by
      rw [hleft, hright]
    _ = M * (M - 1).descFactorial j * (M + 1).ascFactorial j := by ring

/-- The exact factorial/binomial numerator is the central factor times the quadratic defects. -/
theorem choose_factorial_eq_symmetric_defects (M j : ℕ) (hj : j < M) :
    (Nat.choose (M + j) (2 * j + 1) : ℝ) * (((2 * j + 1)! : ℕ) : ℝ) =
      (M : ℝ) *
        ∏ r in Finset.range j,
          ((M : ℝ) ^ 2 - (((r + 1 : ℕ) : ℝ) ^ 2)) := by
  have hidx : M - j + (2 * j + 1) - 1 = M + j := by omega
  have hchoose := Nat.ascFactorial_eq_factorial_mul_choose' (M - j) (2 * j + 1)
  rw [hidx] at hchoose
  calc
    (Nat.choose (M + j) (2 * j + 1) : ℝ) * (((2 * j + 1)! : ℕ) : ℝ) =
        (((M - j).ascFactorial (2 * j + 1) : ℕ) : ℝ) := by
      rw [hchoose]
      push_cast
      ring
    _ = (M : ℝ) * (((M - 1).descFactorial j : ℕ) : ℝ) *
        (((M + 1).ascFactorial j : ℕ) : ℝ) := by
      rw [centeredAscFactorial_factorization M j hj]
      push_cast
    _ = (M : ℝ) *
        ∏ r in Finset.range j,
          ((M : ℝ) ^ 2 - (((r + 1 : ℕ) : ℝ) ^ 2)) := by
      rw [← mul_assoc, descAscFactorial_pair_product M j hj]

/-- Quadratic defects factor out one common `M^2` per mode. -/
theorem symmetric_defects_eq_scaled_unit_defects (M j : ℕ) (hM : 0 < M) :
    (∏ r in Finset.range j,
        ((M : ℝ) ^ 2 - (((r + 1 : ℕ) : ℝ) ^ 2))) =
      ((M : ℝ) ^ 2) ^ j *
        ∏ r in Finset.range j,
          (1 - (((r + 1 : ℕ) : ℝ) ^ 2) / (M : ℝ) ^ 2) := by
  have hM0 : (M : ℝ) ^ 2 ≠ 0 := by positivity
  calc
    (∏ r in Finset.range j,
        ((M : ℝ) ^ 2 - (((r + 1 : ℕ) : ℝ) ^ 2))) =
        ∏ r in Finset.range j,
          ((M : ℝ) ^ 2 *
            (1 - (((r + 1 : ℕ) : ℝ) ^ 2) / (M : ℝ) ^ 2)) := by
      apply Finset.prod_congr rfl
      intro r hr
      field_simp [hM0]
      ring
    _ = (∏ _r in Finset.range j, ((M : ℝ) ^ 2)) *
        ∏ r in Finset.range j,
          (1 - (((r + 1 : ℕ) : ℝ) ^ 2) / (M : ℝ) ^ 2) := by
      rw [Finset.prod_mul_distrib]
    _ = ((M : ℝ) ^ 2) ^ j *
        ∏ r in Finset.range j,
          (1 - (((r + 1 : ℕ) : ℝ) ^ 2) / (M : ℝ) ^ 2) := by
      simp

/--
WSR-L32: exact normalized coefficient identity behind the finite `sin(x)/x` determinant formula.
-/
theorem normalized_choose_eq_unit_defects (M j : ℕ) (hj : j < M) :
    (Nat.choose (M + j) (2 * j + 1) : ℝ) / (M : ℝ) ^ (2 * j + 1) =
      (1 / (((2 * j + 1)! : ℕ) : ℝ)) *
        ∏ r in Finset.range j,
          (1 - (((r + 1 : ℕ) : ℝ) ^ 2) / (M : ℝ) ^ 2) := by
  have hM : 0 < M := lt_of_le_of_lt (Nat.zero_le j) hj
  have hM0 : (M : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hM)
  have hfac0 : ((((2 * j + 1)! : ℕ) : ℝ)) ≠ 0 := by positivity
  have hchoose := choose_factorial_eq_symmetric_defects M j hj
  rw [symmetric_defects_eq_scaled_unit_defects M j hM] at hchoose
  have hpow : (M : ℝ) * ((M : ℝ) ^ 2) ^ j = (M : ℝ) ^ (2 * j + 1) := by
    rw [← pow_mul]
    rw [pow_succ']
  have htotal :
      (Nat.choose (M + j) (2 * j + 1) : ℝ) * (((2 * j + 1)! : ℕ) : ℝ) =
        (M : ℝ) ^ (2 * j + 1) *
          ∏ r in Finset.range j,
            (1 - (((r + 1 : ℕ) : ℝ) ^ 2) / (M : ℝ) ^ 2) := by
    calc
      _ = (M : ℝ) *
          (((M : ℝ) ^ 2) ^ j *
            ∏ r in Finset.range j,
              (1 - (((r + 1 : ℕ) : ℝ) ^ 2) / (M : ℝ) ^ 2)) := hchoose
      _ = _ := by rw [← mul_assoc, hpow]
  field_simp [hM0, hfac0]
  simpa [mul_comm] using htotal

end EnterpriseMath.Precision
