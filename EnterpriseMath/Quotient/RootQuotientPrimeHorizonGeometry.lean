import EnterpriseMath.Quotient.RootQuotientPrimeBasis
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Power-free semantic boundaries are monotone in the root order: if a
boundary excludes every nontrivial `r`-th power divisor, then it also excludes
every nontrivial `s`-th power divisor for `r ≤ s`. -/
theorem rPowerFree_mono_rootOrder
    {r s b : ℕ}
    (hrs : r ≤ s)
    (hbFree : RPowerFree r b) :
    RPowerFree s b := by
  intro t ht hts
  apply hbFree t ht
  obtain ⟨c, hc⟩ := hts
  refine ⟨t ^ (s - r) * c, ?_⟩
  calc
    b = t ^ s * c := hc
    _ = (t ^ r * t ^ (s - r)) * c := by
      rw [← pow_add, Nat.add_sub_of_le hrs]
    _ = t ^ r * (t ^ (s - r) * c) := by
      simp [Nat.mul_assoc]

/-- Enlarging the bounded exact-state domain cannot decrease the exact
prime-only compiler horizon. -/
theorem rootQuotientPrimeHorizon_mono_stateBound
    {r N M : ℕ}
    (hNM : N ≤ M) :
    rootQuotientPrimeHorizon r N ≤ rootQuotientPrimeHorizon r M := by
  apply (rootQuotientPrimeHorizon_le_iff
    (r := r) (N := N) (h := rootQuotientPrimeHorizon r M)).2
  intro b hbPos hbN hbFree
  have hBound :=
    (rootQuotientPrimeHorizon_le_iff
      (r := r) (N := M) (h := rootQuotientPrimeHorizon r M)).1 le_rfl
  exact hBound b hbPos (hbN.trans hNM) hbFree

/-- Increasing root order enlarges the power-free semantic target set, so the
exact prime-only compiler horizon cannot decrease. -/
theorem rootQuotientPrimeHorizon_mono_rootOrder
    {r s N : ℕ}
    (hrs : r ≤ s) :
    rootQuotientPrimeHorizon r N ≤ rootQuotientPrimeHorizon s N := by
  apply (rootQuotientPrimeHorizon_le_iff
    (r := r) (N := N) (h := rootQuotientPrimeHorizon s N)).2
  intro b hbPos hbN hbFree
  have hBound :=
    (rootQuotientPrimeHorizon_le_iff
      (r := s) (N := N) (h := rootQuotientPrimeHorizon s N)).1 le_rfl
  exact hBound b hbPos hbN (rPowerFree_mono_rootOrder hrs hbFree)

/-- Joint monotonicity in root order and bounded state domain. -/
theorem rootQuotientPrimeHorizon_mono
    {r s N M : ℕ}
    (hrs : r ≤ s)
    (hNM : N ≤ M) :
    rootQuotientPrimeHorizon r N ≤ rootQuotientPrimeHorizon s M := by
  exact (rootQuotientPrimeHorizon_mono_rootOrder hrs).trans
    (rootQuotientPrimeHorizon_mono_stateBound hNM)

end EnterpriseMath.Quotient
