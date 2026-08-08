import EnterpriseMath.Arithmetic.IntegerRoot

namespace EnterpriseMath.CollapseCommutation

open EnterpriseMath.IntegerRoot

/-- Perfect-power collapse is monotone for every positive exponent. -/
theorem collapse_mono {p : ℕ} (hp : p ≠ 0) : Monotone (collapse p) := by
  change Monotone (fun x : ℕ => root p x ^ p)
  exact (galoisConnection_pow_root hp).monotone_l_comp_u

/-- If `p ∣ q`, collapsing first to `q`-th powers and then to `p`-th powers changes nothing. -/
theorem collapse_left_absorbs_of_dvd {p q : ℕ} (hp : p ≠ 0) (hpq : p ∣ q) (n : ℕ) :
    collapse p (collapse q n) = collapse q n := by
  rcases hpq with ⟨r, rfl⟩
  apply (collapse_eq_self_iff hp (collapse (p * r) n)).2
  refine ⟨root (p * r) n ^ r, ?_⟩
  unfold collapse
  calc
    (root (p * r) n ^ r) ^ p = root (p * r) n ^ (r * p) :=
      (pow_mul (root (p * r) n) r p).symm
    _ = root (p * r) n ^ (p * r) := by rw [Nat.mul_comm r p]

/-- If `p ∣ q`, the `q`-collapse also absorbs a preceding `p`-collapse. -/
theorem collapse_right_absorbs_of_dvd {p q : ℕ} (hp : p ≠ 0) (hq : q ≠ 0)
    (hpq : p ∣ q) (n : ℕ) : collapse q (collapse p n) = collapse q n := by
  have hq_le_hp : collapse q n ≤ collapse p n := by
    calc
      collapse q n = collapse p (collapse q n) := (collapse_left_absorbs_of_dvd hp hpq n).symm
      _ ≤ collapse p n := collapse_mono hp (collapse_le hq n)
  apply le_antisymm
  · exact collapse_mono hq (collapse_le hp n)
  · have h := collapse_mono hq hq_le_hp
    simpa only [collapse_idempotent hq n] using h

/-- Comparable positive exponents give commuting collapse operators, with exact absorption. -/
theorem collapse_commute_of_dvd {p q : ℕ} (hp : p ≠ 0) (hq : q ≠ 0) (hpq : p ∣ q) (n : ℕ) :
    collapse p (collapse q n) = collapse q (collapse p n) := by
  rw [collapse_left_absorbs_of_dvd hp hpq n, collapse_right_absorbs_of_dvd hp hq hpq n]

/-- Symmetric divisibility orientation. -/
theorem collapse_commute_of_dvd_or_dvd {p q : ℕ} (hp : p ≠ 0) (hq : q ≠ 0)
    (h : p ∣ q ∨ q ∣ p) (n : ℕ) : collapse p (collapse q n) = collapse q (collapse p n) := by
  rcases h with hpq | hqp
  · exact collapse_commute_of_dvd hp hq hpq n
  · exact (collapse_commute_of_dvd hq hp hqp n).symm

end EnterpriseMath.CollapseCommutation
