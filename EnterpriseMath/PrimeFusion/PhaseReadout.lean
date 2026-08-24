import EnterpriseMath.PrimeFusion.MixedLocus

namespace EnterpriseMath.PrimeFusion

/-- Polynomial form of the T6 idempotent `e=-(r+r⁻¹)`. -/
theorem rootIdempotent_eq_polynomial {R : Type*} [CommRing R] (r : R) :
    rootIdempotent r = r ^ 3 + r ^ 2 + r + 1 := by
  simp [rootIdempotent, reciprocalCandidate]
  ring

/-- On the corrected oriented locus, the T6 idempotent is `0` on the Gaussian channel
and `1` on the Eisenstein channel. -/
theorem mixed_rootIdempotent_eq_channelIdempotent {p q : ℕ} {x : MixedCarrier p q}
    (hx : MixedLocus x) : rootIdempotent x = mixedChannelIdempotent p q := by
  apply Prod.ext
  · change rootIdempotent x.1 = (0 : ZMod p)
    rw [rootIdempotent_eq_polynomial]
    have hsq := gaussian_root_sq hx.1
    calc
      x.1 ^ 3 + x.1 ^ 2 + x.1 + 1 =
          x.1 * (-1) + (-1) + x.1 + 1 := by rw [hsq]; ring
      _ = 0 := by ring
  · change rootIdempotent x.2 = (1 : ZMod q)
    rw [rootIdempotent_eq_polynomial]
    have h3 := eisenstein_root_pow_three hx.2
    calc
      x.2 ^ 3 + x.2 ^ 2 + x.2 + 1 =
          1 + (x.2 ^ 2 + x.2 + 1) := by ring
      _ = 1 := by rw [hx.2]; ring

/-- T6/T11 cross-link in the source form: the sixth power is `2e-1`, where `e`
is the reciprocal-trace idempotent, and the proof uses only the two local equations. -/
theorem mixed_sixth_eq_two_rootIdempotent_sub_one {p q : ℕ} {x : MixedCarrier p q}
    (hx : MixedLocus x) : x ^ 6 = 2 * rootIdempotent x - 1 := by
  rw [mixed_rootIdempotent_eq_channelIdempotent hx]
  exact mixed_sixth_eq_two_idempotent_sub_one hx

/-- Divisibility form of the Gaussian sixth-power signature for an integral lift. -/
theorem gaussian_sixth_add_one_dvd {p : ℕ} {z : ℤ}
    (hz : (z : ZMod p) ^ 2 + 1 = 0) : (p : ℤ) ∣ z ^ 6 + 1 := by
  rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]
  push_cast
  rw [gaussian_root_pow_six hz]
  ring

/-- Divisibility form of the Eisenstein sixth-power signature for an integral lift. -/
theorem eisenstein_sixth_sub_one_dvd {q : ℕ} {z : ℤ}
    (hz : (z : ZMod q) ^ 2 + (z : ZMod q) + 1 = 0) : (q : ℤ) ∣ z ^ 6 - 1 := by
  rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]
  push_cast
  rw [eisenstein_root_pow_six hz]
  ring

/-- A prime greater than three is integrally coprime to `2`. -/
theorem two_isCoprime_prime_gt_three {p : ℕ} [Fact p.Prime] (hp3 : 3 < p) :
    IsCoprime (2 : ℤ) (p : ℤ) := by
  have hp : p.Prime := Fact.out
  have hpd : ¬ p ∣ 2 := by
    intro hd
    have hle : p ≤ 2 := Nat.le_of_dvd (by norm_num) hd
    omega
  have hnat : Nat.Coprime 2 p := (hp.coprime_iff_not_dvd.mpr hpd).symm
  rw [Int.isCoprime_iff_nat_coprime]
  simpa using hnat

/-- If `q | z^6-1` and `q>3` is prime, then `z^6+1` has no `q`-factor. -/
theorem sixth_add_one_isCoprime_opposite {q : ℕ} [Fact q.Prime] (hq3 : 3 < q)
    {z : ℤ} (hq : (q : ℤ) ∣ z ^ 6 - 1) : IsCoprime (z ^ 6 + 1) (q : ℤ) := by
  rcases two_isCoprime_prime_gt_three hq3 with ⟨s, t, hst⟩
  rcases hq with ⟨k, hk⟩
  refine ⟨s, t - s * k, ?_⟩
  linear_combination hst + s * hk

/-- If `p | z^6+1` and `p>3` is prime, then `z^6-1` has no `p`-factor. -/
theorem sixth_sub_one_isCoprime_opposite {p : ℕ} [Fact p.Prime] (hp3 : 3 < p)
    {z : ℤ} (hp : (p : ℤ) ∣ z ^ 6 + 1) : IsCoprime (z ^ 6 - 1) (p : ℤ) := by
  rcases two_isCoprime_prime_gt_three hp3 with ⟨s, t, hst⟩
  rcases hp with ⟨k, hk⟩
  refine ⟨-s, t + s * k, ?_⟩
  linear_combination hst - s * hk

/-- T11 dual-prime gcd readout for any integral lift of a corrected mixed-locus point.
The distinctness hypothesis is retained exactly from the source regime even though the local
no-leakage proof needs only primality and `>3`. -/
theorem dualPrime_sixth_gcd_readout {p q : ℕ} [Fact p.Prime] [Fact q.Prime]
    (hp3 : 3 < p) (hq3 : 3 < q) (_hpq : p ≠ q) (z : ℤ)
    (hpRoot : (z : ZMod p) ^ 2 + 1 = 0)
    (hqRoot : (z : ZMod q) ^ 2 + (z : ZMod q) + 1 = 0) :
    Int.gcd ((p * q : ℕ) : ℤ) (z ^ 6 + 1) = p ∧
      Int.gcd ((p * q : ℕ) : ℤ) (z ^ 6 - 1) = q := by
  have hpD : (p : ℤ) ∣ z ^ 6 + 1 := gaussian_sixth_add_one_dvd hpRoot
  have hqD : (q : ℤ) ∣ z ^ 6 - 1 := eisenstein_sixth_sub_one_dvd hqRoot
  constructor
  · exact gcd_recover_left_local rfl hpD
      (sixth_add_one_isCoprime_opposite hq3 hqD)
  · exact gcd_recover_right_local rfl hqD
      (sixth_sub_one_isCoprime_opposite hp3 hpD)

end EnterpriseMath.PrimeFusion
