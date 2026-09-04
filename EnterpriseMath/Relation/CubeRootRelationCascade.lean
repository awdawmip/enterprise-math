import Mathlib.Tactic

namespace EnterpriseMath.CubeRootRelationCascade

/-- Geometrically decaying forcing along cube-root scale levels. -/
def cubeRootForcing (C L : ℝ) (k : ℕ) : ℝ :=
  (C / L) * (1 / 3 : ℝ) ^ k

/-- Closed majorant for the recurrence `E_(k+1) <= E_k/9 + forcing_k`. -/
def cubeRootMajorant (E₀ C L : ℝ) (k : ℕ) : ℝ :=
  (1 / 9 : ℝ) ^ k * E₀ +
    (9 * C / (2 * L)) *
      ((1 / 3 : ℝ) ^ k - (1 / 9 : ℝ) ^ k)

@[simp] theorem cubeRootMajorant_zero (E₀ C L : ℝ) :
    cubeRootMajorant E₀ C L 0 = E₀ := by
  simp [cubeRootMajorant]

/-- The closed majorant obeys the exact affine cube-root recurrence. -/
theorem cubeRootMajorant_succ (E₀ C L : ℝ) (k : ℕ) :
    cubeRootMajorant E₀ C L (k + 1) =
      (1 / 9 : ℝ) * cubeRootMajorant E₀ C L k +
        cubeRootForcing C L k := by
  unfold cubeRootMajorant cubeRootForcing
  simp only [pow_succ]
  ring

/-- Any sequence satisfying the one-ninth recurrence is bounded by the closed majorant. -/
theorem le_cubeRootMajorant
    (E : ℕ → ℝ) (C L : ℝ)
    (hrec : ∀ k,
      E (k + 1) ≤ (1 / 9 : ℝ) * E k + cubeRootForcing C L k) :
    ∀ k, E k ≤ cubeRootMajorant (E 0) C L k := by
  intro k
  induction k with
  | zero =>
      simp
  | succ k ih =>
      calc
        E (k + 1) ≤
            (1 / 9 : ℝ) * E k + cubeRootForcing C L k := hrec k
        _ ≤ (1 / 9 : ℝ) * cubeRootMajorant (E 0) C L k +
            cubeRootForcing C L k := by
              gcongr
        _ = cubeRootMajorant (E 0) C L (k + 1) := by
              rw [cubeRootMajorant_succ]

/-- The forcing part of the majorant has the exact geometric-sum form. -/
theorem cubeRootMajorant_forcing_part
    (E₀ C L : ℝ) (k : ℕ) :
    cubeRootMajorant E₀ C L k - (1 / 9 : ℝ) ^ k * E₀ =
      (9 * C / (2 * L)) *
        ((1 / 3 : ℝ) ^ k - (1 / 9 : ℝ) ^ k) := by
  unfold cubeRootMajorant
  ring

/-- Under nonnegative forcing coefficient, the forcing part is bounded by the `3^-k` scale. -/
theorem cubeRootMajorant_le_geometricRate
    (E₀ C L : ℝ) (k : ℕ) (hCL : 0 ≤ C / L) :
    cubeRootMajorant E₀ C L k ≤
      (1 / 9 : ℝ) ^ k * E₀ +
        (9 * C / (2 * L)) * (1 / 3 : ℝ) ^ k := by
  unfold cubeRootMajorant
  have hcoef : 0 ≤ 9 * C / (2 * L) := by
    calc
      0 ≤ (9 / 2 : ℝ) * (C / L) := mul_nonneg (by norm_num) hCL
      _ = 9 * C / (2 * L) := by ring
  have hpow : 0 ≤ (1 / 9 : ℝ) ^ k := pow_nonneg (by norm_num) k
  nlinarith

end EnterpriseMath.CubeRootRelationCascade
