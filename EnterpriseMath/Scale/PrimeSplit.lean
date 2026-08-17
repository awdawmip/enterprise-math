import Mathlib.Data.Nat.Prime.Basic

namespace EnterpriseMath.Scale

/-- Arithmetic shadow of two-scale overlap disconnection: a nontrivial common divisor
is present exactly when the gcd exceeds one. The geometric identification with graph
components is a separate R007 theorem. -/
def arithmeticSplit (n d : ℕ) : Prop :=
  1 < n.gcd d

/-- At a prime scale, arithmetic splitting is exactly divisibility by that prime. -/
theorem arithmeticSplit_prime_iff {n p : ℕ} (hp : p.Prime) :
    arithmeticSplit n p ↔ p ∣ n := by
  constructor
  · intro hs
    have hdiv : n.gcd p ∣ p := Nat.gcd_dvd_right n p
    rcases hp.eq_one_or_self_of_dvd (n.gcd p) hdiv with h1 | hself
    · exfalso
      unfold arithmeticSplit at hs
      rw [h1] at hs
      exact (Nat.lt_irrefl 1) hs
    · rw [← hself]
      exact Nat.gcd_dvd_left n p
  · intro hpn
    unfold arithmeticSplit
    rw [Nat.gcd_eq_right hpn]
    exact hp.one_lt

/-- The smallest prime factor always produces an arithmetic split for `n ≠ 1`. -/
theorem arithmeticSplit_minFac {n : ℕ} (hn1 : n ≠ 1) :
    arithmeticSplit n n.minFac := by
  exact (arithmeticSplit_prime_iff (Nat.minFac_prime hn1)).2 (Nat.minFac_dvd n)

/-- No positive split scale can occur before the smallest prime factor. -/
theorem minFac_le_of_arithmeticSplit {n d : ℕ} (hd : 0 < d)
    (hs : arithmeticSplit n d) :
    n.minFac ≤ d := by
  have hg_ne_one : n.gcd d ≠ 1 := by
    intro hg
    unfold arithmeticSplit at hs
    rw [hg] at hs
    exact (Nat.lt_irrefl 1) hs
  obtain ⟨p, hp, hpg⟩ := Nat.exists_prime_and_dvd hg_ne_one
  have hpn : p ∣ n := dvd_trans hpg (Nat.gcd_dvd_left n d)
  have hpd : p ∣ d := dvd_trans hpg (Nat.gcd_dvd_right n d)
  exact le_trans (Nat.minFac_le_of_dvd hp.two_le hpn) (Nat.le_of_dvd hd hpd)

/-- Arithmetic first-disconnect theorem: for `n ≠ 1`, `minFac n` is a split scale
and is no larger than every other positive split scale. -/
theorem minFac_is_first_arithmeticSplit {n : ℕ} (hn1 : n ≠ 1) :
    arithmeticSplit n n.minFac ∧
      ∀ d, 0 < d → arithmeticSplit n d → n.minFac ≤ d := by
  refine ⟨arithmeticSplit_minFac hn1, ?_⟩
  intro d hd hs
  exact minFac_le_of_arithmeticSplit hd hs

end EnterpriseMath.Scale
