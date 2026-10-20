import EnterpriseMath.Quotient.RootQuotientRelativeRepairStorage
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.Data.Set.Card
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A target-wise exact repair plan relative to base ISA `G`.

Each semantic target chooses one spare word over the allowed candidate set `C`;
a base residual is then compiled in the remaining horizon. -/
structure RootQuotientRelativeRepairPlan
    (G : Set ℕ) (h : ℕ) (T : Finset ℕ) (C : Set ℕ) where
  word : {t : ℕ // t ∈ T} → List ℕ
  length_le : ∀ t, (word t).length ≤ h
  word_over : ∀ t, RootQuotientWordOver C (word t)
  residual : ∀ t, ∃ b : ℕ,
    RootQuotientProductReachableWithin (h - (word t).length) G b ∧
    rootQuotientWordProduct (word t) * b = t.1

/-- Stored dictionary induced by a repair plan: the union of the literal
instruction supports of all selected target-wise witness words. -/
noncomputable def RootQuotientRelativeRepairPlan.dictionary
    {G : Set ℕ} {h : ℕ} {T : Finset ℕ} {C : Set ℕ}
    (P : RootQuotientRelativeRepairPlan G h T C) : Finset ℕ := by
  classical
  exact T.attach.biUnion (fun t => (P.word t).toFinset)

/-- Every selected witness word is a word over the induced union dictionary. -/
theorem relativeRepairPlan_word_over_dictionary
    {G : Set ℕ} {h : ℕ} {T : Finset ℕ} {C : Set ℕ}
    (P : RootQuotientRelativeRepairPlan G h T C)
    (t : {x : ℕ // x ∈ T}) :
    RootQuotientWordOver
      (P.dictionary : Set ℕ) (P.word t) := by
  classical
  intro g hgWord
  have hgFin : g ∈ (P.word t).toFinset := by simpa using hgWord
  have htAttach : t ∈ T.attach := Finset.mem_attach T t
  have hgDict : g ∈ P.dictionary := by
    dsimp [RootQuotientRelativeRepairPlan.dictionary]
    exact Finset.mem_biUnion.2 ⟨t, htAttach, hgFin⟩
  simpa using hgDict

/-- The induced witness-union dictionary stays inside the allowed candidate
set. -/
theorem relativeRepairPlan_dictionary_subset_candidates
    {G : Set ℕ} {h : ℕ} {T : Finset ℕ} {C : Set ℕ}
    (P : RootQuotientRelativeRepairPlan G h T C) :
    (P.dictionary : Set ℕ) ⊆ C := by
  classical
  intro g hgDict
  have hgFin : g ∈ P.dictionary := by simpa using hgDict
  dsimp [RootQuotientRelativeRepairPlan.dictionary] at hgFin
  obtain ⟨t, _htAttach, hgWordFin⟩ := Finset.mem_biUnion.1 hgFin
  have hgWord : g ∈ P.word t := by simpa using hgWordFin
  exact P.word_over t g hgWord

/-- **A repair plan generates a feasible dictionary exactly from the union of
its witness-word supports.** -/
theorem relativeRepairPlan_dictionary_is_presentation
    {G : Set ℕ} {h : ℕ} {T : Finset ℕ} {C : Set ℕ}
    (P : RootQuotientRelativeRepairPlan G h T C) :
    RootQuotientRelativeRepairPresentation
      G h T C (P.dictionary : Set ℕ) := by
  refine ⟨P.dictionary.finite_toSet,
    relativeRepairPlan_dictionary_subset_candidates P, ?_⟩
  intro t ht
  let x : {x : ℕ // x ∈ T} := ⟨t, ht⟩
  obtain ⟨b, hbReach, hFactor⟩ := P.residual x
  apply
    (rootQuotientProductReachableWithin_union_iff_exists_spareWord_residual).2
  exact ⟨P.word x, b,
    P.length_le x,
    relativeRepairPlan_word_over_dictionary P x,
    hbReach,
    hFactor⟩

/-- Every feasible relative repair presentation admits a target-wise witness
plan whose induced union dictionary is a subset of the original stored
presentation.

This is the exact support-compression statement behind the minimum-union view:
unreferenced stored instruction types can be deleted without losing the chosen
repair witnesses. -/
theorem exists_relativeRepairPlan_dictionary_subset_of_presentation
    {G C S : Set ℕ} {h : ℕ} {T : Finset ℕ}
    (hS : RootQuotientRelativeRepairPresentation G h T C S) :
    ∃ P : RootQuotientRelativeRepairPlan G h T C,
      (P.dictionary : Set ℕ) ⊆ S := by
  classical
  have hWords :=
    (relativeRepairPresentation_iff_residualWords).1 hS
  let W : {t : ℕ // t ∈ T} → List ℕ := fun t =>
    Classical.choose (hWords.2.2 t.1 t.2)
  have hWSpec : ∀ t : {x : ℕ // x ∈ T},
      ∃ b : ℕ,
        (W t).length ≤ h ∧
        RootQuotientWordOver S (W t) ∧
        RootQuotientProductReachableWithin (h - (W t).length) G b ∧
        rootQuotientWordProduct (W t) * b = t.1 := by
    intro t
    exact Classical.choose_spec (hWords.2.2 t.1 t.2)
  let P : RootQuotientRelativeRepairPlan G h T C :=
    { word := W
      length_le := by
        intro t
        obtain ⟨b, hLen, _hOver, _hReach, _hFactor⟩ := hWSpec t
        exact hLen
      word_over := by
        intro t g hgWord
        obtain ⟨b, _hLen, hOver, _hReach, _hFactor⟩ := hWSpec t
        exact hS.2.1 (hOver g hgWord)
      residual := by
        intro t
        obtain ⟨b, _hLen, _hOver, hReach, hFactor⟩ := hWSpec t
        exact ⟨b, hReach, hFactor⟩ }
  refine ⟨P, ?_⟩
  intro g hgDict
  have hgFin : g ∈ P.dictionary := by simpa using hgDict
  dsimp [RootQuotientRelativeRepairPlan.dictionary] at hgFin
  obtain ⟨t, _htAttach, hgWordFin⟩ := Finset.mem_biUnion.1 hgFin
  have hgWord : g ∈ W t := by simpa using hgWordFin
  obtain ⟨b, _hLen, hOver, _hReach, _hFactor⟩ := hWSpec t
  exact hOver g hgWord

/-- Cardinality form of witness-union compression. -/
theorem exists_relativeRepairPlan_dictionary_ncard_le_of_presentation
    {G C S : Set ℕ} {h : ℕ} {T : Finset ℕ}
    (hS : RootQuotientRelativeRepairPresentation G h T C S) :
    ∃ P : RootQuotientRelativeRepairPlan G h T C,
      (P.dictionary : Set ℕ).ncard ≤ S.ncard := by
  obtain ⟨P, hSub⟩ :=
    exists_relativeRepairPlan_dictionary_subset_of_presentation hS
  exact ⟨P, Set.ncard_le_ncard hSub hS.1⟩

end EnterpriseMath.Quotient
