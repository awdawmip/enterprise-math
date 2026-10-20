import EnterpriseMath.Quotient.RootQuotientWordBasis
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- **Spare-generator divisibility principle.**

If a target is reachable within horizon `h` after adjoining one generator `g`
but is not reachable from the base alphabet `G`, then `g` must divide the
target.  Indeed, otherwise a successful word cannot contain `g`; the same word
would already be a base word.

This is the generic finite-certificate mechanism behind the budget-three
transient optimizer search: once hard prime directions consume the forced
slots, the remaining spare macro only needs to be tested among divisors of a
base-hard target. -/
theorem spare_generator_dvd_target_of_reachable_not_reachable_without
    {G : Set ℕ} {g t h : ℕ}
    (hReach : RootQuotientProductReachableWithin h (insert g G) t)
    (hNoBase : ¬RootQuotientProductReachableWithin h G t) :
    g ∣ t := by
  by_contra hNotDvd
  obtain ⟨w, hwLen, hwFull, hProd⟩ := hReach
  apply hNoBase
  refine ⟨w, hwLen, ?_, hProd⟩
  intro a haWord
  have haFull := hwFull a haWord
  simp only [Set.mem_insert_iff] at haFull
  rcases haFull with haG | haBase
  · subst a
    have hgDvd : g ∣ t :=
      word_member_dvd_compiled_product haWord hProd
    exact (hNotDvd hgDvd).elim
  · exact haBase

/-- Two-target form: one spare generator that repairs two targets outside the
base reachability ball must divide their gcd. -/
theorem spare_generator_dvd_gcd_of_two_unreachable_targets
    {G : Set ℕ} {g t u h : ℕ}
    (hReachT : RootQuotientProductReachableWithin h (insert g G) t)
    (hNoBaseT : ¬RootQuotientProductReachableWithin h G t)
    (hReachU : RootQuotientProductReachableWithin h (insert g G) u)
    (hNoBaseU : ¬RootQuotientProductReachableWithin h G u) :
    g ∣ Nat.gcd t u := by
  apply Nat.dvd_gcd
  · exact spare_generator_dvd_target_of_reachable_not_reachable_without
      hReachT hNoBaseT
  · exact spare_generator_dvd_target_of_reachable_not_reachable_without
      hReachU hNoBaseU

/-- If the two base-hard targets are coprime, no nontrivial single spare
instruction can repair both. -/
theorem no_nontrivial_spare_generator_repairs_two_coprime_targets
    {G : Set ℕ} {g t u h : ℕ}
    (hgTwo : 2 ≤ g)
    (hCoprime : Nat.Coprime t u)
    (hReachT : RootQuotientProductReachableWithin h (insert g G) t)
    (hNoBaseT : ¬RootQuotientProductReachableWithin h G t)
    (hReachU : RootQuotientProductReachableWithin h (insert g G) u)
    (hNoBaseU : ¬RootQuotientProductReachableWithin h G u) :
    False := by
  have hgGcd := spare_generator_dvd_gcd_of_two_unreachable_targets
    hReachT hNoBaseT hReachU hNoBaseU
  rw [hCoprime.gcd_eq_one] at hgGcd
  have hgLe : g ≤ 1 := Nat.le_of_dvd (by omega) hgGcd
  omega

end EnterpriseMath.Quotient
