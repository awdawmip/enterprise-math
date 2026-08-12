import EnterpriseMath.Quotient.RootQuotientTwoMacroHorizonTwo
import EnterpriseMath.Quotient.RootQuotientMacroPareto
import Mathlib.Data.Nat.Log
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Exact inverse interval law for optional macro budget two.

For every horizon `h>=3`, the minimum execution depth with two optional macros
is exactly `h` iff the state bound lies between consecutive exact budget-two
capacity thresholds. -/
theorem minimumHorizonAtCompositeMacroBudget_two_eq_iff_threshold_interval
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 3 ≤ h)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N 2 = h ↔
      rootQuotientTwoMacroFullThreshold (h - 1) ≤ N ∧
        N < rootQuotientTwoMacroFullThreshold h := by
  have hPareto :=
    rootQuotientMinimumHorizonAtCompositeMacroBudget_eq_iff_interval
      (r := r) (N := N) (m := 2) (h := h) hr (by omega)
  constructor
  · intro hEq
    have hInterval := hPareto.1 hEq
    have hUpper :=
      (minimumCompositeMacroCount_le_two_iff_stateBound_lt_twoMacroFullThreshold
        (r := r) (N := N) (h := h)
        hr (by omega) hN hBinary).1 hInterval.1
    have hLower : rootQuotientTwoMacroFullThreshold (h - 1) ≤ N := by
      by_contra hNot
      have hPredBelow : N < rootQuotientTwoMacroFullThreshold (h - 1) := by omega
      have hPredLe :=
        (minimumCompositeMacroCount_le_two_iff_stateBound_lt_twoMacroFullThreshold
          (r := r) (N := N) (h := h - 1)
          hr (by omega) hN hBinary).2 hPredBelow
      omega
    exact ⟨hLower, hUpper⟩
  · rintro ⟨hLower, hUpper⟩
    apply hPareto.2
    constructor
    · exact
        (minimumCompositeMacroCount_le_two_iff_stateBound_lt_twoMacroFullThreshold
          (r := r) (N := N) (h := h)
          hr (by omega) hN hBinary).2 hUpper
    · have hPredNotLe : ¬rootQuotientMinimumCompositeMacroCount r N (h - 1) ≤ 2 := by
        intro hLe
        have hPredBelow :=
          (minimumCompositeMacroCount_le_two_iff_stateBound_lt_twoMacroFullThreshold
            (r := r) (N := N) (h := h - 1)
            hr (by omega) hN hBinary).1 hLe
        omega
      omega

/-- The first three nontrivial exact depth phases under budget two. -/
theorem minimumHorizonAtCompositeMacroBudget_two_eq_three_iff
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N 2 = 3 ↔
      27 ≤ N ∧ N < 96 := by
  simpa [rootQuotientTwoMacroFullThreshold,
    rootQuotientTwoMacroOptimalThreshold,
    rootQuotientFourNineThreshold] using
    (minimumHorizonAtCompositeMacroBudget_two_eq_iff_threshold_interval
      (r := r) (N := N) (h := 3) hr (by omega) hN hBinary)

/-- Horizon four phase. -/
theorem minimumHorizonAtCompositeMacroBudget_two_eq_four_iff
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N 2 = 4 ↔
      96 ≤ N ∧ N < 384 := by
  simpa [rootQuotientTwoMacroFullThreshold,
    rootQuotientTwoMacroOptimalThreshold,
    rootQuotientFourNineThreshold] using
    (minimumHorizonAtCompositeMacroBudget_two_eq_iff_threshold_interval
      (r := r) (N := N) (h := 4) hr (by omega) hN hBinary)

/-- Horizon five phase. -/
theorem minimumHorizonAtCompositeMacroBudget_two_eq_five_iff
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N 2 = 5 ↔
      384 ≤ N ∧ N < 1536 := by
  simpa [rootQuotientTwoMacroFullThreshold,
    rootQuotientTwoMacroOptimalThreshold,
    rootQuotientFourNineThreshold] using
    (minimumHorizonAtCompositeMacroBudget_two_eq_iff_threshold_interval
      (r := r) (N := N) (h := 5) hr (by omega) hN hBinary)

/-- Horizon six is the crossover point where the stable `8,9` code first wins. -/
theorem minimumHorizonAtCompositeMacroBudget_two_eq_six_iff
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N 2 = 6 ↔
      1536 ≤ N ∧ N < 7500 := by
  simpa [rootQuotientTwoMacroFullThreshold,
    rootQuotientTwoMacroOptimalThreshold,
    rootQuotientFourNineThreshold,
    rootQuotientEightNineThreshold] using
    (minimumHorizonAtCompositeMacroBudget_two_eq_iff_threshold_interval
      (r := r) (N := N) (h := 6) hr (by omega) hN hBinary)

/-- Arithmetic bridge for the exact stable two-macro tail. -/
theorem three_add_log_five_div_twelve_le_iff_stateBound_lt_eightNineThreshold
    {N h : ℕ}
    (hN : 12 ≤ N)
    (hh : 2 ≤ h) :
    3 + Nat.log 5 (N / 12) ≤ h ↔
      N < rootQuotientEightNineThreshold h := by
  have hDivPos : N / 12 ≠ 0 := by omega
  dsimp [rootQuotientEightNineThreshold]
  calc
    3 + Nat.log 5 (N / 12) ≤ h ↔
        1 + Nat.log 5 (N / 12) ≤ h - 2 := by omega
    _ ↔ Nat.log 5 (N / 12) < h - 1 := by omega
    _ ↔ N / 12 < 5 ^ (h - 1) :=
      Nat.log_lt_iff_lt_pow (by omega) hDivPos
    _ ↔ N < 5 ^ (h - 1) * 12 := by
      rw [Nat.div_lt_iff_lt_mul]
    _ ↔ N < 12 * 5 ^ (h - 2) := by
      rw [show h - 1 = (h - 2) + 1 by omega, pow_add]
      ring

/-- **Exact stable tail horizon under optional macro budget two.**

Once `N>=1536`, all finite transient code phases are past.  The exact optimum
is the next-prime-5 logarithmic law with constant `12` and offset `3`:

`D_2(N) = 3 + log_5(floor(N/12))`.

Thus the stable-base theorem is not merely asymptotic for budget two: after an
explicit finite crossover, it becomes an exact closed form. -/
theorem minimumHorizonAtCompositeMacroBudget_two_eq_stable_log_of_1536_le
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 1536 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N 2 =
      3 + Nat.log 5 (N / 12) := by
  let H := 3 + Nat.log 5 (N / 12)
  have hN2 : 2 ≤ N := by omega
  have hDiv : 128 ≤ N / 12 := by omega
  have hLogThree : 3 ≤ Nat.log 5 (N / 12) :=
    Nat.le_log_of_pow_le (by omega) (by norm_num; omega)
  have hHSix : 6 ≤ H := by dsimp [H]; omega
  apply (minimumHorizonAtCompositeMacroBudget_two_eq_iff_threshold_interval
    (r := r) (N := N) (h := H) hr (by omega) hN2 hBinary).2
  constructor
  · by_cases hHEq : H = 6
    · subst H
      simpa [rootQuotientTwoMacroFullThreshold,
        rootQuotientTwoMacroOptimalThreshold,
        rootQuotientFourNineThreshold] using hN
    · have hHSeven : 7 ≤ H := by omega
      have hPredFive : ¬H - 1 ≤ 5 := by omega
      have hPredThreshold : rootQuotientTwoMacroFullThreshold (H - 1) =
          12 * 5 ^ (H - 3) := by
        simp [rootQuotientTwoMacroFullThreshold,
          rootQuotientTwoMacroOptimalThreshold, hPredFive,
          rootQuotientEightNineThreshold]
      rw [hPredThreshold]
      have hDivPos : N / 12 ≠ 0 := by omega
      have hPowLe : 5 ^ Nat.log 5 (N / 12) ≤ N / 12 :=
        Nat.pow_log_le_self 5 hDivPos
      have hScaled : 12 * 5 ^ Nat.log 5 (N / 12) ≤ N := by
        calc
          12 * 5 ^ Nat.log 5 (N / 12) ≤ 12 * (N / 12) :=
            Nat.mul_le_mul_left 12 hPowLe
          _ ≤ N := Nat.mul_div_le N 12
      have hExp : H - 3 = Nat.log 5 (N / 12) := by
        dsimp [H]
        omega
      rw [hExp]
      exact hScaled
  · have hHNotFive : ¬H ≤ 5 := by omega
    have hThreshold : rootQuotientTwoMacroFullThreshold H =
        rootQuotientEightNineThreshold H := by
      simp [rootQuotientTwoMacroFullThreshold,
        rootQuotientTwoMacroOptimalThreshold, hHNotFive]
    rw [hThreshold]
    exact
      (three_add_log_five_div_twelve_le_iff_stateBound_lt_eightNineThreshold
        (N := N) (h := H) (by omega) (by omega)).1 (by simp [H])

end EnterpriseMath.Quotient
