import EnterpriseMath.Quotient.RootQuotientPenultimateCoverGeometry
import EnterpriseMath.Quotient.RootQuotientPrimeShellBinary
import Mathlib.Data.List.Count
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A product of `n` naturals each at least three is at least `3^n`. -/
theorem pow_three_length_le_list_prod
    {l : List ℕ}
    (hThree : ∀ a : ℕ, a ∈ l → 3 ≤ a) :
    3 ^ l.length ≤ l.prod := by
  induction l with
  | nil => simp
  | cons a l ih =>
      have haThree : 3 ≤ a := hThree a (by simp)
      have hTail : ∀ b : ℕ, b ∈ l → 3 ≤ b := by
        intro b hb
        exact hThree b (by simp [hb])
      have hInd := ih hTail
      simp only [List.length_cons, List.prod_cons, pow_succ]
      simpa [Nat.mul_comm] using Nat.mul_le_mul haThree hInd

/-- If a nonempty prime list contains the prime `2` at most once, its product
is bounded below by one factor `2` and all remaining factors `3`.

No sorting assumption is needed. -/
theorem two_mul_pow_three_pred_length_le_prod_of_prime_list
    {l : List ℕ}
    (hPrime : ∀ p : ℕ, p ∈ l → p.Prime)
    (hCountTwo : l.count 2 ≤ 1)
    (hNonempty : l ≠ []) :
    2 * 3 ^ (l.length - 1) ≤ l.prod := by
  induction l with
  | nil => exact (hNonempty rfl).elim
  | cons a l ih =>
      have haPrime : a.Prime := hPrime a (by simp)
      have hTailPrime : ∀ p : ℕ, p ∈ l → p.Prime := by
        intro p hp
        exact hPrime p (by simp [hp])
      by_cases haTwo : a = 2
      · subst a
        have hTailCountZero : l.count 2 = 0 := by
          rw [List.count_cons] at hCountTwo
          simp at hCountTwo
          omega
        have hTailThree : ∀ p : ℕ, p ∈ l → 3 ≤ p := by
          intro p hp
          have hpPrime := hTailPrime p hp
          have hpNeTwo : p ≠ 2 := by
            intro hpTwo
            subst p
            have hPos : 0 < l.count 2 := List.count_pos_iff.2 hp
            omega
          have hpTwoLe := hpPrime.two_le
          omega
        have hLower := pow_three_length_le_list_prod hTailThree
        simpa using Nat.mul_le_mul_left 2 hLower
      · have haThree : 3 ≤ a := by
          have haTwoLe := haPrime.two_le
          omega
        have hTailCount : l.count 2 ≤ 1 := by
          rw [List.count_cons] at hCountTwo
          simp [haTwo] at hCountTwo
          exact hCountTwo
        cases l with
        | nil =>
            simpa using haPrime.two_le
        | cons b t =>
            have hTailNonempty : b :: t ≠ [] := by simp
            have hIH := ih hTailPrime hTailCount hTailNonempty
            have hScale :
                3 * (2 * 3 ^ t.length) ≤
                  a * (2 * 3 ^ t.length) :=
              Nat.mul_le_mul_right (2 * 3 ^ t.length) haThree
            calc
              2 * 3 ^ ((a :: b :: t).length - 1) =
                  3 * (2 * 3 ^ t.length) := by
                simp [pow_succ, Nat.mul_assoc, Nat.mul_comm,
                  Nat.mul_left_comm]
              _ ≤ a * (2 * 3 ^ t.length) := hScale
              _ ≤ a * (b :: t).prod := by
                have hIHSimple : 2 * 3 ^ t.length ≤ (b :: t).prod := by
                  simpa using hIH
                exact Nat.mul_le_mul_left a hIHSimple
              _ = (a :: b :: t).prod := by rfl

/-- Elementary exponential gap used by the binary penultimate theorem. -/
theorem two_pow_succ_lt_two_mul_three_pow_pred
    {L : ℕ}
    (hL : 3 ≤ L) :
    2 ^ (L + 1) < 2 * 3 ^ (L - 1) := by
  obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hL
  have hAux : ∀ t : ℕ,
      2 ^ (t + 4) < 2 * 3 ^ (t + 2) := by
    intro n
    induction n with
    | zero => norm_num
    | succ n ih =>
        have hMul :
            2 * (2 ^ (n + 4)) < 2 * (2 * 3 ^ (n + 2)) :=
          Nat.mul_lt_mul_left 2 ih
        have hPowPos : 0 < 3 ^ (n + 2) := by positivity
        have hFourSix :
            4 * 3 ^ (n + 2) < 6 * 3 ^ (n + 2) :=
          Nat.mul_lt_mul_right hPowPos (by omega)
        calc
          2 ^ (Nat.succ n + 4) = 2 * (2 ^ (n + 4)) := by
            rw [show Nat.succ n + 4 = (n + 4) + 1 by omega, pow_succ]
            ring
          _ < 2 * (2 * 3 ^ (n + 2)) := hMul
          _ = 4 * 3 ^ (n + 2) := by ring
          _ < 6 * 3 ^ (n + 2) := hFourSix
          _ = 2 * 3 ^ (Nat.succ n + 2) := by
            rw [show Nat.succ n + 2 = (n + 2) + 1 by omega, pow_succ]
            ring
  have h := hAux t
  convert h using 1 <;> omega

/-- In the binary/high-root regime with exact prime horizon at least three,
every maximal-rank semantic boundary is divisible by `4`.

The proof avoids enumerating maximal boundaries.  If `4∤b`, the prime factor
`2` occurs at most once, forcing `b>=2*3^(L-1)`, but maximal rank and the binary
logarithmic shell put `b<2^(L+1)`, impossible for `L>=3`. -/
theorem four_dvd_every_maximalBoundary_in_binary_regime
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hBinary : N < 2 ^ r)
    (hHorizon : 3 ≤ rootQuotientPrimeHorizon r N) :
    ∀ b : ℕ,
      RootQuotientMaximalPrimeRankBoundary r N b →
      4 ∣ b := by
  have hLog : rootQuotientPrimeHorizon r N = Nat.log 2 N :=
    rootQuotientPrimeHorizon_eq_nat_log_two_of_stateBound_lt_two_pow_rootOrder
      hr hN hBinary
  have hLogThree : 3 ≤ Nat.log 2 N := by
    rw [← hLog]
    exact hHorizon
  intro b hbMax
  by_contra hNotFour
  have hbZero : b ≠ 0 := by omega
  have hNotPow : ¬2 ^ 2 ∣ b := by
    have hPow : 2 ^ 2 = (4 : ℕ) := by norm_num
    simpa [hPow] using hNotFour
  have hFactorTwoLeOne : b.factorization 2 ≤ 1 := by
    have hNotTwo : ¬2 ≤ b.factorization 2 := by
      intro hTwo
      exact hNotPow
        ((Nat.prime_two.pow_dvd_iff_le_factorization hbZero).2 hTwo)
    omega
  have hCountTwo : b.primeFactorsList.count 2 ≤ 1 := by
    rw [Nat.primeFactorsList_count_eq]
    exact hFactorTwoLeOne
  have hPrimeList : ∀ p : ℕ, p ∈ b.primeFactorsList → p.Prime := by
    intro p hp
    exact Nat.prime_of_mem_primeFactorsList hp
  have hLength : b.primeFactorsList.length = Nat.log 2 N := by
    have hbCount := hbMax.2.2.2
    rw [hLog] at hbCount
    simpa [rootQuotientPrimeFactorCount] using hbCount
  have hListNonempty : b.primeFactorsList ≠ [] := by
    intro hNil
    have hZeroLen : b.primeFactorsList.length = 0 := by simp [hNil]
    rw [hLength] at hZeroLen
    omega
  have hLower :=
    two_mul_pow_three_pred_length_le_prod_of_prime_list
      hPrimeList hCountTwo hListNonempty
  rw [Nat.prod_primeFactorsList hbZero] at hLower
  rw [hLength] at hLower
  have hUpperN : N < 2 ^ (Nat.log 2 N + 1) :=
    Nat.lt_pow_succ_log_self (by omega) N
  have hbUpper : b < 2 ^ (Nat.log 2 N + 1) :=
    hbMax.2.1.trans_lt hUpperN
  have hGap := two_pow_succ_lt_two_mul_three_pow_pred hLogThree
  omega

/-- The macro `4` is a bounded semantic semiprime and a common divisor of all
maximal-rank boundaries in the binary/high-root regime once `L>=3`. -/
theorem four_is_common_maximal_semiprime_divisor_in_binary_regime
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hBinary : N < 2 ^ r)
    (hHorizon : 3 ≤ rootQuotientPrimeHorizon r N) :
    RootQuotientCommonMaximalSemiprimeDivisor r N 4 := by
  have hLog : rootQuotientPrimeHorizon r N = Nat.log 2 N :=
    rootQuotientPrimeHorizon_eq_nat_log_two_of_stateBound_lt_two_pow_rootOrder
      hr hN hBinary
  have hLogThree : 3 ≤ Nat.log 2 N := by
    rw [← hLog]
    exact hHorizon
  have hNZero : N ≠ 0 := by omega
  have hPowLog : 2 ^ Nat.log 2 N ≤ N :=
    Nat.pow_log_le_self 2 hNZero
  have hEightLePow : 2 ^ 3 ≤ 2 ^ Nat.log 2 N :=
    Nat.pow_le_pow_right (by omega) hLogThree
  have hEightLeN : 8 ≤ N := by
    norm_num at hEightLePow
    omega
  have hRootFour : 2 < r := by
    by_contra hNot
    have hrLe : r ≤ 2 := by omega
    have hPowLe : 2 ^ r ≤ 2 ^ 2 :=
      Nat.pow_le_pow_right (by omega) hrLe
    norm_num at hPowLe
    omega
  have hFourFree : RPowerFree r 4 := by
    have h := two_pow_rPowerFree_of_exponent_lt_rootOrder
      (r := r) (k := 2) hRootFour
    norm_num at h ⊢
    exact h
  have hFourCount : rootQuotientPrimeFactorCount 4 = 2 := by
    have h := rootQuotientPrimeFactorCount_two_pow 2
    norm_num at h ⊢
    exact h
  refine ⟨⟨by omega, by omega, hFourFree⟩, hFourCount, ?_⟩
  intro b hbMax
  exact four_dvd_every_maximalBoundary_in_binary_regime
    hr hN hBinary hHorizon b hbMax

/-- Exact binary penultimate cover number: one composite macro type suffices and
is necessary. -/
theorem rootQuotientPenultimateSemiprimeCoverNumber_eq_one_in_binary_regime
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hBinary : N < 2 ^ r)
    (hHorizon : 3 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientPenultimateSemiprimeCoverNumber r N = 1 := by
  apply (rootQuotientPenultimateSemiprimeCoverNumber_eq_one_iff_common
    (by omega)).2
  exact ⟨4,
    four_is_common_maximal_semiprime_divisor_in_binary_regime
      hr hN hBinary hHorizon⟩

/-- Exact binary penultimate storage law: one macro beyond the forced primes. -/
theorem rootQuotientMinimumStorageSize_penultimate_eq_prime_add_one_in_binary_regime
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hBinary : N < 2 ^ r)
    (hHorizon : 3 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumStorageSize
        r N (rootQuotientPrimeHorizon r N - 1) =
      (RootQuotientPrimeBasis N).ncard + 1 := by
  exact
    (rootQuotientMinimumStorageSize_penultimate_eq_prime_add_one_iff_common
      hr (by omega)).2
      ⟨4, four_is_common_maximal_semiprime_divisor_in_binary_regime
        hr hN hBinary hHorizon⟩

/-- In the binary/high-root regime the explicit single macro `4`, together
with bounded primes, separates at the penultimate prime horizon. -/
theorem prime_union_four_separates_penultimate_in_binary_regime
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 1 ≤ N)
    (hBinary : N < 2 ^ r)
    (hHorizon : 3 ≤ rootQuotientPrimeHorizon r N) :
    SeparatesRootQuotientWordsUpTo
      r N (rootQuotientPrimeHorizon r N - 1)
      (RootQuotientPrimeBasis N ∪ ({4} : Set ℕ)) := by
  have hCommon :=
    four_is_common_maximal_semiprime_divisor_in_binary_regime
      hr hN hBinary hHorizon
  obtain ⟨hSemi, hCover⟩ := singleton_semiprime_divisorCover_of_common hCommon
  exact
    (prime_union_semiprimeFamily_separates_penultimate_iff_divisorCover
      hr (by omega) hSemi).2 hCover

end EnterpriseMath.Quotient
