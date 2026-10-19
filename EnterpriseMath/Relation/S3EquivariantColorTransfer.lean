import EnterpriseMath.Relation.DeepChamberColorBalance
import EnterpriseMath.Relation.WeightedRelationMixer
import Mathlib.Tactic

namespace EnterpriseMath.S3EquivariantColorTransfer

open EnterpriseMath.DeepChamberColorBalance
open EnterpriseMath.WeightedRelationMixer

noncomputable section

/-- Sum of the three color coordinates. -/
def colorSum (h : Fin 3 → ℝ) : ℝ :=
  h 0 + h 1 + h 2

/--
Canonical two-parameter `S_3`-equivariant color transfer: diagonal coefficient
`diag` and common off-diagonal coefficient `off`.
-/
def colorTransfer (diag off : ℝ) (h : Fin 3 → ℝ) (i : Fin 3) : ℝ :=
  (diag - off) * h i + off * colorSum h

/-- Pair differences see only the standard eigenvalue `diag-off`. -/
theorem colorTransfer_sub
    (diag off : ℝ) (h : Fin 3 → ℝ) (i j : Fin 3) :
    colorTransfer diag off h i - colorTransfer diag off h j =
      (diag - off) * (h i - h j) := by
  unfold colorTransfer
  ring

/-- The trivial color line has eigenvalue `diag+2*off`. -/
theorem colorSum_colorTransfer
    (diag off : ℝ) (h : Fin 3 → ℝ) :
    colorSum (colorTransfer diag off h) =
      (diag + 2 * off) * colorSum h := by
  unfold colorSum colorTransfer
  ring

/-- Every standard color vector is an eigenvector with eigenvalue `diag-off`. -/
theorem colorTransfer_standard
    (diag off : ℝ) (h : Fin 3 → ℝ)
    (hstd : IsStandardColor h) :
    colorTransfer diag off h = fun i => (diag - off) * h i := by
  have hzero : colorSum h = 0 := by
    simpa [colorSum, IsStandardColor] using hstd
  funext i
  unfold colorTransfer
  rw [hzero, mul_zero, add_zero]

/-- The standard sector is invariant under every equivariant color transfer. -/
theorem colorTransfer_preserves_standard
    (diag off : ℝ) (h : Fin 3 → ℝ)
    (hstd : IsStandardColor h) :
    IsStandardColor (colorTransfer diag off h) := by
  have hzero : colorSum h = 0 := by
    simpa [colorSum, IsStandardColor] using hstd
  have hout : colorSum (colorTransfer diag off h) = 0 := by
    rw [colorSum_colorTransfer, hzero, mul_zero]
  simpa [colorSum, IsStandardColor] using hout

/-- Complete pair energy on the three-color fiber. -/
def colorPairEnergy (h : Fin 3 → ℝ) : ℝ :=
  (h 0 - h 1) ^ 2 + (h 1 - h 2) ^ 2 + (h 2 - h 0) ^ 2

/-- Equivariant color transfer scales standard pair energy by `(diag-off)^2`. -/
theorem colorPairEnergy_colorTransfer
    (diag off : ℝ) (h : Fin 3 → ℝ) :
    colorPairEnergy (colorTransfer diag off h) =
      (diag - off) ^ 2 * colorPairEnergy h := by
  unfold colorPairEnergy
  rw [colorTransfer_sub, colorTransfer_sub, colorTransfer_sub]
  ring

/-- Markov normalization fixes every constant color channel. -/
theorem colorTransfer_constant_of_markov
    (diag off c : ℝ) (hmarkov : diag + 2 * off = 1) :
    colorTransfer diag off (fun _ : Fin 3 => c) = fun _ => c := by
  funext i
  unfold colorTransfer colorSum
  calc
    (diag - off) * c + off * (c + c + c) =
        (diag + 2 * off) * c := by ring
    _ = c := by rw [hmarkov, one_mul]

/-- The global weighted `S_3` lift--project mixer has diagonal/off-diagonal weights `5/9,2/9`. -/
theorem colorTransfer_five_ninth_two_ninth_eq_s3Mixer
    (h : Fin 3 → ℝ) :
    colorTransfer (5 / 9 : ℝ) (2 / 9 : ℝ) h =
      s3ValueMixer (colorSum h / 3) h := by
  funext i
  unfold colorTransfer colorSum s3ValueMixer
  ring

/-- The `S_3` lift--project color kernel is Markov normalized. -/
theorem five_ninth_two_ninth_markov :
    (5 / 9 : ℝ) + 2 * (2 / 9 : ℝ) = 1 := by
  norm_num

/-- Its standard eigenvalue is exactly `1/3`. -/
theorem five_ninth_two_ninth_standard_eigenvalue :
    (5 / 9 : ℝ) - (2 / 9 : ℝ) = 1 / 3 := by
  norm_num

/-- Its quadratic standard energy survival is exactly `1/9`. -/
theorem five_ninth_two_ninth_energy_survival :
    ((5 / 9 : ℝ) - (2 / 9 : ℝ)) ^ 2 = 1 / 9 := by
  ring

end

end EnterpriseMath.S3EquivariantColorTransfer
