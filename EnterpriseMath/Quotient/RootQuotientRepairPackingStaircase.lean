import EnterpriseMath.Quotient.RootQuotientFourLayerStorageDecomposition
import EnterpriseMath.Quotient.RootQuotientResourceStaircase
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Global repair packing cannot decrease when one more state is exposed. -/
theorem globalRepairDivisorPackingNumber_mono_succ
    {r N h : ℕ} :
    rootQuotientGlobalRepairDivisorPackingNumber r N h ≤
      rootQuotientGlobalRepairDivisorPackingNumber r (N + 1) h := by
  obtain ⟨U, hUT, hPack, hUCard⟩ :=
    exists_maximumRepairDivisorPacking
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N)
  have hUTNew : U ⊆ RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h := by
    intro t ht
    exact primeHardSemanticTargetFinset_mono_stateBound
      (r := r) (h := h) (Nat.le_succ N) (hUT ht)
  have hPackNew : RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r (N + 1)) U := by
    intro g hgNew t ht u hu hgT hgU
    have htOld := (mem_primeHardSemanticTargetFinset_iff).1 (hUT ht)
    have hgLeT : g ≤ t := Nat.le_of_dvd (by omega) hgT
    have hgOld : g ∈ RootQuotientSemanticCompositeCandidates r N := by
      refine ⟨⟨hgNew.1.1, hgLeT.trans htOld.1.2.1, hgNew.1.2.2⟩, ?_⟩
      intro hgPrimeOld
      exact hgNew.2 ⟨hgPrimeOld.1, hgNew.1.2.1⟩
    exact hPack g hgOld t ht u hu hgT hgU
  have hLe := repairDivisorPacking_card_le_number hUTNew hPackNew
  rw [hUCard] at hLe
  exact hLe

/-- Removing the newly exposed target from a next-state maximum packing leaves
an old-state packing; hence the packing number can rise by at most one. -/
theorem globalRepairDivisorPackingNumber_succ_le_add_one
    {r N h : ℕ} :
    rootQuotientGlobalRepairDivisorPackingNumber r (N + 1) h ≤
      rootQuotientGlobalRepairDivisorPackingNumber r N h + 1 := by
  classical
  obtain ⟨U, hUT, hPack, hUCard⟩ :=
    exists_maximumRepairDivisorPacking
      (RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
      (RootQuotientSemanticCompositeCandidates r (N + 1))
  let U₀ := U.erase (N + 1)
  have hU₀Old : U₀ ⊆ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    intro t ht
    have htErase := Finset.mem_erase.1 ht
    have htNe : t ≠ N + 1 := htErase.1
    have htU : t ∈ U := htErase.2
    have htNew := (mem_primeHardSemanticTargetFinset_iff).1 (hUT htU)
    have htN : t ≤ N := by omega
    exact (mem_primeHardSemanticTargetFinset_iff).2
      ⟨⟨htNew.1.1, htN, htNew.1.2.2⟩, htNew.2⟩
  have hPackOld : RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r N) U₀ := by
    intro g hgOld t ht u hu hgT hgU
    have htErase := Finset.mem_erase.1 ht
    have huErase := Finset.mem_erase.1 hu
    have htU : t ∈ U := htErase.2
    have huU : u ∈ U := huErase.2
    have hgNew := semanticCompositeCandidates_mono_stateBound
      (r := r) (Nat.le_succ N) hgOld
    exact hPack g hgNew t htU u huU hgT hgU
  have hOldLe := repairDivisorPacking_card_le_number hU₀Old hPackOld
  have hErase : U.card ≤ U₀.card + 1 := by
    by_cases hMem : N + 1 ∈ U
    · have hEq := Finset.card_erase_add_one hMem
      dsimp [U₀]
      omega
    · dsimp [U₀]
      rw [Finset.erase_eq_of_notMem hMem]
      omega
  rw [hUCard]
  omega

/-- **Global divisor packing is a unit-step staircase in state bound.** -/
theorem globalRepairDivisorPackingNumber_succ_staircase
    (r N h : ℕ) :
    rootQuotientGlobalRepairDivisorPackingNumber r N h ≤
      rootQuotientGlobalRepairDivisorPackingNumber r (N + 1) h ∧
    rootQuotientGlobalRepairDivisorPackingNumber r (N + 1) h ≤
      rootQuotientGlobalRepairDivisorPackingNumber r N h + 1 :=
  ⟨globalRepairDivisorPackingNumber_mono_succ,
    globalRepairDivisorPackingNumber_succ_le_add_one⟩

end EnterpriseMath.Quotient
