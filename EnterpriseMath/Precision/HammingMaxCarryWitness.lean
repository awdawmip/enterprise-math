import EnterpriseMath.Precision.HammingChebyshevSynchronization
import Mathlib.Data.Nat.Choose.Lucas
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

/--
Lucas descent for a prime-power shell: choosing `p^q` from `N` is congruent
modulo `p` to the highest remaining base-`p` digit `N / p^q`.
-/
theorem choose_primePower_modEq_div_pow
    (N p q : ℕ) [hp : Fact p.Prime] :
    Nat.choose N (p ^ q) ≡ N / p ^ q [MOD p] := by
  induction q generalizing N with
  | zero => simp
  | succ q ih =>
      calc
        Nat.choose N (p ^ (q + 1)) ≡
            Nat.choose (N % p) ((p ^ (q + 1)) % p) *
              Nat.choose (N / p) ((p ^ (q + 1)) / p) [MOD p] :=
          Choose.choose_modEq_choose_mod_mul_choose_div_nat
        _ = Nat.choose (N / p) (p ^ q) := by
          simp [pow_succ, hp.out.ne_zero]
        _ ≡ (N / p) / p ^ q [MOD p] := ih (N / p)
        _ = N / p ^ (q + 1) := by
          simp [pow_succ, Nat.div_div_eq_div_mul, Nat.mul_comm]

/-- The quotient by the largest visible prime power is positive. -/
theorem highestVisiblePrimePower_quotient_pos
    {N p : ℕ} [hp : Fact p.Prime] (hN : N ≠ 0) :
    0 < N / p ^ Nat.log p N := by
  exact Nat.div_pos (Nat.pow_log_le_self p hN) (Nat.pow_pos hp.out.pos)

/-- The quotient by the largest visible prime power is a digit strictly below `p`. -/
theorem highestVisiblePrimePower_quotient_lt
    (N p : ℕ) [hp : Fact p.Prime] :
    N / p ^ Nat.log p N < p := by
  have hden : 0 < p ^ Nat.log p N := Nat.pow_pos hp.out.pos
  apply (Nat.div_lt_iff_lt_mul hden).2
  simpa [pow_succ, Nat.mul_comm] using
    (Nat.lt_pow_succ_log_self hp.out.one_lt N)

/-- The highest remaining base-`p` digit is not divisible by `p`. -/
theorem prime_not_dvd_highestVisiblePrimePower_quotient
    {N p : ℕ} [Fact p.Prime] (hN : N ≠ 0) :
    ¬ p ∣ N / p ^ Nat.log p N := by
  exact Nat.not_dvd_of_pos_of_lt
    (highestVisiblePrimePower_quotient_pos (N := N) (p := p) hN)
    (highestVisiblePrimePower_quotient_lt N p)

/-- The highest-visible prime-power binomial coefficient is carry-free at `p`. -/
theorem prime_not_dvd_choose_highestVisiblePrimePower
    {N p : ℕ} [Fact p.Prime] (hN : N ≠ 0) :
    ¬ p ∣ Nat.choose N (p ^ Nat.log p N) := by
  intro hdiv
  have hzeroChoose :
      Nat.choose N (p ^ Nat.log p N) ≡ 0 [MOD p] :=
    hdiv.modEq_zero_nat
  have hcong := choose_primePower_modEq_div_pow N p (Nat.log p N)
  have hzeroQuotient :
      N / p ^ Nat.log p N ≡ 0 [MOD p] :=
    hcong.symm.trans hzeroChoose
  exact prime_not_dvd_highestVisiblePrimePower_quotient hN
    (Nat.modEq_zero_iff_dvd.mp hzeroQuotient)

/-- Exact carry-free valuation of the auxiliary highest-visible shell. -/
theorem padicValNat_choose_highestVisiblePrimePower_eq_zero
    {N p : ℕ} [Fact p.Prime] (hN : N ≠ 0) :
    padicValNat p (Nat.choose N (p ^ Nat.log p N)) = 0 :=
  padicValNat.eq_zero_of_not_dvd
    (prime_not_dvd_choose_highestVisiblePrimePower hN)

end EnterpriseMath.Precision
