import EnterpriseMath.Quotient.RootQuotientFourLayerResourceEvents
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The newly exposed state can extend some old maximum divisor-incompatibility
packing without breaking incompatibility under the enlarged candidate set. -/
def RootQuotientGlobalRepairPackingExtendable
    (r N h : ℕ) : Prop :=
  N + 1 ∈ RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h ∧
  ∃ U : Finset ℕ,
    U ⊆ RootQuotientPrimeHardSemanticTargetFinset r N h ∧
    RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r N) U ∧
    U.card = rootQuotientGlobalRepairDivisorPackingNumber r N h ∧
    RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r (N + 1))
      (insert (N + 1) U)

/-- Every old hard target is at most the old state bound. -/
theorem mem_primeHardSemanticTargetFinset_le_stateBound
    {r N h t : ℕ}
    (ht : t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h) :
    t ≤ N :=
  ((mem_primeHardSemanticTargetFinset_iff).1 ht).1.2.1

/-- The new state is not contained in any old target subfamily. -/
theorem succ_not_mem_old_primeHard_subfamily
    {r N h : ℕ} {U : Finset ℕ}
    (hUT : U ⊆ RootQuotientPrimeHardSemanticTargetFinset r N h) :
    N + 1 ∉ U := by
  intro hMem
  have hLe := mem_primeHardSemanticTargetFinset_le_stateBound (hUT hMem)
  omega

/-- **Packing extendability forces a packing jump.** -/
theorem packingEvent_one_of_globalRepairPackingExtendable
    {r N h : ℕ}
    (hExt : RootQuotientGlobalRepairPackingExtendable r N h) :
    (rootQuotientFourLayerResourceEvent r N h).packing = 1 := by
  obtain ⟨_hNewHard, U, hUT, _hPackOld, hUCard, hPackNew⟩ := hExt
  have hNewNot : N + 1 ∉ U :=
    succ_not_mem_old_primeHard_subfamily hUT
  have hInsertCard : (insert (N + 1) U).card = U.card + 1 :=
    Finset.card_insert_of_notMem hNewNot
  have hInsertSub : insert (N + 1) U ⊆
      RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h := by
    intro t ht
    simp at ht
    rcases ht with rfl | htU
    · exact hExt.1
    · exact primeHardSemanticTargetFinset_mono_stateBound
        (r := r) (h := h) (Nat.le_succ N) (hUT htU)
  have hLower := repairDivisorPacking_card_le_number hInsertSub hPackNew
  rw [hInsertCard, hUCard] at hLower
  have hStep := globalRepairDivisorPackingNumber_succ_staircase r N h
  dsimp [rootQuotientFourLayerResourceEvent]
  omega

/-- If a next-state maximum packing omits the newly exposed state, it is already
an old-state packing. -/
theorem next_packing_omitting_succ_is_old_packing
    {r N h : ℕ} {U : Finset ℕ}
    (hUT : U ⊆ RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
    (hNewNot : N + 1 ∉ U)
    (hPack : RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r (N + 1)) U) :
    U ⊆ RootQuotientPrimeHardSemanticTargetFinset r N h ∧
    RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r N) U := by
  have hOldTargets : U ⊆ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    intro t ht
    have htNew := (mem_primeHardSemanticTargetFinset_iff).1 (hUT ht)
    have htNe : t ≠ N + 1 := by
      intro hEq
      subst t
      exact hNewNot ht
    have htN : t ≤ N := by omega
    exact (mem_primeHardSemanticTargetFinset_iff).2
      ⟨⟨htNew.1.1, htN, htNew.1.2.2⟩, htNew.2⟩
  have hPackOld : RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r N) U := by
    intro g hgOld t ht u hu hgT hgU
    have hgNew := semanticCompositeCandidates_mono_stateBound
      (r := r) (Nat.le_succ N) hgOld
    exact hPack g hgNew t ht u hu hgT hgU
  exact ⟨hOldTargets, hPackOld⟩

/-- **Packing jump forces extendability.**

If the packing staircase rises by one, every next-state maximum packing must use
the new state; deleting it leaves an old maximum packing, so the new state
extends an old optimum. -/
theorem globalRepairPackingExtendable_of_packingEvent_one
    {r N h : ℕ}
    (hNewHard : N + 1 ∈ RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
    (hEvent : (rootQuotientFourLayerResourceEvent r N h).packing = 1) :
    RootQuotientGlobalRepairPackingExtendable r N h := by
  classical
  obtain ⟨U, hUT, hPackNew, hUCard⟩ :=
    exists_maximumRepairDivisorPacking
      (RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
      (RootQuotientSemanticCompositeCandidates r (N + 1))
  have hStep := globalRepairDivisorPackingNumber_succ_staircase r N h
  have hNextEq : rootQuotientGlobalRepairDivisorPackingNumber r (N + 1) h =
      rootQuotientGlobalRepairDivisorPackingNumber r N h + 1 := by
    dsimp [rootQuotientFourLayerResourceEvent] at hEvent
    omega
  have hNewMem : N + 1 ∈ U := by
    by_contra hNot
    have hOld := next_packing_omitting_succ_is_old_packing hUT hNot hPackNew
    have hOldBound := repairDivisorPacking_card_le_number hOld.1 hOld.2
    rw [hUCard, hNextEq] at hOldBound
    omega
  let U₀ := U.erase (N + 1)
  have hEraseCard : U₀.card + 1 = U.card := by
    dsimp [U₀]
    exact Finset.card_erase_add_one hNewMem
  have hU₀Old : U₀ ⊆ RootQuotientPrimeHardSemanticTargetFinset r N h := by
    intro t ht
    have htErase := Finset.mem_erase.1 ht
    have htU : t ∈ U := htErase.2
    have htNe : t ≠ N + 1 := htErase.1
    have htNew := (mem_primeHardSemanticTargetFinset_iff).1 (hUT htU)
    have htN : t ≤ N := by omega
    exact (mem_primeHardSemanticTargetFinset_iff).2
      ⟨⟨htNew.1.1, htN, htNew.1.2.2⟩, htNew.2⟩
  have hU₀PackOld : RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r N) U₀ := by
    intro g hgOld t ht u hu hgT hgU
    have htU := (Finset.mem_erase.1 ht).2
    have huU := (Finset.mem_erase.1 hu).2
    have hgNew := semanticCompositeCandidates_mono_stateBound
      (r := r) (Nat.le_succ N) hgOld
    exact hPackNew g hgNew t htU u huU hgT hgU
  have hU₀Card : U₀.card = rootQuotientGlobalRepairDivisorPackingNumber r N h := by
    rw [hUCard, hNextEq] at hEraseCard
    omega
  have hInsertEq : insert (N + 1) U₀ = U := by
    dsimp [U₀]
    exact Finset.insert_erase hNewMem
  refine ⟨hNewHard, U₀, hU₀Old, hU₀PackOld, hU₀Card, ?_⟩
  rw [hInsertEq]
  exact hPackNew

/-- **Exact packing-jump characterization at a newly hard state.** -/
theorem packingEvent_one_iff_globalRepairPackingExtendable
    {r N h : ℕ}
    (hNewHard : N + 1 ∈ RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h) :
    (rootQuotientFourLayerResourceEvent r N h).packing = 1 ↔
      RootQuotientGlobalRepairPackingExtendable r N h := by
  constructor
  · exact globalRepairPackingExtendable_of_packingEvent_one hNewHard
  · exact packingEvent_one_of_globalRepairPackingExtendable

/-- Binary packing-extension indicator. -/
noncomputable def rootQuotientPackingExtensionIndicator
    (r N h : ℕ) : ℕ :=
  if RootQuotientGlobalRepairPackingExtendable r N h then 1 else 0

@[simp]
theorem packingExtensionIndicator_eq_one_iff
    {r N h : ℕ} :
    rootQuotientPackingExtensionIndicator r N h = 1 ↔
      RootQuotientGlobalRepairPackingExtendable r N h := by
  classical
  unfold rootQuotientPackingExtensionIndicator
  by_cases hExt : RootQuotientGlobalRepairPackingExtendable r N h <;>
    simp [hExt]

/-- At a newly hard state, the packing event coordinate is exactly the packing
extension indicator. -/
theorem packingEvent_eq_packingExtensionIndicator_of_newHard
    {r N h : ℕ}
    (hNewHard : N + 1 ∈ RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h) :
    (rootQuotientFourLayerResourceEvent r N h).packing =
      rootQuotientPackingExtensionIndicator r N h := by
  classical
  have hBits := globalRepairDivisorPackingNumber_succ_staircase r N h
  unfold rootQuotientPackingExtensionIndicator
  by_cases hExt : RootQuotientGlobalRepairPackingExtendable r N h
  · simp [hExt]
    exact (packingEvent_one_iff_globalRepairPackingExtendable hNewHard).2 hExt
  · simp [hExt]
    have hNotOne : (rootQuotientFourLayerResourceEvent r N h).packing ≠ 1 := by
      intro hOne
      exact hExt ((packingEvent_one_iff_globalRepairPackingExtendable hNewHard).1 hOne)
    dsimp [rootQuotientFourLayerResourceEvent] at hNotOne ⊢
    omega

end EnterpriseMath.Quotient
