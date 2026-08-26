import EnterpriseMath.Quotient.RootQuotientThreeLayerPhaseDiagram
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Semantic composite candidate sets are monotone in the bounded state range. -/
theorem semanticCompositeCandidates_mono_stateBound
    {r N M : ℕ}
    (hNM : N ≤ M) :
    RootQuotientSemanticCompositeCandidates r N ⊆
      RootQuotientSemanticCompositeCandidates r M := by
  intro g hg
  have hgSemantic := hg.1
  refine ⟨⟨hgSemantic.1, hgSemantic.2.1.trans hNM, hgSemantic.2.2⟩, ?_⟩
  intro hgPrimeM
  exact hg.2 ⟨hgPrimeM.1, hgSemantic.2.1⟩

/-- Prime-hard semantic target families are monotone in the bounded state
range. -/
theorem primeHardSemanticTargetFinset_mono_stateBound
    {r N M h : ℕ}
    (hNM : N ≤ M) :
    RootQuotientPrimeHardSemanticTargetFinset r N h ⊆
      RootQuotientPrimeHardSemanticTargetFinset r M h := by
  intro t ht
  have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
  apply (mem_primeHardSemanticTargetFinset_iff).2
  exact ⟨⟨htMem.1.1, htMem.1.2.1.trans hNM, htMem.1.2.2⟩, htMem.2⟩

/-- Hard pure-prime direction sets are monotone in the state bound. -/
theorem hardPrimeDirections_mono_stateBound
    {N M h : ℕ}
    (hNM : N ≤ M) :
    RootQuotientHardPrimeDirections N h ⊆
      RootQuotientHardPrimeDirections M h := by
  intro p hp
  exact ⟨hp.1, hp.2.trans hNM⟩

/-- Pure-direction demand cannot decrease when one more state is exposed. -/
theorem primeDirectionDemand_mono_succ
    (N h : ℕ) :
    rootQuotientPrimeDirectionDemand N h ≤
      rootQuotientPrimeDirectionDemand (N + 1) h := by
  rw [← hardPrimeDirections_ncard_eq_primeDirectionDemand,
    ← hardPrimeDirections_ncard_eq_primeDirectionDemand]
  exact Set.ncard_le_ncard
    (hardPrimeDirections_mono_stateBound (Nat.le_succ N))
    (rootQuotientHardPrimeDirections_finite (N + 1) h)

/-- At a fixed horizon, adding one state can create at most one new hard prime
direction. -/
theorem primeDirectionDemand_succ_le_add_one
    (N h : ℕ) :
    rootQuotientPrimeDirectionDemand (N + 1) h ≤
      rootQuotientPrimeDirectionDemand N h + 1 := by
  let H := RootQuotientHardPrimeDirections N h
  let H' := RootQuotientHardPrimeDirections (N + 1) h
  have hSub : H ⊆ H' := hardPrimeDirections_mono_stateBound (Nat.le_succ N)
  have hH'Finite : H'.Finite := rootQuotientHardPrimeDirections_finite (N + 1) h
  have hDiffFinite : (H' \ H).Finite := hH'Finite.sdiff
  have hDiffOne : (H' \ H).ncard ≤ 1 := by
    apply (Set.ncard_le_one hDiffFinite).2
    intro p hp q hq
    have hpNew : p ^ (h + 1) = N + 1 := by
      have hpLe : p ^ (h + 1) ≤ N + 1 := hp.1.2
      have hpNot : ¬p ^ (h + 1) ≤ N := by
        intro hpN
        exact hp.2 ⟨hp.1.1, hpN⟩
      omega
    have hqNew : q ^ (h + 1) = N + 1 := by
      have hqLe : q ^ (h + 1) ≤ N + 1 := hq.1.2
      have hqNot : ¬q ^ (h + 1) ≤ N := by
        intro hqN
        exact hq.2 ⟨hq.1.1, hqN⟩
      omega
    exact Nat.pow_left_injective (by omega : h + 1 ≠ 0)
      (hpNew.trans hqNew.symm)
  have hCardDecomp : (H' \ H).ncard + H.ncard = H'.ncard :=
    Set.ncard_sdiff_add_ncard_of_subset hSub hH'Finite
  rw [hardPrimeDirections_ncard_eq_primeDirectionDemand,
    hardPrimeDirections_ncard_eq_primeDirectionDemand] at hCardDecomp
  omega

/-- Pure-direction demand is a unit-step staircase in the state bound. -/
theorem primeDirectionDemand_succ_staircase
    (N h : ℕ) :
    rootQuotientPrimeDirectionDemand N h ≤
      rootQuotientPrimeDirectionDemand (N + 1) h ∧
    rootQuotientPrimeDirectionDemand (N + 1) h ≤
      rootQuotientPrimeDirectionDemand N h + 1 :=
  ⟨primeDirectionDemand_mono_succ N h,
    primeDirectionDemand_succ_le_add_one N h⟩

/-- Restricting a divisor cover from `N+1` back to `N` cannot increase its
cardinality: any cover instruction used on an old target divides that target
and hence already lies in the old candidate range. -/
theorem globalRepairDivisorCoverNumber_mono_succ
    {r N h : ℕ}
    (hh : 1 ≤ h) :
    rootQuotientGlobalRepairDivisorCoverNumber r N h ≤
      rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h := by
  unfold rootQuotientGlobalRepairDivisorCoverNumber
  have hFeasible : ∃ S : Set ℕ,
      S.Finite ∧
      RootQuotientRepairDivisorCover
        (RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
        (RootQuotientSemanticCompositeCandidates r (N + 1)) S :=
    ⟨RootQuotientSemanticCompositeCandidates r (N + 1),
      semanticCompositeCandidates_finite r (N + 1),
      semanticCompositeCandidates_cover_primeHardTargets hh⟩
  obtain ⟨S, hSFinite, hCover, hSCard⟩ :=
    exists_minimumRepairDivisorCover hFeasible
  let S' : Set ℕ := S ∩ RootQuotientSemanticCompositeCandidates r N
  have hS'Finite : S'.Finite := hSFinite.subset Set.inter_subset_left
  have hS'Cover : RootQuotientRepairDivisorCover
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N) S' := by
    constructor
    · exact Set.inter_subset_right
    · intro t ht
      have htNew := primeHardSemanticTargetFinset_mono_stateBound
        (r := r) (h := h) (Nat.le_succ N) ht
      obtain ⟨g, hgS, hgDvd⟩ := hCover.2 t htNew
      have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
      have hgLeT : g ≤ t := Nat.le_of_dvd (by omega) hgDvd
      have hgOld : g ∈ RootQuotientSemanticCompositeCandidates r N := by
        have hgNew := hCover.1 hgS
        refine ⟨⟨hgNew.1.1, hgLeT.trans htMem.1.2.1, hgNew.1.2.2⟩, ?_⟩
        intro hgPrimeOld
        exact hgNew.2 ⟨hgPrimeOld.1, hgNew.1.2.1⟩
      exact ⟨g, ⟨hgS, hgOld⟩, hgDvd⟩
  have hOldLe := rootQuotientRepairDivisorCoverNumber_le hS'Finite hS'Cover
  have hCardLe : S'.ncard ≤ S.ncard :=
    Set.ncard_le_ncard Set.inter_subset_left hSFinite
  rw [hSCard] at hCardLe
  exact hOldLe.trans hCardLe

/-- The new state itself is an admissible composite candidate whenever it is a
prime-hard semantic target at positive horizon. -/
theorem succ_mem_semanticCompositeCandidates_of_primeHard
    {r N h : ℕ}
    (hh : 1 ≤ h)
    (hHard : N + 1 ∈ RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h) :
    N + 1 ∈ RootQuotientSemanticCompositeCandidates r (N + 1) := by
  have hMem := (mem_primeHardSemanticTargetFinset_iff).1 hHard
  refine ⟨hMem.1, ?_⟩
  intro hPrime
  have hCountOne : rootQuotientPrimeFactorCount (N + 1) = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hPrime.1]
    simp
  omega

/-- At fixed positive horizon, exposing one additional state can increase the
global divisor-cover minimum by at most one: if the new state is hard, storing
that target itself always repairs the new divisor-hitting obligation. -/
theorem globalRepairDivisorCoverNumber_succ_le_add_one
    {r N h : ℕ}
    (hh : 1 ≤ h) :
    rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h ≤
      rootQuotientGlobalRepairDivisorCoverNumber r N h + 1 := by
  unfold rootQuotientGlobalRepairDivisorCoverNumber
  have hFeasibleN : ∃ S : Set ℕ,
      S.Finite ∧
      RootQuotientRepairDivisorCover
        (RootQuotientPrimeHardSemanticTargetFinset r N h)
        (RootQuotientSemanticCompositeCandidates r N) S :=
    ⟨RootQuotientSemanticCompositeCandidates r N,
      semanticCompositeCandidates_finite r N,
      semanticCompositeCandidates_cover_primeHardTargets hh⟩
  obtain ⟨S, hSFinite, hCover, hSCard⟩ :=
    exists_minimumRepairDivisorCover hFeasibleN
  by_cases hNewHard :
      N + 1 ∈ RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h
  · let S' : Set ℕ := S ∪ ({N + 1} : Set ℕ)
    have hS'Finite : S'.Finite := hSFinite.union (by simp)
    have hS'Cover : RootQuotientRepairDivisorCover
        (RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
        (RootQuotientSemanticCompositeCandidates r (N + 1)) S' := by
      constructor
      · intro g hg
        rcases hg with hgS | hgNew
        · exact semanticCompositeCandidates_mono_stateBound
            (r := r) (Nat.le_succ N) (hCover.1 hgS)
        · have hgEq : g = N + 1 := by simpa using hgNew
          subst g
          exact succ_mem_semanticCompositeCandidates_of_primeHard hh hNewHard
      · intro t ht
        by_cases htNew : t = N + 1
        · subst t
          exact ⟨N + 1, Or.inr (by simp), dvd_rfl⟩
        · have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
          have htN : t ≤ N := by omega
          have htOld : t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h :=
            (mem_primeHardSemanticTargetFinset_iff).2
              ⟨⟨htMem.1.1, htN, htMem.1.2.2⟩, htMem.2⟩
          obtain ⟨g, hgS, hgDvd⟩ := hCover.2 t htOld
          exact ⟨g, Or.inl hgS, hgDvd⟩
    have hLe := rootQuotientRepairDivisorCoverNumber_le hS'Finite hS'Cover
    have hCard : S'.ncard ≤ S.ncard + 1 := by
      dsimp [S']
      calc
        (S ∪ ({N + 1} : Set ℕ)).ncard ≤
            S.ncard + ({N + 1} : Set ℕ).ncard := Set.ncard_union_le _ _
        _ = S.ncard + 1 := by simp
    rw [hSCard] at hCard
    exact hLe.trans hCard
  · have hSNewCover : RootQuotientRepairDivisorCover
        (RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
        (RootQuotientSemanticCompositeCandidates r (N + 1)) S := by
      constructor
      · intro g hgS
        exact semanticCompositeCandidates_mono_stateBound
          (r := r) (Nat.le_succ N) (hCover.1 hgS)
      · intro t ht
        have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
        have htN : t ≤ N := by
          by_contra hNot
          have htEq : t = N + 1 := by omega
          exact hNewHard (by simpa [htEq] using ht)
        have htOld : t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h :=
          (mem_primeHardSemanticTargetFinset_iff).2
            ⟨⟨htMem.1.1, htN, htMem.1.2.2⟩, htMem.2⟩
        exact hCover.2 t htOld
    have hLe := rootQuotientRepairDivisorCoverNumber_le hSFinite hSNewCover
    rw [hSCard] at hLe
    omega

/-- The global divisor-cover frontier is a unit-step staircase in state bound. -/
theorem globalRepairDivisorCoverNumber_succ_staircase
    {r N h : ℕ}
    (hh : 1 ≤ h) :
    rootQuotientGlobalRepairDivisorCoverNumber r N h ≤
      rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h ∧
    rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h ≤
      rootQuotientGlobalRepairDivisorCoverNumber r N h + 1 :=
  ⟨globalRepairDivisorCoverNumber_mono_succ hh,
    globalRepairDivisorCoverNumber_succ_le_add_one hh⟩

end EnterpriseMath.Quotient
