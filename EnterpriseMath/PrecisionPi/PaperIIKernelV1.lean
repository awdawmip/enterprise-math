import Mathlib

namespace EnterpriseMath.PrecisionPi.PaperIIKernelV1

/-! ## 1. Enterprise-coordinate `K₄` incidence -/

/-- Six stable unoriented carrier-line families. -/
abbrev LineFamily := Fin 6

/-- Four overlapping three-line slice charts. -/
abbrev SliceChart := Fin 4

/-- The four slice charts, ordered as
`A={L₁,L₃,L₆}`, `B={L₁,L₄,L₅}`, `C={L₂,L₃,L₅}`,
`D={L₂,L₄,L₆}`. -/
def sliceLines : SliceChart → Finset LineFamily :=
  ![({0, 2, 5} : Finset LineFamily),
    ({0, 3, 4} : Finset LineFamily),
    ({1, 2, 4} : Finset LineFamily),
    ({1, 3, 5} : Finset LineFamily)]

theorem sliceLines_card (s : SliceChart) : (sliceLines s).card = 3 := by
  fin_cases s <;> native_decide

def incidentSlices (l : LineFamily) : Finset SliceChart :=
  Finset.univ.filter fun s => l ∈ sliceLines s

theorem incidentSlices_card (l : LineFamily) : (incidentSlices l).card = 2 := by
  fin_cases l <;> native_decide

theorem distinct_slices_share_one
    (s t : SliceChart) (h : s ≠ t) :
    ((sliceLines s) ∩ (sliceLines t)).card = 1 := by
  fin_cases s <;> fin_cases t <;> simp_all [sliceLines]

theorem four_slices : Fintype.card SliceChart = 4 := by
  simp [SliceChart]

theorem six_lines : Fintype.card LineFamily = 6 := by
  simp [LineFamily]

/-! ## 2. Integer slice-to-line residual and the `C₂` obstruction -/

abbrev VertexData := Fin 4 → ℤ

abbrev EdgeData := Fin 6 → ℤ

abbrev MatchingData := Fin 3 → ℤ

def vertexSum (v : VertexData) : ℤ :=
  v 0 + v 1 + v 2 + v 3

def edgeSum (x : EdgeData) : ℤ :=
  x 0 + x 1 + x 2 + x 3 + x 4 + x 5

def delta (v : VertexData) : EdgeData :=
  ![v 0 + v 1, v 0 + v 2, v 0 + v 3,
    v 1 + v 2, v 1 + v 3, v 2 + v 3]

theorem edgeSum_delta (v : VertexData) :
    edgeSum (delta v) = 3 * vertexSum v := by
  simp [edgeSum, delta, vertexSum]
  ring

theorem delta_zero_sum {v : VertexData} (hv : vertexSum v = 0) :
    edgeSum (delta v) = 0 := by
  rw [edgeSum_delta, hv]
  norm_num

def pattern (p q r : ℤ) : EdgeData :=
  ![p, q, r, -r, -q, -p]

@[simp] theorem edgeSum_pattern (p q r : ℤ) :
    edgeSum (pattern p q r) = 0 := by
  simp [edgeSum, pattern]

def matching (e : EdgeData) : MatchingData :=
  ![e 0 + e 5, e 1 + e 4, e 2 + e 3]

@[simp] theorem matching_pattern (p q r : ℤ) :
    matching (pattern p q r) = 0 := by
  funext i
  fin_cases i <;> simp [matching, pattern]

theorem matching_delta_of_zero_sum
    {v : VertexData} (hv : vertexSum v = 0) :
    matching (delta v) = 0 := by
  have hv' : v 0 + v 1 + v 2 + v 3 = 0 := by
    simpa [vertexSum] using hv
  funext i
  fin_cases i <;> simp [matching, delta] <;> omega

def witness (p q r k : ℤ) : VertexData :=
  ![k, p - k, q - k, r - k]

theorem witness_zero_sum
    {p q r k : ℤ} (h : p + q + r = 2 * k) :
    vertexSum (witness p q r k) = 0 := by
  simp [vertexSum, witness]
  omega

theorem delta_witness
    {p q r k : ℤ} (h : p + q + r = 2 * k) :
    delta (witness p q r k) = pattern p q r := by
  funext i
  fin_cases i <;> simp [delta, witness, pattern] <;> omega

theorem pattern_in_image_iff_even (p q r : ℤ) :
    (∃ v : VertexData, vertexSum v = 0 ∧ delta v = pattern p q r) ↔
      ∃ k : ℤ, p + q + r = 2 * k := by
  constructor
  · rintro ⟨v, hv, hd⟩
    have h0 := congrFun hd (0 : Fin 6)
    have h1 := congrFun hd (1 : Fin 6)
    have h2 := congrFun hd (2 : Fin 6)
    simp [delta, pattern] at h0 h1 h2
    have hv' : v 0 + v 1 + v 2 + v 3 = 0 := by
      simpa [vertexSum] using hv
    exact ⟨v 0, by omega⟩
  · rintro ⟨k, hk⟩
    exact ⟨witness p q r k, witness_zero_sum hk, delta_witness hk⟩

theorem basic_parity_nonzero :
    ¬ ∃ v : VertexData, vertexSum v = 0 ∧ delta v = pattern 1 0 0 := by
  intro h
  obtain ⟨k, hk⟩ := (pattern_in_image_iff_even 1 0 0).mp h
  omega

theorem doubled_pattern_in_image (p q r : ℤ) :
    ∃ v : VertexData,
      vertexSum v = 0 ∧ delta v = pattern (2 * p) (2 * q) (2 * r) := by
  apply (pattern_in_image_iff_even (2 * p) (2 * q) (2 * r)).mpr
  exact ⟨p + q + r, by ring⟩

theorem basic_parity_order_two :
    (¬ ∃ v : VertexData, vertexSum v = 0 ∧ delta v = pattern 1 0 0) ∧
    (∃ v : VertexData, vertexSum v = 0 ∧ delta v = pattern 2 0 0) := by
  exact ⟨basic_parity_nonzero, by simpa using doubled_pattern_in_image 1 0 0⟩

/-! ## 3. Paired Pell shells and quartic residual norm -/

def PositiveShell (P d y : ℤ) : Prop := P ^ 2 - d * y ^ 2 = 1

def NegativeShell (P d y : ℤ) : Prop := P ^ 2 - d * y ^ 2 = -1

theorem paired_shells_square_trace
    {P dp yp dm ym : ℤ}
    (hp : PositiveShell P dp yp)
    (hm : NegativeShell P dm ym) :
    (P ^ 2) ^ 2 - (dp * dm) * (yp * ym) ^ 2 = 1 := by
  have hp' : dp * yp ^ 2 = P ^ 2 - 1 := by
    unfold PositiveShell at hp
    linarith
  have hm' : dm * ym ^ 2 = P ^ 2 + 1 := by
    unfold NegativeShell at hm
    linarith
  calc
    (P ^ 2) ^ 2 - (dp * dm) * (yp * ym) ^ 2 =
        (P ^ 2) ^ 2 - (dp * yp ^ 2) * (dm * ym ^ 2) := by ring
    _ = (P ^ 2) ^ 2 - (P ^ 2 - 1) * (P ^ 2 + 1) := by rw [hp', hm']
    _ = 1 := by ring

theorem shell_norm (u : ℚ) : (1 - u) * (1 + u) = 1 - u ^ 2 := by
  ring

theorem n58_positive : PositiveShell 99 2 70 := by
  norm_num [PositiveShell]

theorem n58_negative : NegativeShell 99 58 13 := by
  norm_num [NegativeShell]

theorem n58_square_trace :
    ((99 : ℤ) ^ 2) ^ 2 - (2 * 58) * (70 * 13) ^ 2 = 1 := by
  exact paired_shells_square_trace n58_positive n58_negative

theorem n58_constants :
    (9801 : ℤ) = 99 ^ 2 ∧
    (396 : ℤ) = 4 * 99 ∧
    (26390 : ℤ) = 29 * 70 * 13 ∧
    (4 : ℤ) * 1103 = 29 * 70 * 13 - 2 * 99 * (99 + 13 - 1) := by
  norm_num

/-! ## 4. Finite CM transform and positive reciprocal hierarchy -/

def ordinaryPartial (c : ℕ → ℝ) (z : ℝ) (M : ℕ) : ℝ :=
  (Finset.range (M + 1)).sum fun n => c n * z ^ n

def thetaPartial (c : ℕ → ℝ) (z : ℝ) (M : ℕ) : ℝ :=
  (Finset.range (M + 1)).sum fun n => (n : ℝ) * c n * z ^ n

def cmPartial (A B : ℝ) (c : ℕ → ℝ) (z : ℝ) (M : ℕ) : ℝ :=
  (Finset.range (M + 1)).sum fun n =>
    (A + B * (n : ℝ)) * c n * z ^ n

theorem finite_cm_linearity
    (A B : ℝ) (c : ℕ → ℝ) (z : ℝ) (M : ℕ) :
    A * ordinaryPartial c z M + B * thetaPartial c z M =
      cmPartial A B c z M := by
  unfold ordinaryPartial thetaPartial cmPartial
  rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro n hn
  ring

theorem cmPartial_succ
    (A B : ℝ) (c : ℕ → ℝ) (z : ℝ) (M : ℕ) :
    cmPartial A B c z (M + 1) =
      cmPartial A B c z M +
        (A + B * ((M + 1 : ℕ) : ℝ)) * c (M + 1) * z ^ (M + 1) := by
  unfold cmPartial
  rw [Finset.sum_range_succ]

theorem cm_term_pos
    {A B z : ℝ} {c : ℕ → ℝ}
    (hA : 0 < A) (hB : 0 ≤ B) (hz : 0 < z)
    (hc : ∀ n, 0 < c n) (n : ℕ) :
    0 < (A + B * (n : ℝ)) * c n * z ^ n := by
  have hlin : 0 < A + B * (n : ℝ) := by
    positivity
  exact mul_pos (mul_pos hlin (hc n)) (pow_pos hz n)

theorem cmPartial_pos
    {A B z : ℝ} {c : ℕ → ℝ}
    (hA : 0 < A) (hB : 0 ≤ B) (hz : 0 < z)
    (hc : ∀ n, 0 < c n) (M : ℕ) :
    0 < cmPartial A B c z M := by
  induction M with
  | zero => simpa [cmPartial] using cm_term_pos hA hB hz hc 0
  | succ M ih =>
      rw [cmPartial_succ]
      exact add_pos ih (cm_term_pos hA hB hz hc (M + 1))

theorem reciprocal_cm_step
    {A B z : ℝ} {c : ℕ → ℝ}
    (hA : 0 < A) (hB : 0 ≤ B) (hz : 0 < z)
    (hc : ∀ n, 0 < c n) (M : ℕ) :
    1 / cmPartial A B c z (M + 1) < 1 / cmPartial A B c z M := by
  apply one_div_lt_one_div_of_lt (cmPartial_pos hA hB hz hc M)
  rw [cmPartial_succ]
  exact lt_add_of_pos_right _ (cm_term_pos hA hB hz hc (M + 1))

end EnterpriseMath.PrecisionPi.PaperIIKernelV1
