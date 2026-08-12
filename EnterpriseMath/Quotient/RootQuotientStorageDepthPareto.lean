import EnterpriseMath.Quotient.RootQuotientMinimumStorageGeometry
import EnterpriseMath.Quotient.RootQuotientMinimumStoragePhase
import EnterpriseMath.Quotient.RootQuotientPenultimateStorage
import Mathlib.Data.Set.Card
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- True storage/depth feasibility: there is a normalized finite primitive
presentation using at most `s` stored instruction types and separating the
bounded exact state domain within `h` execution steps. -/
def RootQuotientStorageDepthFeasible
    (r N s h : ℕ) : Prop :=
  ∃ G : Set ℕ,
    RootQuotientFiniteStorageSeparator r N h G ∧
    G.ncard ≤ s

/-- At every positive horizon, the two-dimensional storage/depth feasible
region is exactly the epigraph of the minimum-storage curve `S_r(N,h)`. -/
theorem rootQuotientStorageDepthFeasible_iff_minimumStorage_le
    {r N s h : ℕ}
    (hr : 1 ≤ r)
    (hh : 1 ≤ h) :
    RootQuotientStorageDepthFeasible r N s h ↔
      rootQuotientMinimumStorageSize r N h ≤ s := by
  constructor
  · rintro ⟨G, hG, hGCard⟩
    exact (rootQuotientMinimumStorageSize_le_normalized hG).trans hGCard
  · intro hMin
    obtain ⟨G, hG, hGCard⟩ :=
      exists_rootQuotientMinimumStorageSeparator
        (r := r) (N := N) (h := h) hr hh
    exact ⟨G, hG, by simpa [hGCard] using hMin⟩

/-- Feasibility is monotone in storage budget. -/
theorem rootQuotientStorageDepthFeasible_mono_storage
    {r N s t h : ℕ}
    (hst : s ≤ t)
    (hFeas : RootQuotientStorageDepthFeasible r N s h) :
    RootQuotientStorageDepthFeasible r N t h := by
  obtain ⟨G, hG, hCard⟩ := hFeas
  exact ⟨G, hG, hCard.trans hst⟩

/-- Feasibility is monotone in execution depth. -/
theorem rootQuotientStorageDepthFeasible_mono_horizon
    {r N s h j : ℕ}
    (hhj : h ≤ j)
    (hFeas : RootQuotientStorageDepthFeasible r N s h) :
    RootQuotientStorageDepthFeasible r N s j := by
  obtain ⟨G, hG, hCard⟩ := hFeas
  have hSepJ : SeparatesRootQuotientWordsUpTo r N j G :=
    separatesRootQuotientWordsUpTo_mono_horizon hhj hG.2.2.2
  exact ⟨G, ⟨hG.1, hG.2.1, hG.2.2.1, hSepJ⟩, hCard⟩

/-- Positive horizons at which a storage budget `s` is feasible. -/
def RootQuotientStorageFeasibleHorizons
    (r N s : ℕ) : Set ℕ :=
  {h : ℕ | 1 ≤ h ∧ rootQuotientMinimumStorageSize r N h ≤ s}

/-- Least positive execution horizon attainable under storage budget `s`.

For meaningful nontrivial domains we use it under the natural feasibility
hypothesis `|P_N|≤s`, which guarantees the set of positive feasible horizons is
nonempty. -/
noncomputable def rootQuotientMinimumHorizonAtStorage
    (r N s : ℕ) : ℕ :=
  sInf (RootQuotientStorageFeasibleHorizons r N s)

/-- Any storage budget at least the forced-prime cardinality has some positive
feasible horizon. -/
theorem rootQuotientStorageFeasibleHorizons_nonempty
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤ s) :
    (RootQuotientStorageFeasibleHorizons r N s).Nonempty := by
  let h := max 1 (rootQuotientPrimeHorizon r N)
  have hh : 1 ≤ h := by
    dsimp [h]
    exact le_max_left _ _
  have hL : rootQuotientPrimeHorizon r N ≤ h := by
    dsimp [h]
    exact le_max_right _ _
  have hStorage :=
    rootQuotientMinimumStorageSize_eq_primeBasis_ncard_of_horizon_le
      (r := r) (N := N) (h := h) hr hh hL
  refine ⟨h, hh, ?_⟩
  rw [hStorage]
  exact hPrimeBudget

/-- The least positive horizon under an admissible storage budget is attained. -/
theorem rootQuotientMinimumHorizonAtStorage_mem
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤ s) :
    rootQuotientMinimumHorizonAtStorage r N s ∈
      RootQuotientStorageFeasibleHorizons r N s := by
  exact Nat.sInf_mem
    (rootQuotientStorageFeasibleHorizons_nonempty hr hPrimeBudget)

/-- Exact Pareto duality.

For any storage budget at least the forced-prime core and any positive horizon,
`D_r(N,s)≤h` iff the minimum storage required at horizon `h` fits inside `s`.
Thus `S(h)` and `D(s)` are two coordinate descriptions of the same monotone
storage/execution-depth frontier. -/
theorem rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
    {r N s h : ℕ}
    (hr : 2 ≤ r)
    (hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤ s)
    (hh : 1 ≤ h) :
    rootQuotientMinimumHorizonAtStorage r N s ≤ h ↔
      rootQuotientMinimumStorageSize r N h ≤ s := by
  constructor
  · intro hDh
    have hDMem := rootQuotientMinimumHorizonAtStorage_mem hr hPrimeBudget
    have hDPos : 1 ≤ rootQuotientMinimumHorizonAtStorage r N s := hDMem.1
    have hDStorage :
        rootQuotientMinimumStorageSize r N
          (rootQuotientMinimumHorizonAtStorage r N s) ≤ s := hDMem.2
    have hMono := rootQuotientMinimumStorageSize_anti_horizon
      (r := r) (N := N)
      (h := rootQuotientMinimumHorizonAtStorage r N s) (j := h)
      (by omega) hDPos hDh
    exact hMono.trans hDStorage
  · intro hStorage
    apply Nat.sInf_le
    exact ⟨hh, hStorage⟩

/-- Feasibility-region form of the same Pareto duality. -/
theorem rootQuotientStorageDepthFeasible_iff_minimumHorizon_le
    {r N s h : ℕ}
    (hr : 2 ≤ r)
    (hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤ s)
    (hh : 1 ≤ h) :
    RootQuotientStorageDepthFeasible r N s h ↔
      rootQuotientMinimumHorizonAtStorage r N s ≤ h := by
  rw [rootQuotientStorageDepthFeasible_iff_minimumStorage_le
    (by omega) hh]
  exact
    (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
      hr hPrimeBudget hh).symm

/-- With enough storage for the complete semantic basis, one execution step is
optimal. -/
theorem rootQuotientMinimumHorizonAtStorage_eq_one_of_semanticBudget
    {r N s : ℕ}
    (hr : 2 ≤ r)
    (hSemanticBudget :
      (RootQuotientNontrivialPowerFreeBasis r N).ncard ≤ s) :
    rootQuotientMinimumHorizonAtStorage r N s = 1 := by
  have hPrimeSub :
      RootQuotientPrimeBasis N ⊆
        RootQuotientNontrivialPowerFreeBasis r N :=
    rootQuotientPrimeBasis_subset_semanticBasis hr
  have hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤ s :=
    (Set.ncard_le_ncard hPrimeSub rootQuotientNontrivialPowerFreeBasis_finite).trans
      hSemanticBudget
  have hOneStorage :=
    rootQuotientMinimumStorageSize_one_eq_semanticBasis_ncard
      (r := r) (N := N) (by omega)
  have hUpper : rootQuotientMinimumHorizonAtStorage r N s ≤ 1 :=
    (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
      hr hPrimeBudget (by omega)).2 (by simpa [hOneStorage])
  have hPos := (rootQuotientMinimumHorizonAtStorage_mem hr hPrimeBudget).1
  omega

/-- At exactly the forced-prime storage budget, the minimum positive execution
horizon is the exact prime compiler horizon, provided that horizon is positive. -/
theorem rootQuotientMinimumHorizonAtStorage_primeBudget_eq_primeHorizon
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hLPos : 1 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumHorizonAtStorage
        r N (RootQuotientPrimeBasis N).ncard =
      rootQuotientPrimeHorizon r N := by
  let s := (RootQuotientPrimeBasis N).ncard
  let D := rootQuotientMinimumHorizonAtStorage r N s
  have hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤ s := by rfl
  have hDLeL : D ≤ rootQuotientPrimeHorizon r N := by
    apply (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
      (r := r) (N := N) (s := s)
      (h := rootQuotientPrimeHorizon r N)
      hr hPrimeBudget hLPos).2
    rw [rootQuotientMinimumStorageSize_eq_primeBasis_ncard_of_horizon_le
      hr hLPos le_rfl]
  have hDMem := rootQuotientMinimumHorizonAtStorage_mem hr hPrimeBudget
  have hDPos : 1 ≤ D := hDMem.1
  have hDStorage : rootQuotientMinimumStorageSize r N D ≤ s := hDMem.2
  obtain ⟨G, hG, hGCard⟩ :=
    exists_rootQuotientMinimumStorageSeparator
      (r := r) (N := N) (h := D) (by omega) hDPos
  have hPrimeSubG : RootQuotientPrimeBasis N ⊆ G :=
    rootQuotientPrimeBasis_subset_of_word_separates
      hr hG.2.2.1 hG.2.2.2
  have hGLePrime : G.ncard ≤ (RootQuotientPrimeBasis N).ncard := by
    rw [hGCard]
    exact hDStorage
  have hEq : RootQuotientPrimeBasis N = G :=
    Set.eq_of_subset_of_ncard_le hPrimeSubG hGLePrime hG.2.1
  have hPrimeSep : SeparatesRootQuotientWordsUpTo
      r N D (RootQuotientPrimeBasis N) := by
    rw [hEq]
    exact hG.2.2.2
  have hLLeD := rootQuotientPrimeHorizon_minimal_of_separates
    (r := r) (N := N) (h := D) (by omega) hPrimeSep
  dsimp [D, s] at hDLeL hLLeD ⊢
  exact Nat.le_antisymm hDLeL hLLeD

/-- The exact penultimate set-cover storage budget always reaches at least the
penultimate prime horizon; it may reach still earlier if the storage curve has
a plateau. -/
theorem rootQuotientMinimumHorizonAtStorage_penultimateCoverBudget_le
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumHorizonAtStorage r N
        ((RootQuotientPrimeBasis N).ncard +
          rootQuotientPenultimateSemiprimeCoverNumber r N) ≤
      rootQuotientPrimeHorizon r N - 1 := by
  let s := (RootQuotientPrimeBasis N).ncard +
    rootQuotientPenultimateSemiprimeCoverNumber r N
  have hPrimeBudget : (RootQuotientPrimeBasis N).ncard ≤ s := by
    dsimp [s]
    omega
  have hPenPos : 1 ≤ rootQuotientPrimeHorizon r N - 1 := by omega
  apply (rootQuotientMinimumHorizonAtStorage_le_iff_minimumStorage_le
    (r := r) (N := N) (s := s)
    (h := rootQuotientPrimeHorizon r N - 1)
    hr hPrimeBudget hPenPos).2
  rw [rootQuotientMinimumStorageSize_penultimate_eq_prime_add_semiprimeCoverNumber
    hr hHorizon]

end EnterpriseMath.Quotient
