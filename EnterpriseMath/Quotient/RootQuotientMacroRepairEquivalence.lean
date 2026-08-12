import EnterpriseMath.Quotient.RootQuotientRelativeRepairStorage
import EnterpriseMath.Quotient.RootQuotientCompositeMacroStorage
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Finite target set consisting of every nontrivial canonical semantic action. -/
noncomputable def RootQuotientSemanticTargetFinset
    (r N : ℕ) : Finset ℕ :=
  rootQuotientNontrivialPowerFreeBasis_finite.toFinset

@[simp]
theorem mem_rootQuotientSemanticTargetFinset_iff
    {r N b : ℕ} :
    b ∈ RootQuotientSemanticTargetFinset r N ↔
      b ∈ RootQuotientNontrivialPowerFreeBasis r N := by
  simp [RootQuotientSemanticTargetFinset]

/-- **Composite macro presentation = relative repair presentation.**

At positive root order, once the forced bounded-prime ISA is treated as the
base compiler, choosing optional semantic composite macros is exactly the
relative finite repair problem for the complete nontrivial semantic target
family. -/
theorem compositeMacroPresentation_iff_relativeRepairPresentation
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r) :
    RootQuotientCompositeMacroPresentation r N h S ↔
      RootQuotientRelativeRepairPresentation
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientSemanticTargetFinset r N)
        (RootQuotientSemanticCompositeCandidates r N)
        S := by
  constructor
  · rintro ⟨hFinite, hFamily, hSep⟩
    have hPos : PositiveRootQuotientGenerators
        (RootQuotientPrimeBasis N ∪ S) := by
      intro g hg
      rcases hg with hgPrime | hgS
      · exact hgPrime.1.one_le
      · have hgSemantic := (hFamily hgS).1
        omega
    have hCompile :=
      (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeBasis N ∪ S)
        (by omega) hPos).1 hSep
    refine ⟨hFinite, hFamily, ?_⟩
    intro t ht
    have htSemantic : t ∈ RootQuotientNontrivialPowerFreeBasis r N :=
      (mem_rootQuotientSemanticTargetFinset_iff).1 ht
    exact hCompile t htSemantic
  · rintro ⟨hFinite, hFamily, hRepair⟩
    have hPos : PositiveRootQuotientGenerators
        (RootQuotientPrimeBasis N ∪ S) := by
      intro g hg
      rcases hg with hgPrime | hgS
      · exact hgPrime.1.one_le
      · have hgSemantic := (hFamily hgS).1
        omega
    refine ⟨hFinite, hFamily, ?_⟩
    apply (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeBasis N ∪ S)
      (by omega) hPos).2
    intro t htSemantic
    exact hRepair t
      (mem_rootQuotientSemanticTargetFinset_iff).2 htSemantic

/-- **True optional-macro frontier = exact relative repair storage.**

For every positive horizon, `mu_r(N,h)` is precisely the minimum candidate-
restricted spare-dictionary size needed to repair the complete semantic target
family relative to the forced prime compiler. -/
theorem minimumCompositeMacroCount_eq_minimumRelativeRepairStorage
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientMinimumCompositeMacroCount r N h =
      rootQuotientMinimumRelativeRepairStorage
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientSemanticTargetFinset r N)
        (RootQuotientSemanticCompositeCandidates r N) := by
  apply Nat.le_antisymm
  · obtain ⟨S₀, hComp₀⟩ := exists_compositeMacroPresentation hr hh
    have hFeasible : ∃ S : Set ℕ,
        RootQuotientRelativeRepairPresentation
          (RootQuotientPrimeBasis N)
          h
          (RootQuotientSemanticTargetFinset r N)
          (RootQuotientSemanticCompositeCandidates r N)
          S :=
      ⟨S₀,
        (compositeMacroPresentation_iff_relativeRepairPresentation hr).1 hComp₀⟩
    obtain ⟨S, hRel, hRelCard⟩ :=
      exists_minimumRelativeRepairPresentation hFeasible
    have hComp : RootQuotientCompositeMacroPresentation r N h S :=
      (compositeMacroPresentation_iff_relativeRepairPresentation hr).2 hRel
    have hMuLe := rootQuotientMinimumCompositeMacroCount_le hComp
    rw [hRelCard] at hMuLe
    exact hMuLe
  · obtain ⟨S, hComp, hCompCard⟩ :=
      exists_rootQuotientMinimumCompositeMacroPresentation hr hh
    have hRel : RootQuotientRelativeRepairPresentation
        (RootQuotientPrimeBasis N)
        h
        (RootQuotientSemanticTargetFinset r N)
        (RootQuotientSemanticCompositeCandidates r N)
        S :=
      (compositeMacroPresentation_iff_relativeRepairPresentation hr).1 hComp
    have hRelLe := rootQuotientMinimumRelativeRepairStorage_le hRel
    rw [hCompCard] at hRelLe
    exact hRelLe

/-- **Finite hard-target certificate lower bound on the true macro frontier.**

Any finite family of semantic targets that is horizon-hard for the forced prime
base yields a candidate-restricted divisor-cover lower bound on the global
optional-macro requirement.  This is the reusable certificate interface behind
hard-prime counting, repair gcd kernels, and finite transient optimizer proofs. -/
theorem repairDivisorCoverNumber_le_minimumCompositeMacroCount
    {r N h : ℕ} {T : Finset ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hSemantic : ∀ t ∈ T,
      t ∈ RootQuotientNontrivialPowerFreeBasis r N)
    (hNoPrime : ∀ t ∈ T,
      ¬RootQuotientProductReachableWithin h (RootQuotientPrimeBasis N) t) :
    rootQuotientRepairDivisorCoverNumber
        T (RootQuotientSemanticCompositeCandidates r N) ≤
      rootQuotientMinimumCompositeMacroCount r N h := by
  obtain ⟨S, hS, hSCard⟩ :=
    exists_rootQuotientMinimumCompositeMacroPresentation hr hh
  have hLe := semanticRepairDivisorCoverNumber_le_macroPresentation
    hr hS hSemantic hNoPrime
  rw [hSCard] at hLe
  exact hLe

end EnterpriseMath.Quotient
