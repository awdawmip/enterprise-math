import EnterpriseMath.Scale.OverlapBoundary
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- A scale-`d` boundary index `i` is also an `e`-grid boundary exactly when the
reduced block width `d/gcd(d,e)` divides `i`. -/
theorem scale_dvd_mul_iff_reduced_dvd {d e i : ℕ} (hd : 0 < d) :
    d ∣ i * e ↔ (d / d.gcd e) ∣ i := by
  constructor
  · intro hdiv
    rcases hdiv with ⟨j, hj⟩
    have hboundary : boundaryEq d i e j := by
      unfold boundaryEq
      simpa [Nat.mul_comm] using hj.symm
    rcases (boundaryEq_gcd_iff hd).1 hboundary with ⟨k, hik, _⟩
    exact ⟨k, hik⟩
  · rintro ⟨k, rfl⟩
    let g := d.gcd e
    let d' := d / g
    let e' := e / g
    have hd_decomp : d = d' * g := by
      dsimp [d', g]
      exact (Nat.div_mul_cancel (Nat.gcd_dvd_left d e)).symm
    have he_decomp : e = e' * g := by
      dsimp [e', g]
      exact (Nat.div_mul_cancel (Nat.gcd_dvd_right d e)).symm
    refine ⟨k * e', ?_⟩
    rw [hd_decomp, he_decomp]
    dsimp [d']
    ac_rfl

/-- A reduced-block interior index cannot be a common grid boundary. -/
theorem not_scale_dvd_mul_of_between_reduced_multiples {d e k i : ℕ}
    (hd : 0 < d)
    (hlo : k * (d / d.gcd e) < i)
    (hhi : i < (k + 1) * (d / d.gcd e)) :
    ¬ d ∣ i * e := by
  intro hdiv
  have hred : (d / d.gcd e) ∣ i :=
    (scale_dvd_mul_iff_reduced_dvd hd).1 hdiv
  rcases hred with ⟨t, ht⟩
  have hd' : 0 < d / d.gcd e := Nat.div_gcd_pos_of_pos_left e hd
  have hkt : k < t := by
    apply (Nat.mul_lt_mul_left hd').1
    simpa [ht, Nat.mul_comm] using hlo
  have htk : t < k + 1 := by
    apply (Nat.mul_lt_mul_left hd').1
    simpa [ht, Nat.mul_comm] using hhi
  omega

end EnterpriseMath.Scale
