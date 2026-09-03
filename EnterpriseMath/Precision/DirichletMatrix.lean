import EnterpriseMath.Precision.SpectralPrecision

namespace EnterpriseMath.Precision

/-- Append one endpoint to a finite path matrix, with diagonal entry `2-z`. -/
private def extendDirichletPath (z : ℝ) {n : ℕ} (M : Matrix (Fin n) (Fin n) ℝ) :
    Matrix (Fin n.succ) (Fin n.succ) ℝ :=
  let tailLink := fun i : Fin n ↦ if i.val + 1 = n then -1 else 0
  fun i j ↦
    Fin.lastCases (Fin.lastCases (2 - z) tailLink j)
      (fun i ↦ Fin.lastCases (tailLink i) (fun j ↦ M i j) j) i

private theorem extendDirichletPath_last_last (z : ℝ) {n : ℕ}
    (M : Matrix (Fin n) (Fin n) ℝ) :
    extendDirichletPath z M (Fin.last n) (Fin.last n) = 2 - z := by
  simp [extendDirichletPath]

private theorem extendDirichletPath_tail (z : ℝ) {n : ℕ} (M : Matrix (Fin n) (Fin n) ℝ) :
    (extendDirichletPath z M).submatrix Fin.castSucc Fin.castSucc = M := by
  ext i j
  change extendDirichletPath z M i.castSucc j.castSucc = M i j
  simp [extendDirichletPath]

private theorem extendDirichletPath_minor (z : ℝ) {n : ℕ}
    (M : Matrix (Fin n.succ) (Fin n.succ) ℝ) :
    ((extendDirichletPath z M).submatrix Fin.castSucc
      (Fin.succAbove (Fin.castSucc (Fin.last n)))).det =
      -(M.submatrix Fin.castSucc Fin.castSucc).det := by
  let B := (extendDirichletPath z M).submatrix Fin.castSucc
    (Fin.succAbove (Fin.castSucc (Fin.last n)))
  have hlast : B (Fin.last n) (Fin.last n) = -1 := by
    change extendDirichletPath z M (Fin.castSucc (Fin.last n))
      ((Fin.castSucc (Fin.last n)).succAbove (Fin.last n)) = -1
    simp [extendDirichletPath, Fin.succAbove]
  have hzero (i : Fin n) : B i.castSucc (Fin.last n) = 0 := by
    change extendDirichletPath z M (Fin.castSucc i.castSucc)
      ((Fin.castSucc (Fin.last n)).succAbove (Fin.last n)) = 0
    simp [extendDirichletPath, Fin.succAbove]
    omega
  have hminor : B.submatrix Fin.castSucc Fin.castSucc =
      M.submatrix Fin.castSucc Fin.castSucc := by
    ext i j
    change extendDirichletPath z M (Fin.castSucc i.castSucc)
      ((Fin.castSucc (Fin.last n)).succAbove j.castSucc) = M i.castSucc j.castSucc
    simp [extendDirichletPath, Fin.succAbove]
  change B.det = _
  simp [Matrix.det_succ_column B (Fin.last n), Fin.sum_univ_castSucc, hlast, hzero, hminor]

private theorem extendDirichletPath_det (z : ℝ) {n : ℕ}
    (M : Matrix (Fin n.succ) (Fin n.succ) ℝ) :
    (extendDirichletPath z M).det =
      (2 - z) * M.det - (M.submatrix Fin.castSucc Fin.castSucc).det := by
  let A := extendDirichletPath z M
  have hdiag : A (Fin.last (n + 1)) (Fin.last (n + 1)) = 2 - z := by
    exact extendDirichletPath_last_last z M
  have hlink : A (Fin.last (n + 1)) (Fin.castSucc (Fin.last n)) = -1 := by
    simp [A, extendDirichletPath, Fin.val_last]
  have hzero (b : Fin (n + 1)) (hb : b ≠ Fin.last n) :
      A (Fin.last (n + 1)) b.castSucc = 0 := by
    have hbval : b.val ≠ n := by
      intro h
      apply hb
      apply Fin.ext
      simpa [Fin.val_last] using h
    simp [A, extendDirichletPath, hbval]
  have htail : (A.submatrix Fin.castSucc Fin.castSucc).det = M.det := by
    change ((extendDirichletPath z M).submatrix Fin.castSucc Fin.castSucc).det = M.det
    rw [extendDirichletPath_tail]
  have hminor :
      (A.submatrix Fin.castSucc (Fin.succAbove (Fin.castSucc (Fin.last n)))).det =
        -(M.submatrix Fin.castSucc Fin.castSucc).det := by
    change ((extendDirichletPath z M).submatrix Fin.castSucc
      (Fin.succAbove (Fin.castSucc (Fin.last n)))).det = _
    exact extendDirichletPath_minor z M
  have hodd : Odd ((Fin.last (n + 1)).val + (Fin.castSucc (Fin.last n)).val) := by
    refine ⟨n, ?_⟩
    simp [Fin.val_last]
    omega
  have heven : Even ((Fin.last (n + 1)).val + (Fin.last (n + 1)).val) := by
    refine ⟨n + 1, ?_⟩
    simp [Fin.val_last]
  change A.det = _
  rw [Matrix.det_succ_row A (Fin.last _), Fin.sum_univ_castSucc]
  simp only [Fin.succAbove_last]
  rw [Finset.sum_eq_single_of_mem (Fin.last n) (Finset.mem_univ _)]
  · rw [hlink, hminor, hdiag, htail,
      Odd.neg_one_pow hodd, Even.neg_one_pow heven]
    ring
  · intro b _ hb
    rw [hzero b hb]
    ring

/-- Endpoint extension preserves Hermitian symmetry over the real carrier. -/
private theorem extendDirichletPath_isHermitian (z : ℝ) {n : ℕ}
    (M : Matrix (Fin n) (Fin n) ℝ) (hM : M.IsHermitian) :
    (extendDirichletPath z M).IsHermitian := by
  apply Matrix.IsHermitian.ext
  intro i j
  refine Fin.lastCases ?_ (fun i => ?_) i
  · refine Fin.lastCases ?_ (fun j => ?_) j
    · simp [extendDirichletPath]
    · simp [extendDirichletPath]
  · refine Fin.lastCases ?_ (fun j => ?_) j
    · simp [extendDirichletPath]
    · simpa [extendDirichletPath] using hM.apply i j

/-- Endpoint extension respects the scalar spectral shift. -/
private theorem extendDirichletPath_scalar_sub (z : ℝ) {n : ℕ}
    (M0 Mz : Matrix (Fin n) (Fin n) ℝ)
    (hshift : Matrix.scalar (Fin n) z - M0 = -Mz) :
    Matrix.scalar (Fin (n + 1)) z - extendDirichletPath 0 M0 =
      -extendDirichletPath z Mz := by
  ext i j
  simp only [Matrix.sub_apply, Matrix.neg_apply]
  refine Fin.lastCases ?_ (fun i => ?_) i
  · refine Fin.lastCases ?_ (fun j => ?_) j
    · simp [Matrix.scalar_apply, extendDirichletPath]
      ring
    · simp [Matrix.scalar_apply, extendDirichletPath]
  · refine Fin.lastCases ?_ (fun j => ?_) j
    · simp [Matrix.scalar_apply, extendDirichletPath]
    · have hij := congr_fun (congr_fun hshift i) j
      simpa [Matrix.sub_apply, Matrix.neg_apply, Matrix.scalar_apply, extendDirichletPath] using hij

/--
A concrete finite Dirichlet path matrix, built by repeated endpoint extension.
This recursive representation is definitionally tridiagonal.
-/
def dirichletMatrix (z : ℝ) : (n : ℕ) → Matrix (Fin n) (Fin n) ℝ
  | 0 => fun i ↦ Fin.elim0 i
  | n + 1 => extendDirichletPath z (dirichletMatrix z n)

private theorem dirichletMatrix_one_last (z : ℝ) :
    (dirichletMatrix z 1) (Fin.last 0) (Fin.last 0) = 2 - z := by
  change extendDirichletPath z (dirichletMatrix z 0) (Fin.last 0) (Fin.last 0) = 2 - z
  exact extendDirichletPath_last_last z (dirichletMatrix z 0)

/-- WSR-L34: every finite Dirichlet matrix is Hermitian (symmetric over `ℝ`). -/
theorem dirichletMatrix_isHermitian (z : ℝ) (n : ℕ) :
    (dirichletMatrix z n).IsHermitian := by
  induction n with
  | zero =>
      apply Matrix.IsHermitian.ext
      intro i
      exact Fin.elim0 i
  | succ n ih =>
      change (extendDirichletPath z (dirichletMatrix z n)).IsHermitian
      exact extendDirichletPath_isHermitian z (dirichletMatrix z n) ih

/--
WSR-L35: the spectral parameter enters only through a scalar diagonal shift.
Equivalently, `zI - L(0) = -L(z)`.
-/
theorem dirichletMatrix_scalar_sub_zero (z : ℝ) (n : ℕ) :
    Matrix.scalar (Fin n) z - dirichletMatrix 0 n = -dirichletMatrix z n := by
  induction n with
  | zero =>
      ext i
      exact Fin.elim0 i
  | succ n ih =>
      change Matrix.scalar (Fin (n + 1)) z -
          extendDirichletPath 0 (dirichletMatrix 0 n) =
        -extendDirichletPath z (dirichletMatrix z n)
      exact extendDirichletPath_scalar_sub z
        (dirichletMatrix 0 n) (dirichletMatrix z n) ih

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
  | zero =>
      change (dirichletMatrix z 0).det = 1
      exact Matrix.det_isEmpty
  | one =>
      rw [Matrix.det_fin_one]
      change (dirichletMatrix z 1) (0 : Fin 1) (0 : Fin 1) = 2 - z
      have hzero : (0 : Fin 1) = Fin.last 0 := Subsingleton.elim _ _
      rw [hzero]
      exact dirichletMatrix_one_last z
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
