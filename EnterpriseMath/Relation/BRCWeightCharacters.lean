import EnterpriseMath.Relation.BRCWeightHistogram
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- Every multiplicative character on exact branch weights extends uniquely to a
semiring/algebra readout of the exact finite weight histogram.  This is the
formal universal-property layer behind count, total mass and power moments. -/
noncomputable def histogramCharacter {W R : Type*}
    [Monoid W] [Semiring R] (χ : W →* R) :
    WeightHistogram W →ₐ[ℕ] R :=
  MonoidAlgebra.lift ℕ R W χ

/-- A histogram character evaluates one exact weight bin as multiplicity times
the character value of that weight. -/
@[simp] theorem histogramCharacter_single {W R : Type*}
    [Monoid W] [Semiring R] (χ : W →* R)
    (w : W) (n : ℕ) :
    histogramCharacter χ (MonoidAlgebra.single w n) = n • χ w := by
  simp [histogramCharacter]

/-- Compose a weight character with the framed-to-histogram observer.  This
provides the same readout directly on coordinate-rich framed N-BRC states. -/
noncomputable def framedWeightCharacter {W G C R : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] [Semiring R]
    (ρ : CoordinateAction G C) (χ : W →* R) :
    FramedNBRC W G C ρ →ₐ[ℕ] R :=
  (histogramCharacter χ).comp (weightHistogramAlgHom ρ)

/-- Atomic framed branches evaluate exactly as their multiplicity times the
chosen weight character. -/
@[simp] theorem framedWeightCharacter_single {W G C R : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] [Semiring R]
    (ρ : CoordinateAction G C) (χ : W →* R)
    (p : FramedPath W G C ρ) (n : ℕ) :
    framedWeightCharacter ρ χ (MonoidAlgebra.single p n) = n • χ p.weight := by
  simp [framedWeightCharacter]

/-- The constant-one multiplicative character counts supported branch
multiplicity, with exact recoalescence multiplicity retained by the outer
natural coefficient. -/
def countCharacter (W : Type*) [Monoid W] : W →* ℕ where
  toFun := fun _ => 1
  map_one' := rfl
  map_mul' _ _ := rfl

/-- Exact histogram branch-count readout. -/
noncomputable def histogramCount {W : Type*} [Monoid W] :
    WeightHistogram W →ₐ[ℕ] ℕ :=
  histogramCharacter (countCharacter W)

@[simp] theorem histogramCount_single {W : Type*} [Monoid W]
    (w : W) (n : ℕ) :
    histogramCount (MonoidAlgebra.single w n) = n := by
  simp [histogramCount, countCharacter]

/-- For a commutative semiring used simultaneously as exact weight carrier and
readout carrier, the m-th power character yields the exact m-th power-sum
moment.  In the positive-rational instantiation this is Weighted-BRC `P_m`. -/
noncomputable def histogramPowerMoment {R : Type*} [CommSemiring R] (m : ℕ) :
    WeightHistogram R →ₐ[ℕ] R :=
  histogramCharacter (powMonoidHom m : R →* R)

@[simp] theorem histogramPowerMoment_single {R : Type*} [CommSemiring R]
    (m : ℕ) (q : R) (n : ℕ) :
    histogramPowerMoment m (MonoidAlgebra.single q n) = n • q ^ m := by
  simp [histogramPowerMoment]

/-- Zeroth power moment is the exact multiplicity readout on every atomic bin. -/
@[simp] theorem histogramPowerMoment_zero_single {R : Type*} [CommSemiring R]
    (q : R) (n : ℕ) :
    histogramPowerMoment 0 (MonoidAlgebra.single q n) = n • (1 : R) := by
  simp

/-- First power moment is the exact total-mass contribution of one atomic bin. -/
@[simp] theorem histogramPowerMoment_one_single {R : Type*} [CommSemiring R]
    (q : R) (n : ℕ) :
    histogramPowerMoment 1 (MonoidAlgebra.single q n) = n • q := by
  simp

/-- Global frame relabeling does not change any readout that factors only through
exact branch weight. -/
theorem framedWeightCharacter_relabel {W G C R : Type*}
    [Monoid W] [Group G] [AddMonoid C] [Semiring R]
    (ρ : CoordinateAction G C) (χ : W →* R)
    (s : G) (f : FramedNBRC W G C ρ) :
    framedWeightCharacter ρ χ ((relabelNBRCAlgEquiv ρ s) f) =
      framedWeightCharacter ρ χ f := by
  unfold framedWeightCharacter
  rw [weightHistogram_relabel]

end EnterpriseMath.BranchRecoalescence
