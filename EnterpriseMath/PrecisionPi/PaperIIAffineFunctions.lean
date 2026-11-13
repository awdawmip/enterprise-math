import EnterpriseMath.PrecisionPi.PaperIIResidualCocycleV1

namespace EnterpriseMath.PrecisionPi.PaperIIAffineFunctions

open EnterpriseMath.PrecisionPi.PaperIIKernelV1 (SliceChart)
open EnterpriseMath.PrecisionPi.PaperIIK4RotationV1 (SlicePair)
open EnterpriseMath.PrecisionPi.PaperIIResidualCocycleV1

abbrev F := ZMod 2
abbrev Point := F × F

/-- A scalar function is affine exactly when subtracting its value at the origin
makes it additive. Over the prime field of order two this is also linearity. -/
def IsAffine (f : Point → F) : Prop :=
  ∀ u v : Point, f (u + v) = f u + f v - f 0

instance (f : Point → F) : Decidable (IsAffine f) := by
  unfold IsAffine
  infer_instance

/-- The function space itself, closed under pointwise linear operations. -/
def affineFunctions : Submodule F (Point → F) where
  carrier := {f | IsAffine f}
  zero_mem' := by change IsAffine 0; native_decide
  add_mem' := by
    intro f g hf hg
    exact (show ∀ f g : Point → F, IsAffine f → IsAffine g → IsAffine (f + g) by
      native_decide) f g hf hg
  smul_mem' := by
    intro a f hf
    exact (show ∀ (a : F) (f : Point → F), IsAffine f → IsAffine (a • f) by
      native_decide) a f hf

def evaluate (c : ResidualF2) (z : Point) : F :=
  c.2 + c.1.1 * z.1 + c.1.2 * z.2

def coefficients (f : Point → F) : ResidualF2 :=
  ((f (1, 0) - f 0, f (0, 1) - f 0), f 0)

theorem evaluate_is_affine : ∀ c : ResidualF2, IsAffine (evaluate c) := by
  native_decide

theorem coefficients_evaluate : ∀ c : ResidualF2, coefficients (evaluate c) = c := by
  native_decide

theorem evaluate_coefficients :
    ∀ f : Point → F, IsAffine f → evaluate (coefficients f) = f := by
  native_decide

/-- The manuscript equivalence, linear for the actual residual coordinates of
the previously checked cocycle module. The inverse uses three evaluations. -/
def residualEquiv : ResidualF2 ≃ₗ[F] affineFunctions where
  toFun c := ⟨evaluate c, evaluate_is_affine c⟩
  invFun f := coefficients f.val
  left_inv := coefficients_evaluate
  right_inv f := Subtype.ext (evaluate_coefficients f.val f.property)
  map_add' a b := Subtype.ext
    ((show ∀ c d : ResidualF2, evaluate (c + d) = evaluate c + evaluate d by native_decide) a b)
  map_smul' a b := Subtype.ext
    ((show ∀ (k : F) (c : ResidualF2), evaluate (k • c) = k • evaluate c by native_decide) a b)

/-- Vertices A,B,C,D in the manuscript's order. -/
def pointOf : SliceChart → Point := ![(0, 0), (1, 0), (0, 1), (1, 1)]

def chartOf (z : Point) : SliceChart :=
  if z.2 = 0 then (if z.1 = 0 then 0 else 1) else (if z.1 = 0 then 2 else 3)

def vertexEquiv : SliceChart ≃ Point where
  toFun := pointOf
  invFun := chartOf
  left_inv := by native_decide
  right_inv := by native_decide

/-- Precomposition after transporting a vertex map to the affine plane. -/
def pullback (g : SliceChart → SliceChart) (f : Point → F) (z : Point) : F :=
  f (pointOf (g (chartOf z)))

theorem affine_of_relabelling :
    ∀ g : SliceChart → SliceChart, Function.Injective g →
      ∀ f : Point → F, IsAffine f → IsAffine (pullback g f) := by
  native_decide

def relabel (σ : Equiv.Perm SliceChart) (c : ResidualF2) : ResidualF2 :=
  coefficients (pullback σ.symm (evaluate c))

/-- All vertex permutations act by inverse precomposition on the represented
affine functions. The three identities below identify this full action with
the previously checked generators. -/
theorem equivariant (σ : Equiv.Perm SliceChart) (c : ResidualF2) :
    evaluate (relabel σ c) = pullback σ.symm (evaluate c) :=
  evaluate_coefficients _ (affine_of_relabelling _ σ.symm.injective _ (evaluate_is_affine c))

theorem relabel_identity (c : ResidualF2) : relabel (Equiv.refl SliceChart) c = c := by
  exact (show ∀ d : ResidualF2, relabel (Equiv.refl SliceChart) d = d by native_decide) c

theorem relabel_composition (σ τ : Equiv.Perm SliceChart) (c : ResidualF2) :
    relabel (σ.trans τ) c = relabel τ (relabel σ c) := by
  change coefficients _ = coefficients _
  congr 1
  funext z
  change evaluate c (pointOf (σ.symm (τ.symm (chartOf z)))) =
    evaluate (relabel σ c) (pointOf (τ.symm (chartOf z)))
  rw [equivariant]
  change evaluate c (pointOf (σ.symm (τ.symm (chartOf z)))) =
    evaluate c (pointOf (σ.symm (chartOf (pointOf (τ.symm (chartOf z))))))
  rw [show chartOf (pointOf (τ.symm (chartOf z))) = τ.symm (chartOf z) from
    vertexEquiv.left_inv _]

theorem certified_generators :
    (∀ c : ResidualF2, relabel (Equiv.swap 0 1) c = action01F2 c) ∧
    (∀ c : ResidualF2, relabel (Equiv.swap 1 2) c = action12F2 c) ∧
    (∀ c : ResidualF2, relabel (Equiv.swap 2 3) c = action23F2 c) := by
  native_decide

def support (c : ResidualF2) : Finset SliceChart :=
  Finset.univ.filter fun v => evaluate c (pointOf v) = 1

theorem support_relabel (σ : Equiv.Perm SliceChart) (c : ResidualF2) :
    support (relabel σ c) = (support c).map σ.toEmbedding := by
  ext v
  simp only [support, Finset.mem_filter, Finset.mem_univ, true_and, equivariant, pullback]
  change (evaluate c (pointOf (σ.symm (chartOf (pointOf v)))) = 1) ↔ _
  rw [show chartOf (pointOf v) = v from vertexEquiv.left_inv v]
  constructor
  · intro hv
    exact Finset.mem_map.mpr ⟨σ.symm v, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hv⟩,
      σ.apply_symm_apply v⟩
  · intro hv
    obtain ⟨w, hw, he⟩ := Finset.mem_map.mp hv
    change σ w = v at he
    subst v
    rw [σ.symm_apply_apply]
    exact (Finset.mem_filter.mp hw).2

theorem degree_classifies_support :
    ∀ c : ResidualF2, (support c).card = 2 ↔ c.1 ≠ 0 := by
  native_decide

/-- The nonconstant residual classes are exactly the six edges of this K₄.
The codomain is the unordered-pair type of the existing carrier development. -/
def edgeOf (c : {c : ResidualF2 // c.1 ≠ 0}) : SlicePair :=
  ⟨support c.val, (degree_classifies_support c.val).2 c.property⟩

theorem edgeOf_bijective : Function.Bijective edgeOf := by native_decide

theorem torsion_exchanges_opposite_edges :
    ∀ c : ResidualF2, support (c + torsionF2) = (support c)ᶜ := by
  native_decide

end EnterpriseMath.PrecisionPi.PaperIIAffineFunctions
