import EnterpriseMath.Quotient.RootQuotientRepairRelaxationGap
import EnterpriseMath.Quotient.RootQuotientPrimeDirectionDemand
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Finite hard-prime-direction set as an actual finset. -/
noncomputable def RootQuotientHardPrimeDirectionFinset
    (N h : ℕ) : Finset ℕ :=
  (rootQuotientHardPrimeDirections_finite N h).toFinset

@[simp]
theorem mem_rootQuotientHardPrimeDirectionFinset_iff
    {N h p : ℕ} :
    p ∈ RootQuotientHardPrimeDirectionFinset N h ↔
      p ∈ RootQuotientHardPrimeDirections N h := by
  simp [RootQuotientHardPrimeDirectionFinset]

/-- Pure-prime hard targets `p^(h+1)` associated with every hard direction. -/
noncomputable def RootQuotientHardPrimeTargetFinset
    (N h : ℕ) : Finset ℕ :=
  (RootQuotientHardPrimeDirectionFinset N h).image
    (fun p => p ^ (h + 1))

/-- Positive natural powers with fixed nonzero exponent are injective. -/
theorem hardPrimeTargetMap_injective
    {h : ℕ} :
    Set.InjOn (fun p : ℕ => p ^ (h + 1)) {p : ℕ | p.Prime} := by
  intro p _hp q _hq hEq
  exact Nat.pow_left_injective (by omega : h + 1 ≠ 0) hEq

/-- A hard target remembers its unique prime direction. -/
theorem exists_unique_hardPrimeDirection_of_mem_targetFinset
    {N h t : ℕ}
    (ht : t ∈ RootQuotientHardPrimeTargetFinset N h) :
    ∃! p : ℕ,
      p ∈ RootQuotientHardPrimeDirections N h ∧
      t = p ^ (h + 1) := by
  classical
  obtain ⟨p, hpFin, hpEq⟩ := Finset.mem_image.1 ht
  have hpHard : p ∈ RootQuotientHardPrimeDirections N h :=
    (mem_rootQuotientHardPrimeDirectionFinset_iff).1 hpFin
  refine ⟨p, ⟨hpHard, hpEq.symm⟩, ?_⟩
  intro q hq
  have hPowEq : p ^ (h + 1) = q ^ (h + 1) := by
    rw [← hpEq, hq.2]
  exact hardPrimeTargetMap_injective hpHard.1 hq.1.1 hPowEq

/-- In the high-root regime, `p^2` is an admissible semantic composite macro
for every hard direction `p` at positive horizon. -/
theorem prime_square_mem_semanticCompositeCandidates_of_hard
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hpHard : p ∈ RootQuotientHardPrimeDirections N h) :
    p ^ 2 ∈ RootQuotientSemanticCompositeCandidates r N := by
  have hpPrime : p.Prime := hpHard.1
  have hpSqLe : p ^ 2 ≤ p ^ (h + 1) :=
    Nat.pow_le_pow_right hpPrime.one_le (by omega)
  have hpSqN : p ^ 2 ≤ N := hpSqLe.trans hpHard.2
  have hpSqPos : 1 ≤ p ^ 2 := by positivity
  have hpSqFree : RPowerFree r (p ^ 2) :=
    rPowerFree_of_lt_two_pow_rootOrder hpSqPos (hpSqN.trans_lt hBinary)
  refine ⟨⟨by positivity, hpSqN, hpSqFree⟩, ?_⟩
  intro hpSqPrimeBasis
  exact Nat.Prime.not_prime_pow (by omega : 2 ≤ 2) hpSqPrimeBasis.1

/-- Canonical square macro family: one square for every hard prime direction. -/
noncomputable def RootQuotientHardPrimeSquareMacroSet
    (N h : ℕ) : Set ℕ :=
  (fun p : ℕ => p ^ 2) '' RootQuotientHardPrimeDirections N h

/-- Squaring is injective on the hard prime directions. -/
theorem hardPrimeSquareMap_injective
    {N h : ℕ} :
    Set.InjOn (fun p : ℕ => p ^ 2)
      (RootQuotientHardPrimeDirections N h) := by
  intro p _hp q _hq hEq
  exact Nat.pow_left_injective (by omega : (2 : ℕ) ≠ 0) hEq

/-- The square family has exactly one macro type per hard direction. -/
theorem hardPrimeSquareMacroSet_ncard_eq_direction_ncard
    (N h : ℕ) :
    (RootQuotientHardPrimeSquareMacroSet N h).ncard =
      (RootQuotientHardPrimeDirections N h).ncard := by
  exact hardPrimeSquareMap_injective.ncard_image

/-- The square family is finite. -/
theorem hardPrimeSquareMacroSet_finite
    (N h : ℕ) :
    (RootQuotientHardPrimeSquareMacroSet N h).Finite := by
  exact (rootQuotientHardPrimeDirections_finite N h).image
    (fun p => p ^ 2)

/-- The square family lies in the semantic-composite candidate set. -/
theorem hardPrimeSquareMacroSet_subset_semanticCandidates
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    RootQuotientHardPrimeSquareMacroSet N h ⊆
      RootQuotientSemanticCompositeCandidates r N := by
  rintro g ⟨p, hpHard, rfl⟩
  exact prime_square_mem_semanticCompositeCandidates_of_hard
    hr hh hBinary hpHard

/-- The prime-square family repairs every hard pure-prime target in exactly the
available horizon: one square macro plus `h-1` literal prime instructions. -/
theorem hardPrimeSquareMacroSet_repairs_hardPrimeTargets
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis N)
      h
      (RootQuotientHardPrimeTargetFinset N h)
      (RootQuotientSemanticCompositeCandidates r N)
      (RootQuotientHardPrimeSquareMacroSet N h) := by
  refine ⟨hardPrimeSquareMacroSet_finite N h,
    hardPrimeSquareMacroSet_subset_semanticCandidates hr hh hBinary, ?_⟩
  intro t ht
  obtain ⟨p, hpHard, htEq⟩ :=
    (exists_unique_hardPrimeDirection_of_mem_targetFinset ht).exists
  have hpLeN : p ≤ N := by
    have hpLePow : p ≤ p ^ (h + 1) := by
      calc
        p = p ^ 1 := by simp
        _ ≤ p ^ (h + 1) :=
          Nat.pow_le_pow_right hpHard.1.one_le (by omega)
    exact hpLePow.trans hpHard.2
  have hpPrimeMem : p ∈ RootQuotientPrimeBasis N :=
    ⟨hpHard.1, hpLeN⟩
  have hpSqMem : p ^ 2 ∈ RootQuotientHardPrimeSquareMacroSet N h :=
    ⟨p, hpHard, rfl⟩
  let w : List ℕ := [p ^ 2] ++ List.replicate (h - 1) p
  refine ⟨w, ?_, ?_, ?_⟩
  · dsimp [w]
    simp
    omega
  · intro g hg
    dsimp [w] at hg
    simp at hg
    rcases hg with rfl | hgP
    · exact Or.inr hpSqMem
    · subst g
      exact Or.inl hpPrimeMem
  · rw [htEq, rootQuotientWordProduct_eq_prod]
    dsimp [w]
    simp only [List.prod_append, List.prod_replicate, List.prod_cons,
      List.prod_nil, mul_one]
    rw [← pow_add]
    congr 1
    omega

/-- Pure-prime hard targets are prime-hard at horizon `h`. -/
theorem hardPrimeTarget_not_reachable_prime
    {N h t : ℕ}
    (ht : t ∈ RootQuotientHardPrimeTargetFinset N h) :
    ¬RootQuotientProductReachableWithin h (RootQuotientPrimeBasis N) t := by
  obtain ⟨p, hpHard, htEq⟩ :=
    (exists_unique_hardPrimeDirection_of_mem_targetFinset ht).exists
  intro hReach
  have hCostLe :=
    (rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le
      (by positivity : 1 ≤ p ^ (h + 1)) hpHard.2).1
      (by simpa [htEq] using hReach)
  have hpCount : rootQuotientPrimeFactorCount p = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hpHard.1]
    simp
  have hPowCount : rootQuotientPrimeFactorCount (p ^ (h + 1)) = h + 1 := by
    rw [rootQuotientPrimeFactorCount_pow hpHard.1.one_le, hpCount]
    simp
  rw [hPowCount] at hCostLe
  omega

/-- Any divisor cover of the hard pure-prime targets needs at least one distinct
macro type per hard prime direction. -/
theorem hardDirection_ncard_le_hardTargetRepairCoverNumber
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    (RootQuotientHardPrimeDirections N h).ncard ≤
      rootQuotientRepairDivisorCoverNumber
        (RootQuotientHardPrimeTargetFinset N h)
        (RootQuotientSemanticCompositeCandidates r N) := by
  have hSquare := hardPrimeSquareMacroSet_repairs_hardPrimeTargets
    hr hh hBinary
  have hCoverFeasible : ∃ S : Set ℕ,
      S.Finite ∧
      RootQuotientRepairDivisorCover
        (RootQuotientHardPrimeTargetFinset N h)
        (RootQuotientSemanticCompositeCandidates r N) S := by
    refine ⟨RootQuotientHardPrimeSquareMacroSet N h,
      hSquare.1, hSquare.2.1, ?_⟩
    intro t ht
    obtain ⟨p, hpHard, htEq⟩ :=
      (exists_unique_hardPrimeDirection_of_mem_targetFinset ht).exists
    exact ⟨p ^ 2, ⟨p, hpHard, rfl⟩, by
      rw [htEq]
      exact pow_dvd_pow p (by omega)⟩
  obtain ⟨S, hSFinite, hCover, hSCard⟩ :=
    exists_minimumRepairDivisorCover hCoverFeasible
  have hServe : ∀ p : ℕ,
      p ∈ RootQuotientHardPrimeDirections N h →
      ∃ g : ℕ, g ∈ S ∧ RootQuotientMacroServesPrimeDirection g p := by
    intro p hpHard
    have ht : p ^ (h + 1) ∈ RootQuotientHardPrimeTargetFinset N h := by
      dsimp [RootQuotientHardPrimeTargetFinset]
      exact Finset.mem_image.2 ⟨p,
        (mem_rootQuotientHardPrimeDirectionFinset_iff).2 hpHard, rfl⟩
    obtain ⟨g, hgS, hgDvd⟩ := hCover.2 (p ^ (h + 1)) ht
    have hgCandidate := hCover.1 hgS
    exact ⟨g, hgS,
      macroServesPrimeDirection_of_dvd_primePow
        hpHard.1 hgCandidate.1.1 hgDvd⟩
  let H := RootQuotientHardPrimeDirections N h
  let f : ℕ → ℕ := fun p =>
    if hp : p ∈ H then Classical.choose (hServe p hp) else 1
  have hfSpec : ∀ p : ℕ, (hp : p ∈ H) →
      f p ∈ S ∧ RootQuotientMacroServesPrimeDirection (f p) p := by
    intro p hp
    dsimp [f]
    rw [dif_pos hp]
    exact Classical.choose_spec (hServe p hp)
  have hInj : Set.InjOn f H := by
    intro p hp q hq hEq
    exact primeDirection_eq_of_macro_serves_both
      hp.1 hq.1 (hfSpec p hp).2 (hEq ▸ (hfSpec q hq).2)
  have hCardLe : H.ncard ≤ S.ncard :=
    Set.ncard_le_ncard_of_injOn f
      (fun p hp => (hfSpec p hp).1) hInj hSFinite
  rw [hSCard] at hCardLe
  exact hCardLe

/-- **Pure-direction repair is exact at the divisor-cover level.** -/
theorem hardTargetRepairCoverNumber_eq_direction_ncard
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientRepairDivisorCoverNumber
        (RootQuotientHardPrimeTargetFinset N h)
        (RootQuotientSemanticCompositeCandidates r N) =
      (RootQuotientHardPrimeDirections N h).ncard := by
  apply Nat.le_antisymm
  · have hSquare := hardPrimeSquareMacroSet_repairs_hardPrimeTargets
      hr hh hBinary
    have hCover : RootQuotientRepairDivisorCover
        (RootQuotientHardPrimeTargetFinset N h)
        (RootQuotientSemanticCompositeCandidates r N)
        (RootQuotientHardPrimeSquareMacroSet N h) := by
      refine ⟨hSquare.2.1, ?_⟩
      intro t ht
      obtain ⟨p, hpHard, htEq⟩ :=
        (exists_unique_hardPrimeDirection_of_mem_targetFinset ht).exists
      exact ⟨p ^ 2, ⟨p, hpHard, rfl⟩, by
        rw [htEq]
        exact pow_dvd_pow p (by omega)⟩
    have hLe := rootQuotientRepairDivisorCoverNumber_le hSquare.1 hCover
    rw [hardPrimeSquareMacroSet_ncard_eq_direction_ncard] at hLe
    exact hLe
  · exact hardDirection_ncard_le_hardTargetRepairCoverNumber hr hh hBinary

/-- **Pure-direction exact repair storage equals the hard-direction count.** -/
theorem hardTargetMinimumRelativeRepairStorage_eq_direction_ncard
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientMinimumRelativeRepairStorage
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientHardPrimeTargetFinset N h)
        (RootQuotientSemanticCompositeCandidates r N) =
      (RootQuotientHardPrimeDirections N h).ncard := by
  have hFeasible : ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation
        (RootQuotientPrimeBasis N) h
        (RootQuotientHardPrimeTargetFinset N h)
        (RootQuotientSemanticCompositeCandidates r N) S :=
    ⟨RootQuotientHardPrimeSquareMacroSet N h,
      hardPrimeSquareMacroSet_repairs_hardPrimeTargets hr hh hBinary⟩
  have hNoBase : ∀ t ∈ RootQuotientHardPrimeTargetFinset N h,
      ¬RootQuotientProductReachableWithin h (RootQuotientPrimeBasis N) t := by
    intro t ht
    exact hardPrimeTarget_not_reachable_prime ht
  have hLower := repairDivisorCoverNumber_le_minimumRelativeRepairStorage
    hNoBase hFeasible
  rw [hardTargetRepairCoverNumber_eq_direction_ncard hr hh hBinary] at hLower
  have hUpper := rootQuotientMinimumRelativeRepairStorage_le
    (hardPrimeSquareMacroSet_repairs_hardPrimeTargets hr hh hBinary)
  rw [hardPrimeSquareMacroSet_ncard_eq_direction_ncard] at hUpper
  exact Nat.le_antisymm hUpper hLower

/-- The pure-direction repair relaxation gap vanishes identically. -/
theorem hardTarget_repairRelaxationGap_eq_zero
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientRepairRelaxationGap
      (RootQuotientPrimeBasis N) h
      (RootQuotientHardPrimeTargetFinset N h)
      (RootQuotientSemanticCompositeCandidates r N) = 0 := by
  have hFeasible : ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation
        (RootQuotientPrimeBasis N) h
        (RootQuotientHardPrimeTargetFinset N h)
        (RootQuotientSemanticCompositeCandidates r N) S :=
    ⟨RootQuotientHardPrimeSquareMacroSet N h,
      hardPrimeSquareMacroSet_repairs_hardPrimeTargets hr hh hBinary⟩
  have hNoBase : ∀ t ∈ RootQuotientHardPrimeTargetFinset N h,
      ¬RootQuotientProductReachableWithin h (RootQuotientPrimeBasis N) t := by
    intro t ht
    exact hardPrimeTarget_not_reachable_prime ht
  apply (repairRelaxationGap_eq_zero_iff hNoBase hFeasible).2
  rw [hardTargetMinimumRelativeRepairStorage_eq_direction_ncard hr hh hBinary]
  rw [hardTargetRepairCoverNumber_eq_direction_ncard hr hh hBinary]

end EnterpriseMath.Quotient
