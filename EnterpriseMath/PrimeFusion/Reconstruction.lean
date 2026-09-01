import EnterpriseMath.PrimeFusion.PointedRecovery

namespace EnterpriseMath.PrimeFusion

/-- F2-L01 / T7: the two gcd factors attached to an integral representative of an
idempotent modulo `H` are automatically coprime and multiply to `H`.

This is the source-facing interface for the existing F1 theorem
`idempotent_gcd_partition`; no prime-power splitting is reproved here. -/
theorem idempotent_channel_split {H : ℕ} {e : ℤ}
    (hidem : (H : ℤ) ∣ e * (e - 1)) :
    Int.gcd e (H : ℤ) * Int.gcd (e - 1) (H : ℤ) = H ∧
      Nat.Coprime (Int.gcd e (H : ℤ)) (Int.gcd (e - 1) (H : ℤ)) := by
  rcases idempotent_gcd_partition hidem with ⟨hcop, hmul⟩
  exact ⟨hmul, hcop⟩

/-- F2-L02 / T7 exact reconstruction gate in the integer channel types used by F1.

`su` and `sv` are the chosen nonnegative square roots of
`3*n-2*c` and `2*c-n`. The two divisibility hypotheses are exactly the parity /
integrality gate for `(su+sv)/2` and `(su-sv)/2`. The orientation `c<n`, together
with nonnegative roots, forces `sv<su`, so the reconstructed coordinates are
positive. -/
theorem reconstruct_positive_channels
    {n c su sv : ℤ}
    (horient : c < n)
    (hsu0 : 0 ≤ su)
    (hsv0 : 0 ≤ sv)
    (hsu : su ^ 2 = 3 * n - 2 * c)
    (hsv : sv ^ 2 = 2 * c - n)
    (hparPlus : (2 : ℤ) ∣ su + sv)
    (hparMinus : (2 : ℤ) ∣ su - sv) :
    ∃ a b : ℤ,
      0 < a ∧ 0 < b ∧
      N a b = n ∧ C a b = c ∧
      u a b = su ∧ v a b = sv := by
  have hsvlt : sv < su := by
    nlinarith [hsu, hsv]
  rcases hparPlus with ⟨a, ha⟩
  rcases hparMinus with ⟨b, hb⟩
  have hua : u a b = su := by
    simp only [u]
    linarith
  have hva : v a b = sv := by
    simp only [v]
    linarith
  have hapos : 0 < a := by
    nlinarith [ha, hsvlt, hsv0]
  have hbpos : 0 < b := by
    nlinarith [hb, hsvlt]
  have hNdiag := two_mul_N_eq_u_sq_add_v_sq a b
  have hCdiag := four_mul_C_eq_u_sq_add_three_v_sq a b
  rw [hua, hva] at hNdiag hCdiag
  have hN : N a b = n := by
    nlinarith [hNdiag, hsu, hsv]
  have hC : C a b = c := by
    nlinarith [hCdiag, hsu, hsv]
  exact ⟨a, b, hapos, hbpos, hN, hC, hua, hva⟩

/-- Coprime reconstructed channels force primitive coordinates; primitivity is a
consequence, not an extra reconstruction hypothesis. -/
theorem primitive_of_reconstructed_coprime_channels
    {a b n c : ℤ}
    (hN : N a b = n)
    (hC : C a b = c)
    (hnc : IsCoprime n c) : IsCoprime a b := by
  have hgc : Int.gcd (N a b) (C a b) = 1 := by
    rw [hN, hC]
    exact Int.isCoprime_iff_gcd_eq_one.mp hnc
  have hd2 : Int.gcd a b ^ 2 = 1 := by
    rw [← channel_gcd_exact a b]
    exact hgc
  have hd : Int.gcd a b = 1 := by
    nlinarith [hd2]
  exact Int.isCoprime_iff_gcd_eq_one.mpr hd

/-- F2-L02 combined source-facing reconstruction theorem: the exact square/parity
and orientation gate reconstructs positive coordinates, and coprime channel data
then gives primitivity automatically. -/
theorem reconstruct_positive_primitive_channels
    {n c su sv : ℤ}
    (horient : c < n)
    (hsu0 : 0 ≤ su)
    (hsv0 : 0 ≤ sv)
    (hsu : su ^ 2 = 3 * n - 2 * c)
    (hsv : sv ^ 2 = 2 * c - n)
    (hparPlus : (2 : ℤ) ∣ su + sv)
    (hparMinus : (2 : ℤ) ∣ su - sv)
    (hnc : IsCoprime n c) :
    ∃ a b : ℤ,
      0 < a ∧ 0 < b ∧ IsCoprime a b ∧
      N a b = n ∧ C a b = c ∧
      u a b = su ∧ v a b = sv := by
  rcases reconstruct_positive_channels horient hsu0 hsv0 hsu hsv hparPlus hparMinus with
    ⟨a, b, ha, hb, hN, hC, hu, hv⟩
  have hab : IsCoprime a b :=
    primitive_of_reconstructed_coprime_channels hN hC hnc
  exact ⟨a, b, ha, hb, hab, hN, hC, hu, hv⟩

/-- The strict-interiority residue is exactly the extra `V>0`, equivalently
`n<2*c`, once `sv` is the chosen nonnegative square root of `V`. -/
theorem strict_interior_gate_iff
    {n c sv : ℤ}
    (hsv0 : 0 ≤ sv)
    (hsv : sv ^ 2 = 2 * c - n) :
    0 < sv ↔ n < 2 * c := by
  constructor
  · intro hpos
    nlinarith [hsv]
  · intro hlt
    by_contra hnot
    have hz : sv = 0 := by
      exact le_antisymm (le_of_not_gt hnot) hsv0
    subst sv
    nlinarith [hsv]

/-- Exact square-gate negative control: any actual cell necessarily produces the
T7 pair of squares. -/
theorem reconstruction_square_gate_necessary (a b : ℤ) :
    u a b ^ 2 = 3 * N a b - 2 * C a b ∧
      v a b ^ 2 = 2 * C a b - N a b :=
  diagonal_square_pair a b

/-- Exact orientation negative control: positive coordinates force `N>C`; dropping
this orientation admits data that cannot represent a positive ordered cell. -/
theorem positive_channel_orientation_necessary
    {a b : ℤ} (ha : 0 < a) (hb : 0 < b) :
    C a b < N a b := by
  simp only [N, C]
  have hab : 0 < a * b := mul_pos ha hb
  nlinarith

end EnterpriseMath.PrimeFusion
