import EnterpriseMath.Quotient.RootQuotientLeastPhase
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The empty primitive alphabet is vacuously positive. -/
theorem rootQuotientEmptyAlphabet_positive :
    PositiveRootQuotientGenerators (∅ : Set ℕ) := by
  intro a ha
  simp at ha

/-- On the trivial exact-state domain `0,...,N` with `N ≤ 1`, the empty word
alone separates at horizon zero. -/
theorem rootQuotientEmptyAlphabet_separates_at_zero_of_le_one
    {r N : ℕ}
    (hr : 1 ≤ r)
    (hN : N ≤ 1) :
    SeparatesRootQuotientWordsUpTo r N 0 (∅ : Set ℕ) := by
  apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
    (r := r) (N := N) (h := 0) (G := (∅ : Set ℕ))
    hr rootQuotientEmptyAlphabet_positive).2
  intro b hbPos hbN _hbFree
  have hbOne : b = 1 := by omega
  subst b
  exact ⟨[], by simp, by simp [RootQuotientWordOver],
    by simp [rootQuotientWordProduct]⟩

/-- For root order at least two, no positive primitive alphabet can separate a
domain containing states `0,1,2` at horizon zero.  The required prime boundary
`2` cannot be compiled by the empty word. -/
theorem no_rootQuotient_separation_at_zero_of_two_le
    {r N : ℕ} {G : Set ℕ}
    (hr : 2 ≤ r)
    (hN : 2 ≤ N)
    (hG : PositiveRootQuotientGenerators G) :
    ¬SeparatesRootQuotientWordsUpTo r N 0 G := by
  intro hSep
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := 0) (G := G) (by omega) hG).1 hSep
      2 (by omega) hN (prime_rPowerFree hr Nat.prime_two)
  obtain ⟨w, hwLen, _hwG, hProd⟩ := hReach
  cases w with
  | nil =>
      simp [rootQuotientWordProduct] at hProd
  | cons a w =>
      simp at hwLen

/-- At horizon zero on `N ≤ 1`, the empty alphabet is inclusion-least. -/
theorem rootQuotientEmptyAlphabet_isLeast_at_zero_of_le_one
    {r N : ℕ}
    (hr : 1 ≤ r)
    (hN : N ≤ 1) :
    IsLeastSeparatingRootQuotientAlphabet r N 0 (∅ : Set ℕ) := by
  refine ⟨rootQuotientEmptyAlphabet_positive,
    rootQuotientEmptyAlphabet_separates_at_zero_of_le_one hr hN, ?_⟩
  intro H _hHPos _hHSep
  exact Set.empty_subset H

/-- Inclusion-least separating alphabets, when they exist, are unique. -/
theorem isLeastSeparatingRootQuotientAlphabet_unique
    {r N h : ℕ} {G H : Set ℕ}
    (hG : IsLeastSeparatingRootQuotientAlphabet r N h G)
    (hH : IsLeastSeparatingRootQuotientAlphabet r N h H) :
    G = H := by
  apply Set.Subset.antisymm
  · exact hG.2.2 hH.1 hH.2.1
  · exact hH.2.2 hG.1 hG.2.1

/-- Complete existence phase diagram for inclusion-least primitive quotient
alphabets at every natural word horizon, for root order `r ≥ 2`.

* `h = 0`: a least alphabet exists exactly on the trivial domain `N ≤ 1`, and
  it is empty;
* `h = 1`: the nontrivial bounded power-free semantic basis is least;
* `h ≥ 2`: a least alphabet exists exactly when the exact prime-only horizon
  is at most `h`, in which case the bounded prime alphabet is least. -/
theorem exists_least_separating_rootQuotientAlphabet_iff_full_phase
    {r N h : ℕ}
    (hr : 2 ≤ r) :
    (∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet r N h G) ↔
      (h = 0 ∧ N ≤ 1) ∨
      h = 1 ∨
      (2 ≤ h ∧ rootQuotientPrimeHorizon r N ≤ h) := by
  constructor
  · intro hExists
    by_cases hZero : h = 0
    · left
      refine ⟨hZero, ?_⟩
      by_contra hNot
      have hTwo : 2 ≤ N := by omega
      obtain ⟨G, hLeast⟩ := hExists
      have hNoSep :=
        no_rootQuotient_separation_at_zero_of_two_le
          (r := r) (N := N) (G := G) hr hTwo hLeast.1
      subst h
      exact hNoSep hLeast.2.1
    · by_cases hOne : h = 1
      · exact Or.inr (Or.inl hOne)
      · have hh : 2 ≤ h := by omega
        right
        right
        refine ⟨hh, ?_⟩
        exact
          (exists_least_separating_rootQuotientAlphabet_iff_horizon_le
            (r := r) (N := N) (h := h) hr hh).1 hExists
  · rintro (⟨hZero, hN⟩ | hOne | ⟨hh, hHorizon⟩)
    · subst h
      exact ⟨∅,
        rootQuotientEmptyAlphabet_isLeast_at_zero_of_le_one
          (r := r) (N := N) (by omega) hN⟩
    · subst h
      exact ⟨RootQuotientNontrivialPowerFreeBasis r N,
        rootQuotientNontrivialPowerFreeBasis_isLeast_at_one
          (r := r) (N := N) (by omega)⟩
    · exact
        (exists_least_separating_rootQuotientAlphabet_iff_horizon_le
          (r := r) (N := N) (h := h) hr hh).2 hHorizon

end EnterpriseMath.Quotient
