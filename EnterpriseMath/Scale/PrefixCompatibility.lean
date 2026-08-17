import EnterpriseMath.Scale.ScaleExtensionHelly
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Pairwise overlap compatibility of a residue-map family on all scales `< N`.
Whenever two old source cells overlap, their images overlap as well. -/
def PrefixCompatible (N : ℕ) (ρ : ScaleMapFamily) : Prop :=
  ∀ A B : PrefixCell N,
    cellOverlap A.scale A.index B.scale B.index →
      cellOverlap A.scale (ρ A.scale A.2).1 B.scale (ρ B.scale B.2).1

/-- Two old cells are bridgeable at scale `h` if one scale-`h` cell overlaps both. -/
def PrefixCellsBridgeableAt {N : ℕ} (A B : PrefixCell N) (h : Fin N) : Prop :=
  ∃ k : Fin h.1,
    cellOverlap A.scale A.index h.1 k.1 ∧
      cellOverlap B.scale B.index h.1 k.1

/-- Their images under the prefix map are bridgeable at scale `h`. -/
def PrefixImageCellsBridgeableAt {N : ℕ} (ρ : ScaleMapFamily)
    (A B : PrefixCell N) (h : Fin N) : Prop :=
  ∃ k : Fin h.1,
    cellOverlap A.scale (ρ A.scale A.2).1 h.1 (ρ h.1 k).1 ∧
      cellOverlap B.scale (ρ B.scale B.2).1 h.1 (ρ h.1 k).1

/-- Prefix compatibility automatically preserves every bridge witnessed by an old
scale. This is the operational contradiction target for Farey bridge descent. -/
theorem PrefixCompatible.preserves_bridge {N : ℕ} {ρ : ScaleMapFamily}
    (hcompat : PrefixCompatible N ρ)
    (A B : PrefixCell N) (h : Fin N)
    (hbridge : PrefixCellsBridgeableAt A B h) :
    PrefixImageCellsBridgeableAt ρ A B h := by
  rcases hbridge with ⟨k, hAk, hBk⟩
  let H : PrefixCell N := ⟨h, k⟩
  have hAH : cellOverlap A.scale A.index H.scale H.index := by
    simpa [H] using hAk
  have hBH : cellOverlap B.scale B.index H.scale H.index := by
    simpa [H] using hBk
  have himgAH := hcompat A H hAH
  have himgBH := hcompat B H hBH
  refine ⟨ρ h.1 k, ?_, ?_⟩
  · simpa [H] using himgAH
  · simpa [H] using himgBH

/-- Bridge preservation in the looser existential form used by the later
cell-gap translation. -/
theorem PrefixCompatible.preserves_bridge_exists {N : ℕ} {ρ : ScaleMapFamily}
    (hcompat : PrefixCompatible N ρ)
    (A B : PrefixCell N) {h : ℕ} (hh : 0 < h) (hhN : h < N)
    (hbridge : ∃ k : Fin h,
      cellOverlap A.scale A.index h k.1 ∧
        cellOverlap B.scale B.index h k.1) :
    ∃ k : Fin h,
      cellOverlap A.scale (ρ A.scale A.2).1 h (ρ h k).1 ∧
        cellOverlap B.scale (ρ B.scale B.2).1 h (ρ h k).1 := by
  let hf : Fin N := ⟨h, hhN⟩
  have hbridge' : PrefixCellsBridgeableAt A B hf := by
    simpa [PrefixCellsBridgeableAt, hf] using hbridge
  have himg := hcompat.preserves_bridge A B hf hbridge'
  simpa [PrefixImageCellsBridgeableAt, hf] using himg

end EnterpriseMath.Scale
