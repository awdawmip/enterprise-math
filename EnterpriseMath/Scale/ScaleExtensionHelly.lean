import EnterpriseMath.Scale.AllowedCellInterval
import EnterpriseMath.Scale.FiniteIntervalHelly
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- All old cells on scales strictly below `N`. A `Fin 0` fiber is empty, so positivity
of the scale is automatic for every inhabitant. -/
abbrev PrefixCell (N : ℕ) := Σ d : Fin N, Fin d.1

@[simp]
def PrefixCell.scale {N : ℕ} (A : PrefixCell N) : ℕ := A.1.1

@[simp]
def PrefixCell.index {N : ℕ} (A : PrefixCell N) : ℕ := A.2.1

theorem PrefixCell.scale_pos {N : ℕ} (A : PrefixCell N) : 0 < A.scale := by
  have := A.2.2
  simp [PrefixCell.scale] at *
  omega

/-- A family of old-scale residue maps. Values at scales `>=N` are irrelevant to a
prefix extension step. -/
abbrev ScaleMapFamily := ∀ d : ℕ, Fin d → Fin d

/-- Source-side incidence between one old prefix cell and one new scale-`N` cell. -/
def prefixSourceOverlap {N : ℕ} (A : PrefixCell N) (j : Fin N) : Prop :=
  cellOverlap A.scale A.index N j.1

/-- Target-side incidence after applying the old scale map to the prefix cell. -/
def prefixTargetOverlap {N : ℕ} (ρ : ScaleMapFamily)
    (A : PrefixCell N) (j : Fin N) : Prop :=
  cellOverlap A.scale (ρ A.scale A.2).1 N j.1

/-- Old prefix cells that overlap a fixed new source cell. -/
def prefixNeighbors {N : ℕ} (j : Fin N) : Finset (PrefixCell N) :=
  Finset.univ.filter fun A => prefixSourceOverlap A j

/-- For every `N>=2`, each new cell has at least one old neighbor: the unique scale-1
cell overlaps every new cell. -/
theorem prefixNeighbors_nonempty {N : ℕ} (hN : 2 ≤ N) (j : Fin N) :
    (prefixNeighbors j).Nonempty := by
  let d1 : Fin N := ⟨1, by omega⟩
  let A : PrefixCell N := ⟨d1, (0 : Fin 1)⟩
  refine ⟨A, ?_⟩
  simp [prefixNeighbors, prefixSourceOverlap, A, d1, cellOverlap]
  omega

/-- Pairwise feasibility condition for extending a prefix to scale `N`: whenever two
old source cells overlap the same new source cell, their old-map images admit at least
one common new target cell. -/
def PairwiseNewAllowed {N : ℕ} (ρ : ScaleMapFamily) : Prop :=
  ∀ (j : Fin N) (A B : PrefixCell N),
    prefixSourceOverlap A j → prefixSourceOverlap B j →
      ∃ k : Fin N, prefixTargetOverlap ρ A k ∧ prefixTargetOverlap ρ B k

/-- Under pairwise feasibility, all old-image constraints for one new source cell have
a common new target cell. -/
theorem exists_common_newTarget_of_pairwiseAllowed
    {N : ℕ} (hN : 2 ≤ N) (ρ : ScaleMapFamily)
    (hpair : PairwiseNewAllowed ρ) (j : Fin N) :
    ∃ k : Fin N,
      ∀ A : PrefixCell N,
        prefixSourceOverlap A j → prefixTargetOverlap ρ A k := by
  let s := prefixNeighbors j
  have hs : s.Nonempty := prefixNeighbors_nonempty hN j
  let lo : PrefixCell N → ℕ := fun A =>
    overlapLower A.scale (ρ A.scale A.2).1 N
  let hi : PrefixCell N → ℕ := fun A =>
    overlapUpper A.scale (ρ A.scale A.2).1 N
  have hNpos : 0 < N := by omega
  have hpairIntervals : ∀ A ∈ s, ∀ B ∈ s,
      ∃ x : ℕ,
        lo A ≤ x ∧ x ≤ hi A ∧ lo B ≤ x ∧ x ≤ hi B := by
    intro A hAs B hBs
    have hA : prefixSourceOverlap A j := by
      simpa [s, prefixNeighbors] using (Finset.mem_filter.mp hAs).2
    have hB : prefixSourceOverlap B j := by
      simpa [s, prefixNeighbors] using (Finset.mem_filter.mp hBs).2
    obtain ⟨k, hkA, hkB⟩ := hpair j A B hA hB
    have hIA := (cellOverlap_iff_allowedInterval A.scale_pos hNpos).1 hkA
    have hIB := (cellOverlap_iff_allowedInterval B.scale_pos hNpos).1 hkB
    exact ⟨k.1, hIA.1, hIA.2, hIB.1, hIB.2⟩
  obtain ⟨x, hx⟩ := finite_natInterval_helly_of_pairwise_witness
    s hs lo hi hpairIntervals
  obtain ⟨A0, hA0s⟩ := hs
  have hxA0 := hx A0 hA0s
  have htargetA0 : (ρ A0.scale A0.2).1 < A0.scale := (ρ A0.scale A0.2).2
  have hhi_lt : hi A0 < N := by
    dsimp [hi]
    exact overlapUpper_lt_scale A0.scale_pos hNpos htargetA0
  have hxN : x < N := lt_of_le_of_lt hxA0.2 hhi_lt
  let k : Fin N := ⟨x, hxN⟩
  refine ⟨k, ?_⟩
  intro A hsource
  have hAs : A ∈ s := by
    simp [s, prefixNeighbors, hsource]
  have hAx := hx A hAs
  exact (cellOverlap_iff_allowedInterval A.scale_pos hNpos).2 hAx

/-- Helly assembly theorem: pairwise feasibility is sufficient to extend all new cells
simultaneously. Each new source cell can be chosen independently. -/
theorem exists_oneStepExtension_of_pairwiseAllowed
    {N : ℕ} (hN : 2 ≤ N) (ρ : ScaleMapFamily)
    (hpair : PairwiseNewAllowed ρ) :
    ∃ fN : Fin N → Fin N,
      ∀ (j : Fin N) (A : PrefixCell N),
        prefixSourceOverlap A j → prefixTargetOverlap ρ A (fN j) := by
  have hchoose : ∀ j : Fin N,
      ∃ k : Fin N,
        ∀ A : PrefixCell N,
          prefixSourceOverlap A j → prefixTargetOverlap ρ A k :=
    fun j => exists_common_newTarget_of_pairwiseAllowed hN ρ hpair j
  choose fN hf using hchoose
  exact ⟨fN, hf⟩

end EnterpriseMath.Scale
