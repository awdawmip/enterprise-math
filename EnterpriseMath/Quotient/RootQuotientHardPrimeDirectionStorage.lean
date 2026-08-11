import EnterpriseMath.Quotient.RootQuotientStableMacroObstruction
import EnterpriseMath.Quotient.RootQuotientCompositeMacroStorage
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Pure-prime directions that are individually hard at horizon `h`: their
`(h+1)`-st powers already lie inside the bounded state domain. -/
def RootQuotientHardPrimeDirections
    (N h : ℕ) : Set ℕ :=
  {p : ℕ | p.Prime ∧ p ^ (h + 1) ≤ N}

/-- The hard prime-direction set is finite. -/
theorem rootQuotientHardPrimeDirections_finite
    (N h : ℕ) :
    (RootQuotientHardPrimeDirections N h).Finite := by
  apply (Set.finite_Iic N).subset
  intro p hp
  have hpPrime : p.Prime := hp.1
  have hpLePow : p ≤ p ^ (h + 1) := by
    calc
      p = p ^ 1 := by simp
      _ ≤ p ^ (h + 1) :=
        Nat.pow_le_pow_right hpPrime.one_le (by omega)
  exact hpLePow.trans hp.2

/-- Every hard pure-prime direction must be served by some optional composite
macro in any separator meeting horizon `h`.

If no optional macro serves `p`, then a word compiling `p^(h+1)` can contain no
optional macro at all: every such macro occurrence divides the compiled pure
prime power and hence would itself serve direction `p`.  The word is therefore
prime-only and has exact length `h+1`, contradicting the horizon `h`. -/
theorem exists_macro_serving_hardPrimeDirection_of_separator
    {r N h p : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (hSFamily : RootQuotientCompositeMacroFamily r N S)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ S))
    (hpHard : p ∈ RootQuotientHardPrimeDirections N h) :
    ∃ g : ℕ, g ∈ S ∧ RootQuotientMacroServesPrimeDirection g p := by
  classical
  have hpPrime : p.Prime := hpHard.1
  have hpPowLeN : p ^ (h + 1) ≤ N := hpHard.2
  have hpPowPos : 1 ≤ p ^ (h + 1) := by positivity
  have hpPowFree : RPowerFree r (p ^ (h + 1)) :=
    rPowerFree_of_lt_two_pow_rootOrder hpPowPos
      (hpPowLeN.trans_lt hBinary)
  have hUnionPos : PositiveRootQuotientGenerators
      (RootQuotientPrimeBasis N ∪ S) := by
    intro g hg
    rcases hg with hgPrime | hgS
    · exact hgPrime.1.one_le
    · have hgSemantic := (hSFamily hgS).1
      omega
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeBasis N ∪ S)
      (by omega) hUnionPos).1 hSep
      (p ^ (h + 1)) hpPowPos hpPowLeN hpPowFree
  obtain ⟨w, hwLen, hwUnion, hProd⟩ := hReach
  by_contra hNo
  push_neg at hNo
  have hwPrime : RootQuotientWordOver (RootQuotientPrimeBasis N) w := by
    intro g hgWord
    have hgUnion := hwUnion g hgWord
    rcases hgUnion with hgPrime | hgS
    · exact hgPrime
    · have hgSemantic := (hSFamily hgS).1
      have hgDvd : g ∣ p ^ (h + 1) :=
        word_member_dvd_compiled_product hgWord hProd
      have hgServes : RootQuotientMacroServesPrimeDirection g p :=
        macroServesPrimeDirection_of_dvd_primePow
          hpPrime hgSemantic.1 hgDvd
      exact (hNo g hgS hgServes).elim
  have hExact : w.length =
      rootQuotientPrimeFactorCount (p ^ (h + 1)) :=
    prime_word_length_eq_primeFactorCount hwPrime hProd.symm
  have hpCount : rootQuotientPrimeFactorCount p = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hpPrime]
    simp
  have hPowCount : rootQuotientPrimeFactorCount (p ^ (h + 1)) = h + 1 := by
    rw [rootQuotientPrimeFactorCount_pow hpPrime.one_le, hpCount]
    simp
  rw [hPowCount] at hExact
  omega

/-- **Hard-direction cardinality lower bound.**

Every hard prime direction needs its own optional composite macro type.  Since
one positive integer cannot serve two distinct prime directions, the number of
hard directions is bounded by the size of every feasible composite-macro
family. -/
theorem hardPrimeDirections_ncard_le_macroFamily_of_separator
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hBinary : N < 2 ^ r)
    (hSFinite : S.Finite)
    (hSFamily : RootQuotientCompositeMacroFamily r N S)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ S)) :
    (RootQuotientHardPrimeDirections N h).ncard ≤ S.ncard := by
  classical
  let H := RootQuotientHardPrimeDirections N h
  have hServe : ∀ p : ℕ, p ∈ H →
      ∃ g : ℕ, g ∈ S ∧ RootQuotientMacroServesPrimeDirection g p := by
    intro p hp
    exact exists_macro_serving_hardPrimeDirection_of_separator
      hr hBinary hSFamily hSep hp
  let f : ℕ → ℕ := fun p =>
    if hp : p ∈ H then Classical.choose (hServe p hp) else 1
  have hfSpec : ∀ p : ℕ, (hp : p ∈ H) →
      f p ∈ S ∧ RootQuotientMacroServesPrimeDirection (f p) p := by
    intro p hp
    dsimp [f]
    rw [dif_pos hp]
    exact Classical.choose_spec (hServe p hp)
  apply Set.ncard_le_ncard_of_injOn f
  · intro p hp
    exact (hfSpec p hp).1
  · intro p hp q hq hEq
    have hpPrime : p.Prime := hp.1
    have hqPrime : q.Prime := hq.1
    exact primeDirection_eq_of_macro_serves_both
      hpPrime hqPrime (hfSpec p hp).2 (hEq ▸ (hfSpec q hq).2)
  · exact hSFinite

/-- Fixed-horizon storage consequence: the true minimum optional-macro count is
at least the number of hard pure-prime directions. -/
theorem hardPrimeDirections_ncard_le_minimumCompositeMacroCount
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    (RootQuotientHardPrimeDirections N h).ncard ≤
      rootQuotientMinimumCompositeMacroCount r N h := by
  obtain ⟨S, hS, hSCard⟩ :=
    exists_rootQuotientMinimumCompositeMacroPresentation hr hh
  have hLower := hardPrimeDirections_ncard_le_macroFamily_of_separator
    (r := r) (N := N) (h := h) (S := S)
    hr hBinary hS.1 hS.2.1 hS.2.2
  rw [hSCard] at hLower
  exact hLower

/-- Total-storage form of the hard-direction lower bound. -/
theorem primeBasis_add_hardPrimeDirections_le_minimumStorage
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    (RootQuotientPrimeBasis N).ncard +
        (RootQuotientHardPrimeDirections N h).ncard ≤
      rootQuotientMinimumStorageSize r N h := by
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr hh]
  exact Nat.add_le_add_left
    (hardPrimeDirections_ncard_le_minimumCompositeMacroCount
      hr hh hBinary) _

end EnterpriseMath.Quotient
