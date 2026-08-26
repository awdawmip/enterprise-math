import EnterpriseMath.Quotient.RootQuotientPrimeBirthEventClassification
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Every exact composite-macro presentation is, on the prime-hard target
family, a candidate-restricted divisor cover of the same stored macro set. -/
theorem compositeMacroPresentation_is_globalRepairDivisorCover
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hS : RootQuotientCompositeMacroPresentation r N h S) :
    RootQuotientRepairDivisorCover
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N) S := by
  constructor
  · exact hS.2.1
  · intro t ht
    have hPos : PositiveRootQuotientGenerators
        (RootQuotientPrimeBasis N ∪ S) := by
      intro g hg
      rcases hg with hgPrime | hgS
      · exact hgPrime.1.one_le
      · have hgSemantic := (hS.2.1 hgS).1
        omega
    have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
    have hReach :=
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeBasis N ∪ S)
        (by omega) hPos).1 hS.2.2
        t (by omega) htMem.1.2.1 htMem.1.2.2
    obtain ⟨g, hgS, hgDvd⟩ :=
      exists_spare_divisor_of_union_reachable_not_base
        (G := RootQuotientPrimeBasis N) (S := S)
        hReach ((mem_primeHardSemanticTargetFinset_iff_not_prime_reachable).1 ht).2
    exact ⟨g, hgS, hgDvd⟩

/-- If the old global divisor relaxation is already exact (`tau=mu`), then any
old exact-optimal dictionary is simultaneously a divisor-cover optimum. -/
theorem exactOptimal_is_coverOptimal_of_globalRepairGap_zero
    {r N h : ℕ} {S : Set ℕ}
    (hr : 2 ≤ r)
    (hS : RootQuotientCompositeMacroPresentation r N h S)
    (hSCard : S.ncard = rootQuotientMinimumCompositeMacroCount r N h)
    (hGapZero : rootQuotientGlobalRepairRelaxationGap r N h = 0) :
    RootQuotientRepairDivisorCover
        (RootQuotientPrimeHardSemanticTargetFinset r N h)
        (RootQuotientSemanticCompositeCandidates r N) S ∧
      S.ncard = rootQuotientGlobalRepairDivisorCoverNumber r N h := by
  have hCover := compositeMacroPresentation_is_globalRepairDivisorCover hr hS
  have hDecomp := minimumCompositeMacroCount_eq_globalDivisorCover_add_gap
    (r := r) (N := N) (h := h) hr (by omega)
  rw [hGapZero, Nat.add_zero] at hDecomp
  exact ⟨hCover, hSCard.trans hDecomp⟩

/-- **Exact preinvestment forces cover preinvestment whenever the old repair
relaxation is exact.**

Thus exact-only preinvestment can occur only inside a genuine residual-depth
phase. -/
theorem coverPrimeDirectionPreinvestment_of_exact_of_globalRepairGap_zero
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hGapZero : rootQuotientGlobalRepairRelaxationGap r N h = 0)
    (hExactPre : RootQuotientExactPrimeDirectionPreinvestment r N h p) :
    RootQuotientCoverPrimeDirectionPreinvestment r N h p := by
  obtain ⟨S, hComp, hCard, hPre⟩ := hExactPre
  have hCoverOpt := exactOptimal_is_coverOptimal_of_globalRepairGap_zero
    hr hComp hCard hGapZero
  exact ⟨S, hComp.1, hCoverOpt.1, hCoverOpt.2, hPre⟩

/-- **Dual catch-up requires preexisting residual-depth overhead.**

At a hard-prime birth, event `(1,1,0)` is impossible whenever the old-domain
divisor relaxation is already exact. -/
theorem one_le_globalRepairRelaxationGap_of_dualCatchup_at_prime_birth
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r)
    (hEvent : rootQuotientResourceEvent r N h = rootQuotientDualCatchupEvent) :
    1 ≤ rootQuotientGlobalRepairRelaxationGap r N h := by
  have hExactOnly :=
    (dualCatchupEvent_at_prime_birth_iff_exactOnlyPreinvestment
      hr hh hp hBirth hBinaryNext).1 hEvent
  by_contra hNot
  have hGapZero : rootQuotientGlobalRepairRelaxationGap r N h = 0 := by omega
  exact hExactOnly.1
    (coverPrimeDirectionPreinvestment_of_exact_of_globalRepairGap_zero
      hr hGapZero hExactOnly.2)

end EnterpriseMath.Quotient
