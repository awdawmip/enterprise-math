import EnterpriseMath.Scale.OverlapCells
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Fine-side cell containing the internal boundary `(i+1)/d`. -/
def boundaryBridgeCell (d e i : ℕ) : ℕ :=
  ((i + 1) * e) / d

/-- For coprime positive scales, every internal `d`-boundary lies strictly inside a
unique `e`-cell. That cell overlaps both adjacent `d`-cells.

This gives the explicit bridge chain connecting all `d`-cells in the coprime overlap
component. -/
theorem boundaryBridgeCell_certificate {d e i : ℕ}
    (hcop : d.Coprime e) (hd : 0 < d) (he : 0 < e) (hi : i + 1 < d) :
    let j := boundaryBridgeCell d e i
    j < e ∧ cellOverlap d i e j ∧ cellOverlap d (i + 1) e j := by
  let n := (i + 1) * e
  let j := n / d
  have hnotdvd : ¬ d ∣ n := by
    intro hdvd
    have hdvd_i : d ∣ i + 1 := by
      apply hcop.dvd_of_dvd_mul_right
      simpa [n] using hdvd
    have hle : d ≤ i + 1 := Nat.le_of_dvd (by omega) hdvd_i
    omega
  have hjd_le : j * d ≤ n := by
    simpa [j] using Nat.div_mul_le_self n d
  have hjd_ne : j * d ≠ n := by
    intro hEq
    apply hnotdvd
    refine ⟨j, ?_⟩
    simpa [Nat.mul_comm] using hEq.symm
  have hjd_lt : j * d < n := by omega
  have hn_lt_next : n < (j + 1) * d := by
    have h := Nat.lt_div_mul_add n hd
    simpa [j, Nat.add_mul] using h
  have hn_lt_de : n < d * e := by
    dsimp [n]
    have hmul := (Nat.mul_lt_mul_right he).2 hi
    simpa [Nat.mul_comm, Nat.mul_left_comm, Nat.mul_assoc] using hmul
  have hj_lt_e : j < e := by
    exact (Nat.div_lt_iff_lt_mul hd).2 (by
      simpa [Nat.mul_comm] using hn_lt_de)
  have hi_left : i * e < n := by
    dsimp [n]
    exact (Nat.mul_lt_mul_right he).2 (Nat.lt_succ_self i)
  have hi_right : n < (i + 2) * e := by
    dsimp [n]
    exact (Nat.mul_lt_mul_right he).2 (by omega)
  change
    let j := boundaryBridgeCell d e i
    j < e ∧ cellOverlap d i e j ∧ cellOverlap d (i + 1) e j
  dsimp [boundaryBridgeCell]
  change j < e ∧ cellOverlap d i e j ∧ cellOverlap d (i + 1) e j
  refine ⟨hj_lt_e, ?_, ?_⟩
  · exact ⟨lt_trans hi_left hn_lt_next, hjd_lt⟩
  · exact ⟨hn_lt_next, lt_trans hjd_lt hi_right⟩

/-- Coarse-side cell meeting a chosen `e`-cell, obtained from the left endpoint. -/
def attachmentCell (d e j : ℕ) : ℕ :=
  (j * d) / e

/-- Every valid `e`-cell overlaps at least one valid `d`-cell. No coprimality is needed.

Together with `boundaryBridgeCell_certificate`, this shows that for coprime positive
scales the entire bipartite overlap graph is connected. -/
theorem attachmentCell_certificate {d e j : ℕ}
    (hd : 0 < d) (he : 0 < e) (hj : j < e) :
    let i := attachmentCell d e j
    i < d ∧ cellOverlap d i e j := by
  let n := j * d
  let i := n / e
  have hie_le : i * e ≤ n := by
    simpa [i] using Nat.div_mul_le_self n e
  have hn_lt_next : n < (i + 1) * e := by
    have h := Nat.lt_div_mul_add n he
    simpa [i, Nat.add_mul] using h
  have hn_lt_ed : n < e * d := by
    dsimp [n]
    exact (Nat.mul_lt_mul_right hd).2 hj
  have hi_lt_d : i < d := by
    exact (Nat.div_lt_iff_lt_mul he).2 hn_lt_ed
  have hn_lt_jnext : n < (j + 1) * d := by
    dsimp [n]
    exact (Nat.mul_lt_mul_right hd).2 (Nat.lt_succ_self j)
  change
    let i := attachmentCell d e j
    i < d ∧ cellOverlap d i e j
  dsimp [attachmentCell]
  change i < d ∧ cellOverlap d i e j
  refine ⟨hi_lt_d, ?_⟩
  constructor
  · exact lt_of_le_of_lt hie_le hn_lt_jnext
  · exact hn_lt_next

/-- Explicit finite bridge certificate for coprime overlap connectivity:
all consecutive `d`-cells have a common `e`-neighbor, and every `e`-cell has a
`d`-neighbor. -/
theorem coprime_overlap_connectivity_certificate {d e : ℕ}
    (hcop : d.Coprime e) (hd : 0 < d) (he : 0 < e) :
    (∀ i, i + 1 < d →
      ∃ j, j < e ∧ cellOverlap d i e j ∧ cellOverlap d (i + 1) e j) ∧
    (∀ j, j < e → ∃ i, i < d ∧ cellOverlap d i e j) := by
  constructor
  · intro i hi
    refine ⟨boundaryBridgeCell d e i, ?_⟩
    simpa using boundaryBridgeCell_certificate hcop hd he hi
  · intro j hj
    refine ⟨attachmentCell d e j, ?_⟩
    simpa using attachmentCell_certificate hd he hj

end EnterpriseMath.Scale
