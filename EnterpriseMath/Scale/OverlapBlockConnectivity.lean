import EnterpriseMath.Scale.OverlapComponents
import EnterpriseMath.Scale.OverlapDivisibility
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- An internal scale-`d` boundary that is not also an `e`-boundary lies strictly
inside one `e`-cell, which therefore overlaps both adjacent `d`-cells. -/
theorem boundaryBridgeCell_certificate_of_not_dvd {d e i : ℕ}
    (hd : 0 < d) (he : 0 < e) (hi : i + 1 < d)
    (hnotdvd : ¬ d ∣ (i + 1) * e) :
    let j := boundaryBridgeCell d e i
    j < e ∧ cellOverlap d i e j ∧ cellOverlap d (i + 1) e j := by
  let n := (i + 1) * e
  let j := n / d
  have hjd_le : j * d ≤ n := by
    simpa [j] using Nat.div_mul_le_self n d
  have hjd_ne : j * d ≠ n := by
    intro hEq
    apply hnotdvd
    refine ⟨j, ?_⟩
    simpa [n, Nat.mul_comm] using hEq.symm
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

/-- Consecutive left cells whose separating boundary lies strictly inside one reduced
gcd block are reachable by a two-edge overlap path. -/
theorem overlapGraph_left_succ_reachable_inside_block {d e k i : ℕ}
    (hd : 0 < d) (he : 0 < e) (hi : i + 1 < d)
    (hlo : k * (d / d.gcd e) < i + 1)
    (hhi : i + 1 < (k + 1) * (d / d.gcd e)) :
    (overlapGraph d e).Reachable
      (Sum.inl (⟨i, by omega⟩ : Fin d))
      (Sum.inl (⟨i + 1, hi⟩ : Fin d)) := by
  have hnotdvd : ¬ d ∣ (i + 1) * e :=
    not_scale_dvd_mul_of_between_reduced_multiples hd hlo hhi
  obtain ⟨hj, hov₁, hov₂⟩ :=
    boundaryBridgeCell_certificate_of_not_dvd hd he hi hnotdvd
  let j : Fin e := ⟨boundaryBridgeCell d e i, hj⟩
  have hAdj₁ : (overlapGraph d e).Adj
      (Sum.inl (⟨i, by omega⟩ : Fin d)) (Sum.inr j) :=
    (overlapGraph_adj_left_right _ _).2 hov₁
  have hAdj₂ : (overlapGraph d e).Adj
      (Sum.inl (⟨i + 1, hi⟩ : Fin d)) (Sum.inr j) :=
    (overlapGraph_adj_left_right _ _).2 hov₂
  exact hAdj₁.reachable.trans hAdj₂.symm.reachable

/-- Start index of the gcd block containing a left-side cell. -/
def leftBlockStart (d e i : ℕ) : ℕ :=
  gcdBlockD d e i * (d / d.gcd e)

/-- Every valid left-side cell is reachable from the first left cell of its gcd block. -/
theorem overlapGraph_left_reachable_from_blockStart {d e : ℕ}
    (hd : 0 < d) (he : 0 < e) (i : Fin d) :
    let s := leftBlockStart d e i.1
    ∃ hs : s < d,
      (overlapGraph d e).Reachable
        (Sum.inl (⟨s, hs⟩ : Fin d)) (Sum.inl i) := by
  let g := d.gcd e
  let w := d / g
  let k := i.1 / w
  let a := i.1 % w
  let s := k * w
  have hw : 0 < w := by
    dsimp [w, g]
    exact Nat.div_gcd_pos_of_pos_left e hd
  have hg : 0 < g := by
    dsimp [g]
    exact Nat.gcd_pos_of_pos_left e hd
  have hd_decomp : d = w * g := by
    dsimp [w, g]
    exact (Nat.div_mul_cancel (Nat.gcd_dvd_left d e)).symm
  have hk_lt : k < g := by
    apply (Nat.div_lt_iff_lt_mul hw).2
    rw [← hd_decomp]
    exact i.2
  have hs_lt : s < d := by
    dsimp [s]
    rw [hd_decomp]
    exact (Nat.mul_lt_mul_left hw).2 hk_lt
  have ha_lt : a < w := by
    dsimp [a]
    exact Nat.mod_lt _ hw
  have hdecomp : s + a = i.1 := by
    dsimp [s, a, k]
    have h := Nat.mod_add_div i.1 w
    omega
  have hreach : ∀ t : ℕ, t ≤ a →
      (overlapGraph d e).Reachable
        (Sum.inl (⟨s, hs_lt⟩ : Fin d))
        (Sum.inl (⟨s + t, by omega⟩ : Fin d)) := by
    intro t
    induction t with
    | zero =>
        intro _
        exact SimpleGraph.Reachable.refl
    | succ t ih =>
        intro ht
        have ht_le : t ≤ a := by omega
        have hprev := ih ht_le
        have ht1_lt_w : t + 1 < w := lt_of_le_of_lt ht ha_lt
        have hq_lt_d : s + t + 1 < d := by omega
        have hlo : k * w < s + t + 1 := by
          dsimp [s]
          omega
        have hhi : s + t + 1 < (k + 1) * w := by
          dsimp [s]
          have : t + 1 < w := ht1_lt_w
          omega
        have hstep := overlapGraph_left_succ_reachable_inside_block
          (d := d) (e := e) (k := k) (i := s + t)
          hd he (by omega) (by simpa [w, g] using hlo) (by simpa [w, g] using hhi)
        exact hprev.trans hstep
  change
    let s := leftBlockStart d e i.1
    ∃ hs : s < d,
      (overlapGraph d e).Reachable
        (Sum.inl (⟨s, hs⟩ : Fin d)) (Sum.inl i)
  dsimp [leftBlockStart, gcdBlockD]
  change ∃ hs : s < d,
    (overlapGraph d e).Reachable
      (Sum.inl (⟨s, hs⟩ : Fin d)) (Sum.inl i)
  refine ⟨hs_lt, ?_⟩
  have hfinal := hreach a (Nat.le_refl a)
  convert hfinal using 1 <;> apply congrArg Sum.inl <;> apply Fin.ext <;> simp [hdecomp]

/-- Every right-side cell is reachable from the first left cell of the same gcd block. -/
theorem overlapGraph_right_reachable_from_blockStart {d e : ℕ}
    (hd : 0 < d) (he : 0 < e) (j : Fin e) :
    ∃ i : Fin d,
      overlapVertexBlock d e (Sum.inl i) = overlapVertexBlock d e (Sum.inr j) ∧
      (overlapGraph d e).Reachable (Sum.inl i) (Sum.inr j) := by
  obtain ⟨hi, hov⟩ := attachmentCell_certificate hd he j.2
  let i : Fin d := ⟨attachmentCell d e j.1, hi⟩
  have hAdj : (overlapGraph d e).Adj (Sum.inl i) (Sum.inr j) :=
    (overlapGraph_adj_left_right _ _).2 hov
  refine ⟨i, overlapGraph_adj_same_block hd he hAdj, hAdj.reachable⟩

end EnterpriseMath.Scale
