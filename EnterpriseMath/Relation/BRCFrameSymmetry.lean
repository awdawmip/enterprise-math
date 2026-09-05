import EnterpriseMath.Relation.FramedBranchRecoalescence
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

namespace FramedPath

variable {W G C : Type*} [Monoid W] [Group G] [AddMonoid C]
variable (ρ : CoordinateAction G C)

/-- Global change of frame. Coordinates transform by the declared action and
relative frames transform by conjugation. Weight and raw operation length are
unchanged. -/
def relabel (s : G) (p : FramedPath W G C ρ) : FramedPath W G C ρ :=
  ⟨p.weight, ρ.act s p.coord, s * p.frame * s⁻¹, p.length⟩

@[simp] theorem relabel_weight (s : G) (p : FramedPath W G C ρ) :
    (relabel ρ s p).weight = p.weight := rfl

@[simp] theorem relabel_coord (s : G) (p : FramedPath W G C ρ) :
    (relabel ρ s p).coord = ρ.act s p.coord := rfl

@[simp] theorem relabel_frame (s : G) (p : FramedPath W G C ρ) :
    (relabel ρ s p).frame = s * p.frame * s⁻¹ := rfl

@[simp] theorem relabel_length (s : G) (p : FramedPath W G C ρ) :
    (relabel ρ s p).length = p.length := rfl

@[simp] theorem relabel_one (s : G) :
    relabel ρ s (1 : FramedPath W G C ρ) = 1 := by
  ext
  · rfl
  · change ρ.act s 0 = 0
    exact ρ.act_zero s
  · change s * 1 * s⁻¹ = 1
    group
  · rfl

@[simp] theorem relabel_id (p : FramedPath W G C ρ) :
    relabel ρ (1 : G) p = p := by
  ext
  · rfl
  · change ρ.act 1 p.coord = p.coord
    exact ρ.one_act p.coord
  · change 1 * p.frame * (1 : G)⁻¹ = p.frame
    group
  · rfl

/-- Relabeling commutes with ordered BRC concatenation. This is the precise
algebraic form of global rotation covariance for the generic framed layer. -/
theorem relabel_mul (s : G) (a b : FramedPath W G C ρ) :
    relabel ρ s (a * b) = relabel ρ s a * relabel ρ s b := by
  ext
  · rfl
  · change
      ρ.act s (a.coord + ρ.act a.frame b.coord) =
        ρ.act s a.coord +
          ρ.act (s * a.frame * s⁻¹) (ρ.act s b.coord)
    rw [ρ.act_add]
    congr 1
    have hframe : (s * a.frame * s⁻¹) * s = s * a.frame := by
      group
    rw [← ρ.mul_act s a.frame b.coord, ← hframe,
      ρ.mul_act (s * a.frame * s⁻¹) s b.coord]
  · change
      s * (a.frame * b.frame) * s⁻¹ =
        (s * a.frame * s⁻¹) * (s * b.frame * s⁻¹)
    group
  · rfl

/-- A global frame change is a monoid endomorphism of framed path summaries. -/
def relabelHom (s : G) : FramedPath W G C ρ →* FramedPath W G C ρ where
  toFun := relabel ρ s
  map_one' := relabel_one ρ s
  map_mul' := relabel_mul ρ s

/-- Successive relabelings multiply in the same order as the frame action. -/
theorem relabel_relabel (s t : G) (p : FramedPath W G C ρ) :
    relabel ρ s (relabel ρ t p) = relabel ρ (s * t) p := by
  ext
  · rfl
  · change ρ.act s (ρ.act t p.coord) = ρ.act (s * t) p.coord
    exact (ρ.mul_act s t p.coord).symm
  · change s * (t * p.frame * t⁻¹) * s⁻¹ =
      (s * t) * p.frame * (s * t)⁻¹
    group
  · rfl

@[simp] theorem relabel_inv_relabel (s : G) (p : FramedPath W G C ρ) :
    relabel ρ s⁻¹ (relabel ρ s p) = p := by
  rw [relabel_relabel]
  have hs : s⁻¹ * s = (1 : G) := by
    group
  rw [hs]
  exact relabel_id ρ p

end FramedPath

/-- A coordinate potential is frame-invariant when global relabeling does not
change its value. -/
def CoordinateInvariant {G C : Type*} [Group G] [AddMonoid C]
    (ρ : CoordinateAction G C) (K : C → Int) : Prop :=
  ∀ g n, K (ρ.act g n) = K n

/-- A frame-invariant coordinate compression produces a rotation-invariant BRC
carry. This separates the universal cocycle law from the concrete choice of
compression potential (`K` extraction, common-depth extraction, or another
future observer-safe potential). -/
theorem coordinateCarry_relabel {W G C : Type*}
    [Monoid W] [Group G] [AddMonoid C] {ρ : CoordinateAction G C}
    (K : C → Int) (hK : CoordinateInvariant ρ K)
    (s : G) (a b : FramedPath W G C ρ) :
    coordinateCarry K (FramedPath.relabel ρ s a) (FramedPath.relabel ρ s b) =
      coordinateCarry K a b := by
  unfold coordinateCarry twoCoboundary coordinatePotential
  rw [← FramedPath.relabel_mul ρ s a b]
  change
    K (ρ.act s (a * b).coord) - K (ρ.act s a.coord) - K (ρ.act s b.coord) =
      K (a * b).coord - K a.coord - K b.coord
  rw [hK s (a * b).coord, hK s a.coord, hK s b.coord]

/-- Equivariance for a declared action pair. No group laws are needed for the
fixed-input obstruction below; callers may use a group action, a finite atlas
action, or another typed symmetry family. -/
def EquivariantUnder {G X Y : Type*}
    (actX : G → X → X) (actY : G → Y → Y) (f : X → Y) : Prop :=
  ∀ g x, f (actX g x) = actY g (f x)

/-- A point fixed by every declared transformation. -/
def FixedByAll {G X : Type*} (act : G → X → X) (x : X) : Prop :=
  ∀ g, act g x = x

/-- At a symmetric input, every equivariant single-valued selector must return a
symmetric output. -/
theorem equivariant_value_fixed {G X Y : Type*}
    (actX : G → X → X) (actY : G → Y → Y)
    (f : X → Y) (hf : EquivariantUnder actX actY f)
    (x : X) (hx : FixedByAll actX x) :
    FixedByAll actY (f x) := by
  intro g
  rw [← hf g x, hx g]

/-- If a symmetric input exists but the output candidate carrier has no global
fixed point, an equivariant deterministic selector cannot exist. In BRC this is
the generic formal reason a symmetric optimal branch fibre must remain
set-/branch-valued unless extra symmetry-breaking data are supplied. -/
theorem no_equivariant_single_choice {G X Y : Type*}
    (actX : G → X → X) (actY : G → Y → Y)
    (x : X) (hx : FixedByAll actX x)
    (hNoFixed : ∀ y, ¬ FixedByAll actY y) :
    ¬ ∃ f : X → Y, EquivariantUnder actX actY f := by
  rintro ⟨f, hf⟩
  exact hNoFixed (f x) (equivariant_value_fixed actX actY f hf x hx)

end EnterpriseMath.BranchRecoalescence
