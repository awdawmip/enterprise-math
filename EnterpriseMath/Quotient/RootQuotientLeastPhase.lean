import EnterpriseMath.Quotient.RootQuotientPrimeBasis
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- The nontrivial part of the canonical one-step semantic action basis.
Denominator one is supplied by the empty word/current observation. -/
def RootQuotientNontrivialPowerFreeBasis (r N : ℕ) : Set ℕ :=
  {b : ℕ | 2 ≤ b ∧ b ≤ N ∧ RPowerFree r b}

/-- Omitting one named denominator from the complete nontrivial power-free
primitive alphabet. -/
def RootQuotientCompositeOmissionBasis (r N g : ℕ) : Set ℕ :=
  {b : ℕ | b ∈ RootQuotientNontrivialPowerFreeBasis r N ∧ b ≠ g}

/-- Power-freeness is inherited by positive divisors. -/
theorem rPowerFree_of_dvd_of_rPowerFree
    {r a b : ℕ}
    (hab : a ∣ b)
    (hbFree : RPowerFree r b) :
    RPowerFree r a := by
  intro t ht hta
  exact hbFree t ht (dvd_trans hta hab)

/-- The complete nontrivial power-free alphabet consists of positive
primitive quotient denominators. -/
theorem rootQuotientNontrivialPowerFreeBasis_positive
    {r N : ℕ} :
    PositiveRootQuotientGenerators
      (RootQuotientNontrivialPowerFreeBasis r N) := by
  intro b hb
  rcases hb with ⟨hbTwo, _hbN, _hbFree⟩
  omega

/-- Removing one element preserves positivity of the primitive alphabet. -/
theorem rootQuotientCompositeOmissionBasis_positive
    {r N g : ℕ} :
    PositiveRootQuotientGenerators
      (RootQuotientCompositeOmissionBasis r N g) := by
  intro b hb
  rcases hb with ⟨⟨hbTwo, _hbN, _hbFree⟩, _hbNe⟩
  omega

/-- Separation is monotone in the available quotient-word horizon. -/
theorem separatesRootQuotientWordsUpTo_mono_horizon
    {r N h₁ h₂ : ℕ} {G : Set ℕ}
    (hh : h₁ ≤ h₂)
    (hSep : SeparatesRootQuotientWordsUpTo r N h₁ G) :
    SeparatesRootQuotientWordsUpTo r N h₂ G := by
  intro x y hxy hyN
  obtain ⟨w, hwLen, hwG, hDist⟩ := hSep hxy hyN
  exact ⟨w, hwLen.trans hh, hwG, hDist⟩

/-- The complete nontrivial power-free primitive alphabet realizes the
canonical semantic basis in one quotient instruction. -/
theorem rootQuotientNontrivialPowerFreeBasis_separates_at_one
    {r N : ℕ}
    (hr : 1 ≤ r) :
    SeparatesRootQuotientWordsUpTo
      r N 1 (RootQuotientNontrivialPowerFreeBasis r N) := by
  apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
    (r := r) (N := N) (h := 1)
    (G := RootQuotientNontrivialPowerFreeBasis r N)
    hr rootQuotientNontrivialPowerFreeBasis_positive).2
  intro b hbPos hbN hbFree
  by_cases hbOne : b = 1
  · subst b
    exact ⟨[], by simp, by simp [RootQuotientWordOver],
      by simp [rootQuotientWordProduct]⟩
  · have hbTwo : 2 ≤ b := by omega
    refine ⟨[b], by simp, ?_, by simp [rootQuotientWordProduct]⟩
    intro a ha
    simp at ha
    subst a
    exact ⟨hbTwo, hbN, hbFree⟩

/-- Every nontrivial bounded power-free denominator is forced in a separating
horizon-one primitive alphabet. -/
theorem rootQuotientNontrivialPowerFreeBasis_subset_of_one_step_separates
    {r N : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hG : PositiveRootQuotientGenerators G)
    (hSep : SeparatesRootQuotientWordsUpTo r N 1 G) :
    RootQuotientNontrivialPowerFreeBasis r N ⊆ G := by
  intro b hb
  rcases hb with ⟨hbTwo, hbN, hbFree⟩
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := 1) (G := G) hr hG).1 hSep
      b (by omega) hbN hbFree
  obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
  cases w with
  | nil =>
      simp [rootQuotientWordProduct] at hProd
      omega
  | cons a w =>
      have hwNil : w = [] := by
        cases w with
        | nil => rfl
        | cons c w' =>
            simp at hwLen
      subst w
      have haG : a ∈ G := hwG a (by simp)
      simp [rootQuotientWordProduct] at hProd
      rw [hProd]
      exact haG

/-- Deleting any bounded composite denominator still leaves a horizon-two
separating alphabet.

If the deleted composite is not a required power-free boundary, nothing is
lost.  If it is required, two proper factors remain power-free by divisor
closure and their two-letter word recompiles the deleted denominator. -/
theorem rootQuotientCompositeOmissionBasis_separates_at_two
    {r N g : ℕ}
    (hr : 1 ≤ r)
    (hgTwo : 2 ≤ g)
    (hgN : g ≤ N)
    (hgNotPrime : ¬g.Prime) :
    SeparatesRootQuotientWordsUpTo
      r N 2 (RootQuotientCompositeOmissionBasis r N g) := by
  apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
    (r := r) (N := N) (h := 2)
    (G := RootQuotientCompositeOmissionBasis r N g)
    hr rootQuotientCompositeOmissionBasis_positive).2
  intro b hbPos hbN hbFree
  by_cases hbOne : b = 1
  · subst b
    exact ⟨[], by simp, by simp [RootQuotientWordOver],
      by simp [rootQuotientWordProduct]⟩
  · have hbTwo : 2 ≤ b := by omega
    by_cases hbg : b = g
    · subst b
      obtain ⟨a, c, haLt, hcLt, hac⟩ :=
        (Nat.not_prime_iff_exists_mul_eq hgTwo).1 hgNotPrime
      have haZero : a ≠ 0 := by
        intro ha
        subst a
        simp at hac
        omega
      have hcZero : c ≠ 0 := by
        intro hc
        subst c
        simp at hac
        omega
      have haOne : a ≠ 1 := by
        intro ha
        subst a
        simp at hac
        omega
      have hcOne : c ≠ 1 := by
        intro hc
        subst c
        simp at hac
        omega
      have haTwo : 2 ≤ a := by omega
      have hcTwo : 2 ≤ c := by omega
      have haDvd : a ∣ g := ⟨c, hac.symm⟩
      have hcDvd : c ∣ g := by
        refine ⟨a, ?_⟩
        simpa [Nat.mul_comm] using hac.symm
      have haFree : RPowerFree r a :=
        rPowerFree_of_dvd_of_rPowerFree haDvd hbFree
      have hcFree : RPowerFree r c :=
        rPowerFree_of_dvd_of_rPowerFree hcDvd hbFree
      have haN : a ≤ N := (Nat.le_of_lt haLt).trans hgN
      have hcN : c ≤ N := (Nat.le_of_lt hcLt).trans hgN
      have haMem :
          a ∈ RootQuotientCompositeOmissionBasis r N g :=
        ⟨⟨haTwo, haN, haFree⟩, ne_of_lt haLt⟩
      have hcMem :
          c ∈ RootQuotientCompositeOmissionBasis r N g :=
        ⟨⟨hcTwo, hcN, hcFree⟩, ne_of_lt hcLt⟩
      refine ⟨[a, c], by simp, ?_, ?_⟩
      · intro x hx
        simp at hx
        rcases hx with rfl | rfl
        · exact haMem
        · exact hcMem
      · simpa [rootQuotientWordProduct] using hac.symm
    · have hbMem :
          b ∈ RootQuotientCompositeOmissionBasis r N g :=
        ⟨⟨hbTwo, hbN, hbFree⟩, hbg⟩
      refine ⟨[b], by simp, ?_, by simp [rootQuotientWordProduct]⟩
      intro a ha
      simp at ha
      subst a
      exact hbMem

/-- The composite-omission witness remains separating at every horizon at
least two. -/
theorem rootQuotientCompositeOmissionBasis_separates
    {r N g h : ℕ}
    (hr : 1 ≤ r)
    (hgTwo : 2 ≤ g)
    (hgN : g ≤ N)
    (hgNotPrime : ¬g.Prime)
    (hh : 2 ≤ h) :
    SeparatesRootQuotientWordsUpTo
      r N h (RootQuotientCompositeOmissionBasis r N g) := by
  exact separatesRootQuotientWordsUpTo_mono_horizon hh
    (rootQuotientCompositeOmissionBasis_separates_at_two
      hr hgTwo hgN hgNotPrime)

/-- Inclusion-least separating primitive alphabet at one fixed word horizon. -/
def IsLeastSeparatingRootQuotientAlphabet
    (r N h : ℕ) (G : Set ℕ) : Prop :=
  PositiveRootQuotientGenerators G ∧
  SeparatesRootQuotientWordsUpTo r N h G ∧
  ∀ {H : Set ℕ},
    PositiveRootQuotientGenerators H →
    SeparatesRootQuotientWordsUpTo r N h H →
    G ⊆ H

/-- Horizon one has the canonical nontrivial power-free basis as its
inclusion-least primitive alphabet. -/
theorem rootQuotientNontrivialPowerFreeBasis_isLeast_at_one
    {r N : ℕ}
    (hr : 1 ≤ r) :
    IsLeastSeparatingRootQuotientAlphabet
      r N 1 (RootQuotientNontrivialPowerFreeBasis r N) := by
  refine ⟨rootQuotientNontrivialPowerFreeBasis_positive,
    rootQuotientNontrivialPowerFreeBasis_separates_at_one hr, ?_⟩
  intro H hHPos hHSep
  exact rootQuotientNontrivialPowerFreeBasis_subset_of_one_step_separates
    hr hHPos hHSep

/-- Once the available horizon reaches the exact prime-only horizon, the
bounded prime alphabet is inclusion-least. -/
theorem rootQuotientPrimeBasis_isLeast_of_horizon_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hHorizon : rootQuotientPrimeHorizon r N ≤ h) :
    IsLeastSeparatingRootQuotientAlphabet
      r N h (RootQuotientPrimeBasis N) := by
  refine ⟨rootQuotientPrimeBasis_positive,
    (rootQuotientPrimeBasis_separates_iff_horizon_le
      (r := r) (N := N) (h := h) (by omega)).2 hHorizon, ?_⟩
  intro H hHPos hHSep
  exact rootQuotientPrimeBasis_subset_of_word_separates
    hr hHPos hHSep

/-- In the intermediate fixed-horizon regime, no inclusion-least separating
primitive alphabet exists. -/
theorem no_least_separating_rootQuotientAlphabet_of_intermediate_horizon
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h)
    (hBelow : h < rootQuotientPrimeHorizon r N) :
    ¬∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet r N h G := by
  rintro ⟨G, hLeast⟩
  rcases hLeast with ⟨hGPos, hGSep, hMinimal⟩
  have hPrimeSub : RootQuotientPrimeBasis N ⊆ G :=
    rootQuotientPrimeBasis_subset_of_word_separates hr hGPos hGSep
  have hBaseSep :
      SeparatesRootQuotientWordsUpTo
        r N h (RootQuotientNontrivialPowerFreeBasis r N) :=
    separatesRootQuotientWordsUpTo_mono_horizon (by omega)
      (rootQuotientNontrivialPowerFreeBasis_separates_at_one (by omega))
  have hGSubBase :
      G ⊆ RootQuotientNontrivialPowerFreeBasis r N :=
    hMinimal rootQuotientNontrivialPowerFreeBasis_positive hBaseSep
  have hGSubPrime : G ⊆ RootQuotientPrimeBasis N := by
    intro g hgG
    have hgBase := hGSubBase hgG
    have hgPrime : g.Prime := by
      by_contra hgNotPrime
      have hOmitSep :
          SeparatesRootQuotientWordsUpTo
            r N h (RootQuotientCompositeOmissionBasis r N g) :=
        rootQuotientCompositeOmissionBasis_separates
          (by omega) hgBase.1 hgBase.2.1 hgNotPrime hh
      have hGSubOmit :
          G ⊆ RootQuotientCompositeOmissionBasis r N g :=
        hMinimal rootQuotientCompositeOmissionBasis_positive hOmitSep
      have hgOmit := hGSubOmit hgG
      exact hgOmit.2 rfl
    exact ⟨hgPrime, hgBase.2.1⟩
  have hEq : G = RootQuotientPrimeBasis N :=
    Set.Subset.antisymm hGSubPrime hPrimeSub
  rw [hEq] at hGSep
  have hNecessary : rootQuotientPrimeHorizon r N ≤ h :=
    rootQuotientPrimeHorizon_minimal_of_separates (by omega) hGSep
  omega

/-- Complete existence phase for inclusion-least primitive alphabets once two
or more composition slots are available. -/
theorem exists_least_separating_rootQuotientAlphabet_iff_horizon_le
    {r N h : ℕ}
    (hr : 2 ≤ r)
    (hh : 2 ≤ h) :
    (∃ G : Set ℕ,
      IsLeastSeparatingRootQuotientAlphabet r N h G) ↔
      rootQuotientPrimeHorizon r N ≤ h := by
  constructor
  · intro hExists
    by_contra hNot
    have hBelow : h < rootQuotientPrimeHorizon r N := by omega
    exact
      no_least_separating_rootQuotientAlphabet_of_intermediate_horizon
        hr hh hBelow hExists
  · intro hHorizon
    exact ⟨RootQuotientPrimeBasis N,
      rootQuotientPrimeBasis_isLeast_of_horizon_le hr hHorizon⟩

end EnterpriseMath.Quotient
