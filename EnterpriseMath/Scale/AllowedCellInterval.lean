import EnterpriseMath.Scale.OverlapCells
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Leftmost scale-`N` cell overlapping the scale-`d` cell `i`. -/
def overlapLower (d i N : ℕ) : ℕ :=
  (i * N) / d

/-- Rightmost scale-`N` cell overlapping the scale-`d` cell `i`. -/
def overlapUpper (d i N : ℕ) : ℕ :=
  ((i + 1) * N - 1) / d

/-- Exact intervalization of the overlap relation. For positive scales, the set of
`N`-cell indices overlapping one old `d`-cell is precisely the integer interval
`[overlapLower d i N, overlapUpper d i N]`. -/
theorem cellOverlap_iff_allowedInterval {d i N j : ℕ}
    (hd : 0 < d) (hN : 0 < N) :
    cellOverlap d i N j ↔
      overlapLower d i N ≤ j ∧ j ≤ overlapUpper d i N := by
  let A := (i + 1) * N
  have hA : 0 < A := by
    dsimp [A]
    positivity
  unfold cellOverlap overlapLower overlapUpper
  constructor
  · rintro ⟨hleft, hright⟩
    constructor
    · have hdiv : (i * N) / d < j + 1 :=
        (Nat.div_lt_iff_lt_mul hd).2 hleft
      omega
    · have hmul : j * d ≤ A - 1 := (Nat.lt_iff_le_pred hA).1 hright
      exact (Nat.le_div_iff_mul_le hd).2 hmul
  · rintro ⟨hlow, hupp⟩
    constructor
    · have hdiv : (i * N) / d < j + 1 := by omega
      exact (Nat.div_lt_iff_lt_mul hd).1 hdiv
    · have hmul : j * d ≤ A - 1 := (Nat.le_div_iff_mul_le hd).1 hupp
      have hpred : A - 1 < A := by omega
      exact lt_of_le_of_lt hmul hpred

/-- The left endpoint of an allowed interval is always a valid `N`-cell when the old
cell itself is valid. -/
theorem overlapLower_lt_scale {d i N : ℕ}
    (hd : 0 < d) (hN : 0 < N) (hi : i < d) :
    overlapLower d i N < N := by
  unfold overlapLower
  apply (Nat.div_lt_iff_lt_mul hd).2
  have h := (Nat.mul_lt_mul_right hN).2 hi
  simpa [Nat.mul_comm] using h

/-- The right endpoint of an allowed interval is also a valid `N`-cell. -/
theorem overlapUpper_lt_scale {d i N : ℕ}
    (hd : 0 < d) (hN : 0 < N) (hi : i < d) :
    overlapUpper d i N < N := by
  unfold overlapUpper
  apply (Nat.div_lt_iff_lt_mul hd).2
  have hsucc : i + 1 ≤ d := by omega
  have hA_le : (i + 1) * N ≤ d * N := Nat.mul_le_mul_right N hsucc
  have hA_pos : 0 < (i + 1) * N := by positivity
  have hpred_lt : (i + 1) * N - 1 < d * N := by omega
  simpa [Nat.mul_comm] using hpred_lt

/-- Every valid old cell has at least one allowed new-cell index. -/
theorem overlapLower_le_overlapUpper {d i N : ℕ}
    (hd : 0 < d) (hN : 0 < N) :
    overlapLower d i N ≤ overlapUpper d i N := by
  let j := overlapLower d i N
  have hleft : i * N < (j + 1) * d := by
    have h := Nat.lt_div_mul_add (i * N) hd
    simpa [j, overlapLower, Nat.mul_comm] using h
  have hfloor : j * d ≤ i * N := by
    simpa [j, overlapLower] using Nat.div_mul_le_self (i * N) d
  have hstep : i * N < (i + 1) * N := (Nat.mul_lt_mul_right hN).2 (Nat.lt_succ_self i)
  have hright : j * d < (i + 1) * N := lt_of_le_of_lt hfloor hstep
  exact ((cellOverlap_iff_allowedInterval hd hN).1 ⟨hleft, hright⟩).2

/-- Pairwise overlap of two allowed integer intervals is equivalent to the two crossed
endpoint inequalities. -/
theorem allowedIntervals_intersect_iff {d i e j N : ℕ}
    (hd : 0 < d) (he : 0 < e) (hN : 0 < N) :
    (∃ k,
      cellOverlap d i N k ∧ cellOverlap e j N k) ↔
    overlapLower d i N ≤ overlapUpper e j N ∧
      overlapLower e j N ≤ overlapUpper d i N := by
  constructor
  · rintro ⟨k, hik, hjk⟩
    have hi := (cellOverlap_iff_allowedInterval hd hN).1 hik
    have hj := (cellOverlap_iff_allowedInterval he hN).1 hjk
    exact ⟨le_trans hi.1 hj.2, le_trans hj.1 hi.2⟩
  · rintro ⟨hij, hji⟩
    let k := max (overlapLower d i N) (overlapLower e j N)
    have hki : overlapLower d i N ≤ k := le_max_left _ _
    have hkj : overlapLower e j N ≤ k := le_max_right _ _
    have kiu : k ≤ overlapUpper d i N := by
      exact max_le
        (overlapLower_le_overlapUpper hd hN)
        hji
    have kju : k ≤ overlapUpper e j N := by
      exact max_le
        hij
        (overlapLower_le_overlapUpper he hN)
    refine ⟨k, ?_, ?_⟩
    · exact (cellOverlap_iff_allowedInterval hd hN).2 ⟨hki, kiu⟩
    · exact (cellOverlap_iff_allowedInterval he hN).2 ⟨hkj, kju⟩

end EnterpriseMath.Scale
