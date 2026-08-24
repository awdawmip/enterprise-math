import EnterpriseMath.PrimeFusion.ArithmeticSplit
import Mathlib.RingTheory.Fintype

namespace EnterpriseMath.PrimeFusion

/-- Corrected T10 universe: the first coordinate is the Gaussian/N channel modulo `p`,
and the second coordinate is the Eisenstein/C channel modulo `q`. -/
abbrev MixedCarrier (p q : ℕ) := ZMod p × ZMod q

/-- Corrected channel-oriented mixed locus `M_{p,q}`. -/
def MixedLocus {p q : ℕ} (x : MixedCarrier p q) : Prop :=
  x.1 ^ 2 + 1 = 0 ∧ x.2 ^ 2 + x.2 + 1 = 0

/-- A Gaussian local root has square `-1`. -/
theorem gaussian_root_sq {p : ℕ} {x : ZMod p} (hx : x ^ 2 + 1 = 0) : x ^ 2 = -1 := by
  linear_combination hx

/-- A Gaussian local root has fourth power one. -/
theorem gaussian_root_pow_four {p : ℕ} {x : ZMod p} (hx : x ^ 2 + 1 = 0) : x ^ 4 = 1 := by
  have hsq := gaussian_root_sq hx
  calc
    x ^ 4 = (x ^ 2) ^ 2 := by ring
    _ = (-1) ^ 2 := by rw [hsq]
    _ = 1 := by ring

/-- For a prime modulus greater than two, a Gaussian local root has exact order four. -/
theorem gaussian_root_order {p : ℕ} [Fact p.Prime] (hp2 : 2 < p)
    {x : ZMod p} (hx : x ^ 2 + 1 = 0) : orderOf x = 4 := by
  have htwo : (2 : ZMod p) ≠ 0 := by
    intro hzero
    have hd : p ∣ 2 := (ZMod.natCast_eq_zero_iff 2 p).mp hzero
    have hle : p ≤ 2 := Nat.le_of_dvd (by norm_num) hd
    omega
  have hsq : x ^ 2 = -1 := gaussian_root_sq hx
  have h1 : x ≠ 1 := by
    intro hxeq
    have hz := hx
    rw [hxeq] at hz
    apply htwo
    simpa using hz
  have h2 : x ^ 2 ≠ 1 := by
    intro heq
    have hneg : (-1 : ZMod p) = 1 := hsq.symm.trans heq
    have hadd := congrArg (fun z : ZMod p => z + 1) hneg
    apply htwo
    simpa using hadd.symm
  have h4 : x ^ 4 = 1 := gaussian_root_pow_four hx
  have h3 : x ^ 3 ≠ 1 := by
    intro heq
    apply h1
    calc
      x = x ^ 3 * x := by rw [heq]; simp
      _ = x ^ 4 := by ring
      _ = 1 := h4
  rw [orderOf_eq_iff (by norm_num : 0 < 4)]
  refine ⟨h4, ?_⟩
  intro m hm hpos
  interval_cases m
  · omega
  · simpa using h1
  · simpa using h2
  · simpa using h3

/-- An Eisenstein local root has cube one. -/
theorem eisenstein_root_pow_three {q : ℕ} {x : ZMod q}
    (hx : x ^ 2 + x + 1 = 0) : x ^ 3 = 1 := by
  have hz : x ^ 3 - 1 = 0 := by
    calc
      x ^ 3 - 1 = (x - 1) * (x ^ 2 + x + 1) := by ring
      _ = 0 := by rw [hx]; ring
  linear_combination hz

/-- For a prime modulus greater than three, an Eisenstein local root has exact order three. -/
theorem eisenstein_root_order {q : ℕ} [Fact q.Prime] (hq3 : 3 < q)
    {x : ZMod q} (hx : x ^ 2 + x + 1 = 0) : orderOf x = 3 := by
  have hthree : (3 : ZMod q) ≠ 0 := by
    intro hzero
    have hd : q ∣ 3 := (ZMod.natCast_eq_zero_iff 3 q).mp hzero
    have hle : q ≤ 3 := Nat.le_of_dvd (by norm_num) hd
    omega
  have h1 : x ≠ 1 := by
    intro hxeq
    have hz := hx
    rw [hxeq] at hz
    apply hthree
    simpa using hz
  have h3 : x ^ 3 = 1 := eisenstein_root_pow_three hx
  have h2 : x ^ 2 ≠ 1 := by
    intro heq
    apply h1
    calc
      x = x * x ^ 2 := by rw [heq]; simp
      _ = x ^ 3 := by ring
      _ = 1 := h3
  rw [orderOf_eq_iff (by norm_num : 0 < 3)]
  refine ⟨h3, ?_⟩
  intro m hm hpos
  interval_cases m
  · omega
  · simpa using h1
  · simpa using h2

/-- The local power used for the exponent `5` in the mixed orbit. -/
theorem gaussian_root_pow_five {p : ℕ} {x : ZMod p} (hx : x ^ 2 + 1 = 0) : x ^ 5 = x := by
  have hsq := gaussian_root_sq hx
  calc
    x ^ 5 = x * (x ^ 2) ^ 2 := by ring
    _ = x := by rw [hsq]; ring

/-- Gaussian powers `7` and `11` both switch to the opposite local root. -/
theorem gaussian_root_pow_seven {p : ℕ} {x : ZMod p} (hx : x ^ 2 + 1 = 0) : x ^ 7 = -x := by
  have hsq := gaussian_root_sq hx
  calc
    x ^ 7 = x * (x ^ 2) ^ 3 := by ring
    _ = -x := by rw [hsq]; ring

/-- Gaussian exponent `11` also switches to the opposite local root. -/
theorem gaussian_root_pow_eleven {p : ℕ} {x : ZMod p} (hx : x ^ 2 + 1 = 0) : x ^ 11 = -x := by
  have hsq := gaussian_root_sq hx
  calc
    x ^ 11 = x * (x ^ 2) ^ 5 := by ring
    _ = -x := by rw [hsq]; ring

/-- Eisenstein exponent `5` selects the second local root. -/
theorem eisenstein_root_pow_five {q : ℕ} {x : ZMod q}
    (hx : x ^ 2 + x + 1 = 0) : x ^ 5 = x ^ 2 := by
  have h3 := eisenstein_root_pow_three hx
  calc
    x ^ 5 = x ^ 2 * x ^ 3 := by ring
    _ = x ^ 2 := by rw [h3]; ring

/-- Eisenstein exponent `7` returns to the first local root. -/
theorem eisenstein_root_pow_seven {q : ℕ} {x : ZMod q}
    (hx : x ^ 2 + x + 1 = 0) : x ^ 7 = x := by
  have h3 := eisenstein_root_pow_three hx
  calc
    x ^ 7 = x * (x ^ 3) ^ 2 := by ring
    _ = x := by rw [h3]; ring

/-- Eisenstein exponent `11` selects the second local root. -/
theorem eisenstein_root_pow_eleven {q : ℕ} {x : ZMod q}
    (hx : x ^ 2 + x + 1 = 0) : x ^ 11 = x ^ 2 := by
  have h3 := eisenstein_root_pow_three hx
  calc
    x ^ 11 = x ^ 2 * (x ^ 3) ^ 3 := by ring
    _ = x ^ 2 := by rw [h3]; ring

/-- T10: every point of the corrected mixed locus has exact global multiplicative order `12`. -/
theorem mixed_locus_order_twelve {p q : ℕ} [Fact p.Prime] [Fact q.Prime]
    (hp3 : 3 < p) (hq3 : 3 < q) (hpq : p ≠ q)
    {r : MixedCarrier p q} (hr : MixedLocus r) : orderOf r = 12 := by
  have hpord : orderOf r.1 = 4 := gaussian_root_order (by omega) hr.1
  have hqord : orderOf r.2 = 3 := eisenstein_root_order hq3 hr.2
  have hp4 : r.1 ^ 4 = 1 := by
    have h := pow_orderOf_eq_one r.1
    rwa [hpord] at h
  have hq3p : r.2 ^ 3 = 1 := by
    have h := pow_orderOf_eq_one r.2
    rwa [hqord] at h
  have h12 : r ^ 12 = 1 := by
    ext
    · change r.1 ^ 12 = 1
      calc
        r.1 ^ 12 = (r.1 ^ 4) ^ 3 := by ring
        _ = 1 := by rw [hp4]; simp
    · change r.2 ^ 12 = 1
      calc
        r.2 ^ 12 = (r.2 ^ 3) ^ 4 := by ring
        _ = 1 := by rw [hq3p]; simp
  rw [orderOf_eq_iff (by norm_num : 0 < 12)]
  refine ⟨h12, ?_⟩
  intro m hm hpos hmone
  have hpone : r.1 ^ m = 1 := by
    have h := congrArg Prod.fst hmone
    simpa using h
  have hqone : r.2 ^ m = 1 := by
    have h := congrArg Prod.snd hmone
    simpa using h
  have h4d : 4 ∣ m := by
    have h := orderOf_dvd_of_pow_eq_one hpone
    simpa [hpord] using h
  have h3d : 3 ∣ m := by
    have h := orderOf_dvd_of_pow_eq_one hqone
    simpa [hqord] using h
  have h12d : 12 ∣ m := by
    have h := (show Nat.Coprime 4 3 by norm_num).mul_dvd_of_dvd_of_dvd h4d h3d
    norm_num at h ⊢
    exact h
  have hle : 12 ≤ m := Nat.le_of_dvd hpos h12d
  omega

/-- The Gaussian equation has only the two roots determined by a chosen root over a prime field. -/
theorem gaussian_root_two_choices {p : ℕ} [Fact p.Prime] {r x : ZMod p}
    (hr : r ^ 2 + 1 = 0) (hx : x ^ 2 + 1 = 0) : x = r ∨ x = -r := by
  have hprod : (x - r) * (x + r) = 0 := by
    calc
      (x - r) * (x + r) = x ^ 2 - r ^ 2 := by ring
      _ = 0 := by
        have hxsq := gaussian_root_sq hx
        have hrsq := gaussian_root_sq hr
        rw [hxsq, hrsq]
        ring
  rcases mul_eq_zero.mp hprod with h | h
  · left
    linear_combination h
  · right
    linear_combination h

/-- The Eisenstein equation has only the chosen root and its square over a prime field. -/
theorem eisenstein_root_two_choices {q : ℕ} [Fact q.Prime] {r x : ZMod q}
    (hr : r ^ 2 + r + 1 = 0) (hx : x ^ 2 + x + 1 = 0) : x = r ∨ x = r ^ 2 := by
  have hprod : (x - r) * (x + r + 1) = 0 := by
    calc
      (x - r) * (x + r + 1) =
          (x ^ 2 + x + 1) - (r ^ 2 + r + 1) := by ring
      _ = 0 := by rw [hx, hr]; ring
  rcases mul_eq_zero.mp hprod with h | h
  · left
    linear_combination h
  · right
    linear_combination h - hr

/-- T10: the corrected mixed locus is exactly the four CRT-oriented orbit points
`r, r^5, r^7, r^11`; this theorem says nothing about the full fused-root universe. -/
theorem mixed_locus_four_orbit {p q : ℕ} [Fact p.Prime] [Fact q.Prime]
    {r x : MixedCarrier p q} (hr : MixedLocus r) (hx : MixedLocus x) :
    x = r ∨ x = r ^ 5 ∨ x = r ^ 7 ∨ x = r ^ 11 := by
  rcases gaussian_root_two_choices hr.1 hx.1 with hp | hp <;>
    rcases eisenstein_root_two_choices hr.2 hx.2 with hq | hq
  · exact Or.inl (Prod.ext hp hq)
  · right; left
    apply Prod.ext
    · change x.1 = r.1 ^ 5
      exact hp.trans (gaussian_root_pow_five hr.1).symm
    · change x.2 = r.2 ^ 5
      exact hq.trans (eisenstein_root_pow_five hr.2).symm
  · right; right; left
    apply Prod.ext
    · change x.1 = r.1 ^ 7
      exact hp.trans (gaussian_root_pow_seven hr.1).symm
    · change x.2 = r.2 ^ 7
      exact hq.trans (eisenstein_root_pow_seven hr.2).symm
  · right; right; right
    apply Prod.ext
    · change x.1 = r.1 ^ 11
      exact hp.trans (gaussian_root_pow_eleven hr.1).symm
    · change x.2 = r.2 ^ 11
      exact hq.trans (eisenstein_root_pow_eleven hr.2).symm

/-- T10 inversion guard: inside the four-point corrected orbit, the only coefficient-inversion
pair with the chosen `r` is `r` paired with `r^11`. -/
theorem mixed_orbit_inverse_only_eleven {p q : ℕ} [Fact p.Prime] [Fact q.Prime]
    (hp3 : 3 < p) (hq3 : 3 < q) (hpq : p ≠ q)
    {r x : MixedCarrier p q} (hr : MixedLocus r)
    (hx : x = r ∨ x = r ^ 5 ∨ x = r ^ 7 ∨ x = r ^ 11) :
    r * x = 1 ↔ x = r ^ 11 := by
  have hord : orderOf r = 12 := mixed_locus_order_twelve hp3 hq3 hpq hr
  constructor
  · intro hmul
    rcases hx with rfl | rfl | rfl | rfl
    · exfalso
      have hp : r ^ 2 = 1 := by simpa [pow_succ, mul_comm] using hmul
      have hd := orderOf_dvd_of_pow_eq_one hp
      rw [hord] at hd
      norm_num at hd
    · exfalso
      have hp : r ^ 6 = 1 := by simpa [pow_succ, mul_comm] using hmul
      have hd := orderOf_dvd_of_pow_eq_one hp
      rw [hord] at hd
      norm_num at hd
    · exfalso
      have hp : r ^ 8 = 1 := by simpa [pow_succ, mul_comm] using hmul
      have hd := orderOf_dvd_of_pow_eq_one hp
      rw [hord] at hd
      norm_num at hd
    · rfl
  · rintro rfl
    have hp := pow_orderOf_eq_one r
    rw [hord] at hp
    simpa [pow_succ, mul_comm] using hp

/-- T11 local sixth-power signature on the Gaussian channel. -/
theorem gaussian_root_pow_six {p : ℕ} {x : ZMod p} (hx : x ^ 2 + 1 = 0) : x ^ 6 = -1 := by
  have hsq := gaussian_root_sq hx
  calc
    x ^ 6 = (x ^ 2) ^ 3 := by ring
    _ = -1 := by rw [hsq]; ring

/-- T11 local sixth-power signature on the Eisenstein channel. -/
theorem eisenstein_root_pow_six {q : ℕ} {x : ZMod q}
    (hx : x ^ 2 + x + 1 = 0) : x ^ 6 = 1 := by
  have h3 := eisenstein_root_pow_three hx
  calc
    x ^ 6 = (x ^ 3) ^ 2 := by ring
    _ = 1 := by rw [h3]; ring

/-- CRT idempotent orientation used by the corrected mixed locus: `0` on `p`, `1` on `q`. -/
def mixedChannelIdempotent (p q : ℕ) : MixedCarrier p q := (0, 1)

/-- T11 cross-link `x^6 = 2e - 1`, proved directly from the two local equations and independent
of any orbit-completeness statement. -/
theorem mixed_sixth_eq_two_idempotent_sub_one {p q : ℕ} {x : MixedCarrier p q}
    (hx : MixedLocus x) :
    x ^ 6 = 2 * mixedChannelIdempotent p q - 1 := by
  ext
  · change x.1 ^ 6 = 2 * (0 : ZMod p) - 1
    rw [gaussian_root_pow_six hx.1]
    ring
  · change x.2 ^ 6 = 2 * (1 : ZMod q) - 1
    rw [eisenstein_root_pow_six hx.2]
    ring

/-- H=91 corrected oriented locus: Gaussian/N is modulo `13`, Eisenstein/C modulo `7`. -/
def orientedRoots91 : Finset ℕ :=
  (Finset.range 91).filter fun x =>
    ((x : ZMod 13) ^ 2 + 1 = 0) ∧
      ((x : ZMod 7) ^ 2 + (x : ZMod 7) + 1 = 0)

/-- H=91 full fused-root universe, deliberately separate from the oriented mixed locus. -/
def fusedRoots91 : Finset ℕ :=
  (Finset.range 91).filter fun x =>
    (((x : ZMod 91) ^ 2 + 1) *
      ((x : ZMod 91) ^ 2 + (x : ZMod 91) + 1) = 0)

/-- Required T10 regression guard: exactly four channel-oriented roots at `H=91`. -/
theorem orientedRoots91_exact : orientedRoots91 = {18, 44, 60, 86} := by
  native_decide

/-- Required T10 regression guard: the full fused polynomial has eight roots at `H=91`. -/
theorem fusedRoots91_exact : fusedRoots91 = {9, 16, 18, 44, 60, 74, 81, 86} := by
  native_decide

/-- Required T10 integrity guard: the corrected mixed locus is not silently identified with the
full fused-root universe. -/
theorem orientedRoots91_ne_fusedRoots91 : orientedRoots91 ≠ fusedRoots91 := by
  native_decide

end EnterpriseMath.PrimeFusion
