import EnterpriseMath.Quotient.RootQuotientMixedOverheadFlow
import EnterpriseMath.Quotient.RootQuotientMacroStorageStaircase
import EnterpriseMath.Quotient.RootQuotientResourceStaircase
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A dictionary has preinvested in future prime direction `p` at horizon `h`
when it already stores a nontrivial pure `p`-power `p^e` with `2 ≤ e ≤ h`.

Such a macro is available *before* the hard target `p^(h+1)` itself enters the
state domain. -/
def RootQuotientPrimeDirectionPreinvestment
    (p h : ℕ) (S : Set ℕ) : Prop :=
  ∃ e : ℕ, 2 ≤ e ∧ e ≤ h ∧ p ^ e ∈ S

/-- Exact-storage preinvestment: some old-domain minimum composite-macro
presentation already stores a useful pure power of the future hard prime. -/
def RootQuotientExactPrimeDirectionPreinvestment
    (r N h p : ℕ) : Prop :=
  ∃ S : Set ℕ,
    RootQuotientCompositeMacroPresentation r N h S ∧
    S.ncard = rootQuotientMinimumCompositeMacroCount r N h ∧
    RootQuotientPrimeDirectionPreinvestment p h S

/-- Divisor-cover preinvestment: some old-domain minimum first-order cover
already stores a useful pure power of the future hard prime. -/
def RootQuotientCoverPrimeDirectionPreinvestment
    (r N h p : ℕ) : Prop :=
  ∃ S : Set ℕ,
    S.Finite ∧
    RootQuotientRepairDivisorCover
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N) S ∧
    S.ncard = rootQuotientGlobalRepairDivisorCoverNumber r N h ∧
    RootQuotientPrimeDirectionPreinvestment p h S

/-- The entering prime-power state is prime-hard in the high-root regime. -/
theorem prime_birth_mem_primeHardSemanticTargetFinset
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    N + 1 ∈ RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h := by
  have hPos : 1 ≤ N + 1 := by omega
  have hFree : RPowerFree r (N + 1) :=
    rPowerFree_of_lt_two_pow_rootOrder hPos hBinaryNext
  have hpCount : rootQuotientPrimeFactorCount p = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hp]
    simp
  have hCount : rootQuotientPrimeFactorCount (N + 1) = h + 1 := by
    rw [hBirth, rootQuotientPrimeFactorCount_pow hp.one_le, hpCount]
    simp
  apply (mem_primeHardSemanticTargetFinset_iff).2
  exact ⟨⟨by omega, le_rfl, hFree⟩, by omega⟩

/-- At a prime birth, a useful preinvestment exponent really lies before the
new hard shell. -/
theorem prime_preinvestment_exponent_bounds_of_old_candidate
    {r N h p g e : ℕ}
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hgOld : g ∈ RootQuotientSemanticCompositeCandidates r N)
    (hgPow : g = p ^ e)
    (hePos : 1 ≤ e) :
    2 ≤ e ∧ e ≤ h := by
  have hpLtBirth : p < p ^ (h + 1) := by
    calc
      p = p ^ 1 := by simp
      _ < p ^ (h + 1) := pow_lt_pow_right' hp.one_lt (by omega)
  have hpN : p ≤ N := by
    rw [← hBirth] at hpLtBirth
    omega
  have heTwo : 2 ≤ e := by
    by_contra hNot
    have heOne : e = 1 := by omega
    have hgPrime : g ∈ RootQuotientPrimeBasis N := by
      rw [hgPow, heOne, pow_one]
      exact ⟨hp, hpN⟩
    exact hgOld.2 hgPrime
  have heLe : e ≤ h := by
    by_contra hNot
    have hPowLe : p ^ (h + 1) ≤ p ^ e :=
      pow_le_pow_right' hp.one_le (by omega)
    have hgN : g ≤ N := hgOld.1.2.1
    rw [← hBirth, ← hgPow] at hPowLe
    omega
  exact ⟨heTwo, heLe⟩

/-- Restrict a next-state exact optimum to the old semantic candidate range.
The restricted dictionary still repairs every old prime-hard target. -/
theorem restrict_next_composite_presentation_to_old_primeHard
    {r N h : ℕ} {S : Set ℕ}
    (hS : RootQuotientCompositeMacroPresentation r (N + 1) h S) :
    RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis N)
      h
      (RootQuotientPrimeHardSemanticTargetFinset r N h)
      (RootQuotientSemanticCompositeCandidates r N)
      (S ∩ RootQuotientSemanticCompositeCandidates r N) := by
  let S₀ := S ∩ RootQuotientSemanticCompositeCandidates r N
  have hS₀Finite : S₀.Finite := hS.1.subset Set.inter_subset_left
  have hS₀Candidate : S₀ ⊆ RootQuotientSemanticCompositeCandidates r N :=
    Set.inter_subset_right
  have hFullNew : RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis (N + 1)) h
      (RootQuotientSemanticTargetFinset r (N + 1))
      (RootQuotientSemanticCompositeCandidates r (N + 1)) S :=
    (compositeMacroPresentation_iff_relativeRepairPresentation (by omega)).1 hS
  have hHardNew :=
    (relativeRepairPresentation_fullSemantic_iff_primeHard).1 hFullNew
  refine ⟨hS₀Finite, hS₀Candidate, ?_⟩
  intro b hbHard
  have hbHardNew := primeHardSemanticTargetFinset_mono_stateBound
    (r := r) (h := h) (Nat.le_succ N) hbHard
  obtain ⟨w, hwLen, hwLarge, hProd⟩ := hHardNew.2.2 b hbHardNew
  have hbMem := (mem_primeHardSemanticTargetFinset_iff).1 hbHard
  refine ⟨w, hwLen, ?_, hProd⟩
  exact word_over_larger_presentation_restricts_to_old_range
    (r := r) (N := N) (h := h)
    (b := b) (S := S) (w := w)
    (by omega) hbMem.1.2.1 hS.2.1 hwLarge hProd

/-- **Exact no-jump implies exact preinvestment.**

If optional-macro storage does not increase when the new state is exactly the
hard prime power `p^(h+1)`, then some old-domain exact optimum already contained
a useful pure `p`-power. -/
theorem exactPrimeDirectionPreinvestment_of_macroCount_eq_at_prime_birth
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r)
    (hEq : rootQuotientMinimumCompositeMacroCount r (N + 1) h =
      rootQuotientMinimumCompositeMacroCount r N h) :
    RootQuotientExactPrimeDirectionPreinvestment r N h p := by
  obtain ⟨S, hSNew, hSCard⟩ :=
    exists_rootQuotientMinimumCompositeMacroPresentation
      (r := r) (N := N + 1) (h := h) hr hh
  let S₀ := S ∩ RootQuotientSemanticCompositeCandidates r N
  have hHardOld := restrict_next_composite_presentation_to_old_primeHard hSNew
  have hFullOld := (relativeRepairPresentation_fullSemantic_iff_primeHard).2 hHardOld
  have hCompOld : RootQuotientCompositeMacroPresentation r N h S₀ :=
    (compositeMacroPresentation_iff_relativeRepairPresentation hr).2 hFullOld
  have hMuOldLe : rootQuotientMinimumCompositeMacroCount r N h ≤ S₀.ncard :=
    rootQuotientMinimumCompositeMacroCount_le hCompOld
  have hCardLe : S₀.ncard ≤ S.ncard :=
    Set.ncard_le_ncard Set.inter_subset_left hSNew.1
  have hSLeS₀ : S.ncard ≤ S₀.ncard := by
    rw [hSCard, hEq]
    exact hMuOldLe
  have hS₀EqS : S₀ = S :=
    Set.eq_of_subset_of_ncard_le Set.inter_subset_left hSLeS₀ hSNew.1
  have hCompOldS : RootQuotientCompositeMacroPresentation r N h S := by
    simpa [S₀, hS₀EqS] using hCompOld
  have hSCardOld : S.ncard = rootQuotientMinimumCompositeMacroCount r N h := by
    rw [hSCard, hEq]
  have hpHard : p ∈ RootQuotientHardPrimeDirections (N + 1) h := by
    refine ⟨hp, ?_⟩
    rw [← hBirth]
  obtain ⟨g, hgS, hgServe⟩ :=
    exists_macro_serving_hardPrimeDirection_of_separator
      hr hBinaryNext hSNew.2.1 hSNew.2.2 hpHard
  obtain ⟨e, hePos, hgPow⟩ := hgServe
  have hgOld : g ∈ RootQuotientSemanticCompositeCandidates r N :=
    hCompOldS.2.1 hgS
  have heBounds := prime_preinvestment_exponent_bounds_of_old_candidate
    hh hp hBirth hgOld hgPow hePos
  exact ⟨S, hCompOldS, hSCardOld,
    ⟨e, heBounds.1, heBounds.2, by rw [← hgPow]; exact hgS⟩⟩

/-- A preinvested old exact optimum already compiles the entering hard prime
power without increasing dictionary size. -/
theorem macroCount_eq_at_prime_birth_of_exactPrimeDirectionPreinvestment
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hPre : RootQuotientExactPrimeDirectionPreinvestment r N h p) :
    rootQuotientMinimumCompositeMacroCount r (N + 1) h =
      rootQuotientMinimumCompositeMacroCount r N h := by
  obtain ⟨S, hSOld, hSCard, e, heTwo, heLe, heMem⟩ := hPre
  have hFullOld :=
    (compositeMacroPresentation_iff_relativeRepairPresentation hr).1 hSOld
  have hHardOld :=
    (relativeRepairPresentation_fullSemantic_iff_primeHard).1 hFullOld
  have hSCandidateNew : S ⊆ RootQuotientSemanticCompositeCandidates r (N + 1) :=
    fun g hg => semanticCompositeCandidates_mono_stateBound
      (r := r) (Nat.le_succ N) (hSOld.2.1 hg)
  have hpLeNext : p ≤ N + 1 := by
    calc
      p ≤ p ^ (h + 1) := le_self_pow hp.one_le (by omega)
      _ = N + 1 := hBirth.symm
  have hpPrimeNext : p ∈ RootQuotientPrimeBasis (N + 1) := ⟨hp, hpLeNext⟩
  have hHardNew : RootQuotientRelativeRepairPresentation
      (RootQuotientPrimeBasis (N + 1)) h
      (RootQuotientPrimeHardSemanticTargetFinset r (N + 1) h)
      (RootQuotientSemanticCompositeCandidates r (N + 1)) S := by
    refine ⟨hSOld.1, hSCandidateNew, ?_⟩
    intro t ht
    by_cases htNew : t = N + 1
    · subst t
      let w := [p ^ e] ++ List.replicate (h + 1 - e) p
      refine ⟨w, ?_, ?_, ?_⟩
      · dsimp [w]
        simp
        omega
      · intro g hg
        dsimp [w] at hg
        simp at hg
        rcases hg with hgMacro | hgPrime
        · subst g
          exact Or.inr (hSCandidateNew heMem)
        · subst g
          exact Or.inl hpPrimeNext
      · calc
          N + 1 = p ^ (h + 1) := hBirth
          _ = p ^ (e + (h + 1 - e)) := by congr 1 <;> omega
          _ = p ^ e * p ^ (h + 1 - e) := by rw [pow_add]
          _ = rootQuotientWordProduct w := by
            dsimp [w]
            rw [rootQuotientWordProduct_eq_prod]
            simp [List.prod_append, List.prod_replicate]
    · have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
      have htN : t ≤ N := by omega
      have htOld : t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h :=
        (mem_primeHardSemanticTargetFinset_iff).2
          ⟨⟨htMem.1.1, htN, htMem.1.2.2⟩, htMem.2⟩
      have hReachOld := hHardOld.2.2 t htOld
      exact rootQuotientProductReachableWithin_mono_generators
        (old_presentation_subset_next_with_spares
          (r := r) (N := N) (S := S) (S' := S) Set.Subset.rfl)
        hReachOld
  have hFullNew := (relativeRepairPresentation_fullSemantic_iff_primeHard).2 hHardNew
  have hCompNew : RootQuotientCompositeMacroPresentation r (N + 1) h S :=
    (compositeMacroPresentation_iff_relativeRepairPresentation hr).2 hFullNew
  have hUpper := rootQuotientMinimumCompositeMacroCount_le hCompNew
  rw [hSCard] at hUpper
  have hLower := minimumCompositeMacroCount_mono_succ
    (r := r) (N := N) (h := h) hr hh
  omega

/-- Exact-storage no-jump at a hard-prime birth is *equivalent* to old exact
preinvestment in that future prime direction. -/
theorem macroCount_eq_at_prime_birth_iff_exactPrimeDirectionPreinvestment
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hBinaryNext : N + 1 < 2 ^ r) :
    rootQuotientMinimumCompositeMacroCount r (N + 1) h =
        rootQuotientMinimumCompositeMacroCount r N h ↔
      RootQuotientExactPrimeDirectionPreinvestment r N h p := by
  constructor
  · exact exactPrimeDirectionPreinvestment_of_macroCount_eq_at_prime_birth
      hr hh hp hBirth hBinaryNext
  · exact macroCount_eq_at_prime_birth_of_exactPrimeDirectionPreinvestment
      hr hh hp hBirth

end EnterpriseMath.Quotient
