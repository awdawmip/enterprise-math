import EnterpriseMath.Quotient.RootQuotientRelativeRepairCover
import EnterpriseMath.Quotient.RootQuotientPenultimateStorage
import Mathlib.Data.Set.Card
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A semantic-semiprime divisor cover of an arbitrary finite target family. -/
def RootQuotientRepairSemiprimeCover
    (r N : ℕ) (T : Finset ℕ) (S : Set ℕ) : Prop :=
  RootQuotientPenultimateSemiprimeFamily r N S ∧
  ∀ t ∈ T, ∃ g : ℕ, g ∈ S ∧ g ∣ t

/-- Feasible finite semantic-semiprime cover cardinalities for an arbitrary
target family. -/
def RootQuotientRepairSemiprimeCoverCardinalities
    (r N : ℕ) (T : Finset ℕ) : Set ℕ :=
  {m : ℕ | ∃ S : Set ℕ,
    S.Finite ∧
    RootQuotientRepairSemiprimeCover r N T S ∧
    S.ncard = m}

/-- Minimum semantic-semiprime divisor-cover size for an arbitrary finite target
family. -/
noncomputable def rootQuotientRepairSemiprimeCoverNumber
    (r N : ℕ) (T : Finset ℕ) : ℕ :=
  sInf (RootQuotientRepairSemiprimeCoverCardinalities r N T)

/-- Any semantic-semiprime cover is also a general semantic-composite divisor
cover. -/
theorem repairSemiprimeCover_is_semanticCompositeDivisorCover
    {r N : ℕ} {T : Finset ℕ} {S : Set ℕ}
    (hSemi : RootQuotientRepairSemiprimeCover r N T S) :
    RootQuotientRepairDivisorCover
      T (RootQuotientSemanticCompositeCandidates r N) S := by
  constructor
  · intro g hgS
    have hgSemantic := hSemi.1.1 hgS
    refine ⟨hgSemantic, ?_⟩
    intro hgPrime
    have hPrimeCount : rootQuotientPrimeFactorCount g = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime hgPrime.1]
      simp
    have hSemiCount := hSemi.1.2 g hgS
    omega
  · exact hSemi.2

/-- **General semiprime projection.**

Every finite semantic-composite divisor cover of an arbitrary target family can
be projected, macro by macro, to semantic semiprime divisors without losing any
covered target and without increasing the number of stored types. -/
theorem exists_semiprimeRepairCover_ncard_le_of_semanticCompositeCover
    {r N : ℕ} {T : Finset ℕ} {S : Set ℕ}
    (hSFinite : S.Finite)
    (hCover : RootQuotientRepairDivisorCover
      T (RootQuotientSemanticCompositeCandidates r N) S) :
    ∃ S' : Set ℕ,
      S'.Finite ∧
      RootQuotientRepairSemiprimeCover r N T S' ∧
      S'.ncard ≤ S.ncard := by
  classical
  let f : ℕ → ℕ := rootQuotientChosenSemiprimeDivisor r N
  let S' : Set ℕ := f '' S
  have hRank : ∀ g : ℕ, g ∈ S →
      2 ≤ rootQuotientPrimeFactorCount g := by
    intro g hgS
    have hgC := hCover.1 hgS
    have hgSemantic := hgC.1
    have hCountPos : 0 < rootQuotientPrimeFactorCount g :=
      rootQuotientPrimeFactorCount_pos_of_two_le hgSemantic.1
    by_contra hNot
    have hCountOne : rootQuotientPrimeFactorCount g = 1 := by omega
    have hgPrime : g.Prime :=
      (rootQuotientPrimeFactorCount_eq_one_iff_prime hgSemantic.1).1 hCountOne
    exact hgC.2 ⟨hgPrime, hgSemantic.2.1⟩
  have hS'Finite : S'.Finite := hSFinite.image f
  have hSemiFamily : RootQuotientPenultimateSemiprimeFamily r N S' := by
    constructor
    · intro d hd
      rcases hd with ⟨g, hgS, rfl⟩
      exact (rootQuotientChosenSemiprimeDivisor_spec
        (hCover.1 hgS).1 (hRank g hgS)).1
    · intro d hd
      rcases hd with ⟨g, hgS, rfl⟩
      exact (rootQuotientChosenSemiprimeDivisor_spec
        (hCover.1 hgS).1 (hRank g hgS)).2.1
  have hTargets : ∀ t ∈ T, ∃ d : ℕ, d ∈ S' ∧ d ∣ t := by
    intro t ht
    obtain ⟨g, hgS, hgDvd⟩ := hCover.2 t ht
    have hSpec := rootQuotientChosenSemiprimeDivisor_spec
      (hCover.1 hgS).1 (hRank g hgS)
    exact ⟨f g, ⟨g, hgS, rfl⟩, hSpec.2.2.trans hgDvd⟩
  have hCard : S'.ncard ≤ S.ncard := by
    dsimp [S']
    exact Set.ncard_image_le hSFinite
  exact ⟨S', hS'Finite, ⟨hSemiFamily, hTargets⟩, hCard⟩

/-- The complete semantic-semiprime candidate set covers every semantic
composite target by choosing a semiprime divisor of that target. -/
theorem allSemanticSemiprimes_cover_semanticCompositeTargets
    {r N : ℕ} {T : Finset ℕ}
    (hTargets : ∀ t ∈ T,
      t ∈ RootQuotientSemanticCompositeCandidates r N) :
    RootQuotientRepairSemiprimeCover
      r N T (RootQuotientAllSemanticSemiprimes r N) := by
  refine ⟨allSemanticSemiprimes_is_family, ?_⟩
  intro t ht
  have htC := hTargets t ht
  have hCountPos : 0 < rootQuotientPrimeFactorCount t :=
    rootQuotientPrimeFactorCount_pos_of_two_le htC.1.1
  have hNotOne : rootQuotientPrimeFactorCount t ≠ 1 := by
    intro hOne
    have htPrime : t.Prime :=
      (rootQuotientPrimeFactorCount_eq_one_iff_prime htC.1.1).1 hOne
    exact htC.2 ⟨htPrime, htC.1.2.1⟩
  have hRank : 2 ≤ rootQuotientPrimeFactorCount t := by omega
  obtain ⟨d, hdSemantic, hdCount, hdDvd⟩ :=
    exists_semiprime_semantic_divisor htC.1 hRank
  exact ⟨d, ⟨hdSemantic, hdCount⟩, hdDvd⟩

/-- The general semiprime-cover minimum is attained whenever every target is a
semantic composite candidate. -/
theorem exists_minimumRepairSemiprimeCover
    {r N : ℕ} {T : Finset ℕ}
    (hTargets : ∀ t ∈ T,
      t ∈ RootQuotientSemanticCompositeCandidates r N) :
    ∃ S : Set ℕ,
      S.Finite ∧
      RootQuotientRepairSemiprimeCover r N T S ∧
      S.ncard = rootQuotientRepairSemiprimeCoverNumber r N T := by
  have hAll := allSemanticSemiprimes_cover_semanticCompositeTargets hTargets
  have hAllFinite : (RootQuotientAllSemanticSemiprimes r N).Finite :=
    rootQuotientNontrivialPowerFreeBasis_finite.subset fun d hd => hd.1
  have hNonempty : (RootQuotientRepairSemiprimeCoverCardinalities r N T).Nonempty :=
    ⟨(RootQuotientAllSemanticSemiprimes r N).ncard,
      RootQuotientAllSemanticSemiprimes r N,
      hAllFinite, hAll, rfl⟩
  have hMem : rootQuotientRepairSemiprimeCoverNumber r N T ∈
      RootQuotientRepairSemiprimeCoverCardinalities r N T :=
    Nat.sInf_mem hNonempty
  exact hMem

/-- **Arbitrary-horizon divisor-cover semiprime reduction.**

For any finite family of bounded semantic composite targets, minimum cover by
arbitrary semantic composite macros equals minimum cover by semantic
semiprimes. -/
theorem repairDivisorCoverNumber_eq_semiprimeCoverNumber
    {r N : ℕ} {T : Finset ℕ}
    (hTargets : ∀ t ∈ T,
      t ∈ RootQuotientSemanticCompositeCandidates r N) :
    rootQuotientRepairDivisorCoverNumber
        T (RootQuotientSemanticCompositeCandidates r N) =
      rootQuotientRepairSemiprimeCoverNumber r N T := by
  apply Nat.le_antisymm
  · obtain ⟨S, hSFinite, hSemi, hSCard⟩ :=
      exists_minimumRepairSemiprimeCover hTargets
    have hGeneric := repairSemiprimeCover_is_semanticCompositeDivisorCover hSemi
    have hLe := rootQuotientRepairDivisorCoverNumber_le hSFinite hGeneric
    rw [hSCard] at hLe
    exact hLe
  · have hAll := allSemanticSemiprimes_cover_semanticCompositeTargets hTargets
    have hAllFinite : (RootQuotientAllSemanticSemiprimes r N).Finite :=
      rootQuotientNontrivialPowerFreeBasis_finite.subset fun d hd => hd.1
    have hFeasible : ∃ S : Set ℕ,
        S.Finite ∧
        RootQuotientRepairDivisorCover
          T (RootQuotientSemanticCompositeCandidates r N) S :=
      ⟨RootQuotientAllSemanticSemiprimes r N,
        hAllFinite,
        repairSemiprimeCover_is_semanticCompositeDivisorCover hAll⟩
    obtain ⟨S, hSFinite, hCover, hSCard⟩ :=
      exists_minimumRepairDivisorCover hFeasible
    obtain ⟨S', hS'Finite, hSemi, hS'Le⟩ :=
      exists_semiprimeRepairCover_ncard_le_of_semanticCompositeCover
        hSFinite hCover
    have hTauLe : rootQuotientRepairSemiprimeCoverNumber r N T ≤ S'.ncard := by
      apply Nat.sInf_le
      exact ⟨S', hS'Finite, hSemi, rfl⟩
    rw [hSCard] at hS'Le
    exact hTauLe.trans hS'Le

/-- Every prime-hard semantic target is a semantic composite candidate. -/
theorem primeHardSemanticTarget_mem_semanticCompositeCandidates
    {r N h t : ℕ}
    (hh : 1 ≤ h)
    (ht : t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h) :
    t ∈ RootQuotientSemanticCompositeCandidates r N := by
  have htMem := (mem_primeHardSemanticTargetFinset_iff).1 ht
  refine ⟨htMem.1, ?_⟩
  intro htPrime
  have hOne : rootQuotientPrimeFactorCount t = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime htPrime.1]
    simp
  omega

/-- **Global cover layer is always a semiprime edge-hitting problem.** -/
theorem globalRepairDivisorCoverNumber_eq_semiprimeCoverNumber
    {r N h : ℕ}
    (hh : 1 ≤ h) :
    rootQuotientGlobalRepairDivisorCoverNumber r N h =
      rootQuotientRepairSemiprimeCoverNumber
        r N (RootQuotientPrimeHardSemanticTargetFinset r N h) := by
  unfold rootQuotientGlobalRepairDivisorCoverNumber
  apply repairDivisorCoverNumber_eq_semiprimeCoverNumber
  intro t ht
  exact primeHardSemanticTarget_mem_semanticCompositeCandidates hh ht

end EnterpriseMath.Quotient
