import EnterpriseMath.PrimeFusion.PointedRecovery

namespace EnterpriseMath.PrimeFusion

/-- F2-L01: every integral idempotent modulo `H` splits `H` into the ordered
`gcd(e,H)` and `gcd(e-1,H)` factors, with product `H` and coprime factors. -/
theorem idempotent_universal_channel_split {H : ℕ} {e : ℤ}
    (hidem : (H : ℤ) ∣ e * (e - 1)) :
    Int.gcd e (H : ℤ) * Int.gcd (e - 1) (H : ℤ) = H ∧
      Nat.Coprime (Int.gcd e (H : ℤ)) (Int.gcd (e - 1) (H : ℤ)) := by
  exact ⟨(idempotent_gcd_partition hidem).2, (idempotent_gcd_partition hidem).1⟩

/-- Channel coprimality forces primitive input; primitivity is therefore derived
rather than added as an independent reconstruction hypothesis. -/
theorem channels_isCoprime_implies_primitive {a b : ℤ}
    (hNC : IsCoprime (N a b) (C a b)) : IsCoprime a b := by
  have hNCgcd : Int.gcd (N a b) (C a b) = 1 :=
    Int.isCoprime_iff_gcd_eq_one.mp hNC
  have hd2 : Int.gcd a b ^ 2 = 1 := by
    rw [← channel_gcd_exact a b]
    exact hNCgcd
  have hd : Int.gcd a b = 1 := by
    nlinarith
  exact Int.isCoprime_iff_gcd_eq_one.mpr hd

/-- Positive cells have the exact T7 orientation `N > C`. -/
theorem positive_cell_channel_orientation {a b : ℤ} (ha : 0 < a) (hb : 0 < b) :
    C a b < N a b := by
  have hab : 0 < a * b := mul_pos ha hb
  simp only [N, C]
  nlinarith

/-- The two diagonal perfect-square conditions are necessary for any channel pair. -/
theorem reconstruction_square_gate_necessary {a b n c : ℤ}
    (hN : N a b = n) (hC : C a b = c) :
    (∃ U : ℤ, U ^ 2 = 3 * n - 2 * c) ∧
      (∃ V : ℤ, V ^ 2 = 2 * c - n) := by
  refine ⟨⟨u a b, ?_⟩, ⟨v a b, ?_⟩⟩
  · simpa [hN, hC] using u_sq_eq_three_N_sub_two_C a b
  · simpa [hN, hC] using v_sq_eq_two_C_sub_N a b

/-- Exact square-gate negative control: if the `U²=3N-2C` square is absent,
no integral cell can realize the proposed ordered channels. -/
theorem no_reconstruction_if_U_not_square {n c : ℤ}
    (hU : ¬ ∃ U : ℤ, U ^ 2 = 3 * n - 2 * c) :
    ¬ ∃ a b : ℤ, N a b = n ∧ C a b = c := by
  rintro ⟨a, b, hN, hC⟩
  exact hU ⟨u a b, by simpa [hN, hC] using u_sq_eq_three_N_sub_two_C a b⟩

/-- Exact orientation negative control: `N ≤ C` cannot reconstruct a positive cell. -/
theorem no_positive_reconstruction_if_not_oriented {n c : ℤ} (hnc : n ≤ c) :
    ¬ ∃ a b : ℤ, 0 < a ∧ 0 < b ∧ N a b = n ∧ C a b = c := by
  rintro ⟨a, b, ha, hb, hN, hC⟩
  have hlt := positive_cell_channel_orientation ha hb
  rw [hN, hC] at hlt
  exact (not_lt_of_ge hnc) hlt

/-- F2-L02: exact positive reconstruction from the oriented ordered channels and
integral diagonal square roots. `Even (U+V)` and `Even (U-V)` are the supplied
parity/integrality gate. The diagonal case `V=0` is allowed; strict interiority
is separated below. -/
theorem reconstruct_positive_cell_of_diagonal_roots
    {n c U V : ℤ}
    (hnc : c < n)
    (hU : U ^ 2 = 3 * n - 2 * c)
    (hV : V ^ 2 = 2 * c - n)
    (hUpos : 0 < U)
    (hVnonneg : 0 ≤ V)
    (hsum : Even (U + V))
    (hdiff : Even (U - V)) :
    ∃ a b : ℤ, 0 < a ∧ 0 < b ∧ N a b = n ∧ C a b = c := by
  have hsq : V ^ 2 < U ^ 2 := by
    nlinarith [hU, hV]
  have hVltU : V < U := by
    by_contra hnot
    have hUV : U ≤ V := le_of_not_gt hnot
    have hmul : 0 ≤ (V - U) * (V + U) :=
      mul_nonneg (sub_nonneg.mpr hUV) (add_nonneg hVnonneg (le_of_lt hUpos))
    nlinarith
  rcases hsum with ⟨a, ha⟩
  rcases hdiff with ⟨b, hb⟩
  have hUcoord : u a b = U := by
    simp only [u]
    linarith
  have hVcoord : v a b = V := by
    simp only [v]
    linarith
  have haPos : 0 < a := by
    linarith
  have hbPos : 0 < b := by
    linarith
  have hNdiag := two_mul_N_eq_u_sq_add_v_sq a b
  rw [hUcoord, hVcoord] at hNdiag
  have hNexact : N a b = n := by
    nlinarith [hU, hV, hNdiag]
  have hCdiag := four_mul_C_eq_u_sq_add_three_v_sq a b
  rw [hUcoord, hVcoord] at hCdiag
  have hCexact : C a b = c := by
    nlinarith [hU, hV, hCdiag]
  exact ⟨a, b, haPos, hbPos, hNexact, hCexact⟩

/-- The exact extra T7 gate for strict interiority: on a reconstructed positive
cell, `V>0` is equivalent to choosing the ordering `a>b`; without it `V=0`
permits the positive diagonal. -/
theorem reconstructed_strict_interior_gate {a b : ℤ} (ha : 0 < a) (hb : 0 < b) :
    0 < v a b ↔ b < a := by
  simp [v]

end EnterpriseMath.PrimeFusion
