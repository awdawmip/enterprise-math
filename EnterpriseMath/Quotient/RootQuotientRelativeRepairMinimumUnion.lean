import EnterpriseMath.Quotient.RootQuotientRelativeRepairPlan
import EnterpriseMath.Quotient.RootQuotientMacroRepairEquivalence
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Cardinalities of target-wise witness-support unions for exact relative
repair plans. -/
def RootQuotientRelativeRepairPlanCardinalities
    (G : Set ℕ) (h : ℕ) (T : Finset ℕ) (C : Set ℕ) : Set ℕ :=
  {m : ℕ | ∃ P : RootQuotientRelativeRepairPlan G h T C,
    (P.dictionary : Set ℕ).ncard = m}

/-- Minimum union-cardinality of spare instruction types used by one exact
repair witness word per target. -/
noncomputable def rootQuotientMinimumRelativeRepairPlanStorage
    (G : Set ℕ) (h : ℕ) (T : Finset ℕ) (C : Set ℕ) : ℕ :=
  sInf (RootQuotientRelativeRepairPlanCardinalities G h T C)

/-- The plan minimum is no larger than the support-union cardinality of any one
repair plan. -/
theorem rootQuotientMinimumRelativeRepairPlanStorage_le
    {G C : Set ℕ} {h : ℕ} {T : Finset ℕ}
    (P : RootQuotientRelativeRepairPlan G h T C) :
    rootQuotientMinimumRelativeRepairPlanStorage G h T C ≤
      (P.dictionary : Set ℕ).ncard := by
  apply Nat.sInf_le
  exact ⟨P, rfl⟩

/-- If exact relative repair is feasible, the minimum witness-union
cardinality is attained by some target-wise repair plan. -/
theorem exists_minimumRelativeRepairPlan
    {G C : Set ℕ} {h : ℕ} {T : Finset ℕ}
    (hFeasible : ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation G h T C S) :
    ∃ P : RootQuotientRelativeRepairPlan G h T C,
      (P.dictionary : Set ℕ).ncard =
        rootQuotientMinimumRelativeRepairPlanStorage G h T C := by
  obtain ⟨S, hS⟩ := hFeasible
  obtain ⟨P₀, _hSub⟩ :=
    exists_relativeRepairPlan_dictionary_subset_of_presentation hS
  have hNonempty :
      (RootQuotientRelativeRepairPlanCardinalities G h T C).Nonempty := by
    exact ⟨(P₀.dictionary : Set ℕ).ncard, P₀, rfl⟩
  have hMem :
      rootQuotientMinimumRelativeRepairPlanStorage G h T C ∈
        RootQuotientRelativeRepairPlanCardinalities G h T C :=
    Nat.sInf_mem hNonempty
  exact hMem

/-- **Exact minimum-union theorem for relative repair.**

Minimum spare-dictionary storage equals the minimum cardinality of the union of
instruction types appearing in one exact residual-word witness chosen for each
target.

This is the general form of the monotone-DNF / witness-hyperedge view. -/
theorem minimumRelativeRepairStorage_eq_minimumRepairPlanStorage
    {G C : Set ℕ} {h : ℕ} {T : Finset ℕ}
    (hFeasible : ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation G h T C S) :
    rootQuotientMinimumRelativeRepairStorage G h T C =
      rootQuotientMinimumRelativeRepairPlanStorage G h T C := by
  apply Nat.le_antisymm
  · obtain ⟨P, hPCard⟩ := exists_minimumRelativeRepairPlan hFeasible
    have hPresentation := relativeRepairPlan_dictionary_is_presentation P
    have hRepairLe := rootQuotientMinimumRelativeRepairStorage_le hPresentation
    rw [hPCard] at hRepairLe
    exact hRepairLe
  · obtain ⟨S, hS, hSCard⟩ :=
      exists_minimumRelativeRepairPresentation hFeasible
    obtain ⟨P, hPLe⟩ :=
      exists_relativeRepairPlan_dictionary_ncard_le_of_presentation hS
    have hPlanLe := rootQuotientMinimumRelativeRepairPlanStorage_le P
    rw [hSCard] at hPLe
    exact hPlanLe.trans hPLe

/-- **Global optional-macro storage = minimum witness-support union.**

For the bounded quotient-root task, the true optional composite-macro frontier
is exactly the minimum union of primitive types appearing in one target-wise
repair word per canonical semantic denominator, with the forced bounded primes
serving as the residual backend. -/
theorem minimumCompositeMacroCount_eq_minimumRepairPlanStorage
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientMinimumCompositeMacroCount r N h =
      rootQuotientMinimumRelativeRepairPlanStorage
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientSemanticTargetFinset r N)
        (RootQuotientSemanticCompositeCandidates r N) := by
  obtain ⟨S₀, hComp₀⟩ := exists_compositeMacroPresentation hr hh
  have hFeasible : ∃ S : Set ℕ,
      RootQuotientRelativeRepairPresentation
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientSemanticTargetFinset r N)
        (RootQuotientSemanticCompositeCandidates r N)
        S :=
    ⟨S₀,
      (compositeMacroPresentation_iff_relativeRepairPresentation hr).1 hComp₀⟩
  calc
    rootQuotientMinimumCompositeMacroCount r N h =
        rootQuotientMinimumRelativeRepairStorage
          (RootQuotientPrimeBasis N)
          h
          (RootQuotientSemanticTargetFinset r N)
          (RootQuotientSemanticCompositeCandidates r N) :=
      minimumCompositeMacroCount_eq_minimumRelativeRepairStorage hr hh
    _ = rootQuotientMinimumRelativeRepairPlanStorage
          (RootQuotientPrimeBasis N)
          h
          (RootQuotientSemanticTargetFinset r N)
          (RootQuotientSemanticCompositeCandidates r N) :=
      minimumRelativeRepairStorage_eq_minimumRepairPlanStorage hFeasible

end EnterpriseMath.Quotient
