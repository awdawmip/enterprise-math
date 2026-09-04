import EnterpriseMath.Precision.HammingShellSpectrum
import Mathlib.NumberTheory.Chebyshev

namespace EnterpriseMath.Precision

open Finset

/--
The finite synchronization clock of the shell-zero amplitudes in Hamming row `m`.
By `hammingShellMode_zero`, these are exactly the Pascal-row amplitudes
`choose m 0, ..., choose m m` of the genuine Krawtchouk modes.
-/
def hammingRowClock (m : ℕ) : ℕ :=
  (Finset.range (m + 1)).lcm (Nat.choose m)

/-- Every physical Pascal/Krawtchouk shell-zero amplitude divides the row clock. -/
theorem choose_dvd_hammingRowClock {m k : ℕ} (hk : k ≤ m) :
    Nat.choose m k ∣ hammingRowClock m := by
  unfold hammingRowClock
  exact Finset.dvd_lcm (Finset.mem_range.mpr (Nat.lt_succ_iff.mpr hk))

/-- The finite Hamming row clock is nonzero. -/
theorem hammingRowClock_ne_zero (m : ℕ) : hammingRowClock m ≠ 0 := by
  unfold hammingRowClock
  rw [Finset.lcm_ne_zero_iff]
  intro k hk
  exact (Nat.choose_pos (Nat.lt_succ_iff.mp (Finset.mem_range.mp hk))).ne'

/-- The finite Hamming row clock is positive. -/
theorem hammingRowClock_pos (m : ℕ) : 0 < hammingRowClock m :=
  Nat.pos_of_ne_zero (hammingRowClock_ne_zero m)

/--
The row clock uses no prime-power winding beyond the ordinary saturated envelope
`lcm(1,...,m)`.
-/
theorem hammingRowClock_dvd_lcmUpto (m : ℕ) :
    hammingRowClock m ∣ Nat.lcmUpto m := by
  unfold hammingRowClock
  apply Finset.lcm_dvd
  intro k hk
  exact Chebyshev.choose_dvd_lcmUpto
    (Nat.lt_succ_iff.mp (Finset.mem_range.mp hk))

/-- Numerical monotonicity consequence of the previous divisibility theorem. -/
theorem hammingRowClock_le_lcmUpto (m : ℕ) :
    hammingRowClock m ≤ Nat.lcmUpto m :=
  Nat.le_of_dvd (Nat.lcmUpto_pos m) (hammingRowClock_dvd_lcmUpto m)

/--
The total Hamming row mass is bounded by the number of modes times the common
synchronization clock.
-/
theorem two_pow_le_mul_hammingRowClock (m : ℕ) :
    2 ^ m ≤ (m + 1) * hammingRowClock m := by
  calc
    2 ^ m = ∑ k ∈ Finset.range (m + 1), Nat.choose m k :=
      (Nat.sum_range_choose m).symm
    _ ≤ ∑ _k ∈ Finset.range (m + 1), hammingRowClock m := by
      gcongr with k hk
      exact Nat.le_of_dvd (hammingRowClock_pos m)
        (choose_dvd_hammingRowClock
          (Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)))
    _ = (m + 1) * hammingRowClock m := by simp

/-- The normalized Hamming clock at row `m`. -/
def hammingSaturatedClock (m : ℕ) : ℕ :=
  (m + 1) * hammingRowClock m

/-- The normalized Hamming clock dominates the full binary branch mass `2^m`. -/
theorem two_pow_le_hammingSaturatedClock (m : ℕ) :
    2 ^ m ≤ hammingSaturatedClock m := by
  simpa [hammingSaturatedClock] using two_pow_le_mul_hammingRowClock m

/--
Every physical shell-zero Krawtchouk amplitude divides the row clock, expressed
as an exact rational quotient in the current spectral carrier.
-/
theorem hammingShellMode_zero_mul_quotient
    {m k : ℕ} (hk : k ≤ m) :
    ∃ q : ℕ,
      (hammingRowClock m : ℚ) =
        hammingShellMode m k 0 * (q : ℚ) := by
  rcases choose_dvd_hammingRowClock hk with ⟨q, hq⟩
  refine ⟨q, ?_⟩
  rw [hammingShellMode_zero]
  exact_mod_cast hq

end EnterpriseMath.Precision
