import Mathlib

namespace EnterpriseMath.PrimeFusion

/-- The Gaussian / native squared-length channel. -/
def N (a b : ℤ) : ℤ := a ^ 2 + b ^ 2

/-- The Eisenstein / triangular-carrier channel. -/
def C (a b : ℤ) : ℤ := a ^ 2 - a * b + b ^ 2

/-- Sum diagonal coordinate. -/
def u (a b : ℤ) : ℤ := a + b

/-- Difference diagonal coordinate. -/
def v (a b : ℤ) : ℤ := a - b

/-- T1: `2N = u² + v²`. -/
theorem two_mul_N_eq_u_sq_add_v_sq (a b : ℤ) :
    2 * N a b = u a b ^ 2 + v a b ^ 2 := by
  simp [N, u, v]
  ring

/-- T1: `4C = u² + 3v²`. -/
theorem four_mul_C_eq_u_sq_add_three_v_sq (a b : ℤ) :
    4 * C a b = u a b ^ 2 + 3 * v a b ^ 2 := by
  simp [C, u, v]
  ring

/-- T1 converse: `u² = 3N - 2C`. -/
theorem u_sq_eq_three_N_sub_two_C (a b : ℤ) :
    u a b ^ 2 = 3 * N a b - 2 * C a b := by
  simp [N, C, u]
  ring

/-- T1 converse: `v² = 2C - N`. -/
theorem v_sq_eq_two_C_sub_N (a b : ℤ) :
    v a b ^ 2 = 2 * C a b - N a b := by
  simp [N, C, v]
  ring

/-- The exact T1 square pair, exported for later reconstruction work. -/
theorem diagonal_square_pair (a b : ℤ) :
    u a b ^ 2 = 3 * N a b - 2 * C a b ∧
      v a b ^ 2 = 2 * C a b - N a b :=
  ⟨u_sq_eq_three_N_sub_two_C a b, v_sq_eq_two_C_sub_N a b⟩

/-- A primitive pair makes the `N` channel coprime to the cross term `ab`. -/
theorem primitive_N_mul_isCoprime {a b : ℤ} (hab : IsCoprime a b) :
    IsCoprime (N a b) (a * b) := by
  have hab2 : IsCoprime a (b ^ 2) := hab.pow_right
  have haN : IsCoprime a (N a b) := by
    rcases hab2 with ⟨s, t, hst⟩
    refine ⟨s - t * a, t, ?_⟩
    dsimp [N]
    linear_combination hst
  have hba2 : IsCoprime b (a ^ 2) := hab.symm.pow_right
  have hbN : IsCoprime b (N a b) := by
    rcases hba2 with ⟨s, t, hst⟩
    refine ⟨s - t * b, t, ?_⟩
    dsimp [N]
    linear_combination hst
  exact haN.symm.mul_right hbN.symm

/-- Primitive input prevents cross-channel common divisors. -/
theorem primitive_channels_isCoprime {a b : ℤ} (hab : IsCoprime a b) :
    IsCoprime (N a b) (C a b) := by
  rcases primitive_N_mul_isCoprime hab with ⟨s, t, hst⟩
  refine ⟨s + t, -t, ?_⟩
  dsimp [N, C] at hst ⊢
  linear_combination hst

/-- T2 primitive corollary, stated with the same integer gcd used by the source theorem. -/
theorem primitive_channel_gcd {a b : ℤ} (hab : Int.gcd a b = 1) :
    Int.gcd (N a b) (C a b) = 1 :=
  Int.isCoprime_iff_gcd_eq_one.mp
    (primitive_channels_isCoprime (Int.isCoprime_iff_gcd_eq_one.mpr hab))

/-- T2: exact common-divisor law over all integer pairs. -/
theorem channel_gcd_exact (a b : ℤ) :
    Int.gcd (N a b) (C a b) = Int.gcd a b ^ 2 := by
  by_cases hd : Int.gcd a b = 0
  · have habs : Nat.gcd a.natAbs b.natAbs = 0 := by
      simpa [Int.gcd_def] using hd
    have habzero := Nat.gcd_eq_zero_iff.mp habs
    have ha0 : a = 0 := Int.natAbs_eq_zero.mp habzero.1
    have hb0 : b = 0 := Int.natAbs_eq_zero.mp habzero.2
    subst a
    subst b
    simp [N, C]
  · have hdpos : 0 < Int.gcd a b := Nat.pos_of_ne_zero hd
    obtain ⟨a', b', hprim, ha, hb⟩ := Int.exists_gcd_one hdpos
    have hprimNC : Int.gcd (N a' b') (C a' b') = 1 := primitive_channel_gcd hprim
    have hscaleN :
        N a b = ((Int.gcd a b : ℤ) ^ 2) * N a' b' := by
      conv_lhs => rw [ha, hb]
      simp [N]
      ring
    have hscaleC :
        C a b = ((Int.gcd a b : ℤ) ^ 2) * C a' b' := by
      conv_lhs => rw [ha, hb]
      simp [C]
      ring
    have hbez :
        (1 : ℤ) =
          N a' b' * Int.gcdA (N a' b') (C a' b') +
            C a' b' * Int.gcdB (N a' b') (C a' b') := by
      simpa [hprimNC] using Int.gcd_eq_gcd_ab (N a' b') (C a' b')
    have hgreat :
        ((Int.gcd a b : ℤ) ^ 2) = (Int.gcd (N a b) (C a b) : ℤ) := by
      apply Int.gcd_greatest
      · positivity
      · exact ⟨N a' b', hscaleN⟩
      · exact ⟨C a' b', hscaleC⟩
      · intro e heN heC
        have hcombo :
            ((Int.gcd a b : ℤ) ^ 2) =
              N a b * Int.gcdA (N a' b') (C a' b') +
                C a b * Int.gcdB (N a' b') (C a' b') := by
          calc
            ((Int.gcd a b : ℤ) ^ 2) = ((Int.gcd a b : ℤ) ^ 2) * 1 := by ring
            _ = ((Int.gcd a b : ℤ) ^ 2) *
                (N a' b' * Int.gcdA (N a' b') (C a' b') +
                  C a' b' * Int.gcdB (N a' b') (C a' b')) := by rw [hbez]
            _ = N a b * Int.gcdA (N a' b') (C a' b') +
                C a b * Int.gcdB (N a' b') (C a' b') := by
              rw [hscaleN, hscaleC]
              ring
        rw [hcombo]
        exact dvd_add (dvd_mul_of_dvd_left heN _) (dvd_mul_of_dvd_left heC _)
    exact_mod_cast hgreat.symm

end EnterpriseMath.PrimeFusion
