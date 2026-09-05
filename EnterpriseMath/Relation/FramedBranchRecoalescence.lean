import EnterpriseMath.Relation.BranchRecoalescence
import Mathlib.Algebra.MonoidAlgebra.Defs
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- A typed action of a frame monoid on an additive coordinate carrier.

This is deliberately weaker than a linear representation.  BRC only needs the
laws required to transport a later coordinate increment through the frame left
by an earlier path. -/
structure CoordinateAction (G C : Type*) [Monoid G] [AddMonoid C] where
  act : G → C → C
  one_act : ∀ x, act 1 x = x
  mul_act : ∀ g h x, act (g * h) x = act g (act h x)
  act_zero : ∀ g, act g 0 = 0
  act_add : ∀ g x y, act g (x + y) = act g x + act g y

/-- A composable BRC path summary retaining weight, coordinate content, frame,
and raw operation length.

The outer `ℕ` coefficient used below records multiplicity of identical summaries;
therefore `weight` remains part of the path key instead of being silently summed
away. -/
structure FramedPath (W G C : Type*) [Monoid W] [Monoid G] [AddMonoid C]
    (ρ : CoordinateAction G C) where
  weight : W
  coord : C
  frame : G
  length : Nat

namespace FramedPath

variable {W G C : Type*} [Monoid W] [Monoid G] [AddMonoid C]
variable (ρ : CoordinateAction G C)

/-- Empty framed path. -/
def onePath : FramedPath W G C ρ :=
  ⟨1, 0, 1, 0⟩

/-- Ordered concatenation.  The second coordinate increment is first transported
through the frame left by the first path. -/
def mulPath (a b : FramedPath W G C ρ) : FramedPath W G C ρ :=
  ⟨a.weight * b.weight,
    a.coord + ρ.act a.frame b.coord,
    a.frame * b.frame,
    a.length + b.length⟩

/-- The framed path summaries form a monoid.  This is the algebraic core of the
semidirect BRC composition `(w,n,g,l)(v,m,h,k)=(wv,n+g·m,gh,l+k)`. -/
instance instMonoid : Monoid (FramedPath W G C ρ) where
  one := onePath ρ
  mul := mulPath ρ
  one_mul a := by
    cases a
    simp [onePath, mulPath, ρ.one_act]
  mul_one a := by
    cases a
    simp [onePath, mulPath, ρ.act_zero]
  mul_assoc a b c := by
    cases a
    cases b
    cases c
    simp [mulPath, ρ.mul_act, ρ.act_add, mul_assoc, add_assoc]

@[simp] theorem weight_one :
    (1 : FramedPath W G C ρ).weight = 1 := rfl

@[simp] theorem coord_one :
    (1 : FramedPath W G C ρ).coord = 0 := rfl

@[simp] theorem frame_one :
    (1 : FramedPath W G C ρ).frame = 1 := rfl

@[simp] theorem length_one :
    (1 : FramedPath W G C ρ).length = 0 := rfl

@[simp] theorem weight_mul (a b : FramedPath W G C ρ) :
    (a * b).weight = a.weight * b.weight := rfl

@[simp] theorem coord_mul (a b : FramedPath W G C ρ) :
    (a * b).coord = a.coord + ρ.act a.frame b.coord := rfl

@[simp] theorem frame_mul (a b : FramedPath W G C ρ) :
    (a * b).frame = a.frame * b.frame := rfl

@[simp] theorem length_mul (a b : FramedPath W G C ρ) :
    (a * b).length = a.length + b.length := rfl

end FramedPath

/-- The observer that deliberately forgets all coordinate and frame information
but retains multiplicative weight and additive operation length. -/
structure WeightLength (W : Type*) [Monoid W] where
  weight : W
  length : Nat

namespace WeightLength

variable {W : Type*} [Monoid W]

/-- Componentwise serial composition of the geometry-erased observer. -/
instance instMonoid : Monoid (WeightLength W) where
  one := ⟨1, 0⟩
  mul a b := ⟨a.weight * b.weight, a.length + b.length⟩
  one_mul a := by
    cases a
    simp
  mul_one a := by
    cases a
    simp
  mul_assoc a b c := by
    cases a
    cases b
    cases c
    simp [mul_assoc, add_assoc]

end WeightLength

namespace FramedPath

variable {W G C : Type*} [Monoid W] [Monoid G] [AddMonoid C]
variable (ρ : CoordinateAction G C)

/-- Forgetting coordinate and frame data is a genuine monoid homomorphism for
observers that only ask for weight and raw operation length. -/
def eraseGeometryHom : FramedPath W G C ρ →* WeightLength W where
  toFun p := ⟨p.weight, p.length⟩
  map_one' := rfl
  map_mul' _ _ := rfl

end FramedPath

/-- Positive multiplicity BRC over framed path summaries.  Coefficients are
natural-number path multiplicities; the path key still retains the exact weight,
coordinate, frame and length data. -/
abbrev FramedNBRC (W G C : Type*) [Monoid W] [Monoid G] [AddMonoid C]
    (ρ : CoordinateAction G C) :=
  MonoidAlgebra ℕ (FramedPath W G C ρ)

/-- Boolean/result-support shadow of the positive multiplicity layer. -/
def booleanShadow {W G C : Type*} [Monoid W] [Monoid G] [AddMonoid C]
    {ρ : CoordinateAction G C} (f : FramedNBRC W G C ρ) : Set (FramedPath W G C ρ) :=
  {p | f p ≠ 0}

@[simp] theorem booleanShadow_zero {W G C : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] {ρ : CoordinateAction G C} :
    booleanShadow (0 : FramedNBRC W G C ρ) = ∅ := by
  ext p
  simp [booleanShadow]

/-- Positive recoalescence becomes literal support union.  This is the exact
additive bridge `N-BRC -> Boolean-BRC`; no multiplicity can be reconstructed in
the reverse direction. -/
theorem booleanShadow_add {W G C : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] {ρ : CoordinateAction G C}
    (f g : FramedNBRC W G C ρ) :
    booleanShadow (f + g) = booleanShadow f ∪ booleanShadow g := by
  ext p
  simp [booleanShadow]

/-- Frame-erased state used to state an exact information-loss obstruction. -/
structure FrameErased (W C : Type*) where
  weight : W
  coord : C
  length : Nat

/-- Drop only the frame while retaining the other declared path-summary fields. -/
def eraseFrame {W G C : Type*} [Monoid W] [Monoid G] [AddMonoid C]
    {ρ : CoordinateAction G C} (p : FramedPath W G C ρ) : FrameErased W C :=
  ⟨p.weight, p.coord, p.length⟩

/-- If two states collapse after frame erasure but a common right context separates
their future coordinates, frame erasure is not a future-safe BRC quotient.

This is a direct `NO_RESURRECTION` application: a lost frame cannot be inferred
later from the compressed state. -/
theorem eraseFrame_not_futureSafe {W G C : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] {ρ : CoordinateAction G C}
    {a b c : FramedPath W G C ρ}
    (hsame : eraseFrame a = eraseFrame b)
    (hdiff : (a * c).coord ≠ (b * c).coord) :
    ¬ Recovers eraseFrame (fun p : FramedPath W G C ρ => (p * c).coord) := by
  intro hrec
  exact hdiff (noResurrection hrec hsame)

/-- Integer-valued multiplicative two-coboundary.  BRC carries are instances of
this construction once a compression potential is fixed. -/
def twoCoboundary {M : Type*} [Monoid M] (potential : M → Int) (a b : M) : Int :=
  potential (a * b) - potential a - potential b

/-- Every two-coboundary satisfies the exact serial-composition cocycle law. -/
theorem twoCoboundary_cocycle {M : Type*} [Monoid M]
    (potential : M → Int) (a b c : M) :
    twoCoboundary potential a b + twoCoboundary potential (a * b) c =
      twoCoboundary potential b c + twoCoboundary potential a (b * c) := by
  unfold twoCoboundary
  rw [mul_assoc]
  ring

/-- Superadditivity is the exact extra hypothesis needed to turn an integer
coboundary into a nonnegative carry. -/
def MulSuperadditive {M : Type*} [Monoid M] (potential : M → Int) : Prop :=
  ∀ a b, potential a + potential b ≤ potential (a * b)

/-- A superadditive potential has nonnegative BRC carry. -/
theorem twoCoboundary_nonneg {M : Type*} [Monoid M]
    (potential : M → Int) (h : MulSuperadditive potential) (a b : M) :
    0 ≤ twoCoboundary potential a b := by
  have hab := h a b
  unfold twoCoboundary
  omega

/-- Coordinate-only potential on a framed path. -/
def coordinatePotential {W G C : Type*} [Monoid W] [Monoid G] [AddMonoid C]
    {ρ : CoordinateAction G C} (K : C → Int) (p : FramedPath W G C ρ) : Int :=
  K p.coord

/-- Coordinate carry produced by serial framed BRC composition. -/
def coordinateCarry {W G C : Type*} [Monoid W] [Monoid G] [AddMonoid C]
    {ρ : CoordinateAction G C} (K : C → Int)
    (a b : FramedPath W G C ρ) : Int :=
  twoCoboundary (coordinatePotential K) a b

@[simp] theorem coordinateCarry_eq {W G C : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] {ρ : CoordinateAction G C}
    (K : C → Int) (a b : FramedPath W G C ρ) :
    coordinateCarry K a b =
      K (a.coord + ρ.act a.frame b.coord) - K a.coord - K b.coord := by
  rfl

/-- The coordinate carry inherits exact parenthesization-independence from the
coboundary law. -/
theorem coordinateCarry_cocycle {W G C : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] {ρ : CoordinateAction G C}
    (K : C → Int) (a b c : FramedPath W G C ρ) :
    coordinateCarry K a b + coordinateCarry K (a * b) c =
      coordinateCarry K b c + coordinateCarry K a (b * c) := by
  exact twoCoboundary_cocycle (coordinatePotential K) a b c

/-- Coordinate potential is superadditive under acted concatenation.  Concrete
atlas extraction algorithms discharge this predicate by their own exact theorem. -/
def CoordinateSuperadditive {G C : Type*} [Monoid G] [AddMonoid C]
    (ρ : CoordinateAction G C) (K : C → Int) : Prop :=
  ∀ n m g, K n + K m ≤ K (n + ρ.act g m)

/-- An atlas-superadditive coordinate potential has nonnegative framed carry. -/
theorem coordinateCarry_nonneg {W G C : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] {ρ : CoordinateAction G C}
    (K : C → Int) (h : CoordinateSuperadditive ρ K)
    (a b : FramedPath W G C ρ) :
    0 ≤ coordinateCarry K a b := by
  have hab := h a.coord b.coord a.frame
  rw [coordinateCarry_eq]
  omega

end EnterpriseMath.BranchRecoalescence
