import Mathlib.Data.Int.GCD
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Strict order of nonnegative fractions by cross multiplication. Denominators are
kept explicit so R007's Farey bridge can remain entirely integral. -/
def fracLt (a b c d : ℕ) : Prop :=
  a * d < c * b

/-- The mediant lies strictly between two strictly ordered fractions with positive
denominators. -/
theorem fracLt_mediant {a b c d : ℕ} (hb : 0 < b) (hd : 0 < d)
    (h : fracLt a b c d) :
    fracLt a b (a + c) (b + d) ∧
      fracLt (a + c) (b + d) c d := by
  unfold fracLt at h ⊢
  constructor <;> nlinarith

/-- Minimal determinant data needed from the two Farey parents of a reduced interior
fraction `m/N`. The two denominator pieces sum to `N` and the two numerator pieces
sum to `m`; each parent has determinant one from the center fraction. -/
structure FareyParentData (m N : ℕ) where
  a : ℕ
  b : ℕ
  c : ℕ
  d : ℕ
  b_pos : 0 < b
  b_lt : b < N
  d_pos : 0 < d
  d_lt : d < N
  denom_sum : b + d = N
  numer_sum : a + c = m
  left_det : a * N + 1 = m * b
  right_det : m * d + 1 = c * N

/-- Construct the two determinant-one parents of every reduced proper fraction
`0 < m/N < 1` using a modular inverse of `m` modulo `N`.

This is the exact local substitute for importing a full Farey-sequence library. -/
theorem exists_fareyParentData {m N : ℕ}
    (hm : 0 < m) (hmN : m < N) (hcop : m.Coprime N) :
    Nonempty (FareyParentData m N) := by
  have hN1 : 1 < N := by omega
  obtain ⟨b, hbN, hmod⟩ := Nat.exists_mul_mod_eq_one_of_coprime hcop hN1
  have hb : 0 < b := by
    by_contra h
    have hb0 : b = 0 := Nat.eq_zero_of_not_pos h
    simp [hb0] at hmod
  let a := (m * b) / N
  let d := N - b
  let c := m - a
  have hN : 0 < N := by omega
  have hdecomp : m * b = 1 + N * a := by
    have h := (Nat.mod_add_div (m * b) N).symm
    rw [hmod] at h
    simpa [a] using h
  have hmb_lt_mN : m * b < m * N := (Nat.mul_lt_mul_left hm).2 hbN
  have haN_lt_mb : a * N < m * b := by
    rw [hdecomp]
    simp [Nat.mul_comm]
  have haN_lt_mN : a * N < m * N := lt_trans haN_lt_mb hmb_lt_mN
  have ha_lt_m : a < m := (Nat.mul_lt_mul_right hN).1 haN_lt_mN
  have hd : 0 < d := by
    dsimp [d]
    omega
  have hdN : d < N := by
    dsimp [d]
    omega
  have hc : 0 < c := by
    dsimp [c]
    omega
  have hleft : a * N + 1 = m * b := by
    rw [hdecomp]
    omega
  have hmd : m * d = m * N - m * b := by
    dsimp [d]
    exact Nat.mul_sub_left_distrib m N b
  have hcN : c * N = m * N - a * N := by
    dsimp [c]
    exact Nat.sub_mul m a N
  have hright : m * d + 1 = c * N := by
    rw [hmd, hcN, hleft]
    have hmb_le_mN : m * b ≤ m * N := Nat.le_of_lt hmb_lt_mN
    have haN_le_mN : a * N ≤ m * N := Nat.le_of_lt haN_lt_mN
    omega
  refine ⟨{
    a := a
    b := b
    c := c
    d := d
    b_pos := hb
    b_lt := hbN
    d_pos := hd
    d_lt := hdN
    denom_sum := by dsimp [d]; omega
    numer_sum := by dsimp [c]; omega
    left_det := hleft
    right_det := hright
  }⟩

/-- The constructed parents are strictly on the left and right of the center fraction. -/
theorem FareyParentData.parents_straddle {m N : ℕ}
    (P : FareyParentData m N) :
    fracLt P.a P.b m N ∧ fracLt m N P.c P.d := by
  unfold fracLt
  constructor
  · nlinarith [P.left_det]
  · nlinarith [P.right_det]

/-- The center fraction is exactly the mediant of its two determinant-one parents at
the level of numerator/denominator sums. -/
theorem FareyParentData.center_is_mediant {m N : ℕ}
    (P : FareyParentData m N) :
    P.a + P.c = m ∧ P.b + P.d = N :=
  ⟨P.numer_sum, P.denom_sum⟩

/-- Both parent denominators are strictly smaller than the center denominator. -/
theorem FareyParentData.denominators_descend {m N : ℕ}
    (P : FareyParentData m N) : P.b < N ∧ P.d < N :=
  ⟨P.b_lt, P.d_lt⟩

end EnterpriseMath.Scale
