import EnterpriseMath.Arithmetic.IntegerRoot
import Mathlib.Algebra.Order.Ring.Pow
import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic

namespace EnterpriseMath.Scale

open EnterpriseMath.IntegerRoot

/-- Uniform floor quotient used by the R007 scale-descent problem. -/
def floorQuot (r n : ℕ) : ℕ := n / r

/-- The successor power `(r+1)^p` always has residue one modulo `r` when `r>=2`. -/
theorem successorPower_mod_scale {p r : ℕ} (hr : 2 ≤ r) :
    (r + 1) ^ p % r = 1 := by
  have hbase : r + 1 ≡ 1 [MOD r] := by simp
  have hpow := Nat.ModEq.pow p hbase
  simpa [Nat.ModEq, Nat.mod_eq_of_lt (by omega : 1 < r)] using hpow

/-- The predecessor of `(r+1)^p` lies in the same floor-quotient fiber as the
perfect power itself. -/
theorem successorPower_predecessor_same_floorQuot {p r : ℕ} (hr : 2 ≤ r) :
    floorQuot r ((r + 1) ^ p - 1) = floorQuot r ((r + 1) ^ p) := by
  let z := (r + 1) ^ p
  have hr0 : 0 < r := by omega
  have hzmod : z % r = 1 := by
    dsimp [z]
    exact successorPower_mod_scale hr
  have hz_decomp : z = r * (z / r) + 1 := by
    calc
      z = z % r + r * (z / r) := (Nat.mod_add_div z r).symm
      _ = 1 + r * (z / r) := by rw [hzmod]
      _ = r * (z / r) + 1 := by omega
  have hpred : z - 1 = r * (z / r) := by omega
  unfold floorQuot
  change (z - 1) / r = z / r
  rw [hpred]
  exact Nat.mul_div_cancel_left (z / r) hr0

/-- For every nontrivial exponent and scale, consecutive powers are separated by
more than one whole scale cell. -/
theorem successorPower_gap_gt_scale {p r : ℕ} (hp : 2 ≤ p) (hr : 2 ≤ r) :
    r ^ p + r < (r + 1) ^ p := by
  have hbern : r ^ p + p * r ^ (p - 1) ≤ (r + 1) ^ p := by
    simpa using
      (pow_add_mul_le_add_pow (a := r) (b := 1) (by omega) (by omega) p)
  have hpow_ge : r ≤ r ^ (p - 1) := by
    have hexp : 1 ≤ p - 1 := by omega
    simpa using Nat.pow_le_pow_right (by omega : 0 < r) hexp
  have hterm : r < p * r ^ (p - 1) := by
    nlinarith
  exact lt_of_lt_of_le (Nat.add_lt_add_left hterm (r ^ p)) hbern

/-- Just before the perfect-power boundary `(r+1)^p`, collapse still lands at `r^p`. -/
theorem collapse_successorPower_predecessor {p r : ℕ} (hp : 2 ≤ p) :
    collapse p ((r + 1) ^ p - 1) = r ^ p := by
  have hp0 : p ≠ 0 := by omega
  have hpowlt : r ^ p < (r + 1) ^ p :=
    Nat.pow_lt_pow_left (Nat.lt_succ_self r) hp0
  have hlow : r ^ p ≤ (r + 1) ^ p - 1 := Nat.le_sub_one_of_lt hpowlt
  have hpos : 0 < (r + 1) ^ p := by positivity
  have hhigh : (r + 1) ^ p - 1 < (r + 1) ^ p := by omega
  exact (collapse_eq_pow_iff (p := p) (n := (r + 1) ^ p - 1) (k := r) hp0).2
    ⟨hlow, hhigh⟩

/-- At the perfect-power boundary, collapse fixes the state. -/
theorem collapse_successorPower {p r : ℕ} (hp : 2 ≤ p) :
    collapse p ((r + 1) ^ p) = (r + 1) ^ p := by
  have hp0 : p ≠ 0 := by omega
  exact (collapse_eq_self_iff hp0 ((r + 1) ^ p)).2 ⟨r + 1, rfl⟩

/-- The two same-fiber witness states have strictly different coarse futures after
perfect-power collapse. -/
theorem successorPower_witness_coarse_future_lt {p r : ℕ} (hp : 2 ≤ p) (hr : 2 ≤ r) :
    floorQuot r (collapse p ((r + 1) ^ p - 1)) <
      floorQuot r (collapse p ((r + 1) ^ p)) := by
  rw [collapse_successorPower_predecessor hp, collapse_successorPower hp]
  unfold floorQuot
  have hr0 : 0 < r := by omega
  have hrne : r ≠ 0 := by omega
  have hp0 : p ≠ 0 := by omega
  have hpowdiv : r ^ p / r = r ^ (p - 1) :=
    (Nat.pow_sub_one hrne hp0).symm
  rw [hpowdiv]
  have hmul : (r ^ (p - 1) + 1) * r = r ^ p + r := by
    calc
      (r ^ (p - 1) + 1) * r = r ^ (p - 1) * r + r := by simp [Nat.add_mul]
      _ = r ^ p + r := by rw [pow_sub_one_mul hp0 r]
  have hle : (r ^ (p - 1) + 1) * r ≤ (r + 1) ^ p := by
    rw [hmul]
    exact Nat.le_of_lt (successorPower_gap_gt_scale hp hr)
  have hquot : r ^ (p - 1) + 1 ≤ (r + 1) ^ p / r :=
    (Nat.le_div_iff_mul_le hr0).2 hle
  omega

/-- R007-T01: for every `p,r>=2`, no deterministic map on the bare floor quotient
can reproduce the projected future of bare perfect-power collapse. -/
theorem perfectPowerCollapse_no_floorQuot_descent {p r : ℕ} (hp : 2 ≤ p) (hr : 2 ≤ r) :
    ¬ ∃ G : ℕ → ℕ,
      ∀ n : ℕ, floorQuot r (collapse p n) = G (floorQuot r n) := by
  rintro ⟨G, hG⟩
  let x := (r + 1) ^ p - 1
  let y := (r + 1) ^ p
  have hxy : floorQuot r x = floorQuot r y := by
    dsimp [x, y]
    exact successorPower_predecessor_same_floorQuot hr
  have hfuture : floorQuot r (collapse p x) < floorQuot r (collapse p y) := by
    dsimp [x, y]
    exact successorPower_witness_coarse_future_lt hp hr
  have heq : floorQuot r (collapse p x) = floorQuot r (collapse p y) := by
    calc
      floorQuot r (collapse p x) = G (floorQuot r x) := hG x
      _ = G (floorQuot r y) := congrArg G hxy
      _ = floorQuot r (collapse p y) := (hG y).symm
  exact (Nat.ne_of_lt hfuture) heq

end EnterpriseMath.Scale
