import EnterpriseMath.Quotient.RootQuotientWordBasis
import EnterpriseMath.Quotient.RootQuotientThresholdRegime
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Every prime boundary is `r`-power-free for `r>=2`. -/
theorem prime_rPowerFree
    {r p : ℕ}
    (hr : 2 ≤ r)
    (hp : p.Prime) :
    RPowerFree r p := by
  intro t ht hPowDvd
  rcases hp.eq_one_or_self_of_dvd (t ^ r) hPowDvd with hOne | hPrimePow
  · have hTwoPowLe : 2 ^ r ≤ t ^ r := Nat.pow_le_pow_left ht r
    have hTwoPowGt : 1 < 2 ^ r := by
      have : 2 ^ 1 ≤ 2 ^ r := Nat.pow_le_pow_right (by omega) (by omega)
      simpa using this
    omega
  · have htDvdPow : t ∣ t ^ r := by
      refine ⟨t ^ (r - 1), ?_⟩
      calc
        t ^ r = t ^ ((r - 1) + 1) := by congr 1 <;> omega
        _ = t ^ (r - 1) * t := by rw [pow_succ']
        _ = t * t ^ (r - 1) := by ring
    have htDvdP : t ∣ p := by
      rw [← hPrimePow]
      exact htDvdPow
    rcases hp.eq_one_or_self_of_dvd t htDvdP with htOne | htP
    · omega
    · have htLtPow : t < t ^ r := by
        calc
          t < t ^ 2 := by nlinarith
          _ ≤ t ^ r := Nat.pow_le_pow_right (by omega) hr
      rw [htP] at htLtPow
      omega

/-- If a positive-generator word compiles to a prime denominator, then that
prime occurs as one of the primitive generators in the word.  No factorization
uniqueness is needed: primality of the product is enough. -/
theorem prime_mem_generators_of_word_product
    {G : Set ℕ} {w : List ℕ} {p : ℕ}
    (hp : p.Prime)
    (hw : RootQuotientWordOver G w)
    (hProd : rootQuotientWordProduct w = p) :
    p ∈ G := by
  induction w with
  | nil =>
      simp [rootQuotientWordProduct] at hProd
      exact (hp.ne_one hProd.symm).elim
  | cons a w ih =>
      have haG : a ∈ G := hw a (by simp)
      have hTail : RootQuotientWordOver G w := by
        intro b hb
        exact hw b (by simp [hb])
      have haDvd : a ∣ p := by
        refine ⟨rootQuotientWordProduct w, ?_⟩
        simpa [rootQuotientWordProduct] using hProd.symm
      rcases hp.eq_one_or_self_of_dvd a haDvd with haOne | haPrime
      · have hTailProd : rootQuotientWordProduct w = p := by
          simpa [rootQuotientWordProduct, haOne] using hProd
        exact ih hTail hTailProd
      · simpa [haPrime] using haG

/-- Prime generator skeleton for arbitrary finite horizon.

For root order `r>=2`, any positive primitive quotient-generator language whose
words of length at most `h` separate all exact states in `0,...,N` must contain
every prime `p<=N`.  Composition may reduce the one-step test family, but it
cannot eliminate these prime primitive generators. -/
theorem prime_generator_forced_of_word_separates
    {r N h p : ℕ} {G : Set ℕ}
    (hr : 2 ≤ r)
    (hp : p.Prime)
    (hpN : p ≤ N)
    (hG : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo r N h G) :
    p ∈ G := by
  have hpFree : RPowerFree r p := prime_rPowerFree hr hp
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h) (G := G) (by omega) hG).1 hSep
      p hp.one_le hpN hpFree
  obtain ⟨w, _hwLen, hwG, hProd⟩ := hReach
  exact prime_mem_generators_of_word_product hp hwG hProd.symm

end EnterpriseMath.Quotient
