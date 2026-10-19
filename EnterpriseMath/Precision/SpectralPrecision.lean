import Mathlib

namespace EnterpriseMath.Precision

/-- The exact two-to-one even-site spectral decimation polynomial from #1159. -/
def spectralDecimation (u : ℝ) : ℝ :=
  u * (4 - u)

/--
WSR-L01: eliminating the odd sites in the second-order Dirichlet recurrence
produces the coarse recurrence with spectral parameter `u * (4-u)`.

This is a local algebraic theorem. It uses no trigonometric function, circle,
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
characteristic recurrence. Keeping the recursion explicit makes the finite
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

/-- The recurrence-level form of `det L_M^D = M` used by the later matrix bridge. -/
theorem dirichletContinuant_zero_pred (M : ℕ) (hM : 1 ≤ M) :
    dirichletContinuant 0 (M - 1) = (M : ℝ) := by
  simpa [Nat.sub_add_cancel hM] using dirichletContinuant_zero (M - 1)

end EnterpriseMath.Precision
