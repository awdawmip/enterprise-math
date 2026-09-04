import EnterpriseMath.Relation.DeepChamberColorNoGo
import Mathlib.Tactic

namespace EnterpriseMath.DeepChamberColorBalance

/-- A colored lower-scale kernel is balanced when all three color fibers have equal mass. -/
def BalancedKernel (κ : Fin 3 → ℕ → ℝ) : Prop :=
  ∀ m i j, κ i m = κ j m

/-- A three-color observable belongs to the standard sector when its coordinate sum is zero. -/
def IsStandardColor (h : Fin 3 → ℝ) : Prop :=
  h 0 + h 1 + h 2 = 0

/-- Scalarization of one colored endpoint fiber against a color observable. -/
def scalarizeColor (κ : Fin 3 → ℕ → ℝ) (h : Fin 3 → ℝ) (m : ℕ) : ℝ :=
  κ 0 m * h 0 + κ 1 m * h 1 + κ 2 m * h 2

/-- A balanced colored kernel annihilates every standard color observable pointwise. -/
theorem scalarizeColor_eq_zero_of_balanced
    (κ : Fin 3 → ℕ → ℝ) (h : Fin 3 → ℝ)
    (hκ : BalancedKernel κ) (hstd : IsStandardColor h) (m : ℕ) :
    scalarizeColor κ h m = 0 := by
  unfold scalarizeColor BalancedKernel IsStandardColor at *
  rw [hκ m 1 0, hκ m 2 0]
  calc
    κ 0 m * h 0 + κ 0 m * h 1 + κ 0 m * h 2 =
        κ 0 m * (h 0 + h 1 + h 2) := by ring
    _ = 0 := by rw [hstd, mul_zero]

/-- Colored quadratic energy on one endpoint fiber. -/
def colorEnergy (κ : Fin 3 → ℕ → ℝ) (h : Fin 3 → ℝ) (m : ℕ) : ℝ :=
  κ 0 m * (h 0) ^ 2 + κ 1 m * (h 1) ^ 2 + κ 2 m * (h 2) ^ 2

/-- Under fiberwise balance, color energy factors into endpoint mass and the standard norm. -/
theorem colorEnergy_eq_of_balanced
    (κ : Fin 3 → ℕ → ℝ) (h : Fin 3 → ℝ)
    (hκ : BalancedKernel κ) (m : ℕ) :
    colorEnergy κ h m =
      κ 0 m * ((h 0) ^ 2 + (h 1) ^ 2 + (h 2) ^ 2) := by
  unfold colorEnergy BalancedKernel at *
  rw [hκ m 1 0, hκ m 2 0]
  ring

/-- Forgetting the color preserves scalar mass but kills the standard amplitude. -/
theorem balanced_scalar_mass_and_standard_loss
    (κ : Fin 3 → ℕ → ℝ) (h : Fin 3 → ℝ)
    (hκ : BalancedKernel κ) (hstd : IsStandardColor h) (m : ℕ) :
    (κ 0 m + κ 1 m + κ 2 m = 3 * κ 0 m) ∧
      scalarizeColor κ h m = 0 := by
  constructor
  · unfold BalancedKernel at hκ
    rw [hκ m 1 0, hκ m 2 0]
    ring
  · exact scalarizeColor_eq_zero_of_balanced κ h hκ hstd m

/-- The concrete color vector `(1,-1,0)` is standard. -/
theorem standardColorVector_isStandard :
    IsStandardColor
      (fun i : Fin 3 => if i = 0 then 1 else if i = 1 then -1 else 0) := by
  norm_num [IsStandardColor]

end EnterpriseMath.DeepChamberColorBalance
