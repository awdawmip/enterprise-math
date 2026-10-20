import EnterpriseMath.Quotient.RootQuotientStorageDepthPareto
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Every positive-horizon separator for root order at least two contains the
forced bounded-prime core, so minimum storage is always at least prime-core
cardinality. -/
theorem rootQuotientPrimeBasis_ncard_le_minimumStorageSize
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    (RootQuotientPrimeBasis N).ncard ≤
      rootQuotientMinimumStorageSize r N h := by
  obtain ⟨G, hG, hGCard⟩ :=
    exists_rootQuotientMinimumStorageSeparator
      (r := r) (N := N) (h := h) (by omega) hh
  have hPrimeSubG : RootQuotientPrimeBasis N ⊆ G :=
    rootQuotientPrimeBasis_subset_of_word_separates
      hr hG.2.2.1 hG.2.2.2
  have hCard : (RootQuotientPrimeBasis N).ncard ≤ G.ncard :=
    Set.ncard_le_ncard hPrimeSubG hG.2.1
  simpa [hGCard] using hCard

/-- Increasing storage budget can only decrease the minimum attainable
execution horizon. -/
theorem rootQuotientMinimumHorizonAtStorage_anti_storage
    {r N s t : ℕ}
    (hr : 2 ≤ r)
    (hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤ s)
    (hst : s ≤ t) :
    rootQuotientMinimumHorizonAtStorage r N t ≤
      rootQuotientMinimumHorizonAtStorage r N s := by
  have hPrimeBudgetT : (RootQuotientPrimeBasis N).ncard ≤ t :=
    hPrimeBudget.trans hst
  have hSMem := rootQuotientMinimumHorizonAtStorage_mem hr hPrimeBudget
  have hSPos : 1 ≤ rootQuotientMinimumHorizonAtStorage r N s := hSMem.1
  have hSStorage :
      rootQuotientMinimumStorageSize r N
        (rootQuotientMinimumHorizonAtStorage r N s) ≤ s := hSMem.2
  apply (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
    (r := r) (N := N) (s := t)
    (h := rootQuotientMinimumHorizonAtStorage r N s)
    hr hPrimeBudgetT hSPos).2
  exact hSStorage.trans hst

/-- Exact storage-budget interval for an execution-depth phase.

For `h≥2`, the minimum attainable horizon under budget `s` is exactly `h` iff
`s` fits the half-open interval between the storage requirements at consecutive
horizons:

`D(s)=h  ↔  S(h)≤s<S(h-1)`.

This is the discrete Pareto-frontier phase decomposition. -/
theorem rootQuotientMinimumHorizonAtStorage_eq_iff_budget_interval
    {r N s h : ℕ}
    (hr : 2 ≤ r)
    (hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤ s)
    (hh : 2 ≤ h) :
    rootQuotientMinimumHorizonAtStorage r N s = h ↔
      rootQuotientMinimumStorageSize r N h ≤ s ∧
      s < rootQuotientMinimumStorageSize r N (h - 1) := by
  have hhPos : 1 ≤ h := by omega
  have hPredPos : 1 ≤ h - 1 := by omega
  constructor
  · intro hDh
    constructor
    · apply (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
        (r := r) (N := N) (s := s) (h := h)
        hr hPrimeBudget hhPos).1
      omega
    · by_contra hNot
      have hPredStorage :
          rootQuotientMinimumStorageSize r N (h - 1) ≤ s := by omega
      have hDLePred :=
        (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
          (r := r) (N := N) (s := s) (h := h - 1)
          hr hPrimeBudget hPredPos).2 hPredStorage
      rw [hDh] at hDLePred
      omega
  · rintro ⟨hStorage, hBelowPred⟩
    have hDLeH :=
      (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
        (r := r) (N := N) (s := s) (h := h)
        hr hPrimeBudget hhPos).2 hStorage
    apply Nat.le_antisymm hDLeH
    by_contra hNot
    have hDLePred :
        rootQuotientMinimumHorizonAtStorage r N s ≤ h - 1 := by omega
    have hPredStorage :=
      (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
        (r := r) (N := N) (s := s) (h := h - 1)
        hr hPrimeBudget hPredPos).1 hDLePred
    omega

/-- A positive horizon `h≥2` occurs as an actual minimum-depth Pareto phase
for some admissible storage budget iff the minimum-storage curve strictly drops
when moving from `h-1` to `h`. -/
theorem exists_storageBudget_with_minimumHorizon_eq_iff_storage_strict_drop
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h) :
    (∃ s : ℕ,
      (RootQuotientPrimeBasis N).ncard ≤ s ∧
      rootQuotientMinimumHorizonAtStorage r N s = h) ↔
      rootQuotientMinimumStorageSize r N h <
        rootQuotientMinimumStorageSize r N (h - 1) := by
  constructor
  · rintro ⟨s, hPrimeBudget, hDh⟩
    have hInterval :=
      (rootQuotientMinimumHorizonAtStorage_eq_iff_budget_interval
        (r := r) (N := N) (s := s) (h := h)
        hr hPrimeBudget hh).1 hDh
    exact hInterval.1.trans_lt hInterval.2
  · intro hDrop
    let s := rootQuotientMinimumStorageSize r N h
    have hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤ s := by
      dsimp [s]
      exact rootQuotientPrimeBasis_ncard_le_minimumStorageSize
        hr (by omega)
    refine ⟨s, hPrimeBudget, ?_⟩
    apply (rootQuotientMinimumHorizonAtStorage_eq_iff_budget_interval
      (r := r) (N := N) (s := s) (h := h)
      hr hPrimeBudget hh).2
    exact ⟨le_rfl, hDrop⟩

/-- Storage plateaus are exactly Pareto-inactive execution depths: if allowing
one more execution step does not reduce minimum storage, then no storage budget
has that new horizon as its optimum. -/
theorem no_storageBudget_has_minimumHorizon_of_storage_plateau
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hPlateau :
      rootQuotientMinimumStorageSize r N h =
        rootQuotientMinimumStorageSize r N (h - 1)) :
    ¬∃ s : ℕ,
      (RootQuotientPrimeBasis N).ncard ≤ s ∧
      rootQuotientMinimumHorizonAtStorage r N s = h := by
  intro hExists
  have hDrop :=
    (exists_storageBudget_with_minimumHorizon_eq_iff_storage_strict_drop
      (r := r) (N := N) (h := h) hr hh).1 hExists
  rw [hPlateau] at hDrop
  exact (lt_irrefl _ hDrop)

end EnterpriseMath.Quotient
