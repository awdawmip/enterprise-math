import EnterpriseMath.Quotient.RootQuotientThreeMacroStableOptimality
import EnterpriseMath.Quotient.RootQuotientMacroPareto
import Mathlib.Data.Nat.Log
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Arithmetic inverse for the stable q=7 three-macro state threshold. -/
theorem four_add_log_seven_div_sixty_le_iff_stateBound_lt_threeMacroStableThreshold
    {N h : ℕ}
    (hN : 60 ≤ N)
    (hh : 3 ≤ h) :
    4 + Nat.log 7 (N / 60) ≤ h ↔
      N < rootQuotientThreeMacroStableThreshold h := by
  have hDivPos : N / 60 ≠ 0 := by omega
  dsimp [rootQuotientThreeMacroStableThreshold]
  calc
    4 + Nat.log 7 (N / 60) ≤ h ↔
        1 + Nat.log 7 (N / 60) ≤ h - 3 := by omega
    _ ↔ Nat.log 7 (N / 60) < h - 3 := by omega
    _ ↔ N / 60 < 7 ^ (h - 3) :=
      Nat.log_lt_iff_lt_pow (by omega) hDivPos
    _ ↔ N < 7 ^ (h - 3) * 60 := by
      rw [Nat.div_lt_iff_lt_mul]
    _ ↔ N < 60 * 7 ^ (h - 3) := by
      rw [Nat.mul_comm]

/-- **Exact stable execution horizon for optional macro budget three.**

Beyond the explicit state threshold `60*7^7 = 49,412,580`, both the optimum
horizon and its predecessor lie inside the globally proved saturated q=7 tail.
The true optimum is therefore the exact logarithmic inverse

`D_3(N) = 4 + log_7(floor(N/60))`.

This is the budget-three analogue of the exact budget-two base-five tail. -/
theorem minimumHorizonAtCompositeMacroBudget_three_eq_stable_log_of_threshold_le
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 49412580 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N 3 =
      4 + Nat.log 7 (N / 60) := by
  let H := 4 + Nat.log 7 (N / 60)
  have hN2 : 2 ≤ N := by omega
  have hDiv : 7 ^ 7 ≤ N / 60 := by
    apply (Nat.le_div_iff_mul_le (by omega)).2
    norm_num at hN ⊢
    exact hN
  have hLogSeven : 7 ≤ Nat.log 7 (N / 60) :=
    Nat.le_log_of_pow_le (by omega) hDiv
  have hHEleven : 11 ≤ H := by
    dsimp [H]
    omega
  have hPareto :=
    rootQuotientMinimumHorizonAtCompositeMacroBudget_eq_iff_interval
      (r := r) (N := N) (m := 3) (h := H) hr (by omega)
  apply hPareto.2
  constructor
  · have hUpper : N < rootQuotientThreeMacroStableThreshold H :=
      (four_add_log_seven_div_sixty_le_iff_stateBound_lt_threeMacroStableThreshold
        (N := N) (h := H) (by omega) (by omega)).1 (by simp [H])
    exact
      (minimumCompositeMacroCount_le_three_iff_stateBound_lt_threeMacroStableThreshold
        (r := r) (N := N) (h := H)
        hr (by omega) hN2 hBinary).2 hUpper
  · have hDivPos : N / 60 ≠ 0 := by omega
    have hPowLe : 7 ^ Nat.log 7 (N / 60) ≤ N / 60 :=
      Nat.pow_log_le_self 7 hDivPos
    have hScaled : 60 * 7 ^ Nat.log 7 (N / 60) ≤ N := by
      calc
        60 * 7 ^ Nat.log 7 (N / 60) ≤ 60 * (N / 60) :=
          Nat.mul_le_mul_left 60 hPowLe
        _ ≤ N := Nat.mul_div_le N 60
    have hPredThreshold : rootQuotientThreeMacroStableThreshold (H - 1) =
        60 * 7 ^ Nat.log 7 (N / 60) := by
      dsimp [rootQuotientThreeMacroStableThreshold, H]
      congr 1
      omega
    have hPredNotLe :
        ¬rootQuotientMinimumCompositeMacroCount r N (H - 1) ≤ 3 := by
      intro hLe
      have hBelow :=
        (minimumCompositeMacroCount_le_three_iff_stateBound_lt_threeMacroStableThreshold
          (r := r) (N := N) (h := H - 1)
          hr (by omega) hN2 hBinary).1 hLe
      rw [hPredThreshold] at hBelow
      omega
    omega

end EnterpriseMath.Quotient
