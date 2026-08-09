import Mathlib.Tactic
import EnterpriseMath.Arithmetic.IntegerRoot

namespace EnterpriseMath.CollapseGap

open EnterpriseMath.IntegerRoot

/-- Derived comparison gap between a state and its perfect-power collapse. -/
def collapseGap (p n : ℕ) : ℕ :=
  n - collapse p n

/-- Sharp maximum gap inside the basin with root index `k`. -/
def maxGapInBasin (p k : ℕ) : ℕ :=
  (k + 1) ^ p - k ^ p - 1

/-- The collapse gap is the offset above the selected perfect-power floor. -/
theorem collapseGap_eq_root_offset {p n : ℕ} :
    collapseGap p n = n - root p n ^ p := by
  rfl

/-- P002-T01: the collapse gap is bounded by basin size minus one. -/
theorem collapseGap_le_max {p n : ℕ} (hp : p ≠ 0) :
    collapseGap p n ≤ maxGapInBasin p (root p n) := by
  have hcell := (root_eq_iff (p := p) (n := n) (k := root p n) hp).1 rfl
  simp only [collapseGap_eq_root_offset, maxGapInBasin]
  omega

/-- P002-T01 sharpness: the gap reaches its maximum exactly at the last state of the basin. -/
theorem collapseGap_eq_max_iff {p n : ℕ} (hp : p ≠ 0) :
    collapseGap p n = maxGapInBasin p (root p n) ↔
      n = (root p n + 1) ^ p - 1 := by
  have hcell := (root_eq_iff (p := p) (n := n) (k := root p n) hp).1 rfl
  simp only [collapseGap_eq_root_offset, maxGapInBasin]
  omega

end EnterpriseMath.CollapseGap
