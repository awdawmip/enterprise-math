import EnterpriseMath.Scale.AllowedCellInterval
import EnterpriseMath.Scale.GridBridgeDescent
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- The scale-`d` cell `i` lies weakly to the left of the scale-`e` cell `j`:
its right boundary is at or before the other's left boundary. -/
def cellBefore (d i e j : ℕ) : Prop :=
  (i + 1) * e ≤ j * d

/-- Two cells are bridgeable at scale `h` if a single valid scale-`h` cell overlaps
both in positive length. -/
def cellsBridgeableAt (d i e j h : ℕ) : Prop :=
  ∃ k : Fin h, cellOverlap d i h k.1 ∧ cellOverlap e j h k.1

/-- Non-overlapping cells admit one of the two linear orders. -/
theorem cellBefore_or_reverse_of_not_overlap {d i e j : ℕ}
    (hnot : ¬ cellOverlap d i e j) :
    cellBefore d i e j ∨ cellBefore e j d i := by
  unfold cellOverlap cellBefore at hnot ⊢
  omega

/-- A strict cross-boundary inequality forces the corresponding crossed allowed-cell
endpoint inequality at every positive third scale. -/
theorem overlapLower_le_reverseUpper_of_cross {d i e j h : ℕ}
    (hd : 0 < d) (he : 0 < e) (hh : 0 < h)
    (hcross : i * e < (j + 1) * d) :
    overlapLower d i h ≤ overlapUpper e j h := by
  let k := overlapLower d i h
  have hkfloor : k * d ≤ i * h := by
    dsimp [k, overlapLower]
    exact Nat.div_mul_le_self _ _
  have h₁ : (k * e) * d ≤ (i * h) * e := by
    have h := Nat.mul_le_mul_right e hkfloor
    simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using h
  have hcrossh : (i * h) * e < ((j + 1) * h) * d := by
    have h := (Nat.mul_lt_mul_right hh).2 hcross
    simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using h
  have hkcrossd : (k * e) * d < ((j + 1) * h) * d :=
    lt_of_le_of_lt h₁ hcrossh
  have hkcross : k * e < (j + 1) * h :=
    (Nat.mul_lt_mul_right hd).1 hkcrossd
  have hkpred : k * e ≤ (j + 1) * h - 1 := Nat.le_sub_one_of_lt hkcross
  unfold overlapUpper
  exact (Nat.le_div_iff_mul_le he).2 hkpred

/-- Positive-length direct overlap is bridgeable at every positive third scale. -/
theorem cellsBridgeableAt_of_overlap {d i e j h : ℕ}
    (hd : 0 < d) (he : 0 < e) (hh : 0 < h)
    (hi : i < d) (hj : j < e)
    (hov : cellOverlap d i e j) :
    cellsBridgeableAt d i e j h := by
  have hfirst : overlapLower d i h ≤ overlapUpper e j h :=
    overlapLower_le_reverseUpper_of_cross hd he hh hov.1
  have hsecond : overlapLower e j h ≤ overlapUpper d i h :=
    overlapLower_le_reverseUpper_of_cross he hd hh hov.2
  obtain ⟨k, hAk, hBk⟩ :=
    (allowedIntervals_intersect_iff hd he hh).2 ⟨hfirst, hsecond⟩
  have hIA := (cellOverlap_iff_allowedInterval hd hh).1 hAk
  have hklt : k < h :=
    lt_of_le_of_lt hIA.2 (overlapUpper_lt_scale hd hh hi)
  exact ⟨⟨k, hklt⟩, hAk, hBk⟩

/-- A closed inner gap contains an `h`-grid point iff the ordered allowed `h`-cell
intervals are separated. -/
theorem gapHasGridPoint_iff_allowedSeparated {d i e j h : ℕ}
    (hd : 0 < d) (he : 0 < e) (hh : 0 < h) :
    gapHasGridPoint (i + 1) d j e h ↔
      overlapUpper d i h < overlapLower e j h := by
  unfold gapHasGridPoint fracInClosedGap fracLe
  constructor
  · rintro ⟨m, hleft, hright⟩
    have hApos : 0 < (i + 1) * h := by positivity
    have hUpperLt : overlapUpper d i h < m := by
      unfold overlapUpper
      apply (Nat.div_lt_iff_lt_mul hd).2
      omega
    have hmLower : m ≤ overlapLower e j h := by
      unfold overlapLower
      exact (Nat.le_div_iff_mul_le he).2 hright
    exact lt_of_lt_of_le hUpperLt hmLower
  · intro hsep
    let m := overlapLower e j h
    have hright : m * e ≤ j * h := by
      dsimp [m, overlapLower]
      exact Nat.div_mul_le_self _ _
    have hApos : 0 < (i + 1) * h := by positivity
    have hceil : (i + 1) * h ≤ (overlapUpper d i h + 1) * d := by
      unfold overlapUpper
      have hlt := Nat.lt_div_mul_add ((i + 1) * h - 1) hd
      omega
    have hmge : overlapUpper d i h + 1 ≤ m := by omega
    have hleft : (i + 1) * h ≤ m * d := by
      exact le_trans hceil (Nat.mul_le_mul_right d hmge)
    exact ⟨m, hleft, hright⟩

/-- Under a fixed left-to-right order, the first crossed allowed-interval inequality
is automatic. -/
theorem overlapLower_le_reverseUpper_of_before {d i e j h : ℕ}
    (hd : 0 < d) (he : 0 < e) (hh : 0 < h)
    (hbefore : cellBefore d i e j) :
    overlapLower d i h ≤ overlapUpper e j h := by
  have hcross : i * e < (j + 1) * d := by
    unfold cellBefore at hbefore
    nlinarith
  exact overlapLower_le_reverseUpper_of_cross hd he hh hcross

/-- Central cell-gap equivalence: for two ordered positive cells, being bridgeable by
one scale-`h` cell is equivalent to the closed inner gap containing no `h`-grid point. -/
theorem cellsBridgeableAt_iff_gapNoGridPoint {d i e j h : ℕ}
    (hd : 0 < d) (he : 0 < e) (hh : 0 < h)
    (hi : i < d) (hj : j < e)
    (hbefore : cellBefore d i e j) :
    cellsBridgeableAt d i e j h ↔
      ¬ gapHasGridPoint (i + 1) d j e h := by
  have hfirst := overlapLower_le_reverseUpper_of_before hd he hh hbefore
  rw [gapHasGridPoint_iff_allowedSeparated hd he hh]
  constructor
  · rintro ⟨k, hAk, hBk⟩ hsep
    have hIA := (cellOverlap_iff_allowedInterval hd hh).1 hAk
    have hIB := (cellOverlap_iff_allowedInterval he hh).1 hBk
    omega
  · intro hnotGap
    have hsecond : overlapLower e j h ≤ overlapUpper d i h := by omega
    obtain ⟨k, hAk, hBk⟩ :=
      (allowedIntervals_intersect_iff hd he hh).2 ⟨hfirst, hsecond⟩
    have hIA := (cellOverlap_iff_allowedInterval hd hh).1 hAk
    have hklt : k < h :=
      lt_of_le_of_lt hIA.2 (overlapUpper_lt_scale hd hh hi)
    exact ⟨⟨k, hklt⟩, hAk, hBk⟩

end EnterpriseMath.Scale
