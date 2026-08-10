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

/-- Every positive exact prime horizon is attained by an actual bounded
power-free semantic denominator.  Thus the finite supremum is a genuine
critical boundary rank rather than only an abstract upper bound. -/
theorem exists_powerFree_boundary_at_rootQuotientPrimeHorizon
    {r N : ℕ}
    (hPos : 0 < rootQuotientPrimeHorizon r N) :
    ∃ b : ℕ,
      1 ≤ b ∧ b ≤ N ∧ RPowerFree r b ∧
        rootQuotientPrimeFactorCount b = rootQuotientPrimeHorizon r N := by
  classical
  let f : ℕ → ℕ := fun q =>
    if 1 ≤ q ∧ RPowerFree r q then
      rootQuotientPrimeFactorCount q
    else
      0
  have hRange : (Finset.range (N + 1)).Nonempty := by
    exact ⟨0, by simp⟩
  obtain ⟨b, hbMem, hbSup⟩ :=
    Finset.exists_mem_eq_sup (Finset.range (N + 1)) hRange f
  have hbN : b ≤ N := by
    simp at hbMem
    omega
  have hRequired : 1 ≤ b ∧ RPowerFree r b := by
    by_contra hNot
    have hfZero : f b = 0 := by
      simp [f, hNot]
    have hHorizonZero : rootQuotientPrimeHorizon r N = 0 := by
      rw [rootQuotientPrimeHorizon]
      calc
        (Finset.range (N + 1)).sup (fun q =>
            if 1 ≤ q ∧ RPowerFree r q then
              rootQuotientPrimeFactorCount q
            else
              0) = f b := by
                simpa [f] using hbSup
        _ = 0 := hfZero
    omega
  refine ⟨b, hRequired.1, hbN, hRequired.2, ?_⟩
  have hHorizonEq :
      rootQuotientPrimeHorizon r N = rootQuotientPrimeFactorCount b := by
    rw [rootQuotientPrimeHorizon]
    calc
      (Finset.range (N + 1)).sup (fun q =>
          if 1 ≤ q ∧ RPowerFree r q then
            rootQuotientPrimeFactorCount q
          else
            0) = f b := by
              simpa [f] using hbSup
      _ = rootQuotientPrimeFactorCount b := by
        simp [f, hRequired]
  exact hHorizonEq.symm

end EnterpriseMath.Quotient
