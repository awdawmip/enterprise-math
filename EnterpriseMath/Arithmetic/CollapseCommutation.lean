import Mathlib.Data.Nat.Factorization.PrimePow
import Mathlib.Tactic
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

/-- A power of two cannot be a perfect `p`-th power unless `p` divides its exponent. -/
theorem not_exists_pow_eq_two_pow_of_not_dvd {p q : ℕ} (hp : p ≠ 0) (hpdvd : ¬ p ∣ q) :
    ¬ ∃ a : ℕ, a ^ p = 2 ^ q := by
  rintro ⟨a, ha⟩
  apply hpdvd
  exact Nat.exponent_dvd_of_prime_pow_eq_pow Nat.prime_two ha.symm

/-- P003-T02: for `1 ≤ p < q` with `p ∤ q`, the state `2^q` witnesses noncommutation. -/
theorem collapse_noncommute_two_pow_witness {p q : ℕ}
    (hp : 1 ≤ p) (hpq : p < q) (hpdvd : ¬ p ∣ q) :
    collapse p (collapse q (2 ^ q)) ≠ collapse q (collapse p (2 ^ q)) := by
  have hp0 : p ≠ 0 := by omega
  have hq0 : q ≠ 0 := by omega
  have hqFixed : collapse q (2 ^ q) = 2 ^ q :=
    (collapse_eq_self_iff hq0 (2 ^ q)).2 ⟨2, rfl⟩
  have hpNotFixed : collapse p (2 ^ q) ≠ 2 ^ q := by
    intro hfix
    have hex : ∃ a : ℕ, a ^ p = 2 ^ q :=
      (collapse_eq_self_iff hp0 (2 ^ q)).1 hfix
    exact not_exists_pow_eq_two_pow_of_not_dvd hp0 hpdvd hex
  have hpCollapseLt : collapse p (2 ^ q) < 2 ^ q :=
    lt_of_le_of_ne (collapse_le hp0 (2 ^ q)) hpNotFixed
  have hpowLe : 2 ^ p ≤ 2 ^ q :=
    Nat.pow_le_pow_right (by decide) hpq.le
  have hrootTwo : 2 ≤ root p (2 ^ q) :=
    ((galoisConnection_pow_root hp0) 2 (2 ^ q)).mp hpowLe
  have htwoPowLeCollapse : 2 ^ p ≤ collapse p (2 ^ q) := by
    change 2 ^ p ≤ root p (2 ^ q) ^ p
    exact Nat.pow_le_pow_left hrootTwo p
  have htwoLeTwoPow : 2 ≤ 2 ^ p := by
    have h : (2 : ℕ) ^ 1 ≤ 2 ^ p := Nat.pow_le_pow_right (by decide) hp
    simpa using h
  have honeLtCollapse : 1 < collapse p (2 ^ q) := by omega
  have hqAfterP : collapse q (collapse p (2 ^ q)) = 1 := by
    have h := (collapse_eq_pow_iff
      (p := q) (n := collapse p (2 ^ q)) (k := 1) hq0).2
    refine h ⟨?_, ?_⟩
    · simp
      omega
    · simpa using hpCollapseLt
  rw [hqFixed, hqAfterP]
  exact ne_of_gt honeLtCollapse

/-- P003-T03: global commutation is equivalent to comparability in the divisibility order. -/
theorem collapse_commute_iff_dvd_or_dvd {p q : ℕ} (hp : 1 ≤ p) (hq : 1 ≤ q) :
    (∀ n : ℕ, collapse p (collapse q n) = collapse q (collapse p n)) ↔
      p ∣ q ∨ q ∣ p := by
  have hp0 : p ≠ 0 := by omega
  have hq0 : q ≠ 0 := by omega
  constructor
  · intro hcomm
    by_cases hpq : p ∣ q
    · exact Or.inl hpq
    by_cases hqp : q ∣ p
    · exact Or.inr hqp
    have hpne : p ≠ q := by
      intro hpqe
      apply hpq
      rw [hpqe]
    rcases lt_or_gt_of_ne hpne with hp_lt_q | hq_lt_p
    · exact False.elim ((collapse_noncommute_two_pow_witness hp hp_lt_q hpq)
        (hcomm (2 ^ q)))
    · exact False.elim ((collapse_noncommute_two_pow_witness hq hq_lt_p hqp)
        (hcomm (2 ^ p)).symm)
  · intro hcomp n
    exact collapse_commute_of_dvd_or_dvd hp0 hq0 hcomp n

end EnterpriseMath.CollapseCommutation
