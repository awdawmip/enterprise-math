import EnterpriseMath.PrecisionPi.EqualOccupancyStirling
import EnterpriseMath.PrecisionPi.StirlingLimit
import EnterpriseMath.PrecisionPi.TetrahedralCore

namespace EnterpriseMath.PrecisionPi

open Filter Topology

/-- The real tetrahedral precision approximant from four-state versus six-state
finite equal-occupancy probabilities. -/
noncomputable def tetrahedralPrecision (n : ℕ) : ℝ :=
  Real.sqrt (3 / 8 : ℝ) * equalOccupancyReal 4 n /
    ((n : ℝ) * equalOccupancyReal 6 n)

/-- The square-root normalization in the `4 -> 6` balance ratio cancels
exactly against the two extra Stirling fluctuation dimensions. -/
theorem tetrahedral_sqrt_scale (x : ℝ) (hx : 0 < x) :
    Real.sqrt (3 / 8 : ℝ) *
        (Real.sqrt (8 * x) / Real.sqrt (2 * x) ^ 4) /
        (x * (Real.sqrt (12 * x) / Real.sqrt (2 * x) ^ 6)) = 1 := by
  have h2 : (Real.sqrt (2 * x)) ^ 2 = 2 * x := by
    rw [Real.sq_sqrt]
    positivity
  have h8 : (Real.sqrt (8 * x)) ^ 2 = 8 * x := by
    rw [Real.sq_sqrt]
    positivity
  have h12 : (Real.sqrt (12 * x)) ^ 2 = 12 * x := by
    rw [Real.sq_sqrt]
    positivity
  have h38 : (Real.sqrt (3 / 8 : ℝ)) ^ 2 = 3 / 8 := by
    rw [Real.sq_sqrt]
    norm_num
  have hroot :
      2 * Real.sqrt (3 / 8 : ℝ) * Real.sqrt (8 * x) =
        Real.sqrt (12 * x) := by
    apply (sq_eq_sq₀ (by positivity) (by positivity)).mp
    calc
      (2 * Real.sqrt (3 / 8 : ℝ) * Real.sqrt (8 * x)) ^ 2 =
          4 * (Real.sqrt (3 / 8 : ℝ)) ^ 2 *
            (Real.sqrt (8 * x)) ^ 2 := by ring
      _ = 12 * x := by rw [h38, h8]; ring
      _ = (Real.sqrt (12 * x)) ^ 2 := by rw [h12]
  have hq : Real.sqrt (2 * x) ≠ 0 := by positivity
  have hc : Real.sqrt (12 * x) ≠ 0 := by positivity
  field_simp [hq, hc]
  rw [show (Real.sqrt (2 * x)) ^ 6 =
      (Real.sqrt (2 * x)) ^ 4 * (Real.sqrt (2 * x)) ^ 2 by ring]
  rw [h2, hroot]
  ring

/-- Pointwise identification of the finite multinomial precision approximant
with the Stirling-normalized sequence. -/
theorem tetrahedralPrecision_eq_stirling {n : ℕ} (hn : 0 < n) :
    tetrahedralPrecision n = tetrahedralStirlingPrecision n := by
  rw [tetrahedralPrecision,
    equalOccupancyReal_eq_stirling 4 n (by norm_num) hn,
    equalOccupancyReal_eq_stirling 6 n (by norm_num) hn]
  have hscale := tetrahedral_sqrt_scale (n : ℝ) (by exact_mod_cast hn)
  change
    Real.sqrt (3 / 8 : ℝ) *
          (Stirling.stirlingSeq (4 * n) / Stirling.stirlingSeq n ^ 4 *
            (Real.sqrt (8 * (n : ℝ)) / Real.sqrt (2 * (n : ℝ)) ^ 4)) /
        ((n : ℝ) *
          (Stirling.stirlingSeq (6 * n) / Stirling.stirlingSeq n ^ 6 *
            (Real.sqrt (12 * (n : ℝ)) / Real.sqrt (2 * (n : ℝ)) ^ 6))) =
      Stirling.stirlingSeq (4 * n) * Stirling.stirlingSeq n ^ 2 /
        Stirling.stirlingSeq (6 * n)
  have hSn : Stirling.stirlingSeq n ≠ 0 := by
    unfold Stirling.stirlingSeq
    positivity
  have hS6 : Stirling.stirlingSeq (6 * n) ≠ 0 := by
    unfold Stirling.stirlingSeq
    positivity
  field_simp [hSn, hS6]
  nlinarith [hscale]

/-- The real tetrahedral precision approximants converge to `π`. -/
theorem tendsto_tetrahedralPrecision_pi :
    Tendsto tetrahedralPrecision atTop (𝓝 Real.pi) := by
  refine tendsto_tetrahedralStirlingPrecision_pi.congr' ?_
  filter_upwards [eventually_atTop.2 ⟨1, fun _ h => h⟩] with n hn
  exact tetrahedralPrecision_eq_stirling (by omega)

/-- Every positive-depth tetrahedral precision refinement is strictly smaller. -/
theorem tetrahedralPrecision_succ_lt {n : ℕ} (hn : 0 < n) :
    tetrahedralPrecision (n + 1) < tetrahedralPrecision n := by
  have hcore :
      (tetrahedralCore (n + 1) : ℝ) < (tetrahedralCore n : ℝ) := by
    exact_mod_cast tetrahedralCore_succ_lt hn
  have hscale : 0 < Real.sqrt (3 / 8 : ℝ) := by positivity
  have hcast (j : ℕ) :
      tetrahedralPrecision j = Real.sqrt (3 / 8 : ℝ) * (tetrahedralCore j : ℝ) := by
    rw [tetrahedralPrecision, tetrahedralCore,
      equalOccupancyReal_eq_cast, equalOccupancyReal_eq_cast]
    norm_num
  rw [hcast (n + 1), hcast n]
  exact mul_lt_mul_of_pos_left hcore hscale

/-- The shifted positive-depth precision sequence is strictly antitone. -/
theorem strictAnti_tetrahedralPrecision_shift :
    StrictAnti (fun n : ℕ => tetrahedralPrecision (n + 1)) := by
  apply strictAnti_nat_of_succ_lt
  intro n
  simpa [Nat.add_assoc] using tetrahedralPrecision_succ_lt (Nat.succ_pos n)

/-- Every finite positive-depth tetrahedral precision value lies strictly above
its common continuous completion `π`. -/
theorem pi_lt_tetrahedralPrecision {n : ℕ} (hn : 0 < n) :
    Real.pi < tetrahedralPrecision n := by
  obtain ⟨j, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt hn)
  let f : ℕ → ℝ := fun r => tetrahedralPrecision (r + 1)
  have hanti : StrictAnti f := strictAnti_tetrahedralPrecision_shift
  have hlim : Tendsto f atTop (𝓝 Real.pi) :=
    tendsto_tetrahedralPrecision_pi.comp (tendsto_add_atTop_nat 1)
  have hle : Real.pi ≤ f (j + 1) :=
    hanti.antitone.le_of_tendsto hlim (j + 1)
  exact lt_of_le_of_lt hle (hanti (Nat.lt_succ_self j))

end EnterpriseMath.PrecisionPi
