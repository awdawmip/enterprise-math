import EnterpriseMath.Quotient.RootQuotientStableMacroBudgetSandwich
import Mathlib.Data.Nat.Prime.Nth
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A prime strictly below the stable base `q_s` is one of the first `s`
prime directions. -/
theorem exists_primeIndex_lt_budget_of_prime_lt_stableBase
    {s p : ℕ}
    (hpPrime : p.Prime)
    (hpLt : p < rootQuotientStablePrimeBase s) :
    ∃ i : ℕ, i < s ∧ Nat.nth Nat.Prime i = p := by
  have hpRange : p ∈ Set.range (Nat.nth Nat.Prime) :=
    Nat.subset_range_nth hpPrime
  obtain ⟨i, hiEq⟩ := hpRange
  have hNthLt : Nat.nth Nat.Prime i < Nat.nth Nat.Prime s := by
    rw [hiEq]
    simpa [rootQuotientStablePrimeBase] using hpLt
  exact ⟨i, (Nat.nth_lt_nth Nat.infinite_setOfPred_prime).1 hNthLt, hiEq⟩

/-- Sharper residual token bound for the same coarse macro ladder.

If every prime factor of `b` is below `q_s` and no stored `p_i^q_s` macro
divides `b`, then:

* every prime exponent is at most `q_s-1`;
* at most `s` different prime directions occur.

Hence the total prime-token count is at most `s*(q_s-1)`. -/
theorem primeFactorCount_le_budget_mul_stableBase_pred_of_no_coarseMacro
    {N s b : ℕ}
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N)
    (hSmallPrime : ∀ p : ℕ, p.Prime → p ∣ b →
      p < rootQuotientStablePrimeBase s)
    (hNoMacro : ∀ g : ℕ,
      g ∈ RootQuotientCoarseStableMacroSet N s → ¬g ∣ b) :
    rootQuotientPrimeFactorCount b ≤
      s * (rootQuotientStablePrimeBase s - 1) := by
  classical
  let q := rootQuotientStablePrimeBase s
  have hbZero : b ≠ 0 := by omega
  have hPrimeData : ∀ p : ℕ, p ∈ b.factorization.support →
      p.Prime ∧ p ∣ b ∧ p < q := by
    intro p hpSupport
    have hpNe : b.factorization p ≠ 0 :=
      Finsupp.mem_support_iff.mp hpSupport
    have hpPrime : p.Prime := by
      by_contra hpNot
      exact hpNe (Nat.factorization_eq_zero_of_not_prime b hpNot)
    have hpDvd : p ∣ b := by
      by_contra hpNotDvd
      exact hpNe (Nat.factorization_eq_zero_of_not_dvd hpNotDvd)
    exact ⟨hpPrime, hpDvd, hSmallPrime p hpPrime hpDvd⟩
  have hExpLt : ∀ p : ℕ, p ∈ b.factorization.support → b.factorization p < q := by
    intro p hpSupport
    have hpData := hPrimeData p hpSupport
    by_contra hNot
    have hqLeExp : q ≤ b.factorization p := by omega
    have hpPowDvd : p ^ q ∣ b :=
      (hpData.1.pow_dvd_iff_le_factorization hbZero).2 hqLeExp
    have hpPowLeB : p ^ q ≤ b :=
      Nat.le_of_dvd (by omega) hpPowDvd
    obtain ⟨i, hiLt, hiEq⟩ :=
      exists_primeIndex_lt_budget_of_prime_lt_stableBase
        hpData.1 hpData.2.2
    have hMacroMem : p ^ q ∈ RootQuotientCoarseStableMacroSet N s := by
      apply (mem_rootQuotientCoarseStableMacroSet_iff).2
      refine ⟨hpPowLeB.trans hbN, i, hiLt, ?_⟩
      rw [hiEq]
      simp [q]
    exact hNoMacro (p ^ q) hMacroMem hpPowDvd
  let primeDirections : Finset ℕ :=
    (Finset.range s).image (Nat.nth Nat.Prime)
  have hSupportSubset : b.factorization.support ⊆ primeDirections := by
    intro p hpSupport
    have hpData := hPrimeData p hpSupport
    obtain ⟨i, hiLt, hiEq⟩ :=
      exists_primeIndex_lt_budget_of_prime_lt_stableBase
        hpData.1 hpData.2.2
    dsimp [primeDirections]
    apply Finset.mem_image.2
    exact ⟨i, by simpa using hiLt, hiEq⟩
  have hSupportCard : b.factorization.support.card ≤ s := by
    calc
      b.factorization.support.card ≤ primeDirections.card :=
        Finset.card_le_card hSupportSubset
      _ ≤ (Finset.range s).card := by
        dsimp [primeDirections]
        exact Finset.card_image_le
      _ = s := by simp
  have hSum :
      (∑ p ∈ b.factorization.support, b.factorization p) ≤
        s * (q - 1) := by
    calc
      (∑ p ∈ b.factorization.support, b.factorization p) ≤
          ∑ _p ∈ b.factorization.support, (q - 1) := by
        exact Finset.sum_le_sum fun p hp => by
          have := hExpLt p hp
          omega
      _ = b.factorization.support.card * (q - 1) := by simp
      _ ≤ s * (q - 1) := Nat.mul_le_mul_right (q - 1) hSupportCard
  rw [rootQuotientPrimeFactorCount_eq_factorization_sum]
  simpa [Finsupp.sum, q] using hSum

/-- The coarse canonical family actually satisfies a sharper stable-code
constant `s*(q_s-1)`, obtained by counting the number of possible residual
prime directions rather than bounding them by `q_s`. -/
theorem coarseStableMacroSet_is_countedStableMacroCode
    {N s : ℕ} :
    RootQuotientStableMacroCode
      N
      (rootQuotientStablePrimeBase s)
      (s * (rootQuotientStablePrimeBase s - 1))
      (RootQuotientCoarseStableMacroSet N s) := by
  refine ⟨rootQuotientStablePrimeBase_prime s, ?_, ?_⟩
  · intro g hg
    exact stablePrimeBase_le_of_mem_coarseStableMacroSet hg
  · intro b hbPos hbN hSmallPrime hNoMacro
    exact primeFactorCount_le_budget_mul_stableBase_pred_of_no_coarseMacro
      hbPos hbN hSmallPrime hNoMacro

/-- Counted coarse stable horizon with additive gap `s*(q_s-1)`. -/
def rootQuotientCountedStableMacroHorizon
    (N s : ℕ) : ℕ :=
  s * (rootQuotientStablePrimeBase s - 1) +
    Nat.log (rootQuotientStablePrimeBase s) N

/-- The same explicit `s`-macro family separates by the sharper counted stable
horizon.  This action-level statement also covers trivial domains where the
shortest semantic radius may be zero. -/
theorem coarseStableMacroSet_separates_within_countedStableHorizon
    {r N s : ℕ}
    (hr : 1 ≤ r) :
    SeparatesRootQuotientWordsUpTo
      r N (rootQuotientCountedStableMacroHorizon N s)
      (RootQuotientPrimeBasis N ∪ RootQuotientCoarseStableMacroSet N s) := by
  simpa [rootQuotientCountedStableMacroHorizon] using
    stableMacroCode_separates_within_add_log_stateBound
      (r := r)
      (hCode := coarseStableMacroSet_is_countedStableMacroCode
        (N := N) (s := s))

/-- The true minimum macro count fits the requested budget at the sharper
counted horizon. -/
theorem minimumCompositeMacroCount_countedStableHorizon_le_budget
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumCompositeMacroCount
        r N (rootQuotientCountedStableMacroHorizon N s) ≤ s := by
  let S := RootQuotientCoarseStableMacroSet N s
  have hPresentation : RootQuotientCompositeMacroPresentation
      r N (rootQuotientCountedStableMacroHorizon N s) S := by
    refine ⟨
      rootQuotientCoarseStableMacroSet_finite N s,
      coarseStableMacroSet_is_compositeMacroFamily hr hBinary,
      ?_⟩
    exact coarseStableMacroSet_separates_within_countedStableHorizon
      (r := r) (N := N) (s := s) (by omega)
  exact (rootQuotientMinimumCompositeMacroCount_le hPresentation).trans
    (rootQuotientCoarseStableMacroSet_ncard_le N s)

/-- Sharper upper bound on optimal positive depth under `s` optional macros.
The assumption `N>=2` aligns the action-level radius with the Pareto object's
convention that optimization ranges over positive horizons. -/
theorem minimumHorizonAtCompositeMacroBudget_le_countedStableHorizon
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ≤
      rootQuotientCountedStableMacroHorizon N s := by
  let H := rootQuotientCountedStableMacroHorizon N s
  have hqPrime := rootQuotientStablePrimeBase_prime s
  have hHPos : 1 ≤ H := by
    by_cases hsZero : s = 0
    · subst s
      have hLogPos : 0 < Nat.log 2 N :=
        Nat.log_pos (by omega) hN
      simpa [H, rootQuotientCountedStableMacroHorizon,
        rootQuotientStablePrimeBase] using hLogPos
    · have hsPos : 1 ≤ s := by omega
      have hPredPos : 1 ≤ rootQuotientStablePrimeBase s - 1 := by
        have := hqPrime.two_le
        omega
      have hProdPos : 1 ≤ s * (rootQuotientStablePrimeBase s - 1) :=
        Nat.one_le_mul hsPos hPredPos
      dsimp [H, rootQuotientCountedStableMacroHorizon]
      omega
  have hMuLe : rootQuotientMinimumCompositeMacroCount r N H ≤ s := by
    dsimp [H]
    exact minimumCompositeMacroCount_countedStableHorizon_le_budget
      (r := r) (N := N) (s := s) hr hBinary
  have hStorage :
      rootQuotientMinimumStorageSize r N H ≤
        (RootQuotientPrimeBasis N).ncard + s := by
    rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
      hr hHPos]
    exact Nat.add_le_add_left hMuLe _
  have hPrimeBudget :
      (RootQuotientPrimeBasis N).ncard ≤
        (RootQuotientPrimeBasis N).ncard + s :=
    Nat.le_add_right _ _
  have hDepth :=
    (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
      (r := r) (N := N)
      (s := (RootQuotientPrimeBasis N).ncard + s) (h := H)
      hr hPrimeBudget hHPos).2 hStorage
  simpa [rootQuotientMinimumHorizonAtCompositeMacroBudget, H] using hDepth

/-- Sharpened next-prime stable resource sandwich.

For `N>=2`, the optimal positive horizon under `s` optional macro types differs
from the universal next-prime logarithmic lower bound by at most the
state-independent additive constant `s*(q_s-1)`. -/
theorem nextPrime_log_macroBudget_counted_sandwich
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    Nat.log (rootQuotientStablePrimeBase s) N ≤
        rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ∧
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ≤
        rootQuotientCountedStableMacroHorizon N s := by
  have hLower := nextPrime_log_macroBudget_sandwich
    (r := r) (N := N) (s := s) hr (by omega) hBinary
  exact ⟨hLower.1,
    minimumHorizonAtCompositeMacroBudget_le_countedStableHorizon
      (r := r) (N := N) (s := s) hr hN hBinary⟩

/-- Additive-gap form of the counted sandwich. -/
theorem minimumHorizonAtCompositeMacroBudget_sub_nextPrimeLog_le
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N s -
        Nat.log (rootQuotientStablePrimeBase s) N ≤
      s * (rootQuotientStablePrimeBase s - 1) := by
  have hSandwich := nextPrime_log_macroBudget_counted_sandwich
    (r := r) (N := N) (s := s) hr hN hBinary
  dsimp [rootQuotientCountedStableMacroHorizon] at hSandwich
  omega

end EnterpriseMath.Quotient
