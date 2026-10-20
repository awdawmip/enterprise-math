import EnterpriseMath.Quotient.RootQuotientSingleMacroOptimizerSet
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Elementary comparison used in the penultimate optimizer classification:
for `d>=2`, replacing `d+1` factors two by `d` factors three does not decrease
the product. -/
theorem two_pow_succ_le_three_pow_of_two_le
    {d : ℕ}
    (hd : 2 ≤ d) :
    2 ^ (d + 1) ≤ 3 ^ d := by
  cases d with
  | zero => omega
  | succ d =>
      cases d with
      | zero => omega
      | succ n =>
          induction n with
          | zero => norm_num
          | succ n ih =>
              have hScaled : 2 * 2 ^ (Nat.succ n + 2) ≤
                  2 * 3 ^ (Nat.succ n + 1) :=
                Nat.mul_le_mul_left 2 ih
              have hRaise : 2 * 3 ^ (Nat.succ n + 1) ≤
                  3 * 3 ^ (Nat.succ n + 1) :=
                Nat.mul_le_mul_right (3 ^ (Nat.succ n + 1)) (by omega)
              calc
                2 ^ (Nat.succ (Nat.succ n) + 1) =
                    2 * 2 ^ (Nat.succ n + 2) := by
                  rw [show Nat.succ (Nat.succ n) + 1 = (Nat.succ n + 2) + 1 by omega,
                    pow_succ]
                  ring
                _ ≤ 2 * 3 ^ (Nat.succ n + 1) := hScaled
                _ ≤ 3 * 3 ^ (Nat.succ n + 1) := hRaise
                _ = 3 ^ Nat.succ (Nat.succ n) := by
                  rw [pow_succ]

/-- For a power macro exponent strictly below the prime horizon, the generalized
penultimate hard shell already lies beyond the whole dyadic state shell. -/
theorem two_pow_succ_primeHorizon_le_penultimate_twoPowerShell_of_lt
    {r N m : ℕ}
    (hm : 2 ≤ m)
    (hmL : m < rootQuotientPrimeHorizon r N) :
    2 ^ (rootQuotientPrimeHorizon r N + 1) ≤
      rootQuotientPrimeTwoPowerShellMinimumCandidate
        m (rootQuotientPrimeHorizon r N) := by
  let L := rootQuotientPrimeHorizon r N
  let d := L - m + 1
  have hmLe : m - 1 ≤ L := by omega
  have hdTwo : 2 ≤ d := by
    dsimp [d, L]
    omega
  rw [primeTwoPowerShellCandidate_eq_twoPow_mul_threePow_of_le hmLe]
  have hExp : L - (m - 1) = d := by
    dsimp [d, L]
    omega
  rw [hExp]
  have hCore := two_pow_succ_le_three_pow_of_two_le hdTwo
  have hMul := Nat.mul_le_mul_left (2 ^ (m - 1)) hCore
  have hPowSplit :
      2 ^ (L + 1) = 2 ^ (m - 1) * 2 ^ (d + 1) := by
    rw [← pow_add]
    congr 1
    dsimp [d, L]
    omega
  rw [hPowSplit]
  exact hMul

/-- At exponent exactly `m=L`, the generalized penultimate shell is the single
secondary threshold `3*2^(L-1)`. -/
theorem primeTwoPowerShell_at_primeHorizon_exponent_eq
    {r N : ℕ} :
    rootQuotientPrimeTwoPowerShellMinimumCandidate
        (rootQuotientPrimeHorizon r N)
        (rootQuotientPrimeHorizon r N) =
      3 * 2 ^ (rootQuotientPrimeHorizon r N - 1) := by
  let L := rootQuotientPrimeHorizon r N
  by_cases hLZero : L = 0
  · subst L
    simp [rootQuotientPrimeTwoPowerShellMinimumCandidate]
  · have hLe : L - 1 ≤ L := by omega
    rw [primeTwoPowerShellCandidate_eq_twoPow_mul_threePow_of_le hLe]
    have hSub : L - (L - 1) = 1 := by omega
    rw [hSub]
    simp [Nat.mul_comm]

/-- Complete binary/high-root classification of one composite semantic macro
at the penultimate prime horizon.

Every such macro is a power `2^m`.  All exponents `2<=m<L` work automatically.
The boundary macro `2^L` works exactly on the lower part of the dyadic shell,
`N<3*2^(L-1)`. -/
theorem singleCompositeMacro_separates_penultimate_iff_powerRange
    {r N g : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N)
    (hgSemantic : g ∈ RootQuotientNontrivialPowerFreeBasis r N)
    (hgRank : 2 ≤ rootQuotientPrimeFactorCount g) :
    SeparatesRootQuotientWordsUpTo
        r N (rootQuotientPrimeHorizon r N - 1)
        (RootQuotientPrimeSingleMacroBasis N g) ↔
      ∃ m : ℕ,
        2 ≤ m ∧
        m ≤ rootQuotientPrimeHorizon r N ∧
        g = 2 ^ m ∧
        (m < rootQuotientPrimeHorizon r N ∨
          N < 3 * 2 ^ (rootQuotientPrimeHorizon r N - 1)) := by
  let L := rootQuotientPrimeHorizon r N
  constructor
  · intro hSep
    have hFast : L - 1 < L := by omega
    obtain ⟨m, hm, hgEq⟩ :=
      exists_twoPower_macro_of_singleCompositeMacro_strict_speedup
        (r := r) (N := N) (g := g) (h := L - 1)
        hr hN hBinary hgSemantic hgRank hSep hFast
    have hPowN : 2 ^ m ≤ N := by
      rw [← hgEq]
      exact hgSemantic.2.1
    have hNZero : N ≠ 0 := by omega
    have hmLog : m ≤ Nat.log 2 N :=
      Nat.le_log_of_pow_le (by omega) hPowN
    have hLog : L = Nat.log 2 N := by
      dsimp [L]
      exact rootQuotientPrimeHorizon_eq_nat_log_two_of_stateBound_lt_two_pow_rootOrder
        hr (by omega) hBinary
    have hmL : m ≤ L := by rw [hLog]; exact hmLog
    have hSepM : SeparatesRootQuotientWordsUpTo
        r N (L - 1) (RootQuotientPrimeTwoPowerBasis N m) := by
      simpa [RootQuotientPrimeSingleMacroBasis,
        RootQuotientPrimeTwoPowerBasis, hgEq] using hSep
    have hShell : N <
        rootQuotientPrimeTwoPowerShellMinimumCandidate m L := by
      have hThreshold :=
        (primeTwoPowerBasis_separates_iff_stateBound_lt_nextShell
          (r := r) (N := N) (m := m) (h := L - 1)
          hr hm hN hBinary).1 hSepM
      simpa [show L - 1 + 1 = L by omega] using hThreshold
    refine ⟨m, hm, hmL, hgEq, ?_⟩
    by_cases hmEq : m = L
    · right
      subst m
      rw [primeTwoPowerShell_at_primeHorizon_exponent_eq] at hShell
      exact hShell
    · left
      omega
  · rintro ⟨m, hm, hmL, hgEq, hmCase⟩
    have hShell : N <
        rootQuotientPrimeTwoPowerShellMinimumCandidate m L := by
      rcases hmCase with hmLt | hSecondary
      · have hDyadicUpper : N < 2 ^ (L + 1) := by
          have hLog : L = Nat.log 2 N := by
            dsimp [L]
            exact rootQuotientPrimeHorizon_eq_nat_log_two_of_stateBound_lt_two_pow_rootOrder
              hr (by omega) hBinary
          rw [hLog]
          exact Nat.lt_pow_succ_log_self (by omega) N
        exact hDyadicUpper.trans_le
          (two_pow_succ_primeHorizon_le_penultimate_twoPowerShell_of_lt
            (r := r) (N := N) (m := m) hm hmLt)
      · have hmEq : m = L := by
          by_contra hNe
          have hmLt : m < L := by omega
          have hDyadicUpper : N < 2 ^ (L + 1) := by
            have hLog : L = Nat.log 2 N := by
              dsimp [L]
              exact rootQuotientPrimeHorizon_eq_nat_log_two_of_stateBound_lt_two_pow_rootOrder
                hr (by omega) hBinary
            rw [hLog]
            exact Nat.lt_pow_succ_log_self (by omega) N
          exact hDyadicUpper.trans_le
            (two_pow_succ_primeHorizon_le_penultimate_twoPowerShell_of_lt
              (r := r) (N := N) (m := m) hm hmLt)
        subst m
        rwa [primeTwoPowerShell_at_primeHorizon_exponent_eq]
    have hSepM : SeparatesRootQuotientWordsUpTo
        r N (L - 1) (RootQuotientPrimeTwoPowerBasis N m) :=
      (primeTwoPowerBasis_separates_iff_stateBound_lt_nextShell
        (r := r) (N := N) (m := m) (h := L - 1)
        hr hm hN hBinary).2 (by
          simpa [show L - 1 + 1 = L by omega] using hShell)
    simpa [RootQuotientPrimeSingleMacroBasis,
      RootQuotientPrimeTwoPowerBasis, hgEq] using hSepM

/-- Set-theoretic reading of the executable classification: at the penultimate
horizon, the admissible power-macro exponents are exactly `2,...,L-1`, plus `L`
when `N<3*2^(L-1)`. -/
theorem penultimate_powerMacro_exponent_criterion
    {r N m : ℕ}
    (hr : 2 ≤ r)
    (hm : 2 ≤ m)
    (hmL : m ≤ rootQuotientPrimeHorizon r N)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    SeparatesRootQuotientWordsUpTo
        r N (rootQuotientPrimeHorizon r N - 1)
        (RootQuotientPrimeTwoPowerBasis N m) ↔
      m < rootQuotientPrimeHorizon r N ∨
        N < 3 * 2 ^ (rootQuotientPrimeHorizon r N - 1) := by
  let L := rootQuotientPrimeHorizon r N
  have hNext : L - 1 + 1 = L := by omega
  rw [primeTwoPowerBasis_separates_iff_stateBound_lt_nextShell
    hr hm hN hBinary]
  rw [hNext]
  by_cases hmEq : m = L
  · subst m
    rw [primeTwoPowerShell_at_primeHorizon_exponent_eq]
    simp
  · have hmLt : m < L := by omega
    have hDyadicUpper : N < 2 ^ (L + 1) := by
      have hLog : L = Nat.log 2 N :=
        rootQuotientPrimeHorizon_eq_nat_log_two_of_stateBound_lt_two_pow_rootOrder
          hr (by omega) hBinary
      rw [hLog]
      exact Nat.lt_pow_succ_log_self (by omega) N
    have hAlways : N < rootQuotientPrimeTwoPowerShellMinimumCandidate m L :=
      hDyadicUpper.trans_le
        (two_pow_succ_primeHorizon_le_penultimate_twoPowerShell_of_lt
          (r := r) (N := N) (m := m) hm hmLt)
    simp [hmLt, hAlways]

end EnterpriseMath.Quotient
