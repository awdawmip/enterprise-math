import EnterpriseMath.Quotient.RootQuotientClogStableMacroLadder
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Nat.Prime.Nth
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The first `s` prime directions, represented by their prime values. -/
noncomputable def rootQuotientStablePrimeDirectionFinset
    (s : ℕ) : Finset ℕ := by
  classical
  exact (Finset.range s).image (Nat.nth Nat.Prime)

/-- Sharp residual-slot count for the next-prime minimal-power ladder.

For each prime direction `p_i<q_s`, the stored macro is
`p_i^(clog_{p_i} q_s)`.  After maximal block packing there can remain at most
`clog_{p_i}(q_s)-1` literal `p_i` tokens.  Summing these coordinate-wise caps
gives the exact finite residual constant predicted by the executable ladder. -/
noncomputable def rootQuotientSharpStableResidualBudget
    (s : ℕ) : ℕ :=
  ∑ p in rootQuotientStablePrimeDirectionFinset s,
    Nat.clog p (rootQuotientStablePrimeBase s) - 1

/-- Every prime support coordinate below the stable base occurs in the finite
stable-direction set. -/
theorem factorization_support_subset_stablePrimeDirections
    {s b : ℕ}
    (hbZero : b ≠ 0)
    (hSmallPrime : ∀ p : ℕ, p.Prime → p ∣ b →
      p < rootQuotientStablePrimeBase s) :
    b.factorization.support ⊆ rootQuotientStablePrimeDirectionFinset s := by
  classical
  intro p hpSupport
  have hpNe : b.factorization p ≠ 0 :=
    Finsupp.mem_support_iff.mp hpSupport
  have hpPrime : p.Prime := by
    by_contra hpNot
    exact hpNe (Nat.factorization_eq_zero_of_not_prime b hpNot)
  have hpDvd : p ∣ b := by
    by_contra hpNotDvd
    exact hpNe (Nat.factorization_eq_zero_of_not_dvd hpNotDvd)
  obtain ⟨i, hiLt, hiEq⟩ :=
    exists_primeIndex_lt_budget_of_prime_lt_stableBase
      hpPrime (hSmallPrime p hpPrime hpDvd)
  dsimp [rootQuotientStablePrimeDirectionFinset]
  exact Finset.mem_image.2 ⟨i, by simpa using hiLt, hiEq⟩

/-- Exact coordinate-wise residual exponent cap for the minimal-power ladder. -/
theorem factorization_lt_stableMacroExponent_of_no_clogMacro
    {N s b p : ℕ}
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N)
    (hpSupport : p ∈ b.factorization.support)
    (hSmallPrime : ∀ q : ℕ, q.Prime → q ∣ b →
      q < rootQuotientStablePrimeBase s)
    (hNoMacro : ∀ g : ℕ,
      g ∈ RootQuotientClogStableMacroSet N s → ¬g ∣ b) :
    b.factorization p <
      Nat.clog p (rootQuotientStablePrimeBase s) := by
  classical
  let q := rootQuotientStablePrimeBase s
  let e := Nat.clog p q
  have hbZero : b ≠ 0 := by omega
  have hpNe : b.factorization p ≠ 0 :=
    Finsupp.mem_support_iff.mp hpSupport
  have hpPrime : p.Prime := by
    by_contra hpNot
    exact hpNe (Nat.factorization_eq_zero_of_not_prime b hpNot)
  have hpDvd : p ∣ b := by
    by_contra hpNotDvd
    exact hpNe (Nat.factorization_eq_zero_of_not_dvd hpNotDvd)
  have hpLtQ : p < q := hSmallPrime p hpPrime hpDvd
  obtain ⟨i, hiLt, hiEq⟩ :=
    exists_primeIndex_lt_budget_of_prime_lt_stableBase hpPrime hpLtQ
  by_contra hNot
  have heLe : e ≤ b.factorization p := by omega
  have hpPowDvd : p ^ e ∣ b :=
    (hpPrime.pow_dvd_iff_le_factorization hbZero).2 heLe
  have hpPowLeB : p ^ e ≤ b :=
    Nat.le_of_dvd (by omega) hpPowDvd
  have hMacroEq : p ^ e = rootQuotientStablePrimePowerMacro s i := by
    rw [hiEq]
    simp [e, q, rootQuotientStablePrimePowerMacro,
      rootQuotientStableMacroExponent]
  have hMacroMem : p ^ e ∈ RootQuotientClogStableMacroSet N s := by
    apply (mem_rootQuotientClogStableMacroSet_iff).2
    exact ⟨hpPowLeB.trans hbN, i, hiLt, hMacroEq⟩
  exact hNoMacro (p ^ e) hMacroMem hpPowDvd

/-- Exact sharp residual-token theorem for the minimal-power next-prime ladder. -/
theorem primeFactorCount_le_sharpStableResidualBudget_of_no_macro
    {N s b : ℕ}
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N)
    (hSmallPrime : ∀ p : ℕ, p.Prime → p ∣ b →
      p < rootQuotientStablePrimeBase s)
    (hNoMacro : ∀ g : ℕ,
      g ∈ RootQuotientClogStableMacroSet N s → ¬g ∣ b) :
    rootQuotientPrimeFactorCount b ≤
      rootQuotientSharpStableResidualBudget s := by
  classical
  let q := rootQuotientStablePrimeBase s
  have hbZero : b ≠ 0 := by omega
  have hSupportSubset :
      b.factorization.support ⊆ rootQuotientStablePrimeDirectionFinset s :=
    factorization_support_subset_stablePrimeDirections hbZero hSmallPrime
  have hCoord :
      (∑ p in b.factorization.support, b.factorization p) ≤
        ∑ p in b.factorization.support, (Nat.clog p q - 1) := by
    exact Finset.sum_le_sum fun p hp => by
      have hLt := factorization_lt_stableMacroExponent_of_no_clogMacro
        hbPos hbN hp hSmallPrime hNoMacro
      dsimp [q] at hLt ⊢
      omega
  have hExtend :
      (∑ p in b.factorization.support, (Nat.clog p q - 1)) ≤
        ∑ p in rootQuotientStablePrimeDirectionFinset s,
          (Nat.clog p q - 1) := by
    exact Finset.sum_le_sum_of_subset_of_nonneg
      hSupportSubset (fun p _hpAll _hpNot => Nat.zero_le _)
  rw [rootQuotientPrimeFactorCount_eq_factorization_sum]
  simpa [Finsupp.sum, rootQuotientSharpStableResidualBudget, q] using
    hCoord.trans hExtend

/-- The minimal-power ladder is a stable macro code with the exact residual-slot
constant `T_s`. -/
theorem clogStableMacroSet_is_sharpStableMacroCode
    {N s : ℕ} :
    RootQuotientStableMacroCode
      N
      (rootQuotientStablePrimeBase s)
      (rootQuotientSharpStableResidualBudget s)
      (RootQuotientClogStableMacroSet N s) := by
  refine ⟨rootQuotientStablePrimeBase_prime s, ?_, ?_⟩
  · intro g hg
    obtain ⟨_hgN, i, _hi, rfl⟩ :=
      (mem_rootQuotientClogStableMacroSet_iff).1 hg
    exact stablePrimeBase_le_stablePrimePowerMacro
  · intro b hbPos hbN hSmallPrime hNoMacro
    exact primeFactorCount_le_sharpStableResidualBudget_of_no_macro
      hbPos hbN hSmallPrime hNoMacro

/-- Sharp next-prime ladder horizon using the exact coordinate residual sum. -/
def rootQuotientSharpStableMacroHorizon
    (N s : ℕ) : ℕ :=
  rootQuotientSharpStableResidualBudget s +
    Nat.log (rootQuotientStablePrimeBase s) N

/-- The minimal-power ladder separates by the sharp residual-sum horizon. -/
theorem clogStableMacroSet_separates_within_sharpStableHorizon
    {r N s : ℕ}
    (hr : 1 ≤ r) :
    SeparatesRootQuotientWordsUpTo
      r N (rootQuotientSharpStableMacroHorizon N s)
      (RootQuotientPrimeBasis N ∪ RootQuotientClogStableMacroSet N s) := by
  simpa [rootQuotientSharpStableMacroHorizon] using
    stableMacroCode_separates_within_add_log_stateBound
      (r := r)
      (hCode := clogStableMacroSet_is_sharpStableMacroCode
        (N := N) (s := s))

/-- The sharp residual budget is positive for every nonzero macro budget. -/
theorem rootQuotientSharpStableResidualBudget_pos_of_budget_pos
    {s : ℕ}
    (hs : 1 ≤ s) :
    1 ≤ rootQuotientSharpStableResidualBudget s := by
  classical
  let q := rootQuotientStablePrimeBase s
  have hTwoMem : 2 ∈ rootQuotientStablePrimeDirectionFinset s := by
    dsimp [rootQuotientStablePrimeDirectionFinset]
    apply Finset.mem_image.2
    exact ⟨0, by simpa using hs, by simp⟩
  have hSingletonSubset : ({2} : Finset ℕ) ⊆
      rootQuotientStablePrimeDirectionFinset s := by
    intro p hp
    have hpEq : p = 2 := by simpa using hp
    simpa [hpEq] using hTwoMem
  have hQGtTwo : 2 < q := by
    have hNth : Nat.nth Nat.Prime 0 < Nat.nth Nat.Prime s :=
      (Nat.nth_lt_nth Nat.infinite_setOfPred_prime).2 (by omega)
    simpa [q, rootQuotientStablePrimeBase] using hNth
  have hClog : 1 < Nat.clog 2 q :=
    (Nat.lt_clog_iff_pow_lt Nat.one_lt_two).2 (by simpa using hQGtTwo)
  have hTermPos : 1 ≤ Nat.clog 2 q - 1 := by omega
  have hTermLe : Nat.clog 2 q - 1 ≤
      rootQuotientSharpStableResidualBudget s := by
    calc
      Nat.clog 2 q - 1 =
          ∑ p in ({2} : Finset ℕ), (Nat.clog p q - 1) := by simp
      _ ≤ ∑ p in rootQuotientStablePrimeDirectionFinset s,
          (Nat.clog p q - 1) := by
        exact Finset.sum_le_sum_of_subset_of_nonneg
          hSingletonSubset (fun p _hpAll _hpNot => Nat.zero_le _)
      _ = rootQuotientSharpStableResidualBudget s := by
        simp [rootQuotientSharpStableResidualBudget, q]
  exact hTermPos.trans hTermLe

/-- Sharp minimal-power ladder upper bound on the true macro-budget Pareto
horizon. -/
theorem minimumHorizonAtCompositeMacroBudget_le_sharpStableHorizon
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ≤
      rootQuotientSharpStableMacroHorizon N s := by
  let H := rootQuotientSharpStableMacroHorizon N s
  let S := RootQuotientClogStableMacroSet N s
  have hPresentation : RootQuotientCompositeMacroPresentation r N H S := by
    refine ⟨
      rootQuotientClogStableMacroSet_finite N s,
      clogStableMacroSet_is_compositeMacroFamily hr hBinary,
      ?_⟩
    dsimp [H, S]
    exact clogStableMacroSet_separates_within_sharpStableHorizon
      (r := r) (N := N) (s := s) (by omega)
  have hMuLe : rootQuotientMinimumCompositeMacroCount r N H ≤ s :=
    (rootQuotientMinimumCompositeMacroCount_le hPresentation).trans
      (rootQuotientClogStableMacroSet_ncard_le N s)
  have hHPos : 1 ≤ H := by
    by_cases hsZero : s = 0
    · subst s
      have hLogPos : 0 < Nat.log 2 N := Nat.log_pos (by omega) hN
      simpa [H, rootQuotientSharpStableMacroHorizon,
        rootQuotientSharpStableResidualBudget,
        rootQuotientStablePrimeDirectionFinset,
        rootQuotientStablePrimeBase] using hLogPos
    · have hResidualPos : 1 ≤ rootQuotientSharpStableResidualBudget s :=
        rootQuotientSharpStableResidualBudget_pos_of_budget_pos (by omega)
      dsimp [H, rootQuotientSharpStableMacroHorizon]
      omega
  have hStorage :
      rootQuotientMinimumStorageSize r N H ≤
        (RootQuotientPrimeBasis N).ncard + s := by
    rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
      hr hHPos]
    exact Nat.add_le_add_left hMuLe _
  have hPrimeBudget :
      (RootQuotientPrimeBasis N).ncard ≤
        (RootQuotientPrimeBasis N).ncard + s := Nat.le_add_right _ _
  have hDepth :=
    (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
      (r := r) (N := N)
      (s := (RootQuotientPrimeBasis N).ncard + s) (h := H)
      hr hPrimeBudget hHPos).2 hStorage
  simpa [rootQuotientMinimumHorizonAtCompositeMacroBudget, H] using hDepth

/-- **Sharp finite next-prime stable macro-budget sandwich.**

For `N>=2` in the high-root regime, the optimal positive execution horizon
under `s` optional macro types lies between the information-theoretic
next-prime lower bound and the explicit minimal-power ladder with exact residual
constant `T_s`.

`log_{q_s} N <= D_macro(s) <= T_s + log_{q_s} N`. -/
theorem nextPrime_log_macroBudget_sharp_sandwich
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    Nat.log (rootQuotientStablePrimeBase s) N ≤
        rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ∧
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N s ≤
        rootQuotientSharpStableMacroHorizon N s := by
  have hLower := nextPrime_log_macroBudget_sandwich
    (r := r) (N := N) (s := s) hr (by omega) hBinary
  exact ⟨hLower.1,
    minimumHorizonAtCompositeMacroBudget_le_sharpStableHorizon
      (r := r) (N := N) (s := s) hr hN hBinary⟩

/-- Exact residual-gap form of the sharp next-prime stable law. -/
theorem minimumHorizon_sub_nextPrimeLog_le_sharpResidualBudget
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N s -
        Nat.log (rootQuotientStablePrimeBase s) N ≤
      rootQuotientSharpStableResidualBudget s := by
  have hSandwich := nextPrime_log_macroBudget_sharp_sandwich
    (r := r) (N := N) (s := s) hr hN hBinary
  dsimp [rootQuotientSharpStableMacroHorizon] at hSandwich
  omega

end EnterpriseMath.Quotient
