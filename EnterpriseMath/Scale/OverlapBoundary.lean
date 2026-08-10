import Mathlib.Data.Nat.GCD.Basic

namespace EnterpriseMath.Scale

/-- Cross-multiplication equality for boundaries `i/d = j/e` without introducing rationals. -/
def boundaryEq (d i e j : ℕ) : Prop :=
  i * e = j * d

/-- Multiplying both scale denominators by the same positive factor does not change
boundary coincidence. -/
theorem boundaryEq_mul_right_iff {d e g i j : ℕ} (hg : 0 < g) :
    boundaryEq (d * g) i (e * g) j ↔ boundaryEq d i e j := by
  unfold boundaryEq
  constructor
  · intro h
    apply Nat.mul_right_cancel hg
    simpa [Nat.mul_assoc] using h
  · intro h
    simpa [Nat.mul_assoc] using congrArg (fun x : ℕ => x * g) h

/-- For coprime positive scales, coincident grid boundaries occur exactly at a common
integer index: `i/d = j/e` iff `i=d*k` and `j=e*k` for some `k`.

This is the arithmetic core of the R007 overlap-component decomposition. -/
theorem boundaryEq_coprime_iff {d e i j : ℕ} (hcop : d.Coprime e) (hd : 0 < d) :
    boundaryEq d i e j ↔ ∃ k, i = d * k ∧ j = e * k := by
  constructor
  · intro h
    have hdi : d ∣ i := by
      apply hcop.dvd_of_dvd_mul_right
      rw [h]
      exact Nat.dvd_mul_left d j
    rcases hdi with ⟨k, hk⟩
    refine ⟨k, hk, ?_⟩
    apply Nat.mul_right_cancel hd
    calc
      j * d = i * e := h.symm
      _ = (d * k) * e := by rw [hk]
      _ = (e * k) * d := by
        simp [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  · rintro ⟨k, rfl, rfl⟩
    simp [boundaryEq, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

/-- Two arbitrary positive uniform grids share boundaries exactly at multiples of their
reduced coprime step sizes `d/gcd(d,e)` and `e/gcd(d,e)`.

Equivalently, the common boundary grid is the `gcd(d,e)` grid. -/
theorem boundaryEq_gcd_iff {d e i j : ℕ} (hd : 0 < d) :
    boundaryEq d i e j ↔
      ∃ k, i = (d / d.gcd e) * k ∧ j = (e / d.gcd e) * k := by
  let g := d.gcd e
  change boundaryEq d i e j ↔
    ∃ k, i = (d / g) * k ∧ j = (e / g) * k
  have hg : 0 < g := by
    dsimp [g]
    exact Nat.gcd_pos_of_pos_left e hd
  have hcop : (d / g).Coprime (e / g) := by
    dsimp [g]
    exact Nat.coprime_div_gcd_div_gcd (Nat.gcd_pos_of_pos_left e hd)
  have hd' : 0 < d / g := by
    dsimp [g]
    exact Nat.div_gcd_pos_of_pos_left e hd
  have hd_decomp : d = (d / g) * g := by
    exact (Nat.div_mul_cancel (by
      dsimp [g]
      exact Nat.gcd_dvd_left d e)).symm
  have he_decomp : e = (e / g) * g := by
    exact (Nat.div_mul_cancel (by
      dsimp [g]
      exact Nat.gcd_dvd_right d e)).symm
  have hscale : boundaryEq d i e j ↔ boundaryEq (d / g) i (e / g) j := by
    rw [hd_decomp, he_decomp]
    exact boundaryEq_mul_right_iff hg
  calc
    boundaryEq d i e j ↔ boundaryEq (d / g) i (e / g) j := hscale
    _ ↔ ∃ k, i = (d / g) * k ∧ j = (e / g) * k :=
      boundaryEq_coprime_iff hcop hd'

end EnterpriseMath.Scale
