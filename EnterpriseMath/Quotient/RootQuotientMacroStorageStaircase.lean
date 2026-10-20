import EnterpriseMath.Quotient.RootQuotientResourceStaircase
import EnterpriseMath.Quotient.RootQuotientMacroRepairEquivalence
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Bounded-prime bases are monotone in the state bound. -/
theorem rootQuotientPrimeBasis_mono_stateBound
    {N M : ℕ}
    (hNM : N ≤ M) :
    RootQuotientPrimeBasis N ⊆ RootQuotientPrimeBasis M := by
  intro p hp
  exact ⟨hp.1, hp.2.trans hNM⟩

/-- A word compiling an old target cannot actually use a new out-of-range
instruction: every literal factor divides the compiled product. -/
theorem word_over_larger_presentation_restricts_to_old_range
    {r N h b : ℕ} {S : Set ℕ} {w : List ℕ}
    (hbPos : 1 ≤ b)
    (hbN : b ≤ N)
    (hSFamily : RootQuotientCompositeMacroFamily r (N + 1) S)
    (hw : RootQuotientWordOver
      (RootQuotientPrimeBasis (N + 1) ∪ S) w)
    (hProd : b = rootQuotientWordProduct w) :
    RootQuotientWordOver
      (RootQuotientPrimeBasis N ∪
        (S ∩ RootQuotientSemanticCompositeCandidates r N)) w := by
  intro g hgWord
  have hgDvd : g ∣ b := word_member_dvd_compiled_product hgWord hProd
  have hgLeB : g ≤ b := Nat.le_of_dvd (by omega) hgDvd
  have hgUnion := hw g hgWord
  rcases hgUnion with hgPrime | hgS
  · exact Or.inl ⟨hgPrime.1, hgLeB.trans hbN⟩
  · have hgNew := hSFamily hgS
    have hgOld : g ∈ RootQuotientSemanticCompositeCandidates r N := by
      refine ⟨⟨hgNew.1.1, hgLeB.trans hbN, hgNew.1.2.2⟩, ?_⟩
      intro hgPrimeOld
      exact hgNew.2 ⟨hgPrimeOld.1, hgNew.1.2.1⟩
    exact Or.inr ⟨hgS, hgOld⟩

/-- True optional-macro storage cannot decrease when one more state is exposed. -/
theorem minimumCompositeMacroCount_mono_succ
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientMinimumCompositeMacroCount r N h ≤
      rootQuotientMinimumCompositeMacroCount r (N + 1) h := by
  obtain ⟨S, hComp, hSCard⟩ :=
    exists_rootQuotientMinimumCompositeMacroPresentation
      (r := r) (N := N + 1) (h := h) hr hh
  let S' : Set ℕ := S ∩ RootQuotientSemanticCompositeCandidates r N
  have hS'Finite : S'.Finite := hComp.1.subset Set.inter_subset_left
  have hS'Candidate : S' ⊆ RootQuotientSemanticCompositeCandidates r N :=
    Set.inter_subset_right
  have hFullNew : RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis (N + 1)) h
      (RootQuotientSemanticTargetFinset r (N + 1))
      (RootQuotientSemanticCompositeCandidates r (N + 1)) S :=
    (compositeMacroPresentation_iff_relativeRepairPresentation hr).1 hComp
  have hHardNew : RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis (N + 1)) h
      (RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
      (RootQuotientSemanticCompositeCandidates r (N + 1)) S :=
    (relativeRepairPresentation_fullSemantic_iff_primeHard).1 hFullNew
  have hHardOld : RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis N) h
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N) S' := by
    refine ⟨hS'Finite, hS'Candidate, ?_⟩
    intro b hbHard
    have hbHardNew := primeHardSemanticTargetFinset_mono_stateBound
      (r := r) (h := h) (Nat.le_succ N) hbHard
    obtain ⟨w, hwLen, hwLarge, hProd⟩ := hHardNew.2.2 b hbHardNew
    have hbMem := (mem_primeHardSemanticTargetFinset_iff).1 hbHard
    refine ⟨w, hwLen, ?_, hProd⟩
    exact word_over_larger_presentation_restricts_to_old_range
      (r := r) (N := N) (h := h)
      (b := b) (S := S) (w := w)
      (by omega) hbMem.1.2.1 hComp.2.1 hwLarge hProd
  have hMuOldLe : rootQuotientMinimumCompositeMacroCount r N h ≤ S'.ncard := by
    rw [minimumCompositeMacroCount_eq_primeHardRelativeRepairStorage hr hh]
    exact rootQuotientMinimumRelativeRepairStorage_le hHardOld
  have hCardLe : S'.ncard ≤ S.ncard :=
    Set.ncard_le_ncard Set.inter_subset_left hComp.1
  rw [hSCard] at hCardLe
  exact hMuOldLe.trans hCardLe

/-- Old prime and macro generators embed into the next-state presentation. -/
theorem old_presentation_subset_next_with_spares
    {r N : ℕ} {S S' : Set ℕ}
    (hSS' : S ⊆ S') :
    RootQuotientPrimeBasis N ∪ S ⊆
      RootQuotientPrimeBasis (N + 1) ∪ S' := by
  intro g hg
  rcases hg with hgPrime | hgS
  · exact Or.inl (rootQuotientPrimeBasis_mono_stateBound (Nat.le_succ N) hgPrime)
  · exact Or.inr (hSS' hgS)

/-- At fixed positive horizon, exposing one more state increases the exact
optional-macro minimum by at most one. -/
theorem minimumCompositeMacroCount_succ_le_add_one
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientMinimumCompositeMacroCount r (N + 1) h ≤
      rootQuotientMinimumCompositeMacroCount r N h + 1 := by
  obtain ⟨S, hComp, hSCard⟩ :=
    exists_rootQuotientMinimumCompositeMacroPresentation
      (r := r) (N := N) (h := h) hr hh
  have hFullOld : RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis N) h
      (RootQuotientSemanticTargetFinset r N)
      (RootQuotientSemanticCompositeCandidates r N) S :=
    (compositeMacroPresentation_iff_relativeRepairPresentation hr).1 hComp
  have hHardOld : RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis N) h
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N) S :=
    (relativeRepairPresentation_fullSemantic_iff_primeHard).1 hFullOld
  by_cases hNewHard :
      N + 1 ∈ RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h
  · let S' : Set ℕ := S ∪ ({N + 1} : Set ℕ)
    have hS'Finite : S'.Finite := hComp.1.union (by simp)
    have hS'Candidate : S' ⊆ RootQuotientSemanticCompositeCandidates r (N + 1) := by
      intro g hg
      rcases hg with hgS | hgNew
      · exact semanticCompositeCandidates_mono_stateBound
          (r := r) (Nat.le_succ N) (hComp.2.1 hgS)
      · have hgEq : g = N + 1 := by simpa using hgNew
        subst g
        exact succ_mem_semanticCompositeCandidates_of_primeHard hh hNewHard
    have hHardNew : RootQuotientRelativeRepairPresentation
        (RootQuotientPrimeBasis (N + 1)) h
        (RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
        (RootQuotientSemanticCompositeCandidates r (N + 1)) S' := by
      refine ⟨hS'Finite, hS'Candidate, ?_⟩
      intro t ht
      by_cases htNew : t = N + 1
      · subst t
        refine ⟨[N + 1], ?_, ?_, ?_⟩
        · simp
          omega
        · intro g hg
          have hgEq : g = N + 1 := by simpa using hg
          subst g
          exact Or.inr (by simp [S'])
        · simp [rootQuotientWordProduct]
      · have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
        have htN : t ≤ N := by omega
        have htOld : t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h :=
          (mem_primeHardSemanticTargetFinset_iff).2
            ⟨⟨htMem.1.1, htN, htMem.1.2.2⟩, htMem.2⟩
        have hReachOld := hHardOld.2.2 t htOld
        exact rootQuotientProductReachableWithin_mono_generators
          (old_presentation_subset_next_with_spares
            (r := r) (N := N) (S := S) (S' := S')
            (fun g hg => Or.inl hg))
          hReachOld
    have hMuLe : rootQuotientMinimumCompositeMacroCount r (N + 1) h ≤ S'.ncard := by
      rw [minimumCompositeMacroCount_eq_primeHardRelativeRepairStorage hr hh]
      exact rootQuotientMinimumRelativeRepairStorage_le hHardNew
    have hCard : S'.ncard ≤ S.ncard + 1 := by
      dsimp [S']
      calc
        (S ∪ ({N + 1} : Set ℕ)).ncard ≤
            S.ncard + ({N + 1} : Set ℕ).ncard := Set.ncard_union_le _ _
        _ = S.ncard + 1 := by simp
    rw [hSCard] at hCard
    exact hMuLe.trans hCard
  · have hSCandidateNew : S ⊆ RootQuotientSemanticCompositeCandidates r (N + 1) :=
      fun g hg => semanticCompositeCandidates_mono_stateBound
        (r := r) (Nat.le_succ N) (hComp.2.1 hg)
    have hHardNew : RootQuotientRelativeRepairPresentation
        (RootQuotientPrimeBasis (N + 1)) h
        (RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
        (RootQuotientSemanticCompositeCandidates r (N + 1)) S := by
      refine ⟨hComp.1, hSCandidateNew, ?_⟩
      intro t ht
      have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
      have htN : t ≤ N := by
        by_contra hNot
        have htEq : t = N + 1 := by omega
        exact hNewHard (by simpa [htEq] using ht)
      have htOld : t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h :=
        (mem_primeHardSemanticTargetFinset_iff).2
          ⟨⟨htMem.1.1, htN, htMem.1.2.2⟩, htMem.2⟩
      have hReachOld := hHardOld.2.2 t htOld
      exact rootQuotientProductReachableWithin_mono_generators
        (old_presentation_subset_next_with_spares
          (r := r) (N := N) (S := S) (S' := S) Set.Subset.rfl)
        hReachOld
    have hMuLe : rootQuotientMinimumCompositeMacroCount r (N + 1) h ≤ S.ncard := by
      rw [minimumCompositeMacroCount_eq_primeHardRelativeRepairStorage hr hh]
      exact rootQuotientMinimumRelativeRepairStorage_le hHardNew
    rw [hSCard] at hMuLe
    omega

/-- **Exact optional-macro storage is a unit-step staircase in state bound.** -/
theorem minimumCompositeMacroCount_succ_staircase
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h) :
    rootQuotientMinimumCompositeMacroCount r N h ≤
      rootQuotientMinimumCompositeMacroCount r (N + 1) h ∧
    rootQuotientMinimumCompositeMacroCount r (N + 1) h ≤
      rootQuotientMinimumCompositeMacroCount r N h + 1 :=
  ⟨minimumCompositeMacroCount_mono_succ hr hh,
    minimumCompositeMacroCount_succ_le_add_one hr hh⟩

end EnterpriseMath.Quotient
