import EnterpriseMath.Quotient.RootQuotientPrimeBirthDominance
import EnterpriseMath.Quotient.RootQuotientHardDirectionRepair
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A finite target subfamily is a divisor-incompatibility packing relative to
candidate set `C` when no admissible candidate macro can divide two distinct
packed targets. -/
def RootQuotientRepairDivisorPacking
    (C : Set ℕ) (U : Finset ℕ) : Prop :=
  ∀ g : ℕ, g ∈ C →
    ∀ t ∈ U, ∀ u ∈ U,
      g ∣ t → g ∣ u → t = u

/-- Feasible cardinalities of divisor-incompatibility packings inside `T`. -/
def RootQuotientRepairDivisorPackingCardinalities
    (T : Finset ℕ) (C : Set ℕ) : Set ℕ :=
  {m : ℕ | ∃ U : Finset ℕ,
    U ⊆ T ∧ RootQuotientRepairDivisorPacking C U ∧ U.card = m}

/-- Maximum divisor-incompatibility packing size, implemented as the greatest
feasible cardinality not exceeding `|T|`. -/
noncomputable def rootQuotientRepairDivisorPackingNumber
    (T : Finset ℕ) (C : Set ℕ) : ℕ :=
  Nat.findGreatest
    (fun m => m ∈ RootQuotientRepairDivisorPackingCardinalities T C)
    T.card

/-- The empty target set is always a repair packing. -/
theorem zero_mem_repairDivisorPackingCardinalities
    (T : Finset ℕ) (C : Set ℕ) :
    0 ∈ RootQuotientRepairDivisorPackingCardinalities T C := by
  exact ⟨∅, by simp, by simp [RootQuotientRepairDivisorPacking], by simp⟩

/-- Every feasible packing cardinality is bounded by the packing number. -/
theorem repairDivisorPacking_card_le_number
    {T U : Finset ℕ} {C : Set ℕ}
    (hUT : U ⊆ T)
    (hPack : RootQuotientRepairDivisorPacking C U) :
    U.card ≤ rootQuotientRepairDivisorPackingNumber T C := by
  unfold rootQuotientRepairDivisorPackingNumber
  apply Nat.le_findGreatest
  · exact Finset.card_le_card hUT
  · exact ⟨U, hUT, hPack, rfl⟩

/-- The maximum packing cardinality is attained by an actual finite packed
subfamily. -/
theorem exists_maximumRepairDivisorPacking
    (T : Finset ℕ) (C : Set ℕ) :
    ∃ U : Finset ℕ,
      U ⊆ T ∧
      RootQuotientRepairDivisorPacking C U ∧
      U.card = rootQuotientRepairDivisorPackingNumber T C := by
  have hSpec :
      rootQuotientRepairDivisorPackingNumber T C ∈
        RootQuotientRepairDivisorPackingCardinalities T C := by
    exact Nat.findGreatest_spec
      (P := fun m => m ∈ RootQuotientRepairDivisorPackingCardinalities T C)
      (m := 0) (n := T.card) (Nat.zero_le _)
      (zero_mem_repairDivisorPackingCardinalities T C)
  exact hSpec

/-- **Packing lower bound for every divisor cover.**

A divisor-incompatibility packing of `k` targets forces at least `k` distinct
stored candidate types in any divisor cover. -/
theorem repairDivisorPacking_card_le_cover_ncard
    {T U : Finset ℕ} {C S : Set ℕ}
    (hUT : U ⊆ T)
    (hPack : RootQuotientRepairDivisorPacking C U)
    (hSFinite : S.Finite)
    (hCover : RootQuotientRepairDivisorCover T C S) :
    U.card ≤ S.ncard := by
  classical
  let f : ℕ → ℕ := fun t =>
    if ht : t ∈ U then
      Classical.choose (hCover.2 t (hUT ht))
    else 1
  have hfSpec : ∀ t : ℕ, (ht : t ∈ U) →
      f t ∈ S ∧ f t ∣ t := by
    intro t ht
    dsimp [f]
    rw [dif_pos ht]
    exact Classical.choose_spec (hCover.2 t (hUT ht))
  have hMaps : ∀ t : ℕ, t ∈ (U : Set ℕ) → f t ∈ S := by
    intro t ht
    exact (hfSpec t (by simpa using ht)).1
  have hInj : Set.InjOn f (U : Set ℕ) := by
    intro t ht u hu hEq
    have htU : t ∈ U := by simpa using ht
    have huU : u ∈ U := by simpa using hu
    have hft := hfSpec t htU
    have hfu := hfSpec u huU
    have hfuAsT : f t ∣ u := by rw [hEq]; exact hfu.2
    exact hPack (f t) (hCover.1 hft.1)
      t htU u huU hft.2 hfuAsT
  have hNcard := Set.ncard_le_ncard_of_injOn f hMaps hInj hSFinite
  simpa using hNcard

/-- Maximum packing size is a lower bound on the minimum divisor-cover size
whenever the cover problem is feasible. -/
theorem repairDivisorPackingNumber_le_coverNumber
    {T : Finset ℕ} {C : Set ℕ}
    (hFeasible : ∃ S : Set ℕ,
      S.Finite ∧ RootQuotientRepairDivisorCover T C S) :
    rootQuotientRepairDivisorPackingNumber T C ≤
      rootQuotientRepairDivisorCoverNumber T C := by
  obtain ⟨U, hUT, hPack, hUCard⟩ :=
    exists_maximumRepairDivisorPacking T C
  obtain ⟨S, hSFinite, hCover, hSCard⟩ :=
    exists_minimumRepairDivisorCover hFeasible
  have hLower := repairDivisorPacking_card_le_cover_ncard
    hUT hPack hSFinite hCover
  rw [hUCard, hSCard] at hLower
  exact hLower

/-- Global packing lower bound for the canonical prime-hard repair problem. -/
noncomputable def rootQuotientGlobalRepairDivisorPackingNumber
    (r N h : ℕ) : ℕ :=
  rootQuotientRepairDivisorPackingNumber
    (RootQuotientPrimeHardSemanticTargetFinset r N h)
    (RootQuotientSemanticCompositeCandidates r N)

/-- Hard pure-prime targets are pairwise divisor-incompatible for semantic
composite candidates: one composite integer cannot divide positive powers of
two different primes. -/
theorem hardPrimeTargets_are_repairDivisorPacking
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    RootQuotientRepairDivisorPacking
      (RootQuotientSemanticCompositeCandidates r N)
      (RootQuotientHardPrimeTargetFinset N h) := by
  intro g hgC t ht u hu hgT hgU
  obtain ⟨p, hpHard, htEq⟩ :=
    (exists_unique_hardPrimeDirection_of_mem_targetFinset ht).exists
  obtain ⟨q, hqHard, huEq⟩ :=
    (exists_unique_hardPrimeDirection_of_mem_targetFinset hu).exists
  have hgServeP : RootQuotientMacroServesPrimeDirection g p := by
    apply macroServesPrimeDirection_of_dvd_primePow hpHard.1 hgC.1.1
    simpa [htEq] using hgT
  have hgServeQ : RootQuotientMacroServesPrimeDirection g q := by
    apply macroServesPrimeDirection_of_dvd_primePow hqHard.1 hgC.1.1
    simpa [huEq] using hgU
  have hpq : p = q :=
    primeDirection_eq_of_macro_serves_both
      hpHard.1 hqHard.1 hgServeP hgServeQ
  rw [htEq, huEq, hpq]

/-- Pure-direction demand is a special divisor-packing lower bound on the full
prime-hard target family. -/
theorem primeDirectionDemand_le_globalRepairDivisorPackingNumber
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientPrimeDirectionDemand N h ≤
      rootQuotientGlobalRepairDivisorPackingNumber r N h := by
  have hSub : RootQuotientHardPrimeTargetFinset N h ⊆
      RootQuotientPrimeHardSemanticTargetFinset r N h :=
    hardPrimeTargetFinset_subset_primeHardSemanticTargetFinset hr hh hBinary
  have hLe := repairDivisorPacking_card_le_number
    (C := RootQuotientSemanticCompositeCandidates r N)
    hSub (hardPrimeTargets_are_repairDivisorPacking hr hh hBinary)
  rw [hardPrimeTargetFinset_card_eq_direction_ncard,
    hardPrimeDirections_ncard_eq_primeDirectionDemand] at hLe
  exact hLe

/-- **Four-layer canonical repair hierarchy.**

At positive horizon in the high-root regime:

`pure-direction demand <= divisor-packing <= divisor-cover <= exact storage`.
-/
theorem canonicalRepairFourLayerHierarchy
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hBinary : N < 2 ^ r) :
    rootQuotientPrimeDirectionDemand N h ≤
      rootQuotientGlobalRepairDivisorPackingNumber r N h ∧
    rootQuotientGlobalRepairDivisorPackingNumber r N h ≤
      rootQuotientGlobalRepairDivisorCoverNumber r N h ∧
    rootQuotientGlobalRepairDivisorCoverNumber r N h ≤
      rootQuotientMinimumCompositeMacroCount r N h := by
  have hFeasible : ∃ S : Set ℕ,
      S.Finite ∧ RootQuotientRepairDivisorCover
        (RootQuotientPrimeHardSemanticTargetFinset r N h)
        (RootQuotientSemanticCompositeCandidates r N) S :=
    ⟨RootQuotientSemanticCompositeCandidates r N,
      semanticCompositeCandidates_finite r N,
      semanticCompositeCandidates_cover_primeHardTargets hh⟩
  exact ⟨
    primeDirectionDemand_le_globalRepairDivisorPackingNumber hr hh hBinary,
    repairDivisorPackingNumber_le_coverNumber hFeasible,
    globalRepairDivisorCoverNumber_le_minimumCompositeMacroCount hr hh⟩

end EnterpriseMath.Quotient
