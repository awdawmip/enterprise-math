import EnterpriseMath.Quotient.RootQuotientMinimumStoragePhase
import EnterpriseMath.Quotient.RootQuotientPenultimateSemiprimeCover
import Mathlib.Data.Set.Card
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A total choice function that selects one semantic semiprime divisor from
any bounded semantic macro carrying at least two prime-factor tokens.  Outside
that domain it returns the harmless default `1`. -/
noncomputable def rootQuotientChosenSemiprimeDivisor
    (r N g : ℕ) : ℕ :=
  if h :
      g ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
      2 ≤ rootQuotientPrimeFactorCount g then
    Classical.choose (exists_semiprime_semantic_divisor h.1 h.2)
  else
    1

/-- Specification of the chosen semiprime divisor on its intended domain. -/
theorem rootQuotientChosenSemiprimeDivisor_spec
    {r N g : ℕ}
    (hgSemantic : g ∈ RootQuotientNontrivialPowerFreeBasis r N)
    (hgRank : 2 ≤ rootQuotientPrimeFactorCount g) :
    rootQuotientChosenSemiprimeDivisor r N g ∈
        RootQuotientNontrivialPowerFreeBasis r N ∧
      rootQuotientPrimeFactorCount
          (rootQuotientChosenSemiprimeDivisor r N g) = 2 ∧
      rootQuotientChosenSemiprimeDivisor r N g ∣ g := by
  classical
  unfold rootQuotientChosenSemiprimeDivisor
  rw [dif_pos ⟨hgSemantic, hgRank⟩]
  exact Classical.choose_spec
    (exists_semiprime_semantic_divisor hgSemantic hgRank)

/-- The useful composite semantic part of a primitive alphabet. -/
def RootQuotientUsefulCompositePart
    (r N : ℕ) (G : Set ℕ) : Set ℕ :=
  {g : ℕ |
    g ∈ G ∧
    g ∈ RootQuotientNontrivialPowerFreeBasis r N ∧
    2 ≤ rootQuotientPrimeFactorCount g}

/-- Useful composite semantic instructions are genuinely outside the forced
prime core. -/
theorem rootQuotientUsefulCompositePart_subset_primeComplement
    {r N : ℕ} {G : Set ℕ} :
    RootQuotientUsefulCompositePart r N G ⊆
      G \ RootQuotientPrimeBasis N := by
  intro g hg
  refine ⟨hg.1, ?_⟩
  intro hgPrime
  have hPrimeCount : rootQuotientPrimeFactorCount g = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hgPrime.1]
    simp
  omega

/-- Every finite penultimate separator admits a semantic-semiprime divisor
cover using no more macro types than its non-prime part.

This is the cardinality-preserving reduction that turns the general
penultimate dictionary problem into semiprime set cover. -/
theorem exists_semiprime_cover_le_nonprime_storage_of_penultimate_separator
    {r N : ℕ} {G : Set ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N)
    (hGFinite : G.Finite)
    (hGPos : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo
      r N (rootQuotientPrimeHorizon r N - 1) G) :
    ∃ S : Set ℕ,
      S.Finite ∧
      RootQuotientPenultimateSemiprimeFamily r N S ∧
      RootQuotientPenultimateDivisorCover r N S ∧
      S.ncard ≤ (G \ RootQuotientPrimeBasis N).ncard := by
  classical
  let C := RootQuotientUsefulCompositePart r N G
  let f : ℕ → ℕ := rootQuotientChosenSemiprimeDivisor r N
  let S : Set ℕ := f '' C
  have hCSubG : C ⊆ G := by
    intro g hg
    exact hg.1
  have hCFinite : C.Finite := hGFinite.subset hCSubG
  have hSFinite : S.Finite := hCFinite.image f
  have hSemi : RootQuotientPenultimateSemiprimeFamily r N S := by
    constructor
    · intro d hd
      rcases hd with ⟨g, hgC, rfl⟩
      exact (rootQuotientChosenSemiprimeDivisor_spec hgC.2.1 hgC.2.2).1
    · intro d hd
      rcases hd with ⟨g, hgC, rfl⟩
      exact (rootQuotientChosenSemiprimeDivisor_spec hgC.2.1 hgC.2.2).2.1
  have hCover : RootQuotientPenultimateDivisorCover r N S := by
    intro b hbMax
    obtain ⟨g, hgG, hgSemantic, hgRank, hgDvd⟩ :=
      exists_composite_semantic_divisor_of_penultimate_separator
        hr hHorizon hGPos hSep hbMax
    have hgC : g ∈ C := ⟨hgG, hgSemantic, hgRank⟩
    have hSpec := rootQuotientChosenSemiprimeDivisor_spec hgSemantic hgRank
    exact ⟨f g, ⟨g, hgC, rfl⟩, hSpec.2.2.trans hgDvd⟩
  have hImageCard : S.ncard ≤ C.ncard := by
    dsimp [S]
    exact Set.ncard_image_le hCFinite
  have hCSubDiff : C ⊆ G \ RootQuotientPrimeBasis N := by
    dsimp [C]
    exact rootQuotientUsefulCompositePart_subset_primeComplement
  have hDiffFinite : (G \ RootQuotientPrimeBasis N).Finite :=
    hGFinite.sdiff rootQuotientPrimeBasis_finite
  have hPartCard : C.ncard ≤ (G \ RootQuotientPrimeBasis N).ncard :=
    Set.ncard_le_ncard hCSubDiff hDiffFinite
  exact ⟨S, hSFinite, hSemi, hCover, hImageCard.trans hPartCard⟩

/-- Cardinalities of finite semantic-semiprime divisor covers of all
maximal-rank boundaries. -/
def RootQuotientPenultimateSemiprimeCoverCardinalities
    (r N : ℕ) : Set ℕ :=
  {m : ℕ | ∃ S : Set ℕ,
    S.Finite ∧
    RootQuotientPenultimateSemiprimeFamily r N S ∧
    RootQuotientPenultimateDivisorCover r N S ∧
    S.ncard = m}

/-- Minimum number of additional semantic-semiprime macro types needed in the
penultimate cover problem. -/
noncomputable def rootQuotientPenultimateSemiprimeCoverNumber
    (r N : ℕ) : ℕ :=
  sInf (RootQuotientPenultimateSemiprimeCoverCardinalities r N)

/-- The semiprime-cover feasible cardinality family is nonempty whenever the
prime-only horizon is at least two. -/
theorem rootQuotientPenultimateSemiprimeCoverCardinalities_nonempty
    {r N : ℕ}
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    (RootQuotientPenultimateSemiprimeCoverCardinalities r N).Nonempty := by
  let S := RootQuotientAllSemanticSemiprimes r N
  have hSFinite : S.Finite :=
    rootQuotientNontrivialPowerFreeBasis_finite.subset fun d hd => hd.1
  exact ⟨S.ncard, S, hSFinite,
    allSemanticSemiprimes_is_family,
    allSemanticSemiprimes_cover_maximalBoundaries hHorizon,
    rfl⟩

/-- A minimum semantic-semiprime cover is attained. -/
theorem exists_rootQuotientPenultimateMinimumSemiprimeCover
    {r N : ℕ}
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    ∃ S : Set ℕ,
      S.Finite ∧
      RootQuotientPenultimateSemiprimeFamily r N S ∧
      RootQuotientPenultimateDivisorCover r N S ∧
      S.ncard = rootQuotientPenultimateSemiprimeCoverNumber r N := by
  have hMem :
      rootQuotientPenultimateSemiprimeCoverNumber r N ∈
        RootQuotientPenultimateSemiprimeCoverCardinalities r N := by
    exact Nat.sInf_mem
      (rootQuotientPenultimateSemiprimeCoverCardinalities_nonempty hHorizon)
  exact hMem

/-- The cover number is no larger than any finite semantic-semiprime cover. -/
theorem rootQuotientPenultimateSemiprimeCoverNumber_le
    {r N : ℕ} {S : Set ℕ}
    (hSFinite : S.Finite)
    (hSemi : RootQuotientPenultimateSemiprimeFamily r N S)
    (hCover : RootQuotientPenultimateDivisorCover r N S) :
    rootQuotientPenultimateSemiprimeCoverNumber r N ≤ S.ncard := by
  apply Nat.sInf_le
  exact ⟨S, hSFinite, hSemi, hCover, rfl⟩

/-- Prime and semantic-semiprime families are disjoint because their exact
prime-factor counts are respectively one and two. -/
theorem rootQuotientPrimeBasis_disjoint_semiprimeFamily
    {r N : ℕ} {S : Set ℕ}
    (hSemi : RootQuotientPenultimateSemiprimeFamily r N S) :
    Disjoint (RootQuotientPrimeBasis N) S := by
  refine Set.disjoint_left.2 ?_
  intro g hgPrime hgS
  have hPrimeCount : rootQuotientPrimeFactorCount g = 1 := by
    rw [rootQuotientPrimeFactorCount,
      Nat.primeFactorsList_prime hgPrime.1]
    simp
  have hSemiCount : rootQuotientPrimeFactorCount g = 2 :=
    hSemi.2 g hgS
  omega

/-- Exact penultimate storage law.

At horizon `L_r(N)-1`, minimum primitive-type storage is the forced prime-core
cardinality plus the minimum semantic-semiprime divisor-cover number. -/
theorem rootQuotientMinimumStorageSize_penultimate_eq_prime_add_semiprimeCoverNumber
    {r N : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : 2 ≤ rootQuotientPrimeHorizon r N) :
    rootQuotientMinimumStorageSize
        r N (rootQuotientPrimeHorizon r N - 1) =
      (RootQuotientPrimeBasis N).ncard +
        rootQuotientPenultimateSemiprimeCoverNumber r N := by
  have hPenPos : 1 ≤ rootQuotientPrimeHorizon r N - 1 := by omega
  apply Nat.le_antisymm
  · obtain ⟨S, hSFinite, hSemi, hCover, hSCard⟩ :=
      exists_rootQuotientPenultimateMinimumSemiprimeCover hHorizon
    let G := RootQuotientPrimeBasis N ∪ S
    have hGSemantic :
        G ⊆ RootQuotientNontrivialPowerFreeBasis r N := by
      intro g hg
      rcases hg with hgPrime | hgS
      · exact rootQuotientPrimeBasis_subset_semanticBasis hr hgPrime
      · exact hSemi.1 hgS
    have hGFinite : G.Finite := rootQuotientPrimeBasis_finite.union hSFinite
    have hGPos : PositiveRootQuotientGenerators G := by
      intro g hg
      rcases hg with hgPrime | hgS
      · exact hgPrime.1.one_le
      · have hgTwo : 2 ≤ g := (hSemi.1 hgS).1
        omega
    have hGSep :
        SeparatesRootQuotientWordsUpTo
          r N (rootQuotientPrimeHorizon r N - 1) G :=
      (prime_union_semiprimeFamily_separates_penultimate_iff_divisorCover
        hr hHorizon hSemi).2 hCover
    have hStorage :
        RootQuotientFiniteStorageSeparator
          r N (rootQuotientPrimeHorizon r N - 1) G :=
      ⟨hGSemantic, hGFinite, hGPos, hGSep⟩
    have hMinLe := rootQuotientMinimumStorageSize_le_normalized hStorage
    have hDisjoint := rootQuotientPrimeBasis_disjoint_semiprimeFamily hSemi
    have hGCard :
        G.ncard = (RootQuotientPrimeBasis N).ncard + S.ncard := by
      dsimp [G]
      exact Set.ncard_union_eq hDisjoint rootQuotientPrimeBasis_finite hSFinite
    rw [hGCard, hSCard] at hMinLe
    exact hMinLe
  · obtain ⟨G, hG, hGCard⟩ :=
      exists_rootQuotientMinimumStorageSeparator
        (r := r) (N := N)
        (h := rootQuotientPrimeHorizon r N - 1)
        (by omega) hPenPos
    have hPrimeSubG : RootQuotientPrimeBasis N ⊆ G :=
      rootQuotientPrimeBasis_subset_of_word_separates
        hr hG.2.2.1 hG.2.2.2
    obtain ⟨S, hSFinite, hSemi, hCover, hSLe⟩ :=
      exists_semiprime_cover_le_nonprime_storage_of_penultimate_separator
        hr hHorizon hG.2.1 hG.2.2.1 hG.2.2.2
    have hTauLe :
        rootQuotientPenultimateSemiprimeCoverNumber r N ≤ S.ncard :=
      rootQuotientPenultimateSemiprimeCoverNumber_le hSFinite hSemi hCover
    have hDecomp :
        (G \ RootQuotientPrimeBasis N).ncard +
          (RootQuotientPrimeBasis N).ncard = G.ncard :=
      Set.ncard_sdiff_add_ncard_of_subset hPrimeSubG hG.2.1
    rw [hGCard] at hDecomp
    omega

end EnterpriseMath.Quotient
