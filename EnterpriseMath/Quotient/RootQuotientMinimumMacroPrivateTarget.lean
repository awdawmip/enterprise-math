import EnterpriseMath.Quotient.RootQuotientPrimeBirthStarAxis
import EnterpriseMath.Quotient.RootQuotientPrimeHardRepair
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- **Every stored type in a minimum exact macro dictionary has a private hard
semantic target.**

If `S` is a minimum-cardinality exact optional-macro presentation and `g∈S`,
then deleting `g` breaks horizon-`h` reachability for at least one prime-hard
semantic target.  Moreover `g` divides that target, so the private target is a
literal arithmetic certificate that the stored type is genuinely used. -/
theorem exists_private_primeHard_target_of_mem_minimumCompositeMacroPresentation
    {r N h g : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hS : RootQuotientCompositeMacroPresentation r N h S)
    (hSCard : S.ncard = rootQuotientMinimumCompositeMacroCount r N h)
    (hgS : g ∈ S) :
    ∃ t : ℕ,
      t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h ∧
      RootQuotientProductReachableWithin h
        (RootQuotientPrimeBasis N ∪ S) t ∧
      ¬RootQuotientProductReachableWithin h
        (RootQuotientPrimeBasis N ∪ (S \ {g})) t ∧
      g ∣ t := by
  classical
  let S₀ : Set ℕ := S \ {g}
  have hS₀Finite : S₀.Finite := hS.1.sdiff
  have hS₀Candidate : S₀ ⊆ RootQuotientSemanticCompositeCandidates r N := by
    intro a ha
    exact hS.2.1 ha.1
  have hFail : ∃ t : ℕ,
      t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h ∧
      ¬RootQuotientProductReachableWithin h
        (RootQuotientPrimeBasis N ∪ S₀) t := by
    by_contra hNoFail
    push_neg at hNoFail
    have hRel₀ : RootQuotientRelativeRepairPresentation
        (RootQuotientPrimeBasis N) h
        (RootQuotientPrimeHardSemanticTargetFinset r N h)
        (RootQuotientSemanticCompositeCandidates r N) S₀ :=
      ⟨hS₀Finite, hS₀Candidate, hNoFail⟩
    have hRelFull : RootQuotientRelativeRepairPresentation
        (RootQuotientPrimeBasis N) h
        (RootQuotientSemanticTargetFinset r N)
        (RootQuotientSemanticCompositeCandidates r N) S₀ :=
      (relativeRepairPresentation_fullSemantic_iff_primeHard).2 hRel₀
    have hComp₀ : RootQuotientCompositeMacroPresentation r N h S₀ :=
      (compositeMacroPresentation_iff_relativeRepairPresentation hr).2 hRelFull
    have hMinLe := rootQuotientMinimumCompositeMacroCount_le hComp₀
    have hCardDrop : S₀.ncard = S.ncard - 1 := by
      dsimp [S₀]
      exact Set.ncard_sdiff_singleton_of_mem hgS
    rw [hCardDrop, hSCard] at hMinLe
    omega
  obtain ⟨t, htHard, htNoReach⟩ := hFail
  have hRelS : RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis N) h
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N) S :=
    (relativeRepairPresentation_fullSemantic_iff_primeHard).1
      ((compositeMacroPresentation_iff_relativeRepairPresentation hr).1 hS)
  have htReach := hRelS.2.2 t htHard
  obtain ⟨w, hwLen, hwOver, hProd⟩ := htReach
  have hgWord : g ∈ w := by
    by_contra hgNot
    have hwOver₀ : RootQuotientWordOver
        (RootQuotientPrimeBasis N ∪ S₀) w := by
      intro a ha
      have haUnion := hwOver a ha
      rcases haUnion with haPrime | haS
      · exact Or.inl haPrime
      · exact Or.inr ⟨haS, by
          intro hag
          subst a
          exact hgNot ha⟩
    exact htNoReach ⟨w, hwLen, hwOver₀, hProd⟩
  have hgDvd : g ∣ t :=
    word_member_dvd_compiled_product hgWord hProd
  exact ⟨t, htHard, htReach, htNoReach, hgDvd⟩

/-- **Exact preinvestment has an old private arithmetic witness.**

If an old exact optimum has preinvested in a future prime direction `p`, then
some preinvested `p^e`, `2≤e≤h`, owns a private old prime-hard target divisible
by that pure prime power. -/
theorem exactPrimeDirectionPreinvestment_has_private_target
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hPre : RootQuotientExactPrimeDirectionPreinvestment r N h p) :
    ∃ S : Set ℕ, ∃ e t : ℕ,
      RootQuotientCompositeMacroPresentation r N h S ∧
      S.ncard = rootQuotientMinimumCompositeMacroCount r N h ∧
      2 ≤ e ∧ e ≤ h ∧ p ^ e ∈ S ∧
      t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h ∧
      ¬RootQuotientProductReachableWithin h
        (RootQuotientPrimeBasis N ∪ (S \ {p ^ e})) t ∧
      p ^ e ∣ t := by
  obtain ⟨S, hS, hSCard, e, heTwo, heLe, heMem⟩ := hPre
  obtain ⟨t, htHard, _htReach, htNoReach, htDvd⟩ :=
    exists_private_primeHard_target_of_mem_minimumCompositeMacroPresentation
      hr hh hS hSCard heMem
  exact ⟨S, e, t, hS, hSCard, heTwo, heLe, heMem,
    htHard, htNoReach, htDvd⟩

end EnterpriseMath.Quotient
