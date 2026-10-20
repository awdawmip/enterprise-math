import EnterpriseMath.Quotient.RootQuotientCapacity
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

/-- Enlarging the state bound by one can increase the exact prime-only horizon
by at most one.

If the new boundary carries `m` prime-factor tokens, removing one prime factor
produces a smaller divisor with rank `m-1`; divisor closure keeps that boundary
inside the semantic power-free set. -/
theorem rootQuotientPrimeHorizon_succ_le
    (r N : ℕ) :
    rootQuotientPrimeHorizon r (N + 1) ≤
      rootQuotientPrimeHorizon r N + 1 := by
  apply (rootQuotientPrimeHorizon_le_iff
    (r := r) (N := N + 1)
    (h := rootQuotientPrimeHorizon r N + 1)).2
  intro b hbPos hbNsucc hbFree
  by_cases hbN : b ≤ N
  · have hOldBound :=
      (rootQuotientPrimeHorizon_le_iff
        (r := r) (N := N) (h := rootQuotientPrimeHorizon r N)).1 le_rfl
    exact (hOldBound b hbPos hbN hbFree).trans (Nat.le_succ _)
  · have hbEq : b = N + 1 := by omega
    subst b
    by_cases hOne : N + 1 = 1
    · have hZero : rootQuotientPrimeFactorCount (N + 1) = 0 := by
        simp [hOne, rootQuotientPrimeFactorCount]
      omega
    · obtain ⟨p, hpPrime, hpDvd⟩ := Nat.exists_prime_and_dvd hOne
      rcases hpDvd with ⟨c, hEq⟩
      have hcPos : 1 ≤ c := by
        by_contra hNot
        have hcZero : c = 0 := by omega
        subst c
        simp at hEq
        omega
      have hcLt : c < N + 1 := by
        nlinarith [hEq, hpPrime.two_le, hcPos]
      have hcN : c ≤ N := by omega
      have hcDvd : c ∣ N + 1 := by
        refine ⟨p, ?_⟩
        simpa [Nat.mul_comm] using hEq
      have hcFree : RPowerFree r c := by
        intro t ht htd
        exact hbFree t ht (dvd_trans htd hcDvd)
      have hOldBound :=
        (rootQuotientPrimeHorizon_le_iff
          (r := r) (N := N) (h := rootQuotientPrimeHorizon r N)).1 le_rfl
      have hcCount :
          rootQuotientPrimeFactorCount c ≤ rootQuotientPrimeHorizon r N :=
        hOldBound c hcPos hcN hcFree
      have hpCount : rootQuotientPrimeFactorCount p = 1 := by
        rw [rootQuotientPrimeFactorCount, Nat.primeFactorsList_prime hpPrime]
        simp
      calc
        rootQuotientPrimeFactorCount (N + 1) =
            rootQuotientPrimeFactorCount (p * c) := by rw [hEq]
        _ = rootQuotientPrimeFactorCount p +
            rootQuotientPrimeFactorCount c :=
          rootQuotientPrimeFactorCount_mul hpPrime.one_le hcPos
        _ = 1 + rootQuotientPrimeFactorCount c := by rw [hpCount]
        _ ≤ rootQuotientPrimeHorizon r N + 1 := by omega

/-- The exact prime horizon is a unit-step staircase in the state bound. -/
theorem rootQuotientPrimeHorizon_succ_eq_or_eq_succ
    (r N : ℕ) :
    rootQuotientPrimeHorizon r (N + 1) = rootQuotientPrimeHorizon r N ∨
    rootQuotientPrimeHorizon r (N + 1) = rootQuotientPrimeHorizon r N + 1 := by
  have hMono :
      rootQuotientPrimeHorizon r N ≤ rootQuotientPrimeHorizon r (N + 1) :=
    rootQuotientPrimeHorizon_mono_stateBound (by omega)
  have hUpper := rootQuotientPrimeHorizon_succ_le r N
  omega

/-- Exact jump criterion for the prime-horizon staircase.

The horizon rises at `N+1` exactly when the newly admitted integer is itself a
required power-free boundary whose factor rank is one above the old horizon. -/
theorem rootQuotientPrimeHorizon_succ_eq_succ_iff
    {r N : ℕ} :
    rootQuotientPrimeHorizon r (N + 1) = rootQuotientPrimeHorizon r N + 1 ↔
      RPowerFree r (N + 1) ∧
      rootQuotientPrimeFactorCount (N + 1) =
        rootQuotientPrimeHorizon r N + 1 := by
  constructor
  · intro hJump
    have hPos : 0 < rootQuotientPrimeHorizon r (N + 1) := by omega
    obtain ⟨b, hbPos, hbN, hbFree, hbCount⟩ :=
      exists_powerFree_boundary_at_rootQuotientPrimeHorizon hPos
    have hbEq : b = N + 1 := by
      by_contra hNe
      have hbOld : b ≤ N := by omega
      have hOldBound :=
        (rootQuotientPrimeHorizon_le_iff
          (r := r) (N := N) (h := rootQuotientPrimeHorizon r N)).1 le_rfl
      have hContr := hOldBound b hbPos hbOld hbFree
      omega
    subst b
    exact ⟨hbFree, by omega⟩
  · rintro ⟨hFree, hCount⟩
    have hUpper := rootQuotientPrimeHorizon_succ_le r N
    have hNewBound :=
      (rootQuotientPrimeHorizon_le_iff
        (r := r) (N := N + 1)
        (h := rootQuotientPrimeHorizon r (N + 1))).1 le_rfl
    have hLower := hNewBound (N + 1) (by omega) (by omega) hFree
    omega

end EnterpriseMath.Quotient
