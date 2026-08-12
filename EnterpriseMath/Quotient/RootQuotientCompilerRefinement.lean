import EnterpriseMath.Quotient.RootQuotientPrimeBasis
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Compiled quotient-word products respect list concatenation. -/
theorem rootQuotientWordProduct_append
    (u v : List ℕ) :
    rootQuotientWordProduct (u ++ v) =
      rootQuotientWordProduct u * rootQuotientWordProduct v := by
  induction u with
  | nil => simp [rootQuotientWordProduct]
  | cons a u ih =>
      simp [rootQuotientWordProduct, ih, Nat.mul_assoc]

/-- Concatenating two words over the same primitive alphabet remains a word
over that alphabet. -/
theorem rootQuotientWordOver_append
    {G : Set ℕ} {u v : List ℕ}
    (hu : RootQuotientWordOver G u)
    (hv : RootQuotientWordOver G v) :
    RootQuotientWordOver G (u ++ v) := by
  intro g hg
  rw [List.mem_append] at hg
  rcases hg with hgU | hgV
  · exact hu g hgU
  · exact hv g hgV

/-- Reachable denominator products multiply with additive execution depth. -/
theorem rootQuotientProductReachableWithin_mul
    {G : Set ℕ} {h j a b : ℕ}
    (ha : RootQuotientProductReachableWithin h G a)
    (hb : RootQuotientProductReachableWithin j G b) :
    RootQuotientProductReachableWithin (h + j) G (a * b) := by
  obtain ⟨u, huLen, huG, haProd⟩ := ha
  obtain ⟨v, hvLen, hvG, hbProd⟩ := hb
  refine ⟨u ++ v, ?_, rootQuotientWordOver_append huG hvG, ?_⟩
  · rw [List.length_append]
    omega
  · calc
      a * b = rootQuotientWordProduct u * rootQuotientWordProduct v := by
        rw [← haProd, ← hbProd]
      _ = rootQuotientWordProduct (u ++ v) :=
        (rootQuotientWordProduct_append u v).symm

/-- `H` compiles the primitive alphabet `G` within depth `j` when every
instruction of `G` has an `H`-word implementation of length at most `j`.

The first alphabet is the lower-level implementation ISA; the second is the
higher-level ISA being compiled. -/
def RootQuotientAlphabetCompilesWithin
    (j : ℕ) (H G : Set ℕ) : Prop :=
  ∀ g : ℕ, g ∈ G → RootQuotientProductReachableWithin j H g

/-- Set inclusion is depth-one compilation: every higher-level instruction can
be emitted literally as a one-letter lower-level word. -/
theorem rootQuotientAlphabetCompilesWithin_of_subset
    {H G : Set ℕ}
    (hGH : G ⊆ H) :
    RootQuotientAlphabetCompilesWithin 1 H G := by
  intro g hg
  refine ⟨[g], by simp, ?_, ?_⟩
  · intro a ha
    simp at ha
    subst a
    exact hGH hg
  · simp [rootQuotientWordProduct]

/-- Recompile a literal `G` word through a bounded-depth implementation of the
whole alphabet `G` in `H`.  Word length expands by at most the multiplicative
factor `j`. -/
theorem exists_recompiled_rootQuotientWord
    {H G : Set ℕ} {j : ℕ} {w : List ℕ}
    (hCompile : RootQuotientAlphabetCompilesWithin j H G)
    (hwG : RootQuotientWordOver G w) :
    ∃ v : List ℕ,
      v.length ≤ w.length * j ∧
      RootQuotientWordOver H v ∧
      rootQuotientWordProduct w = rootQuotientWordProduct v := by
  induction w with
  | nil =>
      exact ⟨[], by simp, by simp [RootQuotientWordOver], rfl⟩
  | cons a w ih =>
      have haG : a ∈ G := hwG a (by simp)
      have hwTail : RootQuotientWordOver G w := by
        intro g hg
        exact hwG g (by simp [hg])
      obtain ⟨u, huLen, huH, haProd⟩ := hCompile a haG
      obtain ⟨v, hvLen, hvH, hTailProd⟩ := ih hwTail
      refine ⟨u ++ v, ?_, rootQuotientWordOver_append huH hvH, ?_⟩
      · rw [List.length_append, List.length_cons, Nat.add_mul]
        simp only [Nat.one_mul]
        omega
      · rw [rootQuotientWordProduct, rootQuotientWordProduct_append]
        rw [haProd, hTailProd]

/-- Any reachable higher-level product can be recompiled through a bounded
implementation of the higher-level alphabet.  Execution depths multiply. -/
theorem rootQuotientProductReachableWithin_recompile
    {H G : Set ℕ} {h j d : ℕ}
    (hCompile : RootQuotientAlphabetCompilesWithin j H G)
    (hReach : RootQuotientProductReachableWithin h G d) :
    RootQuotientProductReachableWithin (h * j) H d := by
  obtain ⟨w, hwLen, hwG, hdProd⟩ := hReach
  obtain ⟨v, hvLen, hvH, hProdEq⟩ :=
    exists_recompiled_rootQuotientWord hCompile hwG
  refine ⟨v, ?_, hvH, ?_⟩
  · exact hvLen.trans (Nat.mul_le_mul_right j hwLen)
  · calc
      d = rootQuotientWordProduct w := hdProd
      _ = rootQuotientWordProduct v := hProdEq

/-- Bounded compiler refinement is transitive, with multiplicative depth. -/
theorem rootQuotientAlphabetCompilesWithin_trans
    {K H G : Set ℕ} {j k : ℕ}
    (hHG : RootQuotientAlphabetCompilesWithin j H G)
    (hKH : RootQuotientAlphabetCompilesWithin k K H) :
    RootQuotientAlphabetCompilesWithin (j * k) K G := by
  intro g hg
  exact rootQuotientProductReachableWithin_recompile hKH (hHG g hg)

/-- Exact compiler interpretation of bounded quotient-root separation.

For positive generators, a primitive alphabet separates the bounded exact
state domain within `h` steps iff it compiles every nontrivial canonical
power-free semantic instruction within `h` steps. -/
theorem separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis
    {r N h : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hGPos : PositiveRootQuotientGenerators G) :
    SeparatesRootQuotientWordsUpTo r N h G ↔
      RootQuotientAlphabetCompilesWithin
        h G (RootQuotientNontrivialPowerFreeBasis r N) := by
  constructor
  · intro hSep b hbSemantic
    exact
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h) (G := G) hr hGPos).1 hSep
        b (by omega) hbSemantic.2.1 hbSemantic.2.2
  · intro hCompile
    apply (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h) (G := G) hr hGPos).2
    intro b hbPos hbN hbFree
    by_cases hbOne : b = 1
    · subst b
      exact ⟨[], by simp, by simp [RootQuotientWordOver], by simp [rootQuotientWordProduct]⟩
    · have hbTwo : 2 ≤ b := by omega
      exact hCompile b ⟨hbTwo, hbN, hbFree⟩

/-- Correct presentations compose exactly like compilers: if `H` implements
`G` within `j` steps and `G` separates within `h`, then `H` separates within
`h*j` steps. -/
theorem separatesRootQuotientWordsUpTo_recompile
    {r N h j : ℕ} {H G : Set ℕ}
    (hr : 1 ≤ r)
    (hGPos : PositiveRootQuotientGenerators G)
    (hHPos : PositiveRootQuotientGenerators H)
    (hCompile : RootQuotientAlphabetCompilesWithin j H G)
    (hSep : SeparatesRootQuotientWordsUpTo r N h G) :
    SeparatesRootQuotientWordsUpTo r N (h * j) H := by
  have hGSemantic :=
    (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis hr hGPos).1 hSep
  have hHSemantic :=
    rootQuotientAlphabetCompilesWithin_trans hGSemantic hCompile
  exact
    (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis hr hHPos).2
      hHSemantic

/-- The exact prime-only horizon is precisely the compiler depth needed for the
bounded prime ISA to implement the canonical semantic ISA. -/
theorem rootQuotientPrimeBasis_compiles_semanticBasis_iff_horizon_le
    {r N h : ℕ}
    (hr : 1 ≤ r) :
    RootQuotientAlphabetCompilesWithin
        h (RootQuotientPrimeBasis N)
        (RootQuotientNontrivialPowerFreeBasis r N) ↔
      rootQuotientPrimeHorizon r N ≤ h := by
  exact
    (separatesRootQuotientWordsUpTo_iff_compiles_semanticBasis
      (r := r) (N := N) (h := h)
      (G := RootQuotientPrimeBasis N)
      hr rootQuotientPrimeBasis_positive).symm.trans
      (rootQuotientPrimeBasis_separates_iff_horizon_le hr)

/-- The prime ISA implements the semantic ISA at its exact compiler depth. -/
theorem rootQuotientPrimeBasis_compiles_semanticBasis_at_exact_horizon
    {r N : ℕ}
    (hr : 1 ≤ r) :
    RootQuotientAlphabetCompilesWithin
      (rootQuotientPrimeHorizon r N)
      (RootQuotientPrimeBasis N)
      (RootQuotientNontrivialPowerFreeBasis r N) := by
  exact
    (rootQuotientPrimeBasis_compiles_semanticBasis_iff_horizon_le
      (r := r) (N := N)
      (h := rootQuotientPrimeHorizon r N) hr).2 le_rfl

/-- Any prime-to-semantic compilation depth is at least the exact horizon. -/
theorem rootQuotientPrimeHorizon_minimal_compiler_depth
    {r N h : ℕ}
    (hr : 1 ≤ r)
    (hCompile : RootQuotientAlphabetCompilesWithin
      h (RootQuotientPrimeBasis N)
      (RootQuotientNontrivialPowerFreeBasis r N)) :
    rootQuotientPrimeHorizon r N ≤ h := by
  exact
    (rootQuotientPrimeBasis_compiles_semanticBasis_iff_horizon_le hr).1
      hCompile

end EnterpriseMath.Quotient
