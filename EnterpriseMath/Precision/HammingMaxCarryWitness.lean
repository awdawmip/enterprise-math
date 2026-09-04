import EnterpriseMath.Precision.HammingChebyshevSynchronization
import Mathlib.NumberTheory.Padics.PadicVal.Basic

namespace EnterpriseMath.Precision

/--
The explicit Hamming shell proposed to attain the maximal base-`p` carry depth
in row `N - 1`.  For prime `p`, its index is the full lower block of `p - 1`
digits below the highest visible `p`-power scale.
-/
def hammingMaxCarryWitness (N p : ℕ) : ℕ :=
  p ^ Nat.log p N - 1

/-- The explicit witness is a physical shell of row `N - 1`. -/
theorem hammingMaxCarryWitness_le_pred
    {N p : ℕ} (hN : N ≠ 0) :
    hammingMaxCarryWitness N p ≤ N - 1 := by
  unfold hammingMaxCarryWitness
  have hpow : p ^ Nat.log p N ≤ N := Nat.pow_log_le_self p hN
  omega

/-- For a prime base, adding one recovers the highest visible prime power. -/
theorem hammingMaxCarryWitness_add_one
    (N p : ℕ) [hp : Fact p.Prime] :
    hammingMaxCarryWitness N p + 1 = p ^ Nat.log p N := by
  unfold hammingMaxCarryWitness
  have hpos : 0 < p ^ Nat.log p N := Nat.pow_pos hp.out.pos
  omega

/-- The complementary shell is the residual above the highest visible prime power. -/
theorem hammingMaxCarryCofactor_eq
    {N p : ℕ} [hp : Fact p.Prime] (hN : N ≠ 0) :
    N - 1 - hammingMaxCarryWitness N p = N - p ^ Nat.log p N := by
  unfold hammingMaxCarryWitness
  have hpow : p ^ Nat.log p N ≤ N := Nat.pow_log_le_self p hN
  have hpos : 0 < p ^ Nat.log p N := Nat.pow_pos hp.out.pos
  omega

/--
Exact adjacent-row recurrence at the maximal-carry witness.  It separates the
future valuation proof into the top-state factor `N`, the visible prime power,
and one carry-free binomial coefficient in row `N`.
-/
theorem hammingMaxCarry_choose_recurrence
    {N p : ℕ} [Fact p.Prime] (hN : N ≠ 0) :
    N * Nat.choose (N - 1) (hammingMaxCarryWitness N p) =
      p ^ Nat.log p N * Nat.choose N (p ^ Nat.log p N) := by
  have hN1 : 1 ≤ N := Nat.one_le_iff_ne_zero.mpr hN
  have hsub : N - 1 + 1 = N := Nat.sub_add_cancel hN1
  calc
    N * Nat.choose (N - 1) (hammingMaxCarryWitness N p) =
        (N - 1 + 1) * Nat.choose (N - 1) (hammingMaxCarryWitness N p) := by
          rw [hsub]
    _ = Nat.choose (N - 1 + 1) (hammingMaxCarryWitness N p + 1) *
          (hammingMaxCarryWitness N p + 1) :=
      Nat.add_one_mul_choose_eq (N - 1) (hammingMaxCarryWitness N p)
    _ = Nat.choose N (p ^ Nat.log p N) * (p ^ Nat.log p N) := by
      rw [hsub, hammingMaxCarryWitness_add_one]
    _ = p ^ Nat.log p N * Nat.choose N (p ^ Nat.log p N) := by
      ac_rfl

end EnterpriseMath.Precision
