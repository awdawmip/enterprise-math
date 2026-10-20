import EnterpriseMath.Quotient.RootQuotientRelativeRepairCover
import Mathlib.Data.Set.Card
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A finite candidate-restricted spare dictionary repairs a finite target
family relative to base ISA `G` at horizon `h`. -/
def RootQuotientRelativeRepairPresentation
    (G : Set ℕ) (h : ℕ) (T : Finset ℕ) (C S : Set ℕ) : Prop :=
  S.Finite ∧
  S ⊆ C ∧
  ∀ t ∈ T,
    RootQuotientProductReachableWithin h (G ∪ S) t

/-- Exact residual-word form of a relative repair presentation.

This is the monotone-DNF / repair-hyperedge semantics: every target chooses one
spare word whose literal types lie in the stored dictionary, and the remaining
target is compiled by the base ISA in the residual depth. -/
theorem relativeRepairPresentation_iff_residualWords
    {G C S : Set ℕ} {h : ℕ} {T : Finset ℕ} :
    RootQuotientRelativeRepairPresentation G h T C S ↔
      S.Finite ∧
      S ⊆ C ∧
      ∀ t ∈ T,
        ∃ u : List ℕ, ∃ b : ℕ,
          u.length ≤ h ∧
          RootQuotientWordOver S u ∧
          RootQuotientProductReachableWithin (h - u.length) G b ∧
          rootQuotientWordProduct u * b = t := by
  constructor
  · rintro ⟨hFinite, hSC, hRepair⟩
    refine ⟨hFinite, hSC, ?_⟩
    intro t ht
    exact
      (rootQuotientProductReachableWithin_union_iff_exists_spareWord_residual).1
        (hRepair t ht)
  · rintro ⟨hFinite, hSC, hWords⟩
    refine ⟨hFinite, hSC, ?_⟩
    intro t ht
    exact
      (rootQuotientProductReachableWithin_union_iff_exists_spareWord_residual).2
        (hWords t ht)

/-- Feasible storage cardinalities for exact relative repair. -/
def RootQuotientRelativeRepairCardinalities
    (G : Set ℕ) (h : ℕ) (T : Finset ℕ) (C : Set ℕ) : Set ℕ :=
  {m : ℕ | ∃ S : Set ℕ,
    RootQuotientRelativeRepairPresentation G h T C S ∧
    S.ncard = m}

/-- Minimum exact spare-dictionary cardinality for repairing `T` relative to
base ISA `G` within horizon `h`, constrained to candidate set `C`. -/
noncomputable def rootQuotientMinimumRelativeRepairStorage
    (G : Set ℕ) (h : ℕ) (T : Finset ℕ) (C : Set ℕ) : ℕ :=
  sInf (RootQuotientRelativeRepairCardinalities G h T C)

/-- The exact relative repair minimum is no larger than any feasible finite
repair dictionary. -/
theorem rootQuotientMinimumRelativeRepairStorage_le
    {G C S : Set ℕ} {h : ℕ} {T : Finset ℕ}
    (hS : RootQuotientRelativeRepairPresentation G h T C S) :
    rootQuotientMinimumRelativeRepairStorage G h T C ≤ S.ncard := by
  apply Nat.sInf_le
  exact ⟨S, hS, rfl⟩

/-- Whenever the exact repair problem is feasible, its minimum cardinality is
attained. -/
theorem exists_minimumRelativeRepairPresentation
    {G C : Set ℕ} {h : ℕ} {T : Finset ℕ}
    (hFeasible : ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation G h T C S) :
    ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation G h T C S ∧
      S.ncard = rootQuotientMinimumRelativeRepairStorage G h T C := by
  have hNonempty :
      (RootQuotientRelativeRepairCardinalities G h T C).Nonempty := by
    obtain ⟨S, hS⟩ := hFeasible
    exact ⟨S.ncard, S, hS, rfl⟩
  have hMem :
      rootQuotientMinimumRelativeRepairStorage G h T C ∈
        RootQuotientRelativeRepairCardinalities G h T C :=
    Nat.sInf_mem hNonempty
  exact hMem

/-- **Repair hierarchy inequality.**

For a finite family that is horizon-hard for the base ISA, the first-order
divisor hitting number is a lower bound on the exact relative repair storage.
Equality is a special structural event (for example the penultimate semiprime
cover layer), not a generic fact. -/
theorem repairDivisorCoverNumber_le_minimumRelativeRepairStorage
    {G C : Set ℕ} {h : ℕ} {T : Finset ℕ}
    (hNoBase : ∀ t ∈ T,
      ¬RootQuotientProductReachableWithin h G t)
    (hFeasible : ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation G h T C S) :
    rootQuotientRepairDivisorCoverNumber T C ≤
      rootQuotientMinimumRelativeRepairStorage G h T C := by
  obtain ⟨S, hS, hSCard⟩ :=
    exists_minimumRelativeRepairPresentation hFeasible
  have hCoverLe : rootQuotientRepairDivisorCoverNumber T C ≤ S.ncard := by
    exact repairDivisorCoverNumber_le_spare_storage
      hS.1 hS.2.1 hS.2.2 hNoBase
  rw [hSCard] at hCoverLe
  exact hCoverLe

end EnterpriseMath.Quotient
