import EnterpriseMath.Quotient.RootQuotientPrimeBirthPenaltyFlow
import EnterpriseMath.Quotient.RootQuotientThreeMacroStableOptimality
import EnterpriseMath.Quotient.RootQuotientDivisorCoverFrontier
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- From horizon ten onward, the q=7 three-macro stable shell lies strictly
beyond the next pure direction birth `5^(h+1)`. -/
theorem five_pow_succ_lt_threeMacroStableThreshold_of_ten_le
    {h : ℕ}
    (hTen : 10 ≤ h) :
    5 ^ (h + 1) < rootQuotientThreeMacroStableThreshold h := by
  obtain ⟨n, rfl⟩ := Nat.exists_eq_add_of_le hTen
  have hPow : 5 ^ n ≤ 7 ^ n := Nat.pow_le_pow_left (by omega) n
  calc
    5 ^ (10 + n + 1) = 48828125 * 5 ^ n := by
      simp [pow_add]
      norm_num
    _ < 49412580 * 7 ^ n := by
      nlinarith [show 0 < 7 ^ n by positivity]
    _ = rootQuotientThreeMacroStableThreshold (10 + n) := by
      simp [rootQuotientThreeMacroStableThreshold, pow_add]
      norm_num

/-- Immediately before `5^(h+1)` enters, direction demand is two while both
cover and exact optional storage have already reached three.  Hence the old
state carries exactly one unit of mixed-cover overhead and zero residual-depth
overhead. -/
theorem resources_before_primeFive_birth_of_ten_le
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hTen : 10 ≤ h)
    (hBinary : 5 ^ (h + 1) < 2 ^ r) :
    rootQuotientPrimeDirectionDemand (5 ^ (h + 1) - 1) h = 2 ∧
    rootQuotientGlobalRepairDivisorCoverNumber
        r (5 ^ (h + 1) - 1) h = 3 ∧
    rootQuotientMinimumCompositeMacroCount
        r (5 ^ (h + 1) - 1) h = 3 := by
  let N := 5 ^ (h + 1) - 1
  have hh : 3 ≤ h := by omega
  have hThreeLt : 3 ^ (h + 1) < 5 ^ (h + 1) :=
    pow_lt_pow_left' (by omega : h + 1 ≠ 0) (by omega : (3 : ℕ) < 5)
  have hThreeLeN : 3 ^ (h + 1) ≤ N := by
    dsimp [N]
    omega
  have hNLtFive : N < 5 ^ (h + 1) := by
    dsimp [N]
    have hPos : 0 < 5 ^ (h + 1) := by positivity
    omega
  have hDir := primeDirectionDemand_eq_two_of_three_pow_le_of_lt_five_pow
    hThreeLeN hNLtFive
  have hCoverLower : 3 ≤ rootQuotientGlobalRepairDivisorCoverNumber r N h := by
    have hCoverThreshold : 6 * 5 ^ (h - 1) < 5 ^ (h + 1) :=
      six_mul_five_pow_lt_five_pow_succ (by omega)
    have hThresholdLeN : 6 * 5 ^ (h - 1) ≤ N := by
      dsimp [N]
      omega
    exact three_le_globalRepairDivisorCoverNumber_of_six_mul_five_pow_le
      hr hh (by dsimp [N]; omega) hThresholdLeN
  have hStable : N < rootQuotientThreeMacroStableThreshold h := by
    have hFiveStable := five_pow_succ_lt_threeMacroStableThreshold_of_ten_le hTen
    exact hNLtFive.trans hFiveStable
  have hN2 : 2 ≤ N := by
    have hFiveLe : 5 ≤ 5 ^ (h + 1) :=
      le_self_pow (by omega : (1 : ℕ) ≤ 5) (by omega : h + 1 ≠ 0)
    dsimp [N]
    omega
  have hMuUpper : rootQuotientMinimumCompositeMacroCount r N h ≤ 3 :=
    (minimumCompositeMacroCount_le_three_iff_stateBound_lt_threeMacroStableThreshold
      (r := r) (N := N) (h := h)
      hr hTen hN2 (by dsimp [N]; omega)).2 hStable
  have hCoverLeMu := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
    (r := r) (N := N) (h := h) hr (by omega)
  have hCover : rootQuotientGlobalRepairDivisorCoverNumber r N h = 3 := by omega
  have hMu : rootQuotientMinimumCompositeMacroCount r N h = 3 := by omega
  exact ⟨hDir, hCover, hMu⟩

/-- At the birth state `5^(h+1)`, all three storage layers equal three. -/
theorem resources_at_primeFive_birth_of_ten_le
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hTen : 10 ≤ h)
    (hBinary : 5 ^ (h + 1) < 2 ^ r) :
    rootQuotientPrimeDirectionDemand (5 ^ (h + 1)) h = 3 ∧
    rootQuotientGlobalRepairDivisorCoverNumber
        r (5 ^ (h + 1)) h = 3 ∧
    rootQuotientMinimumCompositeMacroCount
        r (5 ^ (h + 1)) h = 3 := by
  let N := 5 ^ (h + 1)
  have hSeven : N < 7 ^ (h + 1) := by
    dsimp [N]
    exact pow_lt_pow_left' (by omega : h + 1 ≠ 0) (by omega : (5 : ℕ) < 7)
  have hDirLe : rootQuotientPrimeDirectionDemand N h ≤ 3 :=
    (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
      (N := N) (h := h) (s := 3)).2 (by
        simpa [rootQuotientStablePrimeBase, N] using hSeven)
  have hDirNotTwo : ¬rootQuotientPrimeDirectionDemand N h ≤ 2 := by
    intro hLe
    have hState :=
      (primeDirectionDemand_le_iff_stateBound_lt_stablePrimeBase_pow_succ
        (N := N) (h := h) (s := 2)).1 hLe
    have : N < 5 ^ (h + 1) := by
      simpa [rootQuotientStablePrimeBase, N] using hState
    omega
  have hDir : rootQuotientPrimeDirectionDemand N h = 3 := by omega
  have hStable : N < rootQuotientThreeMacroStableThreshold h := by
    dsimp [N]
    exact five_pow_succ_lt_threeMacroStableThreshold_of_ten_le hTen
  have hN2 : 2 ≤ N := by
    dsimp [N]
    have hFiveLe : 5 ≤ 5 ^ (h + 1) :=
      le_self_pow (by omega : (1 : ℕ) ≤ 5) (by omega : h + 1 ≠ 0)
    omega
  have hMuUpper : rootQuotientMinimumCompositeMacroCount r N h ≤ 3 :=
    (minimumCompositeMacroCount_le_three_iff_stateBound_lt_threeMacroStableThreshold
      (r := r) (N := N) (h := h)
      hr hTen hN2 (by simpa [N] using hBinary)).2 hStable
  have hDirLeCover := primeDirectionDemand_le_globalRepairDivisorCoverNumber
    (r := r) (N := N) (h := h) hr (by omega) (by simpa [N] using hBinary)
  have hCoverLeMu := globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount
    (r := r) (N := N) (h := h) hr (by omega)
  have hCover : rootQuotientGlobalRepairDivisorCoverNumber r N h = 3 := by omega
  have hMu : rootQuotientMinimumCompositeMacroCount r N h = 3 := by omega
  exact ⟨hDir, hCover, hMu⟩

/-- **Stable prime-five birth is a pure direction catch-up event.**

For every `h>=10`, once the bounded domain is high-root, the transition
`5^(h+1)-1 -> 5^(h+1)` has event `(1,0,0)`: cover and exact storage had already
preinvested in the future five-direction before it became information-
theoretically mandatory. -/
theorem resourceEvent_at_primeFive_birth_of_ten_le
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hTen : 10 ≤ h)
    (hBinary : 5 ^ (h + 1) < 2 ^ r) :
    rootQuotientResourceEvent r (5 ^ (h + 1) - 1) h =
      rootQuotientDirectionCatchupEvent := by
  let T := 5 ^ (h + 1)
  have hBefore := resources_before_primeFive_birth_of_ten_le
    (r := r) (h := h) hr hTen hBinary
  have hAt := resources_at_primeFive_birth_of_ten_le
    (r := r) (h := h) hr hTen hBinary
  have hSucc : (T - 1) + 1 = T := by
    have hPos : 0 < T := by dsimp [T]; positivity
    omega
  dsimp [rootQuotientResourceEvent, rootQuotientDirectionCatchupEvent]
  rw [show 5 ^ (h + 1) = T by rfl, hSucc,
    hBefore.1, hBefore.2.1, hBefore.2.2,
    hAt.1, hAt.2.1, hAt.2.2]
  rfl

/-- In particular, canonical preinvestment dominance holds at every stable
prime-five birth. -/
theorem primeBirthPreinvestmentDominance_at_primeFive_of_ten_le
    {r h : ℕ}
    (hr : 2 ≤ r)
    (hTen : 10 ≤ h)
    (hBinary : 5 ^ (h + 1) < 2 ^ r) :
    RootQuotientPrimeBirthPreinvestmentDominance
      r (5 ^ (h + 1) - 1) h 5 := by
  have hBirth : (5 ^ (h + 1) - 1) + 1 = 5 ^ (h + 1) := by
    have hPos : 0 < 5 ^ (h + 1) := by positivity
    omega
  apply (primeBirthPreinvestmentDominance_iff_not_dualCatchupEvent
    (r := r) (N := 5 ^ (h + 1) - 1) (h := h) (p := 5)
    hr (by omega) (by norm_num) hBirth (by simpa [hBirth] using hBinary)).2
  intro hDual
  have hCatch := resourceEvent_at_primeFive_birth_of_ten_le
    (r := r) (h := h) hr hTen hBinary
  rw [hCatch] at hDual
  norm_num [rootQuotientDirectionCatchupEvent,
    rootQuotientDualCatchupEvent] at hDual

end EnterpriseMath.Quotient
