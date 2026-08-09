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

/-- A basin state is recovered exactly from its perfect-power floor and collapse gap. -/
theorem basin_state_eq_pow_add_gap {p n k : ℕ} (hp : p ≠ 0)
    (hcollapse : collapse p n = k ^ p) :
    n = k ^ p + collapseGap p n := by
  have hfloor : k ^ p ≤ n := by
    rw [← hcollapse]
    exact collapse_le hp n
  simp only [collapseGap, hcollapse]
  omega

/-- P002-T02: every admissible gap coordinate has exactly one state in the fixed basin. -/
theorem existsUnique_basin_state_with_gap {p k g : ℕ} (hp : p ≠ 0)
    (hg : g ≤ maxGapInBasin p k) :
    ∃! n : ℕ, collapse p n = k ^ p ∧ collapseGap p n = g := by
  have hpow : k ^ p < (k + 1) ^ p := by
    simpa [root_pow hp k] using Nat.lt_pow_nthRoot_add_one hp (k ^ p)
  let n := k ^ p + g
  have hnUpper : n < (k + 1) ^ p := by
    dsimp [n]
    simp only [maxGapInBasin] at hg
    omega
  have hnCollapse : collapse p n = k ^ p :=
    (collapse_eq_pow_iff (p := p) (n := n) (k := k) hp).2 ⟨by
      dsimp [n]
      omega, hnUpper⟩
  have hnGap : collapseGap p n = g := by
    simp only [collapseGap, hnCollapse]
    dsimp [n]
    omega
  refine ⟨n, ⟨hnCollapse, hnGap⟩, ?_⟩
  intro m hm
  have hmRecover := basin_state_eq_pow_add_gap hp hm.1
  rw [hm.2] at hmRecover
  exact hmRecover.trans (by rfl)

end EnterpriseMath.CollapseGap
