import EnterpriseMath.Quotient.RootQuotientPrimeSkeleton
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Bounded primitive prime generator alphabet. -/
def RootQuotientPrimeBasis (N : ℕ) : Set ℕ :=
  {p : ℕ | p.Prime ∧ p ≤ N}

/-- Every bounded prime generator is a positive quotient denominator. -/
theorem rootQuotientPrimeBasis_positive
    {N : ℕ} :
    PositiveRootQuotientGenerators (RootQuotientPrimeBasis N) := by
  intro p hp
  exact hp.1.one_le

/-- Every positive integer `b` admits a literal prime word of length at most `b`
whose compiled quotient denominator is exactly `b`.

The proof is finite strong descent and does not use uniqueness of factorization. -/
theorem exists_prime_word_product
    {b : ℕ}
    (hb : 1 ≤ b) :
    ∃ w : List ℕ,
      w.length ≤ b ∧
      RootQuotientWordOver (RootQuotientPrimeBasis b) w ∧
      b = rootQuotientWordProduct w := by
  induction b using Nat.strong_induction_on with
  | h b ih =>
      intro hb
      by_cases hbOne : b = 1
      · subst b
        exact ⟨[], by simp, by simp [RootQuotientWordOver], by simp [rootQuotientWordProduct]⟩
      · obtain ⟨p, hpPrime, hpDvd⟩ := Nat.exists_prime_and_dvd hbOne
        rcases hpDvd with ⟨c, hbc⟩
        have hcPos : 1 ≤ c := by
          by_contra hnot
          have hcZero : c = 0 := by omega
          subst c
          simp at hbc
          omega
        have hpTwo : 2 ≤ p := hpPrime.two_le
        have hcLt : c < b := by
          nlinarith [hbc, hpTwo, hcPos]
        obtain ⟨w, hwLen, hwPrime, hcProd⟩ := ih c hcLt hcPos
        have hpLeB : p ≤ b := by
          exact Nat.le_of_dvd (by omega) ⟨c, hbc⟩
        have hcLeB : c ≤ b := Nat.le_of_lt hcLt
        have hTail : RootQuotientWordOver (RootQuotientPrimeBasis b) w := by
          intro q hq
          have hqc := hwPrime q hq
          exact ⟨hqc.1, hqc.2.trans hcLeB⟩
        have hWord : RootQuotientWordOver (RootQuotientPrimeBasis b) (p :: w) := by
          intro q hq
          simp at hq
          rcases hq with rfl | hqTail
          · exact ⟨hpPrime, hpLeB⟩
          · exact hTail q hqTail
        have hLen : (p :: w).length ≤ b := by
          have hStep : w.length + 1 ≤ c + 1 := Nat.succ_le_succ hwLen
          have hcOneLeB : c + 1 ≤ b := by
            nlinarith [hbc, hpTwo, hcPos]
          simpa using hStep.trans hcOneLeB
        refine ⟨p :: w, hLen, hWord, ?_⟩
        calc
          b = p * c := hbc
          _ = p * rootQuotientWordProduct w := by rw [hcProd]
          _ = rootQuotientWordProduct (p :: w) := by
            simp [rootQuotientWordProduct]

/-- The bounded prime alphabet is sufficient with the explicit finite horizon
`N`: every required power-free boundary at most `N` has a prime word of length
at most its own value, hence at most `N`. -/
theorem rootQuotientPrimeBasis_separates_at_self_horizon
    {r N : ℕ}
    (hr : 1 ≤ r) :
    SeparatesRootQuotientWordsUpTo r N N (RootQuotientPrimeBasis N) := by
  apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
    (r := r) (N := N) (h := N) (G := RootQuotientPrimeBasis N)
    hr rootQuotientPrimeBasis_positive).2
  intro b hbPos hbN _hbFree
  obtain ⟨w, hwLen, hwPrimeB, hProd⟩ := exists_prime_word_product hbPos
  have hWordN : RootQuotientWordOver (RootQuotientPrimeBasis N) w := by
    intro p hpw
    have hpB := hwPrimeB p hpw
    exact ⟨hpB.1, hpB.2.trans hbN⟩
  exact ⟨w, hwLen.trans hbN, hWordN, hProd⟩

/-- For `r>=2`, the bounded prime alphabet is contained in every primitive
generator set that separates the bounded exact state domain at any finite word
horizon. -/
theorem rootQuotientPrimeBasis_subset_of_word_separates
    {r N h : ℕ} {G : Set ℕ}
    (hr : 2 ≤ r)
    (hG : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo r N h G) :
    RootQuotientPrimeBasis N ⊆ G := by
  intro p hp
  exact prime_generator_forced_of_word_separates
    hr hp.1 hp.2 hG hSep

/-- Exact primitive-alphabet theorem.

For `r>=2`, primes up to `N` form the unique least primitive quotient-generator
alphabet (under inclusion) among all finite-horizon languages capable of exact
state separation on `0,...,N`.  Horizon `N` is an explicit sufficient bound;
the independent depth problem asks how far that horizon can be reduced. -/
theorem rootQuotientPrimeBasis_is_least_finite_horizon_alphabet
    {r N : ℕ}
    (hr : 2 ≤ r) :
    SeparatesRootQuotientWordsUpTo r N N (RootQuotientPrimeBasis N) ∧
    ∀ {h : ℕ} {G : Set ℕ},
      PositiveRootQuotientGenerators G →
      SeparatesRootQuotientWordsUpTo r N h G →
      RootQuotientPrimeBasis N ⊆ G := by
  constructor
  · exact rootQuotientPrimeBasis_separates_at_self_horizon (by omega)
  · intro h G hG hSep
    exact rootQuotientPrimeBasis_subset_of_word_separates hr hG hSep

end EnterpriseMath.Quotient
