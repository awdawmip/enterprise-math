import EnterpriseMath.Precision.N58RatioBound

open Filter
open scoped Topology

namespace EnterpriseMath.PrecisionPi.SharpPositiveTail

/-- Consecutive-term ratio for parameters (1/2, s, 1-s) and weight A+B*n. -/
def step (s x A B : ℝ) (n : ℕ) : ℝ :=
  let y : ℝ := n
  x * ((y + 1 / 2) / (y + 1)) * ((y + s) / (y + 1)) *
    ((y + (1 - s)) / (y + 1)) * ((A + B * (y + 1)) / (A + B * y))

theorem step_pos {s x A B : ℝ} (hs : 0 < s) (hs' : s < 1) (hx : 0 < x)
    (hA : 0 < A) (hB : 0 ≤ B) (n : ℕ) : 0 < step s x A B n := by
  have h : 0 < 1 - s := sub_pos.mpr hs'
  unfold step
  positivity

theorem step_lt_argument {s x A B : ℝ} (hs : 0 < s) (hs' : s < 1)
    (hx : 0 < x) (hA : 0 < A) (hB : 0 ≤ B) {n : ℕ} (hn : 1 ≤ n) :
    step s x A B n < x := by
  let y : ℝ := n
  have hy1 : 1 ≤ y := by exact_mod_cast hn
  have hy : 0 < y := by linarith
  have hden : 0 < A + B * y := by positivity
  have hspos : 0 < 1 - s := sub_pos.mpr hs'
  have hlin : (A + B * (y + 1)) / (A + B * y) < (y + 1) / y := by
    apply (div_lt_div_iff₀ hden hy).2
    nlinarith
  have hp : (y + s) * (y + (1 - s)) ≤ (y + 1 / 2) ^ 2 := by
    nlinarith [sq_nonneg (s - 1 / 2)]
  have hcore : (y + 1 / 2) ^ 3 < y * (y + 1) ^ 2 := by
    nlinarith [sq_nonneg y]
  have hproduct : (y + 1 / 2) * (y + s) * (y + (1 - s)) <
      y * (y + 1) ^ 2 := by
    calc
      _ = (y + 1 / 2) * ((y + s) * (y + (1 - s))) := mul_assoc _ _ _
      _ ≤ (y + 1 / 2) * (y + 1 / 2)^2 :=
        mul_le_mul_of_nonneg_left hp (by positivity)
      _ = (y + 1 / 2)^3 := by ring
      _ < _ := hcore
  let F := (y + 1 / 2) / (y + 1) * ((y + s) / (y + 1)) * ((y + (1 - s)) / (y + 1))
  have hF : 0 < F := by dsimp [F]; positivity
  have hsmall : F * ((y + 1) / y) < 1 := by
    have hy' : 0 < y + 1 := by positivity
    have hid : F * ((y + 1) / y) =
        ((y + 1 / 2) * (y + s) * (y + (1-s))) / (y * (y+1)^2) := by
      dsimp [F]
      field_simp [hy.ne', hy'.ne']
      <;> ring
    rw [hid]
    apply (div_lt_iff₀ (by positivity : 0 < y*(y+1)^2)).2
    simpa only [one_mul] using hproduct
  calc
    step s x A B n = x * (F * ((A + B * (y + 1)) / (A + B * y))) := by
      dsimp [step, F, y]
      ring
    _ < x * 1 := mul_lt_mul_of_pos_left
      ((mul_lt_mul_of_pos_left hlin hF).trans hsmall) hx
    _ = x := mul_one x

/-- Adding fixed shifts to numerator and denominator preserves their asymptotic ratio. -/
private theorem shifted_ratio_tendsto (a b : ℝ) (hb : 0 ≤ b) :
    Tendsto (fun n : ℕ => ((n : ℝ) + a) / (n + b)) atTop (𝓝 1) := by
  have hh := ((tendsto_const_nhds (x := (1 : ℝ))).add
    (tendsto_const_div_atTop_nhds_zero_nat a)).mul (tendsto_natCast_div_add_atTop b)
  simp only [add_zero, one_mul] at hh
  apply hh.congr'
  filter_upwards [eventually_ge_atTop (1 : ℕ)] with n hn
  have hn' : (0 : ℝ) < n := by exact_mod_cast (show 0 < n by omega)
  have hb' : 0 < (n : ℝ) + b := by linarith
  dsimp
  field_simp [hn'.ne', hb'.ne']
  <;> ring

theorem step_tendsto (s x : ℝ) {A B : ℝ} (hA : 0 < A) (hB : 0 ≤ B) :
    Tendsto (step s x A B) atTop (𝓝 x) := by
  have hl : Tendsto (fun n : ℕ => (A+B*((n:ℝ)+1))/(A+B*n)) atTop (𝓝 1) := by
    rcases eq_or_lt_of_le hB with hz | hp
    · subst B
      simpa [hA.ne'] using (tendsto_const_nhds :
        Tendsto (fun _ : ℕ => (1 : ℝ)) atTop (𝓝 1))
    · have hab : 0 < A / B := div_pos hA hp
      apply (shifted_ratio_tendsto (A/B+1) (A/B) hab.le).congr'
      apply Eventually.of_forall
      intro n
      have h1 : 0 < (n : ℝ) + A / B := by positivity
      have h2 : 0 < A + B * (n : ℝ) := by positivity
      dsimp
      field_simp [hp.ne', h1.ne', h2.ne']
      <;> ring
  have hc : Tendsto (fun _ : ℕ => x) atTop (𝓝 x) := tendsto_const_nhds
  have hh := (((hc.mul
    (shifted_ratio_tendsto (1/2) 1 (by norm_num))).mul
    (shifted_ratio_tendsto s 1 (by norm_num))).mul
    (shifted_ratio_tendsto (1-s) 1 (by norm_num))).mul hl
  simpa only [step, mul_one] using hh

/-- The argument is the least real upper bound on the ratios in omitted tails. -/
theorem least_tail_ratio {s x A B : ℝ} (hs : 0 < s) (hs' : s < 1)
    (hx : 0 < x) (hA : 0 < A) (hB : 0 ≤ B) :
    IsLeast {q : ℝ | ∀ n : ℕ, 1 ≤ n → step s x A B n ≤ q} x := by
  refine ⟨fun n hn => (step_lt_argument hs hs' hx hA hB hn).le, ?_⟩
  intro q hq
  apply le_of_tendsto (step_tendsto s x hA hB)
  filter_upwards [eventually_ge_atTop (1 : ℕ)] with n hn
  exact hq n hn

theorem first_ratio (s x A B : ℝ) :
    step s x A B 0 = x * (s * (1-s) * (A+B) / (2*A)) := by
  dsimp [step]
  simp only [Nat.cast_zero, zero_add, mul_zero, mul_one, add_zero, div_one]
  ring

theorem least_full_ratio {s x A B : ℝ} (hs : 0 < s) (hs' : s < 1)
    (hx : 0 < x) (hA : 0 < A) (hB : 0 ≤ B) :
    IsLeast {q : ℝ | ∀ n : ℕ, step s x A B n ≤ q} (max x (step s x A B 0)) := by
  have ht := least_tail_ratio hs hs' hx hA hB
  constructor
  · intro n
    cases n with
    | zero => exact le_max_right _ _
    | succ n => exact (ht.1 _ (by omega)).trans (le_max_left _ _)
  · intro q hq
    exact max_le (ht.2 (fun n _ => hq n)) (hq 0)

open N58RatioBound

/-- Identify the new real ratios with the rational ratios of the existing N=58 development. -/
theorem n58_step (n : ℕ) :
    (ramanujanStepRatio n : ℝ) = step (1/4) (1 / 99^4) 1103 26390 n := by
  unfold ramanujanStepRatio quarticStepRatio linearStepRatio step
  push_cast
  dsimp only
  have h1 : 0 < (n : ℝ) + 1 := by positivity
  have h2 : 0 < 1103 + 26390 * (n : ℝ) := by positivity
  field_simp [h1.ne', h2.ne']
  <;> ring

theorem n58_first_ratio :
    ramanujanStepRatio 0 = (82479 / 35296 : ℚ) / 99^4 := by
  norm_num [ramanujanStepRatio, quarticStepRatio, linearStepRatio]

theorem n58_least_tail_ratio :
    IsLeast {q : ℝ | ∀ n : ℕ, 1 ≤ n → (ramanujanStepRatio n : ℝ) ≤ q}
      (1 / 99^4) := by
  simpa only [n58_step] using
    (least_tail_ratio (s := 1/4) (A := 1103) (B := 26390) (x := 1/99^4)
      (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num))

/-- A positive sequence satisfying the ratio law has a strictly bounded infinite omitted tail. -/
theorem infinite_tail_lt {s x A B : ℝ} (hs : 0 < s) (hs' : s < 1)
    (hx : 0 < x) (hx' : x < 1) (hA : 0 < A) (hB : 0 ≤ B)
    (term : ℕ → ℝ) (hterm : ∀ n, 0 < term n)
    (hrec : ∀ n, term (n+1) = step s x A B n * term n) (M : ℕ) :
    (∑' j : ℕ, term (M+1+j)) < term (M+1) / (1-x) := by
  have hstep (n : ℕ) (hn : 1 ≤ n) : term (n+1) < x * term n := by
    rw [hrec]
    exact mul_lt_mul_of_pos_right (step_lt_argument hs hs' hx hA hB hn) (hterm n)
  have hdom (j : ℕ) : term (M+1+j) ≤ x^j * term (M+1) := by
    induction j with
    | zero => simp
    | succ j ih =>
      calc
        term (M+1+(j+1)) ≤ x * term (M+1+j) := (hstep _ (by omega)).le
        _ ≤ x * (x^j * term (M+1)) := mul_le_mul_of_nonneg_left ih hx.le
        _ = x^(j+1) * term (M+1) := by ring
  have hsum := (summable_geometric_of_lt_one hx.le hx').mul_right (term (M+1))
  have hlt := Summable.tsum_lt_tsum_of_nonneg (i := 1)
    (fun j : ℕ => (hterm (M+1+j)).le) hdom
    (by simpa only [pow_one] using hstep (M+1) (by omega)) hsum
  rwa [tsum_mul_right, tsum_geometric_of_lt_one hx.le hx', inv_mul_eq_div] at hlt

end EnterpriseMath.PrecisionPi.SharpPositiveTail
