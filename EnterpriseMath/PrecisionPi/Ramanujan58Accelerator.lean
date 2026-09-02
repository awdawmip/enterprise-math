import EnterpriseMath.PrecisionPi.EqualOccupancyStirling
import EnterpriseMath.PrecisionPi.PositiveAccelerator

namespace EnterpriseMath.PrecisionPi

open Filter Topology

noncomputable section

/-- Common algebraic prefactor in Ramanujan's `N = 58` quartic formula. -/
noncomputable def ramanujan58Scale : ℝ :=
  2 * Real.sqrt 2 / (99 : ℝ) ^ 2

/-- Constant part of the `N = 58` CM differential functional. -/
noncomputable def ramanujan58A : ℝ :=
  ramanujan58Scale * 1103

/-- Euler-derivative part of the `N = 58` CM differential functional. -/
noncomputable def ramanujan58B : ℝ :=
  ramanujan58Scale * 26390

/-- Quartic residual parameter at the `P = 99` double-Pell point. -/
noncomputable def ramanujan58Z : ℝ :=
  1 / (99 : ℝ) ^ 4

/-- The `n`th inverse-period contribution in the normalized `N = 58`
Ramanujan series. -/
abbrev ramanujan58Term (n : ℕ) : ℝ :=
  acceleratorTerm (equalOccupancyReal 4)
    ramanujan58A ramanujan58B ramanujan58Z n

/-- Inverse-period partial sum through degree `M`. -/
abbrev ramanujan58PartialSum (M : ℕ) : ℝ :=
  acceleratorPartialSum (equalOccupancyReal 4)
    ramanujan58A ramanujan58B ramanujan58Z M

/-- Algebraic finite-precision reciprocal of the `N = 58` partial sum. -/
abbrev ramanujan58Precision (M : ℕ) : ℝ :=
  acceleratedPrecision (equalOccupancyReal 4)
    ramanujan58A ramanujan58B ramanujan58Z M

theorem ramanujan58Scale_pos : 0 < ramanujan58Scale := by
  unfold ramanujan58Scale
  positivity

theorem ramanujan58A_pos : 0 < ramanujan58A := by
  unfold ramanujan58A
  positivity

theorem ramanujan58B_pos : 0 < ramanujan58B := by
  unfold ramanujan58B
  positivity

theorem ramanujan58Z_pos : 0 < ramanujan58Z := by
  unfold ramanujan58Z
  positivity

/-- Every transformed `N = 58` coefficient is strictly positive. -/
theorem ramanujan58Term_pos (n : ℕ) : 0 < ramanujan58Term n := by
  change 0 < acceleratorTerm (equalOccupancyReal 4)
    ramanujan58A ramanujan58B ramanujan58Z n
  unfold acceleratorTerm
  have hlinear :
      0 < ramanujan58A + ramanujan58B * (n : ℝ) := by
    exact add_pos_of_pos_of_nonneg ramanujan58A_pos
      (mul_nonneg (le_of_lt ramanujan58B_pos) (Nat.cast_nonneg n))
  exact mul_pos
    (mul_pos hlinear (equalOccupancyReal_pos 4 n (by norm_num)))
    (pow_pos ramanujan58Z_pos n)

/-- Every finite `N = 58` inverse-period partial sum is positive. -/
theorem ramanujan58PartialSum_pos (M : ℕ) :
    0 < ramanujan58PartialSum M := by
  change 0 < acceleratorPartialSum (equalOccupancyReal 4)
    ramanujan58A ramanujan58B ramanujan58Z M
  unfold acceleratorPartialSum
  apply Finset.sum_pos
  · intro n hn
    exact ramanujan58Term_pos n
  · simp

/-- The finite `N = 58` accelerated precision tower is strictly decreasing. -/
theorem strictAnti_ramanujan58Precision :
    StrictAnti ramanujan58Precision := by
  change StrictAnti
    (acceleratedPrecision (equalOccupancyReal 4)
      ramanujan58A ramanujan58B ramanujan58Z)
  exact strictAnti_acceleratedPrecision
    (equalOccupancyReal 4) ramanujan58A ramanujan58B ramanujan58Z
    ramanujan58PartialSum_pos ramanujan58Term_pos

/-- Any verified lower truncation of the exact inverse period yields a finite
`N = 58` precision value strictly above `π`. -/
theorem pi_lt_ramanujan58Precision_of_partial_lt
    (M : ℕ) (hbelow : ramanujan58PartialSum M < 1 / Real.pi) :
    Real.pi < ramanujan58Precision M := by
  exact pi_lt_acceleratedPrecision_of_partial_lt
    (equalOccupancyReal 4) ramanujan58A ramanujan58B ramanujan58Z M
    (ramanujan58PartialSum_pos M) hbelow

/-- The known exact Ramanujan-Sato inverse-period identity, once supplied as a
convergence theorem, forces the finite algebraic reciprocals to converge to
`π`.  This theorem isolates the sequence-theoretic consequence from the
modular construction of the identity. -/
theorem tendsto_ramanujan58Precision_pi
    (hseries : Tendsto ramanujan58PartialSum atTop (𝓝 (1 / Real.pi))) :
    Tendsto ramanujan58Precision atTop (𝓝 Real.pi) := by
  exact tendsto_acceleratedPrecision_pi
    (equalOccupancyReal 4) ramanujan58A ramanujan58B ramanujan58Z hseries

end

end EnterpriseMath.PrecisionPi
