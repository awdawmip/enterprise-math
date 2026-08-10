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

/-- Non-overlapping positive cells admit one of the two linear orders. -/
theorem cellBefore_or_reverse_of_not_overlap {d i e j : ℕ}
    (hnot : ¬ cellOverlap d i e j) :
    cellBefore d i e j ∨ cellBefore e j d i := by
  unfold cellOverlap cellBefore at hnot ⊢
  omega

/-- A positive-length direct overlap is bridgeable at every positive third scale. -/
theorem cellsBridgeableAt_of_overlap {d i e j h : ℕ}
    (hd : 0 < d) (he : 0 < e) (hh : 0 < h)
    (hi : i < d) (hj : j < e)
    (hov : cellOverlap d i e j) :
    cellsBridgeableAt d i e j h := by
  let k := overlapLower d i h
  have hk : k < h := overlapLower_lt_scale hd hh hi
  have hAk : cellOverlap d i h k := by
    apply (cellOverlap_iff_allowedInterval hd hh).2
    refine ⟨Nat.le_refl _, overlapLower_le_overlapUpper hd hh⟩
  have hleft_cross : overlapLower e j h ≤ overlapUpper d i h := by
    by_contra hnot
    have hgap : overlapUpper d i h < overlapLower e j h := by omega
    have hsep : (i + 1) * e ≤ j * d := by
      -- A separating h-grid boundary between the two cells would force the old
      -- cells themselves to be non-overlapping, contradicting `hov`.
      have hUA : ((i + 1) * h - 1) / d < (j * h) / e := by
        simpa [overlapUpper, overlapLower] using hgap
      have hApos : 0 < (i + 1) * h := by positivity
      have hceil : (i + 1) * h ≤ (((i + 1) * h - 1) / d + 1) * d := by
        have hlt := Nat.lt_div_mul_add ((i + 1) * h - 1) hd
        omega
      have hmid : (((i + 1) * h - 1) / d + 1) ≤ (j * h) / e := by omega
      have hright : ((j * h) / e) * e ≤ j * h := Nat.div_mul_le_self _ _
      nlinarith
    unfold cellOverlap at hov
    omega
  have hBLower : overlapLower e j h ≤ k := by
    dsimp [k]
    exact le_trans hleft_cross (overlapLower_le_overlapUpper hd hh)
  have hBUpper : k ≤ overlapUpper e j h := by
    have hother : overlapLower d i h ≤ overlapUpper e j h := by
      have hpair := (allowedIntervals_intersect_iff hd he hh)
      -- Direct overlap implies the first crossed interval inequality by the same
      -- endpoint geometry; establish it directly by contradiction.
      by_contra hnot
      have hgap : overlapUpper e j h < overlapLower d i h := by omega
      have hsep : (j + 1) * d ≤ i * e := by
        have hApos : 0 < (j + 1) * h := by positivity
        have hceil : (j + 1) * h ≤ (((j + 1) * h - 1) / e + 1) * e := by
          have hlt := Nat.lt_div_mul_add ((j + 1) * h - 1) he
          omega
        have hmid : (((j + 1) * h - 1) / e + 1) ≤ (i * h) / d := by
          simpa [overlapUpper, overlapLower] using hgap
        have hright : ((i * h) / d) * d ≤ i * h := Nat.div_mul_le_self _ _
        nlinarith
      unfold cellOverlap at hov
      omega
    simpa [k] using hother
  refine ⟨⟨k, hk⟩, hAk, ?_⟩
  exact (cellOverlap_iff_allowedInterval he hh).2 ⟨hBLower, hBUpper⟩

/-- Under a fixed left-to-right order, a closed inner gap contains an `h`-grid point
iff the two allowed `h`-cell intervals are disjoint in that order. -/
theorem gapHasGridPoint_iff_allowedSeparated {d i e j h : ℕ}
    (hd : 0 < d) (he : 0 < e) (hh : 0 < h)
    (hbefore : cellBefore d i e j) :
    gapHasGridPoint (i + 1) d j e h ↔
      overlapUpper d i h < overlapLower e j h := by
  unfold gapHasGridPoint fracInClosedGap fracLe
  constructor
  · rintro ⟨m, hleft, hright⟩
    have hApos : 0 < (i + 1) * h := by positivity
    have hUpperLt : overlapUpper d i h < m := by
      unfold overlapUpper
      apply (Nat.div_lt_iff_lt_mul hd).2
      have : (i + 1) * h - 1 < m * d := by omega
      exact this
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
    (hi : i < d) (hj : j < e)
    (hbefore : cellBefore d i e j) :
    overlapLower d i h ≤ overlapUpper e j h := by
  have hleft : i * e < (j + 1) * d := by
    unfold cellBefore at hbefore
    nlinarith
  by_contra hnot
  have hsep : overlapUpper e j h < overlapLower d i h := by omega
  have hgap := (gapHasGridPoint_iff_allowedSeparated he hd hh (by
    unfold cellBefore
    nlinarith)).2 hsep
  rcases hgap with ⟨m, hmleft, hmright⟩
  unfold fracInClosedGap fracLe at hmleft hmright
  nlinarith

/-- Central cell-gap equivalence: for two ordered positive cells, being bridgeable by
one scale-`h` cell is equivalent to the closed inner gap containing no `h`-grid point. -/
theorem cellsBridgeableAt_iff_gapNoGridPoint {d i e j h : ℕ}
    (hd : 0 < d) (he : 0 < e) (hh : 0 < h)
    (hi : i < d) (hj : j < e)
    (hbefore : cellBefore d i e j) :
    cellsBridgeableAt d i e j h ↔
      ¬ gapHasGridPoint (i + 1) d j e h := by
  have hfirst := overlapLower_le_reverseUpper_of_before hd he hh hi hj hbefore
  rw [gapHasGridPoint_iff_allowedSeparated hd he hh hbefore]
  constructor
  · rintro ⟨k, hAk, hBk⟩ hsep
    have hIA := (cellOverlap_iff_allowedInterval hd hh).1 hAk
    have hIB := (cellOverlap_iff_allowedInterval he hh).1 hBk
    omega
  · intro hnotGap
    have hsecond : overlapLower e j h ≤ overlapUpper d i h := by omega
    have hpair : ∃ k,
        cellOverlap d i h k ∧ cellOverlap e j h k :=
      (allowedIntervals_intersect_iff hd he hh).2 ⟨hfirst, hsecond⟩
    rcases hpair with ⟨k, hAk, hBk⟩
    have hk : k < h := overlapLower_lt_scale hd hh hi
    -- `k` itself need not equal the left endpoint, so use either overlap to bound it.
    have hIA := (cellOverlap_iff_allowedInterval hd hh).1 hAk
    have hk' : k < h := by
      exact lt_of_le_of_lt hIA.2 (overlapUpper_lt_scale hd hh hi)
    exact ⟨⟨k, hk'⟩, hAk, hBk⟩

end EnterpriseMath.Scale
