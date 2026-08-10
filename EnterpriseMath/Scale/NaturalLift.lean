import EnterpriseMath.Scale.PerfectPowerNoDescent
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Scale-relative lift of a base endomap `H`: first forget intra-cell residue, apply
`H` to the quotient coordinate, then re-embed at scale `d`. -/
def naturalLift (H : ℕ → ℕ) (d m : ℕ) : ℕ :=
  d * H (m / d)

@[simp]
theorem naturalLift_one (H : ℕ → ℕ) (m : ℕ) :
    naturalLift H 1 m = H m := by
  simp [naturalLift]

/-- The scale-relative lift always lands on a scale boundary. -/
theorem naturalLift_divisible (H : ℕ → ℕ) (d m : ℕ) :
    d ∣ naturalLift H d m := by
  exact ⟨H (m / d), rfl⟩

/-- Exact naturality across one multiplicative scale step. This is the constructive
positive counterpart to the bare perfect-power no-descent theorem. -/
theorem naturalLift_natural_step (H : ℕ → ℕ) {d r m : ℕ} (hr : 0 < r) :
    floorQuot r (naturalLift H (d * r) m) =
      naturalLift H d (floorQuot r m) := by
  unfold floorQuot naturalLift
  have hleft : (d * r) * H (m / (d * r)) / r = d * H (m / (d * r)) := by
    calc
      (d * r) * H (m / (d * r)) / r =
          (d * H (m / (d * r))) * r / r := by
            congr 1
            ac_rfl
      _ = d * H (m / (d * r)) := Nat.mul_div_cancel _ hr
  rw [hleft]
  congr 1
  rw [Nat.div_div_eq_div_mul]
  simp [Nat.mul_comm]

/-- Divisibility-scale form: if `d | e`, the projection from scale `e` to scale `d`
commutes with the lifted dynamics. -/
theorem naturalLift_natural_of_dvd (H : ℕ → ℕ) {d e m : ℕ}
    (hd : 0 < d) (hde : d ∣ e) :
    floorQuot (e / d) (naturalLift H e m) =
      naturalLift H d (floorQuot (e / d) m) := by
  rcases hde with ⟨r, rfl⟩
  have hr : 0 < r := by
    by_contra hzero
    have : r = 0 := Nat.eq_zero_of_not_pos hzero
    subst r
    simp at hd
  have hquot : d * r / d = r := Nat.mul_div_cancel_left r hd
  simpa [hquot] using (naturalLift_natural_step H (d := d) (r := r) (m := m) hr)

/-- If the base map is downward, every positive-scale lift is downward. -/
theorem naturalLift_le {H : ℕ → ℕ} (hH : ∀ n, H n ≤ n) {d m : ℕ} :
    naturalLift H d m ≤ m := by
  calc
    naturalLift H d m = d * H (m / d) := rfl
    _ ≤ d * (m / d) := Nat.mul_le_mul_left d (hH (m / d))
    _ = (m / d) * d := by rw [Nat.mul_comm]
    _ ≤ m := Nat.div_mul_le_self m d

/-- Idempotence of the base map lifts to every positive scale. -/
theorem naturalLift_idempotent {H : ℕ → ℕ} (hH : Function.Idempotent H)
    {d m : ℕ} (hd : 0 < d) :
    naturalLift H d (naturalLift H d m) = naturalLift H d m := by
  unfold naturalLift
  have hdiv : d * H (m / d) / d = H (m / d) :=
    Nat.mul_div_cancel_left (H (m / d)) hd
  rw [hdiv, hH]

/-- Among maps whose outputs erase all scale-`d` residue, the scale-relative lift is
uniquely determined by its projected quotient dynamics. -/
theorem naturalLift_unique_residueErasing {H F : ℕ → ℕ} {d : ℕ} (hd : 0 < d)
    (herase : ∀ m, d ∣ F m)
    (hquot : ∀ m, F m / d = H (m / d)) :
    F = naturalLift H d := by
  funext m
  rcases herase m with ⟨k, hk⟩
  have hkquot : k = H (m / d) := by
    have := hquot m
    rw [hk, Nat.mul_div_cancel_left k hd] at this
    exact this
  rw [hk, hkquot]
  rfl

/-- Perfect-power collapse therefore has a nontrivial scale-natural replacement. -/
def naturalPerfectPowerCollapse (p d m : ℕ) : ℕ :=
  naturalLift (collapse p) d m

/-- The scale-natural perfect-power replacement agrees with bare collapse at scale 1. -/
@[simp]
theorem naturalPerfectPowerCollapse_one (p m : ℕ) :
    naturalPerfectPowerCollapse p 1 m = collapse p m := by
  simp [naturalPerfectPowerCollapse]

/-- For positive exponents, the scale-natural perfect-power replacement is idempotent
at every positive scale. -/
theorem naturalPerfectPowerCollapse_idempotent {p d m : ℕ}
    (hp : p ≠ 0) (hd : 0 < d) :
    naturalPerfectPowerCollapse p d (naturalPerfectPowerCollapse p d m) =
      naturalPerfectPowerCollapse p d m := by
  exact naturalLift_idempotent (fun n => collapse_idempotent hp n) hd

/-- For positive exponents, the scale-natural perfect-power replacement is downward. -/
theorem naturalPerfectPowerCollapse_le {p d m : ℕ} (hp : p ≠ 0) :
    naturalPerfectPowerCollapse p d m ≤ m := by
  exact naturalLift_le (fun n => collapse_le hp n)

end EnterpriseMath.Scale
