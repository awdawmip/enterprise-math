import Mathlib

namespace EnterpriseMath.PrecisionPi.SignatureBalanceRecurrence

/-- One normalized rising-factor step. -/
def riseStep (a : ℚ) (n : ℕ) : ℚ :=
  ((n : ℚ) + a) / (n + 1 : ℕ)

/-- Normalized rising factorial `(a)_n/n!`, defined only by its finite
recurrence. -/
def normalizedRising (a : ℚ) : ℕ → ℚ
  | 0 => 1
  | n + 1 => normalizedRising a n * riseStep a n

/-- One equal-occupancy recurrence step for a `k`-state balance kernel. -/
def balanceStep (k n : ℕ) : ℚ :=
  ∏ r ∈ Finset.Icc 1 (k - 1), riseStep ((r : ℚ) / (k : ℚ)) n

/-- Finite equal-occupancy balance kernel, defined recursively. -/
def balanceRec (k : ℕ) : ℕ → ℚ
  | 0 => 1
  | n + 1 => balanceRec k n * balanceStep k n

/-- The balance recurrence factors into normalized rising factorials indexed
by the nonzero residue classes `1,...,k-1`. -/
theorem balanceRec_eq_prod_normalizedRising (k n : ℕ) :
    balanceRec k n =
      ∏ r ∈ Finset.Icc 1 (k - 1),
        normalizedRising ((r : ℚ) / (k : ℚ)) n := by
  induction n with
  | zero => simp [balanceRec, normalizedRising]
  | succ n ih =>
      simp only [balanceRec, normalizedRising, ih]
      rw [Finset.prod_mul_distrib]
      rfl

/-- Binary balance is the normalized half-rising factorial. -/
theorem balanceRec_two (n : ℕ) :
    balanceRec 2 n = normalizedRising (1 / 2 : ℚ) n := by
  rw [balanceRec_eq_prod_normalizedRising]
  norm_num

/-- Ternary balance factors through the `1/3` and `2/3` channels. -/
theorem balanceRec_three (n : ℕ) :
    balanceRec 3 n =
      normalizedRising (1 / 3 : ℚ) n *
        normalizedRising (2 / 3 : ℚ) n := by
  rw [balanceRec_eq_prod_normalizedRising]
  norm_num

/-- Quartic balance factors through the `1/4,1/2,3/4` channels. -/
theorem balanceRec_four (n : ℕ) :
    balanceRec 4 n =
      normalizedRising (1 / 4 : ℚ) n *
        normalizedRising (1 / 2 : ℚ) n *
          normalizedRising (3 / 4 : ℚ) n := by
  rw [balanceRec_eq_prod_normalizedRising]
  norm_num
  ring

/-- Sextic balance factors through all five nonzero sixth-residue channels. -/
theorem balanceRec_six (n : ℕ) :
    balanceRec 6 n =
      normalizedRising (1 / 6 : ℚ) n *
        normalizedRising (1 / 3 : ℚ) n *
          normalizedRising (1 / 2 : ℚ) n *
            normalizedRising (2 / 3 : ℚ) n *
              normalizedRising (5 / 6 : ℚ) n := by
  rw [balanceRec_eq_prod_normalizedRising]
  norm_num
  ring

/-- Classical signature-2 coefficient kernel. -/
def signature2 (n : ℕ) : ℚ :=
  normalizedRising (1 / 2 : ℚ) n ^ 3

/-- Classical signature-3 coefficient kernel. -/
def signature3 (n : ℕ) : ℚ :=
  normalizedRising (1 / 2 : ℚ) n *
    normalizedRising (1 / 3 : ℚ) n *
      normalizedRising (2 / 3 : ℚ) n

/-- Classical signature-4 coefficient kernel. -/
def signature4 (n : ℕ) : ℚ :=
  normalizedRising (1 / 4 : ℚ) n *
    normalizedRising (1 / 2 : ℚ) n *
      normalizedRising (3 / 4 : ℚ) n

/-- Classical signature-6 coefficient kernel. -/
def signature6 (n : ℕ) : ℚ :=
  normalizedRising (1 / 6 : ℚ) n *
    normalizedRising (1 / 2 : ℚ) n *
      normalizedRising (5 / 6 : ℚ) n

/-- Signature 2 is the cube of binary balance. -/
theorem signature2_eq_balance_two (n : ℕ) :
    signature2 n = balanceRec 2 n ^ 3 := by
  rw [balanceRec_two]
  rfl

/-- Signature 3 is binary balance times ternary balance. -/
theorem signature3_eq_balance_two_mul_three (n : ℕ) :
    signature3 n = balanceRec 2 n * balanceRec 3 n := by
  rw [balanceRec_two, balanceRec_three]
  simp [signature3]
  ring

/-- Signature 4 is exactly quartic equal-occupancy balance. -/
theorem signature4_eq_balance_four (n : ℕ) :
    signature4 n = balanceRec 4 n := by
  rw [balanceRec_four]
  rfl

/-- Sextic balance is signature 6 times ternary balance. -/
theorem signature6_mul_balance_three_eq_balance_six (n : ℕ) :
    signature6 n * balanceRec 3 n = balanceRec 6 n := by
  rw [balanceRec_three, balanceRec_six]
  simp [signature6]
  ring

end EnterpriseMath.PrecisionPi.SignatureBalanceRecurrence
