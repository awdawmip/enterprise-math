import Mathlib

namespace EnterpriseMath.Precision

/-- The exact two-to-one even-site spectral decimation polynomial from #1159. -/
def spectralDecimation (u : ℝ) : ℝ :=
  u * (4 - u)

/--
WSR-L01: eliminating the odd sites in the second-order Dirichlet recurrence
produces the coarse recurrence with spectral parameter `u * (4-u)`.

This is a local algebraic theorem.  It uses no trigonometric function, circle,
or value of `pi`.
-/
theorem spectralDecimation_local
    (u vm2 vm1 v0 vp1 vp2 : ℝ)
    (hp : vp2 = (2 - u) * vp1 - v0)
    (hm : vm2 = (2 - u) * vm1 - v0)
    (h0 : vp1 + vm1 = (2 - u) * v0) :
    vp2 + vm2 = (2 - spectralDecimation u) * v0 := by
  calc
    vp2 + vm2 = ((2 - u) * vp1 - v0) + ((2 - u) * vm1 - v0) := by
      rw [hp, hm]
    _ = (2 - u) * (vp1 + vm1) - 2 * v0 := by ring
    _ = (2 - u) * ((2 - u) * v0) - 2 * v0 := by rw [h0]
    _ = (2 - spectralDecimation u) * v0 := by
      unfold spectralDecimation
      ring

/--
WSR-L02: algebraic inverse-decimation kernel.
If `b^2 = 4-a`, then the identity-near candidate `2-b` maps back to `a`.
-/
theorem inverseDecimation_algebra
    (a b : ℝ) (hb : b ^ 2 = 4 - a) :
    spectralDecimation (2 - b) = a := by
  unfold spectralDecimation
  nlinarith

/-- The square-root inverse branch used by the dyadic first mode. -/
theorem inverseDecimation_sqrt
    (a : ℝ) (ha : a ≤ 4) :
    spectralDecimation (2 - Real.sqrt (4 - a)) = a := by
  have hnonneg : 0 ≤ 4 - a := by linarith
  have hsqrt : (Real.sqrt (4 - a)) ^ 2 = 4 - a := by
    simpa using Real.sq_sqrt hnonneg
  exact inverseDecimation_algebra a (Real.sqrt (4 - a)) hsqrt

/--
WSR-L03: the algebraic kernel behind
`h'(y) = 2 * (1-C(y))^2` once `S^2+C^2=1` is supplied.
-/
theorem richardsonDerivativeKernel
    (s c : ℝ) (hunit : s ^ 2 + c ^ 2 = 1) :
    3 - 4 * c + (c ^ 2 - s ^ 2) = 2 * (1 - c) ^ 2 := by
  nlinarith

/-- The Richardson derivative kernel is nonnegative. -/
theorem richardsonDerivativeKernel_nonneg
    (s c : ℝ) (hunit : s ^ 2 + c ^ 2 = 1) :
    0 ≤ 3 - 4 * c + (c ^ 2 - s ^ 2) := by
  rw [richardsonDerivativeKernel s c hunit]
  positivity

/--
WSR-L04: exact rational value of the finite alternating partial sum used in
the target-free certificate `S(4) < 0`.

The separate analytic layer supplies the alternating-remainder comparison.
-/
theorem sineAtFourPartial_eq :
    (4 : ℚ) - 64 / 6 + 1024 / 120 - 16384 / 5040 + 262144 / 362880
      = -(268 : ℚ) / 405 := by
  norm_num

/-- The finite rational sign certificate is strictly negative. -/
theorem sineAtFourPartial_neg :
    (4 : ℚ) - 64 / 6 + 1024 / 120 - 16384 / 5040 + 262144 / 362880 < 0 := by
  norm_num

/--
The scalar continuant associated with the size-`n` tridiagonal Dirichlet
characteristic recurrence.  A later matrix lemma identifies this recursion
with the actual determinant; keeping the recursion explicit makes the finite
algebraic core reusable independently of a matrix representation.
-/
def dirichletContinuant (z : ℝ) : ℕ → ℝ
  | 0 => 1
  | 1 => 2 - z
  | n + 2 => (2 - z) * dirichletContinuant z (n + 1) - dirichletContinuant z n

/-- WSR-L05: at zero spectral parameter, the size-`n` continuant is `n+1`. -/
theorem dirichletContinuant_zero (n : ℕ) :
    dirichletContinuant 0 n = ((n + 1 : ℕ) : ℝ) := by
  induction n using Nat.twoStepInduction with
  | zero => norm_num [dirichletContinuant]
  | one => norm_num [dirichletContinuant]
  | more n ih0 ih1 =>
      rw [dirichletContinuant, ih0, ih1]
      push_cast
      ring

/--
The recurrence-level form of `det L_M^D = M`: once the determinant/continuant
bridge is installed, this theorem discharges the value calculation itself.
-/
theorem dirichletContinuant_zero_pred (M : ℕ) (hM : 1 ≤ M) :
    dirichletContinuant 0 (M - 1) = (M : ℝ) := by
  simpa [Nat.sub_add_cancel hM] using dirichletContinuant_zero (M - 1)

/-- Append one endpoint to a finite path matrix, with diagonal entry `2-z`. -/
private def extendDirichletPath (z : ℝ) {n : ℕ} (M : Matrix (Fin n) (Fin n) ℝ) :
    Matrix (Fin n.succ) (Fin n.succ) ℝ :=
  let tailLink := fun i : Fin n ↦ if i.val + 1 = n then -1 else 0
  fun i j ↦
    Fin.lastCases (Fin.lastCases (2 - z) tailLink j)
      (fun i ↦ Fin.lastCases (tailLink i) (fun j ↦ M i j) j) i

private theorem extendDirichletPath_tail (z : ℝ) {n : ℕ} (M : Matrix (Fin n) (Fin n) ℝ) :
    (extendDirichletPath z M).submatrix Fin.castSucc Fin.castSucc = M := by
  ext i j
  simp [extendDirichletPath]

private theorem extendDirichletPath_minor (z : ℝ) {n : ℕ}
    (M : Matrix (Fin n.succ) (Fin n.succ) ℝ) :
    ((extendDirichletPath z M).submatrix Fin.castSucc
      (Fin.succAbove (Fin.castSucc (Fin.last n)))).det =
      -(M.submatrix Fin.castSucc Fin.castSucc).det := by
  let B := (extendDirichletPath z M).submatrix Fin.castSucc
    (Fin.succAbove (Fin.castSucc (Fin.last n)))
  have hlast : B (Fin.last n) (Fin.last n) = -1 := by
    simp [B, extendDirichletPath]
  have hzero (i : Fin n) : B i.castSucc (Fin.last n) = 0 := by
    simp [B, extendDirichletPath]
    grind
  have hminor : B.submatrix Fin.castSucc Fin.castSucc =
      M.submatrix Fin.castSucc Fin.castSucc := by
    ext i j
    simp [B, extendDirichletPath]
  change B.det = _
  simp [Matrix.det_succ_column B (Fin.last n), Fin.sum_univ_castSucc, hlast, hzero, hminor]

private theorem extendDirichletPath_det (z : ℝ) {n : ℕ}
    (M : Matrix (Fin n.succ) (Fin n.succ) ℝ) :
    (extendDirichletPath z M).det =
      (2 - z) * M.det - (M.submatrix Fin.castSucc Fin.castSucc).det := by
  rw [Matrix.det_succ_row (extendDirichletPath z M) (Fin.last _), Fin.sum_univ_castSucc]
  simp only [extendDirichletPath, extendDirichletPath_tail, Fin.lastCases_last,
    Fin.lastCases_castSucc, Fin.val_last, Fin.val_castSucc, Fin.succAbove_last]
  rw [Finset.sum_eq_single_of_mem (Fin.last n) (Finset.mem_univ _)]
  · rw [ite_eq_left (by rfl), extendDirichletPath_minor, Fin.val_last,
      Odd.neg_one_pow ⟨n, by ring⟩, Even.neg_one_pow ⟨n + 1, rfl⟩]
    ring
  · intro b _ hb
    rw [ite_eq_right (fun h => hb (Fin.ext (by rw [Fin.val_last]; lia)))]
    ring

/--
A concrete finite Dirichlet path matrix, built by repeated endpoint extension.
This recursive representation is definitionally tridiagonal and is chosen so
its determinant recurrence is visible to Lean without importing a continuum
spectral model.
-/
def dirichletMatrix (z : ℝ) : (n : ℕ) → Matrix (Fin n) (Fin n) ℝ
  | 0 => fun i ↦ Fin.elim0 i
  | n + 1 => extendDirichletPath z (dirichletMatrix z n)

/-- WSR-L06: the actual finite Dirichlet determinant obeys the continuant recurrence. -/
theorem dirichletMatrix_det_add_two (z : ℝ) (n : ℕ) :
    (dirichletMatrix z (n + 2)).det =
      (2 - z) * (dirichletMatrix z (n + 1)).det - (dirichletMatrix z n).det := by
  change (extendDirichletPath z (dirichletMatrix z (n + 1))).det = _
  rw [extendDirichletPath_det]
  have htail :
      (dirichletMatrix z (n + 1)).submatrix Fin.castSucc Fin.castSucc =
        dirichletMatrix z n := by
    change (extendDirichletPath z (dirichletMatrix z n)).submatrix
      Fin.castSucc Fin.castSucc = dirichletMatrix z n
    exact extendDirichletPath_tail z (dirichletMatrix z n)
  rw [htail]

/-- WSR-L07: the finite matrix determinant is exactly the declared continuant. -/
theorem dirichletMatrix_det_eq_continuant (z : ℝ) (n : ℕ) :
    (dirichletMatrix z n).det = dirichletContinuant z n := by
  induction n using Nat.twoStepInduction with
  | zero => simp [dirichletMatrix, dirichletContinuant]
  | one => simp [dirichletMatrix, extendDirichletPath, dirichletContinuant]
  | more n ih0 ih1 =>
      rw [dirichletMatrix_det_add_two, dirichletContinuant, ih0, ih1]

/-- WSR-L08: determinant of the zero-parameter size-`n` Dirichlet path matrix. -/
theorem dirichletMatrix_det_zero (n : ℕ) :
    (dirichletMatrix 0 n).det = ((n + 1 : ℕ) : ℝ) := by
  rw [dirichletMatrix_det_eq_continuant, dirichletContinuant_zero]

/-- The #1159 normalization `det L_M^D = M` for the `(M-1)×(M-1)` path matrix. -/
theorem dirichletMatrix_det_zero_pred (M : ℕ) (hM : 1 ≤ M) :
    (dirichletMatrix 0 (M - 1)).det = (M : ℝ) := by
  rw [dirichletMatrix_det_eq_continuant]
  exact dirichletContinuant_zero_pred M hM

end EnterpriseMath.Precision
