import EnterpriseMath.Relation.BRCObserverAlgebra

namespace EnterpriseMath.BranchRecoalescence

namespace FramedPath

variable {W G C : Type*} [Monoid W] [Monoid G] [AddMonoid C]
variable (ρ : CoordinateAction G C)

/-- Exact branch weight is a multiplicative observer of framed path composition. -/
def weightHom : FramedPath W G C ρ →* W where
  toFun := FramedPath.weight
  map_one' := rfl
  map_mul' _ _ := rfl

@[simp] theorem weightHom_apply (p : FramedPath W G C ρ) :
    weightHom ρ p = p.weight := rfl

end FramedPath

/-- Exact finite weight histogram.  In the canonical positive-rational
instantiation this is the `N[Q_{>0}^×]` carrier used by Weighted-BRC. -/
abbrev WeightHistogram (W : Type*) [Monoid W] := MonoidAlgebra ℕ W

/-- Forget coordinate/frame/length but preserve exact branch weight and
multiplicity.  This is the exact-weight specialization of the generic framed
observer algebra. -/
noncomputable def weightHistogramAlgHom {W G C : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] (ρ : CoordinateAction G C) :
    FramedNBRC W G C ρ →ₐ[ℕ] WeightHistogram W :=
  observerNBRCAlgHom ρ (FramedPath.weightHom (W := W) ρ)

/-- Atomic framed branches map to atomic histogram bins with unchanged
multiplicity. -/
@[simp] theorem weightHistogramAlgHom_single {W G C : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] (ρ : CoordinateAction G C)
    (p : FramedPath W G C ρ) (n : ℕ) :
    weightHistogramAlgHom ρ (MonoidAlgebra.single p n) =
      MonoidAlgebra.single p.weight n := by
  simpa [weightHistogramAlgHom] using
    (observerNBRCAlgHom_single ρ (FramedPath.weightHom (W := W) ρ) p n)

/-- Exact branch weight is frame-invariant at path level. -/
theorem weightHom_frameInvariant {W G C : Type*}
    [Monoid W] [Group G] [AddMonoid C]
    (ρ : CoordinateAction G C) :
    FrameInvariantObserver ρ (FramedPath.weightHom (W := W) ρ) := by
  intro _s _p
  rfl

/-- Global frame relabeling leaves exact branch weight unchanged at path level. -/
@[simp] theorem weight_relabel {W G C : Type*}
    [Monoid W] [Group G] [AddMonoid C] (ρ : CoordinateAction G C)
    (s : G) (p : FramedPath W G C ρ) :
    (FramedPath.relabel ρ s p).weight = p.weight := rfl

/-- The exact-weight histogram observer is rotation/frame invariant on the whole
positive BRC.  This is the formal bridge from coordinate-rich framed BRC to the
existing Weighted-BRC histogram layer. -/
theorem weightHistogram_relabel {W G C : Type*}
    [Monoid W] [Group G] [AddMonoid C] (ρ : CoordinateAction G C)
    (s : G) (f : FramedNBRC W G C ρ) :
    weightHistogramAlgHom ρ ((relabelNBRCAlgEquiv ρ s) f) =
      weightHistogramAlgHom ρ f := by
  exact observerNBRC_relabel ρ (FramedPath.weightHom (W := W) ρ)
    (weightHom_frameInvariant (W := W) ρ) s f

end EnterpriseMath.BranchRecoalescence
