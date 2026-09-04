import EnterpriseMath.Relation.WeightedQuotientRelationField
import Mathlib.Tactic

namespace EnterpriseMath.S3ProvenanceMixer

noncomputable section

/-- Mean of the three first-action readout classes in one `3!` history fiber. -/
def mean3 (x y z : ℝ) : ℝ :=
  (x + y + z) / 3

/-- The induced first-class action of uniform averaging over the three transpositions. -/
def mixer3 (x y z : ℝ) : ℝ × ℝ × ℝ :=
  (mean3 x y z, mean3 x y z, mean3 x y z)

/-- Each first slot sees the three labels exactly once under the three transpositions. -/
theorem transpositionAverage_first_x (x y z : ℝ) :
    (y + z + x) / 3 = mean3 x y z := by
  unfold mean3
  ring

/-- Each first slot sees the three labels exactly once under the three transpositions. -/
theorem transpositionAverage_first_y (x y z : ℝ) :
    (x + z + y) / 3 = mean3 x y z := by
  unfold mean3
  ring

/-- Each first slot sees the three labels exactly once under the three transpositions. -/
theorem transpositionAverage_first_z (x y z : ℝ) :
    (x + y + z) / 3 = mean3 x y z := by
  rfl

/-- The mixer preserves the total first-class readout. -/
theorem mixer3_preserves_sum (x y z : ℝ) :
    (mixer3 x y z).1 + (mixer3 x y z).2.1 + (mixer3 x y z).2.2 =
      x + y + z := by
  unfold mixer3 mean3
  ring

/-- Uniform first-class states are fixed. -/
@[simp] theorem mixer3_uniform (x : ℝ) :
    mixer3 x x x = (x, x, x) := by
  unfold mixer3 mean3
  ext <;> ring

/-- The transposition mixer is an exact one-step projection. -/
theorem mixer3_idempotent (x y z : ℝ) :
    let out := mixer3 x y z
    mixer3 out.1 out.2.1 out.2.2 = out := by
  dsimp
  unfold mixer3 mean3
  ext <;> ring

/-- Standard-sector energy of the three distinct first-action classes. -/
def centeredEnergy3 (x y z : ℝ) : ℝ :=
  (x - mean3 x y z) ^ 2 +
    (y - mean3 x y z) ^ 2 +
    (z - mean3 x y z) ^ 2

/-- Complete pairwise energy of the three first-action classes. -/
def pairEnergy3 (x y z : ℝ) : ℝ :=
  (x - y) ^ 2 + (y - z) ^ 2 + (z - x) ^ 2

/-- Three-point variance is one third of the complete pairwise energy. -/
theorem centeredEnergy3_eq_pairEnergy3_div_three (x y z : ℝ) :
    centeredEnergy3 x y z = pairEnergy3 x y z / 3 := by
  unfold centeredEnergy3 pairEnergy3 mean3
  ring

/-- In the six ordered histories each first-action class occurs twice. -/
def sixHistoryStandardEnergy (x y z : ℝ) : ℝ :=
  2 * centeredEnergy3 x y z

/-- Exact standard-sector norm on the `3!` history fiber. -/
theorem sixHistoryStandardEnergy_eq_two_thirds_pairEnergy3
    (x y z : ℝ) :
    sixHistoryStandardEnergy x y z = 2 * pairEnergy3 x y z / 3 := by
  rw [sixHistoryStandardEnergy, centeredEnergy3_eq_pairEnergy3_div_three]
  ring

/-- The gap-one mixer dissipates the complete six-history standard energy. -/
theorem mixer3_gap_one_dissipation (x y z : ℝ) :
    sixHistoryStandardEnergy x y z =
      2 * ((x - (mixer3 x y z).1) ^ 2 +
        (y - (mixer3 x y z).2.1) ^ 2 +
        (z - (mixer3 x y z).2.2) ^ 2) := by
  rfl

/-- After one mixer step every internal capacity-weighted relation vanishes. -/
theorem mixer3_relationField_zero
    (mass : Fin 3 → ℝ) (x y z : ℝ) (i j : Fin 3) :
    let m := mean3 x y z
    EnterpriseMath.WeightedQuotientRelationField.relationField
      mass
      (EnterpriseMath.WeightedQuotientRelationField.uniformTotal mass m)
      i j = 0 := by
  simp

end

end EnterpriseMath.S3ProvenanceMixer
