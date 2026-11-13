import EnterpriseMath.Precision.N58RatioBound

open Filter
open scoped Topology

noncomputable section

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
  have hy1 : 1 ≤ y := by
    change (1 : ℝ) ≤ (n : ℝ)
    exact_mod_cast hn
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
  field_simp [hn'.ne', hb'.ne']

theorem step_tendsto (s x : ℝ) {A B : ℝ} (hA : 0 < A) (hB : 0 ≤ B) :
    Tendsto (step s x A B) atTop (𝓝 x) := by
  have hl : Tendsto (fun n : ℕ => (A+B*((n:ℝ)+1))/(A+B*n)) atTop (𝓝 1) := by
    rcases eq_or_lt_of_le hB with hz | hp
    · subst B
      simp [hA.ne']
    · have hab : 0 < A / B := div_pos hA hp
      apply (shifted_ratio_tendsto (A/B+1) (A/B) hab.le).congr'
      apply Eventually.of_forall
      intro n
      have h1 : 0 < (n : ℝ) + A / B := by positivity
      have h2 : 0 < A + B * (n : ℝ) := by positivity
      have hden : A+B*(n:ℝ) = B*((n:ℝ)+A/B) := by
        field_simp [hp.ne']
        ring
      have hnum : A+B*((n:ℝ)+1) = B*((n:ℝ)+(A/B+1)) := by
        field_simp [hp.ne']
        ring
      apply (div_eq_div_iff h1.ne' h2.ne').2
      rw [hden, hnum]
      ring
  have hc : Tendsto (fun _ : ℕ => x) atTop (𝓝 x) := tendsto_const_nhds
  have hh := (((hc.mul
    (shifted_ratio_tendsto (1/2) 1 (by norm_num))).mul
    (shifted_ratio_tendsto s 1 (by norm_num))).mul
    (shifted_ratio_tendsto (1-s) 1 (by norm_num))).mul hl
  unfold step
  simpa only [mul_one] using hh

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
  by_cases hA : A = 0
  · simp [hA]
  · field_simp [hA]

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
  have h1 : 0 < (n : ℝ) + 1 := by positivity
  have h2 : 0 < 1103 + 26390 * (n : ℝ) := by positivity
  field_simp [h1.ne', h2.ne']
  ring

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
        term (M+1+(j+1)) ≤ x * term (M+1+j) := (hstep (M+1+j) (by omega)).le
        _ ≤ x * (x^j * term (M+1)) := mul_le_mul_of_nonneg_left ih hx.le
        _ = x^(j+1) * term (M+1) := by ring
  have hsum := (summable_geometric_of_lt_one hx.le hx').mul_right (term (M+1))
  have hlt := Summable.tsum_lt_tsum_of_nonneg (i := 1)
    (fun j : ℕ => (hterm (M+1+j)).le) hdom
    (by simpa only [pow_one] using hstep (M+1) (by omega)) hsum
  rwa [tsum_mul_right, tsum_geometric_of_lt_one hx.le hx', inv_mul_eq_div] at hlt

/-- The normalized infinite remainder converges to the optimal geometric multiplier. -/
theorem normalized_tail_tendsto {s x A B : ℝ} (hs : 0 < s) (hs' : s < 1)
    (hx : 0 < x) (hx' : x < 1) (hA : 0 < A) (hB : 0 ≤ B)
    (term : ℕ → ℝ) (hterm : ∀ n, 0 < term n)
    (hrec : ∀ n, term (n+1) = step s x A B n * term n) :
    Tendsto (fun M : ℕ => (∑' j : ℕ, term (M+1+j)) / term (M+1))
      atTop (𝓝 ((1-x)⁻¹)) := by
  let f (M j : ℕ) := term (M+1+j) / term (M+1)
  have hzero (M : ℕ) : f M 0 = 1 := by simp [f, (hterm (M+1)).ne']
  have hsucc (M j : ℕ) : f M (j+1) = step s x A B (M+1+j) * f M j := by
    dsimp [f]
    rw [show M+1+(j+1) = (M+1+j)+1 by omega, hrec]
    ring
  have hdom (M j : ℕ) : f M j ≤ x^j := by
    induction j with
    | zero => simp [hzero]
    | succ j ih =>
      rw [hsucc, pow_succ']
      have hf : 0 ≤ f M j := (div_pos (hterm _) (hterm _)).le
      exact mul_le_mul ((step_lt_argument hs hs' hx hA hB (by omega : 1 ≤ M+1+j)).le)
        ih hf hx.le
  have hpoint (j : ℕ) : Tendsto (fun M : ℕ => f M j) atTop (𝓝 (x^j)) := by
    induction j with
    | zero => simp only [hzero, pow_zero]; exact tendsto_const_nhds
    | succ j ih =>
      have hshift : Tendsto (fun M : ℕ => step s x A B (M+1+j)) atTop (𝓝 x) := by
        simpa only [Nat.add_assoc] using
          (tendsto_add_atTop_iff_nat (1+j)).2 (step_tendsto s x hA hB)
      simpa only [hsucc, pow_succ'] using hshift.mul ih
  have hbound : ∀ᶠ M : ℕ in atTop, ∀ j : ℕ, ‖f M j‖ ≤ x^j := by
    apply Eventually.of_forall
    intro M j
    have hf : 0 ≤ f M j := (div_pos (hterm _) (hterm _)).le
    simpa only [Real.norm_eq_abs, abs_of_nonneg hf] using hdom M j
  have hlim := tendsto_tsum_of_dominated_convergence (summable_geometric_of_lt_one hx.le hx')
    hpoint hbound
  simpa only [f, tsum_div_const, tsum_geometric_of_lt_one hx.le hx'] using hlim

theorem least_tail_multiplier {s x A B : ℝ} (hs : 0 < s) (hs' : s < 1)
    (hx : 0 < x) (hx' : x < 1) (hA : 0 < A) (hB : 0 ≤ B)
    (term : ℕ → ℝ) (hterm : ∀ n, 0 < term n)
    (hrec : ∀ n, term (n+1) = step s x A B n * term n) :
    IsLeast {c : ℝ | ∀ M : ℕ, (∑' j : ℕ, term (M+1+j)) / term (M+1) ≤ c}
      ((1-x)⁻¹) := by
  constructor
  · intro M
    apply (div_le_iff₀ (hterm _)).2
    rw [inv_mul_eq_div]
    exact (infinite_tail_lt hs hs' hx hx' hA hB term hterm hrec M).le
  · intro c hc
    exact le_of_tendsto (normalized_tail_tendsto hs hs' hx hx' hA hB term hterm hrec)
      (Eventually.of_forall hc)

/-- The N=58 sequence generated by the original rational step ratio, before the constant prefactor. -/
noncomputable def term58 : ℕ → ℝ
  | 0 => 1103
  | n+1 => (ramanujanStepRatio n : ℝ) * term58 n

theorem term58_pos (n : ℕ) : 0 < term58 n := by
  induction n with
  | zero => norm_num [term58]
  | succ n ih =>
    rw [term58, n58_step]
    exact mul_pos (step_pos (by norm_num) (by norm_num) (by norm_num) (by norm_num)
      (by norm_num) n) ih

theorem n58_least_tail_multiplier :
    IsLeast {c : ℝ | ∀ M : ℕ, (∑' j : ℕ, term58 (M+1+j)) / term58 (M+1) ≤ c}
      (96059601 / 96059600) := by
  have hrec (n : ℕ) :
      term58 (n+1) = step (1/4) (1/99^4) 1103 26390 n * term58 n := by
    rw [term58, n58_step]
  have hh := least_tail_multiplier (s := 1/4) (x := 1/99^4) (A := 1103) (B := 26390)
    (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num)
    term58 term58_pos hrec
  convert hh using 1
  norm_num

/-- The ordinary factorial summands, before the common prefactor. -/
noncomputable def factorialTerm58 (n : ℕ) : ℝ :=
  ((4*n).factorial : ℝ) / (n.factorial : ℝ)^4 * (1103 + 26390*(n:ℝ)) / (396:ℝ)^(4*n)

theorem factorialTerm58_succ (n : ℕ) :
    factorialTerm58 (n+1) = (ramanujanStepRatio n : ℝ) * factorialTerm58 n := by
  unfold factorialTerm58 ramanujanStepRatio quarticStepRatio linearStepRatio
  have hi : 4*(n+1) = (4*n)+4 := by omega
  rw [hi, pow_add]
  rw [show (4*n)+4 = (((4*n+1)+1)+1)+1 by omega]
  push_cast
  simp only [Nat.factorial_succ, Nat.cast_mul, Nat.cast_add, Nat.cast_one, Nat.cast_ofNat]
  have hf : (0:ℝ) < (n.factorial : ℝ) := by exact_mod_cast Nat.factorial_pos n
  have hn : 0 < (n:ℝ)+1 := by positivity
  have hlin : 0 < 1103+26390*(n:ℝ) := by positivity
  have hpow : (396:ℝ)^(4*n) ≠ 0 := by positivity
  field_simp [hf.ne', hn.ne', hlin.ne', hpow]
  ring

theorem term58_eq_factorialTerm58 (n : ℕ) : term58 n = factorialTerm58 n := by
  induction n with
  | zero => norm_num [term58, factorialTerm58]
  | succ n ih => rw [term58, factorialTerm58_succ, ih]

end EnterpriseMath.PrecisionPi.SharpPositiveTail

end
