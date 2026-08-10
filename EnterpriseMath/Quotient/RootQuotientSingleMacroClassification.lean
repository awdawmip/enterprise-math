import EnterpriseMath.Quotient.RootQuotientPrimeTwoPowerClosedHorizon
import EnterpriseMath.Quotient.RootQuotientSingleMacroOptimality
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- In the high-root regime, the prime hard target `2^L` lies in the bounded
semantic specification. -/
theorem two_pow_primeHorizon_mem_semanticBasis_in_highRoot
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r) :
    2 ^ rootQuotientPrimeHorizon r N ∈
      RootQuotientNontrivialPowerFreeBasis r N := by
  have hLog : rootQuotientPrimeHorizon r N = Nat.log 2 N :=
    rootQuotientPrimeHorizon_eq_nat_log_two_of_stateBound_lt_two_pow_rootOrder
      hr (by omega) hBinary
  have hNZero : N ≠ 0 := by omega
  have hBound : 2 ^ rootQuotientPrimeHorizon r N ≤ N := by
    rw [hLog]
    exact Nat.pow_log_le_self 2 hNZero
  have hFree : RPowerFree r (2 ^ rootQuotientPrimeHorizon r N) :=
    rPowerFree_of_lt_two_pow_rootOrder (by positivity)
      (hBound.trans_lt hBinary)
  refine ⟨?_, hBound, hFree⟩
  have hLPos : 1 ≤ rootQuotientPrimeHorizon r N := by
    rw [hLog]
    apply Nat.le_log_of_pow_le (by omega)
    simpa using hN
  have hTwoPow : 2 ≤ 2 ^ rootQuotientPrimeHorizon r N := by
    calc
      2 = 2 ^ 1 := by simp
      _ ≤ 2 ^ rootQuotientPrimeHorizon r N :=
        Nat.pow_le_pow_right (by omega) hLPos
  exact hTwoPow

/-- If one added macro does not divide the prime hard target `2^L`, it cannot
improve the exact worst-case depth at all. -/
theorem primeSingleMacro_separates_iff_primeHorizon_le_of_not_dvd_two_pow_horizon
    {r N g h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hgPos : 1 ≤ g)
    (hgNotDvd : ¬g ∣ 2 ^ rootQuotientPrimeHorizon r N) :
    SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeSingleMacroBasis N g) ↔
      rootQuotientPrimeHorizon r N ≤ h := by
  let L := rootQuotientPrimeHorizon r N
  constructor
  · intro hSep
    have hTarget := two_pow_primeHorizon_mem_semanticBasis_in_highRoot
      hr hN hBinary
    have hBasisPos := rootQuotientPrimeSingleMacroBasis_positive hgPos
    have hReach :=
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeSingleMacroBasis N g)
        (by omega) hBasisPos).1 hSep
        (2 ^ L) (by positivity) hTarget.2.1 hTarget.2.2
    obtain ⟨w, hwLen, hwBasis, hProd⟩ := hReach
    have hwPrime : RootQuotientWordOver (RootQuotientPrimeBasis N) w :=
      wordOver_primeSingleMacro_of_macro_not_dvd_product
        hwBasis hProd (by simpa [L] using hgNotDvd)
    have hExact : w.length = rootQuotientPrimeFactorCount (2 ^ L) :=
      prime_word_length_eq_primeFactorCount hwPrime hProd.symm
    rw [rootQuotientPrimeFactorCount_two_pow] at hExact
    omega
  · intro hLLe
    have hPrimeSep : SeparatesRootQuotientWordsUpTo
        r N L (RootQuotientPrimeBasis N) :=
      rootQuotientPrimeBasis_separates_at_exact_horizon (by omega)
    have hPrimeCompile :=
      (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis
        (r := r) (N := N) (h := L)
        (G := RootQuotientPrimeBasis N)
        (by omega) rootQuotientPrimeBasis_positive).1 hPrimeSep
    have hSub : RootQuotientPrimeBasis N ⊆
        RootQuotientPrimeSingleMacroBasis N g := Set.subset_union_left
    have hSingleCompile : RootQuotientAlphabetCompilesWithin
        L (RootQuotientPrimeSingleMacroBasis N g)
          (RootQuotientNontrivialPowerFreeBasis r N) :=
      rootQuotientAlphabetCompilesWithin_mono_implementation hSub hPrimeCompile
    have hSingleSepL : SeparatesRootQuotientWordsUpTo
        r N L (RootQuotientPrimeSingleMacroBasis N g) :=
      (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis
        (r := r) (N := N) (h := L)
        (G := RootQuotientPrimeSingleMacroBasis N g)
        (by omega) (rootQuotientPrimeSingleMacroBasis_positive hgPos)).2
        hSingleCompile
    exact separatesRootQuotientWordsUpTo_mono_horizon hLLe hSingleSepL

/-- Any positive macro dividing the hard target is necessarily a power of two. -/
theorem exists_twoPower_eq_of_dvd_primeHardTarget
    {r N g : ℕ}
    (hgPos : 1 ≤ g)
    (hgDvd : g ∣ 2 ^ rootQuotientPrimeHorizon r N) :
    ∃ m : ℕ, g = 2 ^ m := by
  exact ⟨g.factorization 2,
    eq_two_pow_factorization_two_of_dvd_two_pow hgPos hgDvd⟩

/-- Complete classification of a single composite semantic macro that divides
`2^L`: it is exactly `2^m` with `m>=2`, and its task horizon is the closed-form
`H_m`. -/
theorem primeSingleMacro_separates_iff_twoPowerClosedHorizon_le_of_dvd_hardTarget
    {r N g h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hgSemantic : g ∈ RootQuotientNontrivialPowerFreeBasis r N)
    (hgRank : 2 ≤ rootQuotientPrimeFactorCount g)
    (hgDvd : g ∣ 2 ^ rootQuotientPrimeHorizon r N) :
    let m := g.factorization 2
    SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeSingleMacroBasis N g) ↔
      rootQuotientPrimeTwoPowerHorizon m N ≤ h := by
  let m := g.factorization 2
  have hgPos : 1 ≤ g := by omega
  have hgEq : g = 2 ^ m :=
    eq_two_pow_factorization_two_of_dvd_two_pow hgPos hgDvd
  have hCount : rootQuotientPrimeFactorCount g = m := by
    rw [hgEq]
    exact rootQuotientPrimeFactorCount_two_pow m
  have hm : 2 ≤ m := by omega
  have hBasisEq : RootQuotientPrimeSingleMacroBasis N g =
      RootQuotientPrimeTwoPowerBasis N m := by
    rw [hgEq]
    rfl
  dsimp only
  rw [hBasisEq]
  exact primeTwoPowerBasis_separates_iff_closedHorizon_le
    hr hm hN hBinary

/-- Structural necessity for any strict one-macro speedup.

If one composite semantic macro achieves a horizon strictly below the
prime-only horizon, that macro must be a power of two `2^m` with `m>=2`.
Macros carrying any odd prime factor cannot accelerate the hard target `2^L`
and therefore cannot improve worst-case depth. -/
theorem exists_twoPower_macro_of_singleCompositeMacro_strict_speedup
    {r N g h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hgSemantic : g ∈ RootQuotientNontrivialPowerFreeBasis r N)
    (hgRank : 2 ≤ rootQuotientPrimeFactorCount g)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeSingleMacroBasis N g))
    (hFast : h < rootQuotientPrimeHorizon r N) :
    ∃ m : ℕ, 2 ≤ m ∧ g = 2 ^ m := by
  have hgPos : 1 ≤ g := by omega
  have hgDvd : g ∣ 2 ^ rootQuotientPrimeHorizon r N := by
    by_contra hgNotDvd
    have hNoSpeed :=
      (primeSingleMacro_separates_iff_primeHorizon_le_of_not_dvd_two_pow_horizon
        hr hN hBinary hgPos hgNotDvd).1 hSep
    omega
  let m := g.factorization 2
  have hgEq : g = 2 ^ m :=
    eq_two_pow_factorization_two_of_dvd_two_pow hgPos hgDvd
  have hCount : rootQuotientPrimeFactorCount g = m := by
    rw [hgEq]
    exact rootQuotientPrimeFactorCount_two_pow m
  exact ⟨m, by omega, hgEq⟩

/-- Full dichotomy for one composite semantic macro in the high-root regime:

* if it misses the prime hard target, its exact depth remains `L`;
* if it hits the hard target, it is a `2^m` macro and has exact depth `H_m`.

Thus the entire one-macro design space is reduced to the explicit power-of-two
family. -/
theorem singleCompositeMacro_highRoot_dichotomy
    {r N g : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hgSemantic : g ∈ RootQuotientNontrivialPowerFreeBasis r N)
    (hgRank : 2 ≤ rootQuotientPrimeFactorCount g) :
    (¬g ∣ 2 ^ rootQuotientPrimeHorizon r N ∧
      ∀ h : ℕ,
        SeparatesRootQuotientWordsUpTo
            r N h (RootQuotientPrimeSingleMacroBasis N g) ↔
          rootQuotientPrimeHorizon r N ≤ h) ∨
    (∃ m : ℕ, 2 ≤ m ∧ g = 2 ^ m ∧
      ∀ h : ℕ,
        SeparatesRootQuotientWordsUpTo
            r N h (RootQuotientPrimeSingleMacroBasis N g) ↔
          rootQuotientPrimeTwoPowerHorizon m N ≤ h) := by
  by_cases hgDvd : g ∣ 2 ^ rootQuotientPrimeHorizon r N
  · right
    let m := g.factorization 2
    have hgPos : 1 ≤ g := by omega
    have hgEq : g = 2 ^ m :=
      eq_two_pow_factorization_two_of_dvd_two_pow hgPos hgDvd
    have hCount : rootQuotientPrimeFactorCount g = m := by
      rw [hgEq]
      exact rootQuotientPrimeFactorCount_two_pow m
    refine ⟨m, by omega, hgEq, ?_⟩
    intro h
    exact primeSingleMacro_separates_iff_twoPowerClosedHorizon_le_of_dvd_hardTarget
      hr hN hBinary hgSemantic hgRank hgDvd
  · left
    refine ⟨hgDvd, ?_⟩
    intro h
    exact primeSingleMacro_separates_iff_primeHorizon_le_of_not_dvd_two_pow_horizon
      hr hN hBinary (by omega) hgDvd

end EnterpriseMath.Quotient
