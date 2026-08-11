import EnterpriseMath.Quotient.RootQuotientPrimeBirthPreinvestment
import EnterpriseMath.Quotient.RootQuotientResourceEventLegality
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Restrict a next-state divisor cover to the old semantic candidate range.
Every old hard target keeps a divisor witness inside the old range because that
witness divides the old target itself. -/
theorem restrict_next_globalRepairCover_to_old
    {r N h : ℕ} {S : Set ℕ}
    (hSFinite : S.Finite)
    (hCover : RootQuotientRepairDivisorCover
      (RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
      (RootQuotientSemanticCompositeCandidates r (N + 1)) S) :
    RootQuotientRepairDivisorCover
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N)
      (S ∩ RootQuotientSemanticCompositeCandidates r N) := by
  constructor
  · exact Set.inter_subset_right
  · intro t ht
    have htNew := primeHardSemanticTargetFinset_mono_stateBound
      (r := r) (h := h) (Nat.le_succ N) ht
    obtain ⟨g, hgS, hgDvd⟩ := hCover.2 t htNew
    have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
    have hgLeT : g ≤ t := Nat.le_of_dvd (by omega) hgDvd
    have hgNew := hCover.1 hgS
    have hgOld : g ∈ RootQuotientSemanticCompositeCandidates r N := by
      refine ⟨⟨hgNew.1.1, hgLeT.trans htMem.1.2.1, hgNew.1.2.2⟩, ?_⟩
      intro hgPrimeOld
      exact hgNew.2 ⟨hgPrimeOld.1, hgNew.1.2.1⟩
    exact ⟨g, ⟨hgS, hgOld⟩, hgDvd⟩

/-- **Cover no-jump implies cover preinvestment.**

If the first-order divisor-cover minimum does not increase at a hard-prime
birth, then some old-domain minimum cover already contains a useful pure power
of that future prime direction. -/
theorem coverPrimeDirectionPreinvestment_of_coverNumber_eq_at_prime_birth
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r)
    (hEq : rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h =
      rootQuotientGlobalRepairDivisorCoverNumber r N h) :
    RootQuotientCoverPrimeDirectionPreinvestment r N h p := by
  have hFeasible : ∃ S : Set ℕ,
      S.Finite ∧
      RootQuotientRepairDivisorCover
        (RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
        (RootQuotientSemanticCompositeCandidates r (N + 1)) S :=
    ⟨RootQuotientSemanticCompositeCandidates r (N + 1),
      semanticCompositeCandidates_finite r (N + 1),
      semanticCompositeCandidates_cover_primeHardTargets hh⟩
  obtain ⟨S, hSFinite, hCoverNew, hSCardRaw⟩ :=
    exists_minimumRepairDivisorCover hFeasible
  have hSCard : S.ncard =
      rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h := by
    simpa [rootQuotientGlobalRepairDivisorCoverNumber] using hSCardRaw
  let S₀ := S ∩ RootQuotientSemanticCompositeCandidates r N
  have hS₀Finite : S₀.Finite := hSFinite.subset Set.inter_subset_left
  have hCoverOld : RootQuotientRepairDivisorCover
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N) S₀ :=
    restrict_next_globalRepairCover_to_old hSFinite hCoverNew
  have hTauOldLe : rootQuotientGlobalRepairDivisorCoverNumber r N h ≤ S₀.ncard := by
    unfold rootQuotientGlobalRepairDivisorCoverNumber
    exact rootQuotientRepairDivisorCoverNumber_le hS₀Finite hCoverOld
  have hSLeS₀ : S.ncard ≤ S₀.ncard := by
    rw [hSCard, hEq]
    exact hTauOldLe
  have hS₀EqS : S₀ = S :=
    Set.eq_of_subset_of_ncard_le Set.inter_subset_left hSLeS₀ hSFinite
  rw [hS₀EqS] at hCoverOld
  have hSCardOld : S.ncard = rootQuotientGlobalRepairDivisorCoverNumber r N h := by
    rw [hSCard, hEq]
  have hBirthTarget := prime_birth_mem_primeHardSemanticTargetFinset
    hr hh hp hBirth hBinaryNext
  obtain ⟨g, hgS, hgDvd⟩ := hCoverNew.2 (N + 1) hBirthTarget
  have hgOld : g ∈ RootQuotientSemanticCompositeCandidates r N :=
    hCoverOld.1 hgS
  have hgServe : RootQuotientMacroServesPrimeDirection g p := by
    apply macroServesPrimeDirection_of_dvd_primePow hp hgOld.1.1
    simpa [hBirth] using hgDvd
  obtain ⟨e, hePos, hgPow⟩ := hgServe
  have heBounds := prime_preinvestment_exponent_bounds_of_old_candidate
    hh hp hBirth hgOld hgPow hePos
  exact ⟨S, hSFinite, hCoverOld, hSCardOld,
    ⟨e, heBounds.1, heBounds.2, by rw [← hgPow]; exact hgS⟩⟩

/-- An old minimum divisor cover that already stores a useful `p^e` covers the
new pure target `p^(h+1)` at no extra type cost. -/
theorem coverNumber_eq_at_prime_birth_of_coverPrimeDirectionPreinvestment
    {r N h p : ℕ}
    (hh : 1 ≤ h)
    (hBirth : N + 1 = p ^ (h + 1))
    (hPre : RootQuotientCoverPrimeDirectionPreinvestment r N h p) :
    rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h =
      rootQuotientGlobalRepairDivisorCoverNumber r N h := by
  obtain ⟨S, hSFinite, hCoverOld, hSCard, e, heTwo, heLe, heMem⟩ := hPre
  have hCandidateNew : S ⊆ RootQuotientSemanticCompositeCandidates r (N + 1) :=
    fun g hg => semanticCompositeCandidates_mono_stateBound
      (r := r) (Nat.le_succ N) (hCoverOld.1 hg)
  have hCoverNew : RootQuotientRepairDivisorCover
      (RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
      (RootQuotientSemanticCompositeCandidates r (N + 1)) S := by
    constructor
    · exact hCandidateNew
    · intro t ht
      by_cases htNew : t = N + 1
      · subst t
        refine ⟨p ^ e, heMem, ?_⟩
        rw [hBirth]
        exact pow_dvd_pow p (by omega)
      · have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
        have htN : t ≤ N := by omega
        have htOld : t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h :=
          (mem_primeHardSemanticTargetFinset_iff).2
            ⟨⟨htMem.1.1, htN, htMem.1.2.2⟩, htMem.2⟩
        exact hCoverOld.2 t htOld
  have hUpper : rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h ≤ S.ncard := by
    unfold rootQuotientGlobalRepairDivisorCoverNumber
    exact rootQuotientRepairDivisorCoverNumber_le hSFinite hCoverNew
  rw [hSCard] at hUpper
  have hLower := globalRepairDivisorCoverNumber_mono_succ
    (r := r) (N := N) (h := h) hh
  omega

/-- Divisor-cover no-jump at a hard-prime birth is exactly old cover
preinvestment in that future prime direction. -/
theorem coverNumber_eq_at_prime_birth_iff_coverPrimeDirectionPreinvestment
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h =
        rootQuotientGlobalRepairDivisorCoverNumber r N h ↔
      RootQuotientCoverPrimeDirectionPreinvestment r N h p := by
  constructor
  · exact coverPrimeDirectionPreinvestment_of_coverNumber_eq_at_prime_birth
      hr hh hp hBirth hBinaryNext
  · exact coverNumber_eq_at_prime_birth_of_coverPrimeDirectionPreinvestment
      hh hBirth

/-- Event-component form: exact-storage component zero is exactly exact-layer
preinvestment at a hard-prime birth. -/
theorem exactEvent_zero_iff_exactPrimeDirectionPreinvestment
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    (rootQuotientResourceEvent r N h).exactStorage = 0 ↔
      RootQuotientExactPrimeDirectionPreinvestment r N h p := by
  have hMono := minimumCompositeMacroCount_mono_succ
    (r := r) (N := N) (h := h) hr hh
  constructor
  · intro hZero
    have hEq : rootQuotientMinimumCompositeMacroCount r (N + 1) h =
        rootQuotientMinimumCompositeMacroCount r N h := by
      dsimp [rootQuotientResourceEvent] at hZero
      omega
    exact (macroCount_eq_at_prime_birth_iff_exactPrimeDirectionPreinvestment
      hr hh hp hBirth hBinaryNext).1 hEq
  · intro hPre
    have hEq :=
      (macroCount_eq_at_prime_birth_iff_exactPrimeDirectionPreinvestment
        hr hh hp hBirth hBinaryNext).2 hPre
    dsimp [rootQuotientResourceEvent]
    omega

/-- Event-component form: divisor-cover component zero is exactly cover-layer
preinvestment at a hard-prime birth. -/
theorem coverEvent_zero_iff_coverPrimeDirectionPreinvestment
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    (rootQuotientResourceEvent r N h).divisorCover = 0 ↔
      RootQuotientCoverPrimeDirectionPreinvestment r N h p := by
  have hMono := globalRepairDivisorCoverNumber_mono_succ
    (r := r) (N := N) (h := h) hh
  constructor
  · intro hZero
    have hEq : rootQuotientGlobalRepairDivisorCoverNumber r (N + 1) h =
        rootQuotientGlobalRepairDivisorCoverNumber r N h := by
      dsimp [rootQuotientResourceEvent] at hZero
      omega
    exact (coverNumber_eq_at_prime_birth_iff_coverPrimeDirectionPreinvestment
      hr hh hp hBirth hBinaryNext).1 hEq
  · intro hPre
    have hEq :=
      (coverNumber_eq_at_prime_birth_iff_coverPrimeDirectionPreinvestment
        hr hh hp hBirth hBinaryNext).2 hPre
    dsimp [rootQuotientResourceEvent]
    omega

/-- **Dual catch-up = exact-only preinvestment.**

At a hard-prime birth, once the direction component is known to jump, the
previously unresolved event `(1,1,0)` occurs exactly when the old exact-optimal
layer has preinvested in the future prime direction but the old divisor-cover
optimal layer has not. -/
theorem dualCatchupEvent_iff_exactOnlyPrimeDirectionPreinvestment
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r)
    (hDirectionBirth : (rootQuotientResourceEvent r N h).direction = 1) :
    rootQuotientResourceEvent r N h = rootQuotientDualCatchupEvent ↔
      ¬RootQuotientCoverPrimeDirectionPreinvestment r N h p ∧
      RootQuotientExactPrimeDirectionPreinvestment r N h p := by
  have hCoverBits := rootQuotientResourceEvent_components_zero_or_one hr hh |>.2.1
  have hExactBits := rootQuotientResourceEvent_components_zero_or_one hr hh |>.2.2
  constructor
  · intro hEvent
    constructor
    · intro hCoverPre
      have hCoverZero :=
        (coverEvent_zero_iff_coverPrimeDirectionPreinvestment
          hr hh hp hBirth hBinaryNext).2 hCoverPre
      rw [hEvent] at hCoverZero
      norm_num [rootQuotientDualCatchupEvent] at hCoverZero
    · have hExactZero : (rootQuotientResourceEvent r N h).exactStorage = 0 := by
        rw [hEvent]
        rfl
      exact (exactEvent_zero_iff_exactPrimeDirectionPreinvestment
        hr hh hp hBirth hBinaryNext).1 hExactZero
  · rintro ⟨hNoCoverPre, hExactPre⟩
    have hExactZero :=
      (exactEvent_zero_iff_exactPrimeDirectionPreinvestment
        hr hh hp hBirth hBinaryNext).2 hExactPre
    have hCoverNotZero : (rootQuotientResourceEvent r N h).divisorCover ≠ 0 := by
      intro hZero
      exact hNoCoverPre
        ((coverEvent_zero_iff_coverPrimeDirectionPreinvestment
          hr hh hp hBirth hBinaryNext).1 hZero)
    have hCoverOne : (rootQuotientResourceEvent r N h).divisorCover = 1 := by
      rcases hCoverBits with hZero | hOne
      · exact (hCoverNotZero hZero).elim
      · exact hOne
    apply RootQuotientResourceEvent.ext
    · exact hDirectionBirth.trans rfl
    · exact hCoverOne.trans rfl
    · exact hExactZero.trans rfl

end EnterpriseMath.Quotient
