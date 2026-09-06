import EnterpriseMath.Relation.BRCFrameSymmetry
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- Every multiplicative observer of framed path summaries lifts canonically to
an algebra homomorphism on the whole positive-multiplicity BRC.  This is the
reusable observer interface behind weight histograms, geometry erasure and
future valuation/moment observers. -/
noncomputable def observerNBRCAlgHom {W G C M : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] [Monoid M]
    (ρ : CoordinateAction G C)
    (φ : FramedPath W G C ρ →* M) :
    FramedNBRC W G C ρ →ₐ[ℕ] MonoidAlgebra ℕ M :=
  MonoidAlgebra.mapDomainAlgHom ℕ ℕ φ

/-- An atomic branch is sent to one atomic observer bin with unchanged
multiplicity. -/
@[simp] theorem observerNBRCAlgHom_single {W G C M : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] [Monoid M]
    (ρ : CoordinateAction G C)
    (φ : FramedPath W G C ρ →* M)
    (p : FramedPath W G C ρ) (n : ℕ) :
    observerNBRCAlgHom ρ φ (MonoidAlgebra.single p n) =
      MonoidAlgebra.single (φ p) n := by
  simp [observerNBRCAlgHom]

/-- A path observer is frame-invariant when a global change of frame leaves its
value unchanged. -/
def FrameInvariantObserver {W G C M : Type*}
    [Monoid W] [Group G] [AddMonoid C] [Monoid M]
    (ρ : CoordinateAction G C)
    (φ : FramedPath W G C ρ →* M) : Prop :=
  ∀ s p, φ (FramedPath.relabel ρ s p) = φ p

/-- Path-level frame invariance lifts to the entire positive BRC, including
alternative sums and serial convolutions. -/
theorem observerNBRC_relabel {W G C M : Type*}
    [Monoid W] [Group G] [AddMonoid C] [Monoid M]
    (ρ : CoordinateAction G C)
    (φ : FramedPath W G C ρ →* M)
    (hφ : FrameInvariantObserver ρ φ)
    (s : G) (f : FramedNBRC W G C ρ) :
    observerNBRCAlgHom ρ φ ((relabelNBRCAlgEquiv ρ s) f) =
      observerNBRCAlgHom ρ φ f := by
  induction f using MonoidAlgebra.induction_linear with
  | zero => simp
  | add x y hx hy =>
      simp only [map_add, hx, hy]
  | single p n =>
      simp [observerNBRCAlgHom, relabelNBRCAlgEquiv, FramedPath.relabelEquiv,
        hφ s p]

/-- Joint observation before recoalescence.  Keeping the pair as one key retains
correlation between the two observer coordinates instead of replacing it by two
independent marginals. -/
def pairObserverHom {W G C A B : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] [Monoid A] [Monoid B]
    {ρ : CoordinateAction G C}
    (φ : FramedPath W G C ρ →* A)
    (ψ : FramedPath W G C ρ →* B) :
    FramedPath W G C ρ →* A × B where
  toFun p := (φ p, ψ p)
  map_one' := by simp
  map_mul' a b := by simp

/-- The joint path observer exactly recovers its first component. -/
theorem pairObserver_recovers_left {W G C A B : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] [Monoid A] [Monoid B]
    {ρ : CoordinateAction G C}
    (φ : FramedPath W G C ρ →* A)
    (ψ : FramedPath W G C ρ →* B) :
    Recovers (pairObserverHom φ ψ) φ := by
  refine ⟨Prod.fst, ?_⟩
  intro p
  rfl

/-- The joint path observer exactly recovers its second component. -/
theorem pairObserver_recovers_right {W G C A B : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] [Monoid A] [Monoid B]
    {ρ : CoordinateAction G C}
    (φ : FramedPath W G C ρ →* A)
    (ψ : FramedPath W G C ρ →* B) :
    Recovers (pairObserverHom φ ψ) ψ := by
  refine ⟨Prod.snd, ?_⟩
  intro p
  rfl

/-- If a marginal observer merges two paths that the other component separates,
then the marginal cannot recover the joint observer.  This is the precise
NO_RESURRECTION boundary behind the rule that separate marginals need not retain
observer correlation. -/
theorem observer_not_recovers_pair_of_separates {W G C A B : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] [Monoid A] [Monoid B]
    {ρ : CoordinateAction G C}
    (φ : FramedPath W G C ρ →* A)
    (ψ : FramedPath W G C ρ →* B)
    {p q : FramedPath W G C ρ}
    (hφ : φ p = φ q) (hψ : ψ p ≠ ψ q) :
    ¬ Recovers φ (pairObserverHom φ ψ) := by
  intro hrec
  have hpq : pairObserverHom φ ψ p = pairObserverHom φ ψ q :=
    noResurrection hrec hφ
  exact hψ (congrArg Prod.snd hpq)

/-- Frame invariance is closed under joint observation. -/
theorem pairObserver_frameInvariant {W G C A B : Type*}
    [Monoid W] [Group G] [AddMonoid C] [Monoid A] [Monoid B]
    (ρ : CoordinateAction G C)
    (φ : FramedPath W G C ρ →* A)
    (ψ : FramedPath W G C ρ →* B)
    (hφ : FrameInvariantObserver ρ φ)
    (hψ : FrameInvariantObserver ρ ψ) :
    FrameInvariantObserver ρ (pairObserverHom φ ψ) := by
  intro s p
  apply Prod.ext
  · simpa [pairObserverHom] using hφ s p
  · simpa [pairObserverHom] using hψ s p

end EnterpriseMath.BranchRecoalescence
