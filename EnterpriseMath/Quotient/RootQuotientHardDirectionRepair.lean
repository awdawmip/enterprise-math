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

/-- Pure-prime hard targets `p^(h+1)` associated with every hard prime
direction. -/
noncomputable def RootQuotientHardPrimeTargetFinset
    (N h : ℕ) : Finset ℕ :=
  (RootQuotientHardPrimeDirectionFinset N h).image
    (fun p => p ^ (h + 1))

/-- Distinct hard prime directions give distinct pure-prime targets. -/
theorem hardPrimeTargetMap_injective
    {h : ℕ} :
    Set.InjOn (fun p : ℕ => p ^ (h + 1)) {p : ℕ | p.Prime} := by
  intro p hp q hq hEq
  have hpTwo : 2 ≤ p := hp.two_le
  have hqTwo : 2 ≤ q := hq.two_le
  exact Nat.pow_left_injective (by omega) (by omega) hEq

/-- Hard-target cardinality equals hard-direction cardinality. -/
theorem hardPrimeTargetFinset_card_eq_direction_ncard
    (N h : ℕ) :
    (RootQuotientHardPrimeTargetFinset N h).card =
      (RootQuotientHardPrimeDirections N h).ncard := by
  classical
  let H := RootQuotientHardPrimeDirectionFinset N h
  have hInj : Set.InjOn (fun p : ℕ => p ^ (h + 1)) (H : Set ℕ) := by
    intro p hp q hq hEq
    apply hardPrimeTargetMap_injective
    · exact ((mem_rootQuotientHardPrimeDirectionFinset_iff).1
        (by simpa using hp)).1
    · exact ((mem_rootQuotientHardPrimeDirectionFinset_iff).1
        (by simpa using hq)).1
    · exact hEq
  have hCardImage :
      (H.image (fun p => p ^ (h + 1))).card = H.card :=
    Finset.card_image_iff.mpr fun p hp q hq hEq => by
      exact hInj (by simpa using hp) (by simpa using hq) hEq
  dsimp [RootQuotientHardPrimeTargetFinset]
  rw [hCardImage]
  simpa [H, RootQuotientHardPrimeDirectionFinset] using
    (rootQuotientHardPrimeDirections_finite N h).ncard

/-- A hard target remembers its unique prime direction. -/
theorem exists_unique_hardPrimeDirection_of_mem_targetFinset
    {N h t : ℕ}
    (ht : t ∈ RootQuotientHardPrimeTargetFinset N h) :
    ∃! p : ℕ,
      p ∈ RootQuotientHardPrimeDirections N h ∧
      t = p ^ (h + 1) := by
  classical
  have htImage := Finset.mem_image.1 ht
  obtain ⟨p, hpFin, hpEq⟩ := htImage
  have hpHard : p ∈ RootQuotientHardPrimeDirections N h :=
    (mem_rootQuotientHardPrimeDirectionFinset_iff).1 hpFin
  refine ⟨p, ⟨hpHard, hpEq.symm⟩, ?_⟩
  intro q hq
  have hPowEq : p ^ (h + 1) = q ^ (h + 1) := by
    rw [← hpEq, hq.2]
  exact hardPrimeTargetMap_injective hpHard.1 hq.1.1 hPowEq

/-- In the high-root regime, `p^2` is an admissible semantic composite macro
for every hard direction `p` at every positive horizon. -/
theorem prime_square_mem_semanticCompositeCandidates_of_hard
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r)
    (hpHard : p ∈ RootQuotientHardPrimeDirections N h) :
    p ^ 2 ∈ RootQuotientSemanticCompositeCandidates r N := by
  have hpPrime : p.Prime := hpHard.1
  have hPowLe : p ^ 2 ≤ p ^ (h + 1) :=
    Nat.pow_le_pow_right hpPrime.one_le (by omega)
  have hpSqLeN : p ^ 2 ≤ N := hPowLe.trans hpHard.2
  have hpSqPos : 1 ≤ p ^ 2 := by positivity
  have hpSqFree : RPowerFree r (p ^ 2) :=
    rPowerFree_of_lt_two_pow_rootOrder hpSqPos (hpSqLeN.trans_lt hBinary)
  refine ⟨⟨by positivity, hpSqLeN, hpSqFree⟩, ?_⟩
  intro hpSqPrime
  exact hpSqPrime.1.not_dvd_one (by
    have hpDvdSq : p ∣ p ^ 2 := dvd_pow_self p (by omega)
    have hpDvdP : p ∣ p := dvd_rfl
    exact (hpSqPrime.1.dvd_mul.mp (by simpa [pow_two] using hpDvdSq)).resolve_left
      (by omega))

/-- Canonical square macro family for all hard prime directions. -/
noncomputable def RootQuotientHardPrimeSquareMacroSet
    (N h : ℕ) : Set ℕ :=
  {g : ℕ | ∃ p : ℕ,
    p ∈ RootQuotientHardPrimeDirections N h ∧ g = p ^ 2}

/-- The hard-prime-square family has exactly one macro type per hard direction. -/
theorem hardPrimeSquareMacroSet_ncard_eq_direction_ncard
    (N h : ℕ) :
    (RootQuotientHardPrimeSquareMacroSet N h).ncard =
      (RootQuotientHardPrimeDirections N h).ncard := by
  classical
  let H := RootQuotientHardPrimeDirectionFinset N h
  have hEq : RootQuotientHardPrimeSquareMacroSet N h =
      ((H.image (fun p => p ^ 2) : Finset ℕ) : Set ℕ) := by
    ext g
    constructor
    · rintro ⟨p, hpHard, rfl⟩
      have hpFin : p ∈ H := by
        simpa [H] using
          (mem_rootQuotientHardPrimeDirectionFinset_iff).2 hpHard
      simpa using Finset.mem_image.2 ⟨p, hpFin, rfl⟩
    · intro hg
      have hgFin : g ∈ H.image (fun p => p ^ 2) := by simpa using hg
      obtain ⟨p, hpFin, rfl⟩ := Finset.mem_image.1 hgFin
      exact ⟨p,
        (mem_rootQuotientHardPrimeDirectionFinset_iff).1 (by simpa [H] using hpFin),
        rfl⟩
  rw [hEq]
  have hInj : Set.InjOn (fun p : ℕ => p ^ 2) (H : Set ℕ) := by
    intro p hp q hq hEqPow
    have hpPrime := ((mem_rootQuotientHardPrimeDirectionFinset_iff).1
      (by simpa [H] using hp)).1
    have hqPrime := ((mem_rootQuotientHardPrimeDirectionFinset_iff).1
      (by simpa [H] using hq)).1
    exact hardPrimeTargetMap_injective hpPrime hqPrime (by simpa using hEqPow)
  have hCard : (H.image (fun p => p ^ 2)).card = H.card :=
    Finset.card_image_iff.mpr fun p hp q hq hEqPow =>
      hInj (by simpa using hp) (by simpa using hq) hEqPow
  simpa [H, RootQuotientHardPrimeDirectionFinset, hCard] using
    (rootQuotientHardPrimeDirections_finite N h).ncard

/-- The prime-square family is an exact relative repair presentation of all hard
pure-prime targets at positive horizon. -/
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
  have hFinite : (RootQuotientHardPrimeSquareMacroSet N h).Finite := by
    apply Set.Finite.image
      (rootQuotientHardPrimeDirections_finite N h)
      (fun p => p ^ 2)
  refine ⟨hFinite, ?_, ?_⟩
  · intro g hg
    obtain ⟨p, hpHard, rfl⟩ := hg
    exact prime_square_mem_semanticCompositeCandidates_of_hard
      hr hh hBinary hpHard
  · intro t ht
    obtain ⟨p, hpHard, htEq⟩ :=
      (exists_unique_hardPrimeDirection_of_mem_targetFinset ht).exists
    have hpLeN : p ≤ N := by
      have hpLePow : p ≤ p ^ (h + 1) := by
        calc
          p = p ^ 1 := by simp
          _ ≤ p ^ (h + 1) := Nat.pow_le_pow_right hpHard.1.one_le (by omega)
      exact hpLePow.trans hpHard.2
    have hpPrimeMem : p ∈ RootQuotientPrimeBasis N := ⟨hpHard.1, hpLeN⟩
    have hpSqMem : p ^ 2 ∈ RootQuotientHardPrimeSquareMacroSet N h :=
      ⟨p, hpHard, rfl⟩
    let u : List ℕ := [p ^ 2]
    let v : List ℕ := List.replicate (h - 1) p
    let w := u ++ v
    refine ⟨w, ?_, ?_, ?_⟩
    · dsimp [w, u, v]
      simp
      omega
    · intro g hg
      dsimp [w, u, v] at hg
      simp at hg
      rcases hg with rfl | hgP
      · exact Or.inr hpSqMem
      · subst g
        exact Or.inl hpPrimeMem
    · rw [htEq]
      dsimp [w, u, v]
      rw [rootQuotientWordProduct_eq_prod]
      simp [List.prod_append, List.prod_replicate, pow_add]
      congr 1
      omega

/-- Pure-prime hard targets are all prime-hard at horizon `h`. -/
theorem hardPrimeTarget_not_reachable_prime
    {N h t : ℕ}
    (ht : t ∈ RootQuotientHardPrimeTargetFinset N h) :
    ¬RootQuotientProductReachableWithin h (RootQuotientPrimeBasis N) t := by
  obtain ⟨p, hpHard, htEq⟩ :=
    (exists_unique_hardPrimeDirection_of_mem_targetFinset ht).exists
  intro hReach
  have hpLeN : p ≤ N := by
    have hpLePow : p ≤ p ^ (h + 1) := by
      calc
        p = p ^ 1 := by simp
        _ ≤ p ^ (h + 1) := Nat.pow_le_pow_right hpHard.1.one_le (by omega)
    exact hpLePow.trans hpHard.2
  have hCostLe :=
    (rootQuotientPrimeBasis_reachableWithin_iff_factorCount_le
      (by positivity : 1 ≤ p ^ (h + 1)) hpHard.2).1 (by simpa [htEq] using hReach)
  have hpCount : rootQuotientPrimeFactorCount p = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hpHard.1]
    simp
  have hPowCount : rootQuotientPrimeFactorCount (p ^ (h + 1)) = h + 1 := by
    rw [rootQuotientPrimeFactorCount_pow hpHard.1.one_le, hpCount]
    simp
  rw [hPowCount] at hCostLe
  omega

/-- The first-order divisor-cover number of hard pure-prime targets is at least
the hard-direction count. -/
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
  have hFeasible : ∃ S : Set ℕ,
      S.Finite ∧
      RootQuotientRepairDivisorCover
        (RootQuotientHardPrimeTargetFinset N h)
        (RootQuotientSemanticCompositeCandidates r N)
        S := by
    let S := RootQuotientHardPrimeSquareMacroSet N h
    refine ⟨S, hSquare.1, ?_⟩
    constructor
    · exact hSquare.2.1
    · intro t ht
      obtain ⟨p, hpHard, htEq⟩ :=
        (exists_unique_hardPrimeDirection_of_mem_targetFinset ht).exists
      exact ⟨p ^ 2, ⟨p, hpHard, rfl⟩, by
        rw [htEq]
        exact pow_dvd_pow p (by omega)⟩
  obtain ⟨S, hSFinite, hCover, hSCard⟩ :=
    exists_minimumRepairDivisorCover hFeasible
  have hServe : ∀ p : ℕ, p ∈ RootQuotientHardPrimeDirections N h →
      ∃ g : ℕ, g ∈ S ∧ RootQuotientMacroServesPrimeDirection g p := by
    intro p hpHard
    have ht : p ^ (h + 1) ∈ RootQuotientHardPrimeTargetFinset N h := by
      dsimp [RootQuotientHardPrimeTargetFinset]
      apply Finset.mem_image.2
      exact ⟨p,
        (mem_rootQuotientHardPrimeDirectionFinset_iff).2 hpHard,
        rfl⟩
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

/-- **Pure-direction repair is exact at the divisor-cover level.**

For hard prime-power targets, the divisor-cover number is exactly the number of
hard prime directions. -/
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
      constructor
      · exact hSquare.2.1
      · intro t ht
        obtain ⟨p, hpHard, htEq⟩ :=
          (exists_unique_hardPrimeDirection_of_mem_targetFinset ht).exists
        exact ⟨p ^ 2, ⟨p, hpHard, rfl⟩, by
          rw [htEq]
          exact pow_dvd_pow p (by omega)⟩
    have hLe := rootQuotientRepairDivisorCoverNumber_le hSquare.1 hCover
    rw [hardPrimeSquareMacroSet_ncard_eq_direction_ncard] at hLe
    exact hLe
  · exact hardDirection_ncard_le_hardTargetRepairCoverNumber hr hh hBinary

/-- **Pure-direction exact repair storage equals the direction demand.** -/
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
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientHardPrimeTargetFinset N h)
        (RootQuotientSemanticCompositeCandidates r N)
        S :=
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
      (RootQuotientPrimeBasis N)
      h
      (RootQuotientHardPrimeTargetFinset N h)
      (RootQuotientSemanticCompositeCandidates r N) = 0 := by
  have hFeasible : ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientHardPrimeTargetFinset N h)
        (RootQuotientSemanticCompositeCandidates r N)
        S :=
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
