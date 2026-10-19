import EnterpriseMath.Relation.DeepChamberHighLowCoercivity
import Mathlib.Tactic

namespace EnterpriseMath.DeepChamberNormalizedCascade

/-- Conditional high/low upper envelope for one deepest history-mean packet. -/
def highLowEnvelope (high low₁ low₂ : ℝ) : ℝ :=
  (1 / 2 : ℝ) * high + 2 * (low₁ + low₂)

/-- If all three branch energies lie below one envelope, the conditional mean costs at most `9/2`. -/
theorem highLowEnvelope_le_nine_halves
    {high low₁ low₂ E : ℝ}
    (hhigh : high ≤ E) (hlow₁ : low₁ ≤ E) (hlow₂ : low₂ ≤ E) :
    highLowEnvelope high low₁ low₂ ≤ (9 / 2 : ℝ) * E := by
  unfold highLowEnvelope
  linarith

/--
Exact chamber-normalized contraction: the deepest mass `1/9` turns the
conditional coefficients `(1/2,2,2)` into the strict total coefficient `1/2`.
-/
theorem one_ninth_highLowEnvelope_le_one_half
    {high low₁ low₂ E : ℝ}
    (hhigh : high ≤ E) (hlow₁ : low₁ ≤ E) (hlow₂ : low₂ ≤ E) :
    (1 / 9 : ℝ) * highLowEnvelope high low₁ low₂ ≤
      (1 / 2 : ℝ) * E := by
  have henv := highLowEnvelope_le_nine_halves hhigh hlow₁ hlow₂
  have hscale :
      (1 / 9 : ℝ) * highLowEnvelope high low₁ low₂ ≤
        (1 / 9 : ℝ) * ((9 / 2 : ℝ) * E) :=
    mul_le_mul_of_nonneg_left henv (by norm_num)
  convert hscale using 1 <;> ring

/-- A conditional mean bound inherits the same exact normalized contraction. -/
theorem one_ninth_mean_le_one_half
    {mean high low₁ low₂ E : ℝ}
    (hmean : mean ≤ highLowEnvelope high low₁ low₂)
    (hhigh : high ≤ E) (hlow₁ : low₁ ≤ E) (hlow₂ : low₂ ≤ E) :
    (1 / 9 : ℝ) * mean ≤ (1 / 2 : ℝ) * E := by
  calc
    (1 / 9 : ℝ) * mean ≤
        (1 / 9 : ℝ) * highLowEnvelope high low₁ low₂ :=
      mul_le_mul_of_nonneg_left hmean (by norm_num)
    _ ≤ (1 / 2 : ℝ) * E :=
      one_ninth_highLowEnvelope_le_one_half hhigh hlow₁ hlow₂

/--
Finite chamber-mass slack.  If the normalized deepest mass is at most
`1/9 + eps`, the strict coefficient is `1/2 + (9/2) eps`.
-/
theorem slack_mass_mean_cascade
    {mass eps mean high low₁ low₂ E : ℝ}
    (heps : 0 ≤ eps)
    (hmass : mass ≤ (1 / 9 : ℝ) + eps)
    (hmean0 : 0 ≤ mean)
    (hmean : mean ≤ highLowEnvelope high low₁ low₂)
    (hhigh : high ≤ E) (hlow₁ : low₁ ≤ E) (hlow₂ : low₂ ≤ E) :
    mass * mean ≤
      ((1 / 2 : ℝ) + (9 / 2 : ℝ) * eps) * E := by
  have henv := highLowEnvelope_le_nine_halves hhigh hlow₁ hlow₂
  have hmeanE : mean ≤ (9 / 2 : ℝ) * E := hmean.trans henv
  have hcoef : 0 ≤ (1 / 9 : ℝ) + eps := by positivity
  calc
    mass * mean ≤ ((1 / 9 : ℝ) + eps) * mean :=
      mul_le_mul_of_nonneg_right hmass hmean0
    _ ≤ ((1 / 9 : ℝ) + eps) * ((9 / 2 : ℝ) * E) :=
      mul_le_mul_of_nonneg_left hmeanE hcoef
    _ = ((1 / 2 : ℝ) + (9 / 2 : ℝ) * eps) * E := by ring

/-- The limiting normalized coefficient is strictly below one whenever `eps < 1/9`. -/
theorem slack_coefficient_lt_one
    {eps : ℝ} (heps : eps < 1 / 9) :
    (1 / 2 : ℝ) + (9 / 2 : ℝ) * eps < 1 := by
  linarith

end EnterpriseMath.DeepChamberNormalizedCascade
