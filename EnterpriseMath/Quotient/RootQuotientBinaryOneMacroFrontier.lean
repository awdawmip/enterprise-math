import EnterpriseMath.Quotient.RootQuotientMacroPareto
import EnterpriseMath.Quotient.RootQuotientSingleMacroOptimality
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- In the nontrivial binary/high-root regime, the exact prime-plus-four
horizon is positive. -/
theorem rootQuotientPrimeFourHorizon_pos
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    1 ≤ rootQuotientPrimeFourHorizon N := by
  rw [rootQuotientPrimeFourHorizon_eq hN]
  omega

/-- If the prime-only binary horizon is at least three, the exact one-macro
horizon is at least two. -/
theorem two_le_rootQuotientPrimeFourHorizon_of_three_le_primeHorizon
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N) :
    2 ≤ rootQuotientPrimeFourHorizon N := by
  have hLog : rootQuotientPrimeHorizon r N = Nat.log 2 N :=
    rootQuotientPrimeHorizon_eq_nat_log_two_of_stateBound_lt_two_pow_rootOrder
      hr (by omega) hBinary
  have hLogThree : 3 ≤ Nat.log 2 N := by
    rw [← hLog]
    exact hLThree
  have hNZero : N ≠ 0 := by omega
  have hEightLe : 2 ^ 3 ≤ N :=
    Nat.pow_le_of_le_log hNZero hLogThree
  have hThreeLeDiv : 3 ^ 1 ≤ N / 2 := by
    norm_num at hEightLe ⊢
    omega
  have hLogThreeDiv : 1 ≤ Nat.log 3 (N / 2) :=
    Nat.le_log_of_pow_le (by omega) hThreeLeDiv
  rw [rootQuotientPrimeFourHorizon_eq hN]
  omega

/-- Macro `4` reaches its exact high-root horizon no later than the
penultimate prime horizon. -/
theorem rootQuotientPrimeFourHorizon_le_penultimatePrimeHorizon
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientPrimeFourHorizon N ≤
      rootQuotientPrimeHorizon r N - 1 := by
  have hSep := prime_union_four_separates_penultimate_in_binary_regime
    hr hN hBinary hLThree
  exact rootQuotientPrimeFourHorizon_minimal hr hN hBinary hSep

/-- The singleton family `{4}` is a valid optional composite-macro
presentation at the exact prime-plus-four horizon. -/
theorem four_singleton_is_compositeMacroPresentation_at_primeFourHorizon
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N) :
    RootQuotientCompositeMacroPresentation
      r N (rootQuotientPrimeFourHorizon N) ({4} : Set ℕ) := by
  have hCommon :=
    four_is_common_maximal_semiprime_divisor_in_binary_regime
      hr (by omega) hBinary hLThree
  have hFourSemantic := hCommon.1
  have hFourNotPrime : 4 ∉ RootQuotientPrimeBasis N := by
    intro hPrime
    norm_num at hPrime
  refine ⟨Set.finite_singleton 4, ?_, ?_⟩
  · intro g hg
    have hEq : g = 4 := by simpa using hg
    subst g
    exact ⟨hFourSemantic, hFourNotPrime⟩
  · exact primeFourBasis_separates_at_exact_horizon hr hN hBinary

/-- Exact optional-macro count at the one-macro optimum: one composite macro
is sufficient and, because the horizon is still below the prime-only horizon,
necessary. -/
theorem rootQuotientMinimumCompositeMacroCount_primeFourHorizon_eq_one
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumCompositeMacroCount
      r N (rootQuotientPrimeFourHorizon N) = 1 := by
  have hPresentation :=
    four_singleton_is_compositeMacroPresentation_at_primeFourHorizon
      hr hN hBinary hLThree
  have hUpper :
      rootQuotientMinimumCompositeMacroCount
        r N (rootQuotientPrimeFourHorizon N) ≤ 1 := by
    have hLe := rootQuotientMinimumCompositeMacroCount_le hPresentation
    simpa using hLe
  have hHPos := rootQuotientPrimeFourHorizon_pos hr hN hBinary
  have hHLePen :=
    rootQuotientPrimeFourHorizon_le_penultimatePrimeHorizon
      hr hN hBinary hLThree
  have hHLt : rootQuotientPrimeFourHorizon N <
      rootQuotientPrimeHorizon r N := by omega
  have hLower :=
    rootQuotientMinimumCompositeMacroCount_pos_of_belowPrimeHorizon
      hr hHPos hHLt
  omega

/-- The whole interval from the exact prime-plus-four horizon up to but not
including the prime-only horizon is a one-macro plateau. -/
theorem rootQuotientMinimumCompositeMacroCount_eq_one_of_primeFourHorizon_le_of_lt_primeHorizon
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N)
    (hHLe : rootQuotientPrimeFourHorizon N ≤ h)
    (hLtL : h < rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumCompositeMacroCount r N h = 1 := by
  have hHPos := rootQuotientPrimeFourHorizon_pos hr hN hBinary
  have hUpper :=
    rootQuotientMinimumCompositeMacroCount_anti_horizon
      (r := r) (N := N)
      (h := rootQuotientPrimeFourHorizon N) (j := h)
      hr hHPos hHLe
  rw [rootQuotientMinimumCompositeMacroCount_primeFourHorizon_eq_one
    hr hN hBinary hLThree] at hUpper
  have hh : 1 ≤ h := hHPos.trans hHLe
  have hLower :=
    rootQuotientMinimumCompositeMacroCount_pos_of_belowPrimeHorizon
      hr hh hLtL
  omega

/-- Below the exact one-macro optimum, every separating presentation needs at
least two optional composite macro types. -/
theorem two_le_rootQuotientMinimumCompositeMacroCount_of_lt_primeFourHorizon
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N)
    (hh : 1 ≤ h)
    (hLtH : h < rootQuotientPrimeFourHorizon N) :
    2 ≤ rootQuotientMinimumCompositeMacroCount r N h := by
  have hHLePen :=
    rootQuotientPrimeFourHorizon_le_penultimatePrimeHorizon
      hr hN hBinary hLThree
  have hLtL : h < rootQuotientPrimeHorizon r N := by omega
  have hAtLeastOne :=
    rootQuotientMinimumCompositeMacroCount_pos_of_belowPrimeHorizon
      hr hh hLtL
  by_contra hNot
  have hMuOne : rootQuotientMinimumCompositeMacroCount r N h = 1 := by
    omega
  obtain ⟨S, hS, hSCard⟩ :=
    exists_rootQuotientMinimumCompositeMacroPresentation hr hh
  have hSOne : S.ncard = 1 := by
    rw [hSCard, hMuOne]
  obtain ⟨g, hSEq⟩ := (Set.ncard_eq_one).1 hSOne
  have hgS : g ∈ S := by
    rw [hSEq]
    simp
  have hgFamily := hS.2.1 hgS
  have hgSemantic := hgFamily.1
  have hgNotPrimeBasis := hgFamily.2
  have hCountPos : 0 < rootQuotientPrimeFactorCount g :=
    rootQuotientPrimeFactorCount_pos_of_two_le hgSemantic.1
  have hCountNotOne : rootQuotientPrimeFactorCount g ≠ 1 := by
    intro hOne
    have hgPrime : g.Prime :=
      (rootQuotientPrimeFactorCount_eq_one_iff_prime hgSemantic.1).1 hOne
    exact hgNotPrimeBasis ⟨hgPrime, hgSemantic.2.1⟩
  have hgRank : 2 ≤ rootQuotientPrimeFactorCount g := by omega
  have hSepSingle : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeSingleMacroBasis N g) := by
    have hSep := hS.2.2
    rw [hSEq] at hSep
    simpa [RootQuotientPrimeSingleMacroBasis] using hSep
  have hOptimal :=
    primeFourHorizon_le_of_single_composite_macro_separates
      hr hN hBinary hLThree hgSemantic hgRank hSepSingle
  exact (not_le_of_gt hLtH) hOptimal

/-- Exact one-macro storage window in the binary/high-root regime. -/
theorem rootQuotientMinimumCompositeMacroCount_eq_one_iff_primeFour_window
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N)
    (hh : 1 ≤ h) :
    rootQuotientMinimumCompositeMacroCount r N h = 1 ↔
      rootQuotientPrimeFourHorizon N ≤ h ∧
      h < rootQuotientPrimeHorizon r N := by
  constructor
  · intro hMuOne
    have hLtL : h < rootQuotientPrimeHorizon r N := by
      by_contra hNot
      have hLLe : rootQuotientPrimeHorizon r N ≤ h := by omega
      have hZero :=
        rootQuotientMinimumCompositeMacroCount_eq_zero_of_horizon_le
          hr hh hLLe
      rw [hMuOne] at hZero
      omega
    have hHLe : rootQuotientPrimeFourHorizon N ≤ h := by
      by_contra hNot
      have hLtH : h < rootQuotientPrimeFourHorizon N := by omega
      have hTwo :=
        two_le_rootQuotientMinimumCompositeMacroCount_of_lt_primeFourHorizon
          hr hN hBinary hLThree hh hLtH
      rw [hMuOne] at hTwo
      omega
    exact ⟨hHLe, hLtL⟩
  · rintro ⟨hHLe, hLtL⟩
    exact
      rootQuotientMinimumCompositeMacroCount_eq_one_of_primeFourHorizon_le_of_lt_primeHorizon
        hr hN hBinary hLThree hHLe hLtL

/-- One optional composite macro has exact optimal execution depth equal to the
prime-plus-four horizon. -/
theorem rootQuotientMinimumHorizonAtCompositeMacroBudget_one_eq_primeFourHorizon
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumHorizonAtCompositeMacroBudget r N 1 =
      rootQuotientPrimeFourHorizon N := by
  have hHTwo :=
    two_le_rootQuotientPrimeFourHorizon_of_three_le_primeHorizon
      hr hN hBinary hLThree
  apply (rootQuotientMinimumHorizonAtCompositeMacroBudget_eq_iff_interval
    (r := r) (N := N) (m := 1)
    (h := rootQuotientPrimeFourHorizon N) hr hHTwo).2
  constructor
  · rw [rootQuotientMinimumCompositeMacroCount_primeFourHorizon_eq_one
      hr hN hBinary hLThree]
  · have hPredPos : 1 ≤ rootQuotientPrimeFourHorizon N - 1 := by omega
    have hPredLt : rootQuotientPrimeFourHorizon N - 1 <
        rootQuotientPrimeFourHorizon N := by omega
    have hTwo :=
      two_le_rootQuotientMinimumCompositeMacroCount_of_lt_primeFourHorizon
        hr hN hBinary hLThree hPredPos hPredLt
    omega

/-- Every strict interior point of the one-macro plateau is Pareto-inactive:
there is no optional-macro budget whose optimal execution horizon is `h`. -/
theorem no_macroBudget_has_minimumHorizon_in_binary_oneMacro_plateau_interior
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N)
    (hHLt : rootQuotientPrimeFourHorizon N < h)
    (hLtL : h < rootQuotientPrimeHorizon r N) :
    ¬∃ m : ℕ,
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N m = h := by
  have hHTwo :=
    two_le_rootQuotientPrimeFourHorizon_of_three_le_primeHorizon
      hr hN hBinary hLThree
  have hh : 2 ≤ h := by omega
  have hPred : rootQuotientPrimeFourHorizon N ≤ h - 1 := by omega
  have hPredLtL : h - 1 < rootQuotientPrimeHorizon r N := by omega
  have hMuH :=
    rootQuotientMinimumCompositeMacroCount_eq_one_of_primeFourHorizon_le_of_lt_primeHorizon
      hr hN hBinary hLThree (by omega) hLtL
  have hMuPred :=
    rootQuotientMinimumCompositeMacroCount_eq_one_of_primeFourHorizon_le_of_lt_primeHorizon
      hr hN hBinary hLThree hPred hPredLtL
  apply no_macroBudget_has_minimumHorizon_of_macro_plateau hr hh
  rw [hMuH, hMuPred]

/-- The penultimate prime horizon is Pareto-active in the binary/high-root
regime exactly when it coincides with the exact one-macro horizon.

If `H4<L-1`, the whole interval `(H4,L)` is a one-macro plateau, so the
penultimate point is dominated. -/
theorem binary_penultimate_pareto_active_iff_primeFourHorizon_eq_penultimate
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N) :
    (∃ m : ℕ,
      rootQuotientMinimumHorizonAtCompositeMacroBudget r N m =
        rootQuotientPrimeHorizon r N - 1) ↔
      rootQuotientPrimeFourHorizon N =
        rootQuotientPrimeHorizon r N - 1 := by
  let L := rootQuotientPrimeHorizon r N
  let H := rootQuotientPrimeFourHorizon N
  have hHLe : H ≤ L - 1 := by
    dsimp [H, L]
    exact rootQuotientPrimeFourHorizon_le_penultimatePrimeHorizon
      hr hN hBinary hLThree
  constructor
  · intro hActive
    by_contra hNe
    have hHLt : H < L - 1 := by omega
    have hInactive :=
      no_macroBudget_has_minimumHorizon_in_binary_oneMacro_plateau_interior
        (r := r) (N := N) (h := L - 1)
        hr hN hBinary hLThree hHLt (by omega)
    exact hInactive (by simpa [L] using hActive)
  · intro hEq
    refine ⟨1, ?_⟩
    have hOne :=
      rootQuotientMinimumHorizonAtCompositeMacroBudget_one_eq_primeFourHorizon
        hr hN hBinary hLThree
    dsimp [H, L] at hEq ⊢
    rw [hOne, hEq]

end EnterpriseMath.Quotient
