import EnterpriseMath.Quotient.RootQuotientPrimeFourHorizon
import EnterpriseMath.Quotient.RootQuotientAlphabetNormalization
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Bounded primes together with one arbitrary extra primitive macro. -/
def RootQuotientPrimeSingleMacroBasis (N g : ℕ) : Set ℕ :=
  RootQuotientPrimeBasis N ∪ ({g} : Set ℕ)

/-- A positive extra macro preserves positivity of the primitive alphabet. -/
theorem rootQuotientPrimeSingleMacroBasis_positive
    {N g : ℕ}
    (hgPos : 1 ≤ g) :
    PositiveRootQuotientGenerators
      (RootQuotientPrimeSingleMacroBasis N g) := by
  intro a ha
  rcases ha with haPrime | haG
  · exact haPrime.1.one_le
  · have hEq : a = g := by simpa using haG
    subst a
    exact hgPos

/-- Any positive divisor of a power of two is itself a power of two, with
exponent given by its `2`-adic factorization coordinate. -/
theorem eq_two_pow_factorization_two_of_dvd_two_pow
    {g L : ℕ}
    (hgPos : 1 ≤ g)
    (hgDvd : g ∣ 2 ^ L) :
    g = 2 ^ g.factorization 2 := by
  have hgZero : g ≠ 0 := by omega
  have hPowZero : 2 ^ L ≠ 0 := by positivity
  apply Nat.eq_pow_of_factorization_eq_single hgZero
  ext p
  by_cases hp : p = 2
  · subst p
    simp [Nat.prime_two]
  · have hLe : g.factorization p ≤ (2 ^ L).factorization p :=
      ((Nat.factorization_le_iff_dvd hgZero hPowZero).2 hgDvd) p
    have hPowP : (2 ^ L).factorization p = 0 := by
      rw [Nat.Prime.factorization_pow Nat.prime_two]
      simp [hp]
    have hgP : g.factorization p = 0 := by omega
    rw [hgP]
    simp [hp]

/-- If a positive divisor of a power of two carries at least two prime-factor
tokens, then it is divisible by four. -/
theorem four_dvd_of_dvd_two_pow_of_two_le_factorCount
    {g L : ℕ}
    (hgPos : 1 ≤ g)
    (hgDvd : g ∣ 2 ^ L)
    (hgRank : 2 ≤ rootQuotientPrimeFactorCount g) :
    4 ∣ g := by
  have hEq := eq_two_pow_factorization_two_of_dvd_two_pow hgPos hgDvd
  have hCount :
      rootQuotientPrimeFactorCount g = g.factorization 2 := by
    rw [hEq]
    simpa using rootQuotientPrimeFactorCount_two_pow (g.factorization 2)
  have hExp : 2 ≤ g.factorization 2 := by omega
  rw [hEq]
  have hPow : 2 ^ 2 ∣ 2 ^ g.factorization 2 :=
    pow_dvd_pow 2 hExp
  norm_num at hPow ⊢
  exact hPow

/-- The mixed weighted-shell witness `2*3^(k-1)` has exactly one factor of two,
so four does not divide it. -/
theorem four_not_dvd_two_mul_three_pow_pred
    {k : ℕ}
    (hk : 1 ≤ k) :
    ¬4 ∣ 2 * 3 ^ (k - 1) := by
  have hValuation : (2 * 3 ^ (k - 1)).factorization 2 = 1 := by
    rw [Nat.factorization_mul (by omega) (by positivity)]
    simp [Nat.prime_two, Nat.prime_three]
  intro hFour
  have hPow : 2 ^ 2 ∣ 2 * 3 ^ (k - 1) := by
    norm_num
    exact hFour
  have hExp : 2 ≤ (2 * 3 ^ (k - 1)).factorization 2 :=
    (Nat.prime_two.pow_dvd_iff_le_factorization (by positivity)).1 hPow
  rw [hValuation] at hExp
  omega

/-- If the extra macro cannot divide the target product, every compiling word
uses only the bounded-prime part of the alphabet. -/
theorem wordOver_primeSingleMacro_of_macro_not_dvd_product
    {N g b : ℕ} {w : List ℕ}
    (hw : RootQuotientWordOver (RootQuotientPrimeSingleMacroBasis N g) w)
    (hProd : b = rootQuotientWordProduct w)
    (hgNotDvd : ¬g ∣ b) :
    RootQuotientWordOver (RootQuotientPrimeBasis N) w := by
  intro a ha
  have haBasis := hw a ha
  rcases haBasis with haPrime | haMacro
  · exact haPrime
  · have hEq : a = g := by simpa using haMacro
    subst a
    have hgDvd : g ∣ b := word_member_dvd_compiled_product ha hProd
    exact (hgNotDvd hgDvd).elim

/-- Any single composite semantic macro has worst-case high-root depth at least
the exact prime-plus-four horizon.

This proves that macro `4` is globally depth-optimal among all presentations
obtained by adjoining one composite semantic instruction to the bounded prime
core. -/
theorem primeFourHorizon_le_of_single_composite_macro_separates
    {r N g h : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N)
    (hgSemantic : g ∈ RootQuotientNontrivialPowerFreeBasis r N)
    (hgRank : 2 ≤ rootQuotientPrimeFactorCount g)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeSingleMacroBasis N g)) :
    rootQuotientPrimeFourHorizon N ≤ h := by
  let L := rootQuotientPrimeHorizon r N
  let H := rootQuotientPrimeFourHorizon N
  have hLog : L = Nat.log 2 N := by
    dsimp [L]
    exact rootQuotientPrimeHorizon_eq_nat_log_two_of_stateBound_lt_two_pow_rootOrder
      hr (by omega) hBinary
  have hPowLLeN : 2 ^ L ≤ N := by
    rw [hLog]
    exact Nat.pow_log_le_self 2 (by omega)
  have hPowLFree : RPowerFree r (2 ^ L) :=
    rPowerFree_of_lt_two_pow_rootOrder (by positivity)
      (hPowLLeN.trans_lt hBinary)
  have hMacroPos : 1 ≤ g := by omega
  have hBasisPos : PositiveRootQuotientGenerators
      (RootQuotientPrimeSingleMacroBasis N g) :=
    rootQuotientPrimeSingleMacroBasis_positive hMacroPos
  by_cases hgDvdPow : g ∣ 2 ^ L
  · have hFourDvdG : 4 ∣ g :=
      four_dvd_of_dvd_two_pow_of_two_le_factorCount
        hMacroPos hgDvdPow hgRank
    have hHEq : H = 1 + Nat.log 3 (N / 2) := by
      dsimp [H]
      exact rootQuotientPrimeFourHorizon_eq hN
    have hHPos : 1 ≤ H := by
      rw [hHEq]
      omega
    let b := 2 * 3 ^ (H - 1)
    have hDivPos : N / 2 ≠ 0 := by omega
    have hThreeLe : 3 ^ Nat.log 3 (N / 2) ≤ N / 2 :=
      Nat.pow_log_le_self 3 hDivPos
    have hbN : b ≤ N := by
      dsimp [b]
      rw [hHEq]
      have hExpEq : 1 + Nat.log 3 (N / 2) - 1 = Nat.log 3 (N / 2) := by omega
      rw [hExpEq]
      have hScaled : 2 * 3 ^ Nat.log 3 (N / 2) ≤ 2 * (N / 2) :=
        Nat.mul_le_mul_left 2 hThreeLe
      have hTwiceDiv : 2 * (N / 2) ≤ N := by omega
      exact hScaled.trans hTwiceDiv
    have hbPos : 1 ≤ b := by
      dsimp [b]
      positivity
    have hbFree : RPowerFree r b :=
      rPowerFree_of_lt_two_pow_rootOrder hbPos (hbN.trans_lt hBinary)
    have hgNotDvdB : ¬g ∣ b := by
      intro hgDvdB
      have hFourDvdB : 4 ∣ b := hFourDvdG.trans hgDvdB
      exact four_not_dvd_two_mul_three_pow_pred hHPos hFourDvdB
    have hReach :=
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeSingleMacroBasis N g)
        (by omega) hBasisPos).1 hSep
        b hbPos hbN hbFree
    obtain ⟨w, hwLen, hwBasis, hProd⟩ := hReach
    have hwPrime : RootQuotientWordOver (RootQuotientPrimeBasis N) w :=
      wordOver_primeSingleMacro_of_macro_not_dvd_product
        hwBasis hProd hgNotDvdB
    have hExactLen : w.length = rootQuotientPrimeFactorCount b :=
      prime_word_length_eq_primeFactorCount hwPrime hProd.symm
    have hValuation : b.factorization 2 = 1 := by
      dsimp [b]
      rw [Nat.factorization_mul (by omega) (by positivity)]
      simp [Nat.prime_two, Nat.prime_three]
    have hCostB : rootQuotientPrimeFourCost b = H := by
      dsimp [b]
      exact primeFourCost_two_mul_three_pow_pred hHPos
    have hCountB : rootQuotientPrimeFactorCount b = H := by
      dsimp [rootQuotientPrimeFourCost] at hCostB
      rw [hValuation] at hCostB
      omega
    rw [hCountB] at hExactLen
    omega
  · have hReach :=
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeSingleMacroBasis N g)
        (by omega) hBasisPos).1 hSep
        (2 ^ L) (by positivity) hPowLLeN hPowLFree
    obtain ⟨w, hwLen, hwBasis, hProd⟩ := hReach
    have hwPrime : RootQuotientWordOver (RootQuotientPrimeBasis N) w :=
      wordOver_primeSingleMacro_of_macro_not_dvd_product
        hwBasis hProd hgDvdPow
    have hExactLen : w.length = rootQuotientPrimeFactorCount (2 ^ L) :=
      prime_word_length_eq_primeFactorCount hwPrime hProd.symm
    have hPowCount : rootQuotientPrimeFactorCount (2 ^ L) = L :=
      rootQuotientPrimeFactorCount_two_pow L
    rw [hPowCount] at hExactLen
    have hFourLeL : H ≤ L := by
      dsimp [H, L]
      exact primeFourHorizon_le_primeHorizon hr hN hBinary
    omega

/-- Macro `4` attains the globally optimal worst-case horizon among all single
composite semantic macro extensions of the bounded prime core. -/
theorem primeFour_is_singleCompositeMacro_depthOptimal
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hBinary : N < 2 ^ r)
    (hLThree : 3 ≤ rootQuotientPrimeHorizon r N) :
    SeparatesRootQuotientWordsUpTo
      r N (rootQuotientPrimeFourHorizon N)
      (RootQuotientPrimeFourBasis N) ∧
    (∀ g h : ℕ,
      g ∈ RootQuotientNontrivialPowerFreeBasis r N →
      2 ≤ rootQuotientPrimeFactorCount g →
      SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientPrimeSingleMacroBasis N g) →
      rootQuotientPrimeFourHorizon N ≤ h) := by
  constructor
  · exact primeFourBasis_separates_at_exact_horizon hr hN hBinary
  · intro g h hgSemantic hgRank hSep
    exact primeFourHorizon_le_of_single_composite_macro_separates
      hr hN hBinary hLThree hgSemantic hgRank hSep

end EnterpriseMath.Quotient
