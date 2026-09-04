import EnterpriseMath.Relation.WeightedRelationMixer
import EnterpriseMath.Relation.PrimeWindingStirlingChambers
import Mathlib.Tactic

namespace EnterpriseMath.S3StirlingIntertwiner

open EnterpriseMath.WeightedCoefficientCoercivity
open EnterpriseMath.WeightedRelationMixer
open EnterpriseMath.PrimeWindingStirlingChambers

/-- The normalized deepest degree-three chamber coefficient is `1/9` over `ℝ`. -/
theorem degreeThree_deep_fraction_real :
    (deficiencyChamberCount 3 2 : ℝ) / (3 ^ 3 : ℝ) = 1 / 9 := by
  norm_num [deficiencyChamberCount, imageChamberCount, Nat.stirlingSecond]

/--
The exact quadratic survival coefficient of the global weighted `S_3` mixer
is the normalized deepest Stirling cutoff-chamber mass.
-/
theorem weightedS3_energy_eq_deep_chamber_fraction
    {ι : Type*} (S : Finset ι) (u value : ι → ℝ) (mean : ℝ) :
    weightedPairEnergy S u (s3ValueMixer mean value) =
      ((deficiencyChamberCount 3 2 : ℝ) / (3 ^ 3 : ℝ)) *
        weightedPairEnergy S u value := by
  rw [weightedPairEnergy_s3Mix, degreeThree_deep_fraction_real]

/-- The three deepest chamber components are indexed by the unique uncut slot. -/
abbrev DeepChamberIndex := Fin 3

/-- The three constant maps are indexed by their unique image label. -/
abbrev ConstantMapIndex := Fin 3

/-- Canonical `S_3`-equivariant index correspondence. -/
def deepToConstant : DeepChamberIndex ≃ ConstantMapIndex :=
  Equiv.refl _

@[simp] theorem deepToConstant_apply (i : DeepChamberIndex) :
    deepToConstant i = i := rfl

end EnterpriseMath.S3StirlingIntertwiner
