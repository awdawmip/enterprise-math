import EnterpriseMath.Quotient.RootQuotientMinimumStoragePhase
import EnterpriseMath.Quotient.RootQuotientPenultimateStorage
import Mathlib.Data.Set.Card
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Optional composite-macro part of a normalized presentation: bounded
semantic instructions outside the forced prime core. -/
def RootQuotientCompositeMacroFamily
    (r N : ℕ) (S : Set ℕ) : Prop :=
  S ⊆ RootQuotientNontrivialPowerFreeBasis r N \ RootQuotientPrimeBasis N

/-- A finite composite-macro family is feasible at horizon `h` when adjoining
it to the forced prime core separates the bounded quotient-root task. -/
def RootQuotientCompositeMacroPresentation
    (r N h : ℕ) (S : Set ℕ) : Prop :=
  S.Finite ∧
  RootQuotientCompositeMacroFamily r N S ∧
  SeparatesRootQuotientWordsUpTo
    r N h (RootQuotientPrimeBasis N ∪ S)

/-- Every normalized separator at horizon at least two decomposes exactly as
the forced prime core union its non-prime remainder. -/
theorem normalized_separator_eq_prime_union_compositePart
    {r N h : ℕ} {G : Set ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hG : RootQuotientFiniteStorageSeparator r N h G) :
    G = RootQuotientPrimeBasis N ∪
      (G \ RootQuotientPrimeBasis N) := by
  have hPrimeSubG : RootQuotientPrimeBasis N ⊆ G :=
    rootQuotientPrimeBasis_subset_of_word_separates
      hr hG.2.2.1 hG.2.2.2
  ext g
  constructor
  · intro hg
    by_cases hgPrime : g ∈ RootQuotientPrimeBasis N
    · exact Or.inl hgPrime
    · exact Or.inr ⟨hg, hgPrime⟩
  · intro hg
    rcases hg with hgPrime | hgRest
    · exact hPrimeSubG hgPrime
    · exact hgRest.1

/-- The non-prime remainder of a normalized separator is a valid composite
macro family. -/
theorem normalized_separator_compositePart_is_family
    {r N h : ℕ} {G : Set ℕ}
    (hG : RootQuotientFiniteStorageSeparator r N h G) :
    RootQuotientCompositeMacroFamily
      r N (G \ RootQuotientPrimeBasis N) := by
  intro g hg
  exact ⟨hG.1 hg.1, hg.2⟩

/-- Every positive-horizon minimum separator supplies a feasible finite macro
presentation once the horizon is at least two. -/
theorem exists_compositeMacroPresentation
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h) :
    ∃ S : Set ℕ, RootQuotientCompositeMacroPresentation r N h S := by
  obtain ⟨G, hG, _hGCard⟩ :=
    exists_rootQuotientMinimumStorageSeparator
      (r := r) (N := N) (h := h) (by omega) (by omega)
  let S := G \ RootQuotientPrimeBasis N
  have hSFinite : S.Finite := by
    dsimp [S]
    exact hG.2.1.sdiff
  have hSFamily : RootQuotientCompositeMacroFamily r N S := by
    dsimp [S]
    exact normalized_separator_compositePart_is_family hG
  have hEq := normalized_separator_eq_prime_union_compositePart hr hh hG
  have hSep : SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientPrimeBasis N ∪ S) := by
    rw [← hEq]
    exact hG.2.2.2
  exact ⟨S, hSFinite, hSFamily, hSep⟩

/-- Cardinalities of feasible finite composite-macro families at fixed
horizon. -/
def RootQuotientCompositeMacroCardinalities
    (r N h : ℕ) : Set ℕ :=
  {m : ℕ | ∃ S : Set ℕ,
    RootQuotientCompositeMacroPresentation r N h S ∧
    S.ncard = m}

/-- Minimum number of optional composite macro types beyond the forced prime
core at fixed horizon. -/
noncomputable def rootQuotientMinimumCompositeMacroCount
    (r N h : ℕ) : ℕ :=
  sInf (RootQuotientCompositeMacroCardinalities r N h)

/-- The minimum composite-macro count is attained for every `h>=2`. -/
theorem exists_rootQuotientMinimumCompositeMacroPresentation
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h) :
    ∃ S : Set ℕ,
      RootQuotientCompositeMacroPresentation r N h S ∧
      S.ncard = rootQuotientMinimumCompositeMacroCount r N h := by
  have hNonempty : (RootQuotientCompositeMacroCardinalities r N h).Nonempty := by
    obtain ⟨S, hS⟩ := exists_compositeMacroPresentation hr hh
    exact ⟨S.ncard, S, hS, rfl⟩
  have hMem : rootQuotientMinimumCompositeMacroCount r N h ∈
      RootQuotientCompositeMacroCardinalities r N h :=
    Nat.sInf_mem hNonempty
  exact hMem

/-- The minimum macro count is no larger than any feasible finite macro
presentation. -/
theorem rootQuotientMinimumCompositeMacroCount_le
    {r N h : ℕ} {S : Set ℕ}
    (hS : RootQuotientCompositeMacroPresentation r N h S) :
    rootQuotientMinimumCompositeMacroCount r N h ≤ S.ncard := by
  apply Nat.sInf_le
  exact ⟨S, hS, rfl⟩

/-- Exact forced-core decomposition of true minimum storage.

For every `h>=2`, minimum primitive-type storage equals the mandatory bounded
prime count plus the minimum number of optional composite macro types. -/
theorem rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h) :
    rootQuotientMinimumStorageSize r N h =
      (RootQuotientPrimeBasis N).ncard +
        rootQuotientMinimumCompositeMacroCount r N h := by
  apply Nat.le_antisymm
  · obtain ⟨S, hS, hSCard⟩ :=
      exists_rootQuotientMinimumCompositeMacroPresentation hr hh
    let G := RootQuotientPrimeBasis N ∪ S
    have hGSemantic : G ⊆ RootQuotientNontrivialPowerFreeBasis r N := by
      intro g hg
      rcases hg with hgPrime | hgS
      · exact rootQuotientPrimeBasis_subset_semanticBasis hr hgPrime
      · exact (hS.2.1 hgS).1
    have hGFinite : G.Finite :=
      rootQuotientPrimeBasis_finite.union hS.1
    have hGPos : PositiveRootQuotientGenerators G := by
      intro g hg
      rcases hg with hgPrime | hgS
      · exact hgPrime.1.one_le
      · have hgSemantic := (hS.2.1 hgS).1
        omega
    have hStorage : RootQuotientFiniteStorageSeparator r N h G :=
      ⟨hGSemantic, hGFinite, hGPos, hS.2.2⟩
    have hMinLe := rootQuotientMinimumStorageSize_le_normalized hStorage
    have hDisjoint : Disjoint (RootQuotientPrimeBasis N) S := by
      exact Set.disjoint_left.2 fun g hgPrime hgS => (hS.2.1 hgS).2 hgPrime
    have hGCard : G.ncard = (RootQuotientPrimeBasis N).ncard + S.ncard := by
      dsimp [G]
      exact Set.ncard_union_eq hDisjoint rootQuotientPrimeBasis_finite hS.1
    rw [hGCard, hSCard] at hMinLe
    exact hMinLe
  · obtain ⟨G, hG, hGCard⟩ :=
      exists_rootQuotientMinimumStorageSeparator
        (r := r) (N := N) (h := h) (by omega) (by omega)
    let S := G \ RootQuotientPrimeBasis N
    have hS : RootQuotientCompositeMacroPresentation r N h S := by
      have hSFinite : S.Finite := by
        dsimp [S]
        exact hG.2.1.sdiff
      have hSFamily : RootQuotientCompositeMacroFamily r N S := by
        dsimp [S]
        exact normalized_separator_compositePart_is_family hG
      have hEq := normalized_separator_eq_prime_union_compositePart hr hh hG
      have hSep : SeparatesRootQuotientWordsUpTo
          r N h (RootQuotientPrimeBasis N ∪ S) := by
        rw [← hEq]
        exact hG.2.2.2
      exact ⟨hSFinite, hSFamily, hSep⟩
    have hMacroLe :
        rootQuotientMinimumCompositeMacroCount r N h ≤ S.ncard :=
      rootQuotientMinimumCompositeMacroCount_le hS
    have hPrimeSubG : RootQuotientPrimeBasis N ⊆ G :=
      rootQuotientPrimeBasis_subset_of_word_separates
        hr hG.2.2.1 hG.2.2.2
    have hDecomp :
        S.ncard + (RootQuotientPrimeBasis N).ncard = G.ncard := by
      dsimp [S]
      exact Set.ncard_sdiff_add_ncard_of_subset hPrimeSubG hG.2.1
    rw [hGCard] at hDecomp
    omega

/-- In the intermediate phase, the optional macro frontier is nonempty. -/
theorem rootQuotientMinimumCompositeMacroCount_pos_of_intermediate
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBelow : h < rootQuotientPrimeHorizon r N) :
    1 ≤ rootQuotientMinimumCompositeMacroCount r N h := by
  have hStorageGap :=
    primeBasis_ncard_add_one_le_rootQuotientMinimumStorageSize_of_intermediate
      hr hh hBelow
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr hh] at hStorageGap
  omega

/-- Once the prime horizon is available, no composite macro type is needed. -/
theorem rootQuotientMinimumCompositeMacroCount_eq_zero_of_horizon_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hHorizon : rootQuotientPrimeHorizon r N ≤ h) :
    rootQuotientMinimumCompositeMacroCount r N h = 0 := by
  have hStorage :=
    rootQuotientMinimumStorageSize_eq_primeBasis_ncard_of_horizon_le
      hr (by omega) hHorizon
  rw [rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
    hr hh] at hStorage
  omega

/-- Penultimate specialization: the general minimum composite-macro count
collapses exactly to the minimum semantic-semiprime divisor-cover number. -/
theorem rootQuotientMinimumCompositeMacroCount_penultimate_eq_semiprimeCoverNumber
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumCompositeMacroCount
        r N (rootQuotientPrimeHorizon r N - 1) =
      rootQuotientPenultimateSemiprimeCoverNumber r N := by
  have hPenTwo : 2 ≤ rootQuotientPrimeHorizon r N - 1 := by
    by_cases hEq : rootQuotientPrimeHorizon r N = 2
    · rw [hEq]
      simp
    · omega
  by_cases hLTwo : rootQuotientPrimeHorizon r N = 2
  · rw [hLTwo]
    simp only [Nat.reduceSubDiff]
    have hStorageOne :=
      rootQuotientMinimumStorageSize_one_eq_semanticBasis_ncard
        (r := r) (N := N) (by omega)
    have hPenStorage :=
      rootQuotientMinimumStorageSize_penultimate_eq_prime_add_semiprimeCoverNumber
        hr hHorizon
    rw [hLTwo] at hPenStorage
    simp only [Nat.reduceSubDiff] at hPenStorage
    have hMacroDecomp :=
      rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
        (r := r) (N := N) (h := 1) hr (by omega)
    rw [hMacroDecomp] at hPenStorage
    omega
  · have hPenTwo' : 2 ≤ rootQuotientPrimeHorizon r N - 1 := by omega
    have hMacroDecomp :=
      rootQuotientMinimumStorageSize_eq_prime_add_minimumCompositeMacroCount
        (r := r) (N := N)
        (h := rootQuotientPrimeHorizon r N - 1)
        hr hPenTwo'
    have hPenStorage :=
      rootQuotientMinimumStorageSize_penultimate_eq_prime_add_semiprimeCoverNumber
        hr hHorizon
    rw [hMacroDecomp] at hPenStorage
    omega

end EnterpriseMath.Quotient
